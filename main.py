import discord, tls_client
from discord.ext import commands

from core.modules.init import check_dirs, load_config, check_files
from core.modules.logging import *

class Bot:
    def __init__(self):
        self.session = tls_client.Session()
        self.bot = None

        self.config = {}
        self.token  = ""
        self.prefix = ""

    def init_bot(self):
        check_dirs()
        check_files()

        self.config = load_config()
        self.token  = self.config["token"]
        self.prefix = self.config["prefix"]

        self.bot = commands.Bot(command_prefix=self.prefix, self_bot=True)

        @self.bot.event
        async def on_ready():
            success(f"Logged in as {self.bot.user}")

        @self.bot.event
        async def on_message(message):
            await self.bot.process_commands(message)



    def run_bot(self):
        self.init_bot()
        self.bot.run(self.token, bot=False)

if __name__ == "__main__":
    bot = Bot()
    bot.run_bot()