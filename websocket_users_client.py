import asyncio # Импортируем asyncio для работы с асинхронными операциями

import  websockets # Импортируем библиотеку для работы с WebSockets

async def client():
    uri = "ws://localhost:8765" # Адрес сервера
    async with websockets.connect(uri) as websocket:
        message = "Привет, сервер!" # Сообщение, которое отправит клиент
        print(f"Отправка: {message}")
        await websocket.send(message) # Отправляем сообщение

        for _ in range(5):
            message = await websocket.recv() # Получаем ответ от сервера
            print(message)


asyncio.run(client()) # Запускаем асинхронную функцию клиента