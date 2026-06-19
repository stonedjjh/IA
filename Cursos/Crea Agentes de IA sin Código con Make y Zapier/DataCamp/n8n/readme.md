# N8N

## Concepto

n8n es una herramienta de automatización de flujos de trabajo de código abierto que permite conectar aplicaciones, servicios y APIs para crear procesos automatizados. Funciona con nodos visuales que representan acciones, disparadores y transformaciones de datos, lo que facilita diseñar integraciones sin necesidad de programar.

## Bondades y ventajas

- Automatización visual: crea flujos con arrastrar y soltar nodos.
- Open source: código abierto y personalizable.
- Integraciones nativas: conecta cientos de servicios y aplicaciones.
- Escalabilidad: se puede usar en proyectos personales, empresas y entornos complejos.
- Control de datos: ejecuta n8n en tu propia infraestructura para mayor privacidad.
- Flexibilidad: admite nodos personalizados y funciones JavaScript para lógica avanzada.
- Comunidad activa: recibe actualizaciones, nuevos nodos y soporte colaborativo.

## Instalación

1. Requisitos:
   - Node.js 18 o superior.
   - npm o pnpm.
   - Docker, si prefieres una instalación en contenedor.

2. Instalación con npm:

```bash
npm install n8n -g
```

3. Ejecutar n8n:

```bash
n8n
```

4. Acceder a la interfaz:

Abre un navegador y ve a `http://localhost:5678`.

5. Instalación con Docker:

```bash
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  n8nio/n8n
```

6. Recomendación:
   - Usa `n8n` en un entorno aislado (Docker o servidor propio) para mantener control sobre tus datos.
   - Guarda tus flujos de trabajo y configura autenticación si lo usas en producción.

## Componentes

1. Disparadores:
   - Inicio automático de un flujo cuando ocurre un evento.
   - Ejemplos: HTTP Request, Webhook, Cron, Gmail, Slack, Google Sheets.
   
   **Tipos:**
   - Manual: se inicia de forma directa por el usuario o desde el editor para probar y validar flujos.
   - Automático: se dispara por eventos externos, cron o cambios de datos, permitiendo ejecutar procesos sin intervención.

2. Nodos de acción:
   - Ejecutan tareas como crear registros, enviar correos, actualizar bases de datos.
   - Se conectan en secuencia para procesar datos.
3. Nodos de transformación:
   - Manipulan la información entre nodos, formatean texto, convierten datos, filtran resultados.
4. Nodos de función:
   - Ejecutan código JavaScript personalizado para lógica avanzada.
   - Útiles cuando necesitas cálculos complejos o condicionales.
5. Nodos de control:
   - Permiten ramificar flujos, manejar errores, repetir procesos, esperar eventos.
6. Nodos de salida:
   - Finalizan el flujo con acciones como notificaciones, respuestas HTTP o creación de archivos.


## Tips

`{{ $now }}` Permite obtener el dia y hora en que se esta ejecutando la acción