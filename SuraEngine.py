import numpy as np
import sys
import math
import os
import socket
from _thread import *
import cython
import webbrowser as wb
import jupyter
import datetime
import time
import scipy
import random
ver_a = ''
ver_c = ''
def ify(degisken,operator,deger):
    dogru_mu = 0
    if degisken == 'a':
        if operator == '=':
            if ver_a == deger:
                dogru_mu = 1
        if operator == '!=':
            if ver_a != deger:
                dogru_mu = 1
        if operator == '<':
            if ver_a < deger:
                dogru_mu = 1
        if operator == '>':
            if ver_a > deger:
                dogru_mu = 1
    if degisken == 'b':
        if operator == '=':
            if ver_b == deger:
                dogru_mu = 1
        if operator == '!=':
            if ver_b != deger:
                dogru_mu = 1
        if operator == '<':
            if ver_b < deger:
                dogru_mu = 1
        if operator == '>':
            if ver_b > deger:
                dogru_mu = 1
    if degisken == 'c':
        if operator == '=':
            if ver_c == deger:
                dogru_mu = 1
        if operator == '!=':
            if ver_c != deger:
                dogru_mu = 1
        if operator == '<':
            if ver_c < deger:
                dogru_mu = 1
        if operator == '>':
            if ver_c > deger:
                dogru_mu = 1
    return dogru_mu
    #HOŞ GELDİNİZ 
    #ε=ε=┌( >_<)┘
print("© Bütün hakların Sahibi Sura Tech 2023") 
print("{☆}")
print('ঔৣ☬ 🆂🆄🆁🅰 🅴🅽🅶🅸🅽🅴ঔৣ☬')
print("2.3 Release sürümündeki yenilikler kayıt olma sistemindeki hata düzeltildi, görsel iyileştirmeler yapıldı , network sistemi biraz düzenledi ve Bilgilendirmeler eklendi ~ Sura Tech")
print("Sürüm No. 2.3")
print("Merhaba Sura Engine Hoşgeldiniz")
print("Güvenlik Denetliniyor Lütfen Bekliyiniz")
print("Güvenlik denetlendi :)")
Adınız = "ab2018"
şifreniz = "12345"
#Video çekerken şifrenizi saklayın kimseye göstermeyiniz 
#Your username you want to login to Sura Engine

while True:
    kullanici = input("Kullanıcı adınızı giriniz: ")
    parola = input("Şifrenizi giriniz: ")
    # ikisi de doğru
    if kullanici == user and parola == password:
        print("Hoşgeldiniz")
        break
    # kullanıcı adı doğru şifre yanlış
    elif kullanici == user and parola != password:
        print("Şifreniz yanlış\n")
    # şifre doğru kullacı adı yanlış
    elif kullanici != user and parola == password:
        print("Kullanıcı adınız yanlış \n")
    # ikisi de yanlış
    else:
        print("Kullanıcı adı ve şifre hatalı\n")
    DLC = input('Sura Script Flow-based görsel programlama diline geç')
cevap = input('DLC yüklemek için sura gamesin resmi web sayfasına gidin ')
bad_files = "virus.exe", "exploit.application", "internet_explorer.exe" 
def siteye_yonlendir():

    website = "https://suragames.tr.gg/"

    wb.open(website)

siteye_yonlendir()
#Ek paketi yüklemek için ek paketi satın almanız gerekiyor ek paketler 10,50 TL yada 20,00 TL olucaktır 3 Ek paket yayınlanacaktır hepsini almak için tek seferde Sura Engine Deluxe Edition ve ayrıca yeni özelleştirmeler mevcut olucaktır
 
def view_update(self, context, depsgraph):
    region = context.region
    view3d = context.space_data
    scene = depsgraph.scene
    dimensions = region.width , region.height
class Network:

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "localhost" # For this to work on your machine this must be equal to the ipv4 address of the machine running the server
                                    # You can find this address by typing ipconfig in CMD and copying the ipv4 address. Again this must be the servers
                                    # ipv4 address. This feild will be the same for all your clients.
        self.port = 5555
        self.add = (self.host, self.port)
        self.id = self.connect()

    def connect(self):
        self.client.connect(self.addr)
        return self.client.recv(2048).decode()

    def send(self, data):
        """
        :param data: str
        :return: str
        """
        try:
            self.client.send(str.encode(data))
            reply = self.client.recv(2048).decode()
            return reply
        except socket.error as e:
            return str(e)

isim = input("isminizi giriniz:")
def fonksiyonum(ad, soyad):
  print("Adınız: " + ad + ", Soyadınız: " + soyad)
fonksiyonum("Free License", "i")
def fonksiyonum(): print("Bir fonksiyondan merhaba!") 
fonksiyonum()
string = "yemreak"
tek_metin = "yemre"
metinler = ['emre', 'ak']
x = np.array([1, 2, 3])
print(x)
#array([1, 2, 3])
y = np.arange(10)
print(y)
#array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
a = 200
b = 33
if b > a:
  print("b büyüktür.")
elif a == b:
  print("a ve b eşittir")
else:
  print("a büyüktür.")
  def pyhsics():
      pyhsics.cube.powered.suraengine
işlem = input('Proje Oluştur - 1, Proje Optimize Et -2   :')
if işlem == '1':
    ad = input('Proje Adı:')
    şifre = input('Proje Şifresi:')
    with open(ad + '.ss','a') as dosya:
        dosya.write('passcode = ' + şifre + "\n\n.")
if işlem == '2':
    ad = input('Proje Adı:')
    with open(ad + '.ss') as dosya:
        print('Optimize Ediliyor........\n---------------------------------------------------')
        code = dosya.codelines()
        i = 1
        while True:
            try:
                run[i] = run[i].replace('\n','')
                run[i + 1] = run[i + 1].replace('\n','')
                rood = run[i]
                if 'sys.output = ' in rood:
                    rood = rood.replace('sys.output = ','')
                    rood = rood.replace('\n','')
                    print(rood)
                if 'str; = ' in rood:
                    rood = rood.replace('str; = ','')
                    if 'a' in rood:
                        ver_a = run[i + 1]
                    if 'b' in rood:
                        ver_b = run[i + 1]
                    if 'c' in rood:
                        ver_c = run[i + 1]
                if 'int; = ' in rood:
                    rood = rood.replace('int; = ','')
                    if 'a' in rood:
                        ver_a = int(run[i + 1])
                    if 'b' in rood:
                        ver_b = int(run[i + 1])
                    if 'c' in rood:
                        ver_c = int(run[i + 1])
                if 'sys.output with ver = ' in rood:
                    run[i + 1] = run[i + 1].replace('\n','')
                    rood = rood.replace('sys.output with ver = ','')
                    rood = rood.replace('\n','')
                    if 'a' in run[i + 1]:
                        rood = rood.replace('&',ver_a)
                    if 'b' in run[i + 1]:
                        rood = rood.replace('&',ver_b)
                    if 'c' in run[i + 1]:
                        rood = rood.replace('&',ver_c)
                    print(rood)
                if 'sys.input = ' in rood:
                    rood = rood.replace('sys.input = ','')
                    rood = rood.replace('\n','')
                    if 'a' in run[i + 1]:
                        ver_a = input(rood)
                    if 'b' in run[i + 1]:
                        ver_b = input(rood)
                    if 'c' in run[i + 1]:
                        ver_c = input(rood)
                if 'sys.output if = ' in rood:
                    rood2 = run[i + 1]
                    rood2 = rood2.split()
                    if ify(rood2[0],rood2[1],rood2[2]) == 1:
                        rood = rood.replace('sys.output if = ','')
                        rood = rood.replace('\n','')
                        print(rood)
                if 'sys.input if = ' in rood:
                    rood2 = run[i + 2]
                    rood2 = rood2.split()
                    if ify(rood2[0],rood2[1],rood2[2]) == 1:
                        rood = rood.replace('sys.input if = ','')
                        rood = rood.replace('\n','')
                        if 'a' in run[i + 1]:
                            ver_a = input(rood)
                        if 'b' in run[i + 1]:
                            ver_b = input(rood)
                        if 'c' in run[i + 1]:
                            ver_c = input(rood)
                i += 1
            except:
                break
print("sura programlama dilini kullandığınz için teşekkürler")
input()