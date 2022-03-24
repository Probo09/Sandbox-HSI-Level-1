# List / Array bisa menampung lebih dari 1 tipe data pada umumnya sama tipe data

names = ["Probo", 77, False, 99]

print(names)  # mengambil semua listnya
print(names[0])
print(names[0:3])
print(f"range = {names[2:4]}")
print(f"range = {names[-1]}")
print(90 * "-")

# Menggunakan FOR
for name in names:
    print(f"Item : {type(name)} {name}")
