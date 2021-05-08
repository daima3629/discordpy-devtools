from discord.ext import commands
import logging
import log


class DevTools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger("discordpy-devtools")
        self.logger.addHandler(log.StreamSwitchHandler())
        self.logger.setLevel(logging.DEBUG)


def setup(bot):
    bot.add_cog(DevTools(bot))
