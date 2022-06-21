import requests
from discord.ext import commands
import discord


def get_joke():
    response = requests.get("https://meme-api.herokuapp.com/gimme").json()
    data = response
    return data


class meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(self, ctx):
        joke = get_joke()
        print(joke["nsfw"])
        print(joke["url"])
        imgdat = joke["url"]
        embed = discord.Embed(title="MeMe!", color=discord.Color.purple())
        embed.set_image(url=imgdat)
        embed.set_footer(text="Hello amigos its A Meme!")
        await ctx.channel.send(embed=embed)
