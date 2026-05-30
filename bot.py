import discord
from discord.ext import commands
import os
import sys
from dotenv import load_dotenv
import logging
from logging.handlers import RotatingFileHandler

# Configure rotating log file (5 MB, keep 5 backups)
log_handler = RotatingFileHandler('logs/bot.log', maxBytes=5_000_000, backupCount=5)
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s: %(message)s',
                    handlers=[log_handler])
# Forzar el directorio de trabajo para PebbleHost
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Cargar variables de entorno
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Configuración del bot
class CapitanAlaskin(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        
        super().__init__(
            command_prefix='!', 
            intents=intents,
            help_command=commands.DefaultHelpCommand(no_category="Comandos")
        )

    async def setup_hook(self):

        # Cargar los cogs (módulos)
        print("[-] Cargando módulos...")
        cogs_dir = './cogs'
        if not os.path.exists(cogs_dir):
            print(f"[!] ERROR CRÍTICO: No se encontró la carpeta '{cogs_dir}'.")
            print("[!] Asegúrate de haber subido la carpeta 'cogs' al panel de PebbleHost.")
        else:
            for filename in os.listdir(cogs_dir):
                if filename.endswith('.py') and not filename.startswith('__'):
                    await self.load_extension(f'cogs.{filename[:-3]}')
                    print(f"[+] Módulo cargado: {filename}")
        
        # Sincronizar los comandos de barra (slash commands)
        await self.tree.sync()
        print("[-] Comandos sincronizados con Discord.")

    async def on_ready(self):
        print(f"[-] Bot conectado como {self.user} (ID: {self.user.id})")
        print("[-] ¡Capitán Alaskin listo para el servicio!")
        
        # Estado del bot
        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching, 
                name="sobre los supervivientes"
            )
        )

if __name__ == '__main__':
    bot = CapitanAlaskin()
    bot.run(TOKEN)
