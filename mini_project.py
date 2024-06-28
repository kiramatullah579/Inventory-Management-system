inventory = {
    "Apple_juice":{"price":50,"count":200},
    "Mango_juice":{"price":60,"count":150},
    "Banana_juice":{"price":40,"count":360},
}
def main():
    print("--welcom to Asad cold drink center--")
def add_item():
    name=input("enter the name of items :")
    price=float(input("enter the price of items"))
    count=int(input("enter the quantity of items"))
    inventory[name]={"price":price,"count":count}
    return print(inventory)
def buy_items():
    name=input("enter the name of item :")
    count=int(input("enter the quantity of items :"))
    if name in inventory:
        if inventory[name]["count"]>=count:
            inventory[name]["count"]-=count
            print("items purchased successfully")
        else:
            print("sorry__item not available")
def change_price():
    name=input("enter the name of item :")
    if name in inventory:
        price=int(input("enter the price of the item :"))
        inventory[name]["price"]=price
        print("price updated successfully")
    else:
        print("item not found in inventory")
def update_inventory():
    name=input("enter the name of items :")
    count=int(print("enter the new quantity of items :"))
    for key, velues in inventory.items():
        if key==name:
            inventory[key]["count"]=count
            print("count updated successfully")
            break
    else:
        print("item not available")
        exit()
def desplay_inventory():
    total_sale=0
    print("inventory :")
    for key , values in inventory.items():
        print(f"{key}:{values["count"]}")
        total_sale=values['price']*values['count']
        print(f"total_sale:{total_sale}")
def main():
    while True:
        print("1.Add item")
        print("2.Buy item")
        print("3.change price")
        print("4.display inventory")
        print("5.update inventory count")
        print("6.Add exit")
        try:
            choice=int(input("enter your choice :"))
        except ValueError:
            print("sorry invalid input, pleas enter a numbers.")
            continue
        if choice==1:
            add_item()
        elif choice==2:
            buy_items()
        elif choice==3:
            buy_items()
        elif choice==2:
            change_price()
        elif choice==4:
            desplay_inventory()
        elif choice==5:
            update_inventory()
        elif choice==6:
            exec()
        else:
            print("invalid choice")
            continue
print(inventory)
main()

    





    



 

