# Link Aplikasi Heroku
katalog page: https://assignment-2-raditya.herokuapp.com/katalog/

main page: https://assignment-2-raditya.herokuapp.com

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;

## Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Sebenarnya penggunaan virtual environment tidak wajib dalam pembuatan sebuah project Django. Akan tetapi, penggunaan virtual environment juga sangat disarankan karena beberapa hal berikut:

* Tanpa adanya virtual environment, perubahan atau update yang dilakukan terhadap dependencies akan berpengaruh ke environment global PC dan berpotensi mempengaruhi project lain.
* Project yang dikerjakan bisa saja memiliki dependencies yang berbeda-beda. Maka agar tidak mengusik pengaturan OS yang digunakan, dependencies akan diisolasi di dalam virtual environment.
* Misal project ingin dikerjakan pada beberapa PC yang memiliki versi library/package berbeda, akan lebih mudah apabila dependencies sudah diisolasi berdasarkan project tersebut menggunakan virtual environment.

## Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

#### 1. Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.


#### 2. Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py.


#### 3. Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.


#### 4. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
