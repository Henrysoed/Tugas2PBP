[Investment Portofolio Inventory Application Link](https://investment-portofolio-inventory.adaptable.app)
# Langkah-langkah
## Menyiapkan Library yang diperlukan
Membuat file 'requirements.txt' dengan isi
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```

Lakukan installasi pada terminal dengan:
1. Tanpa Virtual Environment
```sh
pip install -r requirements.txt
```
2. Menggunakan Virtual Environment
```sh
python -m venv venv # membuat virtual env
./venv/Scripts/activate # melakukan aktivasi pada windows
pip install -r requirements.txt
```

## 1. Membuat proyek Django

Buat direktori baru bernama 'NAME' dengan menggunakan command 'django-admin createproject NAME'.
Direktori ini akan berisi file 'manage.py'yang berisi script pyhton yang akan digunakan untuk mengatur proyek dan folder 'NAMA' yang berisi setting dan routing dari proyek. 
Untuk menjalankan proyek, gunakan command 'python manage.py runserver'

## 2. Membuat aplikasi dengan nama main

Buat applikasi bernama 'APPNAME' dengan menggunakan command 'python manage.py createapp APPNAME'. Lalu daftarkan applikasi yang telah dibuat kedalam 'settings.py' pada folder proyek dengan menambahkan 'APPNAME' pada bagian 'INSTALLED_APPS' sehingga seperti di bawah ini
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'APPNAME'
]
```

## 3. Mengonfigurasi Routing URL
Melakukan koknfigurasi link 'APPNAME' dengan menambahkan command 'path('aplikasi/', include('main.urls'))' pada 'urls.py' yang terletak di direktori proyek sehingga seperti dibawah ini
```python
from django.contrib import admin
from django.urls import path, include
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]

```
Tambahkan rute URL seperti berikut untuk mengarahkan ke tampilan 'main' di dalam variabel 'urlpatterns'.
```python
urlpatterns = [
	path('main/', include('main.urls')),
]
```

## 4. Implementasi Template
Buat direktori 'templates' pada 'APPNAME'dan masukkan html 'main.html' seperti dibawah ini
```html
<head>
<title>Investment Portofolio Inventory</title>  
</head>

<body>
<h5>Name: </h5>
<p>Henry Soedibjo</p>
<h5>Class: </h5>
<p>PBP A</p> 
<h5>Amount: </h5>
<p>100</p> 
<h5>Description </h5>
<p>henrysoed Investment Portofolio Inventory for individu task 2 PBP</p> 
</body>
```
pada `views.py` kita dapat mengembalikan `main.html` dengan cara
```python
from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return render(request, 'main.html', context)
```

## 5. Membuat model sebagai Database

Model berfungsi sebagai penghubung python dengan database.Pada Tugas 2 PBP ini, saya ingin membuat database yang berisi nama, amount, dan description masing-masing dengan tipe data character, integer, dan text. Oleh karena itu saya melakukan memodifikasi file `models.py` seperti dibawah ini
```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
```

## Melakukan deployment ke Adaptable
Pastikan repository proyek sudah berada pada github dan bersifat public. Selanjutnya, pada adaptable, pilih opsi `deploy a new app`. Pilih repository sesuai proyek yang akan dideploy. Kemudian `Python App Template`. Selanjutnya adalah opsi database, sementara bisa menggunakan `PostgreSQL`. Sesuaikan versi python dengan versi lokal, `python --version` pada terminal lokal untuk melihat versi. Dan masukan `python manage.py migrate && gunicorn NAMA_PROYEK.wsgi` pada `Start Command`. Tentukan nama applikasi dan checklist `HTTP Listener on PORT`.

# Bagan Request Client ke Web Applikasi Berbasis Django
![Bagan](doc/bagan_django.png)

1. Seorang pengguna meminta browsernya untuk mengakses situs yang menggunakan Django sebagai basisnya
2. Browser akan mengirimkan permintaan HTTP (HTTP Request) untuk halaman web ke server aplikasi
3. Permintaan ini akan mencapai routing yang diatur dalam file 'urls.py', yang akan mencari pola URL yang sesuai dengan permintaan dari pengguna.
4. Setelah pola URL ditemukan, Django akan menjalankan fungsi yang terkait dalam file views.py yang telah terhubung dengan URL tersebut.
5. File views.py dapat melakukan berbagai logika dan operasi terhadap basis data yang telah didefinisikan dalam struktur model yang ada dalam file 'models.py'.
6. Setelah operasi selesai, 'views.py' akan mengirimkan halaman web yang diminta oleh pengguna dalam format HTML, yang tersimpan dalam direktori 'templates'.
7. Browser pengguna kemudian akan merender HTML yang diterima sebagai respons (HTTP Response) dari server Django.

# Mengapa menggunakan Virtual Environment
Virtual environment digunakan dalam pengembangan aplikasi web berbasis Django untuk memisahkan dan mengisolasi dependensi proyek yang berbeda, mencegah konflik antarversi Python dan paket, serta memungkinkan manajemen dependensi yang lebih baik. Meskipun mungkin memungkinkan untuk membuat aplikasi Django tanpa virtual environment, penggunaannya sangat disarankan untuk menjaga kebersihan dan portabilitas kode proyek.

# Apa itu MVC, MVT, dan MVVM
1. MVC (Model View Controller) adalah paradigma desain arsitektur yang memisahkan aplikasi menjadi tiga komponen utama yaitu model (data dan logika bisnis), view (tampilan), dan controller (pengontrol aliran data).
2. MVT (Model-View-Template) adalah paradigma desain arsitektur yang merupakan variasi dari MVC yang digunakan dalam kerangka kerja Django, di mana model (data dan logika bisnis) tetap sama, view (tampilan) lebih berfokus pada presentasi data, dan template digunakan untuk memisahkan logika presentasi.
3. MVVM (Model-View-ViewModel) adalah paradigma desain arsitektur yang memisahkan aplikasi menjadi tiga komponen utama yaitu model (data dan logika bisnis), view (tampilan), dan ViewModel (perantara antara Model dan View yang mengelola tampilan data dan logika presentasi).
