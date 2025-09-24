# 生成的原始input.json文件格式形如["第一篇文章的正文", "第二篇文章的正文", "第三篇文章的正文"]
import os
import json
import glob
import re

def process_text_files_to_json(target_directory):
    """
    将目标目录下的所有txt文件内容读取并生成input.json文件
    
    Args:
        target_directory (str): 目标目录路径
    """
    
    # 检查目录是否存在
    if not os.path.exists(target_directory):
        print(f"错误：目录 '{target_directory}' 不存在")
        return False
    
    # 获取目录下所有的txt文件
    txt_files = glob.glob(os.path.join(target_directory, "*.txt"))
    
    if not txt_files:
        print(f"在目录 '{target_directory}' 中未找到任何txt文件")
        return False
    
    print(f"找到 {len(txt_files)} 个txt文件")
    
    articles = []
    
    # 逐个读取txt文件
    for i, txt_file in enumerate(txt_files, 1):
        try:
            with open(txt_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # 去除英文引号（双引号和单引号）
            content = content.replace('"', '').replace("'", '')
            
            # 可选：去除多余的空行和空白字符
            content = re.sub(r'\n\s*\n', '\n\n', content.strip())
            
            articles.append(content)
            print(f"已处理第 {i} 个文件: {os.path.basename(txt_file)}")
            
        except Exception as e:
            print(f"处理文件 {txt_file} 时出错: {str(e)}")
            continue
    
    if not articles:
        print("没有成功读取到任何文章内容")
        return False
    
    # 生成output.json文件路径
    output_path = os.path.join(target_directory, "input.json")
    
    try:
        # 将文章列表写入JSON文件
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(articles, f, ensure_ascii=False, indent=2)
        
        print(f"\n成功生成 {output_path}")
        print(f"共处理 {len(articles)} 篇文章")
        return True
        
    except Exception as e:
        print(f"写入JSON文件时出错: {str(e)}")
        return False

def main():
    # 使用方法1：直接指定目录
    target_dir = "./novel_corpus-main/original_data"  # 修改为你的目标目录
    
    # 使用方法2：通过命令行参数获取目录
    # import sys
    # if len(sys.argv) > 1:
    #     target_dir = sys.argv[1]
    # else:
    #     target_dir = input("请输入目标目录路径: ")
    
    # 执行处理
    process_text_files_to_json(target_dir)

if __name__ == "__main__":
    main()