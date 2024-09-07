import os
import discord
import asyncio
from datetime import datetime
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


class Experiments(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=".",
            intents=discord.Intents.all(),
            application_id=1282025193727987865,
        )

    async def on_ready(self):
        print(" ")
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} [INFO] {self.user} ({self.user.id}) Connected to Discord!")
        print(" ")

    async def load_cogs(self):
        for root, dirs, files in os.walk("cogs"):
            for file in files:
                if file.endswith(".py"):
                    cog_path = os.path.join(root, file)
                    cog_module = cog_path.replace(os.sep, ".")[:-3]
                    await self.load_extension(cog_module)

bot = Experiments()
asyncio.run(bot.load_cogs())
bot.run(DISCORD_TOKEN)