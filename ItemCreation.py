import discord
import database as db

class EpicCreator(discord.ui.Modal):
    def __init__(self, gid, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.gid = gid
        self.add_item(discord.ui.InputText(label="Title"))
        self.add_item(discord.ui.InputText(label="Description", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        itemData = {
            "type":0,
            "name":self.children[0].value,
            "desc":self.children[1].value,
            "chil":[]
            }
        db.saveItem(itemData,self.gid)
        embed = discord.Embed(title=":zap: Created New Epic", color=discord.Color.yellow())
        embed.add_field(name=self.children[0].value, value=self.children[1].value)
        await interaction.response.send_message(embeds=[embed])

class StoryCreator(discord.ui.Modal):
    def __init__(self, gid, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.gid = gid
        self.add_item(discord.ui.InputText(label="Title"))
        self.add_item(discord.ui.InputText(label="Description", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        itemData = {
            "type":1,
            "name":self.children[0].value,
            "desc":self.children[1].value,
            "prio":'m',
            "assi": None,
            "pren": None,
            "chil": []
            }
        db.saveItem(itemData,self.gid)
        embed = discord.Embed(title=":bulb: Created New User Story", color=discord.Color.green())
        embed.add_field(name=self.children[0].value, value=self.children[1].value)
        await interaction.response.send_message(embeds=[embed])

class BugCreator(discord.ui.Modal):
    def __init__(self, gid, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.gid = gid
        self.add_item(discord.ui.InputText(label="Title"))
        self.add_item(discord.ui.InputText(label="Description", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        itemData = {
            "type":2,
            "name":self.children[0].value,
            "desc":self.children[1].value,
            "prio":'m',
            "assi": None,
            "pren": None,
            "chil": []
            }
        db.saveItem(itemData,self.gid)
        embed = discord.Embed(title=":crab: Created New Bug", color=discord.Color.red())
        embed.add_field(name=self.children[0].value, value=self.children[1].value)
        await interaction.response.send_message(embeds=[embed])

class TaskCreator(discord.ui.Modal):
    def __init__(self, gid, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.gid = gid
        self.add_item(discord.ui.InputText(label="Title"))
        self.add_item(discord.ui.InputText(label="Description", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        itemData = {
            "type":3,
            "name":self.children[0].value,
            "desc":self.children[1].value,
            "prio":'m',
            "assi": None,
            "pren": None,
            "chil": []
            }
        db.saveItem(itemData,self.gid)
        embed = discord.Embed(title=":ballot_box_with_check: Created New Task", color=discord.Color.blue())
        embed.add_field(name=self.children[0].value, value=self.children[1].value)
        await interaction.response.send_message(embeds=[embed])