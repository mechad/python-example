import subprocess
import re

def get_system_uptime():
    # 使用subprocess执行cat /proc/uptime命令，并获取输出
    result = subprocess.run(['cat', '/proc/uptime'], stdout=subprocess.PIPE, text=True)
    
    # 转换输出为字符串并分割
    uptime_str = result.stdout.strip()
    idle_str = uptime_str.split()  # 分割秒数和空闲时间
    
    # 提取系统运行时间的浮点数部分
    uptime = float(idle_str[0])
    
    # 返回系统运行时间，单位为秒
    return uptime

# 调用函数并打印结果
uptime_seconds = get_system_uptime()
print(f"System uptime: {uptime_seconds} seconds")
