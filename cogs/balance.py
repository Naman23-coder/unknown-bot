from discord.ext import commands
import discord
from db.dbmanager import *
from utils import *


class Balance(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="bal")
    async def balance(self, ctx):
        # if ctx == "":
        user = ctx.author.id
        # else:
        #     user = await self.bot.fetch_user(ctx)

        if await user_exist(user):
            embed = discord.Embed(title=f"""{ctx.author.name}'s balance""")
            embed.add_field(name="pocket", value=await get_balance(user))
            embed.add_field(name="bank", value=await get_bank_balance(user))
            embed.add_field(name="net worth", value=await get_networth(user))
            await ctx.channel.send(embed=embed)
        else:
            await ctx.channel.send("hello")


async def setup(bot):
    await bot.add_cog(Balance)
