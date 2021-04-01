#Titus Kurniawan Sandy Purwanto
#I0320102
#Kelas C
#Exercise 5.3

#penggunaan if untuk tiga kasus atau lebih
#input bilangan
print('Masukkan koordinat')
x = int(input('Masukkan nilai x : '))
y = int(input('Masukkan nilai y : '))
info = 'Koordinat (' + str(x) + ',' + str(y) + ') berada pada kuadran '
#memeriksa nilai x dan y
if x>0 and y>0 :
    print(info + 'I')
elif x<0 and y>0 :
    print(info + 'II')
elif x<0 and y<0 :
    print(info + 'III')
elif x>0 and y<0 :
    print(info + 'IV')
else :
    pass
print()