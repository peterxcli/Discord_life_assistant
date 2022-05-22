import discord
import asyncio
from discord.ext import commands
import random

class Probability(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        content = str(message.content)
        if "機率" in content:
            await message.channel.send(str(random.randint(0, 100))+"%")


def setup(bot):
    bot.add_cog(Probability(bot))
