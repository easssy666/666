"""
循环生成3000个文件，文件内容填一个1
"""
import os
from multiprocessing import Pool
from tqdm import tqdm

def create_file(index):
    filename = f"file_{index}.txt"
    with open(filename, 'w') as f:
        f.write('1')
    return filename

# 使用多进程并发创建文件
if __name__ == '__main__':
    with Pool(processes=4) as pool:
        # 使用tqdm显示进度
        results = list(tqdm(pool.imap(create_file, range(3000)), total=3000))

    print("3000个文件生成完成")


