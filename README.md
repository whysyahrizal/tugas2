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
