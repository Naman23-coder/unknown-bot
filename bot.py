from discord.ext import commands
import os
import discord
from cogs.balance import Balance
from cogs.meme import meme

token = os.environ.get("db")

# from dotenv import load_dotenv


class Bot(commands.Bot):
    def __init__(self, command_prefix="?", intents=discord.Intents.all()) -> None:
        super().__init__(command_prefix, intents=intents)

    async def setup_hook(self) -> None:
        await self.add_cog(Balance(bot))
        await self.add_cog(meme(bot))


bot = Bot()


@bot.event
async def on_ready():
    print("running")


bot.run(token=token)
