import discord
import asyncio
from discord.ext import commands
import youtube_dl
import os
from enum import Enum

class Youtube(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if message.content.startswith("dl") or message.content.startswith("download") or message.content.startswith("DL") or message.content.startswith("yt") or message.content.startswith("YT"):
            cmd = str(message.content).split(' ')
            if (cmd[1] == 'mp3' or cmd[1] == '3'):
                content = str(message.content).split(' ')
                url = content[-1]
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                }  
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    info_dict = ydl.extract_info(url, download=False)
                    video_title = info_dict.get('title', None) 
                path = video_title +'.mp3'

                ydl_opts.update({'outtmpl':path})

                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                await message.channel.send(file=discord.File(video_title +'.mp3'))
                os.remove(video_title+'.mp3')
                os.remove(video_title +'.webm')

            elif (cmd[1] == 'mp4' or cmd[1] == '4'):
                content = str(message.content).split(' ')
                url = content[-1]
                if cmd[2] == '0' or cmd[2] == 's' or cmd[2] == 'slient' or cmd[2] == 'off' or cmd[2] == 'false' or cmd[2] == 'f' or cmd[2] == 'F':  
                    download_list = [(url, '137', '136', '135', '134', '133'),]
                else :
                    download_list = [(url, '22', '21', '20', '19', '18'),]
                for cur_data in download_list:
                    cur_url, tuple_format = cur_data[0], cur_data[1:]
                    for format_info in tuple_format:
                        try:
                            video_title = ""
                            with youtube_dl.YoutubeDL(dict(format=format_info, outtmpl=f'%(title)s.%(ext)s', ), ) as ydl:
                                info_dict = ydl.extract_info(url, download=False)
                                video_title = info_dict.get('title', None) 
                            video_title = video_title.replace("/", "")
                            path = video_title +'.mp4'
                            with youtube_dl.YoutubeDL(dict(format=format_info, outtmpl=path)) as ydl:
                                ydl.download([url])
                                try:
                                    await message.channel.send(file=discord.File(video_title +'.mp4'))
                                except discord.errors.HTTPException:
                                    try:
                                        os.remove(video_title+'.mp4')
                                    except:
                                        pass
                                    continue
                            os.remove(video_title+'.mp4')
                            break
                        except youtube_dl.utils.DownloadError:
                            pass


def setup(bot):
    bot.add_cog(Youtube(bot))
