#Author: Max Hsu

import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random

with open('setting.json', 'r', encoding = 'UTF-8') as jfile:
    jdata = json.load(jfile)
    #'r' means open the file for read only.

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):      
        print(f'{member}join!')
        channel = self.bot.get_channel(int(jdata['Channel_Welcome']))
        await channel.send(f'歡迎{member}')
        #When somebody joined.

    @commands.Cog.listener()
    async def on_member_remove(self, member):    
        print(f'{member}left!')
        channel = self.bot.get_channel(int(jdata['Channel_Leave']))  
        await channel.send(f'{member}滾拉')
        #When somebody left.
    @commands.Cog.listener()
    async def on_reaction_add(self,reaction,user):
        channel = self.bot.get_channel(int(jdata['Channel_Welcome']))
        await channel.send('{0} has reacted with {1.emoji}!'.format(user, reaction))



def setup(bot):
    bot.add_cog(Event(bot))