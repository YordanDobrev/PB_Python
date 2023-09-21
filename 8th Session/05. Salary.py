#Read User Input
tabs = int(input())
salary = float(input())

summ = 0

#Logic

for i in range (tabs):
    current_tab = input()
    if current_tab == "Facebook":
        summ += 150
    elif current_tab == "Instagram":
        summ += 100
    elif current_tab == "Reddit":
        summ += 50
    if summ >= salary:
        break

#Print Output

if summ >= salary:
    print(f"You have lost your salary.")
else:
    difference = abs(summ-salary)
    print(int(difference))