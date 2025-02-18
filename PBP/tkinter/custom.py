import tkinter as tk
import customtkinter as ctk

# 使用 Tk() 作为主窗口（支持透明）
root = tk.Tk()
root.attributes("-transparent", True)  # macOS 透明背景
root.config(bg="systemTransparent")    # 兼容 macOS 透明背景

# 创建 CustomTkinter 容器（用于承载控件）
app = ctk.CTkFrame(root, fg_color="#FFFFFF")  # 容器背景设为白色
app.pack(fill="both", expand=True, padx=20, pady=20)

# 添加控件到容器
label = ctk.CTkLabel(app, text="透明背景下的控件")
label.pack()

root.mainloop()
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


