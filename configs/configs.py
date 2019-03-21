import json


json_file = open('configs/configs.json', 'r')
json_obj = json.load(json_file)

# discord関連　汎用的なもの
TOKEN = json_obj['discord']['TOKEN']                            # [必須]botのトークン
COMMAND_PREFIX = json_obj['discord']['COMMAND_PREFIX']          # [必須]コマンド実行を表す接頭語

channel = json_obj['discord']['channel']
BOT_LOG_CHANNEL_ID = channel['BOT_LOG']                         # [任意]botのログを記録するチャンネルID
VOICE_LOG_CHANNEL_ID = channel['VOICE_LOG']                     # [任意]通話入室を記録するチャンネルID
DELETE_MESSAGE_LOG_CHANNEL_ID = channel['DELETE_MESSAGE_LOG']   # [任意]メッセージ削除を記録するチャンネルID
BACKGROUND_TASK_CHANNEL_ID = channel['BACKGROUND_TASK']         # [任意]BG処理を記録するチャンネルID

