import asyncio

orders = [
    ("chips", 8),
    ("lemonade", 3),
    ("soup", 5),
    ("beer", 4)
]

async def cook(order, time_cooking):
    print(f"new order - {order}")
    await asyncio.sleep(time_cooking)
    print(f"{order} -  completed!")
    
def check_kitchen():
        print(f"waiter checking for kitchen...")

async def waiter():
    tasks = []
    for order, time_cooking in orders:
        tasks.append(asyncio.create_task(cook(order, time_cooking)))

    await asyncio.gather(*tasks)

def leave_kitchen():
    print(f"your order is completed! get it!")

check_kitchen()
asyncio.run(waiter())
leave_kitchen()
print(f"cooking is completed!")
