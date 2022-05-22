import discord
from datetime import datetime,timezone,timedelta
from discord.ext import commands
from core.classes import Cog_Extension
import random
import asyncio

class main(Cog_Extension):
    @commands.command()
    async def ping(self, ctx):                  
        await ctx.send(f'{round(self.bot.latency * 1000)}(ms)') 
        #When somebody send "~ping", bot return it's latency to the communicating place.

    @commands.command()
    async def load(self, ctx, extension):
        self.bot.load_extension(f'cmds.{extension}')
        await ctx.send(f'Loaded {extension} successfully.')

    @commands.command()
    async def unload(self, ctx, extension):
        self.bot.unload_extension(f'cmds.{extension}')
        await ctx.send(f'Unload {extension} successfully.')

    @commands.command()
    async def reload(self, ctx, extension):
        self.bot.reload_extension(f'cmds.{extension}')
        await ctx.send(f'Reloaded {extension} successfully.')

    
    @commands.command()
    async def rand_squad(self,ctx, number :int):
        group = []

        groups = []
        """for future in asyncio.as_completed(ctx.guild.fetch_members(limit=None)):
            member = await future
            if str(member.status) == 'online' and member.bot == False:
                online.append(member)"""
        online = await ctx.guild.fetch_members(limit=None).flatten()
        member = len(online)
        group_ids = random.sample(online, k=int(member))
        embed=discord.Embed(title="Team", color=0xaa18a5)
        for i in range(member):
            for j in range(number):
                group.append(j)
                print(len(group))
                if len(group) >= member:
                    break
            if len(group) >= member:
                break
        for l in range(number):
            groups.append([])
            for n in range(member):
                if group[n] == l:
                    groups[l].append(group_ids[n])
            embed.add_field(name= l+1, value= groups[l] , inline=False)
        await ctx.send(embed=embed)

    
def setup(bot):
    bot.add_cog(main(bot))


