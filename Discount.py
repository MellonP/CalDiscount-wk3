Question 1
# calculate discount based on the amount and given discount

discount = calculate_discount(original_price, discount_percent)
print(f"Discount_percent: ${discount_percent:.2f}")

if discount_percent == 20:
    print("Discount Applied")
else:
    print("Original Price")


Question 2
# getting user input

price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percent: "))

discount_amount = calculate_discount(price, discount_percent)
final_price = price - discount_percent

print(f"final price after discount: R{final_price:.2f}")
# the price i need to pay