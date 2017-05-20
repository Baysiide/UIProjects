import discord
from discord.ext import commands
import tosdb

tosdb.init(root="C:/Users/camedee.ENROUTE4/TOSDataBridge/bin")
block1 = tosdb.TOSDB_DataBlock(10000, True)
block1.add_topics(tosdb.TOPICS.LAST.val, "bid", "ASK", "vOLuMe")


class RagnarokToS:
    def init(self, bot):
        self.bot = bot

    @commands.command()
    async def ragToS(self, ctx, text):
        block1.add_items('GLYC')

        #Your code will go here

        await self.bot.say(block1)

def setup(bot):
    bot.add_cog(RagnarokToS(bot))
