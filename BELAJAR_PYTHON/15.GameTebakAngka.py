trying = 0 # Variable untuk mewakili user memulai mencoba menebak
secret_number = 7 # kunci jawabannya
limit = 3 # kesempatan user bermain untuk menebukan jawabannya

# Alur
while trying < limit:
    guess_number = input("Masukkan angka (1-9) = ") #angka yang dimasukan user
    guess_number = int(guess_number) # Ubah ke Tipe Integer
    
    # Melakukan pengecekan
    if guess_number == secret_number: # Sama dengan
        print("Selamat, Kamu Benar")
        break # untuk memaksa perulangan berhenti
    elif guess_number != secret_number:
        print("Angka Salah, coba lagi")
        
    trying += 1 # Agar user tidak bermain unlimit