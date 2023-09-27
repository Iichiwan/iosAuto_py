import os
from PIL import Image

if __name__ == '__main__':
    # 定义图片路径和文件名前缀
    input_folder  = "C:/Users/86139/Desktop/mmdoutput/ed_output/"

    # 生成GIF的文件名和路径
    output_file = "output.gif"
    output_path = os.path.join(input_folder, output_file)

    # 调整GIF帧的延迟时间（以毫秒为单位）
    frame_duration = 100

    # 获取输入文件夹中的所有图像文件
    image_file_list = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if
                       f.endswith(".jpg") or f.endswith(".png")]

    # 打开所有图像文件并将它们存储在Pillow对象中
    image_list = []
    for image_file in image_file_list:
        image = Image.open(image_file)
        image_list.append(image)

    # 将第一张图像作为基准帧，并将其转换为GIF格式
    base_image = image_list.pop(0)
    base_image.save(output_path, save_all=True, append_images=image_list, duration=frame_duration)
