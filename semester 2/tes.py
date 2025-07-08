pilihan = []
pilihan2 = []
pilihan3 = []
pilihan4 = []
print("masukan nama produk")

barang1 = input("Pilih produk belanjaan anda (kelompok 1): ")
pilihan.append(barang1)
barang2 = input("Pilih produk belanjaan anda (kelompok 2): ")
pilihan.append(barang2)
barang3 = input("Pilih produk belanjaan anda (kelompok 3): ")
pilihan.append(barang3)
barang4 = input("Pilih produk belanjaan anda (kelompok 4): ")
pilihan.append(barang4)

for i in pilihan:
    print(f"Kelompok 1: {i}")

for i in pilihan2:
    print(f'Kelompok 2: {i}')

for i in pilihan3:
    print(f'Kelompok 3: {i}')

for i in pilihan4:
    print(f"Kelompok 4: {i}")
