sınıf = [ ]
notlar = [ ]
yoklama = [ ]
  
for i in range(0, 5): 
    isimgiris = [item for item in input("Öğrencinin isim ve soyismini giriniz: ").split()] 
    vizegiris = [int(item) for item in input("Öğrencinin vize notunu giriniz: ").split()] 
    finalgiris = [int(item) for item in input("Öğrencinin final notunu giriniz: ").split()] 
    ödevgiris = [int(item) for item in input("Öğrencinin ödev notunu giriniz: ").split()] 
    notlar.append(vizegiris + finalgiris + ödevgiris) 
    sınıf.append(isimgiris) 
    #Dictionary'de itemlerin ilk elemanları birden fazla elemanlı bir list olarak tutulamadığı için burada list to string dönüşümü yapıldı.
    #(TypeError: unhashable type: 'list') 
    #['Ali', 'Veli']->['Ali Veli']
    donusturucu = " ".join(sınıf[i])
    yoklama.append(donusturucu)
      
print("Sınıf Listesi: ", sınıf) 
print("Not Listesi: ", notlar)

#iki list bir dictionary'de birleştirildi
info = dict(zip(yoklama, notlar))
print("Tüm Bilgilerin Toplandığı Dictionary: ", info)

#Dictionary'deki elemanlar kullanılarak ortalama hesaplandı
averages= {}
for yoklama,notlar in info.items():
    averages[yoklama] = sum(notlar)/ float(len(notlar))
print("Not Ortalamaları: ", averages)

#Sıralama
order = sorted(averages.items(), key=lambda x: x[1], reverse= True)    
print("Başarı Sıralması: ", order)

winner = next(iter(order)) 
   
print("Sınıfımızın birincisi " + str(winner[0]) + " oldu! Başarılarının devamını dileriz..." ) 