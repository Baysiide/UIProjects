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
                           
        if search_type[0] == "finviz":
            url = "http://www.blank.org/"
            response = requests.get(url)
            html = response.content

            soup = BeautifulSoup(html)
            table = soup.find('tbody', attrs={'class': 'stripe'})
            await self.bot.say(table.prettify())
        
        else:
            await self.bot.say('Say Finviz dummy')
        

def setup(bot):
    n = RagnarokClass(bot)
    bot.add_cog(n)
