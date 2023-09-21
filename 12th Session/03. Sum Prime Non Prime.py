#Read User Input
command = input()

sum_of_all_prime_numbers = 0
sum_of_all_non_prime_numbers = 0

#Logic

while command != "stop":
    current_number = int(command )
    if current_number < 0:
        print("Number is negative.")
    else:
        current_number_is_prime = True
        for number in range(2, current_number):
            if current_number % number == 0:
                current_number_is_prime = False
                break
        if current_number_is_prime:
            sum_of_all_prime_numbers += current_number
        else:
            sum_of_all_non_prime_numbers += current_number
    command = input()

#Print Output

print(f"Sum of all prime numbers is: {sum_of_all_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_of_all_non_prime_numbers}")