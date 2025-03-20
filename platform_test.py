import platform
system_info=f"{platform.system()} {platform.release()}"
system_info2=f"{platform.system()} {platform.win32_ver()[0]}"
print(system_info)
print(system_info2)


