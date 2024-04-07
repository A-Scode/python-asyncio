import asyncio

async def fetch_data(delay , id):
    print("Fetching data... id : " , id )
    await asyncio.sleep(delay)
    print("Data Fetched id : " , id)
    return {"data" : "some Data" , "id" : id}


async def main():
    tasks = []

    # async context manager
    async with asyncio.TaskGroup() as tg:

        for i , sleep_time in enumerate([3,2,1] ,start=1):
            task = tg.create_task(fetch_data(i , sleep_time))
            tasks.append(task)
    

    # after all tasks completed
    results = [ task.result() for task in tasks]

    for result in results : print("Recieved data is : " , result)
            

asyncio.run(main())