import logging
import json
import requests
from bs4 import BeautifulSoup
import hashlib
import websiteTrackingSqlite
import discord
from discord.ext import commands

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:˓→%(message)s'))
logger.addHandler(handler)


#TODO: reformat permissions, Figure this out
with open('config.json', 'r') as f:
    config = json.load(f)


bot = commands.Bot(command_prefix=['!!','Good b', 'Good B', 'Shutdown p'], description='testing')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-----------')

#Bot reactions, Personality

#Good bot response
@bot.command(pass_context = True)
async def ot(ctx):
    msg = []
    async for x in bot.logs_from(ctx.message.channel, limit = 2):
        msg.append(x)
    previous_message_author = msg[-1].author
    if "BestBot" in previous_message_author.name and previous_message_author.bot:
        await bot.send_message(ctx.message.channel, 'Thank you!')
        #respond with reaction gif Happy
    #else:
        #if "BestBot" not in previous_message_author.name and previous_message_author.bot:
            #TODO: Wait for response from other bot
            #asyncio.sleep(1)
            #msg = []
            #async for x in bot.logs_from(ctx.message.channel, limit=2):
            #    msg.append(x)
            #if "Thank" not in msg[-1].content or "thank" not in msg[-1].content:
            #await bot.send_message(ctx.message.channel, '@{0.name} Say thank you!'.format(previous_message_author))

#Bad bot response?
#Responding to random phrases
#Maybe respond to nicknames?



#Recipe
        #TODO: Create Recipe JSON

#Remove Recipe
    # Check permissions
    #Validate (!RemoveRecipe Name)
    #Check if name exists
    #Update JSON

#Add Recipe
    #Check permissions
    #Validate input (!AddRecipe Name Type URL)
        #Make Sure URL is valid
    #?Maybe add who added the recipe?
    #Update JSON

#Recall recipe
    #Check permissions
    #Validate input (!Recipe OptionalType) (!Recipe Name) (!Recipe)
    #If type Recall random recipe of type
    #Else Recall random recipe



#Check website for changes, @user when it's changed, stop tracking unless user responds

#whisper or @test  !!whisper

#Add time, user, and website to db !!track https://....
@bot.command(pass_context = True)
async def track(ctx, url):
    #check if valid site
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
        #report if no data returned
    soup = BeautifulSoup(response.text, "html.parser")
    currentHash = hashlib.sha224(soup.encode("utf-8")).hexdigest()
    print("Got hash of {}".format(url))
    #if no local db, create sqllite db with ID, User, Site, Hash, Active
    
    #if loop is not running to check for site updates, start loop
        
        #download hash



#Recall which sites are assigned to user



#Remove site tracking for user




#Reaction GIF
        #TODO: Create Reaction gif JSON



#Add Reaction
    #Check permissions
    #Validate input(!AddReaction Name URL OptionalMood)
    #Validate URL
    #Make sure name isn't already taken by name or mood
    #Update JSON
    #Let user know it's been added (By whisper? or post?)

#Remove Reaction
    #Check permissions
    #Validate Input(!RemoveReaction Name)
    #Check if name exists
    #Update JSON

#Recall Reaction
    #Check permissions
    #Validate Input (!!Name or !!Mood)
    #Check if mood exists
        #Post Random gif from mood
    #Else check if name exists
        #Post Reaction



#Utility

#Shutdown
@bot.command(pass_context = True)
async def ls(ctx):
    msg = []
    async for x in bot.logs_from(ctx.message.channel, limit=1):
        msg.append(x)
    command_author = msg[0].author
    if  command_author.name in config["admin"]:
        await bot.send_message(ctx.message.channel, 'Shutting down!')
        raise SystemExit
    else:
        await bot.send_message(ctx.message.channel, 'You\'re not an admin!')

#Update Permissions

#Check Permissions
    #Whisper @user, Maybe check for specific functions?

#Uptime

#Figure out a restart function

#Help

#Commands

#Moods

#Function for Contributor/Admin check
    #Make sure someone is actually allowed to use bot functions
    #Selective (Each bot function should have a permissions value? Something equivalent
        # Admin Contributor User Banned)?



bot.run(config["bot_token"])
