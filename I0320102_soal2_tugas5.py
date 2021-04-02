#Titus Kurniawan Sandy Purwanto
#I0320102
#Kelas C
#Soal 2

print('------Program Konversi Nilai------')
nama = str(input('Silahkan Masukkan nama anda : '))
nilai = float(input('Silahkan masukkan nilai anda : '))
if nilai <= 100 :
    print('Halo,', nama, '! Nilai anda setelah dikonversi adalah A')
elif nilai <= 84 :
    print('Halo,', nama, '! Nilai anda setelah dikonversi adalah A-')
elif nilai <= 79 :
    print('Halo,', nama, '! Nilai anda setelah dikonversi adalah B+')
elif nilai <= 74 :
    print('Halo,', nama, '! Nilai anda setelah dikonversi adalah B')
elif nilai <= 69 :
    print('Halo,', nama, '! Nilai anda setelah dikonversi adalah C+')
elif nilai <= 64 :
    print('Halo,', nama, '! Nilai anda setelah dikonversi adalah C')
elif nilai <60 :
    print('Halo,', nama, '! Nilai anda setelah dikonversi adalah E')
else :
    print('Maaf,', nama, 'nilai anda tidak valid')