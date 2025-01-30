import tweepy
from datetime import datetime
from pyfiglet import Figlet 
import os

"""
将以下内容添加到 .bashrc 或 .zshrc 文件中,取决于你用的shell是哪种类型
export 'BEARER_TOKEN'='$YOUR_BEARER'
export 'API_KEY'='$your_api_key'
export 'API_SECRET'='$your_api_secret'
export 'ACCESS_TOKEN'='$your_access_token'
export 'ACCESS_TOKEN_SECRET'='$your_access_token_secret'

source ~/.bashrc 
加载配置文件
"""

def send_tweet_v2(text):
    # 使用 OAuth1 用户认证（v2 推文需要用户上下文）
    auth = tweepy.OAuth1UserHandler(
        consumer_key=os.environ.get("API_KEY"),
        consumer_secret=os.environ.get("API_SECRET"),
        access_token=os.environ.get("ACCESS_TOKEN"),
        access_token_secret=os.environ.get("ACCESS_TOKEN_SECRET")
    )
    
    # 创建 v2 客户端
    client = tweepy.Client(
       consumer_key=os.environ.get("API_KEY"),
        consumer_secret=os.environ.get("API_SECRET"),
        access_token=os.environ.get("ACCESS_TOKEN"),
        access_token_secret=os.environ.get("ACCESS_TOKEN_SECRET")
    )

    try:
        # 调用 v2 的创建推文接口
        response = client.create_tweet(text=text)
        print(f"推文成功！ID: {response.data['id']}")
    except tweepy.TweepyException as e:
        print(f"发送失败: {e}")

def show_banner():
    # 动态问候语
    hour = datetime.now().hour
    if 5 <= hour < 12:
        greeting = "🏖️ 早上好咯～想讲点什么？"
    elif 12 <= hour < 18:
        greeting = "☀️ 下午好！"
    else:
        greeting = "🌙 晚上好！"

    # 生成 ASCII 艺术字
    f = Figlet(font='slant')
    print("\033[36m" + f.renderText('Twitter Bot') + "\033[0m")
    print(f"{greeting} 当前时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)

if __name__ == "__main__":
    show_banner()  # 显示终端横幅
    
    try:
        tweet_text = input("有什么话想说：）")
        if len(tweet_text.strip()) == 0:
            print("\033[33m输入内容为空，取消发送\033[0m")
        else:
            # 添加时间戳（可选）
            final_text = f"{tweet_text}\n\n[{datetime.now().strftime('%H:%M:%S')}]"
            send_tweet_v2(final_text)
    except KeyboardInterrupt:
        print("\n\033[33m操作已取消\033[0m")