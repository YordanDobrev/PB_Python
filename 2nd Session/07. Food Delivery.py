chicken_menu = int(input())
fish_menu = int(input())
veggie_menu = int(input())

checkout = (chicken_menu*10.35) + (fish_menu*12.40) + (veggie_menu*8.15)
desert = (checkout * 0.2)+2.50


print(round(checkout+desert,2))