import os
import json

def custom_name_test():  # 移除 self 参数，使其成为普通函数
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__)) #获取当前py文件所在目录
        file_path = os.path.join(current_dir,"test.json") #在当前py文件所在目录寻找test.json
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        print(data["custom_name"]['default'])  # 直接打印数据，无需 self.name
    except FileNotFoundError:
        print("Error: test.json file not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in test.json.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    custom_name_test()