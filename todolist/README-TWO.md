# Link Aplikasi Heroku
https://assignment-2-raditya.herokuapp.com/todolist/

# TUGAS 6

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
1. Asynchronous programming
Bersifat non-blocking, sehingga suatu operasi tidak bergantung pada operasi lain. Dengan begitu, operasi-operasi dapat berjalan bersamaan. Dalam konteks website, penggunaan asynchronous programming memungkinkan user untuk tetap menggunakan website walaupun sedang ada operasi yang dilakukan.

2. Synchronous programming
Bersifat blocking, sehingga suatu operasi bergantung pada operasi lain. Dengan begitu, operasi-operasi tidak dapat berjalan bersamaan. Dalam konteks website, penggunaan synchronous programming membuat user tidak dapat menggunakan website saat sedang ada operasi yang dilakukan.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-Driven Programming adalah suatu paradigma pemrograman di mana alur dari program didasarkan pada event-event yang terjadi, misalnya berbagai action yang dilakukan user berupa mouse click, keyboard input, dan sebagainya.

Salah satu contoh penerapan Event-Driven Programming pada tugas ini adalah penggunaan ```onclick``` pada button untuk menambah task untuk memicu fungsi ```addTodo()``` ketika user klik button Add Task.

## Jelaskan penerapan asynchronous programming pada AJAX.
Secara default AJAX sudah asynchronous. Terdapat beberapa cara untuk menerapkan hal tersebut, salah satunya adalah menggunakan API ```fetch()```, yang merupakan API request AJAX untuk mereturn ```promise``` yang akan menjadi ```response```. Selain itu, dapat juga digunakan ```jQuery.ajax()```.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
### AJAX GET
#### 1. Buatlah view baru yang mengembalikan seluruh data task dalam bentuk JSON. 
Membuat fungsi ```show_json``` pada ```views.py``` sebagai berikut:
```
def show_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

#### 2. Buatlah path /todolist/json yang mengarah ke view yang baru kamu buat.
Menambahkan path pada ```urls.py``` sebagai berikut:
```
urlpatterns = [
    ...
    path('json/', show_json, name='json'),
]
```

#### 3. Lakukan pengambilan task menggunakan AJAX GET.
Buat fungsi async ```getTodo()``` untuk melakukan fetch yang akan mengambil data json dari ```todolist/json/``` sebagai berikut:
```
async function getTodo() {
  return fetch("{% url 'todolist:json' %}").then((res) => res.json())
}
```

### AJAX POST
#### 1. Buatlah sebuah tombol Add Task yang membuka sebuah modal dengan form untuk menambahkan task.
Modal dibuat menggunakan Bootstrap menggunakan ```id="modalAdd"``` untuk menyambungkannya dengan button pada navbar dengan atribut ```data-bs-target="#modalAdd"```. Di dalam content modal akan dimuat form untuk menambahkan task sebagaimana yang terdapat pada ```create-task```

#### 2. Buatlah view baru untuk menambahkan task baru ke dalam database.
Membuat fungsi yang mengecek method POST, mengambil user, title, dan description, serta menyimpan task baru tersebut sebagai berikut:
```
def add(request):
    if request.method == "POST":
        user = request.user
        title = request.POST.get('title')
        description = request.POST.get('description')

        task = Task(user=user, title=title, description=description)
        task.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
```

#### 3. Buatlah path /todolist/add yang mengarah ke view yang baru kamu buat.
Menambahkan path pada ```urls.py``` sebagai berikut:
```
urlpatterns = [
    ...
    path('add/', add, name='add'),
]
```

#### 4. Hubungkan form yang telah kamu buat di dalam modal kamu ke path /todolist/add
Pada bagian footer modal yang sudah dibuat, ditambahkan button dengan ```id="add"``` yang akan dihubungkan dengan fungsi untuk handle add task menggunakan ```onclick```: 
```
document.getElementById("add").onclick = addTodo
```
fungsi untuk menambahkan todo baru akan menggunakan fetch sebagai berikut:
```
function addTodo() {
fetch("{% url 'todolist:add' %}", {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    }).then(refreshTodo)
return false
}
```

#### 5. Tutup modal setelah penambahan task telah berhasil dilakukan.
Menambahkan button baru dengan ```id="close"```, kemudian setelah fetch yang dilakukan pada fungsi addTodo, tambahkan potongan kode: 
```
.then(document.getElementById("close").click())
```

#### 6. Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan list terbaru tanpa reload seluruh page.
Tambahkan potongan kode:
```
.then(refreshTodo)
```
pada akhir fungsi add untuk melakukan refresh, dan tambahkan ```refreshTodo()``` pada akhir script.