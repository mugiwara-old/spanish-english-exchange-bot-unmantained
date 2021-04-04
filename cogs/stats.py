import discord
from discord.ext import commands

class Stats(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    

  @commands.command()
  async def cespr(self, ctx):
    roles = (792508900829298688, 826521461182693466, 826532026513227797,
             826532138017882192, 826532227029663764, 826532349792747541, 826532406135357452)
    total = 0
    
    for role in roles:
      total += len(ctx.guild.get_roles(role).members)

    channel = self.bot.get_channel(827620759487643678)
    await channel.edit(name = f"🦊┃{total}")
    await ctx.send(sum(total))
    

  @commands.command()
  async def cengr(self, ctx):
    roles = (792503398036406282, 826521558037561454, 826532629775384626,
            826532809886793738, 826532912013770802, 826533069649477654, 826533128423473173)
    total = 0
    
    for role in roles:
      total += len(ctx.guild.get_roles(role).member)
      
    channel = self.bot.get_channel(827621040607461446)
    await channel.edit(name = f"🐬┃{total}")
    await ctx.send(sum(total))

def setup(bot):
  bot.add_cog(Stats(bot))
