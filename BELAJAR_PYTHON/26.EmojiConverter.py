kalimat = input(" >>> ") # Variable untuk menangkap inputan

emoji_mapping = {
    ":)": "🙂",
    ":D": "😀",
    ":|": "😐"
}

words = kalimat.split(" ") # pecah masing-masing kata menggunakan split

print(kalimat)
print(words)

output = ""
for w in words:
    output = output + emoji_mapping.get(w, w) + " "
    
print(output)