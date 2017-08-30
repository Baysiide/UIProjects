from discord.ext import commands
from random import choice
from bs4 import BeautifulSoup
import datetime
import requests
from requests.packages.urllib3 import add_stderr_logger
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
        
        
        
        if search_type[0] == "alpha":
            if search_valid == "alpha":
                await self.bot.say("Please add post preference variable")
            else:
                quary = str(ctx.message.content
                            [len(ctx.prefix+ctx.command.name)+7:])
                encode = urllib.parse.quote_plus(quary, encoding='utf-8',
                                                 errors='replace')
                add_stderr_logger()
                s = requests.Session()

                s.headers['User-Agent'] = 'Mozilla/5.0'
    
                url1 = "https://optionalpha.com/wp-login.php"
                values = {'log': 'collinamedee@gmail.com',
                          'pwd': encode}
                r = s.post(url1, data=values)
                url = "https://optionalpha.com/members/watch-list"
                response = s.get(url)
                if encode == "https://optionalpha.com/member-login":
                     await self.bot.say("Variable not found. Please try again")
                else:
                    x = 6
                    html = response.text
                    test = "highiv"
                    indexString = html.find(test)
                    html = html[indexString+10:]
                    
                    indexString = html.find(test)
                    testhtml = html[indexString:]
                
                    nametestStart = testhtml.find("company")
                    nametestEnd = testhtml.find("<", nametestStart)
                    nametestString = testhtml[nametestStart+14:nametestEnd]

                    if nametestString == "Sample Exchange Traded Fund." or nametestString == "Sample Company Name Inc.":
                        x = 0
                        await self.bot.say("Unrecognized preference variable. Please try again.")
                    else:
                        for y in range(0, x):
                            indexString = html.find(test)
                            html = html[indexString:]
                
                            nameStart = html.find("company")
                            nameEnd = html.find("<", nameStart)
                            nameString = html[nameStart+14:nameEnd]
                    
                            symbolStart = html.find("class=\"name\"")
                            symbolEnd = html.find("<", symbolStart)
                            symbolString = html[symbolStart+13:symbolEnd]
                    
                            priceStart = html.find("stockprice")
                            priceEnd = html.find("<", priceStart)
                            priceString = html[priceStart+12:priceEnd]
                     
                            ivStart = html.find(">IV Rank:")
                            ivEnd = html.find("<", ivStart)
                            ivString = html[ivStart+1:ivEnd]
                     
                            stratStart = html.find("serif;\">")
                            stratEnd = html.find("</h3", stratStart)
                            stratString = html[stratStart+8:stratEnd]
                     
                            strattwoStart = html.find("serif;\">", stratEnd)
                            strattwoEnd = html.find("</h3", strattwoStart)
                            strattwoString = html[strattwoStart+8:strattwoEnd]
                        
                            stratthreeStart = html.find("serif;\">", strattwoEnd)
                            stratthreeEnd = html.find("</h3", stratthreeStart)
                            stratthreeString = html[stratthreeStart+8:stratthreeEnd]
                        
                            dayRangeStart = html.find("1 Day Expected Range</h4>")
                            dayRangeEnd = html.find("</h3", dayRangeStart)
                            dayRangeString = html[dayRangeStart+39:dayRangeEnd]
                    
                            weekRangeStart = html.find("1 Week Expected Range</h4>")
                            weekRangeEnd = html.find("</h3", weekRangeStart)
                            weekRangeString = html[weekRangeStart+40:weekRangeEnd]
                     
                            monthRangeStart = html.find("1 Month Expected Range</h4>")
                            monthRangeEnd = html.find("</h3", monthRangeStart)
                            monthRangeString = html[monthRangeStart+41:monthRangeEnd]
                     
                            html = html[monthRangeEnd:]
                            if y == 5:
                                await self.bot.say("**" + nameString + "**  --  **" + symbolString + "**\nPrice: " + priceString + "\n" + ivString + "\n1 Day Range: " + dayRangeString + "\n1 Week Range: " + weekRangeString + "\n1 Month Range: " + monthRangeString + "\n" + stratString + " | " + strattwoString + " | " + stratthreeString)
                            else:
                                await self.bot.say("**" + nameString + "**  --  **" + symbolString + "**\nPrice: " + priceString + "\n" + ivString + "\n1 Day Range: " + dayRangeString + "\n1 Week Range: " + weekRangeString + "\n1 Month Range: " + monthRangeString + "\n" + stratString + " | " + strattwoString + " | " + stratthreeString + "\n -----------------------------------------------------------")
        
        elif search_type[0] == "jaybbsqueeze":
            now = datetime.datetime.now()
            url = "https://swingtradebot.com/events/26/equities?selected_date={}%2F{}%2F{}&min_vol=250000&min_price=1&max_price=10&adx_trend=&grade=&include_etfs=0&html_button=as_html".format(now.month, now.day-1, now.year)
            response = requests.get(url)
            if response.status_code == 404:
                await self.bot.say("Scan not found. Please try again")
            else:
                html = response.text
                indexString = html.find("<tr>")
                html = html[indexString+10:]
                list1 = []
                while html.find("<tr>") != -1:
                    indexString = html.find("<tr>")
                    html = html[indexString:]
                        
                    nameindexStart = html.find("value=")
                    nameindexEnd = html.find(">", nameindexStart)
                    nameString = html[nameindexStart+7:nameindexEnd-1]
                        
                    gradeindexStart1 = html.find("<td class=")
                    html = html[gradeindexStart1:]
                    gradeindexStart = html.find("value=")
                    gradeindexEnd = html.find(">", gradeindexStart)
                    gradeString = html[gradeindexStart+7:gradeindexEnd-1]
                    html = html[gradeindexEnd+4:]
                    
                    percindexStart = html.find("\'>")
                    percindexEnd = html.find("<", percindexStart)
                    percString = html[percindexStart+2:percindexEnd]
                    html = html[percindexEnd+4:]
                    
                    volindexStart = html.find("\'>")
                    volindexEnd = html.find("<", volindexStart)
                    volString = html[volindexStart+2:volindexEnd]
                    html = html[volindexEnd+4:]
                    
                    surgeindexStart = html.find("\'>")
                    surgeindexEnd = html.find("<", surgeindexStart)
                    surgeString = html[surgeindexStart+2:surgeindexEnd]
                    html = html[surgeindexEnd+4:]
                    
                    if float(gradeString) < -69.99:
                        #await self.bot.say(nameString + " " + gradeString + " " + percString + " " + volString + " " + surgeString)
                        list1.append(nameString, gradeString, percString, volString, surgeString)
                    
                await self.bot.say(list1)
                    
        else:
            await self.bot.say('Unrecognized command. Please try again')
            

def setup(bot):
    n = ScrClass(bot)
    bot.add_cog(n)
