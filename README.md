# Sasana Orchid  \\(^-^)/ 🌸

## 🔗 Link Adaptable 🔗
https://sasana-orchid.adaptable.app/

<details>
    <summary>Tugas 2</summary>
    
### ✅ Implementasi Checklist Tugas ✅
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

### 📥 Bagan Request Client dan Response 📥
![](/image/bagan.png)
Pertama user mengetik url pada browser sehingga mengirim http request, lalu di urls.py diatur path (routing) yang sesuai. Setelah dapat path yang sesuai, dicari fungsi mana di views.py yang tepat dan dapat mengolah requestannya. Kemudian hasil fungsi views.py akan ditampilkan melalui html yang ada pada template. Html tersebut pada akhirnya akan menjadi response yang dikirim ke user.

### 💻 Mengapa Harus Menggunakan Virtual Environment? 💻
Virtual Environment digunakan dalam mengerjakan tugas ini agar package dan dependency yang dipakai dalam pengerjaan tugas ini tidak bertabrakan dengan package dan dependency yang ada dalam komputer saya. Yang dimaksud dengan bertabrakan adalah misalnya dependencynya berbeda. Misal versi python yaang ingin dipakai di venv (virtual environment) saya adalah 3.9, tetapi yang ada di komputer saya 3.11.

### ❓ Apa itu MVC, MVT, MVVM? ❓
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
</details>

<details>
    <summary>Tugas 3</summary>

### <samp> 1️⃣ Apa perbedaan antara form POST dan form GET dalam Django? <samp>
| GET  | POST |
| ------------- | ------------- |
| Parameter atau nilainya terlihat pada URL  | Parameter atau nilainya terlihat pada body |
| Hanya menerima tipe data string  | Menerima banyak dan tipe data, misal binary |
| Dapat dicache  | Tidak bisa dicache |
| Digunakan untuk fetch data  | Digunakan untuk update data |

### <samp> 2️⃣ Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data? <samp>
| XML  | JSON | HTML | 
| ------------- | ------------- | ------------- |
| eXtensible Markup Language | JavaScript Object Notation | Hypertext Markup Language |
| Berbentuk tag custom | Berbentuk list of dictionary | Berbentuk tag bawaan |
| Biasa digunakan untuk data interchange | Biasa digunakan untuk API  | Digunakan untuk menampilkan konten website |
| Kodenya sulit dipahami manusia lain yang bukan pembuatnya | Kodenya mudah dipahami baik oleh komputer maupun manusia | Kodenya mudah dipahami baik oleh komputer maupun manusia |

### <samp> 3️⃣ Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern? <samp>
JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena kesimplean dan efesiensinya. Efisien karena format data JSON yang mudah dipahami manusia sehingga memudahkan debugging dan pengembangan. JSON juga sudah terintegrasi dengaan JavaScript sehingga mudah diproses.

### <samp> 4️⃣ Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). <samp>
✅ Pertama, untuk membuat input form, saya membuat file forms.py di dalam main lalu mengisi model yang akan digunakan (Item) dan field yang akan digunakan. Setelah itu menambah fungsi pada views.py dengan nama create_item untuk menerima request lalu membuat form (tidak lupa mengimpor hal-hal yang diperlukan). Lalu menambahkan fungsi show_main dengan ```items = Item.objects.all()```, untuk mengambil semua item yang ada pada database. Setelah itu mengatur routing dengan menambah path create-item pada urls.py dalam main. Kemudian menyusun kode HTML dengan nama file baru create_item untuk mengatur tampilan web saat user ingin mengisi form.
<br>
✅ Untuk membuat fungsi views dengan format XML dan JSON, sebenarnya mirip-mirip semua. intinya adalah:
```
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
Lalu tinggal diganti-ganti xml nya menjadi json sesuai fungsi yang diinginkan. Fungsi tersebut akan menerima request, menyimpan object Item, lalu mereturn data seluruh object dengan format sesuai yang diinginkan.
Untuk membuat fungsi views HTML sudah ada pada show_main.
Untuk membuat fungsi views XML by ID, dan JSON by ID juga mirip, mirip, intinya:
```
def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
Lalu tinggal diganti-ganti xml nya menjadi json. Fungsi tersebut akan menerima request dan id, menyimpan object Item, lalu mereturn data object id yang diminta dengan format sesuai yang diinginkan.
<br>
✅ Untuk membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2, kita tinggal ke urls.py dalam main, mengimpor fungsi-fungsi yaang akan dipakai (yang telah dibuaat pada views tadi), lalu menambahkan path ke dalam urlpatterns seperti ini:
```
path('html/', show_json, name='show_html'), 
path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
```
Lalu ganti sesuai format yang diinginkan (untuk html sudah ada path show_main nya yaitu di halaman utama). Urlpattern ini akan membuat kita bisa mengakses fungsi-fungsi tersebut melalui url sesuai path yang kita tulis.

### <samp> Screenshot Postman <samp>
✨ 1. Format HTML ✨
<img width="1542" alt="Screenshot 2023-09-20 at 09 32 38" src="https://github.com/syazantri/sasana-orchid/assets/108641343/2dd73c98-d372-45f7-a047-1515c2f555b9">
✨ 2. Format XML ✨
<img width="1542" alt="Screenshot 2023-09-20 at 08 00 26" src="https://github.com/syazantri/sasana-orchid/assets/108641343/e364936f-ed16-488d-822f-6ece07636b42">
✨ 3. Format JSON ✨
<img width="1542" alt="Screenshot 2023-09-20 at 08 00 37" src="https://github.com/syazantri/sasana-orchid/assets/108641343/fdf0c948-9885-4248-958d-f9414482cd2a">
✨ 4. Format XML by ID ✨
<img width="1542" alt="Screenshot 2023-09-20 at 08 01 33" src="https://github.com/syazantri/sasana-orchid/assets/108641343/96ad305b-b6c8-4057-b5bd-cb183be0b966">
✨ 5. Format JSON by ID ✨
<img width="1542" alt="Screenshot 2023-09-20 at 08 01 42" src="https://github.com/syazantri/sasana-orchid/assets/108641343/f777cefe-98a8-477d-9c52-f6e36295d5c0">
</details>

<details>
    <summary>Tugas 4</summary>
    
### <samp> 1️⃣ Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya? 
Django UserCreationForm adalah sebuah class bawaan dari Django yang mampu membuat form untuk registrasi user. Kelebihannya adalah mudah digunakan karena sudah ada <i>built-in</i>nya, tinggal pakai. Kekurangannya adalah sulit untuk <i>custom</i> designnya karena formnya adalah form bawaan dan juga isi formnya simple, jadi kalau mau tambah fitur, harus tambah sendiri.

### <samp> 2️⃣ Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting? 
| AUTENTIKASI  | OTORISASI |
| ------------- | ------------- |
| Tentang identitas siapa user tersebut | Tentang permission yang dimiliki seorang user |
| Tujuannya untuk memastikan identitas user yang sedang ingin mengakses sesuatu  | Tujuannya untuk memastikan actions apa saja yang boleh dilakukan user tertentu |
| Contoh implementasinya login-logout  | Contoh implementasinya mengatur Access Control List (ACL) |
<br>
Keduanya penting karena berhubungan erat dengan keamanan dan privasi data. Ketika sudah dipastikan siapa user tersebut dengaan autentikasi, maka otorisasi akan mengurus tentang apa saja yang boleh dilakukan oleh user tersebut. Implementasi autentikasi dan otorisasi yang baik mampu menjaga dan mengatur keamanan suatu data dengan baik pula karena dapat menghindari penyalahgunaan API. 

### <samp> 3️⃣ Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies adalah data berupa session ID yang disimpan di komputer klien yang berisi mengenai suatu user. Cookies dibuat oleh web server ketika user sedang browsing suatu web. Cookies ini akan memudahkan pengalaman online kita karena web browser jadi lebih tahu tentang kita. Django menggunakan set_cookie yang merupakan <i>built-in method</i> untuk membuat cookie. Lalu untuk mengakses dan memanipulasi cookienya bisa dengan ```request.COOKIES```, untuk mendeletenya menggunakaan ```delete.cookie```

### <samp> 4️⃣ Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Seharusnya mennggunakan cookies dengan implementasi yang benar akan membuat aman. Namun, ada beberapa risiko potensial yang harus diwaspadai seperti serangan XSS(Cross-Site Scripting), serangan CSRF(Cross-Site Request Forgery), ataupun pencurian cookies. Dalam rangka mencegah seranngan-serangan tersebuut, kita sebisa mungkin menggunakan HTTPS agar koneksi server dengan user aman, sehingga tidak mudah cookienya disadap akibat tidak dienkripsi. Lalu, kita juga harus set HttpOnly dan Secure agar pengiriman cookies dalam koneksi yang aman. Lalu sebida mungkin, cookies dipersingkat sessionnya agar tidak mudah dicuri.

### <samp> 5️⃣ Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
✅ Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
<br>
Pertama membuat ketiga fungsi di views, lalu menambahkan file-file html untuk ketiga fitur tersebut, lalu set pathnya ke urls.py yang ada di main (tak lupa impor fungsi-fungsinya dulu).
<br>
✅ Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
<br>
Register 2 kali akun namanya dova dan dino, lalu add item masing-masing 3 kali di akunnya.
<br>
✅ Menghubungkan model ```Item``` dengan ```User```.
<br>
Impor dulu User nya pakai ```from django.contrib.auth.models import User```. Habis itu buat user = models.ForeignKey(User, on_delete=models.CASCADE).
<br>
✅ Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
<br>
Untuk menampilkan detail informasi pengguna sesuai yang lagi log in, itu ubah aja context 'name' fungsi show_main di views.py nya jadi ```'name': request.user.username,```. Jadi nanti context yang dipassing ke main.htmlnya berubah sesuai siapa yang login. Lalu untuk last login tambahkan isi context ```'last_login': request.COOKIES['last_login'],``` lalu pakai di main.html
<br>
✅ Menjawab beberapa pertanyaan berikut pada README.md pada root folder (silakan modifikasi README.md yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).
<br>
Inilah readme saya yeay🥳
<br>
</details>

<details>
    <summary>Tugas 5</summary>
    
### <samp> 1️⃣ Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
Selector pada CSS bermanfaat untuk memilih elemen yang ingin diatur designnya. Ada bermacam-macam contoh element selector css, disesuaikan dengan nama elemen nya, misal p untuk paragraf, h1, h2 untuk header dll. Element selector ini cocok digunakan ketika kita ingin menyeragamkan design suatu elemen. Misal kita ingin semua paragraf warnanya biru, berarti kita element selector p saja seperti ini ``` p {
  color: blue;
} ```
### <samp> 2️⃣ Jelaskan HTML5 Tag yang kamu ketahui.
HTML5 Tag setahu saya ada banyak sekali, 
### <samp> 3️⃣ Jelaskan perbedaan antara margin dan padding.
Intinya setahu saya, padding itu jarak antara elemen dengan konten si elemen. Lalu untuk margin adalah jarak antara elemen dengan elemen-elemen lain di luarnya.
### <samp> 4️⃣ Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
Perbedaan antara keduanya adalah kepraktisannya dalam mendesign. Bootstrap menyediakan banyak komponen tinggal pakai yang cocok untuk pemula dan yang tidak mau ribet, misal card. Tailwind memberi kelonggaran pada web developer untuk lebih mendesign sendiri dan membuat sendiri komponen-komponennya, jadi tailwind lebih unggul dalam flexibilitas design.
### <samp> 5️⃣ Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
✅ Kustomisasi desain pada templat HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut
<br>
    ~~ Saya menggunakan framework Tailwind, sehingga pertama-tama yang dilakukan adalah menginstall package django-tailwind dengan ```python -m pip install django-tailwind```. Lalu 
<br>
✅ Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin.
<br>
    ~~ Untuk warna dominan dari designnya, saya memilih warna pink muda yang code hex nya #FDEAED. Lalu setelah menentukan warna dominan, saya mulai mendesign formnya dengan membuat form ada di tengah-tengah page dan juga mewarnainya. Karena memakai tailwind, saya membaca-baca dokumentasi tailwind di https://v2.tailwindcss.com/docs untuk membantu saya menggunakan tailwind. Dengan menambahkan class di tiap tag yang ingin saya atur designnya, saya dapat menyelesaikan tugas ini. 
<br>
✅ Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan Card.
<br>
    ~~ Untuk halaman daftar inventori, saya menambahkkan navbar dan juga mengganti penampilan item menjadi cards. Saya juga menerapkan transisi background, jadi saya masih menggunakan internal css juga untuk membantu mempermudah transisinya. Lalu saya juga menggunakan script untuk transisinya.
<br>
✅ Menjawab beberapa pertanyaan berikut pada README.md pada root folder (silakan modifikasi README.md yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).
<br>
    Inilah readme saya yeay🥳
<br>
</details>
