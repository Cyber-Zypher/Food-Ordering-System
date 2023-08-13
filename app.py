import pymysql

class FoodOrderingSystem:
    def __init__(self):
        self.db = pymysql.connect(host="localhost", user="UNAME", password="PASSWD", database="DB_NAME")
        self.cursor = self.db.cursor()

    def display_menu(self):
        self.cursor.execute("SELECT * FROM menu")
        menu_items = self.cursor.fetchall()
        print("Menu:")
        for item in menu_items:
            print(f"{item[0]}. {item[1]} - ${item[2]}")

    def place_order(self, item_id, quantity):
        self.cursor.execute("SELECT * FROM menu WHERE id = %s", (item_id,))
        item = self.cursor.fetchone()
        if item:
            total_price = item[2] * quantity
            self.cursor.execute("INSERT INTO orders (item_id, quantity, total_price) VALUES (%s, %s, %s)", (item_id, quantity, total_price))
            self.db.commit()
            print(f"Order placed: {quantity} x {item[1]} - Total: ${total_price}")
        else:
            print("Item not found in the menu.")

    def display_orders(self):
        self.cursor.execute("SELECT orders.id, menu.item_name, orders.quantity, orders.total_price FROM orders INNER JOIN menu ON orders.item_id = menu.id")
        orders = self.cursor.fetchall()
        print("Orders:")
        for order in orders:
            print(f"Order ID: {order[0]}, Item: {order[1]}, Quantity: {order[2]}, Total Price: ${order[3]}")

    def close(self):
        self.db.close()

if __name__ == "__main__":
    system = FoodOrderingSystem()

    while True:
        print("\n1. Display Menu")
        print("2. Place Order")
        print("3. Display Orders")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            system.display_menu()
        elif choice == 2:
            item_id = int(input("Enter item ID: "))
            quantity = int(input("Enter quantity: "))
            system.place_order(item_id, quantity)
        elif choice == 3:
            system.display_orders()
        elif choice == 4:
            system.close()
            print("Thank you for using the Food Ordering System.")
            break
