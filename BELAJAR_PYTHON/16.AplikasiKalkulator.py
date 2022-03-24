# variable untuk menyimpan + - * / exit
command = "" # string kosong

while command != "exit": # selama nilainya tidak sama dengan perintah exit
    command = input("Perintah : ")
    
    if command == "exit": # jika perintahnya sama dengan exit maka tidak dilanjutkan
        break # langsung berhenti

    if command != "+" and command != "-" and command != "*" and command != "/": # (!=) tidak sama dengan
        print("Perintah tidak dikenali")
        continue # dia akan memaksa jalannya while kembali keatas tidak lanjut kebawah
        
    a = int(input("Angka Pertama : "))
    b = int(input("Angka Kedua : "))
    
    if command == "+": # jika comand sama dengan + maka ..
        result = a + b
    elif command == "-":
        result = a - b
    elif command == "*":
        result = a * b
    elif command == "/":
        result = a / b
    
    print(f"Hasil : {result}") # (f) Formated String
    
print("Terima Kasih sudah menggunakan aplikasi kami") # jika exit