import asyncio

async def fetch_data(delay , id):
    print("Fetching data... id : " , id )
    await asyncio.sleep(delay)
    print("Data Fetched id : " , id)
    return {"data" : "some Data" , "id" : id}


async def main():

    # this will start tasks concurrently

    task1 = asyncio.create_task(fetch_data(3,1))
    task2 = asyncio.create_task(fetch_data(2,2))
    task3 = asyncio.create_task(fetch_data(1,3))

    result1 = await task1
    result2 = await task2
    result3 = await task3

    print(result1 , result2 , result3)


asyncio.run(main())