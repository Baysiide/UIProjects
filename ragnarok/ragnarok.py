from discord.ext import commands
from random import choice
from bs4 import BeautifulSoup
import requests
import aiohttp
import re
import urllib


class RagnarokClass:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ragnarok", pass_context=True)
    @commands.cooldown(5, 60, commands.BucketType.user)
    async def _ragnarok(self, ctx, text):
        """Compilation #2 of commands for United Investors"""
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
                           
        if search_type[0] == "float":
            if search_valid == "float":
                await self.bot.say("Please actually search something")
            else:
                quary = str(ctx.message.content
                             [len(ctx.prefix+ctx.command.name)+6:].lower())
                    encode = urllib.parse.quote_plus(quary, encoding='utf-8',
                                                     errors='replace')
                
                url = "http://www.finviz.com/quote.ashx?t=" + encode
                test = "Shs Float"
                response = requests.get(url)
                if response.status_code == 404:
                     await self.bot.say("Stock not found. Please try again")
                else:
                    html = response.text
                    indexstring = html.find(test)
                    floatIndexStart = html.find("<b>", indexstring)
                    floatIndexEnd = html.find("</b>", indexstring)
                    floatString = html[floatIndexStart+3:floatIndexEnd] 
            
            
                    await self.bot.say(indexstring)
                    await self.bot.say(floatIndexStart)
                    await self.bot.say(floatIndexEnd)
                    await self.bot.say(floatString + " shares")
        
        else:
            await self.bot.say('Say Finviz dummy')
        

def setup(bot):
    n = RagnarokClass(bot)
    bot.add_cog(n)
