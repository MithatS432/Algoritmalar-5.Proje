def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Örnek kullanım
liste = [2, 3, 4, 5, 8]
aranan = 4
sonuc = binary_search(liste, aranan)
print("Aranan bulundu! İndeks:", sonuc if sonuc != -1 else "Bulunamadı")
