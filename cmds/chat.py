import discord
import asyncio
from discord.ext import commands
import random

from matplotlib.pyplot import flag
from cmds.cmdsBase.chatBase.const import *
from cmds.cmdsBase.chatBase.loadfile import *
from cmds.cmdsBase.chatBase.model import *
from cmds.cmdsBase.chatBase.train import *
from cmds.cmdsBase.chatBase.utils import *
from cmds.cmdsBase.chatBase.voc_class import *
# from google_trans_new import google_translator 
import googletrans 

class Chat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # self.translator = google_translator()  
        self.translator = googletrans.Translator()
        self.flag = 1

    @commands.Cog.listener()
    async def on_message(self, message):
        if "switch" == message.content:
            if self.flag == 1:
                self.flag = 0
                await message.channel.send("switch to zh-tw")
            else :
                self.flag = 1
                await message.channel.send("switch to en")
            return
        if message.content.startswith("!"):
            return
        if message.author.bot:
            return
        if "點" == message.content:
            return
        if message.attachments:
            return
        if(len(message.mentions)):
            return
        # print(message.mentions)
        if (random.randint(1, 3)) :
            inputseq = str(message.content)
            print(inputseq)
            # inputseq = self.translator.translate(inputseq, lang_tgt='en')
            inputseq = self.translator.translate(inputseq, dest='en').text
            print(inputseq)
            outputseq = ""
            try:
                for word in reply(encoder, decoder, searcher, voc, inputseq):
                    outputseq += word+" "
                print(outputseq)
                if self.flag == 1:
                    outputseq = self.translator.translate(outputseq, dest='en').text
                else:
                    outputseq = self.translator.translate(outputseq, dest='zh-tw').text
                # outputseq = self.translator.translate(outputseq, lang_tgt='zh-tw')
                
                print(outputseq)
                outputseq = re.sub('。', '', outputseq)
                await message.channel.send(outputseq)
                
            except KeyError:
                # outputseq = "りしれ供さ小"
                # await message.channel.send(file=discord.File("Li_si_leh_kong_sann_siau_.jpg"))
                pass
            
            


def setup(bot):
    bot.add_cog(Chat(bot))
