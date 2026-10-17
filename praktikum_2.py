harga = 12500
jumlah = 4

total_harga = harga * jumlah
sisa_pembagian = total_harga % 2000
total_diskon = total_harga - 5000

print(f"Harga per buku       : Rp{harga}")
print(f"Jumlah beli          : {jumlah}")
print(f"Total harga          : Rp{total_harga}")
print(f"Sisa pembagian % 2000: {sisa_pembagian}")
print(f"Total setelah diskon : Rp{total_diskon}")