from collections import deque

orders_complete = True
quantity_of_food = int(input())
orders = input().split()
orders_deque = deque(map(int, orders))
print(max(orders_deque))

for x in range(len(orders_deque.copy())):
    current_order = int(orders_deque[0])
    if current_order <= quantity_of_food:
        orders_deque.popleft()
        quantity_of_food -= current_order
    else:
        orders_complete = False
        break

if orders_complete:
    print("Orders complete")
else:
    orders_deque = deque(map(str, orders_deque))
    print(f"Orders left: {' '.join(orders_deque)}")
