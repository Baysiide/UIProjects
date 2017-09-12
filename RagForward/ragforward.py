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
        
    async def proc_mess(self, ctx):
        global messcount
        messcount = messcount + 1
        if ctx.message.content.startswith('@everyone'):
            await self.bot.say("test")
            await self.bot.send_message(discord.Object(id='311323578626867211'), 'hello')
        
        
def setup(bot):
    n = RagForwardClass(bot)
    bot.add_listener(n.proc_mess, "on_message")
    bot.add_cog(n)
