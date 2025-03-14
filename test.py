# x,y为正整数，求x的y次方的个位数是多少
# 输入描述：依次输入两个数（每行一个），第一个为x，第二个为y 
# 输出描述：输出个位数

# def last_digit_of_power(x, y):
#     last_digit_x = x % 10
#     if y == 0:
#         return 1

#     y_mod = y % 4
#     if y_mod == 0:
#         y_mod = 4 

#     result = (last_digit_x ** y_mod) % 10
#     return result

# # 输入
# x = int(input())
# y = int(input())

# # 输出
# print(last_digit_of_power(x, y))

#2
# def max_rotated_number(n):
#     s = str(n)  
#     max_num = n  
#     k = len(s)   
    
#     for i in range(1, k):
        
#         rotated = s[-i:] + s[:-i]
#         if int(rotated) > max_num:
#             max_num = int(rotated)
    
#     return max_num

# # 输入
# n = int(input())

# # 输出
# print(max_rotated_number(n))
    
# import re

# def is_valid_dns_domain(domain):
#     if len(domain) > 255:
#         return False
    
#     labels = domain.split('.')
#     if len(labels) < 2:
#         return False
    

#     for label in labels:
#         if len(label) > 63:
#             return False
#         if label.startswith('-') or label.endswith('-'):
#             return False
#         if not re.match(r'^[a-zA-Z0-9-]+$', label):
#             return False
    
#     return True

# # 输入
# domain = input().strip()

# # 输出
# print(is_valid_dns_domain(domain))

#4
def min_edit_time(T, test_cases):
    results = []
    for case in test_cases:
        n, k, tasks = case
        min_time = float('inf')
        
        for i in range(n - k + 1):
            selected = tasks[i:i + k]
            left, right = 0, k
            while left < right:
                mid = (left + right) // 2
                xiaoming = sum(selected[:mid])
                xiaobai = sum(selected[mid:])
                current_max = max(xiaoming, xiaobai)
                min_time = min(min_time, current_max)
                if xiaoming < xiaobai:
                    left = mid + 1
                else:
                    right = mid
        results.append(min_time)
    return results

# 输入
T = int(input())
test_cases = []
for _ in range(T):
    n, k = map(int, input().split())
    tasks = list(map(int, input().split()))
    test_cases.append((n, k, tasks))

# 输出
results = min_edit_time(T, test_cases)
for res in results:
    print(res)
