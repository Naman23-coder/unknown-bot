from discord.ext import commands
import os


class Bot(commands.Bot):
  def __init__(self) -> None:
    pass
  
  async def setup_hook(self) -> None:
    async for filename in os.listdir('./cogs'):
      if filename.endswith('.py'):
          await bot.load_extension(f'cogs.{filename[:-3]}')
 
