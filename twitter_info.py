import tweepy

bearer_token = "" # 对于 API v2，推荐使用 Bearer Token

def get_tweet_info(tweet_id):
    client = tweepy.Client(bearer_token)  # 使用 API v2 客户端

    try:
        response = client.get_tweet(
            tweet_id,
            expansions=['author_id', 'attachments.media_keys'],
            tweet_fields=['created_at', 'public_metrics'], # 添加 public_metrics
            user_fields=['profile_image_url', 'username'],
            media_fields=['url']
        )

        if response.data:
            tweet = response.data
            author = response.includes['users'][0]
            media = response.includes.get('media', [])

            text = tweet.text
            username = author.username
            avatar_url = author.profile_image_url
            created_at = tweet.created_at

            like_count = tweet.public_metrics['like_count']
            retweet_count = tweet.public_metrics['retweet_count']

            image_urls = [m.url for m in media if m.type == 'photo']

            print("推文 ID:", tweet_id)
            print("推文内容:", text)
            print("账号名:", username)
            print("头像链接:", avatar_url)
            print("发布时间:", created_at)
            print("点赞数:", like_count)
            print("转发数:", retweet_count)
            if image_urls:
                print("图片链接:", image_urls)
            else:
                print("没有图片。")

        else:
            print(f"无法找到 ID 为 {tweet_id} 的推文。")

    except tweepy.errors.NotFound:
        print(f"推文 ID {tweet_id} 不存在。")
    except tweepy.errors.TweepyException as e:
        print(f"获取推文信息时发生错误: {e}")

if __name__ == "__main__":
    tweet_url = "https://x.com/rodreick007/status/1907483864806887502?s=46"
    # 从 URL 中提取推文 ID
    parts = tweet_url.split('/')
    tweet_id = parts[5].split('?')[0]

    get_tweet_info(tweet_id)