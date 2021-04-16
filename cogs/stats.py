from discord.ext import commands
from guild.model import Guild

see_guild = Guild

class Stats(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command()
  async def cespr(self, ctx):
    if not (ctx.channel.id == 814455624006893609 or ctx.channel.id == 827612879963291658):
      await ctx.channel.send("Sorry, you can't use this command in this channel!")
      return

    see_guild_es_roles = see_guild.roles("es")
    total_role_members = len(ctx.guild.get_role(see_guild_es_roles['ns']).members)

    channel = self.bot.get_channel(827620759487643678)
    msg = "We are %s 🦊 Spanish native speakers" % total_role_members
    
    await channel.edit(name = f"🦊┃{total_role_members}")
    await ctx.send(msg)
    

  @commands.command()
  async def cengr(self, ctx):
    if not (ctx.channel.id == 814455624006893609 or ctx.channel.id == 827612858040582184):
      await ctx.channel.send("Sorry, you can't use this command in this channel!")
      return

    see_guild_en_roles = see_guild.roles("en")
    total_role_members = len(ctx.guild.get_role(see_guild_en_roles['ns']).members)
      
    channel = self.bot.get_channel(827621040607461446)
    msg = "We are %s 🐬 English native speakers" % total_role_members

    await channel.edit(name = f"🐬┃{total_role_members}")
    await ctx.send(msg)

def setup(bot):
  bot.add_cog(Stats(bot))