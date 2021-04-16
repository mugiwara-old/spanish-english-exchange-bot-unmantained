from discord.ext import commands

class Perms(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def perms(self, ctx, arg):
    arg = int(arg)
    role = ctx.guild.get_role(arg)

    if role == None:
      await ctx.channel.send("That's not a valid role ID!")
      return

    roles_dict = {}

    for tuple in role.permissions:
      roles_dict[tuple[0]] = tuple[1]

    print(roles_dict)

    await ctx.channel.send(roles_dict)

def setup(bot):
  bot.add_cog(Perms(bot))