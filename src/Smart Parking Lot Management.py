# Smart Parking Lot Management using Linked List

class CarNode:
    def __init__(self, car_number):
        self.car_number = car_number
        self.next = None

class ParkingLot:
    def __init__(self, capacity):
        self.head = None
        self.capacity = capacity
        self.current_count = 0

    def is_full(self):
        return self.current_count >= self.capacity

    def is_empty(self):
        return self.current_count == 0

    def park_car(self, car_number):
        if self.is_full():
            print(f"🚫 Parking Full! Car {car_number} cannot be parked.\n")
            return
        
        new_car = CarNode(car_number)   # dynamic allocation of a new node
        if not self.head:
            self.head = new_car
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_car
        
        self.current_count += 1
        print(f"✅ Car {car_number} parked successfully.\n")

    def remove_car(self, car_number):
        if self.is_empty():
            print("🚫 Parking lot is empty!\n")
            return
        
        temp = self.head
        prev = None
        while temp:
            if temp.car_number == car_number:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                self.current_count -= 1
                print(f"✅ Car {car_number} exited.\n")
                return
            prev = temp
            temp = temp.next
        print(f"⚠️ Car {car_number} not found in the parking lot.\n")

    def display(self):
        if self.is_empty():
            print("🚗 No cars in the parking lot.\n")
            return
        
        print("🚙 Cars currently parked:")
        temp = self.head
        slot = 1
        while temp:
            print(f"Slot {slot}: Car {temp.car_number}")
            temp = temp.next
            slot += 1
        print()


# Example Usage
def menu():
    lot = ParkingLot(capacity=3)  # set parking capacity
    while True:
        print("1. Park Car\n2. Remove Car\n3. View Parking Lot\n4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            car_num = input("Enter Car Number: ")
            lot.park_car(car_num)
        elif choice == '2':
            car_num = input("Enter Car Number to Remove: ")
