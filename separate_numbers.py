with open("numbers.txt", "r") as infile:
    numbers = infile.readlines()

even_numbers = []
odd_numbers = []

for num in numbers:
    num = int(num.strip())
    
    if num % 2 == 0:
        even_numbers.append(str(num))
    else:
        odd_numbers.append(str(num))

with open("even.txt", "w") as even_file:
    even_file.write("\n".join(even_numbers))

with open("odd.txt", "w") as odd_file:
    odd_file.write("\n".join(odd_numbers))

print("Done! Check even.txt and odd.txt.")