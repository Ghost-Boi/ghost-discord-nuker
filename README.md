# Ghost Discord Nuker
A Windows-based Python Discord Bot who's primary function is to nuke a server.

# Warning
This is AGAINST DISCORD TOS (terms of service)! Please do not nuke a random server because you're bored. Only Nuker a server that you own, for testing purposes, or if you have been granted permission form the owner.

**I am not responsible for anything you do with this bot. This was made for creative and legal use.**

# Setup

Before you run this program there are somethings you need:

## Python 3.8.3 
You can download the python scripting language here: https://www.python.org/downloads/ **MAKE SURE YOU ADD PYTHON TO PATH**

## Discord.py
Open command prompt and run the command "python -m pip install discord.py" (without quotation marks)

## A Python Interpreter (coding program)
I recommend PyCharm for Python you can download that here: https://www.jetbrains.com/pycharm/download/ 

## Code Editing
Before you start nuking servers there are a few things you need to add to the code.

In nuker.py on lines 6 & 7 there are 2 empty variables which need to be filled

***TOKEN*** The token can be found by making a new discord bot by going to: https://discord.com/developers/applications and clicking the new application button. You can then choose a name for you bot. Then under settings on the left hand side you will see a tab called "Bot" click that then press Add Bot. Once you've done this press copy token and paste into TOKEN. 
*It should look something like this: TOKEN = 'YOUR TOKEN HERE'*

***AUTHOR_ID*** The Author id is the id of the person who will be running the commands. To get the id of a discord account you must first enable developer mode in your discord settings, under Appearance: Advanced. The you can right click on a user and copy their id you can then paste the id into AUTHOR_ID. 
*It should look something like this: AUTHOR_ID = YOURNUMBERSHERE*

## Running the Bot
Congrats you've completed all the setup now you can run the bot.
Run the start.bat file and nuke away!

## Issues
If your having any issues contact me on discord: Ghost_Boi#0001

# Commands
.help - Will Show You a Message in Discord With All the Commands

.admin - Grants the Author Administrator Permissions.

.ban - Bans Everyone from the Server Except from the Author and the Owner.

.channel - has 3 sub-commands: create, rename, delete.

.channel create - Will Spam Create Channels.

.channel rename - Will Rename All Channels with Random Names.

.channel delete - Will Delete All Channels.

.dm [Message] - Direct Messages Everyone in the Server with [Message].

.kick - Kicks Everyone from the Server Except from the Author and the Owner.

.nickname - Nicknames Everyone in the Server to a Random String Except the Author.

.purge - Deletes Messages in  all Channels.

.role - has 3 sub-commands: create, rename, delete.

.role create - Will Spam Create Roles.

.role rename - Will Rename All Roles.

.role delete - Will Delete All Roles.

.spam [Message] - Spams [Message] in the Current Channel Until Stopped.

.logout - Stops running the bot
