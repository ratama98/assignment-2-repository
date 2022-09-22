## Link Aplikasi Heroku
HTML  : https://assignment-2-raditya.herokuapp.com/mywatchlist/html/

XML   : https://assignment-2-raditya.herokuapp.com/mywatchlist/xml/

JSON  : https://assignment-2-raditya.herokuapp.com/mywatchlist/json/

## Jelaskan perbedaan antara JSON, XML, dan HTML!
* HTML fokus pada cara menampilkan data, sedangkan XML dan JSON fokus pada mendeskripsikan dan menampung data.
* Data pada HTML dan XML disimpan dalam tag-tag markup, sedangkan data pada JSON disimpan dalam bentuk key dan value.
* Untuk data interchange, JSON umumnya lebih cepat daripada XML. Hal ini karena JSON, yang merupakan object notation Javascript, bersifat native terhadap javascript. Kemudian, data dari XML juga harus diambil dari tag markupnya terlebih dahulu.

Sumber referensi:

[Difference between html vs xml vs json - Medium.com](https://medium.com/@oazzat19/what-is-the-difference-between-html-vs-xml-vs-json-254864972bbb)

[Difference between JSON and XML](https://www.google.com/amp/s/www.geeksforgeeks.org/difference-between-json-and-xml/amp/)


## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Tanpa adanya data delivery, website yang dibuat akan bersifat statis, berarti data yang ditampilkan akan selalu sama kecuali jika diubah langsung dari servernya. Sementara itu, penggunaan data delivery dapat membuat website dinamis yang memungkinkan "komunikasi" antara pengguna dan server. Dengan begitu, tampilan website dapat berubah-ubah secara berkala sesuai dengan update yang dilakukan baik dari sisi pengguna maupun sisi server.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
#### 1. Membuat suatu aplikasi baru bernama mywatchlist di proyek Django Tugas 2 pekan lalu
Poin ini dilakukan dengan menjalankan command berikut:

```python manage.py startapp mywatchlist```

#### 2. Menambahkan path mywatchlist sehingga pengguna dapat mengakses http://localhost:8000/mywatchlist
Path ditambahkan di file settings.py project_django sebagai berikut:
``` 
INSTALLED_APPS = [
    ...
    'mywatchlist',
]
```

serta ditambahkan di urls.py sebagai berikut:
```
urlpatterns = [
    ...
    path('mywatchlist/', include('mywatchlist.urls')),
]
```

#### 3. Membuat sebuah model MyWatchList
Buat class baru di models.py dengan field sebagai berikut:
```
class MyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=255)
    rating  = models.FloatField(
        default=1.00,
        validators = [MaxValueValidator(5.00),MinValueValidator(1.00)]
    )
    release_date = models.DateField()
    review = models.TextField()
```

#### 4. Menambahkan minimal 10 data untuk objek MyWatchList yang sudah dibuat di atas
Membuat folder fixtures kemudian membuat file bernama initial_watchlist_data.json dan menambahkan data-data ke dalam file tersebut. Berikut contoh salah satu data yang ditambahkan:
```
[
    {
        "model": "mywatchlist.mywatchlist",
        "pk": 1,
        "fields": {
            "watched": false,
            "title": "Satria Dewa: Gatotkaca",
            "rating": 1.11,
            "release_date": "2022-06-09",
            "review": "Saatnya menggatot or something idk haven't watched it"
        }
    },
    ...
]
```
Setelah itu, file template html juga harus bisa memetakan data sesuai dengan list yang sudah dibuat pada initial_watchlist_data.json. Berikut cara menampilkan data-data tersebut di file template html:
```
{% for item in list %}
    <tr>
        <th>{{item.watched}}</th>
        <th>{{item.title}}</th>
        <th>{{item.rating}}</th>
        <th>{{item.release_date}}</th>
        <th>{{item.review}}</th>
    </tr>
    {% endfor %}
```
Terakhir, model harus dimigrasi serta data dari initial_watchlist_data.json harus dimasukkan ke database lokal Django dengan perintah berikut:
```
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata initial_watchlist_data.json
```

#### 5. Mengimplementasikan sebuah fitur untuk menyajikan data yang telah dibuat sebelumnya dalam tiga format (HTML, XML, JSON)
views.py berperan dalam memilih dan mengolah format yang akan digunakan, berikut potongan code yang digunakan dalam implementasinya (nama function sesuai format yang akan ditampilkan):
```
def show_html(request):
    data_mywatchlist = MyWatchList.objects.all()
    context = {
        "student_nama": "Raditya Aditama",
        "student_id": "2106750313",
        "list": data_mywatchlist ,
    }

    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    
def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

#### 6. Membuat routing sehingga data di atas dapat diakses melalui URL terpisah
Routing fungsi-fungsi pada views.py tersebut akan dilakukan di urls.py folder mywatchlist. Berikut routing untuk ketiga format tersebut:
```
urlpatterns = [
    path('html/', show_html, name = "show_html"),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
]
```

#### 7. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
Caranya sama dengan pada tugas 2, namun karena repository ini sudah dideploy, maka kita tidak perlu mengulang langkahnya dari nol.

Untuk memastikan fixtures mywatchlist diload, file Procfile perlu diupdate sebagai berikut:
```
release: sh -c 'python manage.py migrate && python manage.py loaddata initial_catalog_data.json && python manage.py loaddata initial_watchlist_data.json'
web: gunicorn project_django.wsgi --log-file -
```
Di sini, bagian release ditambahkan ```python manage.py loaddata initial_watchlist_data.json``` untuk load initial_watchlist_data.json ke database local django.


#### 8. Menambahkan unit test pada tests.py untuk menguji bahwa tiga URL di poin 6 dapat mengembalikan respon HTTP 200 OK
Setup terlebih dahulu file tests.py dengan menambahkan class testcase baru sebagai berikut:
```
class WatchlistTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.html = "/mywatchlist/html/"
        self.xml = "/mywatchlist/xml/"
        self.json = "/mywatchlist/json/"

    def test_html(self):
        response = self.client.get(self.html)
        self.assertEqual(response.status_code, 200)

    def test_xml(self):
        response = self.client.get(self.xml)
        self.assertEqual(response.status_code, 200)

    def test_json(self):
        response = self.client.get(self.json)
        self.assertEqual(response.status_code, 200)
```

Setelah itu, untuk menjalankan test hanya perlu menjalankan perintah ```python manage.py test```

## Screenshot Postman
#### HTML
![postman_html](https://user-images.githubusercontent.com/90949238/191583113-f4ec1c05-de38-43c1-8036-17edc5856d43.png)
#### XML
![postman_xml](https://user-images.githubusercontent.com/90949238/191582906-5e403443-f307-4243-9fc9-b211b7ec6cef.png)
#### JSON
![postman_json](https://user-images.githubusercontent.com/90949238/191582870-8b603004-1255-4276-8a7c-7547b1f8e31e.png)
