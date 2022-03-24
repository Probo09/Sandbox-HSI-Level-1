# Sebuah struktur data yang bisa menyimpan data dalam bentuk key value pair
# diruby disebutnya  hash

# contoh
user = {
    "nama": "Probo Sutejo",
    "umur": 26,
    "is_admin": True 
} 

print(user) # cetak semua nilai

print("-" * 50)

nama = user["nama"]

print (nama) # mengambil satu nlai

print("-" * 50)

user["username"] = "Probo_Sutejo"
user["umur"] = 27

temp =  user["umur"] # nilainya dirubah
temp1 = user.get("username") # nilai nya ditambah
temp2 = user.get("alamat", "Jakarta") # jika nilainya ga ada maka parameter yang ke 2 digunakan
temp3 = user.get("alamat") # nilai nya tidak ada

print(temp)
print(temp1)
print(temp2)
print(temp3)
