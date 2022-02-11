# -*- coding: utf-8 -*-


import numpy as np 
import math


error = " "
lmbda_linearNormalization = lambda bst, wrst, cll : (bst-cll)/(bst-wrst)#linear normazlization formulünün lambdası
lmbda_multipliedByWeight = lambda w, cell : w * cell#ağırlık çarpımı için kullanılabilecek lambda
lmbda_Qi_values = lambda q, si, sStar, sEksi, ri, rStar, rEksi: q * (si-sStar)/(sEksi-sStar)+(1-q)*(ri-rStar)/(rEksi-rStar)
#qi değeri hesaplamak için formulünün lambda olarak hazırlanmış hali
lmbda_aras_normalization = lambda value, sum_v : value/sum_v#aras normalize edilmesi için olan formülğün lambdası
lmbda_topsis = lambda value : math.sqrt(value**2)
#topsiste kullanılabilecek formulün lambdası

def is_number(value):#gönderilen değerin float dönüşümü yapılabiliyor mu diye kontrolü yapılıyor
    try:
        float(value)
        return True#değer dönüştülebiliyorsa true değer döndürür
    except ValueError:
        return False
    

def convert_to_numerical(self,array, cCount, rCount):
    #gönderilen matrisin aslında diky ve yatay başlıklar bulunuyor o yüzden satır sütun sayısı parametre olarak alınıyor
    err = "NONE"
    for row in range(rCount):#satır sayısı
        for column in range(cCount):#sütun sayısı
            
            if(is_number(array[row,column])==True):#belirtilen indexteki değer sayı olup olmadığı kontrol ediliyor
                array[row,column]=abs ( float(array[row,column] ) )#değer float a dönüştürülüyor
            
            else:
                err="{} Sayısal Veri Değildir, Düzeltiniz".format(array[row,column])
                break
                
    return array, err #geriye dönüşümü yapılan array ve error metni döndürülür      
    

#******************************************** VIKOR ************************************************



def VIKOR (self, array, empty_array, hHeader, vHeader):
    hHeader[0]= " "#horizontal header ın olduğu dizinin 0. indexinde değer olmasına karşın boş str ile değiştiriyoruz.
    
    best_result, worst_result = min_max_choice(self, array, array.shape[1], "VIKOR", hHeader[1:])#en iyi ve en kötü değer seçimi için fonksiyon çağrılır.
    
    array = np.vstack([array, best_result[1:],worst_result[1:]])#np.vstack ile best ve worst değerlerinin olduğu diziler arraye eklenir
   
    empty_array_linear = linearNormalization(self,  array[0:-3,:], best_result[1:] , worst_result[1:])
    #linear normalize yöntemi ile normalize matris oluşturmak için fonksiyon çağrılır
  
    empty_array_weight = multipliedByWeight(self, array[-3,:], empty_array_linear, "VIKOR")
    #ağırlıklandırılmış matris oluşturmak için normalize matris 
    #ağırlıklandırma için kullanılan fonksiyona ağırlık değerlerinin olduğu dizi ve yöntem adı ile birlikte fonksiyona gönderilir


    result_si = empty_array_weight.sum(axis = 1)# Si sonuçları # array in satır toplamları alınır
    result_si = np.array(result_si, dtype=object)#dizi array e dönüştürülür

    result_ri = empty_array_weight.max(axis = 1)# Ri sonuçları satırdaki en yüksek değeri döndürür dizi şeklinde

    
    result_max_min_si = [result_si.max(axis = 0), result_si.min(axis = 0)]#Si sonuçları 
    #si değerlerinin tutulduğu arrayden max ve min değerleri döndürülür sütun bazında
    #************************* max sonuçları si/riEksi --- min olanlar si/riStar*****************************
    result_max_min_ri = [result_ri.max(axis=0), result_ri.min(axis = 0)]#Ri sonuçları
    #ri değerlerinin tutulduğu arrayden max ve min değerleri döndürülür sütun bazında
    
    qi_outcome = Qi_result(self, result_si, result_ri, result_max_min_si, result_max_min_ri)
    #qi değerlerini bulmak için, işlem yapmak için olan fonksiyona değerler gönderilir ve sonuç satır bazında döner
    qi_outcome_sort = np.copy(qi_outcome).T
    #dönen arrayin transpozu alnır ve copyası yeni bir arraye atanır

    j, k = 1, 1
    #j sayacı koşul sonuçlarının ve sıralanmış qi sonuçlarının birlikte tutulduğu arraye değer atamak için kullanılan sütun indextir
    #k sayacı koşul 
    conditions_1 = ["--", " ", "--", " ", "--", " ", "--", " ", "--", " ",]  #koşul 1 in değerlerinin tutulacağı dizi oluşturulur
    conditions_2 = ["--", " ", "--", " ", "--", " ", "--", " ", "--", " ",]  #koşul 2 nin değerlerinin tutulacağı dizi oluşturulur
    #rank değerlerinin olduğu sütuna denk gelecek şekilde sonuçları diilere ekleme yapıldı
    for i in range(5):#5 adet qi değer arrayleri olduğu için döngü 5 e ayarlandı
        sorted_arr, condition = array_sort(self, qi_outcome[i], "VIKOR", result_si, result_ri)
        #rank sıralama fonksiyonunun içinde vikor yöntemi için ayrı bir fonksiyon daha bulunmaktadır
        #bu fonksiyon koşul sağlanmış mı diye kontrol eder qi değerleri ve si ve ri değerleri ile 
        
        qi_outcome_sort = np.insert(qi_outcome_sort, k, sorted_arr[:,1], axis = 1)    
        
        # j+=2
        if(condition[0]==True):
            conditions_1[k] = "Sağlandı"
        else:
            conditions_1[k] = "Sağlanmadı"
            
        if(condition[1]==True):
            conditions_2[k] = "Sağlandı"
        else:
            conditions_2[k] = "Sağlanmadı"
        k+=2
        
    array = np.insert(array, 0, np.atleast_2d(np.concatenate((vHeader, ["En İyi", "En Kötü"]), axis=None)), axis=1)  
    #array e vertical header eklenir öncesinde 2 boyutlu birleştirilmiş header oluşturulur sonrasında insert ile sütun olarak eklenir
    
    array = np.insert(array, 0, hHeader, axis=0)
    #insert ile horizontal header eklenir satır olarak 0. indexe 
    vHead_SR = np.concatenate((vHeader[0:-1], ["Maksimum", "Minimum"]), axis = None)        
    #si ve ri değerlerinin min ve max değerlerinin vertical header ı olması için 
    #ağırlık başlığının tutulduğu son index dışında vHead ile si ri başlıkları, satır bazında birleştirilir
    conditions_1 = np.array(conditions_1, object)
    conditions_2 = np.array(conditions_2, object)
    #koşulların tutulduğu diziler array e dönüştürülür
    qi_outcome_sort = np.array(qi_outcome_sort, dtype=object)
    #qi_outcome_sort arraye dönüştürülür
    header = ["Qi=0", "Rank", "Qi=0.25", "Rank", "Qi=0.50", "Rank", "Qi=0.75", "Rank", "Qi=1", "Rank"]
    #qi_outcome_sort için horizontal header hazırlanır satır olarak daha sonra eklenecektir.
    qi_outcome_sort = np.insert(qi_outcome_sort, 0, header, axis = 0)
    #qi_outcome_sort arrayine header başlığı eklenir
    qi_outcome_sort = np.insert(qi_outcome_sort, 0, conditions_2, axis = 0)
    #koşul 2 nin sonuçlarının tutulduğu array başlık satırının üstüne eklenir
    qi_outcome_sort = np.insert(qi_outcome_sort, 0, conditions_1, axis = 0)
    #koşul 1 in sonuçlarının tutulduğu array koşul 2 satırının üstüne eklenir 
    vHeader = np.array(vHeader, object)
    
    qi_outcome_sort = np.insert(qi_outcome_sort, 0, np.concatenate((["KOŞUL 1","KOŞUL 2","Qi DEĞERLERİ VE RANK"], vHeader[0:-1]), axis = None), axis = 1)
    #qi_outcome_sort array inde vertical header bulunmamaktadır. 
    #bu yüzden en son eklenen satırlarla birlikte header birleştirilir ve arraye inser ile 0. sütuna eklenir
    SiRi_arr = []#si ve ri değerlerinin birlikte tutulacağıbir array oluşturmak için bir dizi tanımı yapıyoruz
    SiRi_arr= np.c_[result_si, result_ri ]#kolon şeklinde si ve ri değerlerinin tutulduğu arrayler 
    
    SiRi_arr = np.r_[SiRi_arr, np.atleast_2d(np.concatenate((result_max_min_si[0], result_max_min_ri[0] ), axis=None))]
    #max ve min değerleri olan dizilerin 0.ve 1. indexindeki veriler satır bazında birleştirilir ve satır olarak siri_arr ye eklenir
    SiRi_arr = np.r_[SiRi_arr, np.atleast_2d(np.concatenate((result_max_min_si[1], result_max_min_ri[1] ), axis=None))]
    
    SiRi_arr = np.c_[vHead_SR.T, SiRi_arr]
    #sirarr için oluşturulan vertical header satır bazında hazırlanmıştı onun transpozu header olrak sütun bazında eklenir
    SiRi_arr = np.r_[ np.atleast_2d([" ", "Si Değerleri", "Ri Değerleri"]), SiRi_arr]
    #siri_arr arrayine bir horizontal header eklenir
    SiRi_arr = np.array( SiRi_arr, object)
    #son olarak geri döndürülecek bir çıktı olacağı için array dönüşümü yapılır.
    
    # print(SiRi_arr)    
    return array, empty_array_linear, empty_array_weight, SiRi_arr, qi_outcome_sort


def min_max_choice(self, array, cCount, way, hHeader):#kriterlerin min/max beklentilerine("+", "-") göre değer araması yapar
    best, worst = ["BEST"], ["WORST"]#en iyi en kötü değer aramalarının sonuçlarının ekleneceği
    #0. indexinde başlık olarak kullanılacak değerler ile liste tanımlaması yapılmıştır
    for column in range(cCount):#cCount kolon sayısıdır ve belirtilen sayıdaki sütunlarda arama yapılacaktır

        value = hHeader[column]#hHeader horizantal header dır kriterlerin yazılı olduğu array/list tir
        #belirtilen kolon indexindeki değer value değişkenine atanır

        if (value.rfind("+")!=-1):#kriterin yazılı olduğu metnin sonunda + değeri var mı diye kontrol edilir
        #-1 bulunamadığında döndürdüğü değerdir rfind string metodunun 
        #rfind aranan değerin son indexini döndürür. ben + ve - değerlerini sonda istediğim için son indexini döndürmesini istedim
        #başka bir kontrol daha ekleme ihtimaline karşı rfind kullanılmıştır
            best.append(best_worst_value(self, array, "+", column))#min/max değerlerinin aramasının yapıldığı best_worst_value fonksiyonu çağrılır
            
            if (way == "VIKOR" or way == "TOPSIS"):#eğer uygulanan yöntem vikor ya da topsis ise en kötü değer araması da yapılmalıdır
                worst.append( best_worst_value(self, array, "-", column))#en kötü değer için aranan en iyi değerin tam tersinin araması yapılır.
        elif (value.rfind("-")!=-1):
            if(way=="ARAS"):
                #eğer yöntem aras ise min değer beklentisi olan sütun değerleri 1/değer olarak işleme tabi tutulur 
                best.append(1/best_worst_value(self, array, "-", column))
                #işleme tabi tutulmadan önce min değer bulunur ve -1 üssü alınır o şekilde listeye eklemesi yapılır
                array[0:-1,column:column+1] = minValues_Convert(self, array[0:-1,column:column+1])#minValues_Convert fonksiyonu değerlerin -1 üssünü alır
                
            elif (way == "VIKOR" or way == "TOPSIS"):#eğer yöntem aras değilse en iyi ve en kötü değer aramaları yapılır ve listeye eklenir
                worst.append(best_worst_value(self, array, "+", column))
                best.append(best_worst_value(self, array, "-", column))    
        else:
            error = "{} SÜTUNU İÇİN MIN MAX SEÇİMİ BELİRTİLMEMİŞTİR. EKLEYİNİZ".format(value)
            return error
       
    best = np.array(best, dtype=object)
    worst = np.array(worst, dtype=object)
    array = np.array(array, dtype=object)
    if (way=="ARAS"):#yöntem aras ise best ve gönderilen matrisin kendisi(-1 üssü alımı yapıldı) geri döndürülür
        return best, array
    else:#yöntem aras değilse en iyi ve en kötü değerler geri döndürülür
        return best, worst
    
       


def best_worst_value(self, array, choice, column):#for ARAS, this func gives optimum(best) value
      if(choice=="+"):#min/max değerlerinin belirlenmesi için + ve - işaretleri kullanılmıştır
      #min ve max değerlerinin geri döndürülmesi için choice parametresine gönderilen değere göre işlem yaptırılıyor
      #choice + ise max değilse min değeri geri döndürülür
          
          return max(array[0:-1,column])#-1. satırın işleme tabi tutulmamasının sebebi en son satırda ağırlık/W değerleri bulunuyor o yüzden
          #parametre olarak array/matris almaktadır bu yüzden de column parametresi ile belirlenen sütunun indexinde arama yapılır.
          
      else:

          return min(array[0:-1,column])



   
def linearNormalization(self, array, best, worst ):#uses linear normalization for max min choice
    #vikor linear normalization kullanıyor. bunun içinde en iyi en kötü ve matrisin kendisine ihtiyaç vardır.
    #bu değerleri parametre olarak istiyoruz.
    #normalleştirme işlemi sonucunun tutulacağı matrisi verilen matris ile aynı boyutta array olarak oluşturuyoruz
    r_array = np.empty((array.shape[0], array.shape[1]), object)
    for j in range (array.shape[1]):#sütun sayısı
        for i in range(array.shape[0] ):#satır sayısı
            outcome = abs (lmbda_linearNormalization(best[j], worst[j], array[i,j]))
            #en iyi ve en kötü değerler sütun bazında bulunuyor o yüzden best ve worst arrayinin indexi aynı zamanda array in de sütun indexidir
            #her aynı indexteki best ve worst değerini aynı sütun indexinde bulunun her satır elemanı ile işleme alıyoruz
            #lamda ile işlem yaptırılmıştır
            r_array[i,j] = outcome#işleme alınan matristeki değerin indexi geri döndürülecek arraye işlem sonucunun atamasında da kullanılıyor.
    return r_array#sonuçların eklendiği array geri döndürülür


def multipliedByWeight(self, weight, array, way):
    return_array =[]#sonuçların ekleneceği boş liste tanımlanır.
    #ağırlık değerleri ile çarpım kolon olarak yapılır
    return_array_1 = np.empty((array.shape[0], array.shape[1]), object)
    #matris olarak array alınır bu fonksiyonda o yüzden sonuçların matris olarak tutulacağı bir boş matris tanımlanır
    for i in range(array.shape[1]):#sütun sayısı
        for j in range(array.shape[0]):#satır sayısı
            outcome = weight[i]*array[j,i] #gönderilen ağırlık değerlerinin her bir indexi arraydeki sütun indexi ile aynıdır.
            #i indexindeki ağırlık ve sütundaki satır satır her eleman birbiri le çarpılır sonuç listeye eklenir
            return_array.append(outcome)
            
        return_array = np.array(return_array, dtype=object).T#liste arraya dönüştürülür transpozu alınır kolon haline getirilir
        
        return_array_1 = np.insert(return_array_1, i, return_array, axis = 1)#array ile aynı boyutta tanımlanan boş matrise insert metodu ile i. indexe eklenir
        #insert ile ekleme yapıldığında belirtilen indexteki satırı yada sütunu bir yüksek değerdeki indexe kaydırır bu yüzden sondan sütun siliyoruz
        return_array_1 = np.delete(return_array_1, -1, axis = 1)#son sütun silme
        return_array = []#append yöntemi ile eklemeyi seçtiğim için array e dönüşen listeyi tekrar boş liste yapıyoruz
     
    return return_array_1#verilerin işlem sonuclarının tutulduğu array geri döndürülür

def Qi_result(self, si_array, ri_array, s_maxMin, r_maxMin):
    qi_zero, qi_two, qi_five, qi_seven, qi_full = [], [], [], [], []
    #qi değeri 0-1 arası 5 farklı değer olarak alınır ve hesaplanır.
    #sonuçlar alınan qi değerine göre farklı listelere eklenir
    #bu işlem daha kısa yapılabilir ancak 3 yöntem içinde kullanılan başka fonksiyonun verimini düşürüyor o yüzden burada uzun yazılmıştır.
    
    for sayac in range (5):# 5 farklı qi değeri ile işlem yapılacağından değerin sırasını belirlemek açısından döngü uygulanmıştır
    
        if (sayac== 0):
            for i in range(si_array.shape[0]):
                Qi_sonuc=round( lmbda_Qi_values(0, si_array[i], s_maxMin[1], s_maxMin[0], ri_array[i], r_maxMin[1], r_maxMin[0]), 3)
                #yöntemin kısa yazılacağı düşünülerek bir lamda foksiyonu tanımlanmıştı, o yüzden uzun tutulsada işlemin açıklığı için kullanılmıştır.
                qi_zero.append(Qi_sonuc)#sonuç listeye ekleniyor. sonrasında döngü bitince array e dönüştürme yapılmıştır.
            qi_zero = np.array(qi_zero, dtype=object).T #sonuçların sütun şeklinde tutulması istendiği için transpoz yöntemi uygulanmıştır.
            
            
        elif(sayac==1):

            for i in range(si_array.shape[0]):
                Qi_sonuc=round( lmbda_Qi_values(0.25, si_array[i], s_maxMin[1], s_maxMin[0], ri_array[i], r_maxMin[1], r_maxMin[0]), 3)
                qi_two.append(Qi_sonuc)
            qi_two = np.array(qi_two, dtype=object).T  
            
        elif(sayac==2):

            for i in range(si_array.shape[0]):
                Qi_sonuc=round( lmbda_Qi_values(0.50, si_array[i], s_maxMin[1], s_maxMin[0], ri_array[i], r_maxMin[1], r_maxMin[0]), 3)
                qi_five.append(Qi_sonuc)
            qi_five = np.array(qi_five, dtype=object).T 
            
        elif(sayac==3):

            for i in range(si_array.shape[0]):
                Qi_sonuc=round( lmbda_Qi_values(0.75, si_array[i], s_maxMin[1], s_maxMin[0], ri_array[i], r_maxMin[1], r_maxMin[0]), 3)
                qi_seven.append(Qi_sonuc)
            qi_seven = np.array(qi_seven, dtype=object).T  
            
        else:

            for i in range(si_array.shape[0]):
                Qi_sonuc=round( lmbda_Qi_values(1, si_array[i], s_maxMin[1], s_maxMin[0], ri_array[i], r_maxMin[1], r_maxMin[0]), 3)
                qi_full.append(Qi_sonuc)
            qi_full = np.array(qi_full, dtype=object).T    
    # print("ZERO", qi_zero,"\n TWO", qi_two, "\n FIVE",qi_five,"\n SEVEN", qi_seven, "\n FULL ",qi_full)
    return qi_zero, qi_two, qi_five, qi_seven, qi_full #bütün hesaplanmış qi değerlerinin arrayleri geri döndürülür (sıralanmak üzere)

def array_sort (self, arr, way, rsult_si = " ", rsult_ri = " "):
    #bu fonksiyonda vikor yöntemi için koşul kontrolü olduğu için önden değeri atanmış parametreler eklenir. 
    arr = np.array(arr, dtype=object)#gelen array parametresi array a dönüştürülüyor, sıralama işlemi yapabilmek için
   
    index_sort = np.sort(arr)#küçükten büyüğe sıralanmış arrayi yeni bir arraya atıyoruz
    counter = 0#bu sayacı aynı değerden veriler varsa sıra numarasında atlama olmaması için ekliyoruz
    for i, j in list(enumerate(np.sort(arr))):#sıralanmış array i indexleriyle tutup list türüne döüştürüyoruz
    # i değerleri index değerleri j değerleri ise indexteki veridir
        indices = np.where(arr==j)#where ile j deki verinin sıralanmamış arraydeki indexini indices değişkenine aktarıyoruz.
        #aynı değerden birden fazla olma ihtimaline karşılık indices içinde bir for döngüsü ekliyoruz.
        for k in indices:#k değerleri array de aranan verinin index değeridir.
            index_sort[k] = i+1#verileri 1 den başlayarak sıralamak istediğimiz için i+1 ile sıralama yapıyoruz. 
            counter= counter+k.shape[0]#sayaç değişkenine döngüden beklenen yineleme sayısı ile ekleyerek değer atıyoruz.
            #for döngüsü her zaman 1 kere dönüp bir üstteki for döngüsüne geçiyor o yüzden k nın shape metodu değeri ile ekleme yapılıyor.
        if (counter==index_sort.shape[0]):#sayaç değeri toplam array in boyutuna ulaştığında döngüyü sonlanırıyoruz
            break
        
    arr = np.c_[arr, index_sort]#rank değerlerini "array" array ine sütun olarak ekliyoruz.
    
    if (way == "VIKOR"):#vikor yönteminde sonuç için sıralanmış bu değerler ile 2 adet koşul kontrolü yapılmalı
    #hesaplaması yapılan yöntem vikor ise koşul kontrolü için tasarlanmış fonksiyon çağrılıyor.
        boolean = condition_true(self, np.sort(arr[:,0]) , arr[:,0], rsult_si, rsult_ri)#bu fonksiyon boolean değer döndürür
        #koşul sağlandıysa true değilse false döner 
        return arr, boolean #koşul köntrolünün sonuçları ve rank değerleri belirtilmiş array geri döndürülür
    else:
        return arr#yöntem vikor değilse sadece sıra değeri atanmış array geri döner
    
def condition_true(self, index_sort, array, si, ri):
    boolean = []#sonuç değerlerini liste biçiminde tutmak için boş liste tanımlaması yapılıyor.
    result_zero = np.where(array==index_sort[0])#en küçük değer indexi alınır array deki
    result_one = np.where(array==index_sort[1])#en küçük 2. değer indexi alınır arrayden
    condition = array[result_one[0]] - array[result_zero[0]]#koşul 1 için önce en küçük 2 değerin uzaklığı hesaplanır
    
    #--------------------------------------CONDITION 1 -------------------------
    
    if (np.any(condition >= 1/(array.shape[0]-1))): #burada any kullanmak durumunda kalındı çünkü mantık hatası verdi
        #koşul 1 en küçük 2 değerin uzaklığının toplam alternatif sayısının 1 eksiğinin 1 e bölümünden fazla veya eşit olmasıdır.
        boolean.append(True) 
    else:
        boolean.append(False)
        
     #--------------------------------------CONDITION 2 -------------------------
     
      #qi değeri hesaplanmış arraydeki en küçük değere sahip alternatif indexi alınır 
      #alternatiflerin si ve ri değerlerinin en küçükleri ile o indexteki alternatifin si ve ri değerleri karşılaştırılır
      #eşit ise si ya ri deki karşılaştırmalar Koşul 2 sağlanmış olur
      
    if(min(si)==si[result_zero[0]] or min(ri)==ri[result_zero[0]] ):
       
        boolean.append(True) 
    else:
        boolean.append(False)
    boolean = np.array(boolean, dtype=object).T

    return boolean#sonuc list olarak geri döndürülür
    
    
#********************************************** ARAS *************************************************

def ARAS(self, array, empty_array, hHeader, vHeader):
    vHead = np.copy(vHeader)
    hHeader[0] = " " #horizantal header içinde 0. indexte yazı varsa boş str ile değiştiriyoruz. 
    
    optimum, array = min_max_choice(self, array, array.shape[1], "ARAS", hHeader[1:])
    #max-min yada kar-maliyet  durumlarına göre sütunlardaki en iyi değerleri seçtiriyoruz
    optimum[0] = "Optimum"#0. indexte Best yazısını optimum olarak değiştirdik

    # empty_array = np.empty((array.shape[0]-1, array.shape[1]), object)#matematiksel işlemler yapacağımız yeni boş bir array tanımlıyoruz
    # bu boş array optimum satırı dahil boyutta ancak ağırlık satırı dahil değil boyutta olacak ve başlık satır ve sütunu dahil olmayacak

    
    array = np.insert(array, -1, optimum[1:], axis = 0)#son satır index ine optimum list ini ekliyoruz
    
    empty_array = np.insert(empty_array, -1, optimum[1:], axis = 0)#-2. index e optimum değerler eklendi boş array e-- boş arrayin boyutunu gereken miktara yükselttik
    
    result_column_sum = np.sum(array[0:-1,:], axis = 0)#sütun toplamı optimum dahil--array in son satırı W değerleridir
    
    array = np.insert(array, -1, result_column_sum, axis = 0)# ağırlık değerlerinin bir üst index ine sütun toplamı sonuç satırı ekleniyor
    
    result_column_sum = np.insert(result_column_sum, 0, "Sütun Toplamı")# sütun toplamının 0. indexine isim atıyoruz
    
    empty_array = aras_normalization(self, array[0:-2,:], array[-2:-1,:], empty_array)#optimum değerler ile verileri normalizasyon işlemine gönderiliyor
    
    weighted_array = multipliedByWeight(self, array[-1,:], empty_array, "ARAS")#array in son indexinde W değerleri vardır
    
    result_row_sum = np.sum(weighted_array, axis = 1)#ağırlık değerleri ile çarpılmış array in satır toplamlarını alıyoruz
    

    result_ki =[]
    for i in range(result_row_sum.shape[0]):
        result_ki.append(result_row_sum[i]/ result_row_sum[-1])
        #satır toplamının son indexinde optimum değerlerin toplamı bulunmaktadır. o yüzden sıralamaya onu eklemiyoruz. sonuç 1 çıkıyor çünkü
    ranked_array = array_sort(self, result_ki[0:-1], "ARAS") #büyük olan en iyi seçim 
    


#*****************************return için array düzenleme********************************************************************
    
    array = np.c_[np.concatenate((vHead[0:-1], optimum[0], result_column_sum[0], vHead[-1]), axis = None), array]
    #concatenate ile array e eklenecek Vertical Header için verilen değerlerin yatay şekilde birleştirilmesi yapılıyor
    #sonrasın birleşimin sonucu Vertical Header olarak array e ekleniyor
    
    array = np.insert(array, 0, hHeader, axis = 0)#array e Horizontal Header ekleniyor
    
    empty_array= np.c_[np.concatenate((vHead[0:-1], optimum[0]), axis = None), empty_array]#empty_array e Vertical Header ekleniyor
   
    empty_array = np.insert(empty_array, 0, hHeader, axis=0)#np.insert ile empty_array e Horizontal Header ekleniyor
    
    weighted_array = np.c_[np.concatenate((vHead[0:-1], optimum[0]), axis = None), weighted_array]#weighted_array e Vertical Header ekleniyor
    
    weighted_array = np.insert(weighted_array, 0, hHeader, axis=0)#weighted_array e Horizontal Header ekleniyor
    
    result_row_sum = np.insert(result_row_sum, 0, "Satır Toplamı")# satır toplamının 0. indexine isim atıyoruz
   
    weighted_array = np.c_[weighted_array, result_row_sum]#satır toplamları değerlerini son sütun olarak ağırlıklandırılmış array e ekliyoruz.
    
    ranked_array = np.insert(ranked_array, 0, vHeader[0:-1], axis = 1)#ranked_array e Vertical Header ekleniyor
    
    ranked_array = np.insert(ranked_array, 0 , [" ", "SONUÇ", "RANK"], axis = 0)#ranked_array e Horizontal Header ekleniyor
    
    return ranked_array, array, empty_array, weighted_array 
    
    
##################################################################################################################################    
def round_values(self, array, Count, decimal):#yuvarla yapılmak için eklenmiş bir fonksiyondur
    for i in range(Count):#count arrayin yuvarlaması yapılacak boyutudur
        array[i]= round(array[i], decimal)#decimal parametresi virgülden sonra eklenebilecek değer sayısıdır
    # print(array)    
    return array #yuvarlaması yapılmış array geri döndürülür

def minValues_Convert(self, array):#the minValue is divided by 1.
   #aras yönteminde minimum/maliyet beklentisi olan kolon/kriter değerleri 1 e bölünüp matrise eklenir
   #bu işlem için eklenmiş bir fonsiyondur. bu fonksiyon min/max değer seçimlerinin yapıldığı fonksiyonda çağrılır
    for i in range(array.shape[0]):
        array[i]=1/array[i]

    return array # 1 e bölünmüş yeni değer sonuçları geri döndürülür.


def aras_normalization(self, array_value, array_sum, empty_array):

    result = []
    for i in range(array_sum.shape[1]):#sütun sayısı
    
        for j in range(array_value.shape[0]):#satır sayısı
            result.append(array_value[j,i]/array_sum[0,i])
            
        result = np.array(result, object)
        empty_array = np.insert(empty_array, i, result.T, axis = 1) 
        empty_array = np.delete(empty_array, -1, axis=1)
        result = []
        #sütunlar üzerinde işlem yapıldığı ve empty_array boyutu belli olduğundan insert ile veri ekleniyor

    return empty_array

#********************************************** TOPSIS *************************************************

def TOPSIS(self, array, empty_array, hHeader, vHeader):
    vHeader = np.array(vHeader, object)
    hHeader[0] = " " #horizantal header içinde 0. indexte yazı varsa boş str ile değiştiriyoruz. 
    result = np.sum(np.power(array[0:-1,:], 2), axis=0)#sütunların kareleri toplamı
    

    for j in range(empty_array.shape[1]):
        for i in range ( empty_array.shape[0]):
            empty_array[i,j] = array[i,j]/math.sqrt(result[j])
          
    norm_array = np.copy(empty_array)# elimizde bir adet normalize edilmiş matris tutmak için normalleştirilmiş matrisi np.copy ile koyasını oluşturuyoruz
    
    empty_array = multipliedByWeight(self, array[-1,:], empty_array, "TOPSIS")#normalize edilmiş matrisi ağırlıklandırılmış matris olarak dönüştürüyoruz.
    #multipliedbyweight fonksiyonu ağırlık çarpımı için kullanılan bir fonksiyondur

    array[0:-1,:] = empty_array[:,:]#best ve worst seçimini ağırlık değerleri bulunan arrayler üzerinde arama yapılır
    #bu yüzden ağırlıklandırılmış değerler ağırlık değerlerinin olacağı array formatına dönüştürülüyor.
    
  
    # empty_array =  np.insert(empty_array, 0, array[0,1:], axis = 0)
    best, worst = min_max_choice(self, array, empty_array.shape[1], "TOPSIS", hHeader[1:] )
    #best worst seçimleri için min_max_choice fonksiyonuna array in kendisi sütun sayısı yöntem adı 
    #ve seçim şekillerinin olduğu horizontal header parametreleri gönderilir.
    
    siPlus_value, siMinus_value, sSkor = [], [], []#siplus siminus ve si değerlerinin gerekli işlem sonucunun tutulacağı diziler oluşturulur
    result_best, result_worst = 0, 0#işlem sonuçlarının atanacağı değişkenler tanımlanır

    for i in range(empty_array.shape[0]):#satır sayısı
        for j in range (empty_array.shape[1]):#sütun sayısı
            result_best += (array[i,j]-best[j+1])**2 #sütun bazında cell leri tek tek best değerleri ile işleme koyulur 
            result_worst += (array[i,j]-worst[j+1])**2#sütun bazında cell leri tek tek worst değerleri ile işleme koyulur 
        siPlus_value.append(result_best**0.5)#karekökü alınmış değerlerin sonuçları diziye eklenir
        siMinus_value.append(math.sqrt(result_worst))#sonuçların karekökü diziye eklenir
        sSkor.append(siMinus_value[i]/(siMinus_value[i]+siPlus_value[i]))
        #si değerlerinin skorları için işlem uygulanır ve gerekli diziye eklenir
        
    
    sSkor = round_values(self, sSkor, len(sSkor), 5)#sonuçları 5 decimal değerinde yuvarlaması yapılır round_values fonksiyonu ile

    result_RankArray = array_sort(self, sSkor, "TOPSIS") 
    # skorların küçükten büyüğe sıralanmış olduğu durumdaki rank değerlerinin bulunmuş eklenmiş hali için fonksiyona gönderilir.
    
    
#*************************************************return arrayleri düzenleme*******************************************
    norm_array = np.c_[vHeader[0:-1], norm_array]#normalize edilmiş matrise vertical header eklendi
    norm_array = np.insert(norm_array, 0, hHeader, axis=0)#norm_array e horizontal header eklendi
    
    empty_array = np.r_[empty_array, np.atleast_2d(best[1:])]#empty array e en iyi değerlerin olduğu dizi eklendi. 
    #best dizisinin tek boyutlu olması sorun oluşturduğu için boyutunu (numpy.atleast_2d ile ) 2 boyutluya dönüştürüldü
    empty_array = np.r_[empty_array, np.atleast_2d(worst[1:])]#worst dizisini best dizisinin altına satır olarak empty_array e ekliyoruz
    empty_array = np.r_[empty_array, np.atleast_2d(array[-1,:])]
    #array in son satırında ağırlık değerleri bulunmaktadır o değerleri empty_array e ekliyoruz
    empty_array = np.c_[np.concatenate((vHeader[0:-1], best[0], worst[0], vHeader[-1]), axis = None), empty_array]
    #numpy.concatenate ile vertical header oluşturup onu sütun ekleme ile empty_array e ekliyoruz.
    #best worst dizilerinin ilk indexinde başlıkları bulunmaktadır. ayrıca vHeader dışarıdan alınan bir parametredir ve işleme konulan matrisin vertical header ıdır
    empty_array = np.insert(empty_array, 0, hHeader, axis=0)#insert metodu ile horizontal header ekleniyor. 
    #bu header da bir parametredir ve işleme alınan matrisin header ıdır
    
    
    siPlus_value = np.array(siPlus_value, object)
    siMinus_value = np.array(siMinus_value, object)
    #siPlus ve siMinus dizileri array e dönüştürüldü. object dtype ı şeklinde bu yolla içine ne eklenirse onun veri türünü kabul edecektir
    
    siPlus_value = np.c_[vHeader[0:-1], siPlus_value]#vHeader ı vertical header olarak siPlus a ekliyoruz. vHeader da alternatifler ve ağırlık başlıkları bulunur
    
    siMinus_value = np.c_[vHeader[0:-1], siMinus_value]#vHeader ı vertical header olarak siMinus a ekliyoruz
    
    result_RankArray = np.c_[vHeader[0:-1], result_RankArray]#rank değerleri atanmış array e alternatifleri verical header olarak ekliyoruz
    
    print("\n", result_RankArray)#büyük olan en iyi seçim
    return result_RankArray, norm_array, empty_array, siPlus_value, siMinus_value



#********************************************** AĞIRLIK HESABI *************************************************


def weight_Calculate(self, arr, criterias):
    criteriaCount_Ri = [0, 0, 0.58, 0.90, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49, 1.51, 1.48, 1.56, 1.57, 1.58]
    #15 adet kriter sınırı bulunmaktadır.
    empty_arr = np.empty((arr.shape[0], arr.shape[1]), object)
    
    column_sum = np.sum(arr, axis = 0)#sütun toplamı alınır
    
    for j in range(arr.shape[1]):
        for i in range (arr.shape[0]):
            empty_arr[i,j] = arr[i,j]/column_sum[j]
            
    row_sum_W = np.sum(empty_arr, axis = 1)#weights
    for i in range(row_sum_W.shape[0]):
        row_sum_W[i] = row_sum_W[i]/row_sum_W.shape[0]
    
    for j in range (arr.shape[1]):#sütun
        for i in range (arr.shape[0]):#satır
            empty_arr[i,j] = arr[i,j]*row_sum_W[j]
            
    row_sum = np.sum(empty_arr, axis = 1)
    
    max_lambda = 0
    for i in range(row_sum.shape[0]):
        max_lambda +=  (row_sum[i]/row_sum_W[i])/row_sum_W.shape[0]
    
    max_lamda_result = (max_lambda - row_sum_W.shape[0])/(row_sum_W.shape[0]-1)
    
    condition_value = max_lamda_result / (criteriaCount_Ri[row_sum_W.shape[0]-1])
    if  condition_value < 0.10:
        error = "NONE"
        row_sum_W = np.c_[criterias, row_sum_W]
        return row_sum_W, condition_value, error
    else:
        error = "Belirtilen matrisin değerleri ağırlıklandırma koşulunu sağlayamadı "
        return row_sum_W, condition_value, error















