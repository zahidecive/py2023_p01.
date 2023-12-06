import time
from tkinter import *
from tkinter import ttk


class PDFManager:
    def dataRead(self):
        print("PDF Listeleme işlemi yapılıyor.")

    def dataWrite(self):
        print("PDF Okuma işlemi yapılıyor.")

    def getWeb(self):
        print("PDF'leri Dizinleme işlemi yapılıyor.")


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="PDF Dizinleme ve Okuma").grid(column=0, row=0)
ttk.Button(frm, text="Çıkış", command=root.destroy).grid(column=1, row=0)

# Buton
ttk.Button(frm, text="PDF Listele").grid(column=0, row=1, pady=5)
ttk.Button(frm, text="PDF Oku").grid(column=0, row=2, pady=5)
ttk.Button(frm, text="PDF'leri Dizinle").grid(column=0, row=3, pady=5)

root.mainloop()

print("-: PDF Dosyalama ve Dizinleme Uygulamasına Hoş Geldiniz! :")
print("|------------------------------|")
print("")
time.sleep(2)

pdf_manager = PDFManager()

while True:
    print("Menü: 0)Çıkış 1)PDF Listele 2)PDF Oku 3)PDF Dizinle")
    menuSecim = input("Tercihiniz: ")
    if menuSecim.isdigit():
        menuSecim = int(menuSecim)
        if menuSecim == 0:
            print("Kapatılıyor...")
            time.sleep(1)
            break
        elif menuSecim == 1:
            pdf_manager.dataRead()
        elif menuSecim == 2:
            pdf_manager.dataWrite()
        elif menuSecim == 3:
            pdf_manager.getWeb()
        else:
            print("Lütfen geçerli bir seçim yapınız.")
    else:
        print("Lütfen geçerli bir seçim yapınız.")