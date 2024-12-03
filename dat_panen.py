data_panen = {
    "lokasi1": {
        "nama_lokasi": "Kebun A",
        "hasil_panen": {"padi": 1200, "jagung": 800, "kedelai": 500},
    },
    "lokasi2": {
        "nama_lokasi": "Kebun B",
        "hasil_panen": {"padi": 1500, "jagung": 900, "kedelai": 450},
    },
    "lokasi3": {
        "nama_lokasi": "Kebun C",
        "hasil_panen": {"padi": 1100, "jagung": 750, "kedelai": 600},
    },
    "lokasi4": {
        "nama_lokasi": "Kebun D",
        "hasil_panen": {"padi": 1300, "jagung": 850, "kedelai": 550},
    },
    "lokasi5": {
        "nama_lokasi": "Kebun E",
        "hasil_panen": {"padi": 1400, "jagung": 950, "kedelai": 480},
    },
}

# Menampilkan seluruh data
print("Seluruh Data Panen:")
for lokasi, info in data_panen.items():
    print(f"{lokasi.capitalize()}:")
    print(f"  Nama Lokasi: {info['nama_lokasi']}")
    print("  Hasil Panen:")
    for komoditas, jumlah in info["hasil_panen"].items():
        print(f"    - {komoditas.capitalize()}: {jumlah}")
print()

# Menampilkan jumlah hasil panen jagung dari lokasi2
hasil_jagung_lokasi2 = data_panen["lokasi2"]["hasil_panen"]["jagung"]
print(f"Jumlah hasil panen jagung dari Lokasi 2 (Kebun B): {hasil_jagung_lokasi2}")
print()

# Menampilkan nama lokasi dari lokasi3
print(f"Nama Lokasi dari Lokasi 3: {data_panen['lokasi3']['nama_lokasi']}")
print()

# Menyimpan jumlah hasil panen padi dan kedelai ke dalam variabel terpisah dan menentukan status lokasi
for lokasi, info in data_panen.items():
    padi = info["hasil_panen"]["padi"]
    kedelai = info["hasil_panen"]["kedelai"]
    
    # Percabangan untuk menentukan status lokasi
    if padi > 1300 or info["hasil_panen"]["jagung"] > 800:
        kondisi = "memerlukan perhatian khusus"
    else:
        kondisi = "dalam kondisi baik"
    
    # Menampilkan hasil panen dan status lokasi
    print(f"Nama Lokasi: {info['nama_lokasi']}")
    print(f"  Hasil Panen Padi: {padi}")
    print(f"  Hasil Panen Kedelai: {kedelai}")
    print(f"  Status Lokasi: {kondisi}")
    print()
    print('hallo')