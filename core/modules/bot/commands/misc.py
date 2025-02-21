import json

class misc:
    def __init__(self, external_self):
        self.self = external_self

        @self.self.bot.command()
        async def status(ctx):
            discord_ping = round(self.self.bot.latency * 1000)
            await ctx.send(self.self.output("Status", [{"key" : "Discord Ping", "value" : f"{discord_ping} ms"}], ctx.author.name, self.self.style, "general"))

        @self.self.bot.command()
        async def help(ctx, page=1):
            message = []
            from_cmd_count = (page - 1) * 10
            to_cmd_count = page * 10
            commands = json.load(open("core/modules/bot/commands.json"))

            cmds = commands[from_cmd_count:to_cmd_count]

            longest_name = max(len(cmd["name"]) for cmd in cmds) + 2
            longest_args = max(len(", ".join(cmd["arguments"] if cmd["arguments"] else "None")) for cmd in cmds)
            
            for cmd in cmds:
                message.append({
                    "name" : cmd["name"].ljust(longest_name), 
                    "arguments" : f"{', '.join(cmd['arguments']).ljust(longest_args) if cmd['arguments'] else 'None'.ljust(longest_args)}",
                    "description" : cmd["description"]
                })
            await ctx.send(self.self.output("Help | ({} -> {})".format(str(from_cmd_count + 1), str(to_cmd_count)), message, ctx.author.name, self.self.style, "help"))

        @self.self.bot.command()
        async def search(ctx, command_name):
            commands = json.load(open("core/modules/bot/commands.json"))
            for cmd in commands:
                if cmd["name"] == command_name:
                    args = ", ".join(cmd["arguments"]) if cmd["arguments"] else "None"
                    s = "{split}"
                    await ctx.send(self.self.output("Search {}".format(command_name),[{"key" : cmd['name'], "value" : f"[ {args} ] {s} {cmd['description']}"}], ctx.author.name, self.self.style, "general"))