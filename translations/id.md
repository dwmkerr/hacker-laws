# 💻📖 Undang Undang Peretas

[![gitlocalized](https://gitlocalize.com/repo/2513/whole_project/badge.svg)](https://gitlocalize.com/repo/2513/whole_project?utm_source=badge)

Hukum, Teori, Prinsip dan Pola yang berguna bagi pengembang (developer).

[terjemahan](#translations):  [🇧🇷](./translations/pt-BR.md) [🇨🇳](https://github.com/nusr/hacker-laws-zh) [🇫🇷](./translations/fr.md) [🇮🇹](./translations/it-IT.md) [🇱🇻](./translations/lv.md) [🇰🇷](https://github.com/codeanddonuts/hacker-laws-kr) [🇷🇺](https://github.com/solarrust/hacker-laws) [🇪🇸](./translations/es-ES.md) [🇹🇷](./translations/tr.md) [🇯🇵](./translations/jp.md) [🇵🇱](./translations/pl.md) [🇻🇳](./translations/vi.md)

Suka dengan project ini? Silahkan Mempertimbangkan untuk [Mensponsori saya](https://github.com/sponsors/dwmkerr)!

---

<!-- vim-markdown-toc GFM -->

* [Pendahuluan](#pendahuluan)
* [Undang Undang](#undang-undang)
    * [Hukum Amdahl](#hukum-amdahl)
    * [Teori Windows Rusak](#teori-windows-rusak)
    * [Hukum Brooks](#hukum-brook)
    * [Hukum Conway](#hukum-conway)
    * [Hukum Cunningham](#hukum-cunningham)
    * [Nomor Dunbar](#nomor-dunbar)
    * [Hukum Gall](#hukum-gall)
    * [Hukum Goodhart](#hukum-goodhart)
    * [Pisau Cukur Hanlon](#pisau-cukur-hanlon)
    * [Hukum Hofstadter](#hukum-hofstadter)
    * [Hukum Hutber](#hukum-hutber)
    * [Siklus Hype & Hukum Amara](#sirklus-hype-dan-hukum-amara)
    * [Hukum Hyrum (Hukum Antarmuka Implisit)](#hukum-hyrum-hukum-antarmuka-implisit)
    * [Hukum Kernighan](#hukum-kernighan)
    * [Hukum Metcalfe](#hukum-metcalfe)
    * [Hukum Moore](#hukum-moore)
    * [Hukum Murphy / Hukum Sod](#hukum-murphy)
    * [Pisau Cukur Occam](#pisau-cukup-occam)
    * [Hukum Parkinson](#hukum-parkinson)
    * [Efek Optimalisasi Prematur](#efek-optimasi-prematur)
    * [Hukum Putt](#hukum-putt)
    * [Hukum Reed](#hukum-reed)
    * [Hukum Konservasi Kompleksitas (Hukum Tesler)](#hukum-konservasi-kompleksitas-hukum-tesler)
    * [Hukum Abstraksi Kebocoran](#hukum-abstraksi-kebocoran)
    * [Hukum Triviality](#hukum-triviality)
    * [Filsafat Unix](#filsafat-unix)
    * [Model Spotify](#model-spotify)
    * [Hukum Wadler](#hukum-wadler)
    * [Hukum Wheaton](#hukum-gandum)
* [Prinsip](#prinsip)
    * [Prinsip Dilbert](#prinsip-dilbert)
    * [Prinsip Pareto (Aturan 80/20)](#prinsip-pareto-aturan-8020)
    * [Prinsip Peter](#prinsip-peter)
    * [Prinsip Robustness (Hukum Postel)](#prinsip-robustness-princihukumple-postel)
    * [SOLID](#solid)
    * [Prinsip Tanggung Jawab Tunggal](#prinsip-tanggung-jawab-tunggal)
    * [Prinsip Terbuka / Tertutup](#prinsip-terbukatertutup)
    * [Prinsip Substitusi Liskov](#prinsip-substitusi-liskov)
    * [Prinsip Segregasi Antarmuka](#prinsip-segregasi-antarmuka)
    * [Prinsip Ketergantungan Inversi](#prinsip-ketergantungan-inversi)
    * [Prinsip KERING](#prinsip-kering)
    * [Prinsip KISS](#prinsip-kiss)
    * [YAGNI](#yagni)
    * [Kekeliuran Komputasi Terdistribusi](#kekeliuran-komputasi-terdistribusi)
* [Daftar Bacaan](#daftar-bacaan)
* [Berkontribusi](#berkontribusi)
* [TODO](#todo)

<!-- vim-markdown-toc -->

## Pendahuluan

Ada banyak undang-undang yang dibahas orang ketika berbicara tentang pembangunan. Repositori ini adalah referensi dan gambaran umum dari beberapa yang paling umum. Silakan bagikan dan kirimkan PR!

❗: Repo ini berisi penjelasan tentang beberapa undang-undang, prinsip, dan pola, tetapi tidak _advokasi_ untuk salah satu dari mereka. Apakah mereka harus diterapkan akan selalu menjadi masalah perdebatan, dan sangat tergantung pada apa yang sedang Anda kerjakan.

## Undang-undang

Dan ini dia!

### Hukum Amdahl

[Hukum Amdahl di Wikipedia](https://en.wikipedia.org/wiki/Amdahl%27s_law)

> Hukum Amdahl adalah formula yang menunjukkan _kecepatan potensial_ dari tugas komputasi yang dapat dicapai dengan meningkatkan sumber daya suatu sistem. Biasanya digunakan dalam komputasi paralel, ia dapat memprediksi manfaat secara aktual dari peningkatan jumlah prosesor, yang dibatasi oleh kemampuan program yang paralel.

Ilustrasikan terbaik dengan sebuah contoh. Jika suatu program terdiri dari dua bagian, bagian A, yang harus dijalankan oleh satu prosesor, dan bagian B, yang dapat diparalelkan, maka jika kita melihat ketika menambahkan beberapa prosesor ke sistem yang menjalankan program maka hanya dapat memiliki manfaat yang terbatas. Ini berpotensi dapat sangat meningkatkan kecepatan bagian B - tetapi kecepatan bagian A akan tetap tidak berubah.

Diagram di bawah ini menunjukkan beberapa contoh peningkatan kecepatan potensial:

<img width="480px" alt="Diagram: Amdahl's Law" src="./../images/amdahls_law.png" />

*(Gambar referensi: Oleh Daniels220 di Wikipedia Bahasa Inggris, Creative Commons Attribution-Share Alike 3.0 Unported, https://en.wikipedia.org/wiki/File:AmdahlsLaw.svg)*

Seperti dapat dilihat, bahkan sebuah program yang parallelisable 50% akan mendapat manfaat sangat sedikit di luar 10 unit pemrosesan, sedangkan program yang 95% parallelisable masih dapat mencapai peningkatan kecepatan yang signifikan dengan lebih dari seribu unit pemrosesan.

Karena [Hukum Moore](#hukum-moore) melambat, dan akselerasi kecepatan prosesor individu melambat, parallelisation adalah kunci untuk meningkatkan kinerja. Pemrograman grafik adalah contoh yang sangat baik - dengan komputasi berbasis Shader modern, piksel atau fragmen individual dapat diterjemahkan secara paralel - inilah sebabnya modern graphics cards sering memiliki ribuan inti pemrosesan (GPU atau Unit Shader).

Lihat juga:

- [Hukum Brook](#hukum-brook)
- [Hukum Moore](#hukum-moore)

### Teori Windows Rusak

[Teori Windows Rusak di Wikipedia](https://en.wikipedia.org/wiki/Broken_windows_theory)

Teori Windows Rusak menunjukkan bahwa tanda-tanda kejahatan yang nyata (atau kurangnya kepedulian terhadap suatu lingkungan) mengarah pada kejahatan yang semakin serius (atau semakin memburuknya lingkungan).

Teori ini telah diterapkan pada pengembangan perangkat lunak, menunjukkan bahwa kode kualitas yang buruk (atau [Utang Teknis](#TODO)) dapat mengarah pada persepsi bahwa upaya untuk meningkatkan kualitas dapat diabaikan atau diremehkan, sehingga mengarah pada kode kualitas yang lebih buruk lagi. Efek ini mengalir ke penurunan kualitas yang besar dari waktu ke waktu.

Lihat juga:

- [Hutang Teknis](#TODO)

Contoh:

- [The Pragmatic Programming: Software Entropy](https://pragprog.com/the-pragmatic-programmer/extracts/software-entropy)
- [Coding Horror: The Broken Window Theory](https://blog.codinghorror.com/the-broken-window-theory/)
- [OpenSource: Joy of Programming - The Broken Window Theory](https://opensourceforu.com/2011/05/joy-of-programming-broken-window-theory/)

### Hukum Brooks

[Hukum Brooks di Wikipedia](https://en.wikipedia.org/wiki/Brooks%27s_law)

> Menambahkan sumber daya manusia ke proyek pengembangan perangkat lunak yang terlambat membuatnya nanti.

Undang-undang ini menunjukkan bahwa dalam banyak kasus, upaya untuk mempercepat pengiriman proyek yang sudah terlambat, dengan menambah lebih banyak orang, akan membuat pengiriman lebih lambat. Brooks jelas bahwa ini adalah penyederhanaan yang berlebihan, namun, alasan umum adalah bahwa mengingat peningkatan waktu sumber daya baru dan overhead komunikasi, dalam jangka pendek langsung kecepatan berkurang. Selain itu, banyak tugas yang mungkin tidak dapat dibagi, yaitu mudah didistribusikan di antara lebih banyak sumber daya, yang berarti peningkatan kecepatan potensial juga lebih rendah.

Ungkapan umum dalam persalinan "Sembilan wanita tidak bisa menghasilkan bayi dalam satu bulan" berhubungan dengan Hukum Brooks, khususnya, fakta bahwa beberapa jenis pekerjaan tidak dapat dibagi atau diparalelkan.

Ini adalah tema sentral dari buku '[The Mythical Man Month](#daftar-bacaan)'.

Lihat juga:

- [Death March](#todo)
- [Daftar Bacaan: The Mythical Man Month](#daftar-bacaan)

### Hukum Brooks

[Hukum Brooks di Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_law)

Undang-undang ini menyatakan bahwa batasan teknis suatu sistem akan mencerminkan struktur organisasi. Ini biasa disebut ketika melihat perbaikan organisasi, Hukum Brooks menyarankan bahwa jika organisasi terstruktur menjadi banyak unit kecil, terputus, perangkat lunak yang dihasilkannya akan. Jika suatu organisasi dibangun lebih di sekitar 'vertikal' yang berorientasi pada fitur atau layanan, sistem perangkat lunak juga akan mencerminkan hal ini.

Lihat juga:

- [Model Spotify](#model-spotify)

### Hukum Cunningham

[Hukum Cunningham di Wikipedia](https://en.wikipedia.org/wiki/Ward_Cunningham#Cunningham's_Law)

> Cara terbaik untuk mendapatkan jawaban yang benar di Internet adalah tidak dengan mengajukan pertanyaan, itu untuk mengirim jawaban yang salah.

Menurut Steven McGeady, Ward Cunningham menasihatinya pada awal 1980-an: "Cara terbaik untuk mendapatkan jawaban yang benar di Internet adalah tidak mengajukan pertanyaan, itu untuk mengirim jawaban yang salah." McGeady menjuluki Hukum Cunningham ini, meskipun Cunningham menyangkal kepemilikan menyebutnya "salah kutip." Meskipun awalnya merujuk pada interaksi di Usenet, undang-undang tersebut telah digunakan untuk menggambarkan cara kerja komunitas online lainnya (mis., Wikipedia, Reddit, Twitter, Facebook).

Lihat juga:

- [XKCD 386: "Duty Calls"](https://xkcd.com/386/)

### Nomor Dunbar

[Nomor Dunbar di Wikipedia](https://en.wikipedia.org/wiki/Dunbar%27s_number)

"Nomor Dunbar adalah batasan kognitif yang disarankan untuk jumlah orang yang dengannya seseorang dapat mempertahankan hubungan sosial yang stabil — hubungan di mana seorang individu mengetahui siapa setiap orang dan bagaimana setiap orang berhubungan dengan setiap orang lainnya." Ada beberapa perbedaan pendapat tentang jumlah pastinya. "... [Dunbar] mengusulkan agar manusia dapat dengan nyaman mempertahankan hanya 150 hubungan yang stabil." Dia memasukkan nomor itu ke dalam konteks yang lebih sosial, "jumlah orang yang Anda tidak akan merasa malu untuk bergabung tanpa diundang untuk minum jika Anda kebetulan menabrak mereka di sebuah bar." Perkiraan angka umumnya berkisar antara 100 dan 250.

Seperti hubungan stabil antara individu, hubungan pengembang dengan basis kode membutuhkan upaya untuk mempertahankan. Ketika dihadapkan dengan proyek-proyek besar yang rumit, atau kepemilikan banyak proyek, kami bersandar pada konvensi, kebijakan, dan model prosedur untuk menskalakan. Nomor Dunbar tidak hanya penting untuk diingat ketika kantor tumbuh, tetapi juga ketika menetapkan ruang lingkup untuk upaya tim atau memutuskan kapan suatu sistem harus berinvestasi dalam perkakas untuk membantu dalam pemodelan dan mengotomatisasi overhead logistik. Menempatkan nomor ke dalam konteks teknik, itu adalah jumlah proyek (atau kompleksitas dinormalisasi dari satu proyek) di mana Anda akan merasa yakin untuk bergabung dengan rotasi on-call untuk mendukung.

Lihat juga:

- [Hukum Conway](#Hukum-conway)

### Hukum Gall

[Hukum Gall di Wikipedia](https://en.wikipedia.org/wiki/John_Gall_(author)#Gall's_law)

> Sebuah sistem kompleks yang berfungsi selalu ditemukan telah berevolusi dari sistem sederhana yang berfungsi. Sistem kompleks yang dirancang dari awal tidak pernah berfungsi dan tidak dapat ditambal untuk membuatnya berfungsi. Anda harus memulai dari awal dengan sistem sederhana yang berfungsi.
>
> ([John Gall](https://en.wikipedia.org/wiki/John_Gall_(author)))

Hukum Gall menyiratkan bahwa upaya untuk _design_ sistem yang sangat kompleks cenderung gagal. Sistem yang sangat kompleks jarang dibangun dalam sekali jalan, tetapi malah berkembang dari sistem yang lebih sederhana.

Contoh klasik adalah world-wide-web. Dalam kondisi saat ini, ini adalah sistem yang sangat kompleks. Namun, itu didefinisikan pada awalnya sebagai cara sederhana untuk berbagi konten antar institusi akademik. Itu sangat sukses dalam mencapai tujuan-tujuan ini dan berkembang menjadi lebih kompleks dari waktu ke waktu.

Lihat juga:

- [KISS (Keep It Simple, Stupid)](#prinsip-kiss)

### Hukum Goodhart

[Hukum Goodhart di Wikipedia](https://en.wikipedia.org/wiki/Goodhart's_law)

> Setiap keteraturan statistik yang diamati akan cenderung runtuh begitu tekanan diberikan untuk tujuan kontrol.
>
> _Charles Goodhart_

Juga biasa dirujuk sebagai:

> Ketika suatu ukuran menjadi target, itu tidak lagi menjadi ukuran yang baik.
>
> _Marilyn Strathern_

Undang-undang menyatakan bahwa optimasi yang digerakkan oleh tindakan dapat mengarah pada devaluasi hasil pengukuran itu sendiri. Seperangkat tindakan yang terlalu selektif ([KPI](https://en.wikipedia.org/wiki/Performance_indicator)) yang diterapkan secara membuta pada suatu proses menghasilkan efek yang terdistorsi. Orang-orang cenderung untuk mengoptimalkan secara lokal dengan "bermain-main" sistem untuk memenuhi metrik tertentu daripada memperhatikan hasil holistik dari tindakan mereka.

Contoh dunia nyata:
- Tes bebas-konfirmasi memenuhi ekspektasi cakupan kode, meskipun faktanya maksud metrik adalah untuk menciptakan perangkat lunak yang teruji dengan baik.
- Skor kinerja pengembang ditunjukkan oleh jumlah baris yang dilakukan mengarah pada basis kode yang terlalu besar yang tidak dapat dibenarkan.

Lihat juga:

- [Hukum Goodhart: Bagaimana Mengukur Hal-Hal yang Salah Mendorong Perilaku Tidak bermoral](https://coffeeandjunk.com/goodharts-campbells-law/)
- [Dilbert pada perangkat lunak bebas bug](https://dilbert.com/strip/1995-11-13)

### Pisau Cukur Hanlon

[Pisau Cukur Hanlon di Wikipedia](https://en.wikipedia.org/wiki/Hanlon%27s_razor)

> Jangan mengaitkan dengan kedengkian yang dijelaskan dengan cukup oleh kebodohan.
>
> Robert J. Hanlon

Prinsip ini menunjukkan bahwa tindakan yang menghasilkan hasil negatif bukanlah hasil dari niat buruk. Sebaliknya hasil negatif lebih cenderung dikaitkan dengan tindakan-tindakan dan / atau dampak yang tidak sepenuhnya dipahami.

### Hukum Hofstadter

[Hukum Hofstadter di Wikipedia](https://en.wikipedia.org/wiki/Hofstadter%27s_law)

> Itu selalu memakan waktu lebih lama dari yang Anda harapkan, bahkan ketika Anda memperhitungkan Hukum Hofstadter.
>
> (Douglas Hofstadter)

Anda mungkin mendengar undang-undang ini disebut ketika melihat perkiraan berapa lama sesuatu akan terjadi. Tampaknya disangkal dalam pengembangan perangkat lunak yang kita cenderung tidak pandai memperkirakan secara akurat berapa lama waktu yang diperlukan untuk menghasilkan.

Ini dari buku '[Gödel, Escher, Bach: An Eternal Golden Braid](#daftar-bacaan)'.

Lihat juga:

- [Daftar Bacaan: Gödel, Escher, Bach: An Eternal Golden Braid](#daftar-bacaan)

### Hukum Hutber

[Hukum Hutber di Wikipedia](https://en.wikipedia.org/wiki/Hutber%27s_law)

> Perbaikan berarti kemunduran.
>
> ([Patrick Hutber](https://en.wikipedia.org/wiki/Patrick_Hutber))

Undang-undang ini menunjukkan bahwa perbaikan pada suatu sistem akan menyebabkan kerusakan pada bagian lain, atau akan menyembunyikan kemunduran lainnya, yang secara keseluruhan mengarah pada degradasi dari kondisi sistem saat ini.

Sebagai contoh, penurunan latensi respons untuk titik akhir tertentu dapat menyebabkan peningkatan throughput dan masalah kapasitas lebih lanjut dalam aliran permintaan, yang mempengaruhi sub-sistem yang sama sekali berbeda.

### Siklus Hype & Hukum Amara

[Siklus Hype di Wikipedia](https://en.wikipedia.org/wiki/Hype_cycle)

> Kita cenderung melebih-lebihkan efek teknologi dalam jangka pendek dan meremehkan efek dalam jangka panjang.
>
> (Roy Amara)

Hype Siklus adalah representasi visual dari kegembiraan dan pengembangan teknologi dari waktu ke waktu, awalnya diproduksi oleh Gartner. Paling baik ditunjukkan dengan visual:

![Siklus Hype](./../images/gartner_hype_cycle.png)

*(Referensi Gambar: Oleh Jeremykemp di bahasa inggris Wikipedia, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=10547051)*

Singkatnya, siklus ini menunjukkan bahwa biasanya ada ledakan kegembiraan di sekitar teknologi baru dan dampak potensialnya. Tim sering melompat ke teknologi ini dengan cepat, dan kadang-kadang merasa kecewa dengan hasilnya. Ini mungkin karena teknologinya belum cukup matang, atau aplikasi dunia nyata belum sepenuhnya terwujud. Setelah waktu tertentu, kemampuan teknologi meningkat dan peluang praktis untuk menggunakannya meningkat, dan tim akhirnya menjadi produktif. Kutipan Roy Amara meringkas ini dengan paling ringkas - "Kita cenderung melebih-lebihkan efek teknologi dalam jangka pendek dan meremehkan dalam jangka panjang".

### Hukum Hyrum (Hukum Antarmuka Implisit)

[Hukum Hyrum](http://www.hyrumslaw.com/)

> Dengan jumlah pengguna API yang memadai,
> tidak masalah apa yang Anda janjikan dalam kontrak:
> semua perilaku yang dapat diamati dari sistem Anda
> akan bergantung pada seseorang.
>
> (Hyrum Wright)

Hukum Hyrum menyatakan bahwa ketika Anda memiliki jumlah konsumen yang cukup besar dari suatu API, semua perilaku API (bahkan mereka yang tidak didefinisikan sebagai bagian dari kontrak publik) pada akhirnya akan tergantung pada seseorang. Contoh sepele mungkin elemen non-fungsional seperti waktu respons API. Contoh yang lebih halus mungkin konsumen yang mengandalkan menerapkan regex ke pesan kesalahan untuk menentukan * jenis * kesalahan API. Sekalipun kontrak publik API tidak menyatakan apa-apa tentang isi pesan, mengindikasikan bahwa pengguna harus menggunakan kode kesalahan yang terkait, _beberapa_ pengguna  dapat menggunakan pesan tersebut, dan mengubah pesan pada dasarnya merusak API untuk para pengguna tersebut.

Lihat juga:

- [Hukum Abstraksi Kebocoran](#hukum-abstraksi-kebocoran)
- [XKCD 1172](https://xkcd.com/1172/)

### Hukum Kernighan

> Debugging dua kali lebih sulit daripada menulis kode di tempat pertama. Karena itu, jika Anda menulis kode sepintar mungkin, Anda, menurut definisi, tidak cukup pintar untuk debug itu.
>
> (Brian Kernighan)

Hukum Kernighan adalah nama untuk [Brian Kernighan](https://en.wikipedia.org/wiki/Brian_Kernighan) dan berasal dari kutipan dari buku Kernighan dan Plauger [The Elements of Programming Style](https://en.wikipedia.org/wiki/The_Elements_of_Programming_Style):

> Semua orang tahu bahwa debugging dua kali lebih sulit daripada menulis sebuah program. Jadi, jika Anda sepintar ketika Anda menulisnya, bagaimana Anda akan men-debug-nya?

Sementara hiperbolik, Hukum Kernighan berpendapat bahwa kode sederhana lebih disukai daripada kode kompleks, karena men-debug setiap masalah yang muncul dalam kode kompleks mungkin mahal atau bahkan tidak layak.

Lihat juga:

- [Prinsip KISS](#prinsip-kiss)
- [Filsafat Unix](#filsafat-unix)
- [Pisau Cukur Occam](#pisau-cukup-occam)

### Hukum Metcalfe

[Hukum Metcalfe di Wikipedia](https://en.wikipedia.org/wiki/Metcalfe's_law)

> Dalam teori jaringan, nilai suatu sistem tumbuh sekitar kuadrat dari jumlah pengguna sistem.

Undang-undang ini didasarkan pada jumlah kemungkinan koneksi berpasangan dalam suatu sistem dan terkait erat dengan [Hukum Reed](#hukum-reed). Odlyzko dan yang lainnya berpendapat bahwa Hukum Reed dan Hukum Metcalfe melebih-lebihkan nilai sistem dengan tidak memperhitungkan batas-batas kognisi manusia pada efek jaringan; lihat [Nomor Dunbar](#nomor-dunbar).

Lihat juga:

- [Hukum Reed](#hukum-reed)
- [Nomor Dunbar](#nomor-dunbar)

### Hukum Moore

[Hukum Moore di Wikipedia](https://en.wikipedia.org/wiki/Moore%27s_law)

> Jumlah transistor dalam sirkuit terintegrasi bertambah dua kali lipat setiap dua tahun.

Sering digunakan untuk menggambarkan kecepatan di mana semikonduktor dan teknologi chip telah meningkat, prediksi Moore telah terbukti sangat akurat dari tahun 1970-an hingga akhir 2000-an. Dalam beberapa tahun terakhir, tren telah berubah sedikit, sebagian karena [keterbatasan fisik pada sejauh mana komponen dapat miniatur](https://en.wikipedia.org/wiki/Quantum_tunnelling). Namun, kemajuan dalam parallelisation, dan perubahan revolusioner yang berpotensi dalam teknologi semikonduktor dan komputasi kuantum dapat berarti bahwa Hukum Moore dapat terus berlaku selama beberapa dekade mendatang.

### Hukum Murphy / Hukum Sod

[Hukum Murphy di Wikipedia](https://en.wikipedia.org/wiki/Murphy%27s_law)

> Apa pun yang bisa salah akan salah.

Terkait dengan [Edward A. Murphy, Jr](https://en.wikipedia.org/wiki/Edward_A._Murphy_Jr.) _Hukum Murphy_ menyatakan bahwa jika ada sesuatu yang salah, itu akan salah.

Ini adalah pepatah umum di kalangan pengembang. Terkadang hal tak terduga terjadi ketika mengembangkan, menguji, atau bahkan dalam produksi. Ini juga dapat dikaitkan dengan (lebih umum dalam bahasa Inggris Inggris) _Hukum Sod_:

> Jika ada yang salah, itu akan terjadi, pada saat yang paling buruk.

'Hukum' ini umumnya digunakan dalam bentuk komik. Namun, fenomena seperti [_Pastikan Konfirmasi_](#TODO) dan [_Seleksi Pemilu_](#TODO) dapat membuat orang mungkin terlalu menekankan hukum-hukum ini (sebagian besar waktu ketika sesuatu bekerja, mereka tidak diperhatikan, kegagalan namun lebih terlihat. dan menarik lebih banyak diskusi).

Lihat juga:

- [Confirmation Bias](#TODO)
- [Selection Bias](#TODO)

### Pisau Cukur Occam

[Pisau Cukur Occam di Wikipedia](https://en.wikipedia.org/wiki/Occam's_razor)

> Entitas tidak boleh dikalikan tanpa keharusan.
>
> William dari Ockham

Pisau Cukur Occam mengatakan bahwa di antara beberapa solusi yang mungkin, solusi yang paling mungkin adalah solusi dengan jumlah konsep dan asumsi paling sedikit. Solusi ini adalah yang paling sederhana dan hanya menyelesaikan masalah yang diberikan, tanpa memperkenalkan kompleksitas yang tidak disengaja dan kemungkinan konsekuensi negatif.

Lihat juga:

- [YAGNI](#yagni)
- [No Silver Bullet: Kompleksitas Terkadang dan Kompleksitas Esensial](https://en.wikipedia.org/wiki/No_Silver_Bullet)

Contoh:

- [Pengembangan Perangkat Lunak Lean: Menghilangkan Limbah](https://en.wikipedia.org/wiki/Lean_software_development#Eliminate_waste)

### Hukum Parkinson

[Hukum Parkinson di Wikipedia](https://en.wikipedia.org/wiki/Parkinson%27s_law)

> Pekerjaan mengembang untuk mengisi waktu yang tersedia untuk penyelesaiannya.

Dalam konteks aslinya, UU ini didasarkan pada studi tentang birokrasi. Ini mungkin secara pesimis diterapkan pada inisiatif pengembangan perangkat lunak, teorinya adalah bahwa tim akan tidak efisien sampai tenggat waktu dekat, kemudian bergegas untuk menyelesaikan pekerjaan dengan tenggat waktu, sehingga membuat tenggat waktu yang sebenarnya agak sewenang-wenang.

Jika hukum ini digabungkan dengan [Hukum Hofstadter](#hukum-hofstadter), sudut pandang yang lebih pesimistis tercapai - pekerjaan akan meluas untuk mengisi waktu yang tersedia untuk penyelesaiannya dan * masih lebih lama dari yang diharapkan *.

Lihat juga:

- [Hukum Hofstadter](#hukum-hofstadter)

### Efek Optimalisasi Prematur

[Optimalisasi Prematur di WikiWikiWeb](http://wiki.c2.com/?PrematureOptimization)

> Optimalisasi Prematur adalah akar dari semua kejahatan.
>
> [(Donald Knuth)] (https://twitter.com/realdonaldknuth?lang=en)

Dalam makalah Donald Knuth [Pemrograman Terstruktur Dengan Pergi Ke Pernyataan](http://wiki.c2.com/?StructuredProgrammingWithGoToStatements), ia menulis: "Pemrogram menghabiskan banyak waktu memikirkan, atau mengkhawatirkan, kecepatan bagian nonkritis dari program mereka, dan upaya efisiensi ini sebenarnya memiliki dampak negatif yang kuat ketika debugging dan pemeliharaan dipertimbangkan. Kita harus melupakan efisiensi kecil, katakanlah sekitar 97% dari waktu: **Optimalisasi Prematur adalah akar dari semua kejahatan**. Namun kita seharusnya tidak melewatkan peluang kita dalam 3% kritis itu. "

Namun, _Optimalisasi Prematur_ dapat didefinisikan (dalam istilah yang lebih sedikit dimuat) sebagai mengoptimalkan sebelum kita tahu bahwa kita perlu.

### Hukum Putt

[Hukum Putt di Wikipedia](https://en.wikipedia.org/wiki/Putt%27s_Law_and_the_Successful_Technocrat)

> Teknologi didominasi oleh dua jenis orang, mereka yang mengerti apa yang tidak mereka kelola dan mereka yang mengelola apa yang tidak mereka mengerti.

Hukum Putt sering diikuti oleh Putt's Corollary:

> Setiap hierarki teknis, pada waktunya, mengembangkan inversi kompetensi.

Pernyataan-pernyataan ini menunjukkan bahwa karena berbagai kriteria seleksi dan tren dalam bagaimana kelompok mengatur, akan ada sejumlah orang yang terampil di tingkat kerja organisasi teknis, dan sejumlah orang dalam peran manajerial yang tidak menyadari kompleksitas dan tantangan dari pekerjaan yang mereka kelola. Ini bisa disebabkan oleh fenomena seperti [Prinsip Peter](#prinsip-peter) atau [Prinsip Dilbert](#prinsip-dilbert).

Namun, harus ditekankan bahwa Hukum seperti ini adalah generalisasi yang luas dan dapat berlaku untuk jenis organisasi _some_, dan tidak berlaku untuk yang lain.

Lihat juga:

- [Prinsip Peter](#prinsip-peter)
- [Prinsip Dilbert](#prinsip-dilbert)


### Hukum Reed

[Hukum Reed di Wikipedia](https://en.wikipedia.org/wiki/Reed's_law)

> Utilitas jaringan besar, khususnya jaringan sosial, secara eksponensial dengan ukuran jaringan.

Undang-undang ini didasarkan pada teori grafik, di mana skala utilitas sebagai jumlah sub-kelompok yang mungkin, yang lebih cepat dari jumlah peserta atau jumlah kemungkinan koneksi berpasangan. Odlyzko dan lainnya berpendapat bahwa Hukum Reed melebih-lebihkan utilitas sistem dengan tidak memperhitungkan batas-batas kognisi manusia pada efek jaringan; lihat [Nomor Dunbar](#nomor-dunbar).

Lihat juga:

- [Hukum Metcalfe](#hukum-metcalfe)
- [Nomor Dunbar](#nomor-dunbar)

### Hukum Konservasi Kompleksitas (Hukum Tesler)

[Hukum Konservasi Kompleksitas di Wikipedia](https://en.wikipedia.org/wiki/Law_of_conservation_of_complexity)

Hukum ini menyatakan bahwa ada sejumlah kompleksitas dalam suatu sistem yang tidak dapat dikurangi.

Beberapa kompleksitas dalam suatu sistem adalah 'tidak disengaja'. Ini adalah konsekuensi dari struktur yang buruk, kesalahan, atau hanya pemodelan masalah yang buruk untuk dipecahkan. Kompleksitas yang tidak disengaja dapat dikurangi (atau dihilangkan). Namun, beberapa kompleksitas bersifat 'intrinsik' sebagai konsekuensi dari kompleksitas yang melekat pada masalah yang sedang dipecahkan. Kompleksitas ini dapat dipindahkan, tetapi tidak dihilangkan.

Salah satu elemen yang menarik dari undang-undang ini adalah saran bahwa meskipun dengan menyederhanakan seluruh sistem, kompleksitas intrinsiknya tidak berkurang, tetapi dipindah-pindahkan ke pengguna_, yang harus berperilaku dengan cara yang lebih kompleks.

### Hukum Abstraksi Kebocoran

[Hukum Abstraksi Kebocoran on Joel on Software](https://www.joelonsoftware.com/2002/11/11/hukum-abstraksi-kebocoran/)

> Semua abstraksi non-sepele, sampai taraf tertentu, bocor.
>
> ([Joel Spolsky](https://twitter.com/spolsky))

Undang-undang ini menyatakan bahwa abstraksi, yang umumnya digunakan dalam komputasi untuk menyederhanakan bekerja dengan sistem yang rumit, dalam situasi tertentu akan 'membocorkan' elemen sistem yang mendasarinya, ini membuat abstraksi itu berperilaku dengan cara yang tidak terduga.

Contoh mungkin memuat file dan membaca isinya. API sistem file adalah _abstraksi_ dari sistem kernel level bawah, yang merupakan abstraksi atas proses fisik yang berkaitan dengan perubahan data pada plat magnetik (atau memori flash untuk SSD). Dalam kebanyakan kasus, abstraksi memperlakukan file seperti aliran data biner akan berfungsi. Namun, untuk drive magnetik, membaca data secara berurutan akan * secara signifikan * lebih cepat daripada akses acak (karena peningkatan overhead kesalahan halaman), tetapi untuk drive SSD, overhead ini tidak akan hadir. Detail yang mendasarinya perlu dipahami untuk menangani kasus ini (misalnya, file indeks basis data disusun untuk mengurangi overhead akses acak), rincian implementasi 'kebocoran' abstrak yang mungkin perlu diperhatikan pengembang.

Contoh di atas dapat menjadi lebih kompleks ketika abstraksi _lebih_ diperkenalkan. Sistem operasi Linux memungkinkan file diakses melalui jaringan tetapi direpresentasikan secara lokal sebagai file 'normal'. Abstraksi ini akan 'bocor' jika ada kegagalan jaringan. Jika pengembang memperlakukan file ini sebagai file 'normal', tanpa mempertimbangkan fakta bahwa mereka mungkin mengalami latensi dan kegagalan jaringan, solusinya akan bermasalah.

Artikel yang menggambarkan undang-undang ini menunjukkan bahwa ketergantungan yang berlebihan pada abstraksi, dikombinasikan dengan pemahaman yang buruk tentang proses yang mendasarinya, sebenarnya membuat masalah yang dihadapi semakin kompleks dalam beberapa kasus.

Lihat juga:

- [Hukum Hyrum](#hukum-hyrum-hukum-antarmuka-implisit)

Contoh dunia nyata:

- [Photoshop Startup Lambat](https://forums.adobe.com/thread/376152) - masalah yang saya temui di masa lalu. Photoshop akan lambat untuk memulai, kadang-kadang membutuhkan waktu beberapa menit. Tampaknya masalah adalah pada saat startup membaca beberapa informasi tentang printer default saat ini. Namun, jika printer itu sebenarnya adalah printer jaringan, ini bisa memakan waktu yang sangat lama. The _abstraction_ dari printer jaringan yang disajikan ke sistem yang mirip dengan printer lokal menyebabkan masalah bagi pengguna dalam situasi konektivitas yang buruk.

### Hukum Triviality

[Hukum Triviality di Wikipedia](https://en.wikipedia.org/wiki/Law_of_triviality)

Undang-undang ini menunjukkan bahwa kelompok akan memberikan lebih banyak waktu dan perhatian pada masalah-masalah sepele atau kosmetik daripada masalah yang serius dan substansial.

Contoh fiksi umum yang digunakan adalah bahwa komite menyetujui rencana untuk pembangkit listrik tenaga nuklir, yang menghabiskan sebagian besar waktu mereka membahas struktur gudang sepeda, daripada desain yang jauh lebih penting untuk pembangkit listrik itu sendiri. Mungkin sulit untuk memberikan masukan berharga pada diskusi tentang topik yang sangat besar dan kompleks tanpa keahlian atau persiapan subjek tingkat tinggi. Namun, orang ingin dilihat sebagai kontribusi input berharga. Oleh karena itu, kecenderungan untuk memfokuskan terlalu banyak waktu pada perincian kecil, yang dapat dipikirkan dengan mudah, tetapi tidak selalu penting.

Contoh fiksi di atas menyebabkan penggunaan istilah 'Bike Shedding' sebagai ungkapan untuk membuang-buang waktu pada detail sepele. Istilah terkait adalah '[Mencukur Yak](https://en.wiktionary.org/wiki/yak_shaving),' yang mengartikan aktivitas yang tampaknya tidak relevan yang merupakan bagian dari rantai panjang prasyarat untuk tugas utama.

### Filsafat Unix

[Filsafat Unix di Wikipedia](https://en.wikipedia.org/wiki/Unix_philosophy)

Filsafat Unix adalah bahwa komponen perangkat lunak harus kecil, dan fokus pada melakukan satu hal tertentu dengan baik. Ini dapat membuatnya lebih mudah untuk membangun sistem dengan menyusun unit-unit kecil, sederhana, dan terdefinisi dengan baik, daripada menggunakan program-program multi-fungsi yang besar, kompleks, dan multi-guna.

Praktik modern seperti 'Arsitektur Layanan Mikro' dapat dianggap sebagai penerapan undang-undang ini, di mana layanan kecil, fokus, dan melakukan satu hal spesifik, yang memungkinkan perilaku kompleks dapat terdiri dari blok bangunan sederhana.

### Model Spotify

[Model Spotify di Spotify Laboratorium](https://labs.spotify.com/2014/03/27/spotify-engineering-culture-part-1/)

Model Spotify adalah pendekatan terhadap tim dan struktur organisasi yang telah dipopulerkan oleh 'Spotify'. Dalam model ini, tim disusun berdasarkan fitur, bukan teknologi.

Model Spotify juga mempopulerkan konsep Tribes, Guilds, Chapters, yang merupakan komponen lain dari struktur organisasi mereka.

### Hukum Wadler

[Hukum Wadler on wiki.haskell.org](https://wiki.haskell.org/Wadler's_Law)

> Dalam desain bahasa apa pun, total waktu yang dihabiskan untuk mendiskusikan fitur dalam daftar ini sebanding dengan dua yang diangkat pada kekuatan posisinya.
>
> 0. Semantik
> 1. Sintaks
> 2. Sintaks leksikal
> 3. Sintaksis leksikal komentar
>
> (Singkatnya, untuk setiap jam yang dihabiskan untuk semantik, 8 jam akan dihabiskan untuk sintaksis komentar).

Mirip dengan [Hukum Triviality] (# hukum-triviality), Hukum Wadler menyatakan apa ketika merancang suatu bahasa, jumlah waktu yang dihabiskan untuk struktur bahasa sangat tinggi dibandingkan dengan pentingnya fitur-fitur itu.

Lihat juga:

- [Hukum Triviality](#hukum-triviality)

### Hukum Wheaton

[Link](http://www.wheatonslaw.com/)

[Hari Resmi](https://dontbeadickday.com/)

> Jangan menjadi kontol.
>
> _Setelah Wheaton_

Diciptakan oleh Wil Wheaton (Star Trek: The Next Generation, The Big Bang Theory), hukum yang sederhana, ringkas, dan kuat ini bertujuan untuk meningkatkan keharmonisan dan rasa hormat dalam organisasi profesional. Ini dapat diterapkan ketika berbicara dengan rekan kerja, melakukan tinjauan kode, menentang sudut pandang lain, mengkritik, dan secara umum, sebagian besar interaksi profesional yang dimiliki manusia satu sama lain.

## Prinsip

Prinsip umumnya lebih cenderung menjadi pedoman yang berkaitan dengan desain.

### Prinsip Dilbert

[Prinsip Dilbert di Wikipedia](https://en.wikipedia.org/wiki/Dilbert_principle)

> Perusahaan cenderung secara sistematis mempromosikan karyawan yang tidak kompeten ke manajemen untuk mengeluarkan mereka dari alur kerja.
>
> _Scott Adams_

Konsep manajemen yang dikembangkan oleh Scott Adams (pencipta strip komik Dilbert), Prinsip Dilbert terinspirasi oleh [Prinsip Peter](#prinsip-peter). Di bawah Prinsip Dilbert, karyawan yang tidak pernah kompeten dipromosikan ke manajemen untuk membatasi kerusakan yang dapat mereka lakukan. Adams pertama kali menjelaskan prinsip tersebut dalam artikel Wall Street Journal 1995, dan memperluasnya dalam buku bisnisnya tahun 1996, [Prinsip Dilbert](#daftar-bacaan).

Lihat juga:

- [Prinsip Peter](#prinsip-peter)
- [Hukum Putt](#hukum-putt)

### Prinsip Pareto (Aturan 80/20)

[Prinsip Pareto di Wikipedia](https://en.wikipedia.org/wiki/Pareto_principle)

> Sebagian besar hal dalam hidup tidak terdistribusi secara merata.

Prinsip Pareto menyarankan bahwa dalam beberapa kasus, sebagian besar hasil berasal dari minoritas input:

- 80% dari perangkat lunak tertentu dapat ditulis dalam 20% dari total waktu yang dialokasikan (sebaliknya, 20% tersulit dari kode membutuhkan 80% dari waktu)
- 20% dari upaya menghasilkan 80% dari hasilnya
- 20% dari pekerjaan menciptakan 80% dari pendapatan
- 20% dari bug menyebabkan 80% dari crash
- 20% dari fitur menyebabkan 80% dari penggunaan

Pada tahun 1940-an insinyur Amerika-Rumania Dr. Joseph Juran, yang secara luas diakui sebagai bapak kendali mutu, [mulai menerapkan Prinsip Pareto untuk masalah kualitas](https://en.wikipedia.org/wiki/Joseph_M._Juran).

Prinsip ini juga dikenal sebagai: Aturan 80/20, Hukum Beberapa Vital, dan Prinsip Faktor Sparsity.

Contoh dunia nyata:

- Pada tahun 2002 Microsoft melaporkan bahwa dengan memperbaiki 20% bug yang paling banyak dilaporkan, 80% kesalahan dan kerusakan terkait di windows dan office akan dihilangkan ([Referensi](https://www.crn.com/news/security/18821726/microsofts-ceo-80-20-rule-applies-to-bugs-not-just-features.htm)).

### Prinsip Peter

[Prinsip Peter di Wikipedia](https://en.wikipedia.org/wiki/Peter_principle)

> Orang-orang dalam hierarki cenderung naik ke "tingkat ketidakmampuan" mereka.
>
> _Laurence J. Peter_

Sebuah konsep manajemen yang dikembangkan oleh Laurence J. Peter, Prinsip Peter mengamati bahwa orang yang pandai dalam pekerjaannya dipromosikan, sampai mereka mencapai tingkat di mana mereka tidak lagi sukses ("tingkat ketidakmampuan" mereka. Pada titik ini, sebagaimana mereka lebih senior, mereka cenderung dikeluarkan dari organisasi (kecuali mereka tampil sangat buruk) dan akan terus berada dalam peran yang memiliki sedikit keterampilan intrinsik, karena keterampilan asli mereka yang membuat mereka sukses belum tentu keterampilan yang diperlukan untuk pekerjaan baru mereka.

Ini sangat menarik bagi para insinyur - yang awalnya memulai dalam peran teknis yang mendalam, tetapi sering memiliki jalur karier yang mengarah ke _mengelola_ insinyur lainnya - yang memerlukan keahlian yang berbeda secara mendasar.

Lihat juga:

- [Prinsip Dilbert](#prinsip-dilbert)
- [Hukum Putt](#hukum-putt)

### Prinsip Robustness (Hukum Postel)

[Prinsip Robustness di Wikipedia](https://en.wikipedia.org/wiki/Robustness_principle)

> Jadilah konservatif dalam apa yang Anda lakukan, menjadi liberal dalam apa yang Anda terima dari orang lain.

Sering diterapkan dalam pengembangan aplikasi server, prinsip ini menyatakan bahwa apa yang Anda kirim ke orang lain harus seminimal dan sesesuaian mungkin, tetapi Anda harus bertujuan untuk memungkinkan input yang tidak sesuai jika dapat diproses.

Tujuan dari prinsip ini adalah untuk membangun sistem yang kuat, karena mereka dapat menangani input yang terbentuk buruk jika maksudnya masih dapat dipahami. Namun, ada kemungkinan implikasi keamanan dari penerimaan input yang cacat, khususnya jika pemrosesan input tersebut tidak diuji dengan baik.

Membiarkan input yang tidak sesuai, pada waktunya, dapat merusak kemampuan protokol untuk berevolusi karena implementator pada akhirnya akan bergantung pada kebebasan ini untuk membangun fitur mereka.

Lihat juga:

- [Hukum Hyrum](#hukum-hyrum-hukum-antarmuka-implisit)


### SOLID

Ini adalah akronim, yang mengacu pada:

* S: [Prinsip Tanggung Jawab Tunggal](#prinsip-tanggung-jawab-tunggal)
* O: [Prinsip Terbuka / Tertutup](#prinsip-terbukatertutup)
* L: [Prinsip Substitusi Liskov](#prinsip-substitusi-liskov)
* I: [Prinsip Segregasi Antarmuka](#prinsip-segregasi-antarmuka)
* D: [Prinsip Ketergantungan Inversi](#prinsip-ketergantungan-inversi)

Ini adalah Prinsip utama dalam [Pemrograman Berorientasi Objek](#todo). Prinsip Desain seperti ini harus dapat membantu pengembang membangun sistem yang lebih dapat dipelihara.

### Prinsip Tanggung Jawab Tunggal

[Prinsip Tanggung Jawab Tunggal di Wikipedia](https://en.wikipedia.org/wiki/Single_responsibility_principle)

> Setiap modul atau kelas hanya memiliki satu tanggung jawab.

Prinsip pertama '[SOLID](#solid)'. Prinsip ini menyarankan agar modul atau kelas harus melakukan satu hal dan satu hal saja. Dalam istilah yang lebih praktis, ini berarti bahwa satu perubahan kecil ke fitur program harus memerlukan perubahan dalam satu komponen saja. Misalnya, mengubah cara kata sandi divalidasi untuk kompleksitas harus memerlukan perubahan hanya dalam satu bagian dari program.

Secara teoritis, ini harus membuat kode lebih kuat, dan lebih mudah untuk diubah. Mengetahui bahwa komponen yang sedang diubah memiliki tanggung jawab tunggal hanya berarti bahwa _percobaan_ perubahan itu harus lebih mudah. Dengan menggunakan contoh sebelumnya, mengubah komponen kompleksitas kata sandi seharusnya hanya dapat mempengaruhi fitur yang terkait dengan kompleksitas kata sandi. Mungkin akan jauh lebih sulit untuk mempertimbangkan dampak dari perubahan pada komponen yang memiliki banyak tanggung jawab.

Lihat juga:

- [Pemrograman Berorientasi Objek](#todo)
- [SOLID](#solid)

### Prinsip Terbuka / Tertutup

[Prinsip Terbuka / Tertutup di Wikipedia](https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle)

> Entitas harus terbuka untuk ekstensi dan ditutup untuk modifikasi.

Prinsip kedua '[SOLID](#solid)'. Prinsip ini menyatakan bahwa entitas (yang bisa berupa kelas, modul, fungsi, dan sebagainya) harus dapat memiliki perilakunya _diperpanjang_, tetapi bahwa perilaku mereka _ada_ seharusnya tidak dapat dimodifikasi.

Sebagai contoh hipotetis, bayangkan sebuah modul yang mampu mengubah dokumen penurunan harga menjadi HTML. Jika modul dapat diperluas untuk menangani fitur penurunan harga yang baru diusulkan, tanpa memodifikasi internal modul, maka itu akan terbuka untuk ekstensi. Jika modul dapat _tidak_ dimodifikasi oleh konsumen sehingga sekarang fitur Markdown yang ada ditangani, maka akan ditutup _ untuk modifikasi.

Prinsip ini memiliki relevansi khusus untuk Pemrograman Berorientasi Objek, di mana kita dapat mendesain objek agar mudah diperluas, tetapi akan menghindari mendesain objek yang dapat mengubah perilaku mereka saat ini dengan cara yang tidak terduga.

Lihat juga:

- [Pemrograman Berorientasi Objek](#todo)
- [SOLID](#solid)

### Prinsip Substitusi Liskov

[Prinsip Substitusi Liskov di Wikipedia](https://en.wikipedia.org/wiki/Liskov_substitution_principle)

> Seharusnya dimungkinkan untuk mengganti tipe dengan subtipe, tanpa merusak sistem.

Yang ketiga dari Prinsip '[SOLID](#solid)'. Prinsip ini menyatakan bahwa jika suatu komponen bergantung pada suatu tipe, maka ia harus dapat menggunakan subtipe dari tipe itu, tanpa sistem gagal atau harus mengetahui detail dari apa subtipe itu.

Sebagai contoh, bayangkan kita memiliki metode yang membaca dokumen XML dari struktur yang mewakili file. Jika metode ini menggunakan tipe file 'dasar', maka apa pun yang berasal dari 'file' harus dapat digunakan dalam fungsi tersebut. Jika 'file' mendukung pencarian secara terbalik, dan parser XML menggunakan fungsi itu, tetapi tipe turunan 'file jaringan' gagal ketika pencarian terbalik dicoba, maka 'file jaringan' akan melanggar prinsip.

Prinsip ini memiliki relevansi khusus untuk Pemrograman Berorientasi Objek, di mana hierarki jenis harus dimodelkan dengan cermat untuk menghindari pengguna sistem yang membingungkan.

Lihat juga:

- [Pemrograman Berorientasi Objek](#todo)
- [SOLID](#solid)

### Prinsip Segregasi Antarmuka

[Prinsip Segregasi Antarmuka di Wikipedia](https://en.wikipedia.org/wiki/Interface_segregation_principle)

> Tidak ada klien yang harus dipaksa untuk bergantung pada metode yang tidak digunakannya.

Prinsip keempat '[SOLID](#solid)'. Prinsip ini menyatakan bahwa konsumen suatu komponen tidak boleh bergantung pada fungsi-fungsi komponen yang sebenarnya tidak digunakannya.

Sebagai contoh, bayangkan kita memiliki metode yang membaca dokumen XML dari struktur yang mewakili file. Itu hanya perlu membaca byte, bergerak maju atau mundur dalam file. Jika metode ini perlu diperbarui karena fitur yang tidak terkait dari perubahan struktur file (seperti pembaruan untuk model izin yang digunakan untuk mewakili keamanan file), maka prinsipnya telah dibatalkan. Akan lebih baik bagi file untuk mengimplementasikan antarmuka 'seekable-stream', dan bagi pembaca XML untuk menggunakannya.

Prinsip ini memiliki relevansi khusus untuk Pemrograman Berorientasi Objek, di mana antarmuka, hierarki dan tipe abstrak digunakan untuk [meminimalkan kopling] (# todo) antara komponen yang berbeda. [Duck typing] (# todo) adalah metodologi yang menegakkan prinsip ini dengan menghilangkan antarmuka eksplisit.

Lihat juga:

- [Pemrograman Berorientasi Objek](#todo)
- [SOLID](#solid)
- [Duck Typing](#todo)
- [Decoupling](#todo)

### Prinsip Ketergantungan Inversi

[Prinsip Ketergantungan Inversi di Wikipedia](https://en.wikipedia.org/wiki/Dependency_inversion_principle)

> Modul tingkat tinggi tidak boleh bergantung pada implementasi tingkat rendah.

Kelima Prinsip '[SOLID](#solid)'. Prinsip ini menyatakan bahwa komponen pengatur tingkat yang lebih tinggi tidak harus mengetahui rincian ketergantungannya.

Sebagai contoh, bayangkan kita memiliki program yang membaca metadata dari situs web. Kami berasumsi bahwa komponen utama harus mengetahui tentang komponen untuk mengunduh konten halaman web, kemudian komponen yang dapat membaca metadata. Jika kita mempertimbangkan inversi dependensi, komponen utama hanya akan bergantung pada komponen abstrak yang dapat mengambil data byte, dan kemudian komponen abstrak yang dapat membaca metadata dari aliran byte. Komponen utama tidak akan tahu tentang TCP / IP, HTTP, HTML, dll.

Prinsip ini rumit, karena dapat 'membalikkan' dependensi yang diharapkan dari suatu sistem (karenanya namanya). Dalam praktiknya, ini juga berarti bahwa komponen orkestrasi terpisah harus memastikan implementasi yang benar dari tipe abstrak yang digunakan (mis. Dalam contoh sebelumnya, _sesuatu_ masih harus memberikan komponen pembaca metadata menjadi pengunduh file HTTP dan pembaca tag meta HTML). Ini kemudian menyentuh pola seperti [Pembalikan Kontrol](#todo) dan [Ketergantungan Injeksi](#todo).

See also:

- [Pemrograman Berorientasi Objek](#todo)
- [SOLID](#solid)
- [Inversi Kontrol](#todo)
- [Dependensi Injection](#todo)

### Prinsip KERING

[Prinsip KERING di Wikipedia](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)

> Setiap pengetahuan harus memiliki representasi tunggal, tidak ambigu, otoritatif dalam suatu sistem.

KERING adalah akronim untuk _Jangan Ulangi Diri Sendiri_. Prinsip ini bertujuan untuk membantu pengembang mengurangi pengulangan kode dan menyimpan informasi di satu tempat dan dikutip pada 1999 oleh Andrew Hunt dan Dave Thomas dalam buku [Pengembang Pragmatis](https://en.wikipedia.org/wiki/The_Pragmatic_Programmer)

> Kebalikan dari KERING adalah _WET_ (Tulis Semuanya Dua Kali atau Kami Menikmati Mengetik).

Dalam praktiknya, jika Anda memiliki informasi yang sama di dua (atau lebih) tempat berbeda, Anda dapat menggunakan KERING untuk menggabungkannya menjadi satu dan menggunakannya kembali di mana pun Anda inginkan / butuhkan.

Lihat juga:

- [The Pragmatic Developer](https://en.wikipedia.org/wiki/The_Pragmatic_Programmer)

### Prinsip KISS

[KISS di Wikipedia](https://en.wikipedia.org/wiki/KISS_principle)

> Tetap sederhana, bodoh

Prinsip KISS menyatakan bahwa sebagian besar sistem bekerja paling baik jika dibuat sederhana daripada dibuat rumit; oleh karena itu, kesederhanaan harus menjadi tujuan utama dalam desain, dan kompleksitas yang tidak perlu harus dihindari. Berasal dari Angkatan Laut AS pada tahun 1960, frasa tersebut telah dikaitkan dengan insinyur pesawat terbang Kelly Johnson.

Prinsipnya paling baik dicontohkan oleh kisah Johnson yang menyerahkan tim insinyur desain beberapa alat, dengan tantangan bahwa pesawat jet yang mereka desain harus diperbaiki oleh mekanik rata-rata di lapangan dalam kondisi pertempuran hanya dengan alat-alat ini. Oleh karena itu, "bodoh" mengacu pada hubungan antara cara barang pecah dan kecanggihan alat yang tersedia untuk memperbaikinya, bukan kemampuan para insinyur itu sendiri.

Lihat juga:

- [Hukum Gall](#hukum-gall)

### YAGNI

[YAGNI di Wikipedia](https://en.wikipedia.org/wiki/You_ain%27t_gonna_need_it)

Ini adalah akronim untuk _**Y**ou **A**in't **G**onna **N**eed **I**t_.

> Selalu terapkan hal-hal ketika Anda benar-benar membutuhkannya, jangan pernah ketika Anda hanya memperkirakan bahwa Anda membutuhkannya.
>
> ([Ron Jeffries](https://twitter.com/RonJeffries)) (salah satu pendiri dan penulis buku XP "Extreme Programming Installed")

Prinsip _Extreme Programming_ (XP) ini menyarankan pengembang seharusnya hanya mengimplementasikan fungsionalitas yang diperlukan untuk persyaratan segera, dan menghindari upaya untuk memprediksi masa depan dengan mengimplementasikan fungsionalitas yang mungkin diperlukan nanti.

Mematuhi prinsip ini harus mengurangi jumlah kode yang tidak digunakan dalam basis kode, dan menghindari waktu dan usaha yang dihabiskan untuk fungsionalitas yang tidak membawa nilai.

Lihat juga:

- [Daftar Bacaan: Extreme Programming Installed](#daftar-bacaan)

### Kekeliuran Komputasi Terdistribusi

[Kekeliuran Komputasi Terdistribusi di Wikipedia](https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing)

Juga dikenal sebagai _Fallacies of Networked Computing_, Fallacy adalah daftar dugaan (atau kepercayaan) tentang komputasi terdistribusi, yang dapat menyebabkan kegagalan dalam pengembangan perangkat lunak. Asumsinya adalah:

- Jaringannya andal
- Latensi adalah nol
- Bandwidth tidak terbatas
- Jaringan aman
- Topologi tidak berubah
- Ada satu administrator
- Biaya transportasi nol
- Jaringannya homogen

Empat item pertama didaftar oleh [Bill Joy](https://en.wikipedia.org/wiki/Bill_Joy) dan [Tom Lyon](https://twitter.com/aka_pugs) sekitar 1991 dan pertama diklasifikasikan oleh [James Gosling](https://en.wikipedia.org/wiki/James_Gosling) sebagai "Fallacy of Networked Computing". [L. Peter Deutsch](https://en.wikipedia.org/wiki/L._Peter_Deutsch) menambahkan fallacy ke-5, ke-6 dan ke-7. Di akhir tahun 90-an Gosling menambahkan kekeliruan ke-8.

Kelompok itu terinspirasi oleh apa yang terjadi pada saat di dalam [Sun Microsystems](https://en.wikipedia.org/wiki/Sun_Microsystems).

Kekeliruan ini harus dipertimbangkan dengan hati-hati ketika merancang kode yang tangguh; dengan asumsi salah satu dari kesalahan ini dapat menyebabkan cacat logika yang gagal untuk berurusan dengan realitas dan kompleksitas sistem terdistribusi.

Lihat juga:

- [Mencari Makan untuk Kekeliruan Komputasi Terdistribusi (Bagian 1) - Vaidehi Joshi di Medium](https://medium.com/baseds/foraging-for-the-fallacies-of-distributed-computing-part-1-1b35c3b85b53)
- [Deutsch's Fallacies, 10 Years After](http://java.sys-con.com/node/38665)

## Daftar Bacaan

Jika Anda merasa konsep ini menarik, Anda dapat menikmati buku-buku berikut.

- [Extreme Programming Installed - Ron Jeffries, Ann Anderson, Chet Hendrikson](https://www.goodreads.com/en/book/show/67834) - Covers the core Prinsip of Extreme Programming.
- [The Mythical Man Month - Frederick P. Brooks Jr.](https://www.goodreads.com/book/show/13629.The_Mythical_Man_Month) - A classic volume on software engineering. [Hukum Brooks](#hukum-brooks) is a central theme of the book.
- [Gödel, Escher, Bach: An Eternal Golden Braid - Douglas R. Hofstadter.](https://www.goodreads.com/book/show/24113.G_del_Escher_Bach) - This book is difficult to classify. [Hukum Hofstadter](#hukum-hofstadter) is from the book.
- [Prinsip Dilbert - Scott Adams](https://www.goodreads.com/book/show/85574.The_Dilbert_Principle) - A comic look at corporate America, from the author who created the [Dilbert Principle](#prinsip-dilbert).
- [Prinsip Peter - Lawrence J. Peter](https://www.goodreads.com/book/show/890728.The_Peter_Principle) - Another comic look at the challenges of larger organisations dan people management, the source of [Prinsip Peter](#prinsip-peter).

## Berkontribusi

Silakan berkontribusi! [Angkat masalah](https://github.com/dwmkerr/hacker-laws/issues/new) jika Anda ingin menyarankan penambahan atau perubahan, atau [Open a pull request](https://github.com/dwmkerr/hacker-laws/compare) untuk mengusulkan perubahan Anda sendiri.

Pastikan untuk membaca [Panduan Berkontribusi](./../.github/contributing.md) untuk persyaratan teks, gaya dan sebagainya. Harap perhatikan [Code of Conduct](./../.github/CODE_OF_CONDUCT.md) ketika terlibat dalam diskusi tentang proyek.

## TODO

Hai! Jika Anda mendarat di sini, Anda telah mengklik tautan ke topik yang belum saya tulis, maaf tentang ini - ini sedang dalam proses!

Jangan ragu untuk [Mengangkat Masalah](https://github.com/dwmkerr/hacker-laws/issues) meminta lebih banyak detail, atau [Open a Pull Request](https://github.com/dwmkerr/hacker-laws/pulls) untuk menyerahkan definisi topik yang Anda usulkan.
