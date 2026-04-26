def find_highest_gwa(filename):
    best_name = ""
    best_gwa = float('inf')

    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            name = parts[0]
            gwa = float(parts[1])

            if gwa < best_gwa:
                best_gwa = gwa
                best_name = name

    return best_name, best_gwa


file_path = r"C:\Users\admin\Downloads\2nd_activity_file\students.txt"

name, gwa = find_highest_gwa(file_path)

print("Student with highest GWA:")
print(name, "-", gwa)