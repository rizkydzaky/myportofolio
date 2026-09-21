Nama : Rizky Dzaky Hamonangan Manihuruk
NPM : 2506657301
Kelas : PBP C

## Tugas 1

1. Ya, saya menggunakan elemen semantik HTML5 seperti `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, dan `<footer>`. Elemen tersebut membantu membuat struktur website lebih rapi, terorganisir, dan mudah dipahami. 

2. Tantangan yang saya temui adalah menyesuaikan layout agar tetap rapi pada ukuran layar yang berbeda, terutama saat dibuka melalui HP. Saya melakukan testing menggunakan Live Server dan responsive mode pada browser, kemudian menyesuaikan ukuran font, gambar, margin, padding, dan layout menggunakan media query. Saya juga belajar memahami kode agar smooth saat scrolling.

3. Karena website ini masih berupa static web, data masih harus diubah secara manual melalui HTML. Interaksinya juga masih terbatas. Jika saya sudah cukup mahir, Saya ingin menggunakan JavaScript untuk menambahkan fitur seperti filtering project, validasi form, dan interaksi yang lebih dinamis. Saya juga ingin mempelajari backend dan database. Agar website saya lebih complex dam lebih menarik.

- Deklarasi AI
Dalam pengerjaan Tugas 1, Saya menggunakan bantuan Gemini sebagai bantu belajar saya dalam memahami materi dan mencari tahu sumber masalah yang sulit terpecahkan. Saya tetap melakukan pengecekan dan testing secara mandiri menggunakan Live Server di VSCode. Beberapa kode dari AI juga saya sesuaikan kembali dengan struktur dan kebutuhan project saya.

Link Gemini : https://share.gemini.google/lltzRsio3jr9


## Tugas 2

1. Ketika pengguna membuka `/project/`, request pertama diterima oleh `urls.py` proyek dan diteruskan ke `main/urls.py` melalui `include()`. Selanjutnya, `main/urls.py` mengarahkan URL tersebut ke view `show_project`. View mengambil data dari model `Project` menggunakan `Project.objects.all()`, kemudian memasukkannya ke dalam context dan meneruskannya ke template `project.html`. Template menggunakan Django Template Language untuk menampilkan data project. Hasil HTML kemudian dikirim kembali dan ditampilkan pada browser.

2. Data portofolio sebaiknya disimpan pada model agar tidak perlu ditulis langsung di dalam template. Dengan menyimpan data di database, data dapat ditambah, diubah, atau dihapus tanpa mengubah kode HTML. Hal ini membuat aplikasi lebih mudah dipelihara dan dikembangkan, terutama ketika jumlah data semakin banyak.

 3. `makemigrations` digunakan untuk membuat file migration berdasarkan perubahan pada model, sedangkan `migrate` digunakan untuk menerapkan migration tersebut ke database.

Sebagai contoh, saya menambahkan model `Project` dengan field `title`, `description`, dan `date_completed`. Setelah itu, saya menjalankan `python manage.py makemigrations` untuk membuat migration dan `python manage.py migrate` untuk menerapkannya ke database.


- Deklarasi Penggunaan AI
Dalam pengerjaan Tugas 2, saya menggunakan AI sebagai alat bantu untuk memahami konsep Django, seperti model, view, URL routing, template, dan unit testing. AI juga digunakan untuk membantu menemukan dan memahami error yang muncul selama proses pengerjaan. Implementasi kode disesuaikan dengan struktur project dan diuji secara mandiri menggunakan `python manage.py test` dan `python manage.py runserver`.

Link Gemini : https://share.gemini.google/t9EW5EJHBjhw


## Tugas 3

1. ModelForm digunakan untuk membuat form berdasarkan model Django sehingga kita tidak perlu membuat setiap input HTML secara manual. ModelForm juga menyediakan validasi data dan dapat menyimpan data yang valid langsung ke database menggunakan form.save().Saya menggunakan ExperienceForm yang dibuat berdasarkan model Experience untuk menambahkan dan mengubah data experience. Selain itu, {% csrf_token %} digunakan untuk melindungi form dari serangan Cross-Site Request Forgery (CSRF). Token tersebut memastikan bahwa request POST yang dikirim berasal dari aplikasi yang sesuai sehingga Django dapat memverifikasi request sebelum memproses perubahan data.

2. JSON lebih sering digunakan dalam pengembangan aplikasi web modern karena memiliki struktur yang lebih sederhana dan ringan dibandingkan XML. JSON menggunakan format key-value dan array sehingga lebih mudah dibaca oleh manusia maupun diproses oleh program. JSON juga memiliki dukungan yang baik pada JavaScript dan banyak digunakan untuk pertukaran data melalui API. Dibandingkan XML yang menggunakan tag pembuka dan penutup, JSON memiliki struktur yang lebih ringkas sehingga lebih praktis digunakan untuk komunikasi antara client dan server.

3. Saat pengguna mengakses endpoint JSON, request diterima oleh urls.py dan diteruskan ke view get_experiences_json. View tersebut mengambil data dari model Experience menggunakan Experience.objects.all(). Data tersebut kemudian diubah menjadi format JSON menggunakan serializers.serialize(). Setelah proses serialization selesai, data dikembalikan menggunakan HttpResponse dengan content_type="application/json". Serialization diperlukan karena object Django yang diperoleh dari database tidak dapat langsung dikirim dalam format JSON. Proses serialization mengubah object Django beserta field-nya menjadi data yang dapat direpresentasikan dalam JSON dan dikirim melalui HTTP. Pada project ini, data JSON tersebut kemudian digunakan kembali pada show_experience melalui proses deserialization agar dapat ditampilkan pada halaman experience.html.

- Deklarasi Penggunaan AI
Dalam pengerjaan Tugas 3, saya menggunakan AI sebagai alat bantu untuk memahami konsep Django, seperti ModelForm, CSRF token, CRUD, JSON, serialization, dan deserialization. AI juga digunakan untuk membantu menemukan dan memahami error yang muncul selama proses pengerjaan. Implementasi kode disesuaikan dengan struktur project dan diuji secara mandiri menggunakan python manage.py runserver serta pengujian langsung pada halaman web dan endpoint JSON.