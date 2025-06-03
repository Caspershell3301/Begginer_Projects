print("Welcome to the Pizza Ordering Portal ;) ")
size = input("What size pizza you want? S, M, L ").strip().lower()
add_pepperoni = input("Do you want pepperoni? Y or N ").strip().lower()
extra_cheese = input("Do you want extra Cheese? Yes or No ").strip().lower()

# From below is my code :)
bill = 0

if size == "l":
    bill += 25
    if add_pepperoni == "y":
        bill += 3
    else:
        bill += 0
elif size == "m":
    bill += 20
    if add_pepperoni == "y":
        bill += 3
    else:
        bill += 0
elif size == "s":
    bill += 15
    if add_pepperoni == "y":
        bill += 2

else:
    print("Enter Valid Option (S, M, L")

if extra_cheese == "y":
    bill += 1

print(f"\n Thank You for Ordering!! Your total bill is Rs. {bill}/-")
print("Enjoy your meal :) ")



