from discord.ext import commands
import discord
import json
import asyncio
prefix = "!"
token = "token-here"
#token here - go in inspect element -> local storage -> filter items -> type token -> control r to reload -> see it and copy it (QUICKLY)
#tokens give access to your account - avoid anyone asking for your token or files that seem to send your token over a webhook
#changing your password should reset your token.

client = commands.Bot(prefix, self_bot=True)

count = 0
@client.event
async def on_message(ctx):
	global count
	if ctx.author.id == client.user.id:
		count = count + 1
		print(f"[{count}] Editing {ctx.content}")
		try:
			message = ctx
			await message.edit(content=f"{ctx.content} ")
			print(f"[{count}] Edited {ctx.content}")
		except:
			print(f"[{count}] Error Editing {ctx.content}")
client.run(token, bot=False)
