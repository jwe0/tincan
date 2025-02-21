class misc:
    def __init__(self, bot, self2):
        self.bot = bot
        self.self = self2
        
        @self.bot.command()
        async def ping(ctx):
            await ctx.send(self.self.output("Ping pong", "Pong!", ctx.author.name, self.self.style))