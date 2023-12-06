import os
from PyPDF2 import PdfReader

def list_pdf_files(directory):
    pdf_files = []
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            pdf_files.append(filename)
    return pdf_files

def extract_titles(directory, output_directory):
    pdf_files = list_pdf_files(directory)
    index = []

    for filename in pdf_files:
        filepath = os.path.join(directory, filename)
        with open(filepath, "rb") as file:
            pdf = PdfReader(file)
            if "/Title" in pdf.trailer:
                title = pdf.trailer["/Title"]
                index.append(title)

    save_index_to_file(index, output_directory)

def save_index_to_file(index, output_directory):
    output_file = os.path.join(output_directory, "index.txt")

    with open(output_file, "w") as file:
        for title in index:
            file.write(f"- {title}\n")

def display_menu():
    print("------- Menü -------")
    print("1. Klasördeki PDF dosyalarını listele")
    print("2. Başlıkları çıkar ve başka bir klasöre kaydet")
    print("3. Çıkış")
    print("--------------------")

def main():
    while True:
        display_menu()
        choice = input("Lütfen bir seçenek girin (1-3): ")

        if choice == "1":
            directory = input("Lütfen klasör yolunu girin: ")
            pdf_files = list_pdf_files(directory)
            print("PDF Dosyaları:")
            for filename in pdf_files:
                print(filename)
            print()

        elif choice == "2":
            directory = input("Lütfen klasör yolunu girin: ")
            output_directory = input("Lütfen çıktı klasörünün yolunu girin: ")
            extract_titles(directory, output_directory)
            print("Dizinleme tamamlandı. İndeks dosyası kaydedildi.")
            print()

        elif choice == "3":
            print("Çıkış yapılıyor...")
            break

        else:
            print("Geçersiz seçenek! Lütfen tekrar deneyin.")
            print()

if __name__ == "__main__":
    main()