import binascii
import copy
import os
import time
import json

KEYS = [0x80, 0x40, 0x20, 0x10, 0x08, 0x04, 0x02, 0x01]


def generate_content(content, top_fill="10101", btm_fill="10101"):
    rect_list = [[] for _ in range(16)]

    for text in content:

        if is_Chinese(text):
            hans_list = tran_hans(text)
            rect_list = [rect_list[i] + hans_list[i] for i in range(len(rect_list))]

        else:
            asc_list = tran_asc(text)

            rect_list = [rect_list[i] + asc_list[i] for i in range(len(rect_list))]

    # 矩阵转置
    rect_list = _list_trans(rect_list)

    # 列表翻转
    rect_list = [list(reversed(i)) for i in rect_list]

    string_array = []
    # 字符打印
    for i in range(len(rect_list)):
        sub_string = ""

        for j in range(len(rect_list[i])):
            # print(rect_list[i][j])

            if rect_list[i][j] == 0:
                print("  ", end="")
                sub_string += "0"
            else:
                print("▇▇", end="")
                sub_string += "1"
        string_array.append(top_fill + sub_string + btm_fill)

        print("")

    # print(len(string_array[1]))
    # print(len(string_array), string_array)

    return string_array


def _list_trans(l):
    """矩阵转置"""
    l = zip(*l)
    l = [list(i) for i in l]
    return l


def tran_hans(string, font_file="./fonts/hzk16"):
    hans_list = [[] for _ in range(16)]

    # 获取中文的gb2312编码，一个汉字是由2个字节编码组成
    gb2312 = string.encode('gb2312')

    # # 将二进制编码数据转化为十六进制数据, 将数据按unicode转化为字符串
    result = str(binascii.b2a_hex(gb2312), encoding='utf-8')
    # 前两位对应汉字的第一个字节：区码，每一区记录94个字符, 后两位对应汉字的第二个字节：位码，是汉字在其区的位置
    area, index = eval('0x' + result[:2]) - 0xA0, eval('0x' + result[2:]) - 0xA0

    # 汉字在HZK16中的绝对偏移位置，最后乘32是因为字库中的每个汉字字模都需要32字节
    offset = (94 * (area - 1) + (index - 1)) * 32

    # 读取HZK16汉字库文件
    with open(font_file, "rb") as f:
        # 找到目标汉字的偏移位置
        f.seek(offset)
        # 从该字模数据中读取32字节数据
        font_rect = f.read(32)

    # font_rect的长度是32，此处相当于for k in range(16)
    for k in range(len(font_rect) // 2):
        # 每行数据
        row_list = hans_list[k]

        for j in range(2):
            for i in range(8):
                asc = font_rect[k * 2 + j]
                # 此处&为Python中的按位与运算符
                flag = asc & KEYS[i]
                # 数据规则获取字模中数据添加到16行每行中16个位置处每个位置
                row_list.append(flag)

    return hans_list


def tran_asc(string, font_file="./fonts/ASC16"):
    """将asc转换为list"""
    asc_list = []

    offset = ord(string) * 16

    with open(font_file, "rb") as f:
        f.seek(offset)
        font_rect = f.read(15)

    for k in font_rect:
        asc_list.append(bin(k)[2:].zfill(8))

    if len(asc_list) < 16:
        fill_len = 16 - len(asc_list)
        diff_list = ["0" * 8 for _ in range(fill_len)]
        display_list = diff_list + asc_list

    else:
        display_list = asc_list

    other_list = [[int(j) for j in i] for i in display_list]

    return other_list


def is_Chinese(word):
    """
    判断是否为中文
    :param word:
    :return:
    """
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


if __name__ == '__main__':
    string_array = generate_content("中国加油")

    # 存储到当前文件目录
    with open("./font_temp.json", "w") as f:
        f.write(json.dumps(string_array))

