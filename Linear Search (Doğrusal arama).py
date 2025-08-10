def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Bulunan elemanın indeksi
    return -1  # Bulunamadı

# Örnek kullanım
liste = [5, 3, 8, 4, 2]
aranan = 4
sonuc = linear_search(liste, aranan)
print("Aranan bulundu! İndeks:", sonuc if sonuc != -1 else "Bulunamadı")
