import random
kazanma=0
kaybetme=0
i=0
print("Alperen ALPAYDIN","\n")
print("Tarafindan Yapilmistir","\n")

print("Bu program monty hall problemini denemek icin yapilmistir. 3 adet kapi seceneğiniz ve bir kapinin arkasinda araba,","\n","Dger kapinin arkasinda keci vardır")
print("Oncelikle bir kapi secersiniz. Sectikten sonra kalan iki tanesinden arkasında keci bulunan herhangi biri elenir")
print("Ve tekrardan secim yapmak isteyip istemediginizi secersiniz.","\n")
while(1):
    print("Kazanma Sayisi = ",kazanma)
    print("Kaybetme Sayisi = ",kaybetme)
    if(kazanma!=0 or kaybetme!=0):
        ortalama=kazanma/(kazanma+kaybetme)*100
        print("Kazanma Oranınız Yüzde ",ortalama,"\n")
    while(1):
        i=i+1
        tercih=input("birinci kapi icin 1, ikinci kapi icin 2, ucuncu kapi icin 3'ü tuslayin = ")
        if(tercih=='1' or tercih=='2' or tercih=='3'):
            a=0
            
            random.seed(i)
            kutu=random.randint(1,3)
            random.seed(i*9005)
            if(kutu==1 and tercih=='1'):
                a=random.randint(2,3)
            elif(kutu==1 and tercih=='2'):
                a=3
            elif(kutu==1 and tercih=='3'):
                a=2
            elif(kutu==2 and tercih =='1'):
                a=3
            elif(kutu==2 and tercih=='2'):
                liste=[1,3]
                a=random.choice(liste)
            elif(kutu==2 and tercih =='3'):
                a=1
            elif(kutu==3 and tercih=='1'):
                a=2
            elif(kutu==3 and tercih=='2'):
                a=3
            elif(kutu==3 and tercih=='3'):
                a=random.randint(1,2)
               
            if(a==1):
                
                print("1 numaralı kapi elendi")
                if(a==int(tercih)):
                    print("Elendiniz!!!","\n")
                    kaybetme=kaybetme+1
                    break
                else:
                    tercih2=input("Tercihinizi degistirmek icin 1 kalması icin 0 = ")
                    if(tercih2=='1'):
                        if(tercih=='2'):
                            tercih='3'
                        elif(tercih=='3'):
                            tercih='2'
                        print("Tercihiniz degistirildi")
                    if(int(tercih)==kutu):
                        print("Arabaaaa Kazandiniz","\n")
                        kazanma=kazanma+1
                    else:
                        print("Keciiiii Kaybettiniz","\n")
                        kaybetme=kaybetme+1
                    break
            if(a==2):
                 
                print("2 numaralı kapi elendi")
                if(a==int(tercih)):
                    print("Elendiniz!!!","\n")
                    kaybetme=kaybetme+1
                    break
                else:
                    tercih2=input("Tercihinizi degistirmek icin 1 kalması icin 0 = ")
                    if(tercih2=='1'):
                        if(tercih=='1'):
                            tercih='3'
                        elif(tercih=='3'):
                            tercih='1'
                        print("Tercihiniz degistirildi")
                    if(int(tercih)==kutu):
                        print("Arabaaaa Kazandiniz","\n")
                        kazanma=kazanma+1
                    else:
                        print("Keciiiii Kaybettiniz","\n")
                        kaybetme=kaybetme+1
                    break
            if(a==3):
                 
                print("3 numaralı kapi elendi")
                if(a==int(tercih)):
                    print("Elendiniz!!!","\n")
                    kaybetme=kaybetme+1
                    break
                else:
                    tercih2=input("Tercihinizi degistirmek icin 1 kalması icin 0 = ")
                    if(tercih2=='1'):
                        if(tercih=='1'):
                            tercih='2'
                        elif(tercih=='2'):
                            tercih='1'
                        print("Tercihiniz degistirildi")
                    if(int(tercih)==kutu):
                        print("Arabaaaa Kazandiniz","\n")
                        kazanma=kazanma+1
                    else:
                        print("Keciiiii Kaybettiniz","\n")
                        kaybetme=kaybetme+1
                    break
        else:
            print("Gecerli deger giriniz","\n")
            break

                        
                            
