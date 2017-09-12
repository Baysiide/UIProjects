from discord.ext import commands
from random import choice
from bs4 import BeautifulSoup
import requests
import aiohttp
import re
import urllib

counter = 0
messcount = 0
class RagnarokClass:

    def __init__(self, bot):
        self.bot = bot
        
    async def proc_mess(self, ctx):
        global messcount
        messcount = messcount + 1
        
        
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
        
        
        #functions
        def symStringLenCheck(SymString):
                        if len(SymString) == 1:
                            SymString = SymString + "   "
                        elif len(SymString) == 2:
                            SymString = SymString + "  "
                        elif len(SymString) == 3:
                            SymString = SymString + " "
                        return SymString     
        
        def symToPerc(oriString, text):
                    indexstring = oriString.find(text)
                    oriString = oriString[indexstring+1:]
                    indexstring = oriString.find(text)
                    oriString = oriString[indexstring+1:]
                    indexstring = oriString.find(text)
                    oriString = oriString[indexstring+1:]
                    indexstring = oriString.find(text)
                    oriString = oriString[indexstring+1:]
                    indexstring = oriString.find(text)
                    oriString = oriString[indexstring+1:]
                    indexstring = oriString.find(text)
                    oriString = oriString[indexstring+1:]
                    indexstring = oriString.find(text)
                    oriString = oriString[indexstring+1:]
                    indexstring = oriString.find(text)
                    oriString = oriString[indexstring+1:]
                    indexstring = oriString.find(text)
                    oriString = oriString[indexstring+1:]
                    return oriString
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
                test = "Insider Own"
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
        
        elif search_type[0] == "fdacalendar":
            x = 0
            if search_valid == "fdacalendar":
                x = 3
            else:
                quary = str(ctx.message.content
                            [len(ctx.prefix+ctx.command.name)+12:].lower())
                encode = urllib.parse.quote_plus(quary, encoding='utf-8',
                                                 errors='replace')
                x = int(encode)
                
            url = "https://www.biopharmcatalyst.com/calendars/fda-calendar"
            test = "/company/"
            response = requests.get(url)
            if response.status_code == 404:
                await self.bot.say("Site is down. Please try again")
            else:
                html = response.text
                for y in range(0, x):
                    
                    indexstring = html.find(test)
                    IndexStart = html.find("ticker", indexstring)
                    IndexEnd = html.find("</a>", indexstring)
                    compString = html[IndexStart+8:IndexEnd] 
                    html = html[indexstring:]
                
                    indexstring = html.find("data-value")
                    html = html[indexstring:]
                
                    IndexStart = html.find("\">")
                    IndexEnd = html.find("</div>")
                    priceString = html[IndexStart+2:IndexEnd]
                    html = html[IndexEnd:]
                
                    IndexStart = html.find("drug")
                    IndexEnd = html.find("</strong>")
                    drugString = html[IndexStart+6:IndexEnd]
                    html = html[IndexEnd:]
                    
                    IndexStart = html.find("cation")
                    IndexEnd = html.find("</div>")
                    conString = html[IndexStart+8:IndexEnd]
                    html = html[IndexEnd:]
                
                    IndexStart = html.find("a href")
                    IndexEnd = html.find("\" target")
                    urlString = "<" + html[IndexStart+8:IndexEnd] + ">"
                    html = html[IndexEnd:]
                
                    IndexStart = html.find("-date")
                    IndexEnd = html.find("</time>")
                    dateString = html[IndexStart+7:IndexEnd]
                    html = html[IndexEnd:]
                
                    IndexStart = html.find("-note")
                    IndexEnd = html.find("</div>")
                    dataString = html[IndexStart+7:IndexEnd]
                    html = html[IndexEnd:]
                    
                    if y == 0:
                        await self.bot.say("*Dates shown are LATEST expected release dates. FDA data for these may be already released.*")
                    if y != x-1:
                        await self.bot.say(dateString + " - **" + compString + "**  -  " + priceString + "          Drug/Condition: " + drugString + "/" + conString + "\n" + urlString + "\n" + dataString + "\n------------------------------------------------------------------------")
                    else:
                        await self.bot.say(dateString + " - **" + compString + "**  -  " + priceString + "          Drug/Condition: " + drugString + "/" + conString + "\n" + urlString + "\n" + dataString)
                
                
        
        elif search_type[0] == "add":
            if search_valid == "add":
                await self.bot.say("How much was it?")
            else:
                quary = str(ctx.message.content
                            [len(ctx.prefix+ctx.command.name)+5:].lower())
                encode = urllib.parse.quote_plus(quary, encoding='utf-8',
                                                 errors='replace')
                global counter

                amount = int(encode)
                if (amount > 0 and amount <= 99):
                    text = "Solid profits!"
                elif (amount > 99 and amount <= 499):
                    text = "Nice! Go buy yourself a nice dinner!"
                elif (amount > 499 and amount <= 999):
                    text = "Geez buddy save some for the rest of us!" 
                elif (amount > 999 and amount < 9999):
                    text = "Absolutely insane... Congratulations!"
                elif (amount > 9999):
                    text = "That's it, I quit"
                elif (amount < 0):
                    text = "Ouch. That's ok! Tomorrow is another trading day. Message a mod if would like some unbiased loss analysis."
                    
                counter = counter + amount
                
                await self.bot.say(text + "\nTotal of $" + str(counter) + " made in IU today!")    
                
        elif search_type[0] == "clearcounter":
            global counter
            counter = 0
            await self.bot.say("Counter has been cleared to " + str(counter))
            
        elif search_type[0] == "clearmsgcounter":
            global messcount
            messcount = 0
            await self.bot.say("Message counter has been cleared to " + str(messcount))
        
        elif search_type[0] == "total":
            global counter
            
            await self.bot.say("Total of $" + str(counter) + " made in IU today!")
            
        elif search_type[0] == "msgtotal":
            global messcount
            
            await self.bot.say("Message count: " + str(messcount))
        
        elif search_type[0] == "chart":
            if search_valid == "chart":
                await self.bot.say("Please add the ticker symbol for data.")
            else:
                quary = str(ctx.message.content
                            [len(ctx.prefix+ctx.command.name)+6:].lower())
                encode = urllib.parse.quote_plus(quary, encoding='utf-8',
                                                 errors='replace')
                
                url = "http://finviz.com/chart.ashx?t={}&ty=c&ta=1&p=d&s=l".format(encode)
                response = requests.get(url)
                if response.status_code == 404:
                    await self.bot.say("Stock not found. Please try again.")
                else:
                    await self.bot.say(url)
                    #await self.bot.say(response)
                    
        elif search_type[0] == "news":
            if search_valid == "news":
                await self.bot.say("Please add the ticker symbol for data.")
            else:
                quary = str(ctx.message.content
                            [len(ctx.prefix+ctx.command.name)+6:].lower())
                encode = urllib.parse.quote_plus(quary, encoding='utf-8',
                                                 errors='replace')
                
                url = "http://www.nasdaq.com/symbol/{}/news-headlines".format(encode)
                newsList = url
                response = requests.get(url)
                if response.status_code == 404:
                    await self.bot.say("Stock not found. Please try again.")
                else:
                    html = response.text
                    
                    test = "<div class=\"news-headlines\">"
                    indexstring = html.find(test)
                    html = html[indexstring:]
                    
                    test = "href="
                    indexstring = html.find(test)
                    html = html[indexstring:]
                    
                    #await self.bot.say(html[6:105])

                    IndexEnd = html.find(">")
                    newsString = html[6:IndexEnd-1] 
                    
                    test = "<small>"
                    indexstring = html.find(test)
                    html = html[indexstring+7:]
                    
                    IndexEnd = html.find("-")
                    dateString = html[7:IndexEnd-1] 
                    
                    #2nd
                    test = "target="
                    indexstring = html.find(test)
                    html = html[indexstring:]
                    
                    test = "href="
                    indexstring = html.find(test)
                    html = html[indexstring:]
                    
                    IndexEnd = html.find(">")
                    newsString1 = html[6:IndexEnd-1]
                    
                    test = "<small>"
                    indexstring = html.find(test)
                    html = html[indexstring+7:]
                    
                    IndexEnd = html.find("-")
                    dateString1 = html[7:IndexEnd-1]
                    
                    #3rd
                    test = "target="
                    indexstring = html.find(test)
                    html = html[indexstring:]
                    
                    test = "href="
                    indexstring = html.find(test)
                    html = html[indexstring:]
                    
                    IndexEnd = html.find(">")
                    newsString2 = html[6:IndexEnd-1]
                    
                    test = "<small>"
                    indexstring = html.find(test)
                    html = html[indexstring+7:]
                    
                    IndexEnd = html.find("-")
                    dateString2 = html[7:IndexEnd-1]
                    
                    if newsString == "-":
                        await self.bot.say(encode.upper() + " does not have listed news on Nasdaq.")
                    else:
                        await self.bot.say(encode.upper() + " most recent news: \n" + dateString + "  -  " + newsString + "\n" + dateString1 + "  -  " + "<" + newsString1 + ">" + "\n" + dateString2 + "  -  " + "<" + newsString2 + ">")
                        await self.bot.say("Full list: " + "<" + newsList + ">")
        
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
                    SymString1 = symStringLenCheck(SymString = SymString1)
                    
                    html = symToPerc(oriString = html, text = test)
                                        
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
                    SymString2 = symStringLenCheck(SymString = SymString2)
                    
                    html = symToPerc(oriString = html, text = test)
                    
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
                    SymString3 = symStringLenCheck(SymString = SymString3)
                    
                    html = symToPerc(oriString = html, text = test)
                    
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
                    SymString4 = symStringLenCheck(SymString = SymString4)
                    
                    html = symToPerc(oriString = html, text = test)
                    
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
                    SymString5 = symStringLenCheck(SymString = SymString5)
                    
                    html = symToPerc(oriString = html, text = test)
                    
                    indexstring = html.find("><")
                    html = html[indexstring+2:]
                    indexStart = html.find(">")
                    indexEnd = html.find("<")
                    percentChange5 = html[indexStart+1:indexEnd]
                    await self.bot.say("```Top Gainers -- \n1. " + SymString1 + "\t" + percentChange1 +"\n2. " + SymString2 + "\t" + percentChange2 +"\n3. " + SymString3 + "\t" + percentChange3 +"\n4. " + SymString4 + "\t" + percentChange4 +"\n5. " + SymString5 + "\t" + percentChange5 +"```")
        
        elif search_type[0] == "plose":                 
                url = "http://finviz.com/screener.ashx?v=111&o=change"
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
                    SymString1 = symStringLenCheck(SymString = SymString1)
                    
                    html = symToPerc(oriString = html, text = test)
                    
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
                    SymString2 = symStringLenCheck(SymString = SymString2)
                    
                    html = symToPerc(oriString = html, text = test)
                    
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
                    SymString3 = symStringLenCheck(SymString = SymString3)
                    
                    html = symToPerc(oriString = html, text = test)
                    
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
                    SymString4 = symStringLenCheck(SymString = SymString4)
                    
                    html = symToPerc(oriString = html, text = test)
                    
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
                    SymString5 = symStringLenCheck(SymString = SymString5)
                    
                    html = symToPerc(oriString = html, text = test)
                    
                    indexstring = html.find("><")
                    html = html[indexstring+2:]
                    indexStart = html.find(">")
                    indexEnd = html.find("<")
                    percentChange5 = html[indexStart+1:indexEnd]
                    await self.bot.say("```Top Losers -- \n1. " + SymString1 + "\t" + percentChange1 +"\n2. " + SymString2 + "\t" + percentChange2 +"\n3. " + SymString3 + "\t" + percentChange3 +"\n4. " + SymString4 + "\t" + percentChange4 +"\n5. " + SymString5 + "\t" + percentChange5 +"```")
        
        elif search_type[0] == "pummh":                 
                url = "http://finviz.com/screener.ashx?v=111&f=cap_micro,sh_avgvol_o200,ta_sma20_pa,ta_sma200_pa,ta_sma50_pa&ft=4&o=-change"
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
                    SymString1 = symStringLenCheck(SymString = SymString1)
                    
                    html = symToPerc(oriString = html, text = test)
                                        
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
                    SymString2 = symStringLenCheck(SymString = SymString2)
                    
                    html = symToPerc(oriString = html, text = test)
                    
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
                    SymString3 = symStringLenCheck(SymString = SymString3)
                    
                    html = symToPerc(oriString = html, text = test)
                    
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
                    SymString4 = symStringLenCheck(SymString = SymString4)
                    
                    html = symToPerc(oriString = html, text = test)
                    
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
                    SymString5 = symStringLenCheck(SymString = SymString5)
                    
                    html = symToPerc(oriString = html, text = test)
                    
                    indexstring = html.find("><")
                    html = html[indexstring+2:]
                    indexStart = html.find(">")
                    indexEnd = html.find("<")
                    percentChange5 = html[indexStart+1:indexEnd]
                    await self.bot.say("```Small Cap Swing Scanner by PummHead -- \n1. " + SymString1 + "\t" + percentChange1 +"\n2. " + SymString2 + "\t" + percentChange2 +"\n3. " + SymString3 + "\t" + percentChange3 +"\n4. " + SymString4 + "\t" + percentChange4 +"\n5. " + SymString5 + "\t" + percentChange5 +"```")
        
        elif search_type[0] == "afiro":                 
                url = "http://www.finviz.com/screener.ashx?v=111&f=geo_usa,ind_stocksonly,sh_avgvol_o100,sh_price_u5,ta_averagetruerange_o0.25,ta_volatility_wo3&ft=4&o=-change"
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
                    SymString1 = symStringLenCheck(SymString = SymString1)
                    
                    html = symToPerc(oriString = html, text = test)
                                        
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
                    SymString2 = symStringLenCheck(SymString = SymString2)
                    
                    html = symToPerc(oriString = html, text = test)
                    
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
                    SymString3 = symStringLenCheck(SymString = SymString3)
                    
                    html = symToPerc(oriString = html, text = test)
                    
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
                    SymString4 = symStringLenCheck(SymString = SymString4)
                    
                    html = symToPerc(oriString = html, text = test)
                    
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
                    SymString5 = symStringLenCheck(SymString = SymString5)
                    
                    html = symToPerc(oriString = html, text = test)
                    
                    indexstring = html.find("><")
                    html = html[indexstring+2:]
                    indexStart = html.find(">")
                    indexEnd = html.find("<")
                    percentChange5 = html[indexStart+1:indexEnd]
                    await self.bot.say("```Afiron Volatility Scanner -- \n1. " + SymString1 + "\t" + percentChange1 +"\n2. " + SymString2 + "\t" + percentChange2 +"\n3. " + SymString3 + "\t" + percentChange3 +"\n4. " + SymString4 + "\t" + percentChange4 +"\n5. " + SymString5 + "\t" + percentChange5 +"```")
        
        #Start of help
        elif search_type[0] == "help":
            if search_valid == "help":
                await self.bot.say("```Ragnarok's list of working commands-- \n~chart <ticker symbol> :: Shows image of daily chart \n~float <ticker symbol> :: Checks Finviz for float \n~insti <ticker symbol> :: Checks Finviz for institutional ownership \n~short <ticker symbol> :: Checks Finviz for short float \n~pgain :: List of Top % gainers on the day \n~plose :: List of Top % losers on the day" + "```")
                await self.bot.say("```User made custom Finviz scans-- \n~pummh :: Swing scanner for small caps, over moving averages on daily with consistent volume \n~afiro :: Small cap volatility scanner " + "```")
        else:
            await self.bot.say('Unrecognized command. For options, type ~ragnarok help')
            

def setup(bot):
    n = RagnarokClass(bot)
    bot.add_listener(n.proc_mess, "on_message")
    bot.add_cog(n)
