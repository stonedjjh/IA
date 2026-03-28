# Resumen

## Tipos de Agentes de IA

Los agentes se clasifican en funcion de su nivel de inteligencia, sus procesos de toma de decisiones y como interactuan con su entorno.

1. **Simple Reflex**(Reacciona): Es el agente más sencillo; se guía por reglas establecidas. Se puede comparar con una bombilla que se enciende por aplausos: el [disparador](../Glosario.md#disparador) es el aplauso y, según su estado, se encenderá o apagará. Son recomendados para [entornos](../Glosario.md#entorno) estáticos; sin embargo, en entornos dinámicos pueden repetir el mismo error al no almacenar información.

2. **Model-Based Reflex** (Recuerda): Es una versión mejorada del agente de reflejo simple. Incluye un modelo interno del entorno que se almacena en un componente de estado; con esto, se puede realizar un seguimiento de cómo las acciones afectan al entorno. No se limita a reaccionar a lo que percibe, sino que infiere y recuerda el entorno aunque no lo esté percibiendo en el momento.

3. **Goal-Based Agent** (Apunta): Este tipo de agente no solo se guía por reglas, sino que también tiene objetivos específicos que busca alcanzar. Toma decisiones basadas en la evaluación de las posibles acciones y sus consecuencias para lograr las metas propuestas.

Utility-Based Agent (Evalúa): Este agente va más allá de simplemente alcanzar objetivos; también evalúa la utilidad o el valor de los diferentes estados del entorno para tomar decisiones. Se busca maximizar la utilidad a largo plazo, considerando las consecuencias de las acciones realizadas.

Learning Agent (Mejora): Este agente tiene la capacidad de aprender de la experiencia y mejorar su rendimiento con el tiempo. Utiliza algoritmos de aprendizaje automático para ajustar su comportamiento en función de los datos que se recopilan del entorno.

[Fuente](https://www.youtube.com/watch?v=fXizBc03D7E)

## Que es RAG

**RAG (Retrieval-Augmented Generation)** o Generación Aumentada por Recuperación, es una arquitectura diseñada para que los modelos de lenguaje (**LLM**) sean más precisos, fiables y estén permanentemente actualizados.

**Problemas que resuelve:**

1. **Falta de fuentes**: Los modelos estándar suelen generar respuestas sin citar el origen de la información.

2. **Desactualización**: El conocimiento del modelo está limitado a su fecha de entrenamiento (Knowledge Cutoff).

Con la recuperación aumentada, se busca que el LLM no solo se guíe por sus datos internos, sino que consulte un repositorio de contenido dinámico. Este puede ser abierto (Internet) o cerrado (una colección privada de documentos corporativos o técnicos).

**Ejemplo de Aplicación Real:**

Para comprender la utilidad de RAG, se puede observar el siguiente escenario de actualidad:

Consulta: "¿Ha sido impactado un F-35 en combate?"

Respuesta de un LLM estándar: Basado en su entrenamiento previo, el modelo probablemente respondería que no existen registros oficiales de derribos por fuego enemigo.

Respuesta de un LLM con RAG: Al realizar una búsqueda en tiempo real, el sistema detectaría reportes recientes (como las declaraciones de Irán del 19/03/2026 asegurando el impacto contra una unidad).

Resultado: El sistema no solo entrega la información actualizada, sino que es capaz de citar las fuentes de prensa o comunicados oficiales de donde obtuvo el dato, eliminando la alucinación.

[Fuente](https://www.youtube.com/watch?v=T-D1OfcDW1M)

## LangChain

Es un framework de orquestación de código abierto para el desarrollo de aplicaciones que utilizan modelos de lenguaje de gran tamaño (LLM).

**Componentes:**

- **Abstracciones:** Representan pasos y conceptos comunes para trabajar con LLM, los cuales pueden ser encadenados para la creación de aplicaciones.

- **LLM:** Modelos de lenguaje que actúan como el motor de razonamiento de la aplicación.

- **Prompts:** Plantillas que guían la generación de texto de manera estructurada.

- **Chains (Cadenas):** Son el núcleo de trabajo de LangChain; se encargan de enlazar los LLM con otros componentes de forma secuencial.

- **Memory (Memoria):** Permite a las aplicaciones recordar información y contexto a lo largo del tiempo o de una conversación.

- **Indexes (Índices):** Conjuntos de datos que no están incluidos en el modelo de entrenamiento original del LLM.

  > [!NOTE]
  > Anotación personal: ¿Esto no es [RAG](#que-es-rag)?
  - **Doc Loader:** Herramientas para importar datos desde fuentes externas al LLM.
  - **Bases de Datos Vectoriales:** Sistemas de almacenamiento optimizados para la búsqueda semántica.
  - **Text Splitters:** Dividen el texto en fragmentos pequeños con significado semántico, los cuales pueden ser procesados combinando diversos parámetros y métodos.

- **Agents (Agentes):** Entidades que utilizan un LLM para decidir qué acciones tomar y en qué orden, utilizando herramientas externas.

[Fuente](https://www.youtube.com/watch?v=1bUy-1hGZpI)

## ¿Qué son los Modelos de Razonamiento a Gran Escala (LRM)? IA más inteligente más allá de los LLM

Se diferencian de los LLM en que estos modelos elaboran respuestas más analíticas. Mientras que los LLM se basan primordialmente en predicciones estadísticas para generar la siguiente palabra, los LRM integran procesos de razonamiento lógico para resolver problemas.
