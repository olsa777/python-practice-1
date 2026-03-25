customer_name = input("Enter customer name: ")
total_price = 0.0
Quantity = 0

while True:
    product = input("Enter product name (or 'done' to finish): ")
    if product.lower() == 'done':
        break
        
    price = float(input("Enter price: "))
    total_price += price
    Quantity += 1

print(f"\nCustomer : {customer_name.upper()}")
print(f"Items    : {Quantity}")
print(f"Subtotal : {total_price} KZT")

subtotal=0
Discount = 0
if total_price >= 3000 and total_price < 7000:
    Discount = total_pice * 0.05
    subtotal=total_price-Discount
    DT="5%"
elif total_price>7000:
    Discount = total_price * 0.15
    subtotal=total_price-Discount
    DT="15%"
   
if Discount == 0:
    DT="No discount"
    
print(f"\nDiscount tier: {DT}")
print(f"Discount: {Discount}")
print(f"Total: {subtotal}")
print(f"\nName uppercase {customer_name.upper()}")
print(f"Name downcase {customer_name.lower()}")
LN=len(customer_name)
print(f"Name lenght {LN}")
if LN<5:
    print("Short name")
else:
    print("Long name")
