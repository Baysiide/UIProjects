from discord.ext import commands
from random import choice
from bs4 import BeautifulSoup
import requests
import aiohttp
import re
import urllib

class RagForwardClass:

    def __init__(self, bot):
        self.bot = bot
        

    
    async def forward(self, ctx, content):
        #await self.bot.send_message(ctx.channel, message.content)
        if content.startswith("testing"):
            await self.bot.send_message(ctx.channel, content)
        #else:
            #await self.bot.send_message(ctx.channel, pop)
        
        
def setup(bot):
    n = RagForwardClass(bot)
    bot.add_listener(n.forward, "on_message")
    bot.add_cog(n)
