import asyncio


#coroutine function
async def main():
    print("Strat of main coroutine function")


# main() returns -> Coroutine Object

# gives coroutine object it need to be awaited
print(main())

# takes a coroutine object
asyncio.run(main())



async def fetch_data(delay , id):
    print("Fetching data... id : " , id )
    await asyncio.sleep(delay)
    print("Data Fetched")
    return {"data" : "some Data" , "id" : id}

async def show_data():
    task1 = fetch_data(2 , 1)
    task2 = fetch_data(2 , 2)
    print("End of coroutine")

    # coroutine only starts running when it is awaited
    res1 = await task1
    print("Recieved Result : " , res1)
    res2 = await task2
    print("Recieved Result : " , res2)


asyncio.run(show_data())
