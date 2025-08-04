print("Bill Split Calculator")
num1 = float(input())
num2 = float(input())
num_people = int(input())

tip_amount = (num2 / 100) * num1
total_amount = num1 + tip_amount
amount_per_person = total_amount / num_people

print(f"Total (including tip): ${total_amount}")
print(f"Each person pays: ${amount_per_person}")