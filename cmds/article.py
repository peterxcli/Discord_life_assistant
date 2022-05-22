import discord
import asyncio
from discord.ext import commands
import random

class Article(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        


def setup(bot):
    bot.add_cog(Article(bot))
