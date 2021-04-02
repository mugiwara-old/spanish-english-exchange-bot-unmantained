import discord
from discord.ext import commands

class Stats(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def cespr(self, ctx):

    r_esp_native = ctx.guild.get_role(792508900829298688)
    r_esp_c2 = ctx.guild.get_role(826521461182693466)
    r_esp_c1 = ctx.guild.get_role(826532026513227797)
    r_esp_b2 = ctx.guild.get_role(826532138017882192)
    r_esp_b1 = ctx.guild.get_role(826532227029663764)
    r_esp_a2 = ctx.guild.get_role(826532349792747541)
    r_esp_a1 = ctx.guild.get_role(826532406135357452)

    total_r_esp = [
      len(r_esp_native.members),
      len(r_esp_c2.members),
      len(r_esp_c1.members),
      len(r_esp_b2.members),
      len(r_esp_b1.members),
      len(r_esp_a2.members),
      len(r_esp_a1.members)
    ]

    #debug
    #channel = self.bot.get_channel(827612858040582184)
    channel = self.bot.get_channel(827620759487643678)
    
    await channel.edit(name="🦊┃%s" % sum(total_r_esp))
    await ctx.send(sum(total_r_esp))

  @commands.command()
  async def cengr(self, ctx):

    r_eng_native = ctx.guild.get_role(792503398036406282)
    r_eng_c2 = ctx.guild.get_role(826521558037561454)
    r_eng_c1 = ctx.guild.get_role(826532629775384626)
    r_eng_b2 = ctx.guild.get_role(826532809886793738)
    r_eng_b1 = ctx.guild.get_role(826532912013770802)
    r_eng_a2 = ctx.guild.get_role(826533069649477654)
    r_eng_a1 = ctx.guild.get_role(826533128423473173)

    total_r_eng = [
      len(r_eng_native.members),
      len(r_eng_c2.members),
      len(r_eng_c1.members),
      len(r_eng_b2.members),
      len(r_eng_b1.members),
      len(r_eng_a2.members),
      len(r_eng_a1.members)
    ]

    #debug
    #channel = self.bot.get_channel(827612879963291658)
    channel = self.bot.get_channel(827621040607461446)
  
    await channel.edit(name="🐬┃%s" % sum(total_r_eng))
    await ctx.send(sum(total_r_eng))

def setup(bot):
  bot.add_cog(Stats(bot))