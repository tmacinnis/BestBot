import logging
import json
import time
import asyncio
import discord
from discord.ext import commands

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:˓→%(message)s'))
logger.addHandler(handler)

with open('config.json', 'r') as f:
    config = json.load(f)

bot = commands.Bot(command_prefix=['Good b', 'Good B', 'Shutdown p'], description='testing')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-----------')

@bot.command(pass_context = True)
async def ot(ctx):
    msg = []
    async for x in bot.logs_from(ctx.message.channel, limit = 2):
        msg.append(x)
    previous_message_author = msg[-1].author
    if "BestBot" in previous_message_author.name and previous_message_author.bot:
        await bot.send_message(ctx.message.channel, 'Thank you!')
    else:
        if "BestBot" not in previous_message_author.name and previous_message_author.bot:
            #TODO: Wait for response from other bot
            #asyncio.sleep(1)
            #msg = []
            #async for x in bot.logs_from(ctx.message.channel, limit=2):
            #    msg.append(x)
            #if "Thank" not in msg[-1].content or "thank" not in msg[-1].content:
            await bot.send_message(ctx.message.channel, '@{0.name} Say thank you!'.format(previous_message_author))


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

bot.run(config["bot_token"])
