#

## Instalación

Windows PowerShell:

`irm https://antigravity.google/cli/install.ps1 | iex`

CMD de Windows:

`curl -fsSL https://antigravity.google/cli/install.cmd -o install.cmd && install.cmd && del install.cmd`

> [!IMPORTANT]
> La instalación puede fallar en agregar el path a las variable de entorno por lo cual si
> muestra `Warning: /Users/neilirani/.local/bin is not present in your active PATH.` un mensaje parecido a este hay que agregar el path manualmente.

## Uso

- `agy --version`: muestra la version instalada

- `agy`: Ejecuta la cli de **Antigravity**

- `agy --help`: Hay algunos parámetros de línea de comandos que se pueden proporcionar cuando se inicia la CLI de Antigravity. Para obtener una lista completa de las opciones, puedes usar `--help`.

- `/help`: muestra la ayuda en la cli, comandos, atajos.

- `/quit`: salir de la cli de **Antigravity**

- `/setting`:

- `/config`: Esto mostrará varias áreas de Antigravity que puedes personalizar según tus preferencias. Esto incluye el esquema de color, el permiso de la herramienta, la configuración de telemetría y mucho más.

## settings.json

Los parámetros de configuración deben almacenarse en algún lugar, ¿verdad? Todos se almacenan en el archivo ~/.gemini/antigravity-cli/settings.json. A continuación, se muestra un ejemplo:

```JSON
{
      "colorScheme": "dark",
      "model": "Gemini 3.5 Flash (High)",
      "statusLine": {
        "type": "",
        "command": "",
        "enabled": true
      },
      "trustedWorkspaces": [
        "/Users/romin/antigravity-cli-projects",
        "/Users/romin/agy-cli-projects"
      ]
    }
```

## Permiso de la herramienta

Un parámetro de configuración importante que debes comprender es el permiso de la herramienta. Esto controla si los comandos de la terminal requieren tu aprobación antes de ejecutarse. Puedes acceder a esta opción con el comando /config.

```bash
 Tool Permission
  > request-review (current)
    proceed-in-sandbox
    always-proceed
    strict
```

De forma predeterminada, se establece en `request-review`. Analicemos esto con más detalle. En Antigravity, la configuración de permisos de herramientas controla el equilibrio entre la seguridad (protección del sistema host contra cambios no deseados) y la velocidad (qué tan autónomamente puede trabajar el agente sin detenerse para recibir tu entrada). Revisemos las opciones:

**request-review (predeterminado actual):**

En este modo, el agente se considera un socio colaborador que se comunica antes de realizar cualquier acción que pueda afectar los archivos del sistema o del proyecto fuera de los límites aprobados previamente. Cada vez que el agente intenta ejecutar un comando de terminal, realizar una operación de archivo (como escribir o borrar) o llamar a un servicio externo en el que no se aprobó previamente el permiso, la ejecución se pausa. Se le solicita al usuario que apruebe o rechace la acción específica.

**proceed-in-sandbox:**

Este modo permite que el agente ejecute comandos de terminal automáticamente, pero dentro de un contenedor seguro y aislado. El agente puede ejecutar comandos sin pedirte que lo hagas, pero esos comandos se ejecutan en una zona de pruebas virtualizada (p.ej., un contenedor ligero). No pueden modificar el sistema de archivos de tu máquina host real ni acceder a tu red local.

**always-proceed:**

Este es el modo completamente autónomo, que le brinda al agente la máxima velocidad y capacidad. El agente tiene permiso total para ejecutar comandos y escribir archivos directamente en tu máquina anfitrión. Nunca te pedirá confirmación.

**strict:**

Este es un modo de alta seguridad y confianza cero. Las capacidades del agente se restringen a la ejecución de herramientas de lectura. Todas las herramientas que no sean de lectura requerirán que se le solicite al usuario que realice una acción.

## Parámetros de comandos

**Modo no interactivo (autónomo):**

Una opción interesante es ejecutar Antigravity CLI en modo no interactivo. Esto significa que le proporcionas directamente la instrucción y responde a ella sin que se abra la terminal interactiva de Antigravity CLI. Esto es muy útil si planeas usar Antigravity CLI de forma automatizada como parte de la secuencia de comandos o cualquier otro proceso de automatización.

Usas el parámetro `-p` para proporcionar la instrucción a la CLI de Antigravity, como se muestra a continuación:

`agy -p "What is the gcloud command to deploy to Cloud Run"`

Esta puede ser una buena forma de obtener respuestas rápidas, pero ten en cuenta que no hay posibilidad de continuar la conversación con preguntas adicionales.

**Elige un modelo específico:**

La primera es pedirle a la CLI de Antigravity que use un modo específico de Gemini. Puedes usar el parámetro `--model` para indicarle a la CLI de Antigravity que use un modelo específico solo durante su sesión. Esto es muy útil para el modo no interactivo que mencionamos en la sección anterior, en el que te gustaría iniciar varias sesiones de `agy` y usar modelos específicos para tareas específicas.

Pero primero, debes saber qué modelos están disponibles para la CLI de Antigravity. Puedes hacerlo con el subcomando `models`, como se muestra a continuación:

```bash
$ agy models
Gemini 3.5 Flash (Medium)
Gemini 3.5 Flash (High)
Gemini 3.5 Flash (Low)
Gemini 3.1 Pro (Low)
Gemini 3.1 Pro (High)
Claude Sonnet 4.6 (Thinking)
Claude Opus 4.6 (Thinking)
GPT-OSS 120B (Medium)
```

Puedes usar cualquiera de estos nombres de modelos para especificar el modelo que se usará en la sesión. Puedes hacerlo con el comando `--model` que se muestra a continuación:

`agy --model "Gemini 3.5 Flash (Low)"`

Una vez que se inicie la CLI de Antigravity, puedes verificar con el comando `/model` el modelo específico que le pediste que usara o mirar en la parte inferior derecha para ver el modelo que se usó para la sesión.

**Vivir peligrosamente:**

Si te gusta vivir al límite, puedes buscar un parámetro con un nombre muy adecuado llamado `--dangerously-skip-permissions`. Se aprobarán automáticamente todos los permisos de herramientas. No aparecerá ningún mensaje que te solicite permisos. Así que úsala con cuidado.

Ejecuta la CLI de Antigravity con el siguiente comando:

`agy --dangerously-skip-permissions`

Luego, proporciona la siguiente instrucción. Verifica que no me haya pedido permisos de escritura de archivos.

"get the latest news and write it in a file called news.txt. Then create another file that contains the summary of that file."

● ListDir(/Users/romin/agy-cli-projects)
● WebSearch(latest world news May 24 2026 news headlines) (ctrl+o to expand)

▸ Thought for 2s, 95 tokens
Processing News Information

● Create(/Users/romin/agy-cli-projects/news.txt)
● Create(/Users/romin/agy-cli-projects/summary.txt) (ctrl+o to expand)

I have fetched the latest world news headlines and created the requested files in your workspace:

1. news.txt: Contains the detailed news headlines for today (May 24, 2026), including topics on geopolitics (U.S.-Iran negotiations, Ukraine conflict), U.S.
   security incidents, the Ebola outbreak in Central Africa, and the passing of NASCAR champion Kyle Busch.
2. summary.txt: Contains a concise, structured summary of the major categories covered in the news file.

Este modo puede ser útil en situaciones en las que las cosas son locales y están bajo tu control, pero debes estar preparado para sorpresas y, por lo tanto, usarlo con cuidado.

## CLI de Antigravity: modo de Shell

Este es un buen momento para aprender a trabajar directamente con Shell desde la CLI de Antigravity. Puedes ingresar al modo de shell presionando `!` en el cuadro de mensaje. Esto alternará a un modo de Shell. Para volver, presiona `!` de nuevo o la tecla ESC.

En el modo de Shell, verás `!` al principio de la instrucción, como se muestra a continuación:

Puedes verificarlo directamente con comandos estándar como `pwd` y `ls`, como se muestra a continuación. Ten en cuenta que los comandos suponen un SO de tipo Linux. Si usas otro sistema operativo (Windows), usa comandos equivalentes, como (`cd`, `dir` y `type`).
