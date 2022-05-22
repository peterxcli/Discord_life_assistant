import discord
import asyncio
from discord.ext import commands
import random

class Sample(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        content = str(message.content)
        if "點" == content:
            await message.channel.send(str(random.randint(1, 30)))


def setup(bot):
    bot.add_cog(Sample(bot))
