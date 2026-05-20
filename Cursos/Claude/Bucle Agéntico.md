# El Bucle Agéntico de Claude (Agentic Loop)

Este documento forma parte de un curso de preparación para la certificación de Claude y explica en detalle cómo funciona el "bucle agéntico", el cual es el esqueleto de cualquier agente construido con Claude.

## Los 5 pasos del bucle agéntico

El flujo de trabajo de un agente se divide en cinco pasos fundamentales:

1. **Enviar mensaje a Claude**
   - Se realiza una llamada a la API que agrupa tres elementos:
     - el prompt del sistema (instrucciones de comportamiento),
     - el historial completo de la conversación,
     - y el último mensaje del usuario.

2. **Generación de respuesta**
   - Claude procesa la información y devuelve una respuesta.
   - La respuesta puede ser:
     - un mensaje de texto dirigido al usuario, o
     - una solicitud para usar una herramienta (`tool call`).

3. **El diamante de decisión (revisar `stop_reason`)**
   - Este es el paso más importante de todo el bucle.
   - El código debe revisar el campo `stop_reason` (motivo de parada) en la respuesta de la API, y no el texto generado por Claude.

   - Si el `stop_reason` es `end_turn`:
     - Claude ha finalizado su tarea.
     - Se envía la respuesta al usuario y el bucle se cierra.

   - Si el `stop_reason` es `tool_use`:
     - Claude necesita llamar a una función y el bucle continúa al siguiente paso.

4. **Ejecutar la herramienta**
   - El código del desarrollador (no Claude) debe ejecutar la función solicitada.
   - Debe pasar los argumentos especificados por la IA.

5. **Añadir el resultado al historial**
   - El resultado obtenido de la herramienta se añade al historial de la conversación como un mensaje de resultado de herramienta.
   - Una vez hecho esto, el bucle vuelve al paso 1 enviando este nuevo contexto actualizado a Claude.

```Mermaid
graph TD
    %% Paso 1
    P1[1. Enviar mensaje a Claude] -->|Prompt + Historial + Usuario| API(API de Anthropic)

    %% Paso 2
    API --> P2[2. Generación de respuesta]
    P2 --> P3{3. Revisar stop_reason}

    %% Paso 3 - Diamante de Decisión
    P3 -- end_turn --> Final[Enviar respuesta al usuario y cerrar bucle]
    P3 -- tool_use --> P4[4. Ejecutar la herramienta]

    %% Paso 4 y 5
    P4 -->|Código del desarrollador| P5[5. Añadir resultado al historial]

    %% Regreso al bucle
    P5 -->|Contexto actualizado| P1

    %% Estilos
    style P3 fill:#f1c40f,stroke:#f39c12,stroke-width:3px,color:#000
    style P1 fill:#bbf,stroke:#333
    style Final fill:#2ecc71,stroke:#27ae60,color:#fff
    style P4 fill:#e74c3c,stroke:#c0392b,color:#fff
```

## Modos de fallo comunes

La mayoría de los agentes se rompen en producción por un error fundamental: los desarrolladores intentan analizar el texto de respuesta de Claude (buscando palabras como "done" o "completado") en lugar de confiar en el campo `stop_reason`.

Esto provoca dos escenarios de fallo:

- **Fallo 1: Bucle infinito** (`loops forever`)
  - Al no leer el campo correcto, la condición de parada nunca se activa de forma limpia.
  - El código ejecuta la herramienta y la envía a Claude una y otra vez sin parar.
  - Esto consume los créditos de la API rápidamente y suele terminar en un error de tiempo de espera (`timeout`) o límite de contexto.

- **Fallo 2: Terminación prematura** (`terminates too early`)
  - El código asume incorrectamente que la respuesta de Claude está terminada y se la envía al usuario antes de ejecutar la herramienta necesaria.
  - Como resultado, el usuario recibe una respuesta a medias o el razonamiento interno de Claude (por ejemplo, "Voy a buscar esa información por ti") sin que la búsqueda se haya realizado realmente.

- **Fallo 3: No persiste el resultado de la herramienta**

### Pseudocódigo del loop correcto

```PYTHON
# El agente corre indefinidamente hasta que se rompe con break.
# Nunca termina por sí solo.
while True:

    # 📡 LLAMADA A LA API
    # Se envía el historial COMPLETO de mensajes a Claude.
    # La respuesta contiene texto y/o instrucciones de herramientas.
    response = call_claude(messages)

    # ✅ CASO 1: Claude terminó de razonar → respuesta final para el usuario
    # Este if es el "gatekeeper": decide cuándo la tarea está completa.
    if response.stop_reason == "end_turn":  # ← This is the gatekeeper
        send_to_user(response.text)
        break  # ← Clean exit — rompe el while True correctamente

    # 🔧 CASO 2: Claude necesita una herramienta para continuar
    # (buscar en la web, llamar una API, leer archivos, etc.)
    if response.stop_reason == "tool_use":
        # El orquestador (tu código) ejecuta la herramienta
        # usando el nombre y los parámetros que Claude indicó.
        result = run_tool(response.tool_name,
                          response.tool_input)

        # 📌 CLAVE DE MEMORIA: el resultado se agrega al historial.
        # Claude NO tiene estado propio; toda la memoria vive en `messages`.
        # Si no lo agregas, Claude no sabrá qué pasó.
        messages.append(tool_result(result))  # ← Result stays in context

        continue  # ← Back to Claude — regresa al inicio del loop
```

### Conceptos clave

#### Los dos `stop_reason` que debes dominar

| `stop_reason` | Significado                              | Acción                                         |
| ------------- | ---------------------------------------- | ---------------------------------------------- |
| `"end_turn"`  | Claude terminó de razonar                | Enviar respuesta al usuario → `break`          |
| `"tool_use"`  | Claude necesita ejecutar una herramienta | Ejecutar tool → agregar resultado → `continue` |

#### Memoria y contexto

Claude **no guarda estado** entre llamadas a la API. Toda la memoria del agente vive en el array `messages`. El flujo correcto es:

```PYTHON
call_claude(messages)
    → tool_use
        → run_tool()
            → messages.append(tool_result)  ← OBLIGATORIO
                → call_claude(messages)     ← ahora Claude "sabe" qué pasó
```

Si omites `messages.append(tool_result(...))`, Claude entra en la siguiente iteración sin saber el resultado de la herramienta.

---

## El crecimiento del contexto

Es importante tener en cuenta que a lo largo de este bucle, la conversación crece continuamente.

- Cada vez que Claude solicita usar una herramienta, se añade un bloque al historial.
- Cada vez que la herramienta devuelve un resultado, se añade otro bloque.

Este proceso va llenando gradualmente la ventana de contexto de Claude a medida que avanzan los turnos.

---

## Preguntas de repaso

1. ¿Qué sucede si no haces `break` cuando `stop_reason == "end_turn"`?
2. ¿Por qué es obligatorio hacer `messages.append(tool_result(result))`?
3. ¿Cuál es la diferencia entre `break` y `continue` en el loop?
4. ¿Puede Claude terminar el loop por sí solo sin un `break` explícito?
5. ¿Qué contiene `response.tool_name` y `response.tool_input`?

<details>
<summary>Ver respuestas</summary>

1. El loop corre infinitamente; Claude sigue llamándose sin enviar nunca la respuesta al usuario.
2. Porque Claude no tiene memoria propia; si el resultado no está en `messages`, en la siguiente iteración no sabrá qué devolvió la herramienta.
3. `break` termina el `while True`; `continue` salta al inicio de la siguiente iteración.
4. No. El loop es `while True`; solo termina con un `break` explícito en el código del orquestador.
5. `tool_name` es el nombre de la herramienta que Claude quiere usar; `tool_input` son los parámetros que le pasa.

</details>

---

_Fuente: DevCompass — CCA-F Domain 1, Stage 1 · The Agentic Loop Explained_
