import discord
from discord import app_commands
from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="ping", description="Responds with the bot's ping.")
    async def ping(self, interaction: discord.Interaction) -> None:
        
        api_latency = round(self.bot.latency * 1000)
        embed = discord.Embed(title="Latency / Ping", description=f"API Latency: {api_latency}ms",)
        
        if api_latency > 100:
            embed.color = discord.Color.red()
        elif api_latency > 50:
            embed.color = discord.Color.orange()
        else:
            embed.color = discord.Color.green()

        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Ping(bot))
