# Habilidades de agentes y Antigravity

En el ecosistema de Antigravity, las **habilidades** actúan como módulos de entrenamiento especializados que cierran la brecha entre los modelos generalistas y tu contexto específico. Permiten que el agente "equipe" un conjunto definido de instrucciones y protocolos, como estándares de migración de bases de datos o verificaciones de seguridad, solo cuando se solicita una tarea pertinente. Cuando se cargan de forma dinámica estos protocolos de ejecución, las Skills transforman de manera eficaz la IA de un programador genérico en un especialista que se adhiere rigurosamente a las prácticas recomendadas y los estándares de seguridad codificados de una organización.

## ¿Qué es una habilidad en Antigravity?

En el contexto de Google Antigravity, una habilidad es un paquete basado en directorios que contiene un archivo de definición (`SKILL.md`) y recursos complementarios opcionales (secuencias de comandos, referencias, plantillas).

Es un mecanismo para la extensión de capacidades a pedido.

- **A pedido**: A diferencia de una instrucción del sistema (que siempre se carga), una habilidad solo se carga en el contexto del agente cuando este determina que es pertinente para la solicitud actual del usuario. Esto optimiza la ventana de contexto y evita que el agente se distraiga con instrucciones irrelevantes. En proyectos grandes con docenas de herramientas, esta carga selectiva es fundamental para el rendimiento y la precisión del razonamiento.

- **Extensión de capacidad**: Las habilidades pueden hacer más que solo dar instrucciones; también pueden ejecutarlas. Al incluir secuencias de comandos de Python o Bash, una habilidad puede darle al agente la capacidad de realizar acciones complejas de varios pasos en la máquina local o en redes externas sin que el usuario tenga que ejecutar comandos de forma manual. Esto transforma al agente de un generador de texto en un usuario de herramientas.

### Habilidades en comparación con el ecosistema (herramientas, reglas y flujos de trabajo)

Si bien el Protocolo de contexto del modelo (MCP) funciona como las "manos" del agente, ya que proporciona conexiones persistentes y de alta capacidad a sistemas externos como GitHub o PostgreSQL, las habilidades actúan como el "cerebro" que las dirige.

MCP controla la infraestructura con estado, mientras que las habilidades son definiciones de tareas efímeras y ligeras que empaquetan la metodología para usar esas herramientas. Este enfoque sin servidores permite que los agentes ejecuten tareas ad hoc (como generar registros de cambios o migraciones) sin la sobrecarga operativa de ejecutar procesos persistentes, cargar el contexto solo cuando la tarea está activa y liberarlo inmediatamente después.

Las habilidades se **activan por el agente**: El modelo detecta automáticamente la intención del usuario y se equipa de forma dinámica con la experiencia específica requerida. Esta arquitectura permite una potente capacidad de composición. Por ejemplo, una regla global puede exigir el uso de una habilidad de "migración segura" durante los cambios en la base de datos, o un solo flujo de trabajo puede coordinar varias habilidades para crear una canalización de implementación sólida.

## Cómo crear habilidades

Para crear una habilidad en Antigravity, se debe seguir una estructura de directorio y un formato de archivo específicos. Esta estandarización garantiza que las habilidades sean portátiles y que el agente pueda analizarlas y ejecutarlas de manera confiable. El diseño es intencionalmente simple y se basa en formatos ampliamente conocidos, como Markdown y YAML, lo que reduce la barrera de entrada para los desarrolladores que desean extender las capacidades de su IDE.

### Estructura de directorios

Un directorio de Skill típico se ve de la siguiente manera:

```bash
my-skill/
├── SKILL.md # The definition file
├── scripts/ # [Optional] Python, Bash, or Node scripts
     ├── run.py
     └── util.sh
├── references/ # [Optional] Documentation or templates
     └── api-docs.md
└── assets/ # [Optional] Static assets (images, logos)
```

Esta estructura separa las preocupaciones de manera eficaz. La lógica (`scripts`) se separa de la instrucción (`SKILL.md`) y el conocimiento (`references`), lo que refleja las prácticas estándar de ingeniería de software.

#### El archivo de definición SKILL.md

El archivo `SKILL.md` es el cerebro de la skill. Le indica al agente qué es la habilidad, cuándo usarla y cómo ejecutarla.

Está compuesto por dos partes:

- Frontmatter de YAML

- Cuerpo en Markdown.

##### YAML Frontmatter

Esta es la capa de metadatos. Es la única parte de la habilidad que indexa el router de alto nivel del agente. Cuando un usuario envía una instrucción, el agente la compara semánticamente con los campos de descripción de todas las habilidades disponibles.

```yaml
---

name: database-inspector
description: Use this skill when the user asks to query the database, check table schemas, or inspect user data in the local PostgreSQL instance.

# En español

name: database-inspector
description: Usa esta habilidad cuando el usuario solicite hacer consultas a la base de datos, verificar esquemas de tablas o inspeccionar datos de usuarios en la instancia local de PostgreSQL.
---
```

**Campos clave:**

- **name**: No es obligatorio. Debe ser único dentro del alcance. Se permiten letras en minúscula y guiones (p.ej., postgres-query, pr-reviewer). Si no se proporciona, se usará el nombre del directorio de forma predeterminada.

- **description**: Este campo es obligatorio y el más importante. Funciona como la "frase de activación". Debe ser lo suficientemente descriptiva para que el LLM reconozca la relevancia semántica. Una descripción vaga, como "Herramientas de base de datos", no es suficiente. Una descripción precisa, como "Ejecuta consultas de SQL de solo lectura en la base de datos local de PostgreSQL para recuperar datos de usuarios o transacciones. Use this for debugging data states" garantiza que la skill se detecte correctamente.

##### El cuerpo de Markdown

El cuerpo contiene las instrucciones. Esto es la "ingeniería de instrucciones" que se persiste en un archivo. Cuando se activa la skill, este contenido se inserta en la ventana de contexto del agente.

El cuerpo debe incluir lo siguiente:

1. Objetivo: Una declaración clara de lo que logra la habilidad.

2. Instrucciones: Lógica paso a paso.

3. Ejemplos: Son ejemplos de pocas tomas de entradas y salidas para guiar el rendimiento del modelo.

4. Restricciones: Reglas de "no hacer" (p.ej., "No ejecutes consultas DELETE").

**Ejemplo de cuerpo de SKILL.md:**

```markdown
Database Inspector

Goal
To safely query the local database and provide insights on the current data state.

Instructions

- Analyze the user's natural language request to understand the data need.
- Formulate a valid SQL query.
- CRITICAL: Only SELECT statements are allowed.
- Use the script scripts/query_runner.py to execute the SQL.
- Command: python scripts/query_runner.py "SELECT \* FROM..."
- Present the results in a Markdown table.

Constraints

- Never output raw user passwords or API keys.
- If the query returns > 50 rows, summarize the data instead of listing it all.
```

En español

```markdown
Database Inspector

Goal
Seguir de manera segura consultas a la base de datos local y proporcionar información sobre el estado actual de los datos.

Instructions

- Analizar la solicitud en lenguaje natural del usuario para comprender la necesidad de datos.
- Formular una consulta SQL válida.
- CRÍTICO: Solo se permiten sentencias SELECT.
- Usar el script scripts/query_runner.py para ejecutar el SQL.
- Comando: python scripts/query_runner.py "SELECT \* FROM..."
- Presentar los resultados en una tabla Markdown.

Constraints

- Nunca mostrar contraseñas de usuario en bruto ni claves de API.
- Si la consulta devuelve más de 50 filas, resumir los datos en lugar de listarlos todos.
```

### Integración de secuencias de comandos

Una de las funciones más potentes de las Skills es la capacidad de delegar la ejecución en secuencias de comandos. Esto permite que el agente realice acciones que son difíciles o imposibles de hacer directamente para un LLM (como la ejecución binaria, el cálculo matemático complejo o la interacción con sistemas heredados).

Las secuencias de comandos se colocan en el subdirectorio `scripts`/. El `SKILL.md` hace referencia a ellos por ruta de acceso relativa.

## Habilidades de creación

El objetivo de esta sección es desarrollar habilidades que se integren en Antigravity y muestren progresivamente varias funciones, como recursos, secuencias de comandos, etcétera.

Puedes descargar las Skills desde el repo de [GitHub aquí:](https://github.com/rominirani/antigravity-skills).

Antes de comprender cómo se desarrollaron cada una de estas habilidades, veamos cómo las configuramos y las ponemos a disposición en el paquete de productos de Antigravity. Las siguientes carpetas son aplicables en el momento de la publicación de este lab.

### Usa Antigravity o la CLI de Antigravity

Las habilidades se pueden definir en dos permisos, lo que permite habilidades específicas del proyecto y del usuario, es decir, habilidades globales:

- Alcance global (`~/.gemini/config/skills/`): Disponible en todos los productos (Antigravity, IDE de Antigravity, CLI de Antigravity) y proyectos de Antigravity. Estas habilidades están disponibles en todos los proyectos de la máquina del usuario. Esto es adecuado para utilidades generales, como "Formatear JSON", "Generar UUID", "Revisar el estilo de código" o la integración con herramientas de productividad personal.

- Alcance del proyecto o lugar de trabajo (`<project-root>/.agents/skills/`): Esto haría que la habilidad esté disponible solo dentro de un proyecto específico. Esto es ideal para secuencias de comandos específicas del proyecto, como la implementación en un entorno específico, la administración de bases de datos para esa app o la generación de código estándar para un framework propietario.

### Instala las Skills en Antigravity o en la CLI de Antigravity

Para este instructivo, solo necesitamos seguir los siguientes pasos (también puedes hacerlo a tu manera):

**Paso 1**: Haz un git clone de https://github.com/rominirani/antigravity-skills

**Paso 2**: Ahora, según si usas Antigravity o la CLI de Antigravity, puedes navegar a la carpeta antigravity-skills/skills_tutorial.

**Paso 3**: Verás un conjunto de habilidades agrupadas en sus respectivas carpetas. Copia las siguientes 4 carpetas:

- `git-commit-formatter`
- `license-header-adder`
- `database-schema-validator`
- `json-to-pydantic`

en la carpeta de habilidades segmentadas para el producto (alcance del proyecto o alcance global).

**Paso 4**: Si usas **Antigravity** o **Antigravity CLI** , cópialo en <project-root>/.agents/skills/ (alcance del proyecto).

Si ya lanzaste Antigravity, puedes hacer una pregunta simple, como "¿Qué habilidades están disponibles?", y obtendrás la misma respuesta. Puedes ver las 4 habilidades que se enumeran allí. También es posible que tengas habilidades adicionales si las instalaste en tu entorno.

Del mismo modo, si usas la CLI de Antigravity, puedes ejecutar el siguiente comando /skills y debería mostrar las 4 habilidades. A continuación, se muestra un ejemplo:

Ahora que sabemos cómo configurar las habilidades, analicemos cada una de ellas y comprendamos cómo se construyeron. También puedes usar estas plantillas para crear tus propias habilidades.

### Nivel 1 : El router básico ( git-commit-formatter)

Consideremos esto como el "Hola mundo" de las Skills.

Los desarrolladores suelen escribir mensajes de confirmación vagos, p.ej., "wip", "fix bug", "updates". Aplicar "Conventional Commits" de forma manual es tedioso y, a menudo, se olvida. Implementemos una habilidad que aplique la especificación de Conventional Commits. Con solo indicarle al agente las reglas, le permitimos actuar como ejecutor.

```bash
git-commit-formatter/
└── SKILL.md  (Instructions only)
```

A continuación, se muestra el archivo SKILL.md:

```markdown
---
name: git-commit-formatter
description: Formats git commit messages according to Conventional Commits specification. Use this when the user asks to commit changes or write a commit message.
---

Git Commit Formatter Skill

When writing a git commit message, you MUST follow the Conventional Commits specification.

Format
`<type>[optional scope]: <description>`

Allowed Types

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Changes that do not affect the meaning of the code (white-space, formatting, etc)
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **perf**: A code change that improves performance
- **test**: Adding missing tests or correcting existing tests
- **chore**: Changes to the build process or auxiliary tools and libraries such as documentation generation

Instructions

1. Analyze the changes to determine the primary `type`.
2. Identify the `scope` if applicable (e.g., specific component or file).
3. Write a concise `description` in an imperative mood (e.g., "add feature" not "added feature").
4. If there are breaking changes, add a footer starting with `BREAKING CHANGE:`.

Example
`feat(auth): implement login with google`
```

En español

```markdown
---
name: git-commit-formatter
description: Da formato a los mensajes de commit de git de acuerdo con la especificación de Conventional Commits. Usa esta habilidad cuando el usuario solicite hacer commit de los cambios o escribir un mensaje de commit.
---

Git Commit Formatter Skill

Al escribir un mensaje de commit de git, DEBES seguir la especificación de Conventional Commits.

Format
`<type>[optional scope]: <description>`

Allowed Types

- **feat**: Una nueva funcionalidad
- **fix**: Una corrección de errores (bug fix)
- **docs**: Cambios únicamente en la documentación
- **style**: Cambios que no afectan el significado del código (espacios en blanco, formateo, etc.)
- **refactor**: Un cambio de código que no corrige un error ni añade una funcionalidad
- **perf**: Un cambio de código que mejora el rendimiento
- **test**: Añadir pruebas que faltan o corregir pruebas existentes
- **chore**: Cambios en el proceso de construcción o herramientas auxiliares y librerías, como la generación de documentación

Instructions

1. Analizar los cambios para determinar el `type` principal.
2. Identificar el `scope` si corresponde (por ejemplo, un componente o archivo específico).
3. Escribir una `description` concisa en modo imperativo (por ejemplo, "add feature" y no "added feature").
4. Si hay cambios disruptivos (breaking changes), añadir un pie de página que comience con `BREAKING CHANGE:`.

Example
`feat(auth): implement login with google`
```

#### Cómo ejecutar este ejemplo en Antigravity

En los siguientes pasos, se supone que tienes Git disponible en tu máquina local y que está configurado correctamente.

Si ya iniciaste Antigravity o la CLI de Antigravity, sigue estos pasos:

- **Paso 1: Configura un repositorio de Git de prueba**

Pídele al agente que configure un directorio limpio y aislado para probar las operaciones de Git.

Tus instrucciones:

`Create a folder named git_test in the workspace, initialize a git repository inside it, and create an initial file auth.py with def login(): pass. Stage this file and make an initial commit.`

En español

`Crea una carpeta llamada git_test en el espacio de trabajo, inicializa un repositorio de git dentro de ella y crea un archivo inicial auth.py con def login(): pass. Añade este archivo al área de preparación (stage) y realiza un commit inicial.`

El agente creará el directorio, inicializará el repositorio, preparará el archivo y lo confirmará con un mensaje como "`initial commit`".

- **Paso 2: Realiza un cambio de código**

Indícale al agente que modifique el código para que haya un cambio que confirmar.

Tus instrucciones:

`In the git_test folder, modify auth.py to add Google Login functionality.`

En español

`En la carpeta git_test, modifica auth.py para agregar la funcionalidad de inicio de sesión con Google.`

El agente editará el archivo para agregar una nueva función y prepararlo para la fase de confirmación.

- **Paso 3: Agrega y confirma los cambios**

Activa la habilidad `git-commit-formatter` pidiéndole al agente que prepare los cambios y cree una confirmación.

Tus instrucciones:

`Stage the changes in the git_test folder and commit them. Make sure to format the commit message using the Conventional Commits skill.`

En español

`Prepara los cambios (stage) en la carpeta git_test y realiza el commit. Asegúrate de dar formato al mensaje de commit utilizando la habilidad de Conventional Commits.`

El agente ejecutará git add auth.py, analizará la diferencia para determinar que se agregó una nueva función al módulo auth y formulará un mensaje de confirmación convencional como feat(auth): implement google login antes de ejecutar git commit.

- **Paso 4: Verifica el registro de Git**

Pídele al agente que recupere el historial de Git para que puedas confirmar que la confirmación con formato se registró correctamente.

Tus instrucciones:

`Show me the git log in the git_test folder.`

En español

`Muéstrame el registro de git en la carpeta git_test.`

El agente ejecutará `git log -n 5` y mostrará el resultado con el mensaje de confirmación de formato.

### Nivel 2: Utilización de recursos (license-header-adder)

Este es el patrón "Referencia".

Es posible que cada archivo fuente de un proyecto corporativo necesite un encabezado específico de la licencia Apache 2.0 de 20 líneas. Es un desperdicio colocar este texto estático directamente en la instrucción (o SKILL.md). Consume tokens cada vez que se indexa la habilidad, y el modelo podría "alucinar" errores tipográficos en el texto legal. Es una buena práctica descargar el texto estático a un archivo de texto sin formato en una carpeta resources/. La habilidad le indica al agente que lea este archivo solo cuando sea necesario.

Encontrarás los archivos en la carpeta license-header-adder del directorio skills.

```bash
license-header-adder/
├── SKILL.md
└── resources/
└── HEADER_TEMPLATE.txt (The heavy text)
```

A continuación, se muestra el archivo SKILL.md:

```markdown
---
name: license-header-adder
description: Adds the standard open-source license header to new source files. Use involves creating new code files that require copyright attribution.
---

# License Header Adder Skill

This skill ensures that all new source files have the correct copyright header.

## Instructions

1. **Read the Template**:
   First, read the content of the header template file located at `resources/HEADER_TEMPLATE.txt`.

2. **Prepend to File**:
   When creating a new file (e.g., `.py`, `.java`, `.js`, `.ts`, `.go`), prepend the `target_file` content with the template content.

3. **Modify Comment Syntax**:

- For C-style languages (Java, JS, TS, C++), keep the `/* ... */` block as is.
- For Python, Shell, or YAML, convert the block to use `#` comments.
- For HTML/XML, use `<!-- ... -->`.
```

#### Cómo ejecutar este ejemplo en Antigravity

Si ya iniciaste Antigravity o la CLI de Antigravity, sigue estos pasos:

- **Paso 1: Crea el archivo de Python con código de muestra**

Tu instrucción:

```text
Create a new file my_script.py with the following python code:

def hello():
print("Hello, World!")
```

En español

```text
Crea un nuevo archivo my_script.py con el siguiente código de Python:

def hello():
print("Hello, World!")
```

Qué sucedió (explicación): El agente invocó una herramienta de escritura de archivos (`write_to_file`) para crear un archivo nuevo llamado `my_script.py` directamente en el directorio de tu espacio de trabajo activo y escribió la función básica de Python en él.

- **Paso 2: Agrega el encabezado de la licencia**

Tu instrucción:

`Add the license header to my*script.py.`

En español

`Agrega el encabezado de la licencia a my_script.py.`

Qué sucedió (explicación): Esta instrucción activó la habilidad **`license-header-adder`**. El agente ubicó y leyó el archivo de plantilla de licencia (**`HEADER_TEMPLATE.txt`**), modificó el estilo de comentarios de comentarios de bloque de estilo C (`/* … */`) a comentarios de estilo Python (#) y lo antepuso en la parte superior del archivo con la herramienta **`replace_file_content`**.

- **Paso 3: Verifica el contenido del archivo**

Observa el archivo **`my_script.py`**. Contendrá el encabezado de la licencia en la parte superior.

Nivel 3: Aprendizaje con ejemplos (json-to-pydantic)
El patrón "Few-Shot".

Convertir datos flexibles (como una respuesta de la API de JSON) en código estricto (como modelos de Pydantic) implica docenas de decisiones. ¿Cómo debemos nombrar las clases? ¿Deberíamos usar Optional? ¿snake_case o camelCase? Escribir estas 50 reglas en inglés es tedioso y propenso a errores.

Los LLM son motores de correlación de patrones.

Crear tu skill con un ejemplo dorado (Input -> Output) suele ser más eficaz que las instrucciones detalladas.

Ve a la carpeta json-to-pydantic/ que contiene los archivos de la skill, como se muestra a continuación:

json-to-pydantic/
├── SKILL.md
└── examples/
├── input_data.json (The Before State)
└── output_model.py (The After State)
A continuación, se muestra el archivo SKILL.md:

---

name: json-to-pydantic
description: Converts JSON data snippets into Python Pydantic data models.

---

# JSON to Pydantic Skill

This skill helps convert raw JSON data or API responses into structured, strongly-typed Python classes using Pydantic.

Instructions

1. **Analyze the Input**: Look at the JSON object provided by the user.
2. **Infer Types**:

- `string` -> `str`
- `number` -> `int` or `float`
- `boolean` -> `bool`
- `array` -> `List[Type]`
- `null` -> `Optional[Type]`
- Nested Objects -> Create a separate sub-class.

3. **Follow the Example**:
   Review `examples/` to see how to structure the output code. notice how nested dictionaries like `preferences` are extracted into their own class.

- Input: `examples/input_data.json`
- Output: `examples/output_model.py`

Style Guidelines

- Use `PascalCase` for class names.
- Use type hints (`List`, `Optional`) from `typing` module.
- If a field can be missing or null, default it to `None`.
  En la carpeta /examples, se encuentran el archivo JSON y el archivo de salida, es decir, el archivo de Python. Ambos se muestran a continuación:

input_data.json

{
"user_id": 12345,
"username": "jdoe_88",
"is_active": true,
"preferences": {
"theme": "dark",
"notifications": [
"email",
"push"
]
},
"last_login": "2024-03-15T10:30:00Z",
"meta_tags": null
}
output_model.py

from pydantic import BaseModel, Field
from typing import List, Optional

class Preferences(BaseModel):
theme: str
notifications: List[str]

class User(BaseModel):
user_id: int
username: str
is_active: bool
preferences: Preferences
last_login: Optional[str] = None
meta_tags: Optional[List[str]] = None
Cómo ejecutar este ejemplo en Antigravity
Si ya iniciaste Antigravity o la CLI de Antigravity, sigue estos pasos:

Paso 1: Crea el archivo JSON con datos de muestra

Pídele al agente que cree un archivo nuevo product.json que contenga la carga útil JSON sin procesar.

Tu instrucción:

Create a new file product.json with the following JSON:

{
"product": "Widget",
"cost": 10.99,
"stock": null
}
Paso 2: Convierte el JSON en un modelo de Pydantic

Activa la habilidad json-to-pydantic para convertir los datos JSON en una clase Pydantic estructurada.

Tu instrucción:

Convert the JSON in product.json to a Pydantic model and save it to product_model.py.
Paso 3: Verifica el resultado

Observa el archivo product_model.py. Contendrá el modelo Pydantic completado.

Nivel 4: Lógica procedimental (database-schema-validator)
Este es el patrón de "Uso de herramientas".

Si le preguntas a un LLM "¿Este esquema es seguro?", es posible que te diga que todo está bien, incluso si falta una clave principal crítica, simplemente porque el código SQL parece correcto.

Deleguemos esta verificación a un script determinístico. Nuestra habilidad database-schema-validator dirigirá al agente para que ejecute una secuencia de comandos de Python que escribimos. La secuencia de comandos proporciona una verdad binaria (verdadero/falso).

database-schema-validator/
├── SKILL.md
└── scripts/
└── validate_schema.py (The Validator)
A continuación, se muestra el archivo SKILL.md:

---

name: database-schema-validator
description: Validates SQL schema files for compliance with internal safety and naming policies.

---

# Database Schema Validator Skill

This skill ensures that all SQL files provided by the user comply with our strict database standards.

Policies Enforced

1. **Safety**: No `DROP TABLE` statements.
2. **Naming**: All tables must use `snake_case`.
3. **Structure**: Every table must have an `id` column as PRIMARY KEY.

Instructions

1. **Do not read the file manually** to check for errors. The rules are complex and easily missed by eye.
2. **Run the Validation Script**:
   Use the `run_command` tool to execute the python script provided in the `scripts/` folder against the user's file.

`python scripts/validate_schema.py <path_to_user_file>`

3. **Interpret Output**:

- If the script returns **exit code 0**: Tell the user the schema looks good.
- If the script returns **exit code 1**: Report the specific error messages printed by the script to the user and suggest fixes.
  A continuación, se muestra el archivo validate_schema.py:

import sys
import re

def validate_schema(filename):
"""
Validates a SQL schema file against internal policy:

1.  Table names must be snake_case.
2.  Every table must have a primary key named 'id'.
3.  No 'DROP TABLE' statements allowed (safety).
    """
    try:
    with open(filename, 'r') as f:
    content = f.read()

        lines = content.split('\n')
        errors = []

        # Check 1: No DROP TABLE
        if re.search(r'DROP TABLE', content, re.IGNORECASE):
            errors.append("ERROR: 'DROP TABLE' statements are forbidden.")

        # Check 2 & 3: CREATE TABLE checks
        table_defs = re.finditer(r'CREATE TABLE\s+(?P<name>\w+)\s*\((?P<body>.*?)\);', content, re.DOTALL | re.IGNORECASE)

        for match in table_defs:
            table_name = match.group('name')
            body = match.group('body')

            # Snake case check
            if not re.match(r'^[a-z][a-z0-9_]*$', table_name):
                errors.append(f"ERROR: Table '{table_name}' must be snake_case.")

            # Primary key check
            if not re.search(r'\bid\b.*PRIMARY KEY', body, re.IGNORECASE):
                errors.append(f"ERROR: Table '{table_name}' is missing a primary key named 'id'.")

        if errors:
            for err in errors:
                print(err)
            sys.exit(1)
        else:
            print("Schema validation passed.")
            sys.exit(0)

except FileNotFoundError:
print(f"Error: File '{filename}' not found.")
sys.exit(1)

if **name** == "**main**":
if len(sys.argv) != 2:
print("Usage: python validate_schema.py <schema_file>")
sys.exit(1)

validate_schema(sys.argv[1])
Cómo ejecutar este ejemplo en Antigravity
Si ya iniciaste Antigravity o la CLI de Antigravity, sigue estos pasos:

Paso 1: Crea el archivo JSON con datos de muestra

Pídele al agente que cree un archivo nuevo bad_schema.sql que contenga varios incumplimientos de política.

Tu instrucción:

Create a new file bad_schema.sql with the following SQL:

DROP TABLE IF EXISTS legacy_users;

CREATE TABLE userProfile (
id INT PRIMARY KEY,
bio TEXT
);

CREATE TABLE posts (
title TEXT,
content TEXT,
created_at TIMESTAMP
);

CREATE TABLE comments (
id INT PRIMARY KEY,
post_id INT,
body TEXT
);
El archivo de esquema anterior incumple las tres políticas: usa una instrucción DROP TABLE prohibida, usa camelCase para el nombre de la tabla userProfile y olvida la clave primaria id en la tabla posts.

Paso 2: Valida el esquema de SQL

Activa la skill database-schema-validator para ejecutar la secuencia de comandos del validador de Python en tu archivo.

Tus instrucciones:

Validate bad_schema.sql using the database-schema-validator skill.
Paso 3: Verifica el resultado

El agente informará el error y mostrará los errores específicos que encontró la secuencia de comandos directamente en el chat. A continuación, se muestra el resultado de muestra:

Suggested Fixes:

Remove the line DROP TABLE IF EXISTS legacy_users; as dropping tables is forbidden by safety policy.

Rename the table userProfile to use snake_case (e.g., user_profile).

Add a primary key column named id to the posts table definition.
