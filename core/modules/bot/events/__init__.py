from core.modules.bot.events.general import general

class events:
    def __init__(self, external_self):
        self.bot = external_self.bot
        self.self = external_self

        general(self.bot, self.self)
