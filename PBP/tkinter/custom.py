# import customtkinter as ctk
# from tkinter import filedialog

# def select_file():
#     file_path = filedialog.askopenfilename(
#         title="选择要上传的文件",
#         filetypes=[("所有文件", "*.*"), ("图片", "*.jpg *.png")],
#         initialdir="/Users/你的用户名/Documents" # 默认打开路径
#     )
#     if file_path:
#         print("已选择文件:", file_path)
#         # 在这里添加文件处理逻辑

# app = ctk.CTk()
# btn = ctk.CTkButton(
#     app, 
#     text="上传文件", 
#     command=select_file,
#     fg_color="#007AFF",  # macOS 系统按钮蓝色
#     hover_color="#0055CC"
# )
# btn.pack(padx=20, pady=20)
# app.mainloop()


# import tkinter as tk
# import customtkinter as ctk

# # 使用 Tk() 作为主窗口（支持透明）
# root = tk.Tk()
# root.attributes("-transparent", True)  # macOS 透明背景
# root.config(bg="systemTransparent")    # 兼容 macOS 透明背景

# # 创建 CustomTkinter 容器（用于承载控件）
# app = ctk.CTkFrame(root, fg_color="#FFFFFF")  # 容器背景设为白色
# app.pack(fill="both", expand=True, padx=20, pady=20)

# # 添加控件到容器
# label = ctk.CTkLabel(app, text="透明背景下的控件")
# label.pack()

# root.mainloop()

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

# import customtkinter as ctk

# ctk.set_appearance_mode("dark")  # 启用暗黑模式

# app = ctk.CTk()
# frame = ctk.CTkFrame(app)
# frame.pack(pady=20)

# # 第一个组件（左对齐）
# btn1 = ctk.CTkButton(frame, text="按钮1", fg_color="#007AFF")
# btn1.pack(side="left", padx=5)

# # 第二个组件（右侧留白）
# btn2 = ctk.CTkButton(frame, text="按钮2", fg_color="#34C759")
# btn2.pack(side="left", padx=5)


# btn3 = ctk.CTkButton(frame, text="按钮3", fg_color="#34C759")
# btn3.pack(padx=5)
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


import customtkinter as ctk

app = ctk.CTk()
app.geometry("600x400")

# 主容器（深灰色背景）
main_frame = ctk.CTkFrame(app, fg_color="#2B2B2B")
main_frame.pack(expand=True, fill="both", padx=10, pady=10)

# 顶部工具栏（蓝色主题）
toolbar = ctk.CTkFrame(main_frame, height=50, fg_color="#007AFF")
toolbar.pack(fill="x", pady=(0, 10))

# 内容区域（嵌套两层）
content_frame = ctk.CTkFrame(main_frame)
content_frame.pack(expand=True, fill="both")

# 左侧边栏（25% 宽度）
sidebar = ctk.CTkFrame(content_frame, width=150, fg_color="#3C3C3C")
sidebar.pack(side="left", fill="y")

# 右侧主内容区（自动扩展）
main_content = ctk.CTkFrame(content_frame)
main_content.pack(side="left", expand=True, fill="both", padx=10)

app.mainloop()