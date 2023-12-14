"""Write a pseudocode algorithm which
●	inputs 100 barcodes, each input as six individual random digits
●	recalculates the check digit for each one and compares it with the one input
●	outputs the number of barcodes which were input correctly
"""
import random
from random import randint

barcodes = []

def generate_barcode(barcodes):
    temporary_list = []
    count = 0
    for count in range(0, 6):
        ran_digit = random.randint(1, 9)
        temporary_list.append(ran_digit)
        count += 1
    barcodes.append(temporary_list)

num = 0
while num != 100:
    generate_barcode(barcodes)
    num = num + 1

print(barcodes)

for list in barcodes:
    


