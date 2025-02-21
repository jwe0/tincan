from core.modules.bot.commands.misc import misc


class commands:
    def __init__(self, external_self):
        self.bot = external_self.bot
        self.self = external_self
        misc(self.bot, self.self)