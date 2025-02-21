from core.modules.logging import *

class general:
    def __init__(self, external_self):
        self.self = external_self

        @self.self.bot.event
        async def on_ready():
            success(f"Logged in as {self.self.bot.user}")
    
        @self.self.bot.event
        async def on_message(message):
            await self.self.bot.process_commands(message)
    
        @self.self.bot.event
        async def on_command(ctx):
            await ctx.message.delete()