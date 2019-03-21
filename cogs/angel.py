from discord.ext import commands  # Bot Commands Frameworkのインポート
import discord


class Angel(commands.Cog):

    # コンストラクタ
    def __init__(self, bot):
        self.bot = bot

    # メインとなるroleコマンド
    @commands.group()
    @commands.has_permissions(manage_guild=True)
    async def role(self, ctx):
        # サブコマンドが指定されていない場合、メッセージを送信する。
        if ctx.invoked_subcommand is None:
            await ctx.send('このコマンドにはサブコマンドが必要です。')

    # roleコマンドのサブコマンド
    # 指定したユーザーに指定した役職を付与する。
    @role.command()
    async def add(self, ctx, member: discord.Member, role: discord.Role):
        print(member)
        print(role)
        await member.add_roles(role)

    # roleコマンドのサブコマンド
    # 指定したユーザーから指定した役職を剥奪する。
    @role.command()
    async def remove(self, ctx, member: discord.Member, role: discord.Role):
        print(member)
        print(role)
        await member.remove_roles(role)

    @add.error
    @remove.error
    async def role_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('渡された値をサーバーメンバーとして認識できませんでした。')
        else:
            print(error)


# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(Angel(bot))
