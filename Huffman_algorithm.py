# Закодируйте любую строку по алгоритму Хаффмана.
from collections import Counter


class Node:

    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


def get_code(root, codes=None, code=''):
    if codes is None:
        codes = dict()
    if root is None:
        return

    if isinstance(root.value, str):
        codes[root.value] = code
        return codes

    get_code(root.left, codes, code + '0')
    get_code(root.right, codes, code + '1')

    return codes


def get_tree(string):
    string_count = Counter(string)

    if len(string_count) <= 1:
        node = Node(None)

        if len(string_count) == 1:
            node.left = Node([key for key in string_count][0])
            node.right = Node(None)

        string_count = {node: 1}

    while len(string_count) != 1:
        node = Node(None)
        spam = string_count.most_common()[:-3:-1]

        if isinstance(spam[0][0], str):
            node.left = Node(spam[0][0])

        else:
            node.left = spam[0][0]

        if isinstance(spam[1][0], str):
            node.right = Node(spam[1][0])

        else:
            node.right = spam[1][0]

        del string_count[spam[0][0]]
        del string_count[spam[1][0]]
        string_count[node] = spam[0][1] + spam[1][1]

    return [key for key in string_count][0]


def coding(string, codes):
    res = ''

    for symbol in string:
        res += codes[symbol]

    return res


def decoding(string, codes):
    res = ''
    i = 0

    while i < len(string):

        for code in codes:

            if string[i:].find(codes[code]) == 0:
                res += code
                i += len(codes[code])

    return res





# def huffmans_alg(file_name: str):
#     with open(file_name, 'r') as read_file, open('result.txt', 'w') as write_res_file:
#
#
#
#
#         for item in read_file:
#             # print(item)
#             current_line = item
#             current_tree = get_tree(current_line)
#             code_line = get_code(current_tree)
#             # write_code_file.write(code_line)
#             current_coding_str = coding(current_line, code_line)
#             write_res_file.write(current_coding_str + '\n')
#
#             # if current_line == decoding(current_coding_str, code_line):
#         return print('Success')

# return current_coding_str

# with open('result.txt', 'w') as write_res_file, open('test.txt', 'r') as read_file:
#
#     # print(sum(1 for _ in read_file))
#     my_string = read_file.readline(10)
#     tree = get_tree(my_string)
#
#     codes = get_code(tree)
#     print(f'Шифр: {codes}')
#
#     coding_str = coding(my_string, codes)
#     print('Сжатая строка: ', coding_str)
#     write_res_file.write(coding_str + '\n')
#
#     decoding_str = decoding(coding_str, codes)
#     print('Исходная строка: ', decoding_str)
#
#     if my_string == decoding_str:
#         print('Успешно!')
#     else:
#         print('Ошибка!')
