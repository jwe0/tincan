from core.modules.bot.commands import commands
from core.modules.bot.events import events
class BotInit:
    def __init__(self, bot):
        self.bot = bot

        commands(self.bot)
        events(self.bot)