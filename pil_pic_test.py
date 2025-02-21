import customtkinter as ctk
from tkinter import filedialog
import os
from PIL import Image, ImageDraw, ImageFilter

class ImageProcessorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.media_paths = []

        # 窗口设置
        self.title("Image Processor")
        self.geometry("400x300")
        self._set_appearance_mode("dark")
        self.attributes('-alpha', 0.9)

        # 主框架
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.pack(expand=True, fill="both", padx=20, pady=20)

        # 图片选择按钮
        self.select_button = ctk.CTkButton(
            self.main_frame,
            text="Select Images",
            command=self.select_images,
            fg_color="black",
            hover_color="#666666",
            border_color="white",
            border_width=1
        )
        self.select_button.pack(pady=10)

        # 应用Mockup按钮
        self.mockup_button = ctk.CTkButton(
            self.main_frame,
            text="Apply Mockup",
            command=self.apply_mockup_background,
            fg_color="black",
            hover_color="#666666",
            border_color="white",
            border_width=1
        )
        self.mockup_button.pack(pady=10)

        # 状态标签
        self.status_label = ctk.CTkLabel(
            self.main_frame,
            text="Ready",
            text_color="white"
        )
        self.status_label.pack(pady=10)

    def select_images(self):
        file_paths = filedialog.askopenfilenames(
            title="Select images",
            filetypes=[("Images", "*.jpg *.png *.jpeg")],
            initialdir=os.path.expanduser("~/Downloads")
        )
        if file_paths:
            self.media_paths = list(file_paths)  # Convert tuple to list
            self.status_label.configure(text=f"{len(file_paths)} images selected")

    def get_dominant_color(self, image):
        # 缩小图像以加快处理速度
        image = image.resize((100, 100))
        # 获取所有像素
        pixels = image.getcolors(10000)
        # 按出现次数排序
        sorted_pixels = sorted(pixels, key=lambda t: t[0], reverse=True)
        # 返回出现最多的颜色
        return sorted_pixels[0][1]

    def apply_mockup_background(self):
        if not self.media_paths:
            self.status_label.configure(text="No images selected")
            return

        new_paths = []
        for path in self.media_paths:
            with Image.open(path) as img:
                # 获取主要颜色
                dominant_color = self.get_dominant_color(img)
                
                # 创建新图像，稍大一些以容纳背景和边框
                width, height = img.size
                new_width, new_height = width + 200, height + 200
                new_img = Image.new('RGB', (new_width, new_height), color='white')
                
                # 创建渐变背景
                gradient = Image.new('RGB', new_img.size, color='white')
                draw = ImageDraw.Draw(gradient)
                for y in range(new_height):
                    r = int(dominant_color[0] * (1 - y / new_height) + 255 * (y / new_height))
                    g = int(dominant_color[1] * (1 - y / new_height) + 255 * (y / new_height))
                    b = int(dominant_color[2] * (1 - y / new_height) + 255 * (y / new_height))
                    draw.line([(0, y), (new_width, y)], fill=(r, g, b))
                
                # 将渐变背景粘贴到新图像上
                new_img.paste(gradient, (0, 0))
                
                # 创建Mac风格的边框
                border = Image.new('RGBA', (width + 40, height + 40), (255, 255, 255, 0))
                draw = ImageDraw.Draw(border)
                draw.rounded_rectangle([0, 0, width + 39, height + 39], radius=20, fill=(255, 255, 255, 255))
                border = border.filter(ImageFilter.GaussianBlur(10))
                draw = ImageDraw.Draw(border)
                draw.rounded_rectangle([3, 3, width + 36, height + 36], radius=20, fill=(60, 60, 60, 255))
                
                # 将原始图像粘贴到边框上
                border.paste(img, (20, 20))
                
                # 将边框粘贴到新图像上
                new_img.paste(border, (80, 80), border)
                
                # 保存新图像
                new_path = f"{os.path.splitext(path)[0]}_mockup.png"
                new_img.save(new_path)
                new_paths.append(new_path)

        self.media_paths = new_paths
        self.status_label.configure(text=f"Applied mockup to {len(self.media_paths)} images")

if __name__ == "__main__":
    app = ImageProcessorApp()
    app.mainloop()
