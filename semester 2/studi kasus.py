# input belanja array


pilihan = []

pilihan2 = []

pilihan3 = []

pilihan4 = []

print("Pilih belanjaan anda")

barang1 = input("Pilih produk belanjaan anda (kelompok 1): ")
pilihan.append(barang1)

barang2 = input("Pilih produk belanjaan anda (kelompok 2): ")
pilihan2.append(barang2)

barang3 = input("Pilih produk belanjaan anda (kelompok 3): ")
pilihan3.append(barang3)

barang4 = input("Pilih produk belanjaan anda (kelompok 4): ")
pilihan4.append(barang4)
for i in pilihan:
    print(f"Kelompok 1: {i}")

for i in pilihan2:
    print(f"Kelompok 2: {i}")

for i in pilihan3:
    print(f"Kelompok 3: {i}")

for i in pilihan4:
    print(f"Kelompok 4: {i}")


