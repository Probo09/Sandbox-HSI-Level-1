# unpack mencetak value dari index dan di masukkan ke dalam variable
angka = (4,5,6)

# cara manual
x = angka[0]
y = angka[1]
z = angka[2]
print(x , y , z)

# cara unpack
a,b,c = angka
print(c,b,a)

# jika hanya ingin mengambil index 1 saja (_) Variable yang tidak akan digunakan
a,_,_ = angka
print(a)

# tanda (*) membuat angka yang lain akan masuk ke variable k
j, *k = angka
print(j, k)