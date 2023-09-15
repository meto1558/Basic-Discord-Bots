"""
Welcome! This is basic Python Discord bot. (I use nextcord, I think nextcord is better than discord.py.) Good work!
This repository is created by mEt0_. Concact me (Discord): meto1558
"""

import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix="YOUR_COMMAND_PREFIX_HERE", intents=nextcord.Intents.all())

# Bot's ready listener
@bot.event
async def on_ready():
    print("Bot is ready!")

# Command errors listener
@bot.event
async def on_command_error(error, ctx: commands.Context): # Type definition
    # Catch Command Errors
    if isinstance(error, commands.CommandError):
        return await ctx.send("An error occurred in the commands.")
    # Catch Command not defined on your bot
    if isinstance(error, commands.CommandNotFound):
        return await ctx.send("I'm not find this command.")
    # And more...

# Message create listener (i think you use @bot.command listener)
@bot.event
async def on_message(message: nextcord.Message): # Type definition
    # Check if the message owner is a bot
    if (message.author.bot):
        return
    # Check what is written in the resulting message
    if (message.content.lower() == "hello"):
        return await message.reply("Hi!")
    # And more...

# Yeah, we finally got to the part of adding commands to the bot

# Bot's prefix based command builder listener
@bot.command() # If you do not enter a name in the name parameter, the function name is automatically assumed to be the name of the command
async def yo(ctx: commands.Context): # Type definition
    await ctx.send("Hello, how are you?")

# Connect to Discord Gateway
bot.run("YOUR_BOT_TOKEN_HERE")

# Finally, run the bot, use this command: python your_file_name.py (REQUIRED: Python 3.8 or higher, pip Package Manager)