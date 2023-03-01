def cari_kata_terpanjang(kalimat):
    kata_list = kalimat.split()
    kata_terpanjang = kata_list[0]
    for kata in kata_list:
        if len(kata) > len(kata_terpanjang):
            kata_terpanjang = kata
            return kata_terpanjang
kalimat = input("Masukkan sebuah kalimat: ")
print("Kata terpanjang dalam kalimat adalah:", cari_kata_terpanjang(kalimat))