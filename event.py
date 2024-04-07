import asyncio

async def waiter(event: asyncio.Event):
    print("waiting for event to be set")
    await event.wait()
    print("event completed!!")

async def setter(event: asyncio.Event):
    print("setting the event")    
    await asyncio.sleep(2)
    event.set()
    print("Event has been set")

async def main():
    event : asyncio.Event = asyncio.Event()
    await asyncio.gather(setter(event) , waiter(event))

asyncio.run(main())
