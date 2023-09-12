# Sasana Orchid \(^-^)/ 🌸

## 🔗 Links Adaptable 🔗
https://sasana-orchid.adaptable.app/

## ✅ Implementasi Checklist Tugas ✅
- [x] Membuat sebuah proyek Django baru

     Saya membuat proyek Django full mengikuti tutorial-0 PBP, berikut langkah-langkahnya:
     1. Membuat repo github lalu clone ke local
         ```shell
             git clone <URL repo github>
          ```
     3. Membuat virtual environment
          ```shell
            python -m venv env
          ```
     4. Menyalakan virtual environment (karena saya menggunakan MacOS jadi begini)
          ```shell
            source env/bin/activate
          ```
     5. Membuat requirements.txt lalu menginstall dependencynya
          ```shell
            pip install -r requirements.txt
          ```
     6. Membuat proyek Django (yey done membuat proyek Django 😊)
          ```shell
            pip install -r requirements.txt
          ```
- [x] Membuat aplikasi dengan nama `main` pada proyek tersebut.

     Saya membuat aplikasi main full mengikuti tutorial-1 PBP, berikut langkah-langkahnya:
     1. Membuat app baru bernama name
         ```shell
            python manage.py startapp main
          ```
     2. Mendaftarkan aplikasi main ke dalam proyek dengan cara menambahkan 'main' ke INSTALLED_APPS di settings.py
- [x] Melakukan *routing* pada proyek agar dapat menjalankan aplikasi `main`.
- [x] Membuat model pada aplikasi `main` dengan nama `Item` dan memiliki atribut wajib sebagai berikut.
    - `name` sebagai nama *item* dengan tipe `CharField`.
    - `amount` sebagai jumlah *item* dengan tipe `IntegerField`.
    - `description` sebagai deskripsi *item* dengan tipe `TextField`.
- [x] Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah *template* HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
- [x] Membuat sebuah *routing* pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.
- [x] Melakukan *deployment* ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- [x] Membuat sebuah `README.md` yang berisi tautan menuju aplikasi Adaptable yang sudah di-*deploy*, serta jawaban dari beberapa pertanyaan berikut.

## 📥 Bagan Request Client dan Response 📥

## 💻 Mengapa Harus Menggunakan Virtual Environment? 💻

## ❓ Apa itu MVC, MVT, MVVM? ❓
