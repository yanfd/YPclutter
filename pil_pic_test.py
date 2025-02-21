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
                # 🔄 控制圆角半径的主要参数（可调整这个值）
                RADIUS = 20  # 圆角弧度控制点
                
                dominant_color = self.get_dominant_color(img)
                width, height = img.size
                
                # 🔄 新建画布尺寸计算
                new_size = (int(width*1.2), int(height*1.2))  # 留出阴影空间
                
                # 创建渐变背景
                gradient = Image.new('RGB', new_size, color='white')
                draw = ImageDraw.Draw(gradient)
                for y in range(new_size[1]):
                    # 垂直渐变算法
                    ratio = y / new_size[1]
                    r = int(dominant_color[0] * (1 - ratio) + 255 * ratio)
                    g = int(dominant_color[1] * (1 - ratio) + 255 * ratio)
                    b = int(dominant_color[2] * (1 - ratio) + 255 * ratio)
                    draw.line([(0, y), (new_size[0], y)], fill=(r, g, b))

                # 🔄 创建圆角蒙版
                mask = Image.new('L', img.size, 0)
                draw = ImageDraw.Draw(mask)
                draw.rounded_rectangle([(0,0), img.size], radius=RADIUS, fill=255)
                
                # 应用蒙版
                rounded_img = Image.new('RGBA', img.size, (0,0,0,0))
                rounded_img.paste(img.convert('RGBA'), (0,0), mask)
                
                # 🔄 创建阴影层
                shadow_offset = 25  # 阴影偏移量
                shadow = Image.new('RGBA', 
                    (img.width + shadow_offset, img.height + shadow_offset),
                    (0,0,0,0))
                
                shadow_draw = ImageDraw.Draw(shadow)
                shadow_draw.rounded_rectangle(
                    [(shadow_offset, shadow_offset), 
                    (img.width, img.height)],
                    radius=RADIUS,
                    fill=(0,0,0,100)
                )
                shadow = shadow.filter(ImageFilter.GaussianBlur(10))

                # 合成所有元素
                final_image = gradient.convert('RGBA')
                
                # 🔄 计算正确阴影位置（重要修改）
                image_x = (new_size[0] - width) // 2  # 图片水平居中坐标
                image_y = (new_size[1] - height) // 2  # 图片垂直居中坐标
                
                # 阴影位置 = 图片位置 + 偏移量（右下方向）
                shadow_x = image_x + shadow_offset - 15  # 微调-15补偿阴影绘制偏移
                shadow_y = image_y + shadow_offset - 15
                
                final_image.alpha_composite(shadow, (shadow_x, shadow_y))  # 🔄 更新阴影坐标
                
                final_image.alpha_composite(
                    rounded_img, 
                    (image_x, image_y)  # 🔄 使用计算后的坐标
                )

                # 保存结果
                new_path = f"{os.path.splitext(path)[0]}_mockup.png"
                final_image.save(new_path)
                new_paths.append(new_path)

        self.media_paths = new_paths
        self.status_label.configure(text=f"Applied mockup to {len(self.media_paths)} images")
if __name__ == "__main__":
    app = ImageProcessorApp()
    app.mainloop()
