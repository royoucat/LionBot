import discord
from discord.ext import commands
import youtube_dl

TOKEN = "NDQwNzIwNDkxMjUxMjM2ODY0.DvPnCg.epdnWygXjyP4RWKGyyaWXFrhwXI"
command_prefix = '!'
client = commands.Bot(command_prefix=command_prefix)
owner = ["93094996873322496"]
extensions = []
players = {}


@client.event
async def on_ready():
    print("Logged in as " + client.user.name)
    print(client.user.id)
    await client.change_presence(game=discord.Game(name='owo'))


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


@client.command(pass_context = True, hidden = True)
async def logout(ctx):
    if ctx.message.author.id in owner:
        try:
            await client.say("Logging out bot")
            await client.close()
        except:
            await client.say("Failed to log out bot")
    else:
        await client.say("You do not have permissions to do this")
        return

@client.command(pass_context = True)
async def twitter(ctx):
    print('posting twitter')
    await client.send_message(ctx.message.channel, 'owner: https://www.twitter.com/royoucat')
    
@client.command(pass_context = True)
async def beans(ctx):
    print('test')
    await client.send_message(ctx.message.channel, ':feet: :feet:')
        

@client.event
async def on_member_join(member):
    server = client.get_channel("522759933012344835")
    await client.send_message(server, 'meowdy, ' + member.mention)

@client.command(pass_context=True)
async def join(ctx):
    print('join received')
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()
    

@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()
    

if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension("cogs." + extension)
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))

client.run(TOKEN)
