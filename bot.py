import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.lower() == ".psc":
        await message.channel.send(
            """💳 **You want to pay with Paysafe?**

Before sending your codes, please check them here to make sure you copied them correctly:
https://www.paysafecard.com/en-gb/balance-check/

⚠️ The codes are **not sent to the ticket**. They are only sent via DM to **@kobraempty**, and **only the codes themselves** should be written there.

After sending the codes via DM, please write **"have it"** in the ticket so we know you've sent them."""
        )

    elif message.content.lower() == ".pp":
        await message.channel.send(
            """💰 **Paypal**

Try To Send On This Account:
https://www.paypal.me/lgkobramarket

❗ **Before sending:**
• Make sure to send Friends & Family
• No message
• 10€ Minimum

📌 Don't follow these instructions before sending = no product

If not succeeded, please make a **#📬〢tickets**."""
        )

    await bot.process_commands(message)

bot.run(os.getenv("DISCORD_TOKEN"))
