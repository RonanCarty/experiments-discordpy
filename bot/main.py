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
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} [INFO] {self.user} ({self.user.id}) Connected to Discord!")

    async def load_cogs(self):
        cog_directory = os.path.join(os.path.dirname(__file__), 'cogs')
        for root, dirs, files in os.walk(cog_directory):
            for file in files:
                if file.endswith(".py") and not file.startswith("__"):
                    cog_path = os.path.join(root, file)
                    relative_path = os.path.relpath(cog_path, cog_directory)
                    cog_module = relative_path.replace(os.path.sep, ".").replace(".py", "")
                    try:
                        await self.load_extension(f"cogs.{cog_module}")
                    except Exception as e:
                        print(f"Failed to load module {cog_module}: {e}")

bot = Experiments()
asyncio.run(bot.load_cogs())
bot.run(DISCORD_TOKEN)