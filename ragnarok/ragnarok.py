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
    @commands.cooldown(10, 60, commands.BucketType.user)
    async def _ragnarok(self, ctx, text):
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
          #End of Float
        #Start of institutional ownership
        elif search_type[0] == "insti":
            if search_valid == "insti":
                await self.bot.say("Please add the the ticker symbol for data.")
            else:
                quary = str(ctx.message.content
                            [len(ctx.prefix+ctx.command.name)+6:].lower())
                encode = urllib.parse.quote_plus(quary, encoding='utf-8',
                                                 errors='replace')
                
                url = "http://www.finviz.com/quote.ashx?t=" + encode
                test = "Inst Own"
                response = requests.get(url)
                if response.status_code == 404:
                     await self.bot.say("Stock not found. Please try again.")
                else:
                    html = response.text
                    indexstring = html.find(test)
                    floatIndexStart = html.find("<b>", indexstring)
                    floatIndexEnd = html.find("</b>", indexstring)
                    floatString = html[floatIndexStart+3:floatIndexEnd] 
                    if floatString == "-":
                        await self.bot.say(encode[1:].upper() + " does not have listed institutional ownership data on Finviz.")
                    elif floatString[0] == "<":
                        exIndex = floatString.find(">")
                        endIndex = floatString.find("</s")
                        floatString = floatString[exIndex+1:endIndex]
                        await self.bot.say(encode[1:].upper() + " has an institutional ownership of " + floatString + ".")
                    else:
                        await self.bot.say(encode[1:].upper() + " has an institutional ownership of " + floatString + ".")
                        #End of institutional Ownership
        #Start of short float
        elif search_type[0] == "short":
            if search_valid == "short":
                await self.bot.say("Please add the the ticker symbol for data")
            else:
                quary = str(ctx.message.content
                            [len(ctx.prefix+ctx.command.name)+6:].lower())
                encode = urllib.parse.quote_plus(quary, encoding='utf-8',
                                                 errors='replace')
                
                url = "http://www.finviz.com/quote.ashx?t=" + encode
                test = "Short Float"
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
                        await self.bot.say(encode[1:].upper() + " does not have listed short float data on Finviz.")
                    elif floatString[0] == "<":
                        exIndex = floatString.find(">")
                        endIndex = floatString.find("</s")
                        floatString = floatString[exIndex+1:endIndex]
                        await self.bot.say(encode[1:].upper() + " has a short float of " + floatString + ".")
                    else:
                        await self.bot.say(encode[1:].upper() + " has a short float of " + floatString + ".")
                        #End of short float
        elif search_type[0] == "pgain":                 
                url = "http://finviz.com/screener.ashx?v=111&o=-change"
                test = "screener-link"
                response = requests.get(url)
                if response.status_code == 404:
                     await self.bot.say("Scan not found. Please try again")
                else:
                    
                    html = response.text
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    
                    indexstring = html.find(test)
                    IndexStart = html.find(">", indexstring)
                    IndexEnd = html.find("<", indexstring)
                    SymString1 = html[IndexStart+1:IndexEnd]
                    
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    
                    indexstring = html.find("><")
                    html = html[indexstring+2:]
                    indexStart = html.find(">")
                    indexEnd = html.find("<")
                    percentChange1 = html[indexStart+1:indexEnd]
                    
                    #move to 2nd
                    indexstring = html.find(">2<")
                    html = html[indexstring:]
                    
                    indexstring = html.find(test)
                    IndexStart = html.find(">", indexstring)
                    IndexEnd = html.find("<", indexstring)
                    SymString2 = html[IndexStart+1:IndexEnd]
                    
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    
                    indexstring = html.find("><")
                    html = html[indexstring+2:]
                    indexStart = html.find(">")
                    indexEnd = html.find("<")
                    percentChange2 = html[indexStart+1:indexEnd]
                    
                    #3rd
                    indexstring = html.find(">3<")
                    html = html[indexstring:]
                    
                    indexstring = html.find(test)
                    IndexStart = html.find(">", indexstring)
                    IndexEnd = html.find("<", indexstring)
                    SymString3 = html[IndexStart+1:IndexEnd]
                    
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    
                    indexstring = html.find("><")
                    html = html[indexstring+2:]
                    indexStart = html.find(">")
                    indexEnd = html.find("<")
                    percentChange3 = html[indexStart+1:indexEnd]
                    
                    #4th
                    indexstring = html.find(">4<")
                    html = html[indexstring:]
                    
                    indexstring = html.find(test)
                    IndexStart = html.find(">", indexstring)
                    IndexEnd = html.find("<", indexstring)
                    SymString4 = html[IndexStart+1:IndexEnd]
                    
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    
                    indexstring = html.find("><")
                    html = html[indexstring+2:]
                    indexStart = html.find(">")
                    indexEnd = html.find("<")
                    percentChange4 = html[indexStart+1:indexEnd]
                    
                    #5th
                    indexstring = html.find(">5<")
                    html = html[indexstring:]
                    
                    indexstring = html.find(test)
                    IndexStart = html.find(">", indexstring)
                    IndexEnd = html.find("<", indexstring)
                    SymString5 = html[IndexStart+1:IndexEnd]
                    
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    indexstring = html.find(test)
                    html = html[indexstring+1:]
                    
                    indexstring = html.find("><")
                    html = html[indexstring+2:]
                    indexStart = html.find(">")
                    indexEnd = html.find("<")
                    percentChange5 = html[indexStart+1:indexEnd]
                    
                    
                    
                    
                    #indexstringSym = html.find(test)
                    #indexSymEnd = html[indexstringSym:].find("</a")
                    #html = html[indexstringSym+5:indexSymEnd]
                    await self.bot.say("Top Gainers -- \n1. " + SymString1 + "\t" + percentChange1 +"\n2. " + SymString2 + "\t" + percentChange2 +"\n3. " + SymString3 + "\t" + percentChange3 +"\n4. " + SymString4 + "\t" + percentChange4 +"\n5. " + SymString5 + "\t" + percentChange5)
                    #floatIndexStart = html.find("<b>", indexstring)
                    #floatIndexEnd = html.find("</b>", indexstring)
                    #floatString = html[floatIndexStart+3:floatIndexEnd] 
                    #if floatString == "-":
                    #    await self.bot.say(encode[1:].upper() + " does not have listed short float data on Finviz.")
                    #elif floatString[0] == "<":
                    #    exIndex = floatString.find(">")
                    #    endIndex = floatString.find("</s")
                    #    floatString = floatString[exIndex+1:endIndex]
                    #    await self.bot.say(encode[1:].upper() + " has a short float of " + floatString + ".")
                    #else:
                    #    await self.bot.say(encode[1:].upper() + " has a short float of " + floatString + ".")       
        #Start of help
        elif search_type[0] == "help":
            if search_valid == "help":
                await self.bot.say("List of working commands--")
                await self.bot.say("~ragnarok float <ticker symbol> :: Checks Finviz for float \n~ragnarok short <ticker symbol> :: Checks Finviz for short float \n~ragnarok insti <ticker symbol> :: Checks Finviz for institutional ownership \n")
                
        else:
            await self.bot.say('Unrecognized command. For options, type ~ragnarok help')
        

def setup(bot):
    n = RagnarokClass(bot)
    bot.add_cog(n)
