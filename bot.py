BOT_PREFIX = "Bot prefix"
BOT_TOKEN = "Bot Token"
channel = "You Channel Id"
import asyncio
import nextcord
from nextcord.ext import commands
import requests
import json
bot = commands.Bot(command_prefix=BOT_PREFIX, intents=nextcord.Intents.all())

async def anime():
    while True:
        d = requests.get(f'https://api.waifu.pics/sfw/bite').json() #https://waifu.pics/docs
        anime = d['url']
        embed=nextcord.Embed(title=f'Anime Bite', color=0x01ad43)
        embed.set_image(url=(anime))
        embed.set_footer(text="< Black / Eye > ™")
        await bot.get_channel(971317753497665566).send(embed=embed)
        await asyncio.sleep(900)
    
@bot.event
async def on_ready():
    print("Logged in as", bot.user.name)
    bot.remove_command('help')
    bot.loop.create_task(anime())


bot.run(BOT_TOKEN)
