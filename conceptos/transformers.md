# Transformers

*Nota de estudio original: 24 de junio de 2025*

Los Transformers son un tipo de **arquitectura de red neuronal** (un modelo matemático-computacional que simula cómo aprenden las neuronas biológicas) que fue introducida por Google en 2017. Fueron diseñados específicamente para manejar **datos secuenciales**, y el lenguaje es un tipo de dato secuencial (las palabras van una detrás de otra).

---

## ¿Qué los hace revolucionarios? (El "Mecanismo de Atención")

Antes de los Transformers, los modelos de NLP procesaban las palabras de una oración de forma secuencial, una por una, lo que hacía difícil que recordaran y relacionaran información de partes muy distantes de la oración (o del texto). Era como leer un libro línea por línea sin poder saltar fácilmente a lo que dijiste en el capítulo anterior o en la primera frase del párrafo.

Los Transformers introdujeron un concepto fundamental llamado **"mecanismo de atención" (attention mechanism)**.

### ¿Cómo funciona la atención?

Imagina que estás leyendo una oración como:
> *"El **banco** del río es un lugar tranquilo para sentarse, pero necesito ir al **banco** para sacar dinero."*

* Para entender el significado de la segunda palabra "banco", un Transformer no solo mira las palabras inmediatamente anteriores o posteriores. En cambio, puede **"prestar atención"** a todas las demás palabras de la oración al mismo tiempo, y asignar un "peso" o importancia a las palabras más relevantes para el significado de "banco" en ese contexto. En este ejemplo, el segundo "banco" se relaciona más con "sacar dinero" que con "río".
* Este mecanismo les permite comprender el **contexto y las relaciones a largo plazo** entre palabras en una oración o incluso en documentos muy largos, sin importar qué tan separadas estén las palabras.

---

## ¿Por qué son tan importantes?

1. **Paralelización:** A diferencia de arquitecturas anteriores que procesaban secuencias de forma lineal, los Transformers pueden procesar partes de la secuencia en paralelo, lo que los hace **mucho más rápidos y eficientes** para entrenar con cantidades masivas de datos (como todo internet).
2. **Comprensión contextual:** Su mecanismo de atención les permite captar un entendimiento mucho más profundo del contexto y las relaciones en el lenguaje.
3. **Fundamento de los LLMs:** La mayoría de los modelos de lenguaje grandes y avanzados que existen hoy en día (como GPT-3, GPT-4, BERT, LaMDA y Gemini) están **construidos sobre la arquitectura Transformer**. Sin los Transformers, los LLMs como los conocemos hoy no serían posibles.

---

## En Resumen

Los Transformers son una arquitectura de IA que, gracias a su mecanismo de atención, ha revolucionado la forma en que las máquinas entienden y generan el lenguaje, permitiendo el desarrollo de modelos de lenguaje mucho más potentes y conscientes del contexto.
