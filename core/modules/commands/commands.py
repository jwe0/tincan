def init_commands(self):
    @self.bot.command()
    async def ping(ctx):
        await ctx.send(self.output("Ping pong", "Pong!", ctx.author.name, self.style))