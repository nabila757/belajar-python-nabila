# looping
# contoh kasus
# menampilkan bilang 1-10

#menampilkan bilangan 1-10

for i in range(1,11) :
    print(i)

print("\n")
# Menampilkan Data Array

list_siswa = ["irfan", "yoga", "lengga", "ely", "nabila"]

for siswa in list_siswa :
    print(siswa)

print("\n")
# Menampilkan Kalimat Seacara Berulang Dengan Range

kalimat = "Saya Berjanji Tidak Mengulang Lagi"

for i in range (1,2) :
    print(kalimat)

print("\n")
#Menampilkan Bilangan Ganjil

for i in range(1, 30, 2) :
    print((i), end=" ")
    
print("\n")
    
# Menampilkan Bilangan Genap
for i in range(1, 30, 2) :
    print((i)+1, end=" ")
