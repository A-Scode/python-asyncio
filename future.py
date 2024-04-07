import asyncio

import asyncio

async def fetch_data(future , delay , id):
    print("Fetching data... id : " , id )
    await asyncio.sleep(delay)
    print("Data Fetched id : " , id)
    future.set_result({"data" : "some Data" , "id" : id})

    await asyncio.sleep(delay)
    print("fetch complete") 
    


async def main():
    loop = asyncio.get_running_loop()
    future = loop.create_future()

    task = asyncio.create_task(fetch_data(future , 2 , 1))

    # fetches data before the task complete execution
    result = await future

    print(f"Recieved Data : {result}")

    await task

asyncio.run(main())
