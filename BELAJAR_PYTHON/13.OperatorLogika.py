# Operator logika digabungkan dengan IF

name = "Probo Sutejo"
by_pass_validation = False # Variable By Pass

# Cek Panjang dari variable nama lebih dari 3
if len(name) > 3 or by_pass_validation:
    print("Welcome " + name)
else:
    print("Nama Terlalu Pendek")

# (||) atau or
# False or True = True
# True or False = True
# False and True = False
# True and False = False
# True and True = True