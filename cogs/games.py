import random

from discord.ext import commands

class Games(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(brief="Either Heads or Tails")
  async def coin(self, ctx):
    n = random.randint(0, 1)
    await ctx.send("Heads" if n == 1 else "Tails")

  @commands.command(brief="¿Cara o cruz?")
  async def moneda(self, ctx):
    n = random.randint(0, 1)
    await ctx.send("Cara" if n == 1 else "Cruz")

def setup(bot):
  bot.add_cog(Games(bot))