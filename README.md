# 📦 Capitán Alaskin – Bot Discord Comercial

---

## 📖 Descripción General

**Capitán Alaskin** es un bot de Discord totalmente configurable para comunidades de supervivencia (o cualquier otro tipo de servidor).  Todas sus respuestas pueden ser editadas por cualquier usuario mediante los slash‑commands públicos `/edit_command` y `/view_command`.  Esto permite a los compradores vender una **solución “listo‑para‑usar”** donde el cliente final puede personalizar cada mensaje sin tocar código.

---

## ✨ Características Principales

| ✅ Funcionalidad | 🎛️ Personalizable | 📂 Archivo Relacionado |
|---|---|---|
| **Comandos básicos** (`/ping`, `/info`, `/publicar_donaciones`) | ✅ Sí (respuesta) | `cogs/general.py` |
| **Economía** (`/balance`, `/pagar`, `/ranking`) | ✅ Sí | `cogs/economy.py` |
| **Guías y normas** (`/guia`, `/normas`) | ✅ Sí | `cogs/guides.py`, `cogs/rules.py` |
| **Vehículos / weed** (cog de ejemplo) | ✅ Sí | `cogs/vehicles.py`, `cogs/weed.py` |
| **Comandos de edición** (`/edit_command`, `/view_command`) | — | `cogs/custom_commands.py` |
| **Sistema de respuestas dinámicas** (`cogs/utils.py`) | — | `cogs/utils.py` |
| **Canales y layout** | — | *Imágenes de ejemplo* |

---

## 📦 Estructura del proyecto

```
botpara subir/
├─ cogs/
│   ├─ __init__.py
│   ├─ general.py
│   ├─ economy.py
│   ├─ guides.py
│   ├─ rules.py
│   ├─ vehicles.py
│   ├─ weed.py
│   ├─ custom_commands.py   ← Gestión pública de respuestas
│   └─ utils.py             ← Lógica de respuestas personalizadas
├─ bot.py                   ← Entrypoint del bot
├─ requirements.txt
├─ custom_responses.json    ← ¡Se entrega VACÍO! (el cliente podrá rellenarlo)
└─ README.md               ← Este archivo
```

---

## 🛠️ Instalación y puesta en marcha

1. **Clonar o copiar la carpeta** que entregamos (en la carpeta *BotVenta*).
2. Instalar dependencias:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```
3. Crear el archivo `custom_responses.json` (puede quedar vacío; el bot lo creará automáticamente).
4. Ejecutar el bot:
   ```powershell
   python bot.py
   ```
5. Invitar al bot a tu servidor con el **OAuth2 URL** generada en el portal de desarrolladores de Discord (permiso de `applications.commands` y `bot`).

---

## 🎛️ Personalizar respuestas (para el comprador)

Los usuarios pueden cambiar cualquier mensaje del bot sin tocar código:

- **Editar** la respuesta de `/ping`:
  ```
  /edit_command command:"ping" content:"🎉 ¡Pong personalizado!"
  ```
- **Ver** la respuesta actual de `/balance`:
  ```
  /view_command command:"balance"
  ```
- Las respuestas se guardan en `cogs/custom_responses.json` y persisten entre reinicios.

> **Nota:** Los comandos críticos de administración (`/ban`, `/kick`, etc.) **no** están expuestos a este mecanismo por razones de seguridad.

---

## 📸 Mock‑up del layout del servidor (para el cliente)

![Canales principales](/C:/Users/pintu/.gemini/antigravity-ide/brain/e1046662-7934-491b-9c05-e11b80ec5ca3/discord_channels_full_mockup_1780146626594.png)

---

## 📚 Documentación adicional

- **Informe de funciones del bot** – `bot_functions_report.md` (incluye tabla de comandos y descripciones).
- **Guía de venta** – Incluye este README y todos los assets en la carpeta *BotVenta*.

---

## 🚀 Licencia y soporte

Este bot se entrega bajo la licencia **MIT**.  Para soporte o actualizaciones, contacte al autor original.

---

*¡Listo para vender y personalizar!*
