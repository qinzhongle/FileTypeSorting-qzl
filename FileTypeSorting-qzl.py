import os
import shutil

def organize_files_by_extension():
    # 获取当前脚本所在的目录
    current_dir = os.getcwd()

    # 遍历当前目录下的所有文件
    for file_name in os.listdir(current_dir):
        if file_name == 'FileTypeSorting-qzl.exe':
            continue
        file_path = os.path.join(current_dir, file_name)

        # 跳过文件夹，只处理文件
        if os.path.isfile(file_path):
            # 获取文件扩展名（去掉'.'）
            file_extension = file_name.split('.')[-1].lower()

            # 检查文件是否有扩展名
            if len(file_name.split('.')) > 1:
                # 构造目标文件夹路径
                folder_path = os.path.join(current_dir, file_extension)

                # 如果目标文件夹不存在，创建该文件夹
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                # 构造目标文件的路径
                destination_path = os.path.join(folder_path, file_name)

                # 移动文件到对应的文件夹
                shutil.move(file_path, destination_path)

if __name__ == "__main__":
    organize_files_by_extension()
