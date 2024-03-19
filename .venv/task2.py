full_price = 12.0
discount = 0.33
weekday_multiplier = 1.0
weekend_multiplier = 1.2
holiday_multiplier = 1.5

def get_base_price(age):
  if age >= 18:
    return full_price
  else:
    return full_price * (1 - discount)

while True:
  age = int(input("Enter your age: "))
  day = input("Enter the day of the week (Monday-Sunday): ")
  is_holiday = input("Is it a holiday today (yes/no)? ").lower() == "yes"

  base_price = get_base_price(age)

  price_multiplier = weekday_multiplier
  if day.lower() in ["saturday", "sunday"]:
    price_multiplier = weekend_multiplier
  if is_holiday:
    price_multiplier = holiday_multiplier

  final_price = base_price * price_multiplier

  print(f"The ticket price for you is: ${final_price:.2f}")

  choice = input("Do you want to calculate for another person (yes/no)? ").lower()
  if choice == "no":
    break
  elif choice != "yes" and choice != "no":
    print("wrong input")
    break

print("Thank you for using the movie ticket price calculator!")
