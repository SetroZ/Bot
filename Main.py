from Variables import *
from discord.ext import commands
import discord
import requests
import json
import time

client=commands.Bot(command_prefix=".")


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data =json.loads(response.text)
    quote=json_data[0]['q']+" -"+json_data[0]['a']
    return(quote)





@client.event
async def on_ready():
    print("Ready")


@client.command()
async def inspire(ctx):
    quote=get_quote()
    await ctx.send(quote)


@client.command()
async def Hello(ctx):
    await ctx.send("Hi")

@client.command()
async def rules(ctx):
    await ctx.send(Rules)

@client.command()
async def send(ctx):
    await ctx.send(".rule")

@client.command()
async def rule(ctx,*,number):
    await ctx.send(R[int(number)-1])

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx,amount=2):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"Deleted {amount} messages")




@client.command()
@commands.has_permissions(manage_messages=True)
async def clear_all (ctx,amount=99999999):
    await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick (ctx,member : discord.Member,*,reason= "No reason provided"):
    await member.send(f"You have been Kicked , Because {reason}")
    await member.kick(reason=reason)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban (ctx,member : discord.Member,*,reason= "No reason provided"):
    try:
        await member.send(f"You have been banned, Because {reason}\n {b}")
    except:
        print("")
    finally:
        await ctx.send(f"{member} has been banned \n {b}")
        await member.ban(reason=reason)

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx,*,member):
    banned_users=await ctx.guild.bans()
    member_name,member_disc=member.split('#')
    for banned_entry in banned_users:
        user=banned_entry.user
        if(user.name,user.discriminator)==(member_name,member_disc):

            await ctx.guild.unban(user)
            await ctx.send(member_name +" has been unbanned!")
            return
    await ctx.send(member+ " was not found")
@client.command()
async def hamza(ctx):
    await ctx.send("bobux2")













client.run("ODE3NDI2Njg5ODQ3NTkwOTQy.YEJV7Q.ipacP1z1hOny_-_APRNA0kHaRKg")