import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return
        else if ('flat fuck' in message.content
            or 'flatfuck' in message.content
            or 'gator' in message.content):
            # triggers for :flatfuck:
            flatfuck = self.get_emoji(701115789255639061)
            await message.add_reaction(flatfuck)

with open('bot_info.txt') as file:
    token = file.readlines()[0].strip()
    MyClient().run(token)
