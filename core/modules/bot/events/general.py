from core.modules.logging import *

class general:
    def __init__(self, bot, self2):
        self.bot = bot
        self.self = self2

        @self.bot.event
        async def on_ready():
            success(f"Logged in as {self.bot.user}")
    
        @self.bot.event
        async def on_message(message):
            await self.bot.process_commands(message)
    
        @self.bot.event
        async def on_command(ctx):
            await ctx.message.delete()