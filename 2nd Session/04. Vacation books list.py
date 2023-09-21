from math import floor
pages = int(input())
page_per_hour = int(input())
days = int(input())

time = pages / page_per_hour

print(floor(time)/days)
