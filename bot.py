@bot.event
async def on_message(message):
    if message.author.bot:
        return

    msg = message.content.lower().strip()

    if msg == ".psc":
        await message.channel.send(
            """💳 **You want to pay with Paysafe?**

Before sending your codes, please check them here to make sure you copied them correctly:
https://www.paysafecard.com/en-gb/balance-check/

⚠️ The codes are **not sent to the ticket**. They are only sent via DM to **@kobraempty**, and **only the codes themselves** should be written there.

After sending the codes via DM, please write **"have it"** in the ticket so we know you've sent them."""
        )

    if msg == ".pp":
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
