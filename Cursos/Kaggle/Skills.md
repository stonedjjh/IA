# Agent Skills

Agent Skills (o habilidades de agente) son paquetes estructurados y portátiles de conocimiento procedimental que equipan a un agente de IA con el contexto y el "saber cómo" de una empresa.

## Características

- **Portabilidad**: Las habilidades de agente están diseñadas para ser portátiles, lo que permite a los agentes de IA transferir fácilmente su conocimiento y experiencia de una empresa a otra.

- **Son la "memoria procedimental" de la IA**: Históricamente, los modelos de lenguaje eran buenos recordando hechos (memoria semántica) o el historial del chat (memoria episódica), pero carecían de una forma fiable de recordar cómo hacer tareas complejas paso a paso. Las Skills funcionan como el primer mecanismo creíble de memoria procedimental para estos sistemas.

- **Convierten a un generalista en especialista bajo demanda**: En lugar de crear y mantener una arquitectura enorme con cientos de sub-agentes diferentes para cada tarea, las Skills permiten que un único agente de propósito general asuma temporalmente roles hiper-especializados según se necesite.

- **Son ligeras y estandarizadas**: A nivel de código, una Skill es simplemente una carpeta que contiene un archivo obligatorio llamado `SKILL.md` (donde van los metadatos y las instrucciones) junto a carpetas opcionales que guardan scripts ejecutables, material de referencia y plantillas. Esto las hace sumamente portátiles entre diferentes plataformas de desarrollo.

- **Resuelven la sobrecarga de contexto**: Operan bajo un principio llamado "revelación progresiva" (progressive disclosure). En lugar de inyectar todas las reglas de la empresa en el cerebro del agente a la vez (lo que satura su memoria y degrada su rendimiento), el agente solo lee una etiqueta ligera de todas las Skills disponibles al inicio. Solo cuando el agente determina que necesita una habilidad específica para resolver tu problema, carga las instrucciones completas en su memoria dinámica.

## Cómo funciona

Inicialmente, el modelo solo se expone a un "menú" ligero de metadatos. Carga el conocimiento procedimental pesado (instrucciones y secuencias de comandos) solo cuando la intención del usuario coincide específicamente con una habilidad. Esto garantiza que un desarrollador que solicita refactorizar el middleware de autenticación obtenga el contexto de seguridad sin cargar canalizaciones de CSS no relacionadas, lo que mantiene el contexto eficiente, rápido y rentable.

## Crear una Skill de agente de IA

1. Define el propósito principal.
   - Describe claramente qué problema resuelve la Skill.
   - Sé específico: por ejemplo, "gestionar tickets de soporte" en lugar de "ayudar al cliente".

2. Escribe la documentación en `SKILL.md`.
   - Incluye metadatos, instrucciones y ejemplos de uso.
   - Mantén un lenguaje directo y orientado a acciones.

3. Organiza el contenido de soporte.
   - Agrega carpetas opcionales para scripts, plantillas, datos de referencia y ejemplos.
   - Mantén solo lo necesario: la Skill debe ser ligera.

4. Prueba la Skill con casos reales.
   - Valida que el agente active la Skill solo cuando el contexto sea relevante.
   - Ajusta las instrucciones si el agente interpreta mal el alcance.

## Consideraciones clave

- Foco en la intención, no en el texto exacto.
- Evita instrucciones demasiado genéricas o demasiado detalladas.
- Piensa en la Skill como una función especializada, no como un manual completo.
- Asegúrate de que la Skill sea reutilizable, pero no tan amplia que abarque demasiadas tareas distintas.

## ¿Qué tan largo debe ser el archivo?

- No existe un tamaño perfecto, pero la regla general es: suficientemente detallado para que el agente actúe bien, sin convertirse en un libro.
- Un `SKILL.md` efectivo suele tener entre 300 y 1200 palabras.
- Si necesitas más contenido, separa la información en archivos auxiliares o referencias externas.
- Prioriza claridad y ejemplos prácticos sobre abundancia de texto.

## Recomendaciones y buenas prácticas al definir una Skill

- Usa títulos y secciones claras dentro de `SKILL.md`.
- Define entradas y salidas esperadas cuando sea posible.
- Incluye ejemplos de conversación o prompts que el agente debe manejar.
- Añade reglas de exclusión: qué la Skill no debe hacer.
- Especifica limitaciones y suposiciones: contexto disponible, permisos, datos de entrada.
- Usa un estilo consistente entre Skills para facilitar su mantenimiento.
- Revisa y refactoriza regularmente: una Skill viva mejora con el uso.

## Cómo limitar el alcance de una Skill

- Describe el dominio con precisión.
  - Por ejemplo, "gestion de solicitudes de vacaciones" en lugar de "gestionar recursos humanos".
- Define explícitamente lo que no abarca.
  - "No incluye aprobación de gastos"; "No maneja cambios de nómina".
- Usa ejemplos negativos para guiar al agente.
  - Si el prompt del usuario cae fuera del alcance, que devuelva una respuesta de redirección o pida más datos.
- Crea Skills independientes para áreas diferentes.
  - Es mejor tener varias Skills pequeñas y especializadas que una sola Skill enorme.
- Controla la activación.
  - Emplea metadatos y etiquetas claras para que el agente solo cargue la Skill cuando la intención coincide con la tarea.

## Ejemplo práctico: Skill para gestión de solicitudes de vacaciones

A continuación hay un ejemplo de `SKILL.md` para una Skill que ayuda a un agente a gestionar solicitudes de vacaciones. Puedes usar este esquema como plantilla para otras Skills.

```markdown
# Skill: Gestión de solicitudes de vacaciones

## Descripción

Ayuda al agente a manejar solicitudes de vacaciones, verificar el saldo disponible, validar las fechas y responder si la solicitud necesita aprobación adicional.

## Metadatos

- nombre: gestión-vacaciones
- tags: [recursos-humanos, vacaciones, solicitudes]
- nivel: básico

## Objetivo

Actuar solo cuando el usuario quiere:

- solicitar días libres
- verificar el saldo de vacaciones
- conocer el estado de una solicitud existente

## Instrucciones para el agente

1. Identifica si el usuario está hablando de vacaciones o permiso.
2. Si solicita vacaciones, pide:
   - fechas de inicio y fin
   - tipo de permiso (vacaciones, compensatorio, médico)
   - motivo breve si es necesario.
3. Verifica el saldo disponible con el sistema de recursos humanos.
4. Si faltan datos, solicita únicamente la información necesaria.
5. Si la solicitud está completa, genera un resumen y una respuesta clara.
6. No apruebes permisos, solo prepara la solicitud y sugiere los siguientes pasos.

## Ejemplos de uso

- "Quiero pedir vacaciones del 10 al 14 de julio."
- "¿Cuántos días de vacaciones me quedan este año?"
- "Necesito permiso por un día para una cita médica."

## Fuera de alcance

- No aprueba vacaciones.
- No cambia datos de nómina.
- No tramita reembolsos o gastos.

## Comportamiento esperado

- Si el usuario pregunta por el saldo, responde con el estado del saldo disponible.
- Si el usuario solicita fechas, pide confirmación y datos faltantes.
- Si el asunto está fuera de vacaciones, sugiere derivar la consulta a otra Skill.
```

### Cómo usar este ejemplo

1. Copia el contenido en una carpeta propia de Skill, por ejemplo: `skills/gestion-vacaciones/SKILL.md`.
2. Ajusta las secciones de metadatos, ejemplos y alcance a tu caso específico.
3. Añade plantillas o scripts adicionales si necesitas validar fechas, consultar APIs o cargar datos.
4. Prueba con prompts reales y refina las instrucciones según el comportamiento del agente.

Este ejemplo es práctico porque muestra un flujo completo: propósito, instrucciones, ejemplos, límite de alcance y expectativas de uso. Puedes adaptarlo a otros dominios como soporte técnico, facturación o onboarding interno.
