products = []

def readlist() :
    f = open("shoppinglist.txt","r" )
    for l in f :
        product = l.split(',')
        dic = {'ID': product[0],'Name': product[1],'Price':product[2] ,'Count':product[3]}
        products.append(dic)


def menu () :
    while True:
        print("menu: ")
        print('1- Add')
        print('2- Delete ')
        print('3- Search')
        print('4- Buy')
        print('5- Edit')
        print('6- View all products')
        print('7- Exit')


        userpick = int(input("please choose a number: "))
        if userpick == 1:
            add()

        elif userpick == 2:
            delete() 

        elif userpick == 3:
            search()

        elif userpick == 4:
            buy()

        elif userpick == 5:
            edit()

        elif userpick == 6:
            show_products()

        elif userpick == 7:
            print("Done!")
            break

        else:
            print('please try again!')

def add():
    while True:
        id = input('enter the ID number (Enter quit to finish):')
        if id == 'quit': 
            break
        name =input('Enter Name: ')
        for p in products:
            if p['ID'] == id and p['Name'] == name:
                print(f"product {id}  already exists!")
                return
            if p['ID'] == id and p['Name'] != name:
                print(f"product '{id}' already exists with other name!")
                return
            if p['ID'] != id and p['Name'] == name:
                print(f"product '{name}' already exists with other ID!")
                return
            

        price =input('Enter Price:')
        count =input('Enter Count:')
        dic = {'ID':id, 'Name':name, 'Price':price, 'Count': count}
        products.append(dic)
        with open(shoppinglist.txt,'a') as f:  
            line = f"{id},{name},{price},{count}\n"
            f.write(line)
        print('product added!')



def delete():
    while True:
        id = input('Enter the ID number you wanna remove (Enter quit to finish):')
        if id == 'quit': 
            break
        with open('shoppinglist.txt', 'r') as f:
            lines = f.readlines()
        with open('shoppinglist.txt', 'w') as f:
            for line in lines:
                if line.split(',')[0] != id:
                    f.write(line)
        print('product removed!')



def search():
    while True:
        key = input('Enter your key (Enter quit to finish):')
        if key == 'quit': 
            break
        for product in products :
            if key == product['ID'] or key == product['Name'] or key == product['Price'] or key == product['Count']:
                print(product)
                break
        else:
            print('try again!')



def buy():
    cart = []
    total_price = 0
    while True: 
        item_id = input("Enter the ID of your chosen products (Enter quit to finish):")
        if item_id == 'quit': 
            break
        item_found = False
        for product in products:
            if product["ID"] == item_id:
                item_found = True
                count = int(input("Enter the quantity of the product:"))
                if int(product["Count"]) >= count:
                    product["Count"] = str(int(product["Count"]) - count)
                    cart.append({"Name":product["Name"],
                                 "Price":product["Price"],
                                 "Count":count})
                    print("Added to cart!")
                    total_price += int(product["Price"]) * count

                else:
                    print("we are out of source.")
                    print("source:", product["Count"])



        if not item_found:
                print("wrong ID! Try again.")

    print("Cart:", cart)
    print("Total price:", total_price)

    with open("shoppinglist.txt", "w") as f:
        for product in products:
            f.write(product["ID"]+","+product["Name"]+","+product["Price"]+","+product["Count"]+"\n")


        
def edit():
    while True:
        id = input("Enter the ID number of the product you want to edit (Enter quit to finish):")
        if id == 'quit':
            return
        

        for product in products:
            if product['ID'] == id:
                print(" ")
                print('product:')
                print('ID\t Name \t Price \t Count')
                print(product['ID'],'\t',product['Name'],'\t',product['Price'],'\t',product['Count'])
                print(" ")

                while True:
                    print('1- Name')
                    print('2- Price')
                    print('3- Count')
                    choice = input('choose the option you want to edit:')

                    if choice == '1':
                        new_name = input('new name:')
                        product['Name'] = new_name
                        break

                    elif choice == '2':
                        new_price = input('new price:')
                        product['Price'] = new_price
                        break

                    elif choice == '3':
                        new_count = input('new amount:')
                        product['Count'] = new_count
                        break

                    else:
                        print('Try again!')

                with open('shoppinglist.txt', 'w') as f:
                    for product in products:
                        line = f"{product['ID']},{product['Name']},{product['Price']},{product['Count']}\n"
                        f.write(line)
                
                print('The list is up to date!')
                break
            
        else:
            print('Try again!')

def show_products() :
    print('ID \t Name \t Price \t Count')
    for product in products :
        print(product['ID'],'\t',product['Name'],'\t',product['Price'],'\t',product['Count'])
readlist()
menu()