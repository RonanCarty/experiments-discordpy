import discord
from discord import app_commands
from discord.ext import commands
import requests

class Shorten(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="shorten", description="Shortens a URL with an optional custom alias and password.")
    async def shorten(self, interaction: discord.Interaction, url: str, alias: str = None, max_clicks: int = None, password: str = None) -> None:
        api_url = "https://spoo.me"

        payload = {
            "url": url
        }
        if alias:
            payload["alias"] = alias
        if password:
            payload["password"] = password
        if max_clicks is not None:
            payload["max-clicks"] = max_clicks

        headers = {
            "Accept": "application/json"
        }

        try:
            response = requests.post(api_url, data=payload, headers=headers)

            if response.status_code == 200:
                response_data = response.json()
                short_url = response_data.get('short_url', 'No shortened URL returned.')

                embed = discord.Embed(
                    title="URL Shortened Successfully!",
                    description=f"Shortened URL: {short_url}",
                    color=discord.Color.green()
                )
                embed.add_field(name="Original URL", value=url, inline=False)
                if alias:
                    embed.add_field(name="Alias", value=alias, inline=False)
                if max_clicks is not None:
                    embed.add_field(name="Max Clicks", value=max_clicks, inline=False)
                if password:
                    embed.add_field(name="Password", value=password, inline=False)

                await interaction.response.send_message(embed=embed, ephemeral=True)
            else:
                embed = discord.Embed(
                    title="Error",
                    description=f"Error: {response.status_code}\n{response.text}",
                    color=discord.Color.red()
                )
                await interaction.response.send_message(embed=embed, ephemeral=True)
        except Exception as e:
            embed = discord.Embed(
                title="Exception",
                description=f"An error occurred: {str(e)}",
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Shorten(bot))