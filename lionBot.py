import discord
from discord.ext import commands

TOKEN = "NDQwNzIwNDkxMjUxMjM2ODY0.DvPnCg.epdnWygXjyP4RWKGyyaWXFrhwXI"
command_prefix = "!"
client = commands.Bot(command_prefix=command_prefix)
owner = [93094996873322496]
extensions = []


@client.event
async def on_ready():
    print("Logged in as ")
    print(client.user.name)
    print(client.user.id)
    await client.change_presence(game=discord.Game(name='fuck'))


@client.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.NoPrivateMessage):
        await client.send_message(ctx.message.channel, "This command cannot be used in private messages.")

    elif isinstance(error, commands.DisabledCommand):
        await client.send_message(ctx.message.channel, "This command is disabled and cannot be used.")

    elif isinstance(error, commands.MissingRequiredArgument):
        await client.send_message(ctx.message.channel, "You are missing required arguments!")

    elif isinstance(error, commands.CommandNotFound):
        pass

    else:
        print(error)


@client.event
async def on_message(message):
    if message.content.startswith("!!"):
        return
    await client.process_commands(message)


@client.command(pass_context=True, hidden=True)
async def logout(ctx):
    if ctx.message.author.id in owner:
        try:
            await client.say("Logging out.")
            await client.close()
        except:
            await client.say("logout failed")
    else:
        await client.say("you dont have permission bud")
        return


if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension("cogs." + extension)
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))

client.run(TOKEN)
