#Titus Kurniawan Sandy Purwanto
#I0320102
#Kelas C
#Soal 1

print('-----Virtual Front Desk Reception-----')
nama = str(input('Silahkan masukkan nama anda : '))
jenis_kelamin = str(input('Silahkan masukkan jenis kelamin anda (L/P) : '))
if jenis_kelamin == 'L' or jenis_kelamin == 'l' :
    print('Selamat datang, Bapak', nama, '!')
elif jenis_kelamin == 'P' or jenis_kelamin == 'p' :
    print('Selamat datang, Ibu', nama, '!')
else :
    print('Mohon masukkan nama dan jenis kelamin anda dengan benar')