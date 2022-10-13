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
Secara default AJAX sudah asynchronous. Terdapat beberapa cara untuk menerapkan hal tersebut, salah satunya adalah menggunakan API ```fetch()```, yang merupakan API request AJAX untuk mereturn ```promise``` yang akan menjadi ```response```.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
### AJAX GET

#### 1. Buatlah view baru yang mengembalikan seluruh data task dalam bentuk JSON. 

#### 2. Buatlah path /todolist/json yang mengarah ke view yang baru kamu buat.

#### 3. Lakukan pengambilan task menggunakan AJAX GET.

### AJAX POST

#### 1. Buatlah sebuah tombol Add Task yang membuka sebuah modal dengan form untuk menambahkan task.

#### 2. Buatlah view baru untuk menambahkan task baru ke dalam database.

#### 3. Buatlah path /todolist/add yang mengarah ke view yang baru kamu buat.

#### 4. Hubungkan form yang telah kamu buat di dalam modal kamu ke path /todolist/add

#### 5. Tutup modal setelah penambahan task telah berhasil dilakukan.

#### 6. Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan list terbaru tanpa reload seluruh page.