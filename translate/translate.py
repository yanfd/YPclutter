from googletrans import Translator
import asyncio

# 初始化翻译器
translator = Translator()

# Markdown文件路径
markdown_file = "/Users/yanfengwu/Downloads/Obsidian/IELTS/disco elysium.md"

# 检查文件是否存在，如果不存在则创建并写入表头
try:
    with open(markdown_file, "r", encoding="utf-8") as file:
        pass
except FileNotFoundError:
    with open(markdown_file, "w", encoding="utf-8") as file:
        file.write("| 单词 | 含义 |\n")
        file.write("| ---- | ---- |\n")

# 翻译单词（异步调用）
async def translate_word(word):
    translated = await translator.translate(word, src="en", dest="zh-cn")
    return translated.text

# 主循环
async def main():
    while True:
        # 输入英文单词
        word = input("Input (or q): ").strip()

        # 检查是否退出
        if word.lower() == "q":
            print("Exiting the program...")
            print(f"Added to {markdown_file}")
            break

        # 翻译单词
        try:
            translated = await translate_word(word)
        except Exception as e:
            print(f"Translation failed: {e}")
            continue

        # 将结果追加到Markdown文件中
        with open(markdown_file, "r", encoding="utf-8") as file:
            lines = file.read().splitlines()
        word_exists = False
        for line in lines:
            split_word = f" {word} "
            if split_word in line:
                word_exists = True
                print(f'{word} already exists.')
                print(line)
                break
        if word_exists:
            pass
        else:
            with open(markdown_file, "a", encoding="utf-8") as file:
                file.write(f"\n| {word} | {translated} |\n")
            print(f"| {word} | {translated} |\n\n")
            print(f"Added.\n")


# 运行主循环
if __name__ == "__main__":
    asyncio.run(main())