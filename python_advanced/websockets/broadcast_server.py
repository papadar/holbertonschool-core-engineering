#!/usr/bin/env python3
"""Broadcast server using the asyncio API."""

import asyncio
from websockets.asyncio.server import serve

CLIENTS = {}


async def echo(websocket):
    client_id = str(websocket.id)
    CLIENTS[client_id] = websocket
    # print(f"Client connected: {client_id}")

    try:
        async for message in websocket:
            for client in CLIENTS.values():
                await client.send(f"B:{message}")
    finally:
        del CLIENTS[client_id]
        # print(f"Client disconnected: {client_id}")


async def main():
    server = await serve(echo, "127.0.0.1", 8765)
    await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
