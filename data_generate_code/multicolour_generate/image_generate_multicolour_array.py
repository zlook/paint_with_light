import json

import cv2


def image_generate_array(image):
    """从x.y为起点画一个图片"""

    # opencv打开一张图片
    img = cv2.imread(image)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 调整图片大小
    height, wight, _ = img.shape
    # print("height, wight", height, wight)
    # print("scalex height, wight", 26, int((26/height)*wight))
    dst = cv2.resize(img, (int((26 / height) * wight), 26), 0, 0)
    src_dst = dst.transpose(1, 0, 2)

    # cv转list
    list_dst_color = src_dst.tolist()

    # 列表翻转/将上下方向调换
    list_dst_color = [list(reversed(i)) for i in list_dst_color]

    # 列表去重将将8种颜色进行提取
    color_type = []
    temp_all_color =[]
    for i in range(len(list_dst_color)):
        for j in range(len(list_dst_color[i])):
            temp_all_color.append(list_dst_color[i][j])
    for item in temp_all_color:
        if item not in color_type:
            color_type.append(item)

    print("color_type->", color_type) # 图片中包含的颜色类型RGB

    string_array = []

    for i in range(len(list_dst_color)):
        sub_string = ""

        for j in range(len(list_dst_color[i])):
            # print(rect_list[i][j])

            if list_dst_color[i][j] == color_type[0]:
                print("00", end="")
                sub_string += "0"

            if list_dst_color[i][j] == color_type[1]:
                print("11", end="")
                sub_string += "1"

            if list_dst_color[i][j] == color_type[2]:
                print("22", end="")
                sub_string += "2"

            if list_dst_color[i][j] == color_type[3]:
                print("33", end="")
                sub_string += "3"

            if list_dst_color[i][j] == color_type[4]:
                print("44", end="")
                sub_string += "4"

            if list_dst_color[i][j] == color_type[5]:
                print("55", end="")
                sub_string += "5"

            if list_dst_color[i][j] == color_type[6]:
                print("66", end="")
                sub_string += "6"

            if list_dst_color[i][j] == color_type[7]:
                print("77", end="")
                sub_string += "7"


        print()

        string_array.append(sub_string)
    return string_array


if __name__ == '__main__':
    # image_array = image_generate_array("./smail.bmp")
    image_array = image_generate_array("./cat.bmp")

    # 存储到当前文件目录
    with open("./image_temp.json", "w") as f:
        f.write(json.dumps(image_array))

