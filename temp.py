# -*- coding: utf-8 -*-
#try except
#LIST

#sadece bir type içerir
mylist= ["sddhkjfs","hejhf","njkdsf","ben","o","biz","siz"]
mylist2 = list()
print(mylist2)

for i in mylist:
    print(i)
if "sddhkjfs" in mylist:
    print("yes")
mylist.append("lemon")
mylist.insert(1,"benene")
mylist.pop() #son elemanı dçndürür
mylist.remove() #içine yazdığın elemaı kaldırır
mylist.clear() #hepsini siler
mylist.reverse() #elemanları ters çevirir
#sort elemanları küçükten byüğe sıralar
#eğer analisteyi bozmadan başka bi listede sıralanmasını istiyosan
new_list= sorted(mylist)
    
a= mylist[::3] #♥ 3,1,2,3,1,2,3 böyle sayar ve her 3 olanı yazdırır.
copy_list=mylist.copy() #listenin kopyasını oluşturmuş olur. bu methodu kllanmadan yazarwsak o zaman copy listte değişikliik yaptığımızda orijinal listede de değişiklik yapar.
b=[i*i for i in mylist] #listedeki her elemannı kendisi ile çarpar .
#product kartezyen çarpım yapar.

#TUPLE

#birrden fazla type içerir.
mytuple=("şeyma",23,"student",True)
mytuple=tuple(["şeyma",23,"student",True]) #diziyi tuplea dönüştürdük
#namedtuple elemanın 1 olarak gösterilen eleman x olarka getirilebilir.

#SET

#yinelenen elemanları yazmaz , sıralı değil

myset={1,2,1,1,2,3,3} #bunun tipi dictionary 
myset=set([]) #list dönüştürebilirsin
myset2= set("hello") #bunun tipi set
diff=myset.difference(myset2) #myset'te olup myset2 de olmayanlar
#update sıralı ve yinenelenenler olmadan iki seti birleştirir. uniondan farkı

#COLLECTİONS

from collections import Counter
#bir şeyin ne kadar tekrarlandığını sayar.
bak="aaajjjjjssss"
mycounter= Counter(a)
print(mycounter.item) #item,key,values,most_common olarak değiştirebiliriz veya bunları yazmadan da


print2d=[(1,2),(4,5),(4,9),(3,0)]
print(print2d[1])

#LAMBDA

#Anonim fonksiyon denilebilir.

#mesela bir şeyin karesini lambda ile i2 farklı şekilde alalım.

print((lambda x:x**2)(8))

#ya da bi fonksiyonmuş gibi
kare_al = lambda x: x ** 2
print(kare_al(8))

 #ya da bi fonskyionun returnünde bulunabilir
def rutbe(sayi):
    return lambda derece:derece**sayi
print(rutbe(3)(5))

#Filter() fonksiyonunda lambdaya 2 koşul ekleyebilirsin.
list_number = [2, 4, 6, 8, 9, 10, 12, 13]
print(list(filter(lambda x: (x > 7) and (x < 12), list_number))) #list diye filter objesini belirtmek zorundayız

#sorted ile bi diziyi y konumuna göre sıralayalım
print2d=[(1,2),(4,5),(4,9),(3,0)]
def sort_by_y(x):
    return x[1]
sırala=sorted(print2d, key=lambda x:x[1]) #ya da key=sortedby ile de yapabilirsin
print(sırala)

#NormalizasyonLambda ve Apply ile
import pandas as pd
import numpy as np
from datetime import datetime

df = pd.DataFrame({
    'name':['Weber', 'Durkheim', 'Comte'],
    'yearOfBirth':[1864, 1858, 1798],
    'countOfBook':[18, 10, 15]
})

#0-1 arasında normalizasyon için kulllanılacak değerler
minValue = df["countOfBook"].min()
minMaxDifferenceValue = df["countOfBook"].max() - df["countOfBook"].min()

#Apply methodu ile değişkenin değiştirebilmek ya da türetmek

df["countOfBook"]=df["countOfBook"].apply(lambda x: (x-minValue)/minMaxDifferenceValue)
print(df["countOfBook"])

#MAP

#map(fonksiyon,div veya list) fonksiyona listedeki her elemanı paremetre olarak atar. fonksiyon ile mthodu karıştırma. method=hazır. fonk=def
#burdaki fonksiyonu lambda ile de kurabiliriz.
listem=["a","b","c","d","e"]
listem2=[1,2,3,4,5]
def ilkuc(x):
    return x.swapcase()
#print(list(map(ilkuc,listem)))
print(list(map(lambda x,y: (x + str(y)),listem,listem2)))

#RANDOM

import random
import numpy as np

a=random.uniform(1, 10) #randint dersek int değer alır. choice veya sample dersek seçim yapar. shuffle random sıralar.

sayilar=[1,2,3,4,5]
print(*sayilar) #dzeden .ıkartarak yazdırır.

matrix= np.random.rand(3,4)
print(matrix)
matrix2=np.random.randint(1,10,(3,4))
print(matrix2)

#DEKARATOR

# @ ile gösterilir
#Dekoratörler parametre olarak fonksiyon alan, geriye fonksiyon döndüren fonksiyonlardır.
#Temelde alınan parametreyi iç fonskiyona(wrapper) gönderir. Ve wrapperı return eder.

"""-Birinci Sınıf Nesne : Dinamik olarak oluşturulabilen, yok edilebilen,
bir fonksiyona parametre olarak verilebilen ya da bir fonksiyondan sonuç değeri olarak döndürülebilen,
değişkenlerle aynı haklara sakip varlıklardır.
 -Dinamik nesneler, derleme zamanında değil, çalışma zamanında"""
 
""" -Parametre: fonsiyona girdi olarak kullanılan değişkene yani formal parameter.
     -Argüman: fonksiyon çağrılırken gönderilen değişken yani actual argument."""

#(*args) sözdizimi, bir fonksiyona değişken sayıda argüman iletmek için kullanılır.



def add(x, y):
    return x + y

print('add: {}'.format(add))
print('add.__name__: {}'.format(add.__name__))
print('add(2, 3): {}'.format(add(2, 3)))
print('type(add): {}'.format(type(add)))

def call_function(func, *args):
    return func(*args)

print('call_function(add, 2, 3): {}'.format(
    call_function(add, 2, 3)
))
del add

#başka bir örnek

def factorial(n: int):

    def fact(n):
        if n == 1:
            return 1
        return n * fact(n - 1)

    return fact(n)
 
while (True):
   print("Lütden Pozitif Tam Sayı Girin:")
   deger= input()
   sayi= int(deger)
   if type(sayi) == int and sayi >0:
       print(factorial(sayi))
       break
   
#try exceptli hali
def factorial(n: int):
    
    def fact(n):
        if n <= 1:
            return 1
        return n * fact(n - 1)

    return fact(n)

while (True):
    
    print("Lütden Pozitif Tam Sayı Girin:")
    deger= input()
    sayi= int(deger)
    try:
        if type(sayi) == int and sayi >0:
            print(factorial(sayi))
            break
    except:
        continue
        
#GENARATORS

#Genaratörler
#fonksiyonu generatör yapan şey yield ifadesidir.
#-SELF, Sınıfın nesnesinin özelliğini argümanlarla bağlar.
#- __init__ , Sınıf içinde nesne  kurucu fonksiyondur.
#
#Örn:
class Person:
	
	# init method or constructor
	def __init__(self, name):
		self.name = name
	
	# Sample Method
	def say_hi(self):
		print('Hello, my name is', self.name)
	
p = Person('Nikhil')
p.say_hi()

#Örn:
class A(object):
	def __init__(self, something):
		print("A init called")
		self.something = something
		print(self.something)

class B(A):
	def __init__(self, something):
		# Calling init of parent class
		A.__init__(self, something)
		print("B init called")
		self.something = something
obj = B("Something")


#generatör birde fazla değer döndürebilir. Bunlar için next kullanmalıyız ya da iteratör yardımı ile.
def ilkgenerator(num):
    print("Starting")
    yield 1
    yield 2
#print(ilkgenerator(4))
a=ilkgenerator()
print(next(a))
print(next(a))


def secgenerator():
    print("hdjh")
    yield 1
    yield 2

for i in secgenerator():
    print(i)
#örnek


def rev_str(my_str):
    'Döngülü yield'
    length = len(my_str)
    for i in range(length - 1,-1,-1):
        yield my_str[i] #yield yerine return yazsaydık bir tane değer döndürürdü
 
for char in rev_str("merhaba"):
     print(char)
#generatör idafesi lambda gibi kullanılabilir.
#Bir liste döndürmek için normal bir fonksiyon, sonucu döndürmeden önce belleğe tüm diziyi oluşturur. Eğer liste çok büyükse bu diziyi tamamen belleğe yüklemek belleği aşırı şekilde kullanılmasına neden olabilir. Generator ise bellek dostu olup bir seferde sadece bir öğe ürettiği için tercih edilir.
#örnek
my_list = [1, 3, 6, 10]

print([x**2 for x in my_list])#lambda örneği

a= (x**2 for x in my_list)#genaratör örneğinde sadece bunu değişkene atayarak next ifadesi kullanmalıyız.

print(next(a))
print(next(a))
print(next(a))
print(next(a))


print(sum(x**2 for x in my_list)) #lambda gibi fonksiyonların içinde de kullanılabiilri.


# THREADİNG VE MULTİPROCESSİNGLER
"""
"""
#daha az yer kaplaması için process bir işlemdir , processin içinde başka açılan işlemciklere threading denir.
#threading bellekte daha az yer kullanmak için.


# *args,*kwargs, **kwargs

"""python *args'tan sonra **kwargs koymamıza izin verir. **kwargs default value alabilir. *args'a value vermeliyiz"""

#ÖRNEK for *args, *kwargs

def addition(a, b, *args, option=True):
   result = 0
   if option:
      for i in args:
          result += i
      return a + b + result
   else:
      return result
  
print(addition(1,4,5,6,7))
#output:23
print(addition(1, 4, 5,6, option=False))
#output:0

#ÖRNEK hepsi için

def arg_printer(a, b, *args, option=True, **kwargs):
   print(a, b)
   print(args)
   print(option)
   print(kwargs)
arg_printer(1, 4, 6, 5, param1=5, param2=6)
"""output 
1 4
(6, 5)
True
{'param1': 5, 'param2': 6}"""

#*args'a liste atarsak tek elemeanlı bir tuple olarak saklar. bunu *kwargs il eyapmak istediğimizde dictionary atayabiliriz zaten kwargsların çıktısı da ona benzer.


# * nerelerde kullanılır
#formal parametreyi sadece liste vs olarak girmek istiyosak "*" yardım eder. [],() ise "*" dict ise{} "**" 
def foo(a,b,c):
    print(a,b,c)
    
my_dict={"a":1,"b":2,"c":3}
print(foo(**my_dict))


#ÖRNEK
numbers=[1,2,3,4,5,6]

*beggining,last=numbers
print(beggining)
#output 1,2,3,4,5
print(last)
#output: 6

#tuple ve listi birleştirebiliriz. #aynı şekilde ** kullnarak dict leri de birleştirebilirz.
my_tuple=(9,a,7,8)
my_list=[1,2,3,4]

newlist=[*my_tuple,*my_list]

#Shallow ve Deep

"""bir nesneyi kopyalamak istediğimizde "=" operatörü kullanırız. fakat a=b de a yı değiştirdiğiimzde
b de değişir çünkü aynı bellek adresini gösterirler. Orjinal değerleri kaybetmeden değiişkenimizin kopya-
sına ihiyaç duyduğumuzda bu yöntem kullanılır.

Shallow kopyalamada örneğin bir listenin değerlerini referans bazlı taşır fakat listenin
kendisi farklı bi adreste kopyalar. listeye ekleme yaptığımızda orjinallik bozulmaz ama [0][0]. elemanında
değişiklik yaptığımızda orjinallik bozulur. çünkü elemanları referans tiplidir.

Deep tarzı kopyalamada hem değişken hem de değişken üyeleri farklı bir adrese kopyalanır. *****"""

import copy
 
eski_list = [[10, 20.2, 30], [-40, 50, 60], [70, 80, 'Test']]
yeni_list = copy.deepcopy(eski_list) #shallowda copy.copy
 
print('Eski Liste:', eski_list)
print('Eski liste ID si:', id(eski_list))
print('Eski liste 1. eleman ID si', id(eski_list[0]))
 
print('Yeni Liste:', yeni_list)
print('Yeni Liste ID si:', id(yeni_list)) #orjinalden farklıdır.
print('Yeni liste 1. eleman ID si', id(yeni_list[0])) #orjinalden farklıdır.

#Context Manager

"""bir dosya yüklediğimizde kullandığımız kaynak sınırsız olmadığı için onu kapamamız ve iade etmeliyiz.
cont.mng ve with bu ile yarar.

Context manager oluşturmanın 2 yolu var.
-Class Kullanmak
-Contexmanager decorator kullanmak"""

#Örnek With olmadan, try except te finally eklediğmizde her türlü dosyayı kapatabiliriz.

with open("dosyaismi.txt", "w") as fw:
    fw.write("with deyimi kullanimi...")

#---------------------------------------------

try:
    # Dosya ac
    file = open('kerem.txt', 'w')
    # Islem yap
    file.write("Lisp dili candır... o_O")
except IOError:
    # Exception IO HATA MESAJI
finally:
    # Dosya kapa
    file.close()


#Örnek __exit__ işlevine with işleminden sonra giriyor.

class File(object):

    # Constructor metodumuzu yazalim
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        # Islemleri yapildigi metod
        self.f_obj = open(self.file_name, self.mode)
        return self.f_obj

    def __exit__(self, exc_type, exc_val, traceback):
        # Dosya kapama islemi
        #if self.f_obj:
        self.f_obj.close()


with File('kerem.txt', 'w') as f_write:
    f_write.write('Test...')
    print(f"Dosya Kapatildi mi?[With Body] -> {f_write.closed}") #exc_type , exc_value

print(f"Dosya Kapatildi mi?[With blogu disi] -> {f_write.closed}")

#ÖRNEK dekaratör olarak

from contextlib import contextmanager

@contextmanager
def dosyaisleme(dosya_adi, mod):
    dosya = open(dosya_adi, mod)  # __init__ islemi
    yield dosya                   # __enter__ islemi
    dosya.close()                 # __exit__ islemi
