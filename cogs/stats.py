import discord
from discord.ext import commands

class Stats(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    

  @commands.command()
  async def cespr(self, ctx):
    channel = self.bot.get_channel(827620759487643678)
    total = len(ctx.guild.get_role(792508900829298688).members)
    
    await channel.edit(name = f"🦊┃{total}")
    await ctx.send(total)
    

  @commands.command()
  async def cengr(self, ctx):
    channel = self.bot.get_channel(827621040607461446)
    total = len(ctx.guild.get_role(792503398036406282).members)
    
    await channel.edit(name = f"🐬┃{total}")
    await ctx.send(total)

def setup(bot):
  bot.add_cog(Stats(bot))
