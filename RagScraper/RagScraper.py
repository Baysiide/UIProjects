from discord.ext import commands
from random import choice
from bs4 import BeautifulSoup
import requests
import aiohttp
import re
import urllib

class ScrClass:

    def __init__(self, bot):
        self.bot = bot
     
        

        
        
    @commands.command(name="scr", pass_context=True)
    @commands.cooldown(10, 60, commands.BucketType.user)
    async def _scr(self, ctx, text):
        """Compilation of commands for United Investors. Type '~ragnarok help' for a list"""
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
        
        
        #Start of float calculations                   
        if search_type[0] == "float":
            if search_valid == "float":
                await self.bot.say("Please add the the ticker symbol for data")
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
                    if floatString == "-":
                        await self.bot.say(encode[1:].upper() + " does not have listed float data on Finviz.")
                    elif floatString[0] == "<":
                        exIndex = floatString.find(">")
                        endIndex = floatString.find("</s")
                        floatString = floatString[exIndex+1:endIndex]
                        await self.bot.say(encode[1:].upper() + " has a float of " + floatString + ".")
                    else:
                        await self.bot.say(encode[1:].upper() + " has a float of " + floatString + " shares.")
                        
        elif search_type[0] == "inside":
            if search_valid == "inside":
                await self.bot.say("Please add the the ticker symbol for data")
            else:
                quary = str(ctx.message.content
                            [len(ctx.prefix+ctx.command.name)+7:].lower())
                encode = urllib.parse.quote_plus(quary, encoding='utf-8',
                                                 errors='replace')
                
                url = "http://www.finviz.com/quote.ashx?t=" + encode
                test = "<li class=\"oagrid-item  highiv earnings\">"
                response = requests.get(url)
                if response.status_code == 404:
                     await self.bot.say("Stock not found. Please try again")
                else:
                    html = response.text
                    indexstring = html.find(test)
                    floatIndexStart = html.find("<b>", indexstring)
                    floatIndexEnd = html.find("</b>", indexstring)
                    floatString = html[floatIndexStart+3:floatIndexEnd] 
                    if floatString == "-":
                        await self.bot.say(encode[1:].upper() + " does not have listed insider data on Finviz.")
                    elif floatString[0] == "<":
                        exIndex = floatString.find(">")
                        endIndex = floatString.find("</s")
                        floatString = floatString[exIndex+1:endIndex]
                        await self.bot.say(encode[1:].upper() + " has an insider ownership of " + floatString + ".")
                    else:
                        await self.bot.say(encode[1:].upper() + " has an insider ownership of " + floatString + ".")
        
        
        elif search_type[0] == "alpha":
            url = "http://optionalpha.com/members"
            response = requests.get(url)
            if response.status_code == 404:
                 await self.bot.say("Site not found. Please try again")
            else:
                 #x = 6
                 #test = "<li class=\"oagrid-item  highiv earnings\">"
                 html = response.text
                 await self.bot.say(html[:100])
                 #for y in range(0, x):
                 #   indexstring = html.find(test)
        else:
            await self.bot.say('Unrecognized command. For options, type ~ragnarok help')
            

def setup(bot):
    n = ScrClass(bot)
    bot.add_cog(n)
