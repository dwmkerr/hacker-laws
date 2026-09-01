# 💻📖 hacker-laws

Programcıların faydalı bulacağı yasalar, teoriler, prensipler ve desenler.

[Çeviriler](#%C3%A7eviriler): [🇧🇷](./translations/pt-BR.md) [🇨🇳](https://github.com/nusr/hacker-laws-zh) [🇫🇷](./translations/fr.md) [🇮🇹](./translations/it-IT.md) [🇱🇻](./translations/lv.md) [🇰🇷](https://github.com/codeanddonuts/hacker-laws-kr) [🇷🇺](https://github.com/solarrust/hacker-laws) [🇪🇸](./translations/es-ES.md) [🇮🇩](./translations/id.md) [🇯🇵](./translations/jp.md) [🇵🇱](./translations/pl.md) [🇻🇳](./translations/vi.md)

Bu projeyi beğendiniz mi? Lütfen [sponsor olmayı](https://github.com/sponsors/dwmkerr) düşünün!

---

<!-- vim-markdown-toc GFM -->

- [Giriş](#giri%C5%9F)
- [Yasalar](#yasalar)
    - [90–9–1 Prensibi (1% Kuralı)](#9091-prensibi-1-kural%C4%B1)
    - [Amdahl Yasası](#amdahl-yasas%C4%B1)
    - [Kırık Camlar Teorisi](#the-broken-windows-theory)
    - [Brooks Yasası](#brooks-law)
    - [CAP Teorisi (Brewer Teorisi)](#cap-teroisi-brewer-teorisi)
    - [Conway Yasası](#conways-law)
    - [Cunningham Yasası](#cunninghams-law)
    - [Dunbar Sayısı](#dunbars-number)
    - [Fitt Yasası](#fitt-yasas%C4%B1)
    - [Gall Yasası](#galls-law)
    - [Goodhart Yasası](#goodharts-law)
    - [Hanlon'un Usturası](#hanlons-razor)
    - [Hick Yasası (Hick-Hyman Yasası)](#hick-yasas%C4%B1-hick-hyman-yasas%C4%B1)
    - [Hofstadter Yasası](#hofstadters-law)
    - [Hutber Yasası](#hutbers-law)
    - [Hype Döngüsü ve Amara Yasası](#the-hype-cycle--amaras-law)
    - [Hyrum Yasası (Arabirimlerin Örtülü Hukuku)](#hyrums-law-the-law-of-implicit-interfaces)
    - [Kernighan Yasası](#kernighans-law)
    - [Metcalfe Yasası](#metcalfes-law)
    - [Moore Yasası](#moores-law)
    - [Murphy Yasası / Sod  Yasası](#murphys-law--sods-law)
    - [Occam'ın Usturası](#occams-razor)
    - [Parkinson Yasası](#parkinsons-law)
    - [Olgunlaşmamış Optimizasyon Etkisi](#premature-optimization-effect)
    - [Putt Yasası](#putts-law)
    - [Reed Yasası](#reeds-law)
    - [Karmaşıklığın Korunması Yasası (Tesler Yasası)](#the-law-of-conservation-of-complexity-teslers-law)
    - [Demeter Yasası](#demeter-yasas%C4%B1)
    - [Sızdıran Soyutlamalar Yasası](#the-law-of-leaky-abstractions)
    - [Önemsizlik Yasası](#the-law-of-triviality)
    - [Unix Felsefesi](#the-unix-philosophy)
    - [Spotify Modeli](#the-spotify-model)
    - [Wadler Yasası](#wadlers-law)
    - [Wheaton Yasası](#wheatons-law)
- [Prensipler](#principles)
    - [Ölü Deniz Etkisi](#%C3%B6l%C3%BC-deniz-etkisi)
    - [Dilbert Prensibi](#the-dilbert-principle)
    - [Pareto Prensibi (80/20 Kuralı)](#the-pareto-principle-the-8020-rule)
    - [Peter Prensibi](#the-peter-principle)
    - [Dayanıklılık Prensibi (Postel Yasası)](#the-robustness-principle-postels-law)
    - [SOLID](#solid)
    - [Tek Sorumluluk Prensibi](#the-single-responsibility-principle)
    - [Açık/Kapalı Prensibi](#the-openclosed-principle)
    - [Liskov Yerine Geçme Prensibi](#the-liskov-substitution-principle)
    - [Arayüz Ayrım Prensibi](#the-interface-segregation-principle)
    - [Bağımlılığın Ters Çevrilmesi](#the-dependency-inversion-principle)
    - [DRY Prensibi](#the-dry-principle)
    - [KISS prensibi](#the-kiss-principle)
    - [YAGNI](#yagni)
    - [Dağıtık Sistemlerin Yanılgıları](#da%C4%9F%C4%B1t%C4%B1k-sistemlerin-yan%C4%B1lg%C4%B1lar%C4%B1)
- [Ek Kaynaklar](#reading-list)
- [Çeviriler](#translations)
- [Katkıda Bulunmak İçin](#related-projects)
- [Katkıda Bulunmak İçin](#contributing)
- [TODO](#todo)

<!-- vim-markdown-toc -->

## Giriş

İnsanların geliştirme hakkında konuşurken tartıştıkları birçok yasa var. Bu depo, en yaygın olanlardan bazılarının referanslarını ve özetini barındırır. Katkıda bulunmak için PR açıp gönderebilirsiniz!

❗: Bu depo yasaların, prensiplerin ve modellerin bilgi vermek amaçlı açıklamalarını içerir ve hiçbirini *savunma* amacı gütmez. Bunların hangisinin uygulanıp uygulanmayacağı tamamen tartışma konusudur ve yapılan işe bağlıdır..

## Yasalar

Tek tek başlayalım!

### 90–9–1 Prensibi (1% Kuralı)

[Wikipedia'da 1% Kuralı](https://en.wikipedia.org/wiki/1%25_rule_(Internet_culture))

90-9-1 prensibi der ki, bir internet topluluğunda (örneğin bir wiki) üyelerin %90'ı sadece içeriği okur, %9'u içeriği düzenleme ya da düzeltme yapar ve %1'i ise yeni içerik ekler.

Gerçek dünyadan örnekler:

- Dört dijital sağlık sosyal ağlarına ilişkin 2014 yılında yapılan bir araştırma, topluluğun %1'inin gönderilerin %73'ünü oluşturduğunu, %9'unun ortalama %25'ini ve geri kalan %90'ının da ortalama %2'sini oluşturduğunu buldu ([Referans](https://www.jmir.org/2014/2/e33/)).

Ek kaynaklar:

- [Pareto prensibi](#pareto-prensibi-8020-kural%C4%B1)

### Amdahl Yasası

[Wikipedia Amdahl Yasası](https://en.wikipedia.org/wiki/Amdahl%27s_law)

> Amdahl Yasası kaynakları artırarak bir hesaplama işleminin *olası* hızlanma miktarını hesaplayan bir formülü tanımlar. Genellikle paralel işleme hesaplarında kullanılır ve işlemci sayısının artırılmasının programın paralelleştirilebilme kapasitesine bağlı olarak etkisinin doğru şekilde saplanmasını sağlar.

En güzel şu örnekle anlatılabilir. Bir programın iki bölümden oluştuğunu düşünelim. Bölüm A sadece tek işlemci ile çalıştırılabilir. Bölüm B ise paralelleştirilebilecek şekilde yazılmış. Bu durumda bu programı çok işlemci ile çalıştırdığımızda Bölüm B'de oluşacak kadar bir kazanım sağlayabiliriz. Bölüm A'da her hangi bir katkı olamayacaktır.

Aşağıdaki diyagram bazı olası hız geliştirmelerine örnekler içeriyor:

<img width="480px" alt="Diagram: Amdahl's Law" src="../../../../images/amdahls-law.svg">

*(Diyagramın kaynağı: Daniels220 tarafından İngilizce Wikipedia'da, Creative Commons Attribution-Share Alike 3.0 Unported, https://en.wikipedia.org/wiki/File:AmdahlsLaw.svg)*

Diyagramdaki örneklerden görüldüğü üzere, eğer bir programın sadece %50'si paralelleştirilebiliyorsa 10 işlemciden sonra işlemci eklemek hızda gözle görünür bir artış sağlamıyor ama %95 paralelleştirilebilen bir programda 1000 işlemciden sonra bile işlemci eklemenin hızı artırdığı gözlenebilir.

[Moore Yasasında](#moores-law) söylenen artışın azalma eğiliminde olması ve aynı zamanda işlemci hızının artışında da ivme kaybı olması, paralelleştirilebilme özelliğini performans artışında anahtar duruma getirdi. Grafik programlama bu konuda en belirgin örnek. Shader tabanlı modern işleme ile pixel ve fragmanların paralel olarak render edilebilmesi sayesinde modern grafik kartlarında binlerce işlemci çekirdeği olabiliyor.

Ek kaynaklar:

- [Brooks Yasası](#brooks-law)
- [Moore Yasası ](#moores-law)

### Kırık Camlar Teorisi

[Wikipedia'da Kırık Camlar Teorisi](https://en.wikipedia.org/wiki/Broken_windows_theory)

Kırık Camlar Teorisi, gözle görülebilir suç belirtilerinin (ya da ortamın  bakımsızlığının) daha ciddi suçlara (ya da ortamın daha da bozulmasına) yol açtığını göstermektedir.

Bu teori, yazılım geliştirmeye şu şekilde uygulanabilir; düşük kalite kodun (veya [Teknik Borcun](#TODO)) varlığı kaliteyi geliştirme çabalarının göz ardı edilebileceği veya önemsenmeyeceği algısına yol açabileceği ve dolayısıyla düşük kalite koda sebep olabileceğidir. Bu etki zamanla kalitenin daha çok azalmasına neden olur.

Ek kaynaklar:

- [Teknik Borç](#TODO)

Örnekler:

- [Pragmatik Programlama: Yazılım Entropisi](https://pragprog.com/the-pragmatic-programmer/extracts/software-entropy)
- [Kodlama Kabusu: Kırık Camlar Teorisi](https://blog.codinghorror.com/the-broken-window-theory/)
- [Açık Kaynak: Eğlenceli Programlama - Kırık Camlar Teorisi](https://opensourceforu.com/2011/05/joy-of-programming-broken-window-theory/)

### Brooks Yasası

[Wikipedia'da Brooks Yasası](https://en.wikipedia.org/wiki/Brooks%27s_law)

> Gecikmesi kesinleşmiş projeye yeni insan kaynağı eklemek projeyi daha da geciktirir.

Bu yasa, gecikmiş bir projeyi hızlandırmak için ek insan kaynağı koymanın projeyi daha geciktireceğini iddia ediyor. Brook'a göre bunun gereksiz bir sadeleştirme olduğu kesin. Yeni katılanların adapte edilmesi ve iletişim karmaşası hemen etkisini göstererek hızın yavaşlamasına sebep olur. Ayrıca, yapılacak işlerin birçoğu genellikle daha küçük parçalara bölünemez ve birden fazla kaynak bu işlerin yapılması için kullanılmaz. Bu durum beklenen artışın sağlanmaması ile sonuçlanır.

Meşhur "Dokuz kadın ile 1 ayda doğum sağlanamaz" deyimi bu yasanın en pratik anlatımıdır. Bazı işlerin bölünemediği veya paralelleştirilemediği gerçeğini unutmamak lazım.

'[The Mythical Man Month](#reading-list)' adlı kitabın ana konularından biri budur.

Ek kaynaklar:

- [Death March](#todo)
- [Reading List: The Mythical Man Month](#reading-list)

### CAP Teorisi (Brewer Teorisi)

CAP Teoremi (Eric Brewer tarafından tanımlanmıştır) dağıtılmış bir veri deposu için aşağıdaki üç garantiden sadece ikisinin (en fazla) sağlanabileceğini belirtmektedir:

- Tutarlılık: verileri okurken, her istek verinin *en son* halini alır veya bir hata döndürülür
- Erişilebilirlik: veri okurken, her istek verinin *en son*hali olduğunu garanti etmeden *hata içermeyen bir yanıt* alır
- Parçalara Ayrılma Toleransı: Düğümler arasında belli bir sayıda ağ isteği başarısız olduğunda, sistem beklendiği gibi çalışmaya devam eder

Tartışmanın özü şöyledir. Bir ağ paylaşımının olmayacağını garanti etmek imkansızdır (bkz. [Dağıtık Sistemlerin Yanılgıları ](#da%C4%9F%C4%B1t%C4%B1k-sistemlerin-yan%C4%B1lg%C4%B1lar%C4%B1)). Bu nedenle bir paylaşımlı yapı söz konusu olduğunda, işlemi iptal edebilir (tutarlılığı artırabilir ve kullanılabilirliği azaltabiliriz) veya devam edebiliriz (kullanılabilirliği artırabilir, tutarlılığı azaltabilir).

Teorinin ismi, garanti edilmeye çalışılan kavramların ilk harflerinden (Consistency, Availability, Partition Tolerance) oluşturulmuştur. Bunun [*ACID*](#TODO) ile alakalı *olmayan* farklı bir tanımı olduğunu bilmenin çok önemli olduğunu unutmayın. Daha güncel olarak, ağın paylaşımlı *olmadığı* yapılarda (sistem beklendiği çalışmaya devam ederken) gecikmeye ve tutarlılığa bazı kısıtlamalar getiren [PACELC](#TODO) teoremi geliştirilmiştir.

Çoğu modern veritabanı platformu, veritabanı kullanıcılarına yüksek düzeyde kullanılabilirlik ('kirli okuma' içerebilir) veya yüksek düzeyde tutarlık (örneğin 'yeterli çoğunlukla onaylanmış yazma') arasında seçim yapma seçeneği sunarak bu teoremi örtük olarak kabul eder.

Gerçek dünyadan örnekler:

- [Google Cloud Spanner ve CAP Teorisi](https://cloud.google.com/blog/products/gcp/inside-cloud-spanner-and-the-cap-theorem) - İlk olarak CAP garantilerinin *hepsine* sahip gibi görünen, ancak kaputun altında bir CP sistemi olan Cloud Spanner'ın nasıl çalıştığının ayrıntıları anlatılıyor.

Ek kaynaklar:

- [ACID](#TODO)
- [Dağıtık Sistemlerin Yanılgıları](#the-fallacies-of-distributed-computing)
- [PACELC](#TODO)

### Conway Yasası

[Wikipedia'da Conway Yasası](https://en.wikipedia.org/wiki/Conway%27s_law)

Conway yasası der ki; üretilen sistemler kendilerini üreten organizasyonun teknik sınırlarını yansıtır. Bu yasa daha çok organizasyon değişiklikleri sırasında dikkate alınır. Eğer bir organizasyon birbirinden bağımsız küçük birimlerden oluşuyorsa üretilen yazılımlar da buna uygun olacaktır. Eğer bu organizasyon servis odaklı dikey yapılandırılmışsa, yazılımlar bunu yansıtacaktır.

Ek kaynaklar:

- [Spotify Modeli](#the-spotify-model)

### Cunningham Yasası

[Wikipedia'da Cunningham Yasası](https://en.wikipedia.org/wiki/Ward_Cunningham#Cunningham's_Law)

> İnternette doğru cevabı almanın en iyi yolu, soru sormak değil, yanlış olan cevabı yazmaktır.

Steven McGeady'ye göre, Ward Cunningham, 1980'lerin başında ona tavsiye olarak “İnternette doğru cevabı almanın en iyi yolu, bir soru sormak değil, yanlış olan cevabı yazmaktır” dedi. McGeady bunu Cunningham kanunu olarak adlandırdı, ancak Cunningham bu sahipliği bunun "yanlış bir alıntı" olduğunu nitelendirerek reddetti. Her ne kadar orjinalinde Usenet'teki etkileşimlerle ilgili olsa da, yasa diğer çevrimiçi toplulukların nasıl çalıştığını açıklamak için kullanılmıştır (örneğin, Wikipedia, Reddit, Twitter, Facebook).

Ek kaynaklar:

- [XKCD 386: "Duty Calls"](https://xkcd.com/386/)

### Dunbar Sayısı

[Wikipedia'da Dunbar Sayısı](https://en.wikipedia.org/wiki/Dunbar%27s_number)

"Dunbar'ın sayısı, bir kişinin istikrarlı bir sosyal ilişkide bulunabileceği kişilerin sayısının kavramsal sınırıdır - bu ilişki bireyin ilişkide olduğu her bir kişinin kim olduğunu ve her bir kişinin diğer bir kişiler ile ilişkisini bildiği ilişkidir." Sayının tam değeri konusunda bir anlaşmazlık vardır. "... [Dunbar] insanların ancak 150 kişilik ilişkiler istikrarlı bir şekilde bulunabileceğini söylemiş."... Dunbar sayıyı daha sosyal bir bağlam içine koydu, "sayıyı bir barda içki içmeye davet edildiğinizde sıkılmadan ya da utanmadan kabul edebileceğiniz kişi sayısı olarak değerlendirdi". Bu da 100 ile 250 arasındaki bir sayı olarak düşünülebilir.

Kişiler arası insani ilişkilerde olduğu gibi, insanlarla kod arasındaki ilişki de sürüdürülebilmek için çaba gerektirir. Karmaşık projelerle karşılaştığımızda ya da bu projeleri yönetmek sorunda kaldığımızda, projeyi ölçekleyebilmek için eğilimlere, politikalara ve modellenmiş prosedürlere yaslanmaya çalışırız. Dunbar sayısını sadece çalışan sayısı büyüdüğünde değil, takımın harcayacağı emeğin kapsamını belirlerken ya da sistemdeki lojistik ek yükün modellenmesine ve otomatikleştirilmesine yardımcı olmak için takımlara yatırım yaparken de göz önünde bulundurulmalıdır. Bir başka mühendislik bağlamında düşünürsek, bu sayı müşteri destek sisteminde nöbetçi olunurken sorumluluğunu alabileceğiniz proje/ürün sayısını belirlerken de rehber olabilir.

Ek kaynaklar:

- [Conway Yasası](#conways-law)

### Fitt Yasası

[Wikipedia'da Fitt Yasası](https://en.wikipedia.org/wiki/Fitts%27s_law)

Fitts yasası, bir hedef alana gitmek için gereken sürenin hesaplanmasında, hedefe olan mesafenin hedefin genişliğine bölünmesinin bir işlevi olduğunu öngörür.

<img width="300px" alt="The Hype Cycle" src="./images/fitts-law.svg">

Bu yasanın sonuçları, UX veya UI tasarlanırken etkileşimli öğelerin mümkün olduğunca büyük olması ve kullanıcıların dikkat alanı ile etkileşimli öğe arasındaki mesafenin mümkün olduğunca küçük olması gerektiğini ortaya çıkarır. Bunun tasarım üzerinde sonuçları vardır, örneğin birbirleriyle yakın kullanılan işlevlerin gruplanması gibi.

Ayrıca, ekranın köşeleri için temel kullanıcı arayüzü öğelerinin yerleştirilebileceği 'sihirli köşeler' (bir kullanıcının farelerini kolayca vurabileceği ya da süpürebileceği) kavramını resmileştiriyor. Windows Başlat düğmesi sihirli bir köşede, seçmeyi kolaylaştırıyor ve ilginç bir kontrast olarak, MacOS'un 'pencereyi kapat' düğmesi sihirli bir köşede *değil*, yanlışlıkla tıklanmayı zorlaştırıyor.

Ek kaynaklar:

- [İnsan motor sisteminin hareket genliğini kontrol etme veri kapasitesi.](https://www.semanticscholar.org/paper/The-information-capacity-of-the-human-motor-system-Fitts/634c9fde5f1c411e4487658ac738dcf18d98ea8d)

### Gall Yasası

[Wikipedia'da Gall Yasası](https://en.wikipedia.org/wiki/John_Gall_(author)#Gall's_law)

> Çalışan karmaşık bir sistemin her zaman işe yarayan daha basit bir sistemden evrimleştiği kesinlikle söylenebilir. Başlangıçtan itibaren karmaşık tasarlanmış bir sistemin asla çalışmayacağı ve sonradan da düzeltilemeyeceği kesindir. Çalışsan daha basit bir sistem ile başlamanız gerekir. ([John Gall](https://en.wikipedia.org/wiki/John_Gall_(author)))
> ([John Gall](https://en.wikipedia.org/wiki/John_Gall_(author)))

Gall Yasası der ki, çok karmaşık sistemleri *tasarlamaya* çalışmak her zaman başarısızlıkla sonuçlanır. Bu tür sistemlerin ilk denemede başarılı olmaları çok nadir görülür ama genellikle basit sistemlerden evrilirler.

En klasik örnek günümüzdeki internettir.  Şu an çok karmaşık bir sistemdir.  Aslında başlangıçta sadece akademik kurumlar arası içerik paylaşımı olarak tanımlanmıştı. Bu tanımı karşılamada çok başarılı oldu ve zamanla gelişerek bugünkü karmaşık halini aldı.

Ek kaynaklar:

- [KISS (Keep It Simple, Stupid)](#the-kiss-principle)

### Goodhart Yasası

[Wikipedia'da Goodhart Yasası](https://en.wikipedia.org/wiki/Goodhart's_law)

> Gözlemlenen herhangi bir istatistiksel düzenlilik, kontrol amaçları için üzerine baskı uygulandığında çökme eğiliminde olacaktır. *Charles Goodhart*
> *Charles Goodhart*

Ayrıca şu şekilde de ifade edilir:

> Bir ölçüm hedef haline geldiğinde, iyi bir ölçüm olmaktan çıkar. *Marilyn Strathern*
> *Marilyn Strathern*

Bu yasa, ölçüme dayalı optimizasyonların, ölçüm sonucunun kendisinin anlamsızlaşmasına yol açabileceğini belirtmektedir. Bir prosese kör bir şekilde uygulanan aşırı seçici tedbirler ( [KPI'ler](https://en.wikipedia.org/wiki/Performance_indicator) ) çarpık bir etkiye neden olur. İnsanlar, eylemlerinin bütünsel sonuçlarına dikkat etmek yerine belirli metrikleri tatmin etmek için sistemle "oynayarak" yerel olarak optimize etme eğilimindedir.

Gerçek dünyadan örnekler:

- "Asert" olmadan yazılan testler, ölçümün amacının iyi test edilmiş bir yazılım oluşturmak olmasına rağmen sadece kod kapsamı beklentisini karşılar.
- Yazılan satır sayısının gösterdiği geliştirici performans puanı haksız yere şişirilmiş kod tabanına yol açar.

Ek kaynaklar:

- [Goodhart Yasası: Yanlış Şeyleri Ölçmek Ahlaksız Davranışları Nasıl Yönlendirir?](https://coffeeandjunk.com/goodharts-campbells-law/)
- [Sorunsuz bir yazılım dünyasında Dilbert](https://dilbert.com/strip/1995-11-13)

### Hanlon'un Usturası

[Wikipedia'da Hanlon'un Usturası](https://en.wikipedia.org/wiki/Hanlon%27s_razor)

> Aptallıkla layıkıyla açıklanabilecek bir şeyi, asla kötü niyete bağlamayın. Robert J. Hanlon
> Robert J. Hanlon

Bu prensip, olumsuz sonuçlara yol açan eylemlerin, çoğunlukla kötü niyetin sonucu olmadığını savunmaktadır. Aksine, olumsuz sonuç daha büyük olasılıkla bu eylemlerin ve/veya etkinin tam olarak anlaşılamamasına bağlıdır.

### Hick Yasası (Hick-Hyman Yasası)

[Wikipedia'da Hick Yasası](https://en.wikipedia.org/wiki/Hick%27s_law)

> Karar verme süresi, seçebileceğiniz seçeneklerin sayısı ile logaritmik orantılı olarak büyür.
> William Edmund Hick and Ray Hyman

Aşağıdaki denklemde, `T` karar verme zamanıdır, `n` seçenek sayısıdır ve `b` verilerin analizi ile belirlenen bir sabittir.

![Hicks law](./images/hicks-law.svg)

*(Diagramın Kaynağı: Creative Commons Attribution-Share Alike 3.0 Unported, https://en.wikipedia.org/wiki/Hick%27s_law)*

Bu yasa yalnızca seçeneklerin sayısı *sıralandığında* (örneğin alfabetik olarak) geçerlidir. Bu, temel iki logaritmada ima edilir - bu, karar vericinin aslında bir *ikili arama* gerçekleştirdiğini ima eder. Seçenekler iyi sıralanmamışsa, deneyler geçen sürenin doğrusal olduğunu gösterir.

Bunun UI tasarımında önemli bir etkisi vardır; kullanıcıların seçenekleri kolayca arayabilmelerini sağlamak daha hızlı karar almayı sağlar.

Hick Yasasında IQ ile reaksiyon süresi arasında [Bilgi İşleme Hızı: Gelişimsel Değişim ve İstihbarat Bağlantıları](https://www.sciencedirect.com/science/article/pii/S0022440599000369) makalesinde bahsedildiği gibi bir korelasyon da gösterilmiştir.

Ek kaynaklar:

- [Fitts Yasası](#fitts-law)

### Hofstadter Yasası

[Wikipedia'da Hofstadter Yasası](https://en.wikipedia.org/wiki/Hofstadter%27s_law)

> Bir iş her zaman umduğundan daha uzun sürer, Hofstadter yasasını göz önünde bulundursan bile. (Douglas Hofstadter)
> (Douglas Hofstadter)

Bu yasayı bir işin ne kadar süreceğini tahminlenirken hatırlatıldığı için duymuş olabilirsiniz. Herkesin kabul ettiği bir gerçek var ki, yazılım geliştirmede en kötü olduğumuz alan işin ne kadar sürede biteceğini tahmin etmektir.

'[Gödel, Escher, Bach: An Eternal Golden Braid](#reading-list)' adlı kitaptan bir alıntı.

Ek kaynaklar:

- [Reading List: Gödel, Escher, Bach: An Eternal Golden Braid](#reading-list)

### Hutber Yasası

[Wikipedia'da Hutber Yasası ](https://en.wikipedia.org/wiki/Hutber%27s_law)

> İyileştirme, bozulma anlamına da gelir. ([Patrick Hutber](https://en.wikipedia.org/wiki/Patrick_Hutber))
> ([Patrick Hutber](https://en.wikipedia.org/wiki/Patrick_Hutber))

Bu yasa der ki; sistemde yapılan bir iyileştirme sistemin diğer taraflarında bozulmaya sebep olabilir ya da başka bozuklukları gizleyebilir, bu da sistemin mevcut durumunun daha da bozulmasına sebep olabilir.

Örneğin, bir servisin cevap verme zamanında bir geliştirme yapılıp hızlandırılırsa bu durum süreçteki diğer aşamalarda kapasite ve çıktı artışına sebep olabilir. Bu da sistemin diğer taraflarını olumsuz etkileyebilir.

### Hype Döngüsü ve Amara Yasası

[Wikipedia'da Hype Döngüsü](https://en.wikipedia.org/wiki/Hype_cycle)

> Bir teknolojinin kısa vadede oluşacak etkisini abartıp, uzun vadede oluşacak etkisini hafife alıyoruz. (Roy Amara) (Roy Amara)
> (Roy Amara)

Hype Döngüsü bir teknolojinin zamanla yarattığı heyecan ve gelişiminin görsel olarak sunumudur ve Gartner tarafından ilk olarak oluşturulmuştur. En güzel anlatım aşağıdaki bir görsel ile yapılabilir:

![The Hype Cycle](./images/hype-cycle.svg)

*(Resmin Kaynağı: Jeremykemp tarafından İngilizce Wikipeda'da, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=10547051)*

Kısaca anlatmak gerekirse, bu döngü her yeni teknolojinin ilk zamanlarında teknolojinin kendisi ve olası etkisi üzerinde bir heyecan dalgası oluştuğunu iddia ediyor. Ekipler yeni teknolojiler hemen kullanmaya çalışıyorlar ve genelde kendilerini sonuçtan memnun olmamış bir halde buluyorlar. Bu ya teknolojinin henüz olgunlaşmamış olmasından, ya da uygulamanın tam anlamıyla gerçekleşmemiş olmasından olabilir. Belirli bir süre geçtikten sonra, teknolojinin yeterliliği ve pratik kullanım alanları artar ve ekipler daha üretken olmaya başlar. Roy Amara'nın sözü bu durumu en özlü şekilde toparlıyor diyebiliriz - "Bir teknolojinin kısa vadede oluşacak etkisini abartıp, uzun vadede oluşacak etkisini hafife alıyoruz".

### Hyrum Yasası (Arabirimlerin Örtülü Hukuku)

[Hyrum Yasası Web Sitesi](http://www.hyrumslaw.com/)

> Belli sayıda kullanıcıya ulaştığında, servis sözleşmesinde ne demiş olduğunuzdan bağımsız olarak ürününüzün ya da sisteminizin bütün gözlemlenebilir davranışları artık üçüncü kişilere göre şekillenecektir.
> (Hyrum Wright)

Hyrum Yasası göre, eğer bir API'nin *oldukça büyük sayılabilecek sayıda kullanıcısı* olduğunda, artık bütün sonuçlar ve davranışlar (API sözleşmesinde belirtilmemiş olsalar bile) kullanıcılara göre şekillenecektir. Buna bir örnek olarak bir API'nin tepki süresi olabilir. Daha kapsamlı bir örnek olarak kullanıcıların bir regex ile dönen cevap metninin içinden hatanın *tipini* ayıkladıkları bir senaryoyu düşünelim. API sözleşmesinde bu cevap metinleri ile ilgili bir şey belirtilmemiş olmasına ve kullanıcıların hata kodunu kullanmalarını belirtilmesine rağmen, cevap metnini değiştirmeniz *bazı* kullanıcıların metni kullanmalarından dolayı hata ile karşılaşmalarına sebep olacaktır.

Ek kaynaklar:

- [The Law of Leaky Abstractions](#the-law-of-leaky-abstractions)
- [XKCD 1172](https://xkcd.com/1172/)

### Kernighan Yasası

> Kodda hata ayıklama yapmak, o kodun sıfırdan yazılmasından iki kat daha zordur. Dolayısıyla, yazdığın bir kodu hatasız yazdığını düşünüyorsan, tanım olarak o koddaki hatayı ayıklayacak kadar zeki değilsin demektir. (Brian Kernighan)
> (Brian Kernighan)

Kernighan Yasası adını [Brian Kernighan](https://en.wikipedia.org/wiki/Brian_Kernighan)'dan almıştır ve "[The Elements of Programming Style](https://en.wikipedia.org/wiki/The_Elements_of_Programming_Style)" adlı Kernighan ve Plauger tarafından yazılan kitaptaki bir cümleden türetilmiştir:

> Herkes hata ayıklamanın kodu sıfırdan yazmaktan iki katı daha zor olduğunu bilir. Dolayısıyla, kodu yazarken bütün zekanızı kullanıp elinizden gelenin en iyisini yaptığınızda o koddaki hatayı daha sonra nasıl ayıklayabilirsiniz?

Abartılı olmakla birlikte, Kernighan Yasası karmaşık kod yerine basit kodun tercih edileceği iddiasını ortaya koymaktadır, çünkü karmaşık kodda ortaya çıkan herhangi bir sorunu ayıklamak maliyetli veya hatta mümkün olmayabilir.

Ek kaynaklar:

- [KISS Prensibi](#the-kiss-principle)
- [Unix Felsefesi](#the-unix-philosophy)
- [Occam'ın Usturası](#occams-razor)

### Metcalfe Yasası

[Wikipedia'da Metcalfe Yasası](https://en.wikipedia.org/wiki/Metcalfe's_law)

> Ağ teorisinde, bir sistemin değeri yaklaşık olarak sistemin kullanıcı sayısının karesi ile orantılı olarak büyür.

Bu yasa, bir sistem içindeki muhtemel çift bağlantıların sayısına dayanmaktadır ve [Reed Yasası](#reeds-law) ile yakından ilgilidir. Odlyzko ve diğerleri, hem Reed Yasası hem de Metcalfe Yasası'nın, insan bilişinin ağ etkileri üzerindeki sınırlarını hesaba katmayarak sistemin değerini abarttığını öne sürerler; [Dunbar Sayısı'na](#dunbars-number) bakınız.

Ek kaynaklar:

- [Reed Yasası](#reeds-law)
- [Dunbar Sayısı](#dunbars-number)

### Moore Yasası

[Wikipedia'da Moore Yasası](https://en.wikipedia.org/wiki/Moore%27s_law)

> Entegre devre içerisindeki transistörlerin sayısı yaklaşık olarak iki yılda bir ikiye katlanır.

Çoğu zaman yarı-iletken ve çip teknolojisinin gelişim hızını tahmin etmek için kullanılan Moore yasasının, 1970'lerden 2000'lerin sonlarına doğru oldukça doğru olduğu biliyoruz. Son yıllarda, [komponentlerin küçülmesinde fiziksel sınırlara](https://en.wikipedia.org/wiki/Quantum_tunnelling) ulaşıldığı için bu tahminlemenin tutmadığını da söyleyebiliriz. Ama paralelleştirmede uzmanlaşılması ve yarı-iletken teknolojilerindeki devrim potansiyelindeki değişiklikler Moore Yasası'nın yakın zamanda tekrar doğrulanacağını tahminler yapabileceğini düşünebiliriz.

### Murphy Yasası / Sod Yasası

[Wikipedia'da Murphy Yasası](https://en.wikipedia.org/wiki/Murphy%27s_law)

> Eğer bir işin kötü gitme ihtimali varsa mutlaka kötü gider.

İsmini [Edward A. Murphy, Jr](https://en.wikipedia.org/wiki/Edward_A._Murphy_Jr.)'dan alan *Murphy Yasası* der ki eğer bir işin kötü gitme ihtimali varsa mutlaka kötü gider.

Bu programcılar arasında çok kullanılan bir atasözüdür. Geliştirme yaparken, test ederken ya da canlı sistemlerde çoğunlukla hep beklenmedik sorunlar olur. Bu durum  (İngiltere'de yaygın kullanılan) *Sod Yasası* ile de ilişkilendirilebilir:

> Eğer bir işin kötü gitme ihtimali varsa, olabilecek en kötü zamanda kötüye gidecektir.

Bu iki 'yasa' daha çok espri amaçlı kullanılır. Bunun yanında, [*Doğrulama Önyargısı*](#TODO) ve [*Seçim Tarafgirliği*](#TODO) gibi olgular bu yasaların insanlar tarafında çok fazla vurgulanmasına sebep olabilir (işler yolundayken hiçbirşeye dikkat etmeyiz, ama bunun yanında sorunlar yaşanınca herşey göze batmaya başlar ve tartışılır).

Ek kaynaklar:

- [Doğrulama Önyargısı](#TODO)
- [Seçim Tarafgirliği](#TODO)

### Occam'ın Usturası

[Wikipedia'da Occam'ın Usturası](https://en.wikipedia.org/wiki/Occam's_razor)

> Çözümün elemanları sebep olmaksızın çoğaltılmamalıdır. Ockham'lı William
> Ockham'lı William

Occam'ın usturası, birkaç olası çözüm arasında en olası çözümün, en az sayıda kavram ve varsayımı olan çözüm olduğunu söylüyor. Bu çözüm en basit olandır ve yanlışlıkla ortaya çıkan karmaşıklığa ya da olası olumsuz sonuçlara sebep olmadan sadece verilen sorunu çözer.

Ek kaynaklar:

- [YAGNI](#yagni)
- [Gümüş Bir Mermi Yok: Kazara Oluşan Karmaşıklık ve Gerekli Karmaşıklık](https://en.wikipedia.org/wiki/No_Silver_Bullet)

Örnek:

- [Yalın Yazılım Geliştirme: Çöpü Boşaltın](https://en.wikipedia.org/wiki/Lean_software_development#Eliminate_waste)

### Parkinson Yasası

[Wikipedia'da Parkinson Yasası](https://en.wikipedia.org/wiki/Parkinson%27s_law)

> Bir iş, daima, bitirilmesi için kendisine ayrılan sürenin hepsini kapsayacak şekilde uzar.

Orijinal bağlamında, bu kanun bürokrasi alanındaki çalışmalara dayanıyordu. Kötümser bir bakış açısıyla yazılım geliştirme girişimleri için de söylenebilir. Şöyle ki ekipler genelde proje bitiş tarihi yaklaşana kadar düşük verimde çalışırlar, bitiş tarihi yaklaştıkça bitirmek için yoğun bir çaba içine girerler ve sonuç olarak aslında bitiş tarihini tutturmuş olurlar.

Bu yasa ile [Hofstadter Yasası](#hofstadters-law) birleştirilirse, daha kötümser bir yasaya ulaşılır. Bir iş bitirilmesi için harcanması gereken zamanı kapsar ve *her zaman gecikir*.

Ek kaynaklar:

- [Hofstadter Yasası](#hofstadters-law)

### Olgunlaşmamış Optimizasyon Etkisi

[WikiWikiWeb'de Olgunlaşmamış Optimizasyon Etkisi](http://wiki.c2.com/?PrematureOptimization)

> Vakti gelmeden gelmeden yapılan optimizasyon bütün kötülüklerin anasıdır. [(Donald Knuth)](https://twitter.com/realdonaldknuth?lang=en)
> [(Donald Knuth)](https://twitter.com/realdonaldknuth?lang=en)

Donald Knuth yazdığı [Structured Programming With Go To Statements](http://wiki.c2.com/?StructuredProgrammingWithGoToStatements) isimli makalede, "Programcılar, programlarının kritik olmayan bölümlerinin hızını düşünerek veya endişelenerek çok fazla zaman harcarlar ve bu bakış açısı ile yaptıkları verimlilik geliştirmelerin hata ayıklama ve bakım yapma aşamalarına çok olumsuz etkileri olur. Kesinlikle bu tarz küçük geliştirmeleri (zamanımızın %97'sini harcadığımız) göz ardı etmeliyiz, **Vakti gelmeden yapılan optimizasyon bütün kötülüklerin anasıdır** gerçeğini unutmamalılıyız. Yine de, geride kalan % 3'teki kritik fırsatları kaçırmamalıyız."

Aslında, *olgunlaşmamış optimizasyonu* ihtiyacımızın ne olduğunu bilmeden yapılan optimizasyon olarak tanımlayabiliriz (daha basit kelimelerle).

### Putt Yasası

[Wikipedia'da Putt Yasası](https://en.wikipedia.org/wiki/Putt%27s_Law_and_the_Successful_Technocrat)

> Teknolojide iki tür insan egemendir, yönetmedikleri şeyleri anlayanlar ve anlamadıkları şeyleri yönetenler.

Putt yasasını çoğunlukla Putt sonucu takip eder:

> Her teknik hiyerarşi, zaman içinde bir yetkinlik dönüşümü geliştirir.

Bu iki cümle der ki grupların organiza olma şekillerindeki seçim kıstasları ve eğilimleri yüzünden bir zaman sonra teknik organizasyonun çalışma seviyelerinde bir grup yetenekli insan varken yönettikleri işin karmaşıklığından ve zorluklarından bihaber bir grup insan da yönetim kademelerini işgal edecektir. Bu durum [Peter Prensibi](#the-peter-principle) ya da [Dilbert Prensibi](#the-dilbert-principle) ile de açıklanabilir.

Bununla birlikte, bunun gibi yasaların çok büyük genellemeler olduğu ve *bazı* organizasyon türleri için geçerli olabileceği gibi başkaları için geçerli olmayacağı unutulmamalıdır.

Ek kaynaklar:

- [Peter Prensibi](#the-peter-principle)
- [Dilbert Prensibi](#the-dilbert-principle)

### Reed Yasası

[Wikipedia'da Reed Yasası](https://en.wikipedia.org/wiki/Reed's_law)

> Büyük ağların, özellikle sosyal ağların kullanımı, ağın boyutuna katlanarak ölçeklenir.

Bu yasa, programın faydasının olası katılımcı veya ikili bağlantı sayısından daha hızlı olan olası alt grup sayısı olarak ölçeklendiği grafik teorisine dayanmaktadır. Odlyzko ve diğerleri, Reed Yasası'nın, insan bilişinin ağ etkileri üzerindeki sınırlarını hesaba katarak sistemin yararını abarttığını öne sürerler; [Dunbar Sayısı'na](#dunbars-number) bakınız.

Ek kaynaklar:

- [Metcalfe Yasası](#metcalfes-law)
- [Dunbar Sayısı](#dunbars-number)

### Karmaşıklığın Korunması Yasası (Tesler Yasası)

[Wikipedia'da Karmaşıklığın Korunması Yasası](https://en.wikipedia.org/wiki/Law_of_conservation_of_complexity)

Bu yasa der ki, her sistemde kesinlikle ayıklanamayacak bir miktarda karmaşıklık vardır.

Bir sistem ve yazılımdaki karmaşıklıkların bazıları dikkatsizlik veya yanlışlıktan ortaya çıkar. Bu kötü kurgulanmış yapının, herhangi bir dikkatsizliğin, ya da problemin kötü modellenmesinin sonucu olabilir. Bu tarz karmaşıklıklar giderilebilir ve sistemden ayıklanabilir. Bunun yanında, bazı karmaşıklıklar sistemin gerçekleridir yani sistemin çözmeye çalıştığı problemin doğası gereği ortaya çıkarlar. Bu tarz karmaşıklıklar sistem içinde farklı yerlere taşınabilirler ama sistemden ayıklanmazlar.

O yasanın farklı bir yansıması olarak şöyle düşünülebilir, eğer bir karmaşıklık esastan geliyorsa ve sistem sadeleştirilerek bile ayıklanamıyorsa, daha karmaşık bir şekilde davranması beklenen *kullanıcının tarafına taşınabilir*.

### Demeter Yasası

[Wikipedia'da Demeter Yasası](https://en.wikipedia.org/wiki/Law_of_Demeter)

> Asla yabancılarla konuşma.

"En Az Bilgi İlkesi" olarak da bilinen Demeter Yasası, yazılım tasarımı için, özellikle nesne tabanlı dillerle ilgili bir ilkedir.

Bir yazılım biriminin sadece en yakın işbirlikçileriyle konuşması gerektiğini belirtir. `B` nesnesine bir referansı olan bir `A` nesnesi yöntemlerini çağırabilir, ancak `B` `C` nesnesine bir referansı varsa, `A` `C` yöntemlerini direk çağırmamalıdır. Yani, eğer `C` bir `doThing()` yöntemine sahipse, `A` doğrudan çağırmamalıdır; `B.getC().doThis()`.

Bu ilkeyi izlemek, değişikliklerin kapsamını sınırlayarak gelecekte değiştirmelerin daha kolay ve daha güvenli olmasını sağlar.

### Sızdıran Soyutlamalar Yasası

[Sızdıran Soyutlamalar Yasası, Joel on Software](https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/)

> Önemsiz sayılmayacak bütün soyutlamar belli ölçüde sızıntı içerir. ([Joel Spolsky](https://twitter.com/spolsky))
> ([Joel Spolsky](https://twitter.com/spolsky))

Bu yasa, karmaşık sistemleri sadeleştirmek için kullandığımız soyutlamaların bazı durumlarda soyutlamanın altındaki sistemin öğelerini sorunları ile birlikte sızdırır ve bu da beklenmedik davranışlar ortaya çıkması ile sonuçlanır.

Dosya açma ve okuma işlemlerini örneklemek için kullanabiliriz. Dosya sistemi arayüzleri altta yeralan çekirdek sistemlerinin bir *soyutlamasıdır*, ki çekirdek sistemleri de aslında manyetik plakalardaki (fash disk ya da SDD) veriyi fiziksel olarak değiştiren işlemlerin soyutlamasıdır. Çoğu durumda, bir dosyayı ikili sistemdeki verilerin akışı olarak soyutlamak işe yarar. Manyetik sürücüler sıralı okuma yapıldığında rastgele erişimli sürücülere göre *daha* hızlıdır (sayfalama hatalarının artmasından dolayı) ama bu durum SDD sürücülerle karşılaştırmada geçerli değildir. Bu durumun üstesinden gelmek için, detayların altında yatan bilgileri (yani geliştiricinin bilmesi gereken uygulama detaylarını) soyutlamanın sızdırıyor olacağı dikkate alınmalıdır.

Yukarıda verdiğimiz örnek *daha fazla* soyutlanma göz önünde bulundurulursa daha da karmaşıklaşabilir. Linux işletim sistemi dosyalara bir ağ üzerinden erişilmesine olanak sağlıyor ama bu dosyalar sanki yerel dosyalarmış gibi gösterilir. Bu soyutlama da eğer bir network sorunu olursa sızıntı oluşturur. Eğer bir uygulama geliştirici bu tür dosyaları normal dosyalarmış gibi düşünerek geliştirme yaparsa, ağızda oluşan herhangi bir gecikme ya da sorun çözümü sorunlu hale getirecektir.

Yasa savunmaya çalıştığı durum, herhangi bir soyutlamaya çok fazla güvenmenin alta yatan işlemleri de tam anlamamayla birleşince çözülmeye çalışılan problemin çoğunlukla *daha da* karmaşıklaşması ile sonuçlanacağıdır.

Ek kaynaklar:

- [Hyrum Yasası](#hyrums-law-the-law-of-implicit-interfaces)

Gerçek dünyadan örnekler:

- [Photoshop'taki yavaş açılma problemi](https://forums.adobe.com/thread/376152): Photoshop bir zamanlar çok yavaş açılırdı, hatta bazen açılması dakikalar sürerdi. Sorunun sebebi program her başlangıçta ön tanımlı yazıcı ile ilgili belli bilgileri çekmeye çalışması olarak gözüküyordu. Eğer yazıcı bir ağ yazıcısıysa açılma daha da uzun sürüyordu. Ağ yazıcılarının yerel yazıcıları gibi *soyutlanması* kullanıcılara bu kötü deneyimi yaşatmış oldu.

### Önemsizlik Yasası

[Wikipedia'da Önemsizlik Yasası](https://en.wikipedia.org/wiki/Law_of_triviality)

Bu yasa diyor ki, ekipler önemsiz ve kozmetik sorunlara ciddi ve önemli sorunlara göre daha fazla zaman harcarlar.

En çok kullanılan kurgu örnek nükleer enerji reaktörünü onaylayacak olan komitenin reaktörün genel tasarımını onaylama zamanından çok bisiklet parkının tasarımını onaylamak için zaman harcamasıdır. Çok büyük ve karmaşık konularla ilgili o alanda bir eğitime, tecrübeye ve hazırlığa sahip olmadan kayda değer yorum getirmek zordur. İnsanlar genelde değerli katkılar verdiklerinin görülmesini isterler. Dolayısıyla insanlar kolayca katkı verebilecekleri gerekli ve önemli olmasa bile küçük detaylara odaklanma eğilimi gösterirler.

Bu kurgu örnek 'Bike Shedding' diye bir deyimin yaygınlaşmasına sebep olmuştur. Türkçe'deki 'pire için yorgan yakmak' ya da 'attığın taş ürküttüğün kurbağaya değsin' gibi deyimlere benzer. Alternatif bir terim 'Yak Shaving' de kullanılmaktadır.

### Unix Felsefesi

[Wikipedia'da Unix Felsefesi](https://en.wikipedia.org/wiki/Unix_philosophy)

Unix felsefesi şöyle özetlenebilir; bir yazılım parçası olabildiğince küçük olmalı ve sadece bir işi yapmaya odaklanmalıdır. Bu felsefeye uymak sistemleri büyük, karmaşık ve çok amaçlı programlarla oluşturmak yerine küçük, basit ve iyi tanımlanmış parçalardan daha kolayca oluşturmayı sağlar.

Modern yaklaşımlardan biri olan 'Mikro-service Mimarisi' de bu felsefenin uygulaması olarak düşünülebilir. Çünkü bu mimari ile servislerin küçük, amaç odaklı ve tek bir iş yapacak şekilde geliştirilmesi ve karmaşık yapıların küçük basit bloklar halinde oluşturulması hedefleniyor.

### Spotify Modeli

[Spotify Modeli, Spotify Labs](https://labs.spotify.com/2014/03/27/spotify-engineering-culture-part-1/)

Spotify Modeli Spotify'daki uygulamasından dolayı popüler olmuş ekip ve organizasyon yapıları için yeni bir yaklaşımdır. Model basitçe ekiplerin teknolojilere göre değil de özellikler etrafında organize edilmesidir.

Spotify Modeli kabileler (Tribes), birlikler (Guilds) ve kısımlar (Chapter) gibi organizasyon yapısında kullanılacak öğeleri de yaygın hale getirdi.

Organizasyonun üyeleri bu grupların gerçek anlamlarının zamanla değiştiğini, geliştiğini ve bunun devam eden bir deney olduğunu söylüyorlar. Modelin sabit bir modelden ziyade *hareket halinde bir süreç * olması, yapının değişen yorumlarına yol açmaya devam etmektedir (konferanslarda konuyla ilgili yapılan sunumlarına dayanarak söyleyebiliriz). Bu, 'anlık görüntülerin' üçüncü taraflar tarafından *sabit bir yapı * olarak yeniden paketlenebileceği anlamına gelir ve modelin dinamikliğinin kaybolmasına sebep olabilir.

### Wadler Yasası

[Wadler Yasası, wiki.haskell.org](https://wiki.haskell.org/Wadler's_Law)

> Herhangi bir programlama dilini tasarlarken, aşağıdaki listedeki herhangi bir özelliği tartışmak için harcanan zaman iki üzeri özelliğin listeki sırası ile doğru orantılıdır.
> 1. Semantik
> 2. Genel sözdizimi
> 3. Sözcük sözdizimi
> 4. Yorumlardaki sözcük sözdizimi (Kısaca semantic için harcanan her bir saat için yorumlardaki sözcük sözdizimi için sekiz saat harcanacaktır).
> (Kısaca semantic için harcanan her bir saat için yorumlardaki sözcük sözdizimi için sekiz saat harcanacaktır).

[Önemsizlik Yasasında](#the-law-of-triviality) öne sürülene benzer olarak, Wadler Yasası yeni bir programlama dili tasarlanırken konunun önemi ile o konu için harcanan zaman ters orantılı olduğunu söylüyor.

Ek kaynaklar:

- [Önemsizlik Yasası](#the-law-of-triviality)

### Wheaton Yasası

[Link](http://www.wheatonslaw.com/)

[Resmi Gün](https://dontbeadickday.com/)

> Öküzlük yapmayın. *Wil Wheaton* *Wil Wheaton*
> *Wil Wheaton*

Wil Wheaton (Star Trek: The Next Generation, The Big Bang Theory) tarafından oluşturulan bu basit, özlü ve güçlü yasa, profesyonel bir organizasyon içinde uyum ve saygının artmasını amaçlamaktadır. İş arkadaşlarınızla konuşurken, kod incelemeleri yaparken, diğer bakış açılarını öne sürerken, insanları eleştirirken ve genel olarak insanların birbirleriyle olan profesyonel etkileşimlerinin çoğunda uygulanabilir.

## Prensipler

Prensiplerin genellikle tasarıma ilişkin rehberlerdir.

### Ölü Deniz Etkisi

[Bruce F. Webster'e göre Ölü Deniz Etkisi](http://brucefwebster.com/2008/04/11/the-wetware-crisis-the-dead-sea-effect/)

> "... [E]n yetenekli ve verimli BT mühendisleri şirketleri terketmeye en yakın olanlardır, [kalıcı olma taraftarı olanlar] ise tortuya (daha az yetenekli ve verimsiz) benzetilebilir" *Bruce F. Webster*
> *Bruce F. Webster*

"Ölü Deniz Etkisi" bir organizasyonda mühendislerin becerilerinin/yeteneklerinin/verimliliklerinin  sıklıkla o organizasyonda harcadıkları zamanla ters orantılı olduğunu söyler.

Genellikle, yüksek vasıflı mühendisler başka yerlerde iş bulması kolay kolay olan ve bunu ilk yapan kişilerdir. Eskimiş veya zayıf becerilere sahip mühendisler, başka bir yerde iş bulmak zor olduğu için şirkette kalma eğilimindedir. Bu, özellikle şirketteki zamanları boyunca artan ücret artışları elde ettikleri takdirde de geçerlidir, çünkü başka bir yerde eşdeğer ücret almaları zor olabilir.

### Dilbert Prensibi

[Wikipedia'da Dilbert Prensibi](https://en.wikipedia.org/wiki/Dilbert_principle)

> Şirketler, yetersiz çalışanları, iş akışından uzaklaştırmak için sistematik olarak yönetici olmaya teşvik etme eğilimindedir. *Scott Adams*
> *Scott Adams*

Scot Adams (Dilbert çizgi dizisinin yazarı) [Peter prensibinden](#the-peter-principle) esinlenerek ortaya atılmış bir yönetim kavramıdır. Dilbert prensibine göre yetenekli olmayan çalışanlar yönetim kadorlarına doğru yükseltilirler ki üretime verecekleri zarar aza indirilsin. Adams bunu ilk olarak 1995'te Wall Street Journal'da yazdığı bir makalede açıkladı daha sonra ise 1996'da yazdığı [Dilbert Prensibi](#reading-list) adlı kitabında detaylandırdı.

Ek kaynaklar:

- [Peter Prensibi](#the-peter-principle)
- [Putt Yasası](#putts-law)

### Pareto Prensibi (80/20 Kuralı)

[Wikipedia'da Pareto Prensibi](https://en.wikipedia.org/wiki/Pareto_principle)

> Hayattaki çoğu şey eşit dağılmaz.

Pareto Prensibi der ki, çıktıların önemli bir çoğunluğu girdilerin çok azı tarafından oluşturulur:

- Bir yazılımın 80%'i harcanan zamanın %20'sinde yazılır (bir başka deyişle, kodun en zor %20'lik bölümü haracanan zamanın %80'inde yazılır)
- Harcanan eforun %20'si sonucun %80'ini oluşturur
- Yapılan işin %20'si gelirin %80'ini oluşturur
- Koddaki hataların %20'si sistem sorunlarının %80'ini oluşturur
- Özelliklerin %20'si hizmetin %80'ini oluşturur

1940'lı yıllarda Romanya kökenli Amerikalı mühendis Dr. Joseph Juran, kendisi kalite kontrolün babası olarak nitelendirilir, [kalite kontrol sorunlarında Pareto Prensibini kullanmaya başladı](https://en.wikipedia.org/wiki/Joseph_M._Juran).

Bu prensip aynı zamanda 80/20 Kuralı (The Law of the Vital Few and The Principle of Factor Sparsity) olarak da bilinir.

Gerçek dünyadan örnekler:

- 2002'de Microsoft en çok rapor edilen hataların üstten %20'sini çözünce kullanıcıların yaşadığı sorunların %80'inin çözüldüğünü gözlemlemiş ([Referans](https://www.crn.com/news/security/18821726/microsofts-ceo-80-20-rule-applies-to-bugs-not-just-features.htm)).

### Peter Prensibi

[Wikipedia'da Peter Prensibi](https://en.wikipedia.org/wiki/Peter_principle)

> Hiyerarşideki insanlar “yetersizlik seviyelerine” göre yükselme eğilimindedir. *Laurence J. Peter* *Laurence J. Peter*
> *Laurence J. Peter*

Laurence J. Peter tarafından geliştirilen bir yönetim konsepti olan Peter Prensibi, işlerinde iyi olan kişilerin, artık başarılı olamadıkları bir seviyeye (kendi "yetersizlik seviyelerine") ulaşana kadar terfi ettiğini gözlemlemektedir. Bu durumda şirket içinde çok tecrübeli olduklarından organizasyondan (çok aykırı birşey yapmadıkları sürece) dışlanmazlar ve az sayıda temel beceriye sahip olacakları bir rolde kalmaya devam edecekler, çünkü onları başarılı kılan orijinal becerileri mutlaka bu yeni rolleri için gereken beceriler değildir.

Bu, temelde farklı bir beceri kümesi gerektirdiğinden özellikle mühendislerle - kariyerine teknik rollerle başlayan ama sonra kariyer değiştirip diğer mühendisleri *yönetmeye* başlayan -  alakalıdır.

Ek kaynaklar:

- [Dilbert Prensibi](#the-dilbert-principle)
- [Putt Yasası](#putts-law)

### Dayanıklılık Prensibi (Postel Yasası)

[Wikipedia'da Dayanıklılık Prensibi](https://en.wikipedia.org/wiki/Robustness_principle)

> Yaptıklarınızda muhafazakar olun, başkalarından kabul ettiğiniz şeyler konusunda liberal olun.

Genellikle sunucu uygulamaları geliştirirken uygulanabilir. Bu prensip der ki; kendi uygulamanızdan dışarıya veri gönderirken kılı kırk yararcasına dikkatli olun ama dışardan veri alırken mümkün olabilecek her durumda veriyi kabul etmeye çalışın.

Bu prensibin amacı dayanıklı sistemlere geliştirmektir ve bu sistemler kötü yapılandırılmış girdileri bile anlayabildikleri durumda işleyebilmeliler. Bunun güvenlik açısından kötü amaçlı ve yeterince kontrol edilmemiş girdileri kabul etmek anlamına gelebileceği için riskli olduğu düşünülebilir. Tabiki bu riskin de göz önünde bulundurulması gerekir.

Uygun olmayan girdilere zaman içinde izin verilmesi, uygulayıcıların yeni özellikler oluştururken bu serbestliğe güvenmesini sağlayacağından en sonunda protokollerin evrimleşme yeteneğini zayıflatabilir.

Ek kaynaklar:

- [Hyrum Yasası](#hyrums-law-the-law-of-implicit-interfaces)

### SOLID

SOLID aşağıdaki beş prensibin baş harflerinden oluşan bir kısaltmadır;

- S: [Tek Sorumluluk Prensibi - The Single Responsibility Principle](#the-single-responsibility-principle)
- O: [Açık/Kapalı Prensibi - The Open/Closed Principle](#the-openclosed-principle)
- L: [Liskov Yerine Geçme Prensibi - The Liskov Substitution Principle](#the-liskov-substitution-principle)
- I: [Arayüz Ayrım Prensibi - The Interface Segregation Principle](#the-interface-segregation-principle)
- D: [Bağımlılığın Ters Çevrilmesi - The Dependency Inversion Principle](#the-dependency-inversion-principle)

Bunları [Nesne Tabanlı Proglamlama'nın](#todo) temel prensipleri olarak değerlendirilebilir ve bu prensiplerin programcılara geliştirilebilir ve desteklenebilir sistemler geliştirmelerinde yardımcı oldukları kesindir.

### Tek Sorumluluk Prensibi

[Wikipedia'da Tek Sorumluluk Prensibi](https://en.wikipedia.org/wiki/Single_responsibility_principle)

> Her sistem parçasının ya da programlama sınıfının sadece bir sorumluluğu olmalı.

Bu '[SOLID](#solid)' prensiplerinin ilkidir. Bu prensip der ki her bir sistem parçasının yada programlama sınıfının sadece ama sadece bir sorumluluğu olması gerekir. Daha sade anlatmak gerekirse, bir programdaki sadece bir özelliği etkileyen bir değişiklik sadece o özelliği ilgilendiren parça ya da sınıfta yapılmalı. Örneğin, şifrelerin doğruluğunun kontrolünde bir değiştirme yapılacaksa sadece programın o bölümünde değişiklik yapılmalı.

Teorik olarak, bu prensibe uygun yazılmış kodlar daha sağlam ve değiştirilmesi kolaydır. Sadece tek bir parçanın değiştirildiğine emin olunduğunda değişimi *test etmek* de kolay olacaktır. Önceki şifre örneğini düşünürsek, şifrenin zorluk seviyesi değiştirildiğinde sadece şifre ilgili bölümlerin etkilenecektir. Birden fazla sorumluluğu olan bir bölümde olan değişikliğin nereleri etkileceğini hesaplamak daha zordur.

Ek kaynaklar:

- [Nesne Tabanlı Programlama](#todo)
- [SOLID](#solid)

### Açık/Kapalı Prensibi

[Wikipedia'da Açık/Kapalı Prensibi](https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle)

> Her sistem parçası (sınıf, modül, fonksiyon vs) genişletilmeye (türev alınmaya, miras alınma vs) açık olmalı ama değiştirilmeye (modifiye etme) kapalı olmalı.

Bu '[SOLID](#solid)' prensiplerinin ikincisidir ve herhangi bir sistem parçasının *mevcut* davranışının değiştirilememesini ama kullanılarak/türetilerek *genişletilebilmesinin* gerekliliğini savunur.

Örneğin Markdown formatındaki belgeleri HTML formatına çeviren bir modülü düşünelim. Eğer bu modül kendisi değiştirilmeden yeni bir Markdown formatını da işlemesi sağlanacak şekilde geliştirilebiliyorsa, bu modül genişletilmeye açık demektir. Eğer sonradan değiştirilip Markdown formatı işlemesi ile ilgili geliştirme *yapılamıyorsa*, bu modül değiştirilmeye *kapalı* demektir.

Bu prensip nesne-tabanlı programlamaya tam uygundur. Şöyle ki, kendi nesne ve sınıflarımızı miras alınarak geliştirmeye uygun ve değiştirmeye ihtiyaç duymayacak şekilde tasarlarsak ve yazarsak nesne-tabanlı programlamaya tam uygun kod yazmış oluruz.

Ek kaynaklar:

- [Nesne Tabanlı Programlama](#todo)
- [SOLID](#solid)

### Liskov Yerine Geçme Prensibi

[Wikipedia'da Liskov Yerine Geçme Prensibi](https://en.wikipedia.org/wiki/Liskov_substitution_principle)

> Bir sistemde var olan bir özellik kendinden türetilmiş türetilmiş bir özellikle herhangi bir sistemsel soruna sebep olmadan yer değiştirilebilmeli.

'[SOLID](#solid)' prensiplerinin üçüncüsüdür. Bu prensibe göre herhangi bir bileşenin üzerine dayandığı bir özelliği (sınıf vs) o özelliklikten türetilmiş alt özellikle değiştirebilmeliyiz ve bu durumda bir sistem sorununa neden olunmaz ya da alt özelliğin bütün detaylarını bilmeye gerek kalmaz.

Örneğin dosyayı temsil eden bir yapıdan XML verisi okuyan bir metod düşünelim. Eğer bu metod 'dosya' tipini kullanıyorsa, 'dosya' tipinden türeyen bütün tipleri de kullanabilmelidir. Eğer 'dosya' tipi geriye dönük aramayı destekliyorsa ama 'dosya' tipinden türetilmiş 'ağ dosyası' tipi bunu desteklemiyorsa o zaman 'ağ dosyası' tipi bu prensibi ihlal ediyor demektir.

Bu prensip nesne-tabanlı programlamanın bağlı olduğu prensiplerden biridir ve geliştiricilerin kafasını karıştırmamak için sınıf hiyerarşisinin dikkatli tarasarlanması gerektiğini söyler.

Ek kaynaklar:

- [Nesne Tabanlı Programlama](#todo)
- [SOLID](#solid)

### Arayüz Ayrım Prensibi

[Wikipedia'da Arayüz Ayrım Prensibi](https://en.wikipedia.org/wiki/Interface_segregation_principle)

> Hiçbir kullanıcı/müşteri/istemci, kullanmadığı yöntemlere bağlı kalmamalıdır.

'[SOLID](#solid)' prensiplerinin dördüncüsüdür ve bir bileşenin kullanıcılarının, kullanmadığı bir bileşenin işlevlerine bağımlı olmaması gerektiğini belirtir.

Örnek olarak dosyayı temsil eden bir yapıdan XML verisi okuyan bir metod düşünelim. Bu metod sadece dosyadan byte byte veri okumalı ve dosya içinde ileri ya da geri hareket etmeli. Eğer bu method dosya okuma dışında (dosya izinleri değişimi gibi) herhangi bir özellik değişiminden dolayı güncellenmek zorunda kalınıyorsa bu prensip ihlal edilmiş demektir.

Bu prensip de nesne-tabanlı programlama ile direk ilişkilidir. 'interface' yapıları, sınıf hiyerarşileri ve soyut türler farklı bileşenler arası bağımlığı en aza indirmek için kullanılır. Duck typing de bu prensibi uygulamaya yardımcı olur.

Ek kaynaklar:

- [Nesne Tabanlı Programlama](#todo)
- [SOLID](#solid)
- [Duck Typing](#todo)
- [Ayrışma](#todo)

### Bağımlılığın Ters Çevrilmesi

[Wikipedia'da Bağımlılığın Ters Çevrilmesi](https://en.wikipedia.org/wiki/Dependency_inversion_principle)

> Yüksek seviye modülleri, düşük seviye uygulamalarına bağlı olmamalıdır.

'[SOLID](#solid)' prensiplerin beşincisidir. Bu ilke, daha üst seviye bileşenlerinin bağımlılıklarının ayrıntılarını bilmek zorunda olmadıklarını belirtir.

Örnek olarak bir web sitesinden metadata okuyan bir program düşünelim. Bu programın ana bileşeninin web sitesinden içeriği indiren ve metadayı okuyan bileşenlerinden ne yaptığından haberdar olması gerekir. Eğer bu prensibe uyarsak ana bileşenin byte verisi okuyan ve byte verisinden metada çıkaran soyutlamalara bağımlı olması lazım. Ana bileşenin TCP/IP, HTTP ya da HTML hakında bir detaya hakim olmasına gerek yoktur.

Bu prensip olması gereken bağımlığı tersine çevirdiği düşünebileceğinden (isminden dolayı) biraz karmaşık gelebilir. Pratikte, ayrı bir düzenleme bileşeninin, soyut türlerin doğru uygulamalarının kullanılmasını sağlaması gerektiği anlamına gelir (önceki örnekte, *bir şey* hala meta veri okuyucu bileşenine bir HTTP dosyası indiricisi ve HTML meta etiketi okuyucu sağlamalıdır). Bu prensip aynı zamanda [Kontrolün Ters Çevirilmesi](#todo) ve [Bağımlık Enjeksiyonu](#todo) gibi konularla da bağlantılıdır.

Ek kaynaklar:

- [Nesne Tabanlı Programlama](#todo)
- [SOLID](#solid)
- [Bağımlılığın Ters Çevrilmesi](#todo)
- [Bağımlılık Enjeksiyonu](#todo)

### DRY Prensibi

[Wikipedia'da DRY Prensibi](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)

> Her bilgi parçasının bir sistem içinde tek, açık ve net bir temsiline sahip olması gerekir.

*DRY Don't Repeat Yourself* yani Kendini Tekrar Etme deyimin kısaltılmasıdır. İlk olarak Andrew Hunt ve Dave Thomas tarafından [The Pragmatic Developer](https://en.wikipedia.org/wiki/The_Pragmatic_Programmer) kitabında bahsedilmiştir. Bu ilke, geliştiricilere kod tekrarını azaltma ve bilgileri tek bir yerde tutmalarına yardımcı olmayı amaçlamaktadır.

> DRY'nin tam tersi *WET* olacaktır (Write Everything Twice (Her Şeyi İki Kez Yaz) We Enjoy Typing (Yazmayı Seviyoruz)).

Uygulamada, aynı bilgi parçasını iki (veya daha fazla) farklı yerde kullanıyorsanız, DRY'yi bunları tek bir tanede birleştirmek ve istediğiniz / ihtiyaç duyduğunuz yerde tekrar kullanmak için kullanabilirsiniz.

Ek kaynaklar:

- [The Pragmatic Developer](https://en.wikipedia.org/wiki/The_Pragmatic_Programmer)

### KISS prensibi

[Wikipedia'da KISS](https://en.wikipedia.org/wiki/KISS_principle)

> Olabildiğince basit ve aptal (Keep it simple, stupid)

KISS prensibi, çoğu sistemin karmaşıklaştırılmak yerine basit tutulması durumunda en iyi şekilde çalışacağını belirtir; bu nedenle sadelik tasarımda kilit bir amaç olmalı ve gereksiz karmaşıklıktan kaçınılmalıdır. Bu 1960’da ABD Donanması’nda çalışan uçak mühendisi Kelly Johnson ile ilişkilendirilen bir cümle.

Prensip, Johnson'ın bir tasarım mühendisleri ekibine bir avuç el aleti teslim etmesinin öyküsüyle en iyi örneklenmiştir, tasarladıkları jet uçağının sahadaki ortalama bir tamirci tarafından yalnızca bu aletlerle mücadele koşullarında tamir edilebilir olması zorunluluğu ile karşı karşıyadır. Bu nedenle, "aptal" kelimesi mühendislerin kendi yeteneklerini değil, işlerin kırılma şekli ile onları tamir etmek için mevcut araçların karmaşıklığı arasındaki ilişkiyi ifade eder.

Ek kaynaklar:

- [Gall Yasası](#galls-law)

### YAGNI

[Wikipedia'da YAGNI](https://en.wikipedia.org/wiki/You_ain%27t_gonna_need_it)

***Y**ou **A**ren't **G**onna **N**eed **I**t* (İhtiyacın olmayacak) deyiminin kısaltmasıdır.

> İhtiyaç duyduğunuz şeyleri her zaman ihtiyaç duyduğunuzda geliştirin, onlara ihtiyacınız olacağını düşündüğünüzde değil. ([Ron Jeffries](https://twitter.com/RonJeffries)) (XP co-founder and author of the book "Extreme Programming Installed")
> ([Ron Jeffries](https://twitter.com/RonJeffries)) (XP co-founder and author of the book "Extreme Programming Installed")

Bu *Aşırı Programlama* (XP) ilkesi, geliştiricilerin yalnızca acil gereksinimler için gerekli olan işlevleri yerine getirmeleri gerektiğini ve daha sonra ihtiyaç duyulabilecek işlevleri uygulayarak geleceği tahmin etme girişimlerinden kaçınmalarını önerir.

Bu ilkeye bağlı kalmak, kod tabanındaki kullanılmayan kod miktarının ve hiçbir değer getirmeyen işlevlerde haracanan zamanın ve çabanın azalmasını sağlayacaktır.

Ek kaynaklar:

- [Reading List: Extreme Programming Installed](#reading-list)

### Dağıtık Sistemlerin Yanılgıları

[Wikipedia'da Dağıtık Sistemlerin Yanılgıları](https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing)

*Ağ Tabanlı Sistemlerin Yanılgıları* olarak da bilinen yanılgılar dağıtık sistemleri geliştirme sırasında başarısızlıklara yol açabilecek varsayımların (veya inançların) bir listesidir. Varsayımlar:

- Ağ güvenilirdir.
- Gecikme yoktur.
- Bant genişliği sonsuzdur.
- Ağ güvenlidir.
- Topoloji değişmez.
- Sadece bir tane yönetici vardır.
- Taşıma maaliyeti sıfırdır.
- Ağ homojendir.

İlk dört madde 1991'de [Bill Joy](https://en.wikipedia.org/wiki/Bill_Joy) ve [Tom Lyon](https://twitter.com/aka_pugs) tarafından listelenmiştir ve ilk önce [James Gosling](https://en.wikipedia.org/wiki/James_Gosling) tarafından "Ağ Tabanlı Sistemlerin Yanılgıları" olarak sınıflandırılmıştır. [L. Peter Deutsch](https://en.wikipedia.org/wiki/L._Peter_Deutsch)  5., 6. ve 7. yanılgıları ekledi. 90'lı yılların sonlarında Gosling 8. yanılgıyı ekledi.

Grup [Sun Microsystems](https://en.wikipedia.org/wiki/Sun_Microsystems) içinde başlarına gelen olaydan ilham aldı.

Dayanıklı sistemler tasarlarken bu yanılgılar dikkatlice ele alınmalı; bu yanılgılardan herhangi birinin varsayılması, dağıtılmış sistemlerin gerçeklikleri ve karmaşıklıkları ile başa çıkamayan hatalı bir mantığa yol açabilir.

Ek kaynaklar:

- [Foraging for the Fallacies of Distributed Computing (Part 1) - Vaidehi Joshi on Medium](https://medium.com/baseds/foraging-for-the-fallacies-of-distributed-computing-part-1-1b35c3b85b53)
- [Deutsch's Fallacies, 10 Years After](http://java.sys-con.com/node/38665)

## Ek Kaynaklar

Bu kavramları ilginç bulduysanız, aşağıdaki kitapların keyfini çıkarabilirsiniz.

- [Extreme Programming Installed - Ron Jeffries, Ann Anderson, Chet Hendrikson](https://www.goodreads.com/en/book/show/67834) - Extreme Programming kavramının temel prensiplerini içerir.
- [The Mythical Man Month - Frederick P. Brooks Jr.](https://www.goodreads.com/book/show/13629.The_Mythical_Man_Month) - Yazılım mühendisliği klasiği sayılabilir. Brooks Yasası bu kitabın ana temasıdır.
- [Gödel, Escher, Bach: An Eternal Golden Braid - Douglas R. Hofstadter.](https://www.goodreads.com/book/show/24113.G_del_Escher_Bach) - Sınıflandırması zor bir kitap. Hofstadter Yasası bu kitaptan alıntıdır.
- [Dilbert Prensibi - Scott Adams](https://www.goodreads.com/book/show/85574.The_Dilbert_Principle) - [Dilbert İlkesini](#the-dilbert-principle) oluşturan yazardan, kurumsal Amerika'ya komik bir bakış.
- [The Peter Principle - Lawrence J. Peter](https://www.goodreads.com/book/show/890728.The_Peter_Principle) - Another comic look at the challenges of larger organisations and people management, the source of [The Peter Principle](#the-peter-principle).

## Çeviriler:

Katkıda bulunan harika insanlar sayesinde Hacker Laws birçok dilde mevcuttur. Lütfen çeviri sahiplerine de sponsor olmayı düşünün!

Dil | Moderatör | Durum
--- | --- | ---
[🇮🇩 Bahasa Indonesia / Indonesian](./translations/pt-BR.md) | [arywidiantara](https://github.com/arywidiantara) | [](https://gitlocalize.com/repo/2513/id?utm_source=badge)![gitlocalized ](https://gitlocalize.com/repo/2513/id/badge.svg)
[🇧🇷 Brasileiro / Brazilian](./translations/pt-BR.md) | [Leonardo Costa](https://github.com/leofc97) | [](https://gitlocalize.com/repo/2513/id?utm_source=badge)![gitlocalized ](https://gitlocalize.com/repo/2513/id/badge.svg)
[🇨🇳 中文 / Chinese](https://github.com/nusr/hacker-laws-zh) | [Steve Xu](https://github.com/nusr) | Kısmen tamamlandı
[🇩🇪 Deutsch / German](./translations/de.md) | [Vikto](https://github.com/viktodergunov) | [](https://gitlocalize.com/repo/2513/lv?utm_source=badge)[](https://gitlocalize.com/repo/2513/tr?utm_source=badge)![gitlocalized ](https://gitlocalize.com/repo/2513/tr/badge.svg)[![gitlocalized ](https://gitlocalize.com/repo/2513/lv/badge.svg)](https://gitlocalize.com/repo/2513/lv?utm_source=badge)
[🇫🇷 Français / French](./translations/fr.md) | [Kevin Bockelandt](https://github.com/KevinBockelandt) | [](https://gitlocalize.com/repo/2513/tr?utm_source=badge)![gitlocalized ](https://gitlocalize.com/repo/2513/tr/badge.svg)
[🇬🇷 ελληνικά / Greek](./translations/el.md) | [Panagiotis Gourgaris](https://github.com/0gap) | [](https://gitlocalize.com/repo/2513/ja?utm_source=badge)[](https://gitlocalize.com/repo/2513/lv?utm_source=badge)![gitlocalized ](https://gitlocalize.com/repo/2513/lv/badge.svg)[![gitlocalized ](https://gitlocalize.com/repo/2513/ja/badge.svg)](https://gitlocalize.com/repo/2513/ja?utm_source=badge)
[🇮🇹 Italiano / Italian](https://github.com/csparpa/hacker-laws-it) | [Claudio Sparpaglione](https://github.com/csparpa) | Kısmen tamamlandı
[🇯🇵 JP 日本語 / Japanese](./translations/jp.md) | [Fumikazu Fujiwara](https://github.com/freddiefujiwara) | [](https://gitlocalize.com/repo/2513/fr?utm_source=badge)![gitlocalized ](https://gitlocalize.com/repo/2513/fr/badge.svg)
[🇰🇷 한국어 / Korean](https://github.com/codeanddonuts/hacker-laws-kr) | [Doughnut](https://github.com/codeanddonuts) | Kısmen tamamlandı
[🇱🇻 Latviešu Valoda / Latvian](./translations/lv.md) | [Arturs Jansons](https://github.com/iegik) | [](https://gitlocalize.com/repo/2513/de?utm_source=badge)![gitlocalized ](https://gitlocalize.com/repo/2513/de/badge.svg)
[🇷🇺 Русская версия / Russian](https://github.com/solarrust/hacker-laws) | [Alena Batitskaya](https://github.com/solarrust) | Kısmen tamamlandı
[🇪🇸 Castellano / Spanish](./translations/es-ES.md) | [Manuel Rubio](https://github.com/manuel-rubio) ([Sponsor](https://github.com/sponsors/manuel-rubio)) | Kısmen tamamlandı
[🇹🇷 Türkçe / Turkish](https://github.com/umutphp/hacker-laws-tr) | [Umut Işık](https://github.com/umutphp) | [](https://gitlocalize.com/repo/2513/id?utm_source=badge)![gitlocalized ](https://gitlocalize.com/repo/2513/id/badge.svg)

Bir çeviriyi güncellemek isterseniz, [bir PR açmanız yeterlidir](https://github.com/dwmkerr/hacker-laws/pulls) . Yeni bir dil eklemek istiyorsanız, bir hesap oluşturmak için [GitLocalize'a](https://gitlocalize.com/) giriş yapın, ardından dili yönetmek istediğinizi belirten bir Issue açın; sizi projeye ekleyeceğim! Yukarıdaki tabloyu güncelleyen bir PR açabilmeniz de çok yararlı olacaktır.

## İlgili Projeler

- [Tip of the Day](https://tips.darekkay.com/html/hacker-laws-en.html) - Hergün bir hacker yasası ya da prensibi.
- [Hacker Laws CLI](https://github.com/umutphp/hacker-laws-cli) - Terminalden yasaları listeleyin, ve rastgele bir yasa görüntüleyin!

## Katkıda Bulunmak İçin

Lütfen katkıda bulunun! Bir ekleme veya değişiklik önermek istiyorsanız [bir sorun oluşturun](https://github.com/dwmkerr/hacker-laws/issues/new) veya kendi değişikliklerinizi önermek için [bir PR açın](https://github.com/dwmkerr/hacker-laws/compare) .

Lütfen metin, stil ve benzeri gereksinimler için [Katkıda Bulunma Kılavuzunu](./.github/contributing.md) okuduğunuzdan emin olun. Lütfen projeyle ilgili tartışmalarda [Davranış Kurallarına](./.github/CODE_OF_CONDUCT.md) dikkat edin.

## TODO

Selam!. Buraya ulaştıysanız, henüz yazmadığım bir konunun bağlantısını tıkladınız, bunun için üzgünüm - ve en kısa zamanda tamamlamaya çalışacağım!

Soru ve önerileriniz için [issue](https://github.com/dwmkerr/hacker-laws/issues) açabilirsiniz, ya da katkıda bulunmak isterseniz [Pull Request](https://github.com/dwmkerr/hacker-laws/pulls) açabilirsiniz.
