from datetime import datetime, timedelta, timezone
import locale
JST = timezone(timedelta(hours=+9), 'JST')


class VoiceUtils:

    @staticmethod
    def create_voice_channel_log(member, before, after):
        now = datetime.now(JST)
        locale.setlocale(locale.LC_ALL, '')
        if (before.self_mute is not after.self_mute) or (before.self_deaf is not after.self_deaf):
            # マイク情報の変動は通知不要
            return
        if after.channel is None:
            # 退出時の通知も不要
            return
        if before.channel is not None and before.channel.name is after.channel.name:
            # 同chでの遷移時も不要
            return

        msg = member.name + "が[" + after.channel.name + "]に入室。(" + '{0:%Y年%m月%d日%H時%M分%S秒}'.format(now) + ")"

        return msg
