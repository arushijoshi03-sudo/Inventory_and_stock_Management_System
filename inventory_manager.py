class Item:
    def __init__(self, name , quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
            return f"{self.name} | Qty: {self.quantity} | Price: ₹{self.price}"

def show_inventory(items):
    if not items:
         print("No items in inventory.")
    else:
       print("\n--- Inventory Report ---") 
       total_values = 0
       for i in items:
           if i.quantity < 5:
               print(f"{i} Low Stock!")
           else:
               print(i)
           total_value =+ (i.quantity * i.price) 
       print(f"\nTotal Inventory Value: ₹{total_value}")


def save_inventory(items, filename="inventory.txt"):
     with open(filename, "w") as f:
          for i in items:
              f.write(f"{i.name},{i.quantity},{i.price}\n")

def load_inventory(filename="inventory.txt"):
    items =[]
    try:
        with open(filename,"r") as f:
            for line in f:
                name, qty, price = line.strip().split(",")
                items.append(Item(name, int(qty), float(price)))
    except FileNotFoundError:
        pass
    return items                  
def menu():
     items = load_inventory()  #simpe python list to store inventory
     while True:
          print("\n--- Inventory & Stock Management (Python Essentials) ---")
          print("1. Add Item")
          print("2. View Inventory")
          print("3. Update Stock")
          print("4. Issue Item (Sale)")
          print("5. Delete item")
          print("6. Exit")
          print("7. Top 3 Expensive Items")
          print("8. Highest Stock Item")
          print("9. Low Stock Report")

          choice = input("Enter choice: ")

          if choice =="1":
               name = input("Enter item name: ")
               qty = int(input("enter quantity: "))
               price = float(input("Enter price: "))
               items.append(Item(name, qty, price))

          elif choice == "2":
               return show_inventory(items)

          elif choice == "3":
              name = input("Enter item name to update: ")
              for i in items:
                    if i.name == name:
                         qty = int(input("Enter new  quantity: "))
                         i.quantity = qty
                         print("Stock updated")
                         break
                    else:
                         print("item not found.")

          elif choice == "4":
               show_inventory(items)
               name = input("Enter item name to issue: ")
               for i in items:
                    if i.name == name:
                         qty = int(input("Enter quantity to issue: "))
                         if qty <= i.quantity:
                              i.quantity -= qty
                              print("Item issued")
                         else:
                              print("Not enough stock")
                         break
                    else:
                         print("Item not found.")
          elif choice == "5":
               show_inventory(items)
               name = input("Enter item name to delete : ")
               items = [i for i in items if i.name.lower() != name.lower()]
               print("Item deleted")

          elif choice == "6":
               print("Goodbye ")
               save_inventory(items)
               print("Inventory saved to file. Goodbye")
               break
        

          elif choice =="7":
              top_items = sorted(items, key=lambda x: x.price, reverse=True)[:3]
              print("\n--- Top 3 Expensive Items---")
              for i in top_items:
                  print(i)

          elif choice =="8":
              if items:
                  max_item = max(items, key=lambda x: x.quantity)
                  print(f"\nHighest Stock Item: {max_item}")
              else:
                  print("No items in inventory.")

          elif choice =="9":
              print("\n--- Low Stock report ---")
              low_items = [i for i in items if i.quantity < 5]
              if not low_items:
                  print("No items are low in stock.")
              else:
                  for i in low_items:
                      print(f"{i} low stock!")

          else:
              print("Invalid choice. Try again.")

if __name__ == "__main__":
     menu()

                                    

                     
                                   

        
                     
            