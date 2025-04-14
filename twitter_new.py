import time
import tweepy
from datetime import datetime
import os
import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from atproto import Client

# 假设你已经设置了这两个账号的环境变量
ACCOUNT_1 = {
    "API_KEY": os.environ.get("API_KEY"),
    "API_SECRET": os.environ.get("API_SECRET"),
    "ACCESS_TOKEN": os.environ.get("ACCESS_TOKEN"),
    "ACCESS_TOKEN_SECRET": os.environ.get("ACCESS_TOKEN_SECRET"),
    "AVATAR_PATH": "src/yanfd.jpg",  # 替换为你的头像路径
    "ACCOUNT_NAME": "YANFD"       # 可选，显示账号名称
}

ACCOUNT_2 = {
    "API_KEY": os.environ.get("API_KEY2"),
    "API_SECRET": os.environ.get("API_SECRET2"),
    "ACCESS_TOKEN": os.environ.get("ACCESS_TOKEN2"),
    "ACCESS_TOKEN_SECRET": os.environ.get("ACCESS_TOKEN_SECRET2"),
    "AVATAR_PATH": "src/Rodrick.png",  # 替换为你的头像路径
    "ACCOUNT_NAME": "Rodrick"       # 可选，显示账号名称
}

BS_ACCOUNT = {
    "ACCOUNT": os.environ.get("bs_account"),
    "PWD": os.environ.get("bs_pwd"),
}

class twitter_create(ctk.CTk):
    def __init__(self):
        super().__init__()
        print(os.getcwd())
        self.media_paths = []
        self.current_account = ACCOUNT_1  # 默认使用第一个账号
        self.accounts = [ACCOUNT_1, ACCOUNT_2]
        self.account_index = 0

        # window
        self.title("TwitterNew")
        self._set_window_geometry()
        self._set_appearance_mode("dark")
        self.attributes('-alpha', 0.8)

        # main frame
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.pack(expand=True, fill="both", padx=20, pady=20)

        # account switch frame
        self.account_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.account_frame.grid(row=0, column=0, padx=(0, 10), pady=(10, 10), sticky="w")

        # avatar button
        try:
            avatar_image = ctk.CTkImage(Image.open(self.current_account["AVATAR_PATH"]), size=(40, 40))
            self.avatar_button = ctk.CTkButton(
                self.account_frame,
                image=avatar_image,
                text="",
                width=40,
                height=40,
                corner_radius=20,
                fg_color="gray20",
                hover_color="gray30",
                command=self.switch_account
            )
            self.avatar_button.pack(side="left")
        except FileNotFoundError:
            self.avatar_label = ctk.CTkLabel(self.account_frame, text="👤", font=("Arial", 24))
            self.avatar_label.pack(side="left")
            print(f"Error: Avatar image not found at {self.current_account['AVATAR_PATH']}")

        # greetings
        def show_banner():
            # 动态问候语
            current_time = datetime.now().strftime("%H:%M")
            hour = datetime.now().hour
            if 5 <= hour < 12:
                greeting = f"{current_time} 🌧️ ›Morning ideas?"
            elif 12 <= hour < 18:
                greeting = f"{current_time} 🌆 ›Share?"
            else:
                greeting = f"{current_time} 🌌 ›Midnight thoughts?"
            return greeting
        greetings = show_banner()
        self.label1 = ctk.CTkLabel(
            self.main_frame,
            text=f'{greetings}',
            font=("Monospace", 18, "bold"),
            text_color="white"
        )
        self.label1.grid(row=0, column=1, padx=(10, 20), pady=(10, 10), sticky="ew")
        self.main_frame.grid_columnconfigure(1, weight=1) # 让 greetings 可以水平扩展

        # text entry
        self.text_box = ctk.CTkTextbox(
            self.main_frame,
            border_color="white",
            font=("Microsoft YaHei", 18, "bold"),
            border_width=2,
            fg_color="transparent",
            corner_radius=8
        )
        self.text_box.grid(row=1, column=0, columnspan=2, padx=20, pady=5, sticky="ew")

        # image insert frame
        self.image_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.image_frame.grid(row=2, column=0, columnspan=2, padx=20, pady=5, sticky="ew")

        # image insert
        def file_uploading():
            file_paths = filedialog.askopenfilenames(
                title="select the pic you wanna share:",
                filetypes=[("Images", "*.jpg *.png *.jpeg")],
                initialdir=os.path.expanduser("~/Downloads/StableDiffusion/output/")
            )
            if file_paths:
                self.media_paths = file_paths
                try:
                    file_label_update(f"{len(file_paths)} PICS SELECTED.")
                    status_label_update("Image selected.")
                except Exception as e:
                    print(e)
                    status_label_update("Failed.")

        def file_label_update(display_text):
            self.file_label.configure(text=f"{display_text}")

        self.file_label = ctk.CTkLabel(
            self.image_frame,
            text="ANY PICS?",
            text_color="white"
        )
        self.file_label.pack(expand=True, side="left", pady=5)

        self.insert_image_button = ctk.CTkButton(
            self.image_frame,
            corner_radius=32,
            fg_color="black",
            hover_color="#666666",
            border_color="white",
            border_width=1,
            text="INSERT",
            command=file_uploading
        )
        self.insert_image_button.pack(expand=False, side="right", padx=5, pady=5)

        # mockup
        self.mockup_check_box = ctk.CTkCheckBox(self.main_frame, text="WRAP WITH MOCKUP", onvalue=True, offvalue=False,
                                               fg_color="white", checkmark_color="black",
                                               font=("Microsoft YaHei", 12, "bold"), border_color="white", border_width=2)
        self.mockup_check_box.grid(row=3, column=0, columnspan=2, padx=92, pady=5, sticky="ew")

        # sending
        def sending():
            
            tweet_text = self.text_box.get("1.0", "end-1c")
            try:
                if not tweet_text.strip() and not self.media_paths:
                    print("\033[33mEmpty input, cancelled.\033[0m")
                else:
                    if self.mockup_check_box.get():
                        self.apply_mockup_background()
                        if self.media_paths and all(path.endswith("_mockup.png") for path in self.media_paths):
                            self.send_tweet(tweet_text, self.media_paths)
                            status_label_update("PUBLISHED (with mockup).")
                        elif self.mockup_check_box.get() and self.media_paths and not all(path.endswith("_mockup.png") for path in self.media_paths):
                            status_label_update("Mockup generation failed or not yet complete.")
                        elif self.mockup_check_box.get() and not self.media_paths:
                            status_label_update("No images to apply mockup to.")
                    else:
                        self.send_tweet(tweet_text, self.media_paths)
                        status_label_update("PUBLISHED.")

            except KeyboardInterrupt:
                print("\n\033[33mCANCELLED. SEE YA.\033[0m")
                status_label_update("Cancelled.")
            except Exception as e:
                print(e)
                status_label_update("Failed.")

            except KeyboardInterrupt:
                print("\n\033[33mCANCELLED. SEE YA.\033[0m")
                status_label_update("Cancelled.")
            except Exception as e:
                print(e)
                status_label_update("Failed.")

        self.send_button = ctk.CTkButton(
            self.main_frame,
            text="SEND",
            corner_radius=32,
            command=sending,
            fg_color="black", border_color="white", border_width=1,
            hover_color="#666666",
            font=("Microsoft YaHei", 16, "bold")
        )
        self.send_button.grid(row=4, column=0, columnspan=2, padx=20, pady=5, sticky="ew")

        # status
        def status_label_update(status):
            self.status_label.configure(text=f"{status}")

        self.status_label = ctk.CTkLabel(
            self.main_frame,
            text="READY",
            text_color="white",
            anchor="center",
            font=("Microsoft YaHei", 10, "bold"),
        )
        self.status_label.grid(row=5, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

    def get_v1_client(self):
        """根据当前账号信息获取 v1 客户端"""
        auth = tweepy.OAuth1UserHandler(
            consumer_key=self.current_account["API_KEY"],
            consumer_secret=self.current_account["API_SECRET"],
            access_token=self.current_account["ACCESS_TOKEN"],
            access_token_secret=self.current_account["ACCESS_TOKEN_SECRET"]
        )
        return tweepy.API(auth)

    def send_tweet(self, text, media_paths=None):
        """根据当前账号信息发送推文"""
        client_v2 = tweepy.Client(
            consumer_key=self.current_account["API_KEY"],
            consumer_secret=self.current_account["API_SECRET"],
            access_token=self.current_account["ACCESS_TOKEN"],
            access_token_secret=self.current_account["ACCESS_TOKEN_SECRET"]
        )

        api_v1 = self.get_v1_client()
        media_ids = []

        # 上传媒体文件
        if media_paths:
            for path in media_paths:
                if not os.path.exists(path):
                    print(f"⚠️ File not found: {path}")
                    continue
                try:
                    media = api_v1.media_upload(filename=path)
                    media_ids.append(media.media_id)
                    print(f"🖼️ Media uploaded: {path}")
                except Exception as e:
                    print(f"❌ Failed to upload {path}: {e}")

        try:
            response = client_v2.create_tweet(
                text=text,
                media_ids=media_ids if media_paths else None
            )
            client = Client()
            client.login(BS_ACCOUNT["ACCOUNT"], BS_ACCOUNT["PWD"])
            post = client.send_post(text)
            print(f"✅ PUBLISHED. ID: {response.data['id']}")
        except tweepy.TweepyException as e:
            print(f"❌ FAILED: {e}")

    def switch_account(self):
        """切换账号"""
        self.account_index = (self.account_index + 1) % len(self.accounts)
        self.current_account = self.accounts[self.account_index]
        print(f"Switched to account: {self.current_account.get('ACCOUNT_NAME', 'Account')}")
        try:
            avatar_image = ctk.CTkImage(Image.open(self.current_account["AVATAR_PATH"]), size=(40, 40))
            self.avatar_button.configure(image=avatar_image)
        except FileNotFoundError:
            print(f"Error: Avatar image not found at {self.current_account['AVATAR_PATH']}")

    def _set_window_geometry(self):
        """设置窗口位置和大小"""
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = 400
        window_height = 480
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 4  # 偏上方
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.minsize(300, 450)
        self.resizable(True, True)

    def get_dominant_color(self, image):
        """获取图片的主色调"""
        image = image.resize((100, 100))
        pixels = image.getcolors(10000)
        sorted_pixels = sorted(pixels, key=lambda t: t[0], reverse=True)
        return sorted_pixels[0][1]

    def apply_mockup_background(self):
        """应用mockup效果"""
        if not self.media_paths:
            self.status_label.configure(text="No images selected")
            return

        new_paths = []
        for path in self.media_paths:
            try:
                with Image.open(path) as img:
                    width, height = img.size

                    if self.account_index == 0:
                        new_paths = []
                        for path in self.media_paths:
                            with Image.open(path) as img:
                                RADIUS = 20  # 圆角弧度控制点
                                dominant_color = self.get_dominant_color(img)
                                width, height = img.size
                                new_size = (int(width * 1.4), int(height * 1.3))  # 留出阴影空间

                                # 创建渐变背景
                                gradient = Image.new('RGB', new_size, color='white')
                                draw = ImageDraw.Draw(gradient)
                                for y in range(new_size[1]):
                                    ratio = y / new_size[1]
                                    r = int(dominant_color[0] * (1 - ratio) + 255 * ratio)
                                    g = int(dominant_color[1] * (1 - ratio) + 255 * ratio)
                                    b = int(dominant_color[2] * (1 - ratio) + 255 * ratio)
                                    draw.line([(0, y), (new_size[0], y)], fill=(r, g, b))

                                # 创建圆角蒙版
                                mask = Image.new('L', img.size, 0)
                                draw = ImageDraw.Draw(mask)
                                draw.rounded_rectangle([(0, 0), img.size], radius=RADIUS, fill=255)

                                # 应用蒙版
                                rounded_img = Image.new('RGBA', img.size, (0, 0, 0, 0))
                                rounded_img.paste(img.convert('RGBA'), (0, 0), mask)

                                # 创建阴影层
                                shadow_offset = 25  # 阴影偏移量
                                shadow = Image.new('RGBA',
                                                (img.width + shadow_offset, img.height + shadow_offset),
                                                (0, 0, 0, 0))

                                shadow_draw = ImageDraw.Draw(shadow)
                                shadow_draw.rounded_rectangle(
                                    [(shadow_offset, shadow_offset),
                                    (img.width, img.height)],
                                    radius=RADIUS,
                                    fill=(0, 0, 0, 100)
                                )
                                shadow = shadow.filter(ImageFilter.GaussianBlur(10))

                                # 合成所有元素
                                final_image = gradient.convert('RGBA')

                                # 计算正确阴影位置
                                image_x = (new_size[0] - width) // 2  # 图片水平居中坐标
                                image_y = (new_size[1] - height) // 2  # 图片垂直居中坐标

                                shadow_x = image_x + shadow_offset - 15  # 微调-15补偿阴影绘制偏移
                                shadow_y = image_y + shadow_offset - 15

                                final_image.alpha_composite(shadow, (shadow_x, shadow_y))  # 更新阴影坐标

                                final_image.alpha_composite(
                                    rounded_img,
                                    (image_x, image_y)  # 使用计算后的坐标
                                )

                                # 添加文字，绘制文字
                                draw = ImageDraw.Draw(final_image)
                                font_size = int(height * 0.05)
                                try:
                                    font = ImageFont.truetype("Impact.ttf", font_size)
                                except IOError:
                                    font = ImageFont.load_default().font_variant(size=font_size)

                                text = "POWERED BY YANFD"
                                bbox = font.getbbox(text)
                                text_width = bbox[2] - bbox[0]
                                text_height = bbox[3] - bbox[1]
                                text_x = (new_size[0] - text_width) // 2 #水平居中
                                bottom_margin = new_size[1] - height - (image_y + height)
                                text_y = image_y + height - int(bottom_margin * 0.02)

                                draw.text((text_x, text_y), text, font=font, fill="#191919")
                                    # 保存新图片
                            new_path = f"{os.path.splitext(path)[0]}_mockup.png"
                            final_image.save(new_path)
                            new_paths.append(new_path)
                    else:
                        new_paths = []
                        for path in self.media_paths:
                            with Image.open(path) as img:
                                width, height = img.size  # 获取原始图片尺寸
                                draw = ImageDraw.Draw(img)
                                font_size = int(height * 0.05)
                                try:
                                    font = ImageFont.truetype("Impact.ttf", font_size)
                                except IOError:
                                    font = ImageFont.load_default().font_variant(size=font_size)

                                text = "@Rodreick007"
                                bbox = font.getbbox(text)
                                text_width = bbox[2] - bbox[0]
                                text_height = bbox[3] - bbox[1]
                                text_x = (width - text_width) // 2  # 水平居中
                                bottom_margin = int(height * 0.1)  # 底部留白
                                text_y = height - text_height - bottom_margin  # 靠近底部

                                draw.text((text_x, text_y), text, font=font, fill="#5E6077")
                        # 保存新图片
                        new_path = f"{os.path.splitext(path)[0]}_mockup.png"
                        img.save(new_path)
                        new_paths.append(new_path)

            except FileNotFoundError:
                self.status_label.configure(text=f"Error: Image not found at {path}")
                continue
            except Exception as e:
                self.status_label.configure(text=f"Error processing {path}: {e}")
                continue

        self.media_paths = new_paths
        self.status_label.configure(text=f"Applied mockup to {len(self.media_paths)} images")

if __name__ == "__main__":
    app = twitter_create()
    app.mainloop()