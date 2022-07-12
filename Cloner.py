mytitle = "forked by risq from a deleted repo"
from os import system
system("title "+mytitle)
import psutil
from pypresence import Presence
import time
import sys
client_id = '891955385903226880'
RPC = Presence(client_id,pipe=0)
RPC.connect()
start_time=time.time()
RPC.update(start=start_time, state=f"Cloning a server!",large_image="lua", large_text="Made byMade by risq",
            small_image="me", small_text="https://discord.gg/Fg5fekmpKC",buttons=[{"label": "Join Server", "url": "https://discord.gg/Fg5fekmpKC"}])
import discord
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
from serverclone import Clone

client = discord.Client()
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
print(f"""{Fore.WHITE}
                             ▄████▄   ██▓    ▒█████   ███▄    █  ▓█████
                            ▒██▀ ▀█  ▓██▒   ▒██▒  ██▒ ██ ▀█   █  ▓█   ▀
                            ▒▓█    ▄ ▒██░   ▒██░  ██▒▓██  ▀█ ██▒ ▒███  
                            ▒▓▓▄ ▄██ ▒██░   ▒██   ██░▓██▒  ▐▌██▒ ▒▓█  ▄
                            ▒ ▓███▀ ▒░██████░ ████▓▒░▒██░   ▓██░▒░▒████
                            ░ ░▒ ▒  ░░ ▒░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░░ ▒░ 
                            ░  ▒  ░░ ░ ▒    ░ ▒ ▒░ ░ ░░   ░ ▒░░ ░ ░  
                            ░          ░ ░  ░ ░ ░ ▒     ░   ░ ░     ░  
                            ░ ░     ░    ░      ░ ░           ░ ░   ░  
                            {Fore.LIGHTYELLOW_EX}Made by risq | https://discord.gg/Fg5fekmpKC{Style.RESET_ALL}                                
{Style.RESET_ALL}              
        """)
token = input(f'[>]  Token:')
guild_s = input('\n[>]  Server ID:')
guild = input('\n[>]  Enter Guild ID Where You Want to Copy:')
input_guild_id = guild_s  # <-- input guild id
output_guild_id = guild  # <-- output guild id
token = token  # <-- your token


print("  ")
print("  ")

@client.event
async def on_ready():
    extrem_map = {}
    print(f"Logged In as : {client.user}")
    print("Cloning Server")
    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)
    print(f"""{Fore.GREEN}

 ██████╗ ██████╗ ███╗   ███╗██████╗ ██╗     ███████╗████████╗███████╗██████╗ 
██╔════╝██╔═══██╗████╗ ████║██╔══██╗██║     ██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██║     ██║   ██║██╔████╔██║██████╔╝██║     █████╗     ██║   █████╗  ██║  ██║
██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝     ██║   ██╔══╝  ██║  ██║
╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ███████╗███████╗   ██║   ███████╗██████╔╝
 ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═════╝ 
    {Style.RESET_ALL}""")
    await asyncio.sleep(5)
    client.close()


client.run(token, bot=False)