print("\n\n\n################# ICT-O2 LAB_ACT 01 #################")
print("################# by Rachel Joy P. Pacot #################\n")

print("\n\n################# S T A C K #################\n")
class Stack:
    # This example shows how to implement a stack (toy box) using a list in Python

    def __init__(self):
        self.items = []  # The toy box starts empty.

    def isEmpty(self):
        return self.items == []  # Check if the toy box is empty.

    def push(self, item):
        self.items.append(item)  # Put a toy in the box (on top).

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()  # Take the top toy out.
        return "The toy box is empty!"  # If no toys, say it's empty.

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]  # Look at the top toy without removing.
        return "The toy box is empty!"

    def size(self):
        return len(self.items)  # Count how many toys are in the box.


# Example of using our toy box (stack)
toy_box = Stack()

# Adding toys
toy_box.push("Teddy Bear")
toy_box.push("Toy Car")
toy_box.push("Doll")

# This prints the header
print("\n**** STACK 1: THE TOY BOX ****\n")

# Checking the top toy
print("Top toy:", toy_box.peek())  # This will show the Doll since it was the last one added.

# Taking a toy out
print("Taking out:", toy_box.pop())  # This will take out the Doll since it was the last one added.
print("Taking out:", toy_box.pop())  # This will take out the Toy Car since this was added before the Doll.

# Checking the number of toys left
print("Toys left:", toy_box.size())  # only Teddy Bear remains.

# Taking out the last toy
print("Taking out:", toy_box.pop())  # This will take out the last toy in the box which is the Teddy Bear. This was the last to go since it was the first that was added.
print("Taking out:", toy_box.pop())  # This will show that the toy box is empty since there are no toys left.

####################################################################################################



class Stack:
    def __init__(self):
        self.plates = []  # This is an empty stack of plates.

    def isEmpty(self):
        return self.plates == []  # Check whether there are or there are no plates.

    def push(self, plate):
        self.plates.append(plate)  # This will add a plate to the stack.

    def pop(self):
        if not self.isEmpty():
            return self.plates.pop()  # This will take the top plate
        return "No more plates!"  # If there are no more plates, it will say that the stack is empty.

    def peek(self):
        if not self.isEmpty():
            return self.plates[-1]  # This will let us look at the top plate.
        return "No plates to check!"

    def size(self):
        return len(self.plates)  # Count the number of plates


# 🍽️ Example: Using the Stack of Plates
cafeteria = Stack()

# Adding plates to the stack
cafeteria.push("Blue Plate") # First plate added. This becomes the bottom plate.
cafeteria.push("Yellow Plate") # Second plate added. This is now on top of the Blue Plate.
cafeteria.push("Purple Plate") # Third plate added. This is now on top of the Yellow Plate.
cafeteria.push("Green Plate") # Fourth plate added. This is now on top of the Purple Plate.
cafeteria.push("Red Plate") # Fifth plate added. This is now on top of the Green Plate.

# This prints the header
print("\n\n\n**** 🍽️ STACK 2: THE CAFETERIA PLATES 🍽️ ****\n")

# Checking the top plate
print("Top plate:", cafeteria.peek())  # This will show the Red Plate since it was the last one added.

# Removing plates one by one
print("Taking out:", cafeteria.pop())  # This will take out the Red Plate since it was the last one added.
print("Taking out:", cafeteria.pop())  # This will take out the Green Plate since this was added before the Red Plate.

# Checking how many plates are left
print("Plates left:", cafeteria.size())  # Three plates are left.

# Taking the next plate
print("Taking out:", cafeteria.pop())  # This will take out the Purple Plate since this was added before the Green Plate.
print("Taking out:", cafeteria.pop())  # This will take out the Yellow Plate since this was added before the Purple Plate.
print("Taking out:", cafeteria.pop())  # This will take out the Blue Plate, the first plate of the stack, since this was added before the Yellow Plate.
print("Taking out:", cafeteria.pop())  # There are no more plates!



####################################################################################################
####################################################################################################
####################################################################################################



print("\n\n\n################# Q U E U E #################\n")

from collections import deque

class FlowerQueue:

    
    # This prints the header
    print("\n**** 🌷 QUEUE 1: RYSHCRAFTS ORDERING SYSTEM 🌷 ****\n")

    def __init__(self):
        self.orders = deque()  # this is a Queue to hold flower orders.

    def isEmpty(self):
        return len(self.orders) == 0  # This will check if the queue is empty.

    def add_order(self, customer, bouquet):
        self.orders.append((customer, bouquet))  # Add order to the queue.
        print(f"✅ Order placed: {customer} ordered {bouquet}")

    def serve_order(self):
        if not self.isEmpty():
            customer, bouquet = self.orders.popleft()  # The first one who ordered gets served first.
            print(f"🎉 Order served: {customer} received {bouquet}")
        else:
            print("🚫 No orders left to serve!")

    def next_order(self):
        if not self.isEmpty():
            customer, bouquet = self.orders[0]  # Check the first order.
            print(f"🔜 Next order: {customer} - {bouquet}")
        else:
            print("No pending orders.")

    def queue_size(self):
        return len(self.orders)  # Count pending orders.


# 🌷 Simulating Ryshcrafts Orders
ryshcrafts = FlowerQueue()

# Customers placing orders
ryshcrafts.add_order("Alice", "Fuzzy Bouquet")
ryshcrafts.add_order("Bob", "Everlush Mix")
ryshcrafts.add_order("Charlie", "Mini Daisy Bouquet")

# Checking the next order
ryshcrafts.next_order()  # The next order Ryshcrafts needs to do it from Alice - Fuzzy Bouquet since she was the first one to place an order.

# Serving orders (FIFO - First In, First Out)
ryshcrafts.serve_order()  # Alice gets her bouquet
ryshcrafts.serve_order()  # Bob gets his bouquet after Alice, since he ordered after her.

# Checking queue size
print(f"📦 Pending orders: {ryshcrafts.queue_size()}")  # This will show how many orders are left.

# Serving the last order
ryshcrafts.serve_order()  # Charlie gets his bouquet
ryshcrafts.serve_order()  # No more orders



####################################################################################################


from collections import deque


class TerminalQueue:

    # This prints the header
    print("\n\n**** 🖥️ QUEUE 2: TRANSPORTATION 🖥️ ****\n")

    def __init__(self):
        self.commands = deque()  # This is the Queue to hold terminal commands

    def isEmpty(self):
        return len(self.commands) == 0  # This will check if queue is empty

    def add_command(self, command):
        self.commands.append(command)  # Add command to queue
        print(f"📥 Passenger: {command}")

    def execute_command(self):
        if not self.isEmpty():
            command = self.commands.popleft()  # Process first command
            print(f"⚡ Sent to school: {command}")
        else:
            print("🚫 No passengers left!")

    def next_command(self):
        if not self.isEmpty():
            print(f"🔜 Next passenger: {self.commands[0]}")
        else:
            print("No pending passengers.")

    def queue_size(self):
        return len(self.commands)  # Count pending commands


# 🖥️ Simulating Terminal Command Processing
terminal = TerminalQueue()

# Adding passengers to the queue
terminal.add_command("Rachel")
terminal.add_command("Joy") # Joy is sent to school after Rachel.
terminal.add_command("Hihi") # Hihi is sent to school after Joy.

# Checking the next passenger
terminal.next_command() 

# Sending the passengers to school in FIFO - First In, First Out
terminal.execute_command()
terminal.execute_command()

# Checking queue size
print(f"📦 Pending passengers: {terminal.queue_size()}")  # 1 passenger left

# Sending the last passenger
terminal.execute_command() # Hihi is sent to school
terminal.execute_command()  # No more passengers left.



####################################################################################################
####################################################################################################
####################################################################################################



print("\n\n\n################# A R R A Y #################\n")

# 🌸 Array (List) to store flowers

# This prints the header
print("\n**** 🌸 ARRAY 1: RYSHCRAFTS FLOWER INVENTORY 🌸 ****\n")

flower_inventory = ["Roses", "Tulips", "Lilies", "Daisies", "Sunflowers"]

# 🏷 Displaying all flowers
print("🌼 Flower Inventory:", flower_inventory)

# 📍 Accessing flowers by index
print("🔹 First flower:", flower_inventory[0])  # Roses
print("🔹 Third flower:", flower_inventory[2])  # Lilies

# ✨ Updating a flower type
flower_inventory[1] = "Orchids"  # Replacing Tulips with Orchids
print("🌿 Updated Inventory:", flower_inventory)

# ➕ Adding a new flower to the inventory
flower_inventory.append("Peonies")
print("🌷 After Adding Peonies:", flower_inventory)

# ❌ Removing a flower
flower_inventory.remove("Daisies")
print("🗑 After Removing Daisies:", flower_inventory)

# 🔍 Checking if a flower is in stock
if "Roses" in flower_inventory:
    print("✅ Roses are available!")
else:
    print("❌ Roses are out of stock!")

# 📦 Counting the number of flowers
print("📊 Total flower types:", len(flower_inventory))



####################################################################################################

# This prints the header
print("\n\n**** 📂 ARRAY 2: APPS IN MY COMPUTER 📂 ****\n")

# 📂 Array (List) of installed apps
installed_apps = ["Chrome", "Spotify", "VS Code", "Zoom", "Photoshop"]

# 🖥️ Displaying all installed apps
print("📲 Installed Apps:", installed_apps)

# 🔍 Checking if an app is installed
app_to_check = "Zoom"
if app_to_check in installed_apps:
    print(f"✅ {app_to_check} is installed!")
else:
    print(f"❌ {app_to_check} is not installed!")

# ➕ Installing a new app
new_app = "Discord"
installed_apps.append(new_app)
print(f"📥 Installed {new_app}: {installed_apps}")

# ❌ Uninstalling an app
app_to_remove = "Photoshop"
if app_to_remove in installed_apps:
    installed_apps.remove(app_to_remove)
    print(f"🗑 Uninstalled {app_to_remove}: {installed_apps}")
else:
    print(f"❌ {app_to_remove} is not installed!")

# 📊 Counting installed apps
print("📦 Total Installed Apps:", len(installed_apps))

# 🔄 Updating an app (Replacing an old one)
installed_apps[2] = "Sublime Text"  # Replacing VS Code
print("🔄 Updated App List:", installed_apps)

# 🔢 Accessing an app by index
print("🔹 First installed app:", installed_apps[0])
print("🔹 Last installed app:", installed_apps[-1])



####################################################################################################
####################################################################################################
####################################################################################################


print("\n\n\n################# L I N K E D L I S T S #################\n")

# This prints the header
print("\n**** 🔄 LINKED LIST 1: APP UPDATES 🔄 ****\n")

class Node:
    """Represents an app update in the linked list."""
    def __init__(self, app_name):
        self.app_name = app_name  # Store app name
        self.next = None  # Link to the next app (initially None)


class AppUpdateList:
    """Linked List to manage app updates."""
    def __init__(self):
        self.head = None  # Start with an empty list

    def add_update(self, app_name):
        """Add a new app update to the end of the list."""
        new_node = Node(app_name)
        if self.head is None:  # If the list is empty, set as first app
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Find the last node
                current = current.next
            current.next = new_node  # Attach new update at the end
        print(f"📥 Update queued: {app_name}")

    def remove_update(self, app_name):
        """Remove an app update from the list."""
        current = self.head
        prev = None

        while current and current.app_name != app_name:
            prev = current
            current = current.next

        if current is None:
            print(f"❌ {app_name} not found in update queue!")
            return

        if prev is None:
            self.head = current.next  # Remove the first app update
        else:
            prev.next = current.next  # Skip the removed app

        print(f"🗑 {app_name} removed from updates.")

    def show_updates(self):
        """Display the app updates queue."""
        if self.head is None:
            print("✅ No pending updates!")
            return

        print("🔄 Pending Updates:")
        current = self.head
        while current:
            print(f"   - {current.app_name}")
            current = current.next

    def process_updates(self):
        """Process updates one by one (FIFO)."""
        while self.head:
            print(f"⚡ Updating: {self.head.app_name}")
            self.head = self.head.next  # Move to the next update
        print("✅ All updates installed!")


# 📲 Simulating App Update Queue
updates = AppUpdateList()

# Adding app updates
updates.add_update("Chrome v105")
updates.add_update("Spotify v8.7")
updates.add_update("VS Code v1.70")

# Display pending updates
updates.show_updates()

# Removing an update
updates.remove_update("Spotify v8.7")
updates.show_updates()

# Processing updates
updates.process_updates()

# Checking if all updates are done
updates.show_updates()



####################################################################################################


# This prints the header
print("\n\n**** 🌸🚚    LINKED LIST 2: RYSHCRAFTS FLOWER DELIVERY 🚚🌸 ****\n")

class OrderNode:
    """Represents a flower delivery order."""
    def __init__(self, customer, bouquet):
        self.customer = customer  #  customer name
        self.bouquet = bouquet  #  bouquet type
        self.next = None  # Link to next order (initially None)


class DeliveryQueue:
    """Linked List for managing Ryshcrafts' deliveries."""
    def __init__(self):
        self.head = None  # Start with an empty queue

    def add_order(self, customer, bouquet):
        """Add a new flower delivery order to the queue."""
        new_order = OrderNode(customer, bouquet)
        if self.head is None:
            self.head = new_order  # First order in queue
        else:
            current = self.head
            while current.next:  # Find last order
                current = current.next
            current.next = new_order  # Attach new order at the end
        print(f"📥 New order added: {customer} ordered {bouquet}")

    def deliver_order(self):
        """Deliver the first order in the queue (FIFO)."""
        if self.head is None:
            print("🚫 No pending deliveries!")
            return

        print(f"🚚 Delivering: {self.head.customer} - {self.head.bouquet}")
        self.head = self.head.next  # Move to next order

    def show_orders(self):
        """Display all pending orders."""
        if self.head is None:
            print("✅ No pending deliveries!")
            return

        print("📦 Pending Deliveries:")
        current = self.head
        while current:
            print(f"   - {current.customer} → {current.bouquet}")
            current = current.next

    def cancel_order(self, customer):
        """Remove an order from the queue (if it exists)."""
        current = self.head
        prev = None

        while current and current.customer != customer:
            prev = current
            current = current.next

        if current is None:
            print(f"❌ No order found for {customer}!")
            return

        if prev is None:
            self.head = current.next  # Remove first order
        else:
            prev.next = current.next  # Skip canceled order

        print(f"🗑 Order for {customer} has been canceled.")


# 🌷 Simulating Ryshcrafts' Flower Deliveries
ryshcrafts_deliveries = DeliveryQueue()

# Adding orders
ryshcrafts_deliveries.add_order("Alice", "Fuzzy Bouquet")
ryshcrafts_deliveries.add_order("Bob", "Everlush Mix")
ryshcrafts_deliveries.add_order("Charlie", "Mini Daisy Bouquet")

# Checking pending deliveries
ryshcrafts_deliveries.show_orders()

# Cancelling an order
ryshcrafts_deliveries.cancel_order("Bob")
ryshcrafts_deliveries.show_orders()

# Delivering orders (FIFO)
ryshcrafts_deliveries.deliver_order()  # Alice's order
ryshcrafts_deliveries.deliver_order()  # Charlie's order

# Checking if all deliveries are done
ryshcrafts_deliveries.show_orders()
