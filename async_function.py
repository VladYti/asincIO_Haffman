import huffman_function
import asyncio


async def async_func(file_name: str):

    huffman_function.huffmans_alg(file_name, 'async function')
    await asyncio.sleep(2)
    return 20


