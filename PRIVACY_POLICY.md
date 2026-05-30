# Política de Privacidad

Este bot de Discord almacena únicamente la siguiente información:

- **ID de usuario (Discord Snowflake)** y su **balance** de botellines, guardados en una base de datos SQLite local (`economy.db`).
- **Configuración de respuestas personalizadas** en `cogs/custom_responses.json` (texto introducido por los administradores del servidor).

No se recopilan ni transmiten datos personales a terceros, ni se almacenan mensajes de los usuarios.  Todos los datos permanecen en el disco local del servidor donde se ejecuta el bot.

### Derechos del usuario
- El propietario del servidor puede **borrar** o **resetear** los datos simplemente eliminando `economy.db` y `custom_responses.json`.
- No se comparte información con servicios externos salvo los que ya están configurados (por ejemplo, Twitch o Gemini) mediante sus propias claves de API, que deben ser provistas por el usuario en `.env`.

Esta política cumple con el RGPD y la CCPA al no manejar datos sensibles ni identificadores fuera de los necesarios para la lógica del bot.
