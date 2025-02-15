import tkinter as tk

root = tk.Tk()
root.title("tkinter testing")
root.geometry("300x200")

label = tk.Label(root, text="which type of animals you are?").pack(padx=10, pady=10)

options = [
    "Dog",
    "Cat",
    "Bird",
    "Fish"
]

selected = tk.StringVar(value="请选择：")
xiala = tk.OptionMenu(root, selected, *options)
xiala.pack(padx=10, pady=10)

result_text = tk.Label(root, text="")
result_text.pack(padx=10, pady=10)


def update_label(*args):
    text = f'You are a {selected.get()}'
    result_text.config(text=text)

selected.trace_add("write", update_label)


if __name__ == "__main__":
    root.mainloop()


