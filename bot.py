import discord
from discord.ext import commands

TOKEN = "MTUxMzM0MDcyOTU0MjU3ODI4Ng.G_G8sY.0Itu7PE-tK6q1tKUAf6gAZ_Mzih4INTSSlJoJY"

intents = discord.Intents.default()
intents.members = True  # wajib untuk mendeteksi member baru
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} telah online!")

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="welcome")

    if channel:
        await channel.send(
            f"👋 Selamat datang di **{member.guild.name}**, {member.mention}!\n"
            f"Semoga betah dan jangan lupa baca aturan server ya. 😊"
        )

bot.run(TOKEN)