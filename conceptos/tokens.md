# Tokens y Tokenización

*Nota de estudio original: 24 de junio de 2025*

Los **tokens** son los **bloques de construcción más pequeños** del lenguaje que el modelo procesa.

Piensa en ellos como las "piezas" en las que se divide el texto (tanto lo que le das al modelo como lo que el modelo genera) para que la IA pueda "entenderlo" y "trabajar con ello".

---

## ¿Qué son exactamente los tokens?

* **No siempre son palabras completas:** A veces, un token es una palabra completa (`"perro"`, `"casa"`). Pero otras veces, puede ser una **parte de una palabra** (`"pro-"`, `"grama-"`, `"-ción"`), un **signo de puntuación** (`"."`, `","`, `"?"`), o incluso **espacios en blanco**.
* **Representación numérica:** Para una IA, los tokens son convertidos en números (vectores) que el modelo puede manipular matemáticamente. Es su forma de "leer".
* **Vocabulario limitado:** Cada LLM tiene un "vocabulario" predefinido de tokens que ha aprendido durante su entrenamiento. Esto le permite manejar eficientemente una vasta cantidad de texto, incluso palabras que nunca ha visto directamente, dividiéndolas en sus tokens constituyentes.

---

## ¿Por qué se usan los tokens?

1. **Manejo de la complejidad:** Es más fácil para un modelo procesar unidades más pequeñas y consistentes que palabras enteras, que pueden tener una variedad infinita.
2. **Eficiencia:** Trabajar con tokens permite que los modelos sean más eficientes computacionalmente.
3. **Manejo de palabras raras o nuevas:** Si el modelo encuentra una palabra que nunca ha visto, en lugar de no saber qué hacer, la puede dividir en sub-palabras o caracteres que sí reconoce como tokens. Por ejemplo, `"desoxirribonucleico"` podría dividirse en varios tokens más pequeños (`des-`, `oxirri-`, `bo-`, `nu-`, `cleico`).
4. **Límite de contexto:** Cuando un LLM te responde, tiene un "límite de tokens" (o "ventana de contexto"). Esto significa que solo puede "recordar" y procesar una cierta cantidad de tokens de la conversación o del texto de entrada a la vez. Si la conversación es muy larga, las partes más antiguas pueden "salir" de esta ventana.

---

## Ejemplos de Tokenización

* **Oración:** `"Hola, ¿cómo estás?"`
  * **Tokens (ejemplo simplificado):** `"Hola"`, `","`, `"¿"`, `"cómo"`, `" "`, `"estás"`, `"?"` (Un espacio también puede ser un token o parte de uno).

* **Oración:** `"Un Transformer es genial."`
  * **Tokens (ejemplo):** `"Un"`, `" "`, `"Trans"`, `"former"`, `" "`, `"es"`, `" "`, `"genial"`, `"."` (Observa cómo `"Transformer"` se divide en dos para este ejemplo hipotético, mostrando sub-palabras).

---

## En Resumen

Los tokens son la forma en que los modelos de lenguaje descomponen y recomponen el lenguaje humano para poder procesarlo a nivel computacional. Son la unidad fundamental de su comunicación y entendimiento.
