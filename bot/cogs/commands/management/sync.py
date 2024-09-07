import discord
import asyncio
from discord.ext import commands

class Sync(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    ## This command can only be run by the OWNER of the Discord Application - This is a TEXT COMMAND.
    @commands.command(name="sync", hidden=True)
    @commands.is_owner()
    async def sync(self, ctx):
        try:
            await ctx.message.delete()
            await self.bot.tree.sync()
            message = await ctx.send("Successfully synced slash commands.")
            await asyncio.sleep(5)
            await message.delete()
        except discord.HTTPException as e:
            await ctx.send(f"Failed to sync commands: {e}")
            await asyncio.sleep(5)
            await message.delete()

    @sync.error
    async def sync_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.message.delete()
            message = await ctx.send("You are not authorized to use this command!")
            await asyncio.sleep(5)
            await message.delete()
        else:
            await ctx.send(error)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Sync(bot))