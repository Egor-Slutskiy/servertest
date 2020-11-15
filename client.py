import asyncio


async def tcp_echo_client():
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    while True:

        msg = input()
        print(f'Send: {msg!r}')
        writer.write(msg.encode())

        data = await reader.read(100)
        print(f'Received: {data.decode()!r}')

asyncio.run(tcp_echo_client())