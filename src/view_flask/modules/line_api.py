from linebot import LineBotApi
from linebot.models import TextSendMessage

from config.line_setting import LINE_CHANNEL_SECRET, LINE_CHANNEL_ACCESS_TOKEN, USER_ID


class LinePush:
    def __init__(self) -> None:
        self.line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
        pass

    def push_scraping_error(self, error):
        messages = TextSendMessage(error)
        self.line_bot_api.push_message(USER_ID, messages=messages)

def main():
    line_push = LinePush()
    line_push.push_scraping_error()
    pass


if __name__ == "__main__":
    main()