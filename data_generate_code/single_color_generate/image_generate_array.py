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

    # 转list
    list_dst_color = src_dst.tolist()

    # 列表翻转
    list_dst_color = [list(reversed(i)) for i in list_dst_color]

    string_array = []

    for i in range(len(list_dst_color)):
        sub_string = ""

        for j in range(len(list_dst_color[i])):
            # print(rect_list[i][j])

            if list_dst_color[i][j] == [0, 0, 0]:
                print("▇▇", end="")
                sub_string += "1"

            else:
                print("  ", end="")
                sub_string += "0"
        print()

        string_array.append(sub_string)
    return string_array


if __name__ == '__main__':
    image_array = image_generate_array("./wing.png")
    # print(image_array)

    # 存储到当前文件目录
    with open("./image_temp.json", "w") as f:
        f.write(json.dumps(image_array))

