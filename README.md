Nama : Rizky Dzaky Hamonangan Manihuruk
NPM : 2506657301
Kelas : PBP C

Deklarasi AI
Saya menggunakan bantuan Gemini sebagai bantu belajar saya dalam memahami materi dan mencari tahu sumber masalah yang sulit terpecahkan. Saya tetap melakukan pengecekan dan testing secara mandiri menggunakan Live Server di VSCode. Beberapa kode dari AI juga saya sesuaikan kembali dengan struktur dan kebutuhan project saya.

# Tugas 2

1. Ketika pengguna membuka `/project/`, request pertama diterima oleh `urls.py` proyek dan diteruskan ke `main/urls.py` melalui `include()`. Selanjutnya, `main/urls.py` mengarahkan URL tersebut ke view `show_project`. View mengambil data dari model `Project` menggunakan `Project.objects.all()`, kemudian memasukkannya ke dalam context dan meneruskannya ke template `project.html`. Template menggunakan Django Template Language untuk menampilkan data project. Hasil HTML kemudian dikirim kembali dan ditampilkan pada browser.

2. Data portofolio sebaiknya disimpan pada model agar tidak perlu ditulis langsung di dalam template. Dengan menyimpan data di database, data dapat ditambah, diubah, atau dihapus tanpa mengubah kode HTML. Hal ini membuat aplikasi lebih mudah dipelihara dan dikembangkan, terutama ketika jumlah data semakin banyak.

 3. `makemigrations` digunakan untuk membuat file migration berdasarkan perubahan pada model, sedangkan `migrate` digunakan untuk menerapkan migration tersebut ke database.

Sebagai contoh, saya menambahkan model `Project` dengan field `title`, `description`, dan `date_completed`. Setelah itu, saya menjalankan `python manage.py makemigrations` untuk membuat migration dan `python manage.py migrate` untuk menerapkannya ke database.


# Deklarasi Penggunaan AI

Dalam pengerjaan Tugas 2, saya menggunakan AI sebagai alat bantu untuk memahami konsep Django, seperti model, view, URL routing, template, dan unit testing. AI juga digunakan untuk membantu menemukan dan memahami error yang muncul selama proses pengerjaan. Implementasi kode disesuaikan dengan struktur project dan diuji secara mandiri menggunakan `python manage.py test` dan `python manage.py runserver`.


Link Gemini : https://share.gemini.google/fXW9sVUmhVeX

