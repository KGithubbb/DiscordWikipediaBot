import wikipediaapi
import discord
from discord import app_commands

TOKEN = ""

# Wikipediaの言語を日本語に設定
wiki_lang = "ja"

# ユーザーエージェントを指定してWikipediaにアクセス
wiki_wiki = wikipediaapi.Wikipedia(
    language=wiki_lang,
    user_agent="URUSERAGENT"
)
global text
def EoN():
    global Title
    global Summary
    global Error
    page = wiki_wiki.page(Intext)
    if page.exists():
    # ページの概要を表示
        Title = "タイトル:", page.title
        Summary = "概要:", page.summary
        return Title, Summary, None
    else:
        Error = ("ページが存在しません")
        return None, None, Error

intents = discord.Intents.default()#適当に。
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print("起動完了")
    await tree.sync()#スラッシュコマンドを同期

@tree.command(name="summary", description="writes out summary for you. (it needs to be perfectly right)")
async def wiki_command(interaction: discord.Interaction, text: str):
    global Intext
    Intext = text
    try:
        EoN()
        if Title and Summary:
            response_message = f"{Title}\n{Summary}"
        else:
            response_message = "ページが存在しません"
        
        await interaction.response.send_message(response_message, ephemeral=True)
    except Exception as e:
        # 例外をログに記録
        print(f"エラーが発生しました: {e}")
    print(interaction.user,"used wikipedia Command")

client.run(TOKEN)
