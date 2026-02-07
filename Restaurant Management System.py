# سیستم مدیریت رستوران 

#این پروژه یک برنامه پایتون برای مدیریت رستوران است.  
#در این نسخه، همه اطلاعات منو و سفارش‌ها فقط در حافظه برنامه ذخیره می‌شوند و پس از بسته شدن برنامه پاک می‌شوند.

## ویژگی‌ها:

#- افزودن غذا با نام، قیمت و موجودی
#- ویرایش غذا
#- حذف غذا
#- مشاهده منو
#- ثبت سفارش با محاسبه مبلغ کل
#- مشاهده سفارش‌ها
#- منوی انتخابی برای کاربر
#- خروج از برنامه

## نحوه اجرا:

#1. کد را اجرا کنید.
#2. گزینه مورد نظر از منو را انتخاب کنید.
#3. اطلاعات غذا یا سفارش را وارد کنید.
#4. برای خروج از برنامه گزینه 7 را انتخاب کنید.



# Restaurant Management System 

#This project is a Python program to manage a restaurant.  
#In this version, all menu and order information is stored only in the program memory and will be lost when the program is closed.

## Features:

#- Add food with name, price, and stock
#- Edit food
#- Delete food
#- Show menu
#- Place orders with total calculation
#- View all orders
#- User menu for actions
#- Exit the program

## How to run:

#1. Run the code.
#2. Choose an option from the menu.
#3. Enter food or order details.
#4. To exit the program, choose option 7.






from datetime import datetime

menu = []
orders = []

while True:
    print("\n--- Restaurant Management System ---")
    print("1. Add food")
    print("2. Edit food")
    print("3. Delete food")
    print("4. Show menu")
    print("5. Place order")
    print("6. Show orders")
    print("7. Exit")
    
    choice = input("Choose an option (1-7): ")

    if choice == "1":
        name = input("Enter food name: ")
        price = float(input("Enter price: "))
        stock = int(input("Enter stock quantity: "))
        food = {"name": name, "price": price, "stock": stock}
        menu.append(food)
        print(f"{name} added to menu successfully!")

    elif choice == "2":
        edit_name = input("Enter food name to edit: ")
        found = False
        for food in menu:
            if food["name"] == edit_name:
                found = True
                food["price"] = float(input("Enter new price: "))
                food["stock"] = int(input("Enter new stock: "))
                print(f"{edit_name} updated successfully!")
                break
        if not found:
            print("Food not found in menu.")

    elif choice == "3":
        del_name = input("Enter food name to delete: ")
        found = False
        for food in menu:
            if food["name"] == del_name:
                menu.remove(food)
                found = True
                print(f"{del_name} removed from menu.")
                break
        if not found:
            print("Food not found in menu.")

    elif choice == "4":
        if not menu:
            print("Menu is empty.")
        else:
            for food in menu:
                print(f"Name: {food['name']} | Price: {food['price']} | Stock: {food['stock']}")

    elif choice == "5":
        order_name = input("Enter food name to order: ")
        quantity = int(input("Enter quantity: "))
        found = False
        for food in menu:
            if food["name"] == order_name:
                found = True
                if food["stock"] >= quantity:
                    food["stock"] -= quantity
                    total = food["price"] * quantity
                    order = {"name": order_name, "quantity": quantity, "total": total, "date": str(datetime.now())}
                    orders.append(order)
                    print(f"Order placed! Total amount: {total}")
                else:
                    print("Insufficient stock!")
                break
        if not found:
            print("Food not found.")

    elif choice == "6":
        if not orders:
            print("No orders placed yet.")
        else:
            for o in orders:
                print(f"{o['date']} - {o['name']} x{o['quantity']} - Total: {o['total']}")

    elif choice == "7":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")
