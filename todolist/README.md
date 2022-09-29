## Link Aplikasi Heroku
https://assignment-2-raditya.herokuapp.com/todolist/

## Apa kegunaan ```{% csrf_token %}``` pada elemen ```<form>```? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen ```<form>```?
Tag tersebut menyediakan proteksi terhadap Cross Site Request Forgery (CSRF). CSRF itu sendiri merupakan tipe serangan yang terjadi ketika website membuat suatu browser mengirim request yang dapat melakukan perubahan yang tidak diinginkan pada server.  

## Apakah kita dapat membuat elemen ```<form>``` secara manual (tanpa menggunakan generator seperti ```{{ form.as_table }}```)? Jelaskan secara gambaran besar bagaimana cara membuat ```<form>``` secara manual.
Bisa, tag ```<form>``` serta penggunaan tag ```{% csrf_token %}``` dilakukan sama seperti jika mmenggunakan generator. Perbedaannya terdapat pada cara menampilkan isi formnya itu sendiri. Dalam tugas ini, penampilan form diatur dalam tag ```<table>```. Masing-masing elemen yang membutuhkan input akan menggunakan tag ```<input>``` dengan atribut yang diatur sesuai dengan kebutuhan field masing-masing.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.


## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
#### 1. Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya.
Pada repository yang sama, gunakan command ```python manage.py startapp todolist```

#### 2. Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.
Path ditambahkan di file settings.py project_django sebagai berikut:
``` 
INSTALLED_APPS = [
    ...
    'todolist',
]
```

serta ditambahkan di urls.py sebagai berikut:
```
urlpatterns = [
    ...
    path('todolist/', include('todolist.urls')),
]
```

#### 3. Membuat sebuah model Task
Buat class baru di models.py dengan field sebagai berikut:
```
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
```
```auto_now_add=True``` pada date berfungsi untuk mengambil current time server saat menambahkan data Task sebagai default date.

#### 4. Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.
* Registrasi
Pada ```views.py```, ditambahkan fungsi ```register``` yang akan menggunakan ```UserCreationForm()``` untuk membuat form. Form tersebut kemudian akan digenerate oleh html pada ```register.html```. path register juga akan ditambahkan pada ```urls.py``` sebagai berikut:
```path('register/', register, name='register'),```

* Login
Pada ```views.py```, ditambahkan fungsi ```login_user``` untuk membuat form. Form tersebut kemudian akan digenerate oleh html pada ```register.html```. path login juga akan ditambahkan pada ```urls.py``` sebagai berikut:
```path('login/', login_user, name='login'),```


* Logout
Pada ```views.py```, ditambahkan fungsi ```logout_user``` untuk membuat form. Form tersebut kemudian akan digenerate oleh html pada ```register.html```. path logout juga akan ditambahkan pada ```urls.py``` sebagai berikut:
```path('logout/', logout_user, name='logout'),```


#### 5. Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.
Membuat terlebih dahulu fungsi ```show_html(request)``` pada ```views.py``` yang mengambil data-data todolist yang difilter berdasarkan user, yang mengembalikan data-data tersebut. Kemudian membuat ```todolist.html``` yang mengambil data-data dari ```show_html(request)``` dan menampilkannya melalui tabel.

Untuk menampilkan username, ditambahkan potongan kode berikut: ```<p>User logged in: {{user}}</p>```

Untuk menampilkan tombol tambah task baru dan tombol logout, ditambahkan potongan kode berikut (masing-masing tombol akan mengarahkan ke url sesuai fungsinya di ```views.py```): 
```
<button><a href="{% url 'todolist:create-task' %}">Create Task</a></button>
<button><a href="{% url 'todolist:logout' %}">Logout</a></button>
```

Untuk menampilkan tabel, ditambahkan potongan kode berikut: ```
<table>
    <tr>
    <th>Date</th>
    <th>Title</th>
    <th>Description</th>
    </tr>
    {% comment %} Tambahkan data di bawah baris ini {% endcomment %}
    {% for item in list %}
    <tr>
        <th>{{item.date}}</th>
        <th>{{item.title}}</th>
        <th>{{item.description}}</th>
    </tr>
    {% endfor %}
</table>
```

#### 6. Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.
Pada ```views.py```, dibuat ```ModelForm``` baru bernama ```NewTask``` yang memuat class ```Meta``` sebagai berikut.
```
class NewTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
```
Dengan begitu, form akan mengambil title dan descrition sesuai dengan tipe field yang sudah dispesifikasikan di ```models.py```. Date sudah memiliki nilai default dan user akan dihandle di ```views.py```.

Kemudian dibuat fungsi ```add_task``` untuk generate form dan mengarahkan ke ```add_task.html```. Form akan divalidasi, disave, dan task baru juga akan mengambil data user di fungsi ini.

```add_task.html``` akan generate form dengan menggunakan ```{{ form.as_table }}```. 

#### 7. Membuat routing
Pada ```urlpatterns``` di file ```urls.py``` todolist, tambahkan potongan kode berikut:

* http://localhost:8000/todolist berisi halaman utama yang memuat tabel task.
```path('', show_html, name = "show_html"),```
* http://localhost:8000/todolist/login berisi form login.
```path('login/', login_user, name='login'),```

* http://localhost:8000/todolist/register berisi form registrasi akun.
```path('register/', register, name='register'),```

* http://localhost:8000/todolist/create-task berisi form pembuatan task.
```path('create-task/', add_task, name='create-task'),```

* http://localhost:8000/todolist/logout berisi mekanisme logout.
```path('logout/', logout_user, name='logout'),```

#### 8. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
Caranya sama dengan pada tugas 2, namun karena repository ini sudah dideploy, maka kita tidak perlu mengulang langkahnya dari nol.

Untuk memastikan todolist terdaftarkan pada website heroku, ditambahkan ```'todolist'``` pada ```INSTALLED_APPS``` file ```./project_django/settings.py```, serta tambahkan routing dengan menambah kode ```path('todolist/', include('todolist.urls')),``` pada ```urlpatterns``` di file ```./project_django/urls.py```.

#### 9. Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.
Buat terlebih dahulu akun dengan cara register, kemudian login melalui masing-masing akun. Pada masing-masing akun, lakukan create task 3 kali untuk membuat 3 dummy data tersebut.