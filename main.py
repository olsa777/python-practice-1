print("Enter customer name: ", end="")
CN=input()
print("Enter product name: ", end="")
PN=input()
print("Enter price per unit (KZT): ", end="")
Price=float(input())
print("Enter quantity: ", end="")
Quantity=int(input())

Subtotal = Price * Quantity
Total=0
Discount = Subtotal * 0.10
if Subtotal > 5000:
    Total=Subtotal-Discount
print()
print()
print("==============================")
print("         SHOP RECEIPT         ")
print("==============================")
print(f"Customer : {CN}")
print(f"Product : {PN}")
print(f"Price : {Price}")
print(f"Quantity : {Quantity}")
print("------------------------------")
print(f"Subtotal : {Subtotal} KZT")
print(f"Discount : {Discount} KZT")
print(f"Total : {Total} KZT")
print("==============================")
    
    

