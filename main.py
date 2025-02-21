# Imports
import discord, tls_client
from discord.ext import commands

# Init core modules
from core.modules.init import check_dirs, load_config, check_files
from core.modules.logging import *
from core.modules.output import output

# Init core Discord modules
from core.modules.commands.events import init_events
from core.modules.commands.commands import init_commands

class Bot:
    def __init__(self):
        self.session = tls_client.Session()
        self.bot = None

        self.config = {}
        self.token  = ""
        self.prefix = ""
        self.style  = ""
        self.output = output

    def init_bot(self):
        check_dirs()
        check_files()

        self.config = load_config()
        self.token  = self.config["token"]
        self.prefix = self.config["prefix"]
        self.style  = self.config["active_style"]

        self.bot = commands.Bot(command_prefix=self.prefix, self_bot=True)

        init_events(self)
        init_commands(self)

    def run_bot(self):
        self.init_bot()
        self.bot.run(self.token, bot=False)

if __name__ == "__main__":
    bot = Bot()
    bot.run_bot()