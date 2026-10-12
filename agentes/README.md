# Agentes de IA

Este directorio recopila notas de estudio, disenos de arquitectura y analisis sobre sistemas agenticos autonomos basados en Modelos de Lenguaje Grande (LLMs).

---

## Indice del Modulo

| Tema / Documento | Descripcion | Documento |
| :--- | :--- | :--- |
| **Arquitectura y Evolucion** | Del diseno clasico (Cerebro + Tools + Memory + Planning) a los agentes modernos con MCP, Guardrails, Harness y Memoria Dual. | [Ver Documento](./arquitectura_y_evolucion.md) |

---

## Hoja de Ruta de Aprendizaje

1. **Fundamentos Clasicos:** El bucle agéntico basico, ReAct y descomposicion de tareas.
2. **Evolucion Arquitectonica:**
   * **Memoria:** Separacion de memoria de trabajo (corto plazo) y memoria episodica/semantica (largo plazo con bases vectoriales).
   * **Conectividad con MCP:** Integracion mediante Model Context Protocol para estandarizar acceso a herramientas y datos.
   * **Seguridad y Control:** Implementacion de Guardrails y evaluacion de seguridad.
   * **Entorno y Harness:** Maquinas de estado, circuit breakers y marcos de orquestacion.
