Link deployment: [https://whysyahrizal.up.railway.app/tracker/](https://web-production-fe86a.up.railway.app/tracker/)

# Readme Tugas 2

## Bagian 1: Bagan Request dan Response Django

![Django Request-Response Flow](https://niagaspace.sgp1.digitaloceanspaces.com/blog/wp-content/uploads/2022/06/17132515/2-belajar-django-framework-mtv-1024x464.jpg) 

Bagan di atas menjelaskan aliran request dan response dalam aplikasi web Django. Berikut penjelasannya:

1. Client mengirim request ke web server.
2. Web server menerima request dan memprosesnya melalui `urls.py` pada proyek Django.
3. `urls.py` akan memetakan request URL ke fungsi view yang sesuai di `views.py`.
4. Fungsi view dapat mengakses data melalui `models.py`, jika diperlukan.
5. Fungsi view akan merender template HTML yang sesuai dan menggabungkannya dengan data yang diterima dari `models.py`.
6. Fungsi view akan mengembalikan response berupa HTML yang telah dirender.
7. Web server mengirimkan response ke client.

## Bagian 2: Virtual Environment

Virtual environment merupakan suatu lingkungan yang terisolasi untuk mengelola dependensi proyek Python. Penggunaannya sangat direkomendasikan karena memiliki beberapa kelebihan, seperti:

1. Mengisolasi dependensi proyek, sehingga tidak ada konflik antar proyek yang berbeda.
2. Memudahkan untuk mengatur versi pustaka yang berbeda untuk setiap proyek.
3. Menyederhanakan proses deploy aplikasi.

Kita dapat membuat aplikasi web Django tanpa menggunakan virtual environment, tetapi tidak direkomendasikan karena dapat menyebabkan konflik dependensi dan kesulitan dalam mengelola proyek.

## Bagian 3: Implementasi Poin 1-4

1. Membuat aplikasi baru bernama `study_tracker`:
   - Jalankan perintah `python manage.py startapp study_tracker` untuk membuat aplikasi baru.

2. Melakukan routing pada `django_project`:
   - Tambahkan `'study_tracker'` ke dalam `INSTALLED_APPS` pada `settings.py`.
   - Tambahkan `path('study_tracker/', include('study_tracker.urls'))` ke dalam `urlpatterns` pada `urls.py` di proyek Django.
   - Buat berkas `urls.py` di direktori `study_tracker` dan tambahkan konfigurasi routing untuk aplikasi tersebut.

3. Membuat model `Assignment`:
   - Tambahkan model `Assignment` pada `models.py` di aplikasi `study_tracker`:

```python
from django.db import models

class Assignment(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    progress = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
```
- Jalankan perintah `python manage.py makemigrations` dan `python manage.py migrate` untuk membuat tabel `Assignment` pada database.

4. Membuat fungsi pada `views.py`:
   - Tambahkan fungsi `show_tracker` pada `views.py`:

```python
from django.shortcuts import render
from study_tracker.models import Assignment

def show_tracker(request):
    assignment_data = Assignment.objects.all()
    context = {
        'list_of_assignment': assignment_data,
        'name': 'Wahyu Sahrijal'
    } 

    return render(request, "tracker.html", context)
```
- Buat direktori `/study_tracker/templates` dan buat berkas `tracker.html` di dalamnya.
- Tambahkan kode HTML dan template tag Django untuk menampilkan data `Assignment` pada berkas `tracker.html`.

# Readme Tugas 3

## Pertanyaan

### 1. Apakah kita dapat menginput data selain melalui form? Namun mengapa form dapat dikatakan lebih baik daripada menggunakan cara tersebut?

Ya, kita dapat menginput data melalui cara lain seperti melalui API atau langsung memasukkan data ke dalam database. Namun, form lebih baik karena:
- Form memberikan antarmuka yang lebih mudah dan intuitif bagi pengguna.
- Form membantu mencegah kesalahan input data karena dapat memberikan validasi input dan memberikan pesan kesalahan yang relevan.
- Form menyediakan cara yang konsisten dan terstruktur untuk mengumpulkan informasi dari pengguna.

### 2. Jelaskan perbedaan antara JSON, XML, dan HTML!

- JSON (JavaScript Object Notation) adalah format ringan untuk pertukaran data. JSON mudah dibaca dan ditulis oleh manusia serta mudah diurai dan dihasilkan oleh mesin. JSON biasanya digunakan dalam aplikasi web untuk mengirim dan menerima data melalui API.

- XML (eXtensible Markup Language) adalah bahasa markup yang digunakan untuk menyimpan dan mengangkut data. XML adalah format yang agak lebih kompleks dan lebih berat daripada JSON. XML mendukung penggunaan atribut dan namespace, yang membuatnya lebih fleksibel daripada JSON.

- HTML (Hypertext Markup Language) adalah bahasa markup yang digunakan untuk membuat dan merender dokumen web. HTML mendefinisikan struktur dan tampilan halaman web menggunakan elemen dan atribut. Berbeda dengan JSON dan XML, HTML lebih fokus pada penyajian data daripada struktur data.

### 3. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform.

Kita memerlukan data delivery karena:
- Data delivery memungkinkan pertukaran data antara sistem yang berbeda atau komponen dalam platform.
- Data delivery membantu dalam integrasi sistem dan mempermudah pengembangan aplikasi dengan menyediakan API atau titik akses data.
- Data delivery memungkinkan aplikasi untuk menyajikan data dalam format yang berbeda sesuai dengan kebutuhan pengguna, seperti JSON, XML, atau HTML.

### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Membuat form pada `forms.py`:
   - Buat berkas `forms.py` di direktori `study_tracker`.
   - Buat kelas `AssignmentForm` dan sesuaikan fields dengan model `Assignment`

2. Membuat fungsi baru pada `views.py`:
   - Import `AssignmentForm` dan tambahkan fungsi `create_assignment`

3. Membuat file HTML baru untuk menampilkan form:
   - Buat file `form_create_assignment.html` di direktori `/study_tracker/templates`.
   - Tambahkan kode berikut untuk menampilkan form

4. Modifikasi file HTML yang menampilkan tabel tugas:
   - Buka file `tracker.html` di direktori `/study_tracker/templates`.
   - Tambahkan tombol untuk menuju ke halaman form

5. Menyajikan data dalam format XML dan JSON:
   - Tambahkan dua fungsi baru pada `views.py` untuk menghasilkan data dalam format XML dan JSON

6. Membuat routing untuk XML dan JSON:
   - Tambahkan path baru pada `urls.py` di direktori `study_tracker`

# Readme Tugas 4

## Jawaban:

1. {% csrf_token %} digunakan untuk mencegah serangan Cross-Site Request Forgery (CSRF). Jika tidak ada potongan kode ini pada elemen `<form>`, aplikasi akan rentan terhadap serangan CSRF, yang memungkinkan pengguna jahat untuk melakukan aksi yang tidak sah atas nama pengguna yang sah.

2. Ya, kita dapat membuat elemen `<form>` secara manual tanpa menggunakan generator seperti `{{ form.as_table }}`. kita dapat menentukan setiap bidang form secara individual, seperti `<input type="text" name="username">` untuk bidang username. Pastikan kita menambahkan atribut `name` yang sesuai dan `{% csrf_token %}` pada elemen `<form>`.

3. Alur data dari submisi form melalui HTML, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML melibatkan beberapa langkah:
   - Pengguna mengisi form dan menekan tombol submit
   - Data dikirim ke view yang ditentukan dalam atribut `action` elemen `<form>`
   - View menerima data dan melakukan validasi (jika ada)
   - View menyimpan data ke database
   - View mengambil data yang disimpan dari database dan mengirimkannya ke template HTML
   - Template HTML menampilkan data yang telah disimpan

Berikut adalah langkah-langkah untuk mengimplementasikan poin checklist yang kita sebutkan:

1. Membuat form registrasi pada aplikasi study tracker:

   - Buat file `register.html` di dalam folder `study_tracker/templates`
   - Isi file tersebut dengan kode HTML untuk form registrasi, pastikan kita menggunakan `{% csrf_token %}` di dalam elemen `<form>` dan memasukkan informasi yang diperlukan dari `UserCreationForm`

2. Membuat form login pada aplikasi study tracker:

   - Buat file `login.html` di dalam folder `study_tracker/templates`
   - Isi file tersebut dengan kode HTML untuk form login, pastikan kita menggunakan `{% csrf_token %}` di dalam elemen `<form>` dan memasukkan informasi yang diperlukan untuk login

3. Membuat fungsi logout pada aplikasi study tracker:

   - Tambahkan fungsi `logout_user` pada `views.py`, yang akan menghapus informasi login dan mengalihkan pengguna ke halaman utama
   - Tambahkan URL untuk fungsi logout ini di `urls.py`

4. Melakukan restriksi akses pada halaman study tracker:

   - Gunakan decorator `@login_required(login_url='/study_tracker/login/')` sebelum fungsi `show_tracker` di `views.py` untuk memastikan bahwa hanya pengguna yang telah login yang dapat mengakses halaman study tracker

5. Membuat sebuah README.md:

   - Buat file README.md di folder utama aplikasi kita
   - Isi file tersebut dengan informasi yang relevan, seperti tautan ke aplikasi Railway yang sudah di-deploy (jika ada), dan jawaban untuk pertanyaan yang diberikan

# Readme Tugas 5

1. Perbedaan dari inline, internal, dan external CSS adalah:

- Inline CSS: CSS yang diterapkan langsung ke elemen HTML dengan menambahkan atribut "style" pada tag. Contohnya: `<p style="color: blue;">Ini teks berwarna biru</p>`. Kelebihan dari inline CSS adalah mudah diterapkan dan bisa membuat styling yang spesifik untuk satu elemen tertentu, namun kelemahannya adalah sulit untuk diatur ulang dan membuat perubahan pada seluruh elemen yang membutuhkan styling yang sama.

- Internal CSS: CSS yang ditulis di dalam tag `<style>` pada bagian head dokumen HTML. Contohnya:

```html
<head>
  <style>
    p {
      color: blue;
    }
  </style>
</head>
```

Kelebihan dari internal CSS adalah bisa diterapkan pada seluruh elemen yang sama dalam dokumen HTML dan mudah diatur ulang jika dibutuhkan, namun kelemahannya adalah masih terbatas pada satu dokumen HTML saja.

- External CSS: CSS yang disimpan di file terpisah dengan ekstensi .css dan dihubungkan dengan dokumen HTML dengan menggunakan tag `<link>` pada bagian head dokumen HTML. Contohnya:

```html
<head>
  <link rel="stylesheet" href="style.css">
</head>
```

Kelebihan dari external CSS adalah mudah diatur ulang dan bisa digunakan pada berbagai dokumen HTML, namun kelemahannya adalah membutuhkan waktu loading yang lebih lama karena memerlukan request ke server untuk mengambil file CSS.

2. Tag HTML5 yang saya ketahui antara lain:

- `<header>`: digunakan untuk mengelompokkan konten bagian atas (atas halaman atau suatu bagian tertentu).
- `<nav>`: digunakan untuk mengelompokkan tautan navigasi.
- `<section>`: digunakan untuk mengelompokkan konten menjadi bagian-bagian yang lebih besar.
- `<article>`: digunakan untuk mengelompokkan konten mandiri yang bisa berdiri sendiri, seperti artikel, postingan blog, atau berita.
- `<aside>`: digunakan untuk mengelompokkan konten pendukung dari konten utama, seperti sidebar atau iklan.
- `<footer>`: digunakan untuk mengelompokkan konten bagian bawah (bawah halaman atau suatu bagian tertentu).

3. Beberapa tipe CSS selector yang saya ketahui antara lain:

- Selector Elemen: Menggunakan nama elemen untuk memilih elemen pada dokumen HTML, contohnya `p` untuk memilih semua paragraf pada dokumen HTML.
- Selector Kelas: Menggunakan nama kelas untuk memilih elemen dengan kelas tertentu, contohnya `.kelas` untuk memilih elemen dengan kelas "kelas".
- Selector ID: Menggunakan nama ID untuk memilih elemen dengan ID tertentu, contohnya `#id` untuk memilih elemen dengan ID "id".
- Selector Universal: Menggunakan tkita bintang (*) untuk memilih semua elemen pada dokumen HTML.
- Selector Grup: Menggunakan tkita koma (,) untuk memilih beberapa selector dalam satu perintah, contohnya `p, .kelas, #id` untuk memilih semua paragraf, elemen dengan kelas "kelas", dan elemen dengan ID "

Untuk mengimplementasikan checklist yang diberikan, berikut adalah langkah-langkah yang dapat diikuti:

1. Menggunakan Bootstrap:
   - Tambahkan tautan CDN Bootstrap pada file `base.html` di dalam tag `<head>`:
    ```
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    ```

2. Kustomisasi templat untuk halaman login, register, dan add tugas:
   - Untuk halaman login dan register, kita dapat menggunakan class Bootstrap seperti `container`, `row`, `col`, `form-control`, dan `btn` untuk merapikan dan membuat tata letak yang menarik.
   - Untuk halaman tambah tugas, gunakan class Bootstrap seperti `form-label`, `form-control`, dan `btn` untuk membuat form yang lebih menarik dan mudah digunakan.

3. Kustomisasi halaman utama study tracker menggunakan cards:
   - Ubah tabel dalam `tracker.html` dengan menggunakan komponen card Bootstrap. Gunakan class `card`, `card-body`, `card-title`, dan `card-text` untuk menampilkan informasi tugas dalam bentuk card.
   - kita dapat menggunakan class `row` dan `col` untuk mengatur card tugas secara responsif pada layar yang berbeda.

4. Membuat keempat halaman yang dikustomisasi menjadi responsive:
   - Bootstrap sudah mendukung responsivitas secara default. Pastikan kita menggunakan class `container`, `row`, dan `col` untuk mengatur elemen pada halaman.
   - kita juga dapat menggunakan class `d-*-none`, `d-*-block`, `d-*-inline`, dan `d-*-inline-block` untuk mengontrol visibilitas elemen pada berbagai ukuran layar.

5. Menambahkan button ubah untuk memperbarui data tugas:
   - Tambahkan tombol 'Ubah' pada setiap card tugas di `tracker.html`. Berikan atribut `href` yang mengarah ke view `update_assignment` dengan ID tugas yang relevan.
   - Buat view `update_assignment` yang menampilkan form dengan data tugas yang ada dan memproses data yang diperbarui saat form dikirim.

6. Menambahkan button hapus untuk menghapus data tugas:
   - Tambahkan tombol 'Hapus' pada setiap card tugas di `tracker.html`. Berikan atribut `href` yang mengarah ke view `delete_assignment` dengan ID tugas yang relevan.
   - Buat view `delete_assignment` yang menghapus tugas saat tombol 'Hapus' diklik dan mengarahkan pengguna kembali ke halaman utama.

Dengan mengikuti langkah-langkah di atas, kita dapat mengimplementasikan semua poin dalam checklist yang kita berikan.

# Readme Tugas 6


1. Perbedaan antara asynchronous programming dan synchronous programming:
   - Synchronous programming: kode dieksekusi secara berurutan, dan proses berikutnya harus menunggu proses sebelumnya selesai. Ini mengakibatkan aplikasi yang responsif terhambat.
   - Asynchronous programming: kode dieksekusi tanpa menunggu proses sebelumnya selesai. Ini memungkinkan aplikasi untuk tetap responsif dan melakukan beberapa tugas secara bersamaan.

2. Event-driven programming adalah paradigma pemrograman di mana aliran eksekusi kode ditentukan oleh peristiwa (events), seperti klik mouse atau input keyboard. Pada tugas ini, contoh penerapan event-driven programming adalah menambahkan event listener ke tombol submit form yang akan menangani pengiriman form secara asinkronus menggunakan AJAX.

3. Penerapan asynchronous programming pada AJAX: AJAX (Asynchronous JavaScript and XML) adalah teknologi yang memungkinkan pertukaran data antara browser dan server secara asinkronus. Dengan AJAX, Anda dapat memuat data baru atau mengirim data ke server tanpa memuat ulang seluruh halaman. Ini memungkinkan aplikasi web lebih responsif dan dinamis.

4. Untuk mengimplementasikan checklist:
   - Buat view baru dan URL yang mengarah ke view tersebut.
   - Tambahkan modal dengan form di `tracker.html` dan hubungkan ke URL yang baru dibuat.
   - Gunakan JavaScript untuk menambahkan event listener ke tombol submit form.
   - Kirim data ke server menggunakan AJAX dan tutup modal setelah berhasil menambahkan tugas.
   - Refresh bagian halaman yang menampilkan daftar tugas secara asinkronus menggunakan AJAX untuk memperbarui daftar tanpa memuat ulang seluruh halaman.
