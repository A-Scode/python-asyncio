import asyncio

shared_var = 0 

lock = asyncio.Lock()

async def modify_shared_var():

    global shared_var 
    async with lock:
        # Critical Section 
        print("Before Modify Shared Variable : " , shared_var)
        shared_var += 1 
        await asyncio.sleep(2)
        print("After Modify Shared Variable : " , shared_var)
    
async def main():
    await asyncio.gather( *(modify_shared_var() for _ in range(5)))

asyncio.run(main())