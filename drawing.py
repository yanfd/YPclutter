from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import ImageFormatter
import numpy as np
from io import BytesIO

def create_mac_style_screenshot(code_text, output_path):
    # 创建背景（带模糊效果）
    bg_size = (1200, 800)
    background = Image.new('RGB', bg_size, (28, 32, 37))
    
    # 生成代码截图
    code_img = generate_code_image(code_text, (900, 600))
    
    # 创建窗口框架
    window_size = (code_img.width + 80, code_img.height + 120)
    window = create_window_frame(window_size)
    
    # 合成图像
    code_position = (40, 80)
    window.paste(code_img, code_position)
    
    # 添加阴影
    final_img = add_shadow(window, blur_radius=20, offset=(0, 10))
    
    # 居中放置到背景
    bg_position = (
        (bg_size[0] - final_img.width) // 2,
        (bg_size[1] - final_img.height) // 2
    )
    background.paste(final_img, bg_position, final_img)
    
    background.save(output_path)

def generate_code_image(code, size):
    """生成带语法高亮的代码图片"""
    formatter = ImageFormatter(
        style="monokai",
        font_name="Courier New",  # 确保字体已安装或指定路径
        font_size=18,
        line_numbers=False,
        image_format="png"
    )
    
    # 生成二进制 PNG 数据
    img_bytes = highlight(code, PythonLexer(), formatter)
    
    # 将 bytes 转换为 PIL Image 对象
    img = Image.open(BytesIO(img_bytes))
    
    # 调整尺寸
    img = img.resize(size, Image.LANCZOS)
    
    return img

def create_window_frame(size):
    """创建Mac风格窗口框架"""
    window = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(window)
    
    # 绘制窗口主体
    body_rect = [(0, 40), (size[0], size[1])]
    draw.rounded_rectangle(body_rect, radius=15, fill=(40, 40, 40))
    
    # 绘制标题栏
    title_bar = [(0, 0), (size[0], 50)]
    draw.rounded_rectangle(title_bar, radius=15, fill=(60, 60, 60))
    
    # 添加控制按钮
    button_colors = [(255, 95, 86), (255, 189, 46), (39, 201, 63)]
    for i, color in enumerate(button_colors):
        draw.ellipse((20 + i*40, 15, 40 + i*40, 35), fill=color)
    
    return window

def add_shadow(image, blur_radius=20, offset=(5, 5), opacity=0.7):
    """添加阴影效果"""
    shadow = Image.new('RGBA', image.size, (0, 0, 0, 0))
    
    # 创建阴影蒙版
    mask = Image.new('L', image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([(0, 0), image.size], radius=15, fill=255)
    
    # 应用模糊
    blurred_mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))
    
    # 创建阴影层
    shadow_layer = Image.new('RGBA', 
        (image.width + 2*blur_radius, 
         image.height + 2*blur_radius), 
        (0, 0, 0, 0))
    
    # 组合阴影
    shadow_layer.paste(
        (0, 0, 0, int(255*opacity)), 
        (blur_radius + offset[0], 
         blur_radius + offset[1]), 
        blurred_mask
    )
    
    # 合并图像和阴影
    final = Image.new('RGBA', shadow_layer.size)
    final.alpha_composite(shadow_layer)
    final.alpha_composite(image, (blur_radius, blur_radius))
    return final

if __name__ == "__main__":
    sample_code = '''def hello_world():
    print("Hello, World!")
    
class Demo:
    def __init__(self):
        self.message = "Mac Style Window"
'''
    create_mac_style_screenshot(sample_code, "output.png")
