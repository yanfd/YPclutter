import tkinter as tk
import customtkinter as ctk

def create_transparent_window():
    root = tk.Tk()
    root.title("透明调试器")
    
    # macOS 透明核心配置
    root.attributes("-transparent", True)
    root.config(bg="systemTransparent")
    root.attributes("-topmost", True)
    root.attributes("-topmost", False)
    
    # 透明中间层
    canvas = tk.Canvas(root, bg="systemTransparent", highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    
    # 内容容器
    container = ctk.CTkFrame(
        canvas,
        fg_color="#FFFFFF",
        border_width=2,
        border_color="#E0E0E0",
        corner_radius=15
    )
    container.pack(padx=40, pady=40)
    
    # 调试控件
    label = ctk.CTkLabel(container, text="✅ 透明背景生效", text_color="#333333")
    label.pack(pady=15)
    
    color_button = ctk.CTkButton(
        container,
        text="切换背景色",
        command=lambda: container.configure(fg_color="#F0F0F0" if container.cget("fg_color") == "#FFFFFF" else "#FFFFFF")
    )
    color_button.pack(pady=5)
    
    exit_button = ctk.CTkButton(
        container,
        text="退出",
        fg_color="#FF4444",
        hover_color="#CC0000",
        command=root.destroy
    )
    exit_button.pack(pady=15)
    
    root.mainloop()

if __name__ == "__main__":
    create_transparent_window()
# import customtkinter as ct

# app = ct.CTk()
# app.title("CustomTkinterAnimalRewrite")
# app.geometry("300x200")

# def update_label(stuff):
#     result_text.configure(text=f'You are a {stuff}')

# app._set_appearance_mode("dark")
# label1 = ct.CTkLabel(app, text='which type of animals you are?').pack(padx=10, pady=10)
# options = ["select:","Dog", "Cat", "Bird", "Fish"]


# xiala = ct.CTkOptionMenu(app,values=options, command=update_label)
# xiala.pack(padx=10, pady=10)

# result_text = ct.CTkLabel(app, text="")
# result_text.pack(padx=10, pady=10)


# app.mainloop()







# # import tkinter as tk

# # root = tk.Tk()
# # root.title("tkinter testing")
# # root.geometry("300x200")

# # label = tk.Label(root, text="which type of animals you are?").pack(padx=10, pady=10)

# # options = [
# #     "Dog",
# #     "Cat",
# #     "Bird",
# #     "Fish"
# # ]

# # selected = tk.StringVar(value="请选择：")
# # xiala = tk.OptionMenu(root, selected, *options)
# # xiala.pack(padx=10, pady=10)

# # result_text = tk.Label(root, text="")
# # result_text.pack(padx=10, pady=10)


# # def update_label(*args):
# #     text = f'You are a {selected.get()}'
# #     result_text.config(text=text)

# # selected.trace_add("write", update_label)


# # if __name__ == "__main__":
# #     root.mainloop()


