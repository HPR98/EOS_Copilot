from pythonosc.osc_server import AsyncIOOSCUDPServer
from pythonosc.dispatcher import Dispatcher
import asyncio
from osc_handler import message_handler


dispatcher = Dispatcher()
dispatcher.map("*", message_handler)

ip = "127.0.0.1"
port = 8001


async def loop():
    for i in range(999999999999999):
        print("Loop")
        await asyncio.sleep(1)


async def init_main():
    server = AsyncIOOSCUDPServer((ip, port), dispatcher, asyncio.get_event_loop())
    transport, protocol = await server.create_serve_endpoint()  # Create datagram endpoint and start serving

    await loop()  # Enter main loop of program

    transport.close()  # Clean up serve endpoint

def run_server():
    asyncio.run(init_main())

if __name__ == "__main__":
    run_server()
