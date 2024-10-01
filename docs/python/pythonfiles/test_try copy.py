# Subsystem classes
class Inventory:
    def check_stock(self, item):
        print(f"Checking stock for {item}")
        return True

class Payment:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")
        return True

class Notification:
    def send_notification(self, message):
        print(f"Sending notification: {message}")

# Facade class
class OrderFacade:
    def __init__(self):
        self.inventory = Inventory()
        self.payment = Payment()
        self.notification = Notification()

    def place_order(self, item, amount):
        if self.inventory.check_stock(item):
            if self.payment.process_payment(amount):
                self.notification.send_notification(f"Order placed for {item}")
                print("Order processing complete.")
            else:
                print("Payment failed.")
        else:
            print("Item out of stock.")

# Client code
if __name__ == "__main__":
    Facade = OrderFacade()
    Facade.place_order("Laptop", 1500)
