#Read User Input
detergent = int(input())

run_counter = 0
total_pots = 0
total_dishes = 0
total_detergent = 750 * detergent

#Logic

while total_detergent >= 0:
    current_run = input()
    if current_run == "End":
        break
    current_run = int(current_run)
    run_counter += 1
    if run_counter % 3 == 0:
        run_counter = 0
        total_pots += current_run
        total_detergent -= current_run * 15
    else:
        total_dishes += current_run
        total_detergent -= current_run * 5

#Print Output

if total_detergent >= 0:
    print("Detergent was enough!")
    print(f"{total_dishes} dishes and {total_pots} pots were washed.")
    print(f"Leftover detergent {total_detergent} ml.")
else:
    print(f"Not enough detergent, {abs(total_detergent)} ml. more necessary!")