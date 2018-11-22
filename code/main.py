from os import path
import discord
from discord.ext import commands

#import commands
import user_manager

basepath = path.dirname(__file__)
filepath = path.abspath(path.join(basepath, '..', 'token.txt'))

with open(filepath, 'r') as f:
    TOKEN = f.read()
    
global bot
bot = commands.Bot(command_prefix='!', description='placeholder')

# async def on_message(message):

    # ------------------------------------------
    # --------Actions on all messages-----------
    # ------------------------------------------

    # # we do not want the bot to reply to itself
    # if message.author == bot.user:
        # return
        
    # # We don't want the bot to reply to other bots
    # if message.author.bot:
        # return
        
    # Tell people if they do not have a character with each message
  #  if message.author in userlist == False
  #      await user_manager.notonlist
  

    # ------------------------------------------
    # ------------Command list------------------
    # ------------------------------------------


    

# Pretty obvious, if a message starts with "!hello" The bot replie "hello" + message.author.mention
@bot.command(pass_context=True)
async def hello(ctx):
    msg = 'Hello {0.message.author.mention}'.format(ctx)
    await bot.say(msg)
 
# Command to create new character, takes places in user_manager.py
@bot.command(pass_context=True) 
async def create(ctx):
    await user_manager.create(ctx.message, bot)
        
@bot.command() 
async def quit():
    await bot.logout()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

# This conects to discord, on a sucsees it gives the "ready" event
bot.run(TOKEN)