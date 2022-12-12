import qrcode

products = []

def read_from_database():
    f = open('database.txt', 'r')

    for line in f:
        result = line.split(', ')
        my_dict = {'code': result[0], 'name': result[1], 'price': result[2], 'count': result[3]}

        products.append(my_dict)


    f.close()

def write_to_database():
    ff = open('database.txt', 'w')
    for product in products:
        ff.write(f"{product['code']},{product['name']},{product['price']},{product['count']}\n")
    ff.close()
        
def find_product(code=0, name=0):
    for product in products:
        if product['code'] == code or product["name"] == name:
            return product
    else:
        return False        

    
def show_menu():
    print('1-add')
    print('2- Edit')
    print('3- Remove')
    print('4- Search')
    print('5- Show List')
    print('6- Buy')
    print('7- Make QR Code')
    print('8 - Exit')

def add():
    code = input('enter code: ')
    name = input('enter name: ')
    price= input('enter price: ')
    count= input('enter count: ')
    new_product = {'code': code, 'name': name, 'price': price, 'count': count}
    products.append(new_product)

def edit():
    user_input = input('Enter the product code: ')
    for product in products:
        if product['code'] == user_input: 
            editable = input('Edit Name, Price or Count?! ')
            for i in products:
                   if i['code'] == product['code']:
                        i[editable] = input('Enter New Value for this product: ')
            print('Product features Updated Successfully')
        else:
            print('Product not Found!')

def remove():
    code = input('Enter the code of the Product you want to remove: ')
    for product in products:
        if  product['code'] == code:
            del product['code']
            del product['name']
            del product['price']
            del product['count']
            print('Product was successfully removed!')
            break
    else:
        print('Product not Found!!')

def search():
    user_input = input('type your keyword: ')
    for product in products:
        if product['code'] == user_input or product['name'] == user_input:
            print(product["code"], "\t\t", product["name"], "\t\t", product["price"])
            break
    else:
        print('not found')
            

def show_list():
    print("code\t\tname\t\tprice")
    for product in products:
        print(product["code"], "\t\t", product["name"], "\t\t", product["price"])

def buy():
    cart = []
    while True:
        user_input = input("Enter the product code for buying a product and enter 0 for back to menu: ")
        if user_input == "0":
            total_price = 0
            print("name\t\tcount\t\tprice")
            for product in cart:
                total_price += int(product["price"])
                print(f"{product['name']}\t\t{product['count']}\t\t{product['price']}")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Total Price:", total_price)
            break
        product = find_product(code=user_input)
        if product:
            count = int(input("How many of this product do you want? "))
            if int(product["count"]) >= count:
                for obj in products:
                    if product["code"] == obj["code"]:
                        obj["count"] = int(obj["count"]) - count
                        cart.append({
                            "name": obj["name"],
                            "count": count,
                            "price": int(obj["price"])*count
                            })
                        break
            else:
                print("Insufficient inventory")
        else:
            print("Product not found.")
            


def make_qrcode():
    user_input = input('type your keyword: ')
    for product in products:
        if product['code'] == user_input:
            q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
            q.add_data(product['code'])
            q.add_data('|')           
            q.add_data(product['name'])
            q.add_data('|')           
            q.add_data(product['price'])
            q.add_data('|')
            q.add_data(product['count'])
            q.add_data('|')
            i = q.make_image(fill_color = 'black', back_color = 'green')
            i.save(f"{product['code']}.png")
            break
    else:
        print('Product not Found')
                   

print('Welcome to the Store')
print('Loading...')
read_from_database()
print('Data loaded.')

while True:
    show_menu()
    choice = int(input('Enter your choice:  '))

    if choice == 1:
        add()
    elif choice == 2:
        edit()
    elif choice == 3:
        remove()
    elif choice == 4:
        search()
    elif choice == 5:
        show_list()
    elif choice == 6:
        buy()
    elif choice == 7:
        make_qrcode()
    elif choice == 8:
        write_to_database()
        exit(0)
    else:
        print('Wrong Choice!!')