import discord
from discord.ext import commands
import json
import os
import keep_alive


intents = discord.Intents.default()
intents.members = True

with open('setting.json', mode='r', encoding='utf8')as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='/', intents = intents)

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

@bot.event
async def on_ready():
    print(">>Bot is online<<")
    channel = bot.get_channel(726771704466243598)
    await channel.send("I'm running")
if __name__ == "__main__":
    keep_alive.keep_alive()
    bot.run(jdata['Token1']+jdata['Token2'])


