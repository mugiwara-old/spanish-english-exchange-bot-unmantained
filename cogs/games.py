import random

from discord.ext import commands

class Games(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(brief="Either Heads or Tails")
  async def coin(self, ctx):
    n = random.choice(("Heads", "Tails"))
    await ctx.send(n)

  @commands.command(brief="¿Cara o cruz?")
  async def moneda(self, ctx):
    n = random.choice(("Cara", "Cruz"))
    await ctx.send(n)

def setup(bot):
  bot.add_cog(Games(bot))
