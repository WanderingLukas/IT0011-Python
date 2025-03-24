class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return "ID: " +str(self.item_id)+ " \nName: " +self.name+ " \nDescription: " +self.description+  " \nPrice: $" +str(self.price)

class ItemManagement: 
  def __init__ (self):
    self.items = {}
    
    #Creating items
  def create_item(self, item_id, name, description, price):
    try:
      if item_id in self.items:
                raise Exception("Item ID " + str(item_id) + " already exists.")
      if price < 0:
        raise ValueError ("Price cannot be negative.")
      item = Item(item_id, name, description, price)        
      self.items[item_id] = item
      print("Item created successfully: " + str(item))  
    except Exception as e:
        print("Warning: " +str(e))
      
      #Read Items
  def read_item(self, item_id):
        try:
            item = self.items.get(item_id)
            if not item:
                raise Exception("Item with ID " + str(item_id) + " not found. Please create the item first")
            print("Item details:" +str(item))
        except Exception as e:
          print("Warning: " +str(e))
          
    #Updating Items
  def update_item(self, item_id, name=None, description=None, price=None):
      try:
        if item_id not in self.items: 
            raise Exception("Item with ID " + str(item_id) + " not found.")

        item = self.items[item_id]
          
        if name:
            item.name = name
        if description:
            item.description = description
        if price is not None:
            if price < 0:  
                raise ValueError("Price cannot be negative.") 
            item.price = price
        print("Item updated successfully: " +str(item))
            
      except Exception as e:
              print("Warning: " +str(e)) 
                 
    #Deleting Items
  def delete_item(self, item_id):
        try:
            if item_id not in self.items:
                raise Exception("Item with ID " +str(item_id)+ " not found.")
            del self.items[item_id]
            print("Item with ID " +str(item_id)+ " deleted successfully.")
        except Exception as e:
          print("Warning: " +str(e))

    #Listing the Items
  def list_items(self):
        if not self.items:
            print("No items available.")
        else:
            for item in self.items.values():
                print(item)

#options
def options ():
  print("")
  print("Item Managment Menu")
  print("1. Create Item")
  print("2. Read Item")
  print("3. Update Item")
  print("4. Delete Item")
  print("5. List All Items")
  print("6. Exit")
  
  #menu
def main_menu ():
  management = ItemManagement()
  while True:
      options ()
      try:
        choose = int(input("Please select an option using numbers 1-6: "))
        print("")
      except ValueError:
          print("Please enter a number between 1 and 6.")  
          continue
      

      if choose == 1:
                item_id = int(input("Enter Item ID : "))
                name = input("Enter Item Name: ")
                description = input("Enter Item Description: ")
                price = float(input("Enter Item Price: "))
                management.create_item(item_id, name, description, price)
            
      elif choose == 2:
        try:
                item_id = int(input("Enter Item ID to read: "))
                management.read_item(item_id)
        except ValueError:
                print("Item ID must be a number.")
        
      elif choose == 3:
        try:
            item_id = int(input("Enter Item ID to update: "))
            name = input("Enter new Item Name: ")
            description = input("Enter new Item Description: ")
            price_input = input("Enter new Item Price: ")

            price = None
            if price_input.strip():
                    price = float(price_input)
                    
            management.update_item(item_id, name if name else None, description if description else None, price)
        except ValueError:
            print("Price must be a number.")
        
        
      elif choose == 4:
        try:
                item_id = int(input("Enter Item ID to delete: "))
                management.delete_item(item_id)
        except ValueError:
                print("Item ID must be a number.")
            
            
      elif choose == 5:
        management.list_items()
            
            
      elif choose == 6:
        print("Exiting Item Management System.")
        break
      
      else:
        print("Invalid choice. Please enter a number between 1 and 6.")

main_menu()