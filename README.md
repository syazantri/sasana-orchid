# Sasana Orchid  \\(^-^)/ 🌸

## 🔗 Link Adaptable 🔗
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
      
     Saya melakukan routing full mengikuti tutorial-1 PBP, berikut langkah-langkahnya:
     1. Membuat file urls.py dalam main, lalu mengisinya sesuai yang ada di urls.py saya sekarang
     2. Menambahkan rute URL pada urlpatterns di dalam sasana-orchid agar main bisa diaakses
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
Virtual Environment digunakan dalam mengerjakan tugas ini agar package dan dependency yang dipakai dalam pengerjaan tugas ini tidak bertabrakan dengan package dan dependency yang ada dalam komputer saya. Yang dimaksud dengan bertabrakan adalah misalnya dependencynya berbeda. Misal versi python yaang ingin dipakai di venv (virtual environment) saya adalah 3.9, tetapi yang ada di komputer saya 3.11.

## ❓ Apa itu MVC, MVT, MVVM? ❓
Ketiganya merupakan konsep arsitektur yang digunakan dalam pengembangan web. Berikut penjelasan dari masing-masing konsep:
1. MVC (Model-View-Controller)
     
3. MVT (Model-View-Template) Konsep ini adalah konsep yang dipakai untuk tugas PBP kali ini. MVT terdiri dari tiga struktur utama, yaitu:
     - Model: tempat mengatur bagaimana ketentuan setiap variabel data yang akan dipakai
     - View: mengelola model data atau variabel yang telah dibuat dengan fungsi-fungsi
     - Template: berisi html untuk menampilkan hasil dari views ke halaman web
   MVT biasa digunakan dalam proyek Django,
5. MVVM (Model-View-ViewModel)
Perbedaan ketiganya adalah
