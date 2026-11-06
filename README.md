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


Link Gemini : https://share.gemini.google/vmjU27125cc4

## Tugas 4
*hanya deklarasi AI

- Deklarasi Penggunaan AI

Dalam pengerjaan Tugas 4, saya menggunakan AI sebagai alat bantu untuk memahami dan mengimplementasikan konsep Django, seperti authentication, authorization, Group dan role pengguna, server-side permission checking, serta fitur star/unstar menggunakan ManyToManyField. Saya cukup kesulitan untuk menentukan fitur star/unstar sesuai ketentuan. AI juga digunakan untuk membantu menemukan dan memahami error yang muncul selama proses pengerjaan, serta memberikan arahan dalam menyesuaikan fitur berdasarkan kebutuhan tugas. Saya juga belajar memahai apa itu hak akses guest, user biasa, editor dan Superuser.  Penggunaan AI inilah yang membantu saya untuk mengerjakan tugas 4 PBP ini


Link Gemini : https://share.gemini.google/3dlh7sBhTJDP



## Tugas 5
1. Debouncing adalah teknik untuk menunda eksekusi suatu fungsi sampai pengguna berhenti melakukan suatu aktivitas selama waktu tertentu. Pada fitur pencarian AJAX, debouncing digunakan agar request ke server tidak dikirim setiap kali pengguna mengetik satu karakter.

Contohnya, ketika pengguna mengetik `Experience`, tanpa debouncing bisa terjadi banyak request AJAX untuk setiap perubahan karakter. Dengan debouncing, request hanya dikirim setelah pengguna berhenti mengetik selama beberapa saat. Hal ini dapat mengurangi jumlah request ke server, meningkatkan efisiensi, dan membuat fitur pencarian lebih responsif.

2. `fetch()` merupakan operasi asynchronous yang membutuhkan waktu untuk mendapatkan response dari server. Penggunaan `await` membuat JavaScript menunggu hingga proses tersebut selesai sebelum melanjutkan ke baris kode berikutnya.

Dengan `await`, kita dapat langsung memperoleh response dari `fetch()` dan kemudian memprosesnya, misalnya dengan menggunakan `await response.json()` untuk mendapatkan data JSON.

Jika tidak menggunakan `await`, `fetch()` akan mengembalikan sebuah `Promise`, bukan response yang sudah selesai. Akibatnya, kode yang membutuhkan hasil response dapat dijalankan sebelum data dari server tersedia sehingga dapat menyebabkan error atau hasil yang tidak sesuai.

3. XSS (*Cross-Site Scripting*) adalah serangan ketika penyerang memasukkan kode atau script berbahaya ke dalam data yang kemudian ditampilkan dan dijalankan oleh browser pengguna.

Data yang ditampilkan melalui AJAX/JavaScript lebih rentan jika developer memasukkan data langsung ke dalam HTML tanpa melakukan escaping. Berbeda dengan data yang dirender melalui template Django, Django secara default melakukan HTML escaping terhadap nilai yang ditampilkan menggunakan template sehingga karakter HTML tertentu tidak langsung dianggap sebagai kode HTML.

Pada implementasi AJAX, data JSON diterima oleh JavaScript dan kemudian dapat dimasukkan ke halaman menggunakan `innerHTML`. Jika data tersebut tidak di-*escape*, input berbahaya dapat dianggap sebagai HTML dan berpotensi menjalankan script. Oleh karena itu, pada implementasi ini digunakan fungsi `escapeHtml()` sebelum memasukkan data ke HTML, serta `strip_tags()` pada `ModelForm` untuk membersihkan input dari tag HTML.


- Deklarasi Penggunaan AI

Dalam pengerjaan Tugas 5, saya menggunakan AI sebagai alat bantu untuk memahami dan mengimplementasikan AJAX, fetch(), JsonResponse, debouncing, modal, dan toast pada halaman Experience. AI juga membantu saya dalam memahami dan mengatasi error selama proses pengerjaan, terutama pada fitur pencarian, penambahan data, permission, dan pencegahan XSS. Penggunaan AI membantu saya memahami konsep sekaligus menyelesaikan Tugas 5 PBP ini.


Link Gemini : https://share.gemini.google/KhhDN0p2wz1p


## Tugas 6
1. REST (Representational State Transfer) adalah sebuah gaya arsitektur dalam pengembangan API yang mengatur bagaimana client dan server berkomunikasi melalui HTTP. REST menggunakan resource sebagai objek yang diakses melalui URL dan memanfaatkan HTTP method seperti GET, POST, PUT, PATCH, dan DELETE untuk melakukan operasi terhadap resource tersebut. Mengembalikan JSON saja belum cukup untuk menyebut sebuah API sebagai RESTful karena REST tidak hanya berkaitan dengan format data, tetapi juga memiliki prinsip arsitektur seperti penggunaan resource, pemisahan client dan server, stateless communication, serta penggunaan HTTP method dan status code sesuai fungsinya.

Perbedaan PUT dan PATCH yaitu pada cara keduanya memperbarui data. PUT digunakan untuk mengganti keseluruhan representasi suatu resource, sedangkan PATCH digunakan untuk memperbarui sebagian field saja. Contohnya, ketika ingin mengganti seluruh informasi Experience seperti judul, deskripsi, dan kategori, kita dapat menggunakan PUT. Namun, ketika hanya ingin mengubah deskripsi Experience tanpa mengubah field lainnya, kita dapat menggunakan PATCH.

2. Serializer pada Django REST Framework berfungsi untuk mengubah objek model Django menjadi data yang dapat dikirimkan melalui API, seperti JSON. Serializer juga dapat melakukan proses deserialisasi, yaitu mengubah data yang diterima dari client menjadi bentuk yang dapat digunakan untuk membuat atau memperbarui objek model. Selain itu, serializer menyediakan validasi data sebelum data disimpan ke database.

Dibandingkan merakit dictionary secara manual menggunakan JsonResponse seperti pada Tutorial 05, penggunaan serializer lebih praktis dan terstruktur. Serializer dapat mengelola proses konversi data, validasi field, penentuan field yang hanya dapat dibaca (read-only), serta penanganan data yang tidak valid. Dengan demikian, kode menjadi lebih konsisten, mudah dikelola, dan mengurangi kebutuhan untuk menulis proses validasi secara manual.

3. Autentikasi adalah proses untuk memverifikasi identitas pengguna yang melakukan permintaan ke API, misalnya melalui session atau token. Sementara itu, otorisasi adalah proses menentukan apakah pengguna yang sudah teridentifikasi memiliki izin untuk melakukan tindakan tertentu terhadap suatu resource.

Pada Django REST Framework, autentikasi dapat dilakukan menggunakan SessionAuthentication, sedangkan otorisasi dapat diatur menggunakan permission class. Permission class digunakan untuk memeriksa hak akses pengguna di sisi server sebelum suatu operasi dijalankan. Pemeriksaan hak akses tidak cukup hanya dengan menyembunyikan tombol pada template karena pengguna masih dapat mengirimkan HTTP request secara langsung melalui browser atau tools lainnya. Oleh karena itu, pemeriksaan permission harus tetap dilakukan di server agar data terlindungi dan setiap operasi hanya dapat dilakukan oleh pengguna yang memiliki izin.

4. API menggunakan SessionAuthentication, permintaan yang mengubah data seperti POST, PUT, PATCH, dan DELETE tetap memerlukan token CSRF. Hal ini karena autentikasi session menggunakan cookie yang secara otomatis dikirimkan oleh browser ketika pengguna mengakses suatu website. Kondisi tersebut dapat dimanfaatkan dalam serangan Cross-Site Request Forgery (CSRF), yaitu ketika pengguna yang sedang login tanpa sadar diarahkan untuk mengirimkan permintaan yang tidak diinginkan ke server.

Token CSRF digunakan untuk memastikan bahwa permintaan yang mengubah data berasal dari sumber yang memiliki token valid, sehingga membantu mencegah permintaan palsu dari situs lain. Dalam Django REST Framework, SessionAuthentication melakukan pemeriksaan CSRF terhadap permintaan yang membutuhkan perlindungan tersebut.

Pengujian menggunakan force_authenticate saja tidak cukup untuk membuktikan bahwa perlindungan CSRF berjalan karena metode tersebut melewati proses autentikasi normal yang digunakan oleh aplikasi. Akibatnya, pengujian tersebut tidak membuktikan bahwa mekanisme CSRF benar-benar diterapkan. Untuk menguji perlindungan CSRF, kita dapat menggunakan APIClient dengan enforce_csrf_checks=True, kemudian melakukan login menggunakan .login() dan mengirimkan permintaan tanpa token CSRF. Dengan cara ini, kita dapat memastikan bahwa server menolak permintaan yang tidak menyertakan token CSRF yang valid.


Link Gemini : https://share.gemini.google/9uXP1rIl5tSU