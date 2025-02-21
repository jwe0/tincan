from core.modules.bot.commands.misc import misc
from core.modules.bot.commands.spotify import spotify


class commands:
    def __init__(self, external_self):
        misc(external_self)
        spotify(external_self)