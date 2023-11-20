import time
import huffman_function
from threading import Thread
import logging


def thread_func(readable_file: str, count: int):
    my_format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=my_format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    threads = list()
    result = str()
    logging.info("Main    : create and start thread %d.", count)
    # Создание потоков
    th = Thread(target=huffman_function.huffmans_alg, args=(readable_file, result, count))
    # Запуск потоков
    th.start()
    time.sleep(2)
    th.join()

    output_str = 'file {} processed successfully '.format(readable_file) + 'by thread - {}'.format(count) + '\n'

    return output_str
