import discord
from discord.ext import commands
import json
import io
from osintcat import osintcat

tkn = "bot tkn"
catid = "CatID / LoginID"
bot = commands.Bot(intents=discord.Intents.all())

@bot.slash_command(name="search")
async def search(ctx, module: discord.Option(description="choice module", choices=["breach", "email-osint", "discord"]), query):
    await ctx.defer()
    try:
        result = osintcat(cat_id=catid, module=module, query=query)
        jd = json.dumps(result, indent=2, ensure_ascii=False)
        json_file = io.StringIO(jd)
        file = discord.File(fp=io.BytesIO(jd.encode('utf-8')),filename=f"{module}_{query.replace(' ', '_')}.json")
        await ctx.followup.send(content=f"🔍 Results for `{query}`:",file=file)
    
    except Exception as e:
        await ctx.followup.send(f"❌ Error`")

bot.run(tkn)