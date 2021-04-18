

def amountConverter(x):
    if x.isnumeric() and int(x) <= 35999: #untuk memfilter inputan user, jika condition True maka akan dilanjut perhitungan
        #menghitung inputan user ke RIM, KODI, dan LUSIN
        #1 rim = 500 buah
        #1 kodi = 20 buah
        #1 lusin = 12 buah
        RIM = (int(x) // 500)
        KODI = (int(x) % 500) // 20
        LUSIN = ((int(x) % 500) % 20) // 12
        print('{:02d}:{:02d}:{:02d}'.format(RIM,KODI,LUSIN)) #menampilkan hasil perhitungan dengan format 2 bilangan integer dengan urutan RIM, KODI, LUSIN
    else:
        print('Invalid') #bilan condition pertama False maka akan keluar Invalid di terminal
        return False

bilangan = input('Masukkan bilangan bulat: ') #mengambil hasil inputan user
amountConverter(bilangan)