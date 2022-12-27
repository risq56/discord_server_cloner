mytitle = "made by risq"
from os import system
system("title "+mytitle)
import psutil
from pypresence import Presence
import time
import sys
client_id = '1057279162785747015'
RPC = Presence(client_id,pipe=0) 
RPC.connect()
start_time=time.time()
RPC.update(start=start_time, state=f"Cloning a server!",large_image="logo", large_text="Made by risq",
            small_image="img", small_text="https://discord.gg/ngcsuUEd")#,buttons=[{"label": "aaaaaaaa", "url": "https://youtube.com"},{"label": "aaaaaaaa", "url": "https://youtube.com"}])
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
    print("1")
    guild_to = client.get_guild(int(output_guild_id))
    print("2")
    await Clone.guild_edit(guild_to, guild_from)
    print("3")
    await Clone.roles_delete(guild_to)
    print("4")
    await Clone.channels_delete(guild_to)
    print("5")
    await Clone.roles_create(guild_to, guild_from)
    print("6")
    await Clone.categories_create(guild_to, guild_from)
    print("7")
    await Clone.channels_create(guild_to, guild_from)
    print("8")
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