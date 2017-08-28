from discord.ext import commands
from random import choice
from bs4 import BeautifulSoup
import requests
import aiohttp
import re
import urllib


class ScraperClass:

    def __init__(self, bot):
        self.bot = bot
        
    
        
    @commands.command(name="scraper", pass_context=True)
    @commands.cooldown(10, 60, commands.BucketType.user)
    async def _scraper(self, ctx, text):
        """Scraper tasks"""
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
        
        
        #functions
        
        
        #Option Alpha                   
        if search_type[0] == "alpha":
              url = "https://optionalpha.com/members/watch-list"
              response = requests.get(url)
              if response.status_code == 404:
                  await self.bot.say("Site not found. Please try again")
              else:
                  test = "<li class=\"oagrid-item  highiv earnings\">"
                  await self.bot.say("Got this far")
        else:
            await self.bot.say('Unrecognized command. For options, type ~ragnarok help')   
        await self.bot.say("ayooooo")
            
def setup(bot):
    n = ScraperClass(bot)
    bot.add_cog(n)
