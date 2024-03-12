import pandas as pd
import argparse

# 创建命令行参数解析器
parser = argparse.ArgumentParser(description='处理Excel文件中指定列的内容')
parser.add_argument('file_path', type=str, help='Excel文件路径')
parser.add_argument('sheet_name', type=str, help='Sheet名称')
parser.add_argument('column_name', type=str, help='要处理的列名')
args = parser.parse_args()

# 读取Excel文件
df = pd.read_excel(args.file_path, sheet_name=args.sheet_name)

# 提取指定列中以特定结尾的内容
def process_content(content):
    valid_extensions = ('exe', 'msi', 'zip', 'rar', '7z')
    if isinstance(content, str) and content.lower().endswith(valid_extensions):
        return content.split('/')[-1]
    print(content)
    return content

# 提取指定列中最后一部分内容
df[args.column_name] = df[args.column_name].apply(process_content)

# 将处理后的数据保存回Excel文件
output_file = 'output_excel_file.xlsx'
df.to_excel(output_file, index=False)

print(f"处理完成，已保存到{output_file}")

