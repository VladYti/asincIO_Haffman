import time
import huffman_function
from threading import Thread
import logging


def thread_func(list_of_readable_files: list, result: list):
    my_format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=my_format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    threads = list()
    # result = []
    for count, item in enumerate(list_of_readable_files):
        logging.info("Main    : create and start thread %d.", count)
        # Создание потоков
        th = Thread(target=huffman_function.huffmans_alg, args=(item, result, count))
        threads.append(th)
        # Запуск потоков
        th.start()
        # return result[count]
        time.sleep(2)
        # return result[count]


    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)

    return result
