from discord.ext import commands
from random import choice
from bs4 import BeautifulSoup
import requests
import aiohttp
import re
import urllib

counter = 0
messcount = 0
class RagForwardClass:

    def __init__(self, bot):
        self.bot = bot
        

    
    async def forward(message, ctx):
        global messcount
        messcount = messcount + 1
        await self.bot.send_message(ctx.channel, "got this far")
        if message.content.startswith("testing"):
            await self.bot.say("Hello biotch")
        
        
def setup(bot):
    n = RagForwardClass(bot)
    bot.add_listener(n.forward, "on_message")
    bot.add_cog(n)
