import Huffman_algorithm
import logging
import time


def huffmans_alg(file_name: str, result, *args):
    try:
        logging.info("Thread %s: starting", args)
    except ValueError:
        return 10

    with open('text_files/' + file_name, 'r') as read_file, \
            open('text_files/' + 'result_' + file_name, 'w') as write_res_file:
        for item in read_file:
            # print(item)
            current_line = item
            current_tree = Huffman_algorithm.get_tree(current_line)
            code_line = Huffman_algorithm.get_code(current_tree)
            # write_code_file.write(code_line)
            current_coding_str = Huffman_algorithm.coding(current_line, code_line)
            write_res_file.write(current_coding_str + '\n')

        #time.sleep(2)

        # if current_line == Huffman_algorithm.decoding(current_coding_str, code_line):
        try:
            logging.info("Thread %s: finishing", args)
        except ValueError:
            return 10
        output_str = 'file {} processed successfully '.format(file_name) + 'by thread - {}'.format(args) + '\n'
        result.append(output_str)
        return output_str
