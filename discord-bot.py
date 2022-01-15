import os
from discord.ext import commands
from dotenv import load_dotenv
from knowyourmeme import KnowYourMeme

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

@bot.command(name='knowyourmeme')
async def search(ctx):
    kym = KnowYourMeme() 
    #response = kym.search('pepehands')
    response = kym.random_image()
    await ctx.send(response)

bot.run(TOKEN)
