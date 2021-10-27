#Author: Max Hsu

import discord 
from discord.ext import commands
from core.classes import Cog_Extension
import json, asyncio, datetime

with open('setting.json', 'r', encoding = 'UTF-8') as jfile:
    jdata = json.load(jfile)
    #'r' means open the file for read only.

class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = 0

        async def time_task():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(726771704466243598)
            while not self.bot.is_closed():
                now_time = datetime.datetime.now().strftime('%H%M')
                if now_time == jdata['time'] and self.counter == 0:
                    await self.channel.send(jdata['reminder'])
                    self.counter = 1
                    await asyncio.sleep(1) #second
                else:
                    await asyncio.sleep(1) #second
                    pass

        self.bg_task = self.bot.loop.create_task(time_task())

    @commands.command()
    async def set_channel(self, ctx, ch: int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'Set channel{self.channel.mention}')

    @commands.command()
    async def remind(self, ctx, time, *, reminder):

        self.counter = 0

        with open('setting.json', 'r', encoding = 'UTF-8') as jfile:
            jdata = json.load(jfile)
            #'r' means open the file for read only. 
        jdata['time'] = time
        jdata['reminder'] = reminder

        with open('setting.json', 'w', encoding = 'UTF-8') as jfile:
            json.dump(jdata, jfile, indent = 4)
            #'w' means write something into the file.

        if jdata['time'] == time:
            await ctx.send("Set reminder successfully.")

def setup(bot):
    bot.add_cog(Task(bot))
