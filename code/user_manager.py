# tools to manage users and characters
import discord
import json
from discord.ext import commands
from strings import strings

#loads a list of users ID
with open('users.json') as f:
    userlist = json.load(f)


#bot = commands.Bot(command_prefix='!', description='placeholder')


# -----------------------------------------
# -----------Functions---------------------
# -----------------------------------------


def jdefault(o):
    return o._asdict()
    

    
# Function to create a new character
async def create(message, bot):
    if not message.author.id in userlist:
        userlist.append(message.author.id)
        await saveusers(userlist)
        print(message.author.name + ' has been added to userlist')
        await bot.send_message(message.channel, strings['newuser']['eng'])

# Saves the list of users to user.json, should be done eveytime userlist is modified        
async def saveusers(userlist):
    with open("users.json", mode = "w") as f:
        f.write(json.dumps(userlist))    
        
        
        
# -----------------------------------------
# -----------Classes-----------------------
# -----------------------------------------

#Using the swedish for user to avoid conflict with discord.py 
# not in use currently
class anvandare:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.language = 'unknown'
        self.characters = 'None'
    
    
    
