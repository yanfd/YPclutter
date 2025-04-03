# x,y为正整数，求x的y次方的个位数是多少
# 输入描述：依次输入两个数（每行一个），第一个为x，第二个为y 
# 输出描述：输出个位数

# def last_digit_of_power(x, y):
#     last_digit_x = x % 10
#     if y == 0:
#         return 1

#     y_mod = y % 4
#     if y_mod == 0:
#         y_mod = 4 

#     result = (last_digit_x ** y_mod) % 10
#     return result

# # 输入
# x = int(input())
# y = int(input())

# # 输出
# print(last_digit_of_power(x, y))

#2
# def max_rotated_number(n):
#     s = str(n)  
#     max_num = n  
#     k = len(s)   
    
#     for i in range(1, k):
        
#         rotated = s[-i:] + s[:-i]
#         if int(rotated) > max_num:
#             max_num = int(rotated)
    
#     return max_num

# # 输入
# n = int(input())

# # 输出
# print(max_rotated_number(n))
    
# import re

# def is_valid_dns_domain(domain):
#     if len(domain) > 255:
#         return False
    
#     labels = domain.split('.')
#     if len(labels) < 2:
#         return False
    

#     for label in labels:
#         if len(label) > 63:
#             return False
#         if label.startswith('-') or label.endswith('-'):
#             return False
#         if not re.match(r'^[a-zA-Z0-9-]+$', label):
#             return False
    
#     return True

# # 输入
# domain = input().strip()

# # 输出
# print(is_valid_dns_domain(domain))

#4
# def min_edit_time(T, test_cases):
#     results = []
#     for case in test_cases:
#         n, k, tasks = case
#         min_time = float('inf')
        
#         for i in range(n - k + 1):
#             selected = tasks[i:i + k]
#             left, right = 0, k
#             while left < right:
#                 mid = (left + right) // 2
#                 xiaoming = sum(selected[:mid])
#                 xiaobai = sum(selected[mid:])
#                 current_max = max(xiaoming, xiaobai)
#                 min_time = min(min_time, current_max)
#                 if xiaoming < xiaobai:
#                     left = mid + 1
#                 else:
#                     right = mid
#         results.append(min_time)
#     return results

# # 输入
# T = int(input())
# test_cases = []
# for _ in range(T):
#     n, k = map(int, input().split())
#     tasks = list(map(int, input().split()))
#     test_cases.append((n, k, tasks))

# # 输出
# results = min_edit_time(T, test_cases)
# for res in results:
    # print(res)







# def hanoi(n, src, dst, via):
#     if n == 1:
#         print(f'{src} -> {dst}')
#     else:
#         hanoi(n-1, src, via, dst)
#         print(f'{src} -> {dst}')
#         hanoi(n-1, via, dst, src)


# if __name__ == '__main__':
#     n = int(input())
#     hanoi(n, 'A', 'C', 'B')








# import psutil
# import time

# def get_network_speed():
#     """计算每秒网络速率"""
#     initial_net = psutil.net_io_counters()
#     time.sleep(1)  # 等待1秒
#     final_net = psutil.net_io_counters()

#     # 计算差值
#     bytes_sent = final_net.bytes_sent - initial_net.bytes_sent
#     bytes_recv = final_net.bytes_recv - initial_net.bytes_recv
#     # 转换为MB/s
#     mb_sent = bytes_sent / (1024 * 1024)
#     mb_recv = bytes_recv / (1024 * 1024)
#     return mb_sent, mb_recv

# if __name__ == "__main__":
#     sent, recv = get_network_speed()
#     print(f"发送速率: {sent:.2f} MB/s, 接收速率: {recv:.2f} MB/s")

#     #可以循环执行，以达到持续监控的目的
#     #while True:
#     #    sent, recv = get_network_speed()
#     #    print(f"发送速率: {sent:.2f} MB/s, 接收速率: {recv:.2f} MB/s")
#     #    time.sleep(1)


import tweepy
import os
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from datetime import datetime

# 替换为您的 API 凭据
consumer_key = os.environ.get("API_KEY")
consumer_secret = os.environ.get("API_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

bearer_token = "AAAAAAAAAAAAAAAAAAAAALTnrQEAAAAASq2mZWi2Dfq%2Bkg9HpVAPhIWaslw%3DIGNGoRIQ88VaVdXQ2hgRpwvZvmsCCtbH8Vm7SannjHUcRUPMPV" # 替换为您的 Bearer Token

# 设置默认字体大小 (Pillow 会尝试使用系统默认字体)
font_title_size = 24
font_body_size = 18
font_small_size = 14

try:
    font_title = ImageFont.truetype("arial.ttf", font_title_size)
    font_body = ImageFont.truetype("arial.ttf", font_body_size)
    font_small = ImageFont.truetype("arial.ttf", font_small_size)
    print("尝试加载 arial.ttf")
except IOError:
    print("加载 arial.ttf 失败，使用默认字体")
    font_title = ImageFont.load_default()
    font_body = ImageFont.load_default()
    font_small = ImageFont.load_default()

# 设置颜色
color_text = (0, 0, 0)
color_light_gray = (150, 150, 150)
color_white = (255, 255, 255)
color_like = (225, 0, 0)

def download_image(url):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        return Image.open(BytesIO(response.content))
    except requests.exceptions.RequestException as e:
        print(f"下载图片失败: {e}")
        return None

def create_tweet_image(tweet_data, author_data, media_data, like_count):
    # 设置图片尺寸和边距
    width = 800
    padding = 20
    y_offset = padding

    # 创建白色背景图片
    img = Image.new("RGB", (width, 1), color_white)
    draw = ImageDraw.Draw(img)

    # 下载头像
    avatar_size = 70
    avatar_url = author_data.profile_image_url.replace("_normal", "_400x400") # 获取更高清的头像
    avatar = download_image(avatar_url)
    if avatar:
        avatar = avatar.resize((avatar_size, avatar_size))
        img = add_to_image(img, avatar, padding, y_offset)
    avatar_x_offset = padding + avatar_size + padding

    # 绘制账号名
    username = author_data.username
    draw.text((avatar_x_offset, y_offset), username, font=font_title, fill=color_text)
    y_offset += font_title.getbbox(username)[3] + 5

    # 绘制推文内容
    text = tweet_data.text
    text_y = y_offset
    for line in text.splitlines():
        draw.text((avatar_x_offset, text_y), line, font=font_body, fill=color_text)
        text_y += font_body.getbbox(line)[3] + 5
    y_offset = text_y + padding

    # 下载并绘制推文图片 (如果存在)
    image_height = 0
    if media_data and media_data[0].type == 'photo':
        image_url = media_data[0].url
        tweet_image = download_image(image_url)
        if tweet_image:
            max_image_height = 400
            ratio = max_image_height / tweet_image.height
            resized_width = int(tweet_image.width * ratio)
            resized_image = tweet_image.resize((resized_width, max_image_height))
            img = add_to_image(img, resized_image, padding, y_offset)
            image_height = max_image_height + padding
            y_offset += image_height

    # 绘制发布时间
    created_at = datetime.strptime(str(tweet_data.created_at)[:-6], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
    draw.text((padding, y_offset), f"发布于: {created_at}", font=font_small, fill=color_light_gray)
    y_offset += font_small.getbbox(f"发布于: {created_at}")[3] + padding

    # 绘制点赞数
    like_icon = "❤️" # 可以使用实际的图标图片
    like_text = f"{like_icon} {like_count}"
    draw.text((padding, y_offset), like_text, font=font_body, fill=color_like)
    y_offset += font_body.getbbox(like_text)[3] + padding

    # 调整图片高度
    final_height = y_offset
    img = img.resize((width, final_height))

    return img

def add_to_image(base_img, new_img, x, y):
    combined_width = max(base_img.width, x + new_img.width)
    combined_height = max(base_img.height, y + new_img.height)
    new_base = Image.new(base_img.mode, (combined_width, combined_height), color_white)
    new_base.paste(base_img, (0, 0))
    new_base.paste(new_img, (x, y))
    return new_base

def get_tweet_info(tweet_id):
    client = tweepy.Client(bearer_token)

    try:
        response = client.get_tweet(
            tweet_id,
            expansions=['author_id', 'attachments.media_keys'],
            tweet_fields=['created_at', 'public_metrics'],
            user_fields=['profile_image_url', 'username'],
            media_fields=['url']
        )

        if response.data:
            tweet = response.data
            author = response.includes['users'][0]
            media = response.includes.get('media', [])
            like_count = tweet.public_metrics['like_count']

            image = create_tweet_image(tweet, author, media, like_count)
            image.save(f"tweet_{tweet_id}.png")
            print(f"推特信息已保存到 tweet_{tweet_id}.png")

        else:
            print(f"无法找到 ID 为 {tweet_id} 的推文。")

    except tweepy.errors.NotFound:
        print(f"推文 ID {tweet_id} 不存在。")
    except tweepy.errors.TweepyException as e:
        print(f"获取推文信息时发生错误: {e}")

if __name__ == "__main__":
    tweet_url = "https://x.com/mryanfd/status/1907691330102563175?s=46"
    parts = tweet_url.split('/')
    try:
        tweet_id = parts[5].split('?')[0]
        get_tweet_info(tweet_id)
    except IndexError:
        print("无效的推特链接格式。")