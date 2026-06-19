# MCP con Antigravity

## Preparar el entorno

### Configura el proyecto de Cloud

Crea o selecciona un proyecto de Google Cloud
En la consola de Google Cloud, selecciona o crea un proyecto de Google Cloud.

### Habilita la API

Para usar el servidor de MCP de Developer Knowledge, debes habilitar la API estándar de Developer Knowledge. [Habilitar](https://console.cloud.google.com/flows/enableapi?apiid=developerknowledge.googleapis.com&hl=es-419)

### Crea la clave de API

Para usar el servidor de MCP de Developer Knowledge, debes usar una clave de API. En la consola de Google Cloud, haz lo siguiente:

1. Ve a **APIs y servicios > Credenciales**.

   [Ir a Credenciales](https://console.cloud.google.com/apis/credentials?hl=es-419)

2. Haz clic en **+ Crear credenciales** y, luego, selecciona **Clave de API** en el menú.
3. Establece **Nombre** con un nombre arbitrario, como `Antigravity`.
4. Haz clic en el menú desplegable **Select API restrictions**, escribe `Developer Knowledge API`, marca el resultado y, luego, haz clic en OK.
5. Haz clic en **Crear**.
6. Ahora, tu clave de API se muestra en la pantalla de confirmación. Cópiala en el portapapeles, ya que la necesitarás para configurar **Antigravity** en los próximos pasos.

## Cómo configurar Antigravity

Ahora, configuremos Antigravity para que use el extremo de MCP. Si no tienes instalados Antigravity 2.0, el IDE o la CLI, sigue las instrucciones del [sitio web de Antigravity](https://antigravity.google/docs/home?hl=es-419)

### Cómo agregar servidores MCP personalizados

Antigravity 2.0, el IDE y la CLI comparten una configuración central de MCP en el archivo `~/.gemini/config/mcp_config.json`.

1. Ábrelo en tu editor de texto preferido.

   > [!NOTE]
   > Puedes acceder al archivo directamente desde el IDE de Antigravity si lo tienes instalado. Para ello, sigue estos pasos:
   >
   > a. Abre MCP Servers a través del menú desplegable … en la parte superior del panel del agente del editor.
   > b. Haz clic en Manage MCP Servers y, luego, en View raw config.

2. Modifícalo con la siguiente configuración personalizada del servidor de MCP. Antes de hacerlo, reemplaza el marcador de posición <YOUR_API_KEY> por la clave de API que creaste en los pasos anteriores:

```JSON
{
"mcpServers": {
"google-developer-knowledge": {
"headers": {
"X-Goog-Api-Key": "<YOUR_API_KEY>"
},
"serverUrl": "https://developerknowledge.googleapis.com/mcp"
}
...
}
...
}
```

### Validar

Deberías ver el servidor de MCP que configuraste como instalado en Antigravity: `google-developer-knowledge`.

#### Antigravity 2.0

1. Haz clic en **Configuración** en la parte inferior izquierda.
2. Navega a **Personalizaciones**.
3. En **Installed MCP Servers**, haz clic en **Refresh**.

![Antigravity 2.0](configuracion MCP.png)
