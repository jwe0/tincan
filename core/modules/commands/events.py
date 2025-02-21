from core.modules.logging import *

def init_events(self):
    @self.bot.event
    async def on_ready():
        success(f"Logged in as {self.bot.user}")

    @self.bot.event
    async def on_message(message):
        await self.bot.process_commands(message)

    @self.bot.event
    async def on_command(ctx):
        await ctx.message.delete()