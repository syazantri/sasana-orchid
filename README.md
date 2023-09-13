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
     5. Membuat file requirements.txt lalu menginstall dependencynya
          ```shell
            pip install -r requirements.txt
          ```
     6. Membuat proyek Django (yey done membuat proyek Django 😊)
          ```shell
            django-admin startproject sasana-orchid .
          ```
- [x] Membuat aplikasi dengan nama `main` pada proyek tersebut.

     Saya membuat aplikasi main full mengikuti tutorial-1 PBP, berikut langkah-langkahnya:
     1. Membuat app baru bernama main
         ```shell
            python manage.py startapp main
          ```
     2. Mendaftarkan aplikasi main ke dalam proyek dengan cara menambahkan 'main' ke INSTALLED_APPS di settings.py
- [x] Melakukan *routing* pada proyek agar dapat menjalankan aplikasi `main`.
      
     Menambahkan rute URL pada urlpatterns di dalam proyek sasana-orchid agar main bisa diakses (routing tingkat proyek)
- [x] Membuat model pada aplikasi `main` dengan nama `Item` dan memiliki atribut wajib sebagai berikut.
    - `name` sebagai nama *item* dengan tipe `CharField`. 
    - `amount` sebagai jumlah *item* dengan tipe `IntegerField`.
    - `description` sebagai deskripsi *item* dengan tipe `TextField`.
    - ini tinggal diketik saja di dalam models.py dan sesuaikan kriteria tipe field nya.
- [x] Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah *template* HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

     Buat fungsi di views.py dengaan menyesuaikan model data yang telah dibuat, lalu nanti tinggal dipakaai di template
- [x] Membuat sebuah *routing* pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.

     Membuat file urls.py dalam main, lalu mengisi pattern url untuk mengatur routing dalam app main
- [x] Melakukan *deployment* ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

     Buka adaptable, sign in, create new app, pilih python dan postgre, pilih versi python sesuai versi di venv, lalu tambahkan start command python3 manage.py migrate &&  gunicorn shopping_list.wsgi && sudo apt install python3-pip, terakhir checklist HTTP Listener on PORT.
- [x] Membuat sebuah `README.md` yang berisi tautan menuju aplikasi Adaptable yang sudah di-*deploy*, serta jawaban dari beberapa pertanyaan berikut.

     Inilah readme saya.

## 📥 Bagan Request Client dan Response 📥
![](/image/bagan.png)
Pertama user mengetik url pada browser sehingga mengirim http request, lalu di urls.py diatur path (routing) yang sesuai. Setelah dapat path yang sesuai, dicari fungsi mana di views.py yang tepat dan dapat mengolah requestannya. Kemudian hasil fungsi views.py akan ditampilkan melalui html yang ada pada template. Html tersebut pada akhirnya akan menjadi response yang dikirim ke user.

## 💻 Mengapa Harus Menggunakan Virtual Environment? 💻
Virtual Environment digunakan dalam mengerjakan tugas ini agar package dan dependency yang dipakai dalam pengerjaan tugas ini tidak bertabrakan dengan package dan dependency yang ada dalam komputer saya. Yang dimaksud dengan bertabrakan adalah misalnya dependencynya berbeda. Misal versi python yaang ingin dipakai di venv (virtual environment) saya adalah 3.9, tetapi yang ada di komputer saya 3.11.

## ❓ Apa itu MVC, MVT, MVVM? ❓
Ketiganya merupakan konsep arsitektur yang digunakan dalam pengembangan web. Berikut penjelasan dari masing-masing konsep:
1. MVC (Model-View-Controller) : Bisa digunakan untuk banyak framework
     - Model: tempat mengatur bagaimana ketentuan setiap variabel data yang akan dipakai dan logiicnya
     - View: membuat fungsi untuk merespon request dengan mengelola model data atau variabel yang telah dibuat dan memberinya ke input controller
     - Controller: mengakses input user, mengolahnya, lalu mengupdate views dan model
3. MVT (Model-View-Template) :Konsep ini adalah konsep yang dipakai untuk tugas PBP kali ini. MVT biasa digunakan dalam proyek Django, dengan kata lain biasa digunakan dalam bahasa python. Konsep ini terdiri dari tiga struktur utama, yaitu:
     - Model: tempat mengatur bagaimana ketentuan setiap variabel data yang akan dipakai dan logiicnya
     - View: membuat fungsi untuk merespon request dengan mengelola model data atau variabel yang telah dibuat
     - Template: berisi html untuk menampilkan hasil dari views ke halaman web
5. MVVM (Model-View-ViewModel) : Konsep ini cocok dipakai ketika ingin menggunakan dynamic UI, biasa digunakan dalam framework JavaScript seperti Angular
     - Model: tempat mengatur bagaimana ketentuan setiap variabel data yang akan dipakai dan logicnya
     - View: mengelola model data atau variabel yang telah dibuat dengan fungsi-fungsi
     - ViewModel: menyambungkan view dan model
#####
Perbedaan ketiganya adalah MVT dan MVC biasa digunakan untuk server-side atau backend, sedangkan MVVM biasa digunakan pada client-side atau frontend. MVVM juga mampu memisahkan antara view dan model sehingga mudah dipakai untuk mendesign. Lalu MVC yang tidak memisahkan model dan views membuat kita sulit ketika ingin memodifikasi suatu fitur. Lalu pada MVC, controller menghandle user input, pada MVT, view yang menerima request, lalu pada MVVM, view menerima user input sekaligus menerima request.
