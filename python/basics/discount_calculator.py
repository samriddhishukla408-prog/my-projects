price = float(input("Enter original price (Rs): "))
discount = float(input("Enter discount percentage: "))
discount_amount = (price * discount) / 100
final_price = price - discount_amount
print("Original Price: Rs", price)
print("Discount:", discount, "%")
print("Discount Amount: Rs", discount_amount)
print("Final Price: Rs", final_price)