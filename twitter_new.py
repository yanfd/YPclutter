import tweepy
from datetime import datetime
from pyfiglet import Figlet 
import os
# 替换为你的凭证（注意：v2 可能需要 Bearer Token）
#BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAALTnrQEAAAAASq2mZWi2Dfq%2Bkg9HpVAPhIWaslw%3DIGNGoRIQ88VaVdXQ2hgRpwvZvmsCCtbH8Vm7SannjHUcRUPMPV"
#API_KEY = "eqTmIqIdyT0vR4TWTv0lzvvNj"
#API_SECRET = "DQUIySCLWrmk5kj6u1REi8tn9BmmRmDwu8QoR8n9toowz1wrHB"
#ACCESS_TOKEN = "820599551375511556-isKFhbVzhS2Vi3CCKBlfZSu5VEUg4xt"
#ACCESS_TOKEN_SECRET = "HcNphjNa9h0stdzYvTejT7QzfbpzjnYhtRse2YiXJpBq4"

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

if __name__ == "__main__":
    time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    text = input("有什么话想说：）")
    send_tweet_v2(f"{text}")
