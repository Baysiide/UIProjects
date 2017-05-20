import discord
from discord.ext import commands
import tosdb

tosdb.init(root="C:/Users/camedee.ENROUTE4/TOSDataBridge/bin")
block1 = tosdb.TOSDB_DataBlock(10000, True)
block1.add_topics(tosdb.TOPICS.LAST.val, "bid", "ASK", "vOLuMe")


class RagnarokToS:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ragToS", pass_context=True)
    @commands.cooldown(10, 60, commands.BucketType.user)
    async def _ragToS(self, ctx, text):
        """Compilation of ToS commands for United Investors. Type '~ragnarok help' for a list"""
        search_type = ctx.message.content[len(ctx.prefix+ctx.command.name)+1:].lower().split(" ")
        option = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
        }
        regex = [
            re.compile(",\"ou\":\"([^`]*?)\""),
            re.compile("<h3 class=\"r\"><a href=\"\/url\?url=([^`]*?)&amp;"),
            re.compile("<h3 class=\"r\"><a href=\"([^`]*?)\""),
            re.compile("\/url?url=")
            ]
        search_valid = str(ctx.message.content
                           [len(ctx.prefix+ctx.command.name)+1:].lower())
        
        block1.add_items('GLYC')

        #Your code will go here

        await self.bot.say(block1)

def setup(bot):
    bot.add_cog(RagnarokToS(bot))
