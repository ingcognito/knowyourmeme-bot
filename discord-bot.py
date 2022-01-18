import os
from discord.ext import commands
from dotenv import load_dotenv
from knowyourmeme import KnowYourMeme

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

# get input working here? how do you parse
@bot.command(name='knowyourmeme')
async def search(ctx, arg):
    kym = KnowYourMeme() 
    response = kym.search(arg)
    #print('{} arguments: {}'.format(len(args), ', '.join(args)))
    #response = kym.random_image()
    await ctx.send(response)

bot.run(TOKEN)
