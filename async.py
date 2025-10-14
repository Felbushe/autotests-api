import  time
import asyncio

# def fetch_data():
#     print("Fetching data ...")
#     time.sleep(2)


# for _ in range(5):
#     fetch_data()

#
# async def fetch_data_async():
#     print("Fetching data ...")
#     await asyncio.sleep(2)  # Имитация задержки I/O
#
#
# loop = asyncio.new_event_loop()
# tasks = [
#     loop.create_task((fetch_data_async())),
#     loop.create_task((fetch_data_async())),
#     loop.create_task((fetch_data_async())),
#     loop.create_task((fetch_data_async())),
#     loop.create_task((fetch_data_async())),
#     loop.create_task((fetch_data_async())),
# ]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

async def fetch_data():
    print("Начинаем загрузку...")
    await asyncio.sleep(2)  # Имитация задержки I/O
    print("Данные загружены")
    return {"data": "Пример данных"}

async def main():
    result = await fetch_data()
    print(result)

asyncio.run(main())
