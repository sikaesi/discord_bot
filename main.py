from discord.ext import commands
from configs import configs
import cogs.common
import cogs.voice
import asyncio
import random


# クラスの定義。ClientのサブクラスであるBotクラスを継承。
class Main(commands.Bot):

    # constructor
    def __init__(self, command_prefix):
        super().__init__(command_prefix)
        cogs.common.setup(self, configs)
        cogs.voice.setup(self, configs)
        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.background_task())

    # Bot起動完了時実行イベント
    async def on_ready(self):
        print('-----')
        print(self.user.name)
        print(self.user.id)
        print('-----')

    # 定期実行イベント
    async def background_task(self):
        await self.wait_until_ready()
        counter = 0
        channel = self.get_channel(configs.BACKGROUND_TASK_CHANNEL_ID)
        if channel:
            while not self.is_closed():
                counter += 1
                await channel.send(counter)
                await asyncio.sleep(60)

    # メッセージ受信時実行イベント
    async def on_message(self, message):
        if message.author.bot:
            return

        if message.content.startswith('にゃー'):
            rand = ('ー' * random.randint(0, 30))
            msg = "にゃ" + rand + "ん"
            await message.channel.send(msg)
            return

        await self.process_commands(message)


# インスタンス化及び起動処理。
if __name__ == '__main__':
    bot = Main(command_prefix=configs.COMMAND_PREFIX)
    bot.run(configs.TOKEN)
