# Frameworks y Arquitecturas de IA

Este directorio recopila notas tecnicas, analisis de arquitectura y resumenes conceptuales sobre frameworks, modelos y metodologias enfocadas en razonamiento composicional, uso de herramientas (*tool use*), invocacion de APIs y sistemas agenticos basados en LLMs.

---

## Indice de Contenidos

| Framework / Proyecto | Enfoque Principal | Institucion / Origen | Documento |
| :--- | :--- | :--- | :--- |
| **LangChain** | Framework de desarrollo en codigo (Python / JS) para cadenas, RAG, agentes y despliegue en produccion. | LangChain Inc. (Open Source) | [Ver Documento](./langchain.md) |
| **Chameleon** | Razonamiento composicional, planificacion secuencial y aumento con herramientas modulares. | UCLA / Microsoft Research | [Ver Documento](./chameleon.md) |
| **Gorilla** | Invocacion estricta y precisa de APIs a gran escala mediante Retrieval-Aware Training. | UC Berkeley / Microsoft Research | [Ver Documento](./gorilla.md) |
| **GPT4Tools** | Adaptacion de LLMs de codigo abierto para control y uso de herramientas visuales/multimodales mediante LoRA. | Investigacion de codigo abierto | [Ver Documento](./gpt4tools.md) |
| **HuggingGPT** | LLM como controlador central (JARVIS) para conectar y coordinar modelos expertos de Hugging Face. | Universidad de Zhejiang / Microsoft | [Ver Documento](./hugginggpt.md) |

---

## Panorama General y Casos de Uso

* **Desarrollo Integral en Codigo:** Consulta [LangChain](./langchain.md) para construir aplicaciones completas combinando prompts, cadenas, RAG (cargadores de documentos y bases vectoriales) y agentes con observabilidad (LangSmith).
* **Orquestacion y Logica por Pasos:** Consulta [Chameleon](./chameleon.md) cuando analices como un LLM puede funcionar como planificador para descomponer tareas en programas y orquestar interpretes de Python, buscadores y modelos de vision.
* **Integracion con Servicios y Codigo:** Consulta [Gorilla](./gorilla.md) para comprender como entrenar y preparar LLMs para interactuar con miles de APIs reales sin alucinar firmas, parametros o sintaxis.
* **Agentes Multimodales Locales:** Consulta [GPT4Tools](./gpt4tools.md) para estudiar tecnicas de instruction tuning con adaptadores eficientes aplicados al manejo de herramientas de vision por computadora.
* **Coordinacion de Modelos de ML Heterogeneos:** Consulta [HuggingGPT](./hugginggpt.md) para ver la arquitectura de 4 etapas (planificacion, seleccion de modelo, ejecucion y respuesta) usando a un LLM como director de orquesta sobre el catalogo de Hugging Face.
