import huffman_function
import threading_function
import async_function
import asyncio


def main():

    # huffman_function.huffmans_alg('test4.txt')
    my_list = ['test1.txt', 'test2.txt', 'test3.txt']
    threading_function.thread_func(my_list)

    #
    # asyncio.run(async_function.async_func('test1.txt'))


    return 0


if __name__ == '__main__':
    main()
