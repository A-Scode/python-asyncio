import asyncio

async def fetch_data(delay , id):
    print("Fetching data... id : " , id )
    await asyncio.sleep(delay)
    print("Data Fetched id : " , id)

    if id == 2 : raise RuntimeError("invalid id")

    return {"data" : "some Data" , "id" : id}


async def main():
    # runs concurrently and store data in list 
    # it will complete other tasks even if some of them fails
    results = await asyncio.gather(fetch_data(3,1) , fetch_data(2,2) , fetch_data(1,3))
    
    for result in results : print("Recieved data : " , result)


asyncio.run(main())

