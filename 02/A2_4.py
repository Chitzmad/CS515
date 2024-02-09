import threading
import time
from queue import Queue

# List of orders
orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']

# Queue to store orders
order_queue = Queue()

# Function to place orders
def place_order(orders):
    for order in orders:
        print(f"Placing order: {order}")
        order_queue.put(order)  # Put the order into the queue
        time.sleep(0.5)  # Simulate some delay between placing orders

# Function to serve orders
def serve_order():
    while True:
        order = order_queue.get()  # Get the order from the queue
        print(f"Serving order: {order}")
        time.sleep(2)  # Simulate some time taken to serve the order

# Create threads for placing orders and serving orders
place_order_thread = threading.Thread(target=place_order, args=(orders,))
serve_order_thread = threading.Thread(target=serve_order)

# Start the thread for placing orders
place_order_thread.start()

# Wait for 1 second before starting the thread for serving orders
time.sleep(1)

# Start the thread for serving orders
serve_order_thread.start()

# Wait for both threads to finish
place_order_thread.join()
serve_order_thread.join()
