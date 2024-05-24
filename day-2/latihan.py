# Latihan

# nilai = input("Masukan Nilai Anda :")
# if int (nilai) >= 80 and int (nilai) <= 100 :
#     print("A")

# elif int (nilai) >= 70 and int (nilai) <= 80 :
#     print("B")

# elif int (nilai) >= 60 and int (nilai) <= 70 :
#     print("C")

# elif int (nilai) >= 50 and int (nilai) <= 60 :
#     print("D")

# elif int (nilai) > 100 or int (nilai) < 0 :
#     print("Tidak Valid")

# else :
#     print("E")

nilai = int(input("Masukan Nilai Anda : "))

#Konversi Nilai

if nilai > 100 or nilai < 0 :
    
    print("Nilai Tidak Valid")
    
elif nilai >= 80 :
    
    print("Nilai Anda adalah " + str(nilai) + " Predikat nilai anda : A") 

elif nilai >= 70 and nilai < 80 :
    
    print("Nilai Anda adalah " + str(nilai) + " Predikat nilai anda : B")
    
elif nilai >= 60 and nilai < 70 :
    
    print("Nilai Anda adalah " + str(nilai) + " Predikat nilai anda : C")
    
elif nilai >= 50 and nilai < 60 :
    
    print("Nilai Anda adalah " + str(nilai) + " Predikat nilai anda : D") 
    
else :
    
    print("Nilai Anda adalah " + str(nilai) + " Predikat nilai anda : E") 


