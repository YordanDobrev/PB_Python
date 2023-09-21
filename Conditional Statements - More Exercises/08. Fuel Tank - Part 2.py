fuel_type = input()
fuel = float(input())
discount_card = input()

petrol = 2.22 * fuel
diesel = 2.33 * fuel
gas = 0.93 * fuel

petrol_discount = 2.04 * fuel
diesel_discount = 2.21 * fuel
gas_discount = 0.85 * fuel

if discount_card == "Yes":
    if fuel_type == "Gas":
        if fuel > 25:
            print(f'{gas_discount - (gas_discount*0.1):.2f}' + " lv.")
        elif fuel > 20 <= 25:
            print(f'{gas_discount - (gas_discount*0.08):.2f}' + " lv.")
        else:
            print(f'{gas_discount:.2f}' + " lv.")
    elif fuel_type == "Gasoline":
        if fuel > 25:
            print(f'{petrol_discount - (petrol_discount*0.1):.2f}' + " lv.")
        elif fuel > 20 <= 25:
            print(f'{petrol_discount - (petrol_discount*0.08):.2f}' + " lv.")
        else:
            print(f'{petrol_discount:.2f}' + " lv.")
    elif fuel_type == "Diesel":
        if fuel > 25:
            print(f'{diesel_discount - (diesel_discount*0.1):.2f}' + " lv.")
        elif fuel > 20 <= 25:
            print(f'{diesel_discount - (diesel_discount*0.08):.2f}' + " lv.")
        else:
            print(f'{diesel_discount:.2f}' + " lv.")

elif discount_card == "No":
    if fuel_type == "Gas":
        if fuel > 25:
            print(f'{gas - (gas*0.1):.2f}' + " lv.")
        elif fuel > 20 <= 25:
            print(f'{gas - (gas*0.08):.2f}' + " lv.")
        else:
            print(f'{gas:.2f}' + " lv.")
    elif fuel_type == "Gasoline":
        if fuel > 25:
            print(f'{petrol - (petrol*0.1):.2f}' + " lv.")
        elif fuel > 20 <= 25:
            print(f'{petrol - (petrol*0.08):.2f}' + " lv.")
        else:
            print(f'{petrol:.2f}' + " lv.")
    elif fuel_type == "Diesel":
        if fuel > 25:
            print(f'{diesel - (diesel*0.1):.2f}' + " lv.")
        elif fuel > 20 <= 25:
            print(f'{diesel - (diesel * 0.08):.2f}' + " lv.")
        else:
            print(f'{diesel:.2f}' + " lv.")