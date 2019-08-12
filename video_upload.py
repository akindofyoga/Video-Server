import asyncio
import websockets
import videoclient_pb2
import os

async def receive(websocket, path):
    raw_update = await websocket.recv()
    update = videoclient_pb2.Update()
    update.ParseFromString(raw_update)

    filename = os.path.basename(update.filename)
    print('received', filename)

    with open(filename, 'wb') as video_file:
        video_file.write(update.video)


def main():
    start_server = websockets.serve(receive, "gs17934.sp.cs.cmu.edu", 8765, max_size=None)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


if __name__ == '__main__':
    main()
