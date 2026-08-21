price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: "))
total_cost = price * quantity

print("Total cost: ", total_cost)

discount = float(input("Enter the discount percentage: "))
gst = float(input("Enter the GST percentage: "))

discount_amount = total_cost * (discount / 100)
gst_amount = total_cost * (gst / 100)
final_cost = total_cost - discount_amount + gst_amount

print("Final cost after discount and GST: ", final_cost)
payment_method = input("Enter the payment method (cash/card): ")

if payment_method.lower() == "cash":
    print("Payment method: Cash")
elif payment_method.lower() == "card":
    print("Payment method: Card")

