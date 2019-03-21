from discord.ext import commands
from utils.voiceUtils import VoiceUtils


class Common(commands.Cog):

    # コンストラクタ
    def __init__(self, bot, configs):
        self.bot = bot
        self.configs = configs

    # テキストメッセージの削除時実行イベント
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot:
            return

        channel = self.bot.get_channel(self.configs.DELETE_MESSAGE_LOG_CHANNEL_ID)
        if channel:
            msg = '[' + str(message.author.name) + ']'
            msg += 'がメッセージを削除しました。\r\n'
            msg += message.content
            await channel.send(msg)
        return

    # VoiceState変更時実行イベント
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):

        channel = self.bot.get_channel(self.configs.VOICE_LOG_CHANNEL_ID)
        if channel:
            msg = VoiceUtils.create_voice_channel_log(member, before, after)
            if msg is not None:
                await channel.send(msg)
            return

    # 使い方
    @commands.command(aliases=['use'], usage="this command")
    async def usage(self, ctx):
        cmds = self.bot.get_cog('Common').get_commands()
        for c in cmds:
            word = c.name + ' : ' + c.usage + '\r\n'
        await ctx.send(word)


# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot, configs):
    bot.add_cog(Common(bot, configs))
