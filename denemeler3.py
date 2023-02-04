import tkinter as tk
import time
root = tk.Tk()
root.title("FAİZ HESAPLAMA")
root.geometry('400x400')
frame1 = tk.Frame(root)
anapara_girisi = tk.Entry(frame1)
faiz_orani_girisi = tk.Entry(frame1)
vade_türü_girisi = tk.Entry(frame1)
vade_süresi_girisi =tk.Entry(frame1)
anaparavar = tk.Variable()
faizoranivar = tk.Variable()
vadetürüvar = tk.Variable()
vadesüresivar = tk.Variable()
anapara = anapara_girisi.get()
faiz = faiz_orani_girisi.get()
vadetürü = vade_süresi_girisi.get()
vadesüresi = vade_süresi_girisi.get()
vade_turu_menu = tk.OptionMenu(frame1, vadetürüvar, "Yıl","Ay","Gün")
anapara_etiket = tk.Label(frame1, text="Anapara:")
faiz_orani_etiket = tk.Label(frame1, text="Faiz Oranı %:")
vade_türü_etiket = tk.Label(frame1, text="Vade Türü:")
vade_süresi_etiket = tk.Label(frame1, text="Vade Süresi:")
anapara_etiket.grid(row=0,column=0)
anapara_girisi.grid(row=0, column=1)
faiz_orani_etiket.grid(row=1, column=0)
faiz_orani_girisi.grid(row=1,column=1)
vade_türü_etiket.grid(row=2, column=0)
vade_turu_menu.grid(row=2,column=1)
vade_süresi_etiket.grid(row=3,column=0)
vade_süresi_girisi.grid(row=3, column=1)
#varsayılan olarak yılı hesaplar
def hesaplama(payda=100): 
    if vade_türü_girisi == "Yıl":
        getiri = round(((anapara * faiz * 100) / payda),2)
        sonuc= round((anapara + getiri),2)
        result.configure(
        text=f"Anapara: {anapara:.2f} kWh\n"
        f"Faiz Oranı: {faiz:.2f} %\n"
        f"Vade Türü: {vadetürü:.2f} Yıl\n"
        f"Vade Süresi:{vadesüresi:.2f} Yıl\n"
        f"Kazanç: {sonuc:.2f} Türk Lirası\n" bg='lightgreen', font=('Helvatical bold',16))
    
    elif vade_türü_girisi == "Ay":
        getiri = round(((anapara * faiz * 1200) / payda),2)
        sonuc= round((anapara + getiri),2)
        
    
    else:
        getiri = round(((anapara * faiz * 36500) / payda),2)
        sonuc= round((anapara + getiri),2)
hesapla_butonu = tk.Button(frame1, text="Hesapla", command=hesaplama)
hesapla_butonu.grid(row=4,column=0)


#     sonuc= round((anaPara + getiri),2)

#     anaPara = int(anapara_girisi.get())
#     faizOrani = int(entry2.get())
#     tarihSayisi = int(entry3.get().format(tarih))

#     getiri = round(((anaPara * faizOrani * tarihSayisi) / payda),2)
#     sonuc= round((anaPara + getiri),2)

#     print("{} TL, %{} faizle {} {} sonunda \n{} TL faiz getirirken toplamda {} TL paran olur.".format(anaPara, faizOrani, tarihSayisi, tarih, getiri, sonuc))

# def giris():
#         baslık="Faiz Hesaplama Programı"
#         print("*"*len(baslık),baslık.upper(),"*"*len(baslık),sep="\n",end="\n\n")

#         tercihYazisi={
#                     "0":"Aşağıdakilerden birini tercih ediniz(Sıra numarasını giriniz) :",
#                     "1":"\n1) Yıllık basit faiz hesaplama",
#                     "2":"\n2) Aylık basit faiz hesaplama",
#                     "3":"\n3) Günlük basit faiz hesaplama"
#                     }
    
#         tercih=input("{}{}{}{}\nTercihiniz :".format(*tercihYazisi.values()))

#         if tercih == "1":
#             hesaplama("yıl", 100)
#         elif tercih == "2":
#             hesaplama("ay", 1200)
#         elif tercih == "3":
#             hesaplama("gün", 36500)
#         else:
#             print("Anlamsız bir tecih numarası girdiniz.")

result = tk.Label(frame1, text="")
result.grid(row=4, column=0)
frame1.pack()
root.mainloop()