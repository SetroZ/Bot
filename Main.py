from Rules import *

from discord.ext import commands
from discord import *
import requests
import json

client = commands.Bot(command_prefix=".")


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


@client.event
async def on_ready():
    print("Ready")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission")
        await ctx.message.delete()
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please provide all required arguments")
        await ctx.message.delete()
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send(embed=discord.Embed(title="Not Found", description="User was not found", color=Color.red()))
        await ctx.message.delete()
    else:
        raise error


@client.command()
async def inspire(ctx):
    quote = get_quote()
    await ctx.send(quote)


@client.command()
async def Hello(ctx):
    await ctx.send("Hi")


@client.command()
async def rules(ctx):
    em = discord.Embed(title="Rules", description=Rules, color=Color.red())
    await ctx.send(embed=em)


@client.command()
async def rule(ctx, *, number):
    em = discord.Embed(title="Rules", description=R[int(number) - 1], color=Color.blue())
    await ctx.send(embed=em)


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"Deleted {amount} messages")


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear_all(ctx, amount=99999999):
    await ctx.channel.purge(limit=amount)


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="No reason provided"):
    await member.send(f"You have been Kicked , Because {reason}")
    await member.kick(reason=reason)
    em = discord.Embed(title="Kicked", description=member + " Has been Kicked!", color=Color.red())
    await ctx.send(embed=em)


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="No reason provided"):
    try:
        await member.send(f"You have been banned, Because {reason}\n {b}")
    except:
        print("")
    finally:
        em = discord.Embed(title="Banned", description=f"{member} has been banned \n ", color=Color.red())
        await ctx.send(embed=em)
        await ctx.send(b)
        await member.ban(reason=reason)


@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')
    for banned_entry in banned_users:
        user = banned_entry.user
        if (user.name, user.discriminator) == (member_name, member_disc):
            await ctx.guild.unban(user)
            em = discord.Embed(title="Unbanned", description=member_name + " Has been unbanned!", color=Color.red())
            await ctx.send(embed=em)
            return
    await ctx.send(embed=discord.Embed(title="Not Found", description=member + " was not found", color=Color.red()))


mute_role = False


@client.command()
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member):
    muted = ctx.guild.get_role(821972019176144977)
    await member.add_roles(muted)
    global mute_role

    if mute_role == True:
        em = discord.Embed(title="Mutes", description=member.mention + " Is already muted", color=Color.green())
        await ctx.send(embed=em)
    else:
        mute_role = True
        em = discord.Embed(title="Mutes", description=member.mention + " Has Been Muted", color=Color.green())
        await ctx.send(embed=em)


@client.command()
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member):
    muted = ctx.guild.get_role(821972019176144977)
    await member.remove_roles(muted)
    global mute_role
    if mute_role == False:
        em = discord.Embed(title="Mutes", description=member.mention + " Is already unmuted", color=Color.green())
        await ctx.send(embed=em)
    else:
        mute_role = False
        em = discord.Embed(title="Mutes", description=member.mention + " Has been unmuted", color=Color.green())
        await ctx.send(embed=em)


client.run("ODE3NDI2Njg5ODQ3NTkwOTQy.YEJV7Q.ipacP1z1hOny_-_APRNA0kHaRKg")
