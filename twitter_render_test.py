from io import BytesIO
from tkinter import Image
from jinja2 import Template
import requests
import tweepy

async def render():
    markdown_template = """
                        <div style="display: flex; align-items: center; margin-bottom: 5px;">
                          <img src="{{ avatar_url }}" alt="头像" width="30" style="margin-right: 10px;">
                          <b>{{ username }}</b>
                        </div>
                        <div style="margin-bottom: 10px;">
                          {{ tweet_text }} <a href="{{ tweet_url }}" target="_blank">🔗</a>
                        </div>
                        {% if image_urls %}
                        <div align="center" style="margin-bottom: 10px;">
                          {% for image_url in image_urls %}
                          <img src="{{ image_url }}" alt="推文图片" width="300" style="margin-bottom: 5px;">
                          {% endfor %}
                        </div>
                        {% endif %}
                        <hr style="margin: 5px 0;">
                        <div style="display: flex; justify-content: space-between; align-items: center; font-size: 0.8em; color: #888;">
                          <div>
                            📅 `{{ created_at }}`
                          </div>
                          <div>
                            👍 {{ like_count }} 🔁 {{ retweet_count }}
                          </div>
                        </div>
                        <div style="font-size: 0.7em; color: #aaa; text-align: right;">
                          ID: `{{ tweet_id }}`
                        </div>
                        """
    template = Template(markdown_template)
    html = template.render(
        avatar_url="https://pbs.twimg.com/profile_images/1905510883721445381/6kGJ86d8_normal.jpg",
        username="Rodreick007",
        tweet_text="My lord! You're back! #AIart #furry https://t.co/hyybdl4VaK",
        tweet_url="https://t.co/hyybdl4VaK",
        image_urls="https://pbs.twimg.com/media/Gni-doEa8AAQ6G_.jpg",
        created_at="2025-04-02 17:22:47+00:00",
        like_count=2,
        retweet_count=0,
        tweet_id="1907483864806887502",
    )
    url = await self.html_render(html, {})

    response = requests.get(url)
    response.raise_for_status()
    pic = Image.open(BytesIO(response.content))
    pic.save("status.png")

"""
推文 ID: 1907483864806887502
推文内容: My lord! You're back!
#AIart #furry https://t.co/hyybdl4VaK
账号名: Rodreick007
头像链接: https://pbs.twimg.com/profile_images/1905510883721445381/6kGJ86d8_normal.jpg
发布时间: 2025-04-02 17:22:47+00:00
点赞数: 2
转发数: 0
图片链接: ['https://pbs.twimg.com/media/Gni-doEa8AAQ6G_.jpg']
"""