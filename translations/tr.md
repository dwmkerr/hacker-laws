# 💻📖 hacker-laws

Programcıların faydalı bulacağı yasalar, teoriler, prensipler ve desenler.

- 🇨🇳 [中文 / Çince İçin](https://github.com/nusr/hacker-laws-zh) - Teşekkürler [Steve Xu](https://github.com/nusr)!
- 🇮🇹 [Italyanca için](https://github.com/csparpa/hacker-laws-it) - Teşekkürler [Claudio Sparpaglione](https://github.com/csparpa)!
- 🇰🇷 [한국어 / Korece İçin](https://github.com/codeanddonuts/hacker-laws-kr) - Teşekkürler [Doughnut](https://github.com/codeanddonuts)!
- 🇷🇺 [Русская версия / Rusça İçin](https://github.com/solarrust/hacker-laws) - Teşekkürler [Alena Batitskaya](https://github.com/solarrust)!
- 🇹🇷 [Türkçe / Turkçe İçin](https://github.com/umutphp/hacker-laws-tr) - Teşekkürler [Umut Işık](https://github.com/umutphp)
- 🇧🇷 [Brasileiro / Brezilyaca İçin](./translations/pt-BR.md) - Teşekkürler [Leonardo Costa](https://github.com/LeoFC97)

Bu projeyi beğendiniz mi? Lütfen [sponsorluk olmayı](https://github.com/sponsors/dwmkerr) düşünün!

---

<!-- vim-markdown-toc GFM -->

- [Giriş](#introduction)
- [Yasalar](#laws)
    - [Amdahl Yasası](#amdahls-law)
    - [Brooks Yasası](#brooks-law)
    - [Conway Yasası](#conways-law)
    - [Cunningham Yasası](#cunninghams-law)
    - [Dunbar Sayısı](#dunbar-say%C4%B1s%C4%B1)
    - [Gall Yasası](#galls-law)
    - [Hanlon'un Usturası](#hanlons-razor)
    - [Hofstadter Yasası](#hofstadters-law)
    - [Hutber Yasası](#hutbers-law)
    - [Hype Döngüsü ve Amara Yasası](#the-hype-cycle--amaras-law)
    - [Hyrum Yasası (Arabirimlerin Örtülü Hukuku)](#hyrums-law-the-law-of-implicit-interfaces)
    - [Metcalfe Yasası](#metcalfes-kanunu)
    - [Moore Yasası](#moores-law)
    - [Murphy Yasası / Sod  Yasası](#murphys-law--sods-law)
    - [Parkinson Yasası](#parkinsons-law)
    - [Olgunlaşmamış Optimizasyon Etkisi](#premature-optimization-effect)
    - [Putt Yasası](#putts-law)
    - [Reed Yasası](#sazl%C4%B1k-kanunu)
    - [Karmaşıklığın Korunması Yasası (Tesler Yasası)](#the-law-of-conservation-of-complexity-teslers-law)
    - [Sızdıran Soyutlamalar Yasası](#the-law-of-leaky-abstractions)
    - [Önemsizlik Yasası](#the-law-of-triviality)
    - [Unix Felsefesi](#the-unix-philosophy)
    - [Spotify Modeli](#the-spotify-model)
    - [Wadler Yasası](#wadlers-law)
- [Prensipler](#principles)
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
- [Ek Kaynaklar](#reading-list)
- [TODO](#todo)

<!-- vim-markdown-toc -->

## Giriş

İnsanların geliştirme hakkında konuşurken tartıştıkları birçok yasa var. Bu depo, en yaygın olanlardan bazılarının referanslarını ve özetini barındırır. Katkıda bulunmak için PR açıp gönderebilirsiniz!

❗: Bu depo yasaların, prensiplerin ve modellerin bilgi vermek amaçlı açıklamalarını içerir ve hiçbirini *savunma* amacı gütmez. Bunların hangisinin uygulanıp uygulanmayacağı tamamen tartışma konusudur ve yapılan işe bağlıdır..

## Yasalar

Tek tek başlayalım!

### Amdahl Yasası

[Wikipedia Amdahl Yasası](https://en.wikipedia.org/wiki/Amdahl%27s_law)

> Amdahl Yasası kaynakları artırarak bir hesaplama işleminin *olası* hızlanma miktarını hesaplayan bir formülü tanımlar. Genellikle paralel işleme hesaplarında kullanılır ve işlemci sayısının artırılmasının programın paralelleştirilebilme kapasitesine bağlı olarak etkisinin doğru şekilde saplanmasını sağlar.

En güzel şu örnekle anlatılabilir. Bir programın iki bölümden oluştuğunu düşünelim. Bölüm A sadece tek işlemci ile çalıştırılabilir. Bölüm B ise paralelleştirilebilecek şekilde yazılmış. Bu durumda bu programı çok işlemci ile çalıştırdığımızda Bölüm B'de oluşacak kadar bir kazanım sağlayabiliriz. Bölüm A'da her hangi bir katkı olamayacaktır.

Aşağıdaki diyagram bazı olası hız geliştirmelerine örnekler içeriyor:

![Diagram: Amdahl's Law](../images/amdahls_law.png)

*(Diyagramın kaynağı: Daniels220 tarafından İngilizce Wikipedia'da, Creative Commons Attribution-Share Alike 3.0 Unported, https://en.wikipedia.org/wiki/File:AmdahlsLaw.svg)*

Diyagramdaki örneklerden görüldüğü üzere, eğer bir programın sadece %50'si paralelleştirilebiliyorsa 10 işlemciden sonra işlemci eklemek hızda gözle görünür bir artış sağlamıyor ama %95 paralelleştirilebilen bir programda 1000 işlemciden sonra bile işlemci eklemenin hızı artırdığı gözlenebilir.

[Moore Yasasında](#moores-law) söylenen artışın azalma eğiliminde olması ve aynı zamanda işlemci hızının artışında da ivme kaybı olması, paralelleştirilebilme özelliğini performans artışında anahtar duruma getirdi. Grafik programlama bu konuda en belirgin örnek. Shader tabanlı modern işleme ile pixel ve fragmanların paralel olarak render edilebilmesi sayesinde modern grafik kartlarında binlerce işlemci çekirdeği olabiliyor.

Ek kaynaklar:

- [Brooks Yasası](#brooks-law)
- [Moore Yasası ](#moores-law)

### Brooks Yasası

[Wikipedia'da Brooks Yasası](https://en.wikipedia.org/wiki/Brooks%27s_law)

> Gecikmesi kesinleşmiş projeye yeni insan kaynağı eklemek projeyi daha da geciktirir.

Bu yasa, gecikmiş bir projeyi hızlandırmak için ek insan kaynağı koymanın projeyi daha geciktireceğini iddia ediyor. Brook'a göre bunun gereksiz bir sadeleştirme olduğu kesin. Yeni katılanların adapte edilmesi ve iletişim karmaşası hemen etkisini göstererek hızın yavaşlamasına sebep olur. Ayrıca, yapılacak işlerin birçoğu genellikle daha küçük parçalara bölünemez ve birden fazla kaynak bu işlerin yapılması için kullanılmaz. Bu durum beklenen artışın sağlanmaması ile sonuçlanır.

Meşhur "Dokuz kadın ile 1 ayda doğum sağlanamaz" deyimi bu yasanın en pratik anlatımıdır. Bazı işlerin bölünemediği veya paralelleştirilemediği gerçeğini unutmamak lazım.

'[The Mythical Man Month](#reading-list)' adlı kitabın ana konularından biri budur.

Ek kaynaklar:

- [Death March](#todo)
- [Reading List: The Mythical Man Month](#reading-list)

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

### Gall Yasası

[Wikipedia'da Gall Yasası](https://en.wikipedia.org/wiki/John_Gall_(author)#Gall's_law)

> Çalışan karmaşık bir sistemin her zaman işe yarayan daha basit bir sistemden evrimleştiği kesinlikle söylenebilir. Başlangıçtan itibaren karmaşık tasarlanmış bir sistemin asla çalışmayacağı ve sonradan da düzeltilemeyeceği kesindir. Çalışsan daha basit bir sistem ile başlamanız gerekir.
> ([John Gall](https://en.m.wikipedia.org/wiki/John_Gall_(author)))

Gall Yasası der ki, çok karmaşık sistemleri *tasarlamaya* çalışmak her zaman başarısızlıkla sonuçlanır. Bu tür sistemlerin ilk denemede başarılı olmaları çok nadir görülür ama genellikle basit sistemlerden evrilirler.

En klasik örnek günümüzdeki internettir.  Şu an çok karmaşık bir sistemdir.  Aslında başlangıçta sadece akademik kurumlar arası içerik paylaşımı olarak tanımlanmıştı. Bu tanımı karşılamada çok başarılı oldu ve zamanla gelişerek bugünkü karmaşık halini aldı.

Ek kaynaklar:

- [KISS (Keep It Simple, Stupid)](#the-kiss-principle)

### Hanlon'un Usturası

[Wikipedia'da Hanlon'un Usturası](https://en.wikipedia.org/wiki/Hanlon%27s_razor)

> Aptallıkla layıkıyla açıklanabilecek bir şeyi, asla kötü niyete bağlamayın.
> Robert J. Hanlon

Bu prensip, olumsuz sonuçlara yol açan eylemlerin, çoğunlukla kötü niyetin sonucu olmadığını savunmaktadır. Aksine, olumsuz sonuç daha büyük olasılıkla bu eylemlerin ve/veya etkinin tam olarak anlaşılamamasına bağlıdır.

### Hofstadter Yasası

[Wikipedia'da Hofstadter Yasası](https://en.wikipedia.org/wiki/Hofstadter%27s_law)

> Bir iş her zaman umduğundan daha uzun sürer, Hofstadter yasasını göz önünde bulundursan bile.
> (Douglas Hofstadter)

Bu yasayı bir işin ne kadar süreceğini tahminlenirken hatırlatıldığı için duymuş olabilirsiniz. Herkesin kabul ettiği bir gerçek var ki, yazılım geliştirmede en kötü olduğumuz alan işin ne kadar sürede biteceğini tahmin etmektir.

'[Gödel, Escher, Bach: An Eternal Golden Braid](#reading-list)' adlı kitaptan bir alıntı.

Ek kaynaklar:

- [Reading List: Gödel, Escher, Bach: An Eternal Golden Braid](#reading-list)

### Hutber Yasası

[Wikipedia'da Hutber Yasası ](https://en.wikipedia.org/wiki/Hutber%27s_law)

> İyileştirme, bozulma anlamına da gelir.
> ([Patrick Hutber](https://en.wikipedia.org/wiki/Patrick_Hutber))

Bu yasa der ki; sistemde yapılan bir iyileştirme sistemin diğer taraflarında bozulmaya sebep olabilir ya da başka bozuklukları gizleyebilir, bu da sistemin mevcut durumunun daha da bozulmasına sebep olabilir.

Örneğin, bir servisin cevap verme zamanında bir geliştirme yapılıp hızlandırılırsa bu durum süreçteki diğer aşamalarda kapasite ve çıktı artışına sebep olabilir. Bu da sistemin diğer taraflarını olumsuz etkileyebilir.

### Hype Döngüsü ve Amara Yasası

[Wikipedia'da Hype Döngüsü](https://en.wikipedia.org/wiki/Hype_cycle)

> Bir teknolojinin kısa vadede oluşacak etkisini abartıp, uzun vadede oluşacak etkisini hafife alıyoruz.
> (Roy Amara)

Hype Döngüsü bir teknolojinin zamanla yarattığı heyecan ve gelişiminin görsel olarak sunumudur ve Gartner tarafından ilk olarak oluşturulmuştur. En güzel anlatım aşağıdaki bir görsel ile yapılabilir:

![The Hype Cycle](../images/gartner_hype_cycle.png)

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

### Metcalfe Yasası

[Wikipedia'da Metcalfe Yasası](https://en.wikipedia.org/wiki/Metcalfe's_law)

> Ağ teorisinde, bir sistemin değeri yaklaşık olarak sistemin kullanıcı sayısının karesi ile orantılı olarak büyür.

Bu yasa, bir sistem içindeki muhtemel çift bağlantıların sayısına dayanmaktadır ve [Reed Yasası](#reeds-law) ile yakından ilgilidir. Odlyzko ve diğerleri, hem Reed Yasası hem de Metcalfe Yasası'nın, insan bilişinin ağ etkileri üzerindeki sınırlarını hesaba katmayarak sistemin değerini abarttığını öne sürerler; [Dunbar Sayısı'na](#dunbars-number) bakınız.

Ek kaynaklar:

- [Reed Yasası](#sazl%C4%B1k-kanunu)
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

### Parkinson Yasası

[Wikipedia'da Parkinson Yasası](https://en.wikipedia.org/wiki/Parkinson%27s_law)

> Bir iş, daima, bitirilmesi için kendisine ayrılan sürenin hepsini kapsayacak şekilde uzar.

Orijinal bağlamında, bu kanun bürokrasi alanındaki çalışmalara dayanıyordu. Kötümser bir bakış açısıyla yazılım geliştirme girişimleri için de söylenebilir. Şöyle ki ekipler genelde proje bitiş tarihi yaklaşana kadar düşük verimde çalışırlar, bitiş tarihi yaklaştıkça bitirmek için yoğun bir çaba içine girerler ve sonuç olarak aslında bitiş tarihini tutturmuş olurlar.

Bu yasa ile [Hofstadter Yasası](#hofstadters-law) birleştirilirse, daha kötümser bir yasaya ulaşılır. Bir iş bitirilmesi için harcanması gereken zamanı kapsar ve *her zaman gecikir*.

Ek kaynaklar:

- [Hofstadter Yasası](#hofstadters-law)

### Olgunlaşmamış Optimizasyon Etkisi

[WikiWikiWeb'de Olgunlaşmamış Optimizasyon Etkisi](http://wiki.c2.com/?PrematureOptimization)

> Vakti gelmeden gelmeden yapılan optimizasyon bütün kötülüklerin anasıdır.
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

- [Metcalfe Yasası](#metcalfes-kanunu)
- [Dunbar Sayısı](#dunbar-say%C4%B1s%C4%B1)

### Karmaşıklığın Korunması Yasası (Tesler Yasası)

[Wikipedia'da Karmaşıklığın Korunması Yasası](https://en.wikipedia.org/wiki/Law_of_conservation_of_complexity)

Bu yasa der ki, her sistemde kesinlikle ayıklanamayacak bir miktarda karmaşıklık vardır.

Bir sistem ve yazılımdaki karmaşıklıkların bazıları dikkatsizlik veya yanlışlıktan ortaya çıkar. Bu kötü kurgulanmış yapının, herhangi bir dikkatsizliğin, ya da problemin kötü modellenmesinin sonucu olabilir. Bu tarz karmaşıklıklar giderilebilir ve sistemden ayıklanabilir. Bunun yanında, bazı karmaşıklıklar sistemin gerçekleridir yani sistemin çözmeye çalıştığı problemin doğası gereği ortaya çıkarlar. Bu tarz karmaşıklıklar sistem içinde farklı yerlere taşınabilirler ama sistemden ayıklanmazlar.

O yasanın farklı bir yansıması olarak şöyle düşünülebilir, eğer bir karmaşıklık esastan geliyorsa ve sistem sadeleştirilerek bile ayıklanamıyorsa, daha karmaşık bir şekilde davranması beklenen *kullanıcının tarafına taşınabilir*.

### Sızdıran Soyutlamalar Yasası

[Sızdıran Soyutlamalar Yasası, Joel on Software](https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/)

> Önemsiz sayılmayacak bütün soyutlamar belli ölçüde sızıntı içerir.
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

Bu kurgu örnek 'Bike Shedding' diye bir deyimin yaygınlaşmasına sebep olmuştur. Türkçe'deki 'pire için yorgan yakmak' ya da 'attığın taş ürküttüğün kurbağaya değsin' gibi deyimlere benzer.

### Unix Felsefesi

[Wikipedia'da Unix Felsefesi](https://en.wikipedia.org/wiki/Unix_philosophy)

Unix felsefesi şöyle özetlenebilir; bir yazılım parçası olabildiğince küçük olmalı ve sadece bir işi yapmaya odaklanmalıdır. Bu felsefeye uymak sistemleri büyük, karmaşık ve çok amaçlı programlarla oluşturmak yerine küçük, basit ve iyi tanımlanmış parçalardan daha kolayca oluşturmayı sağlar.

Modern yaklaşımlardan biri olan 'Mikro-service Mimarisi' de bu felsefenin uygulaması olarak düşünülebilir. Çünkü bu mimari ile servislerin küçük, amaç odaklı ve tek bir iş yapacak şekilde geliştirilmesi ve karmaşık yapıların küçük basit bloklar halinde oluşturulması hedefleniyor.

### Spotify Modeli

[Spotify Modeli, Spotify Labs](https://labs.spotify.com/2014/03/27/spotify-engineering-culture-part-1/)

Spotify Modeli Spotify'daki uygulamasından dolayı popüler olmuş ekip ve organizasyon yapıları için yeni bir yaklaşımdır. Model basitçe ekiplerin teknolojilere göre değil de özellikler etrafında organize edilmesidir.

Spotify Modeli kabileler (Tribes), birlikler (Guilds) ve kısımlar (Chapter) gibi organizasyon yapısında kullanılacak öğeleri de yaygın hale getirdi.

### Wadler Yasası

[Wadler Yasası, wiki.haskell.org](https://wiki.haskell.org/Wadler's_Law)

> Herhangi bir programlama dilini tasarlarken, aşağıdaki listedeki herhangi bir özelliği tartışmak için harcanan zaman iki üzeri özelliğin listeki sırası ile doğru orantılıdır.
> 1. Semantik
> 2. Genel sözdizimi
> 3. Sözcük sözdizimi
> 4. Yorumlardaki sözcük sözdizimi
> (Kısaca semantic için harcanan her bir saat için yorumlardaki sözcük sözdizimi için sekiz saat harcanacaktır.)

[Önemsizlik Yasasında](#the-law-of-triviality) öne sürülene benzer olarak, Wadler Yasası yeni bir programlama dili tasarlanırken konunun önemi ile o konu için harcanan zaman ters orantılı olduğunu söylüyor.

Ek kaynaklar:

- [Önemsizlik Yasası](#the-law-of-triviality)

## Prensipler

Prensiplerin genellikle tasarıma ilişkin rehberlerdir.

### Dilbert Prensibi

[Wikipedia'da Dilbert Prensibi](https://en.wikipedia.org/wiki/Dilbert_principle)

> Şirketler, yetersiz çalışanları, iş akışından uzaklaştırmak için sistematik olarak yönetici olmaya teşvik etme eğilimindedir.
> *Scott Adams*

Scot Adams (Dilbert çizgi dizisinin yazarı) [Peter prensibinden](#the-peter-principle) esinlenerek ortaya atılmış bir yönetim kavramıdır. Dilbert prensibine göre yetenekli olmayan çalışanlar yönetim kadorlarına dopru yükseltilirler ki üretime verecekleri zarar aza indirilsin. Adams bunu ilk olarak 1995'te Wall Street Journal'da yazdığı bir makalede açıkladı daha sonra ise 1996'da yazdığı [Dilbert Prensibi](#reading-list) adlı kitabında detaylandırdı.

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

> Hiyerarşideki insanlar “yetersizlik seviyelerine” göre yükselme eğilimindedir.
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

Teorik olarak, bu prensibe uygun yazılmış kodlar daha sağlam ve değiştirilmesi kolaydır. Sadece tek bir parçanın değiştirildiğine emin olunduğunda değişimi *tesk etmek* de kolay olacaktır. Önceki şifre örneğini düşünürsek, şifrenin zorluk seviyesi değiştirildiğinde sadece şifre ilgili bölümlerin etkilenecektir. Birden fazla sorumluluğu olan bir bölümde olan değişikliğin nereleri etkileceğini hesaplamak daha zordur.

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
> 

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

[Wikipedia'da YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it)

***Y**ou **A**ren't **G**onna **N**eed **I**t* (İhtiyacın olmayacak) deyiminin kısaltmasıdır.

> İhtiyaç duyduğunuz şeyleri her zaman ihtiyaç duyduğunuzda geliştirin, onlara ihtiyacınız olacağını düşündüğünüzde değil.
> ([Ron Jeffries](https://twitter.com/RonJeffries)) (XP eş-kurucusu and "Extreme Programming Installed" kitabının yazarı)

Bu *Aşırı Programlama* (XP) ilkesi, geliştiricilerin yalnızca acil gereksinimler için gerekli olan işlevleri yerine getirmeleri gerektiğini ve daha sonra ihtiyaç duyulabilecek işlevleri uygulayarak geleceği tahmin etme girişimlerinden kaçınmalarını önerir.

Bu ilkeye bağlı kalmak, kod tabanındaki kullanılmayan kod miktarının ve hiçbir değer getirmeyen işlevlerde haracanan zamanın ve çabanın azalmasını sağlayacaktır.

Ek kaynaklar:

- [Reading List: Extreme Programming Installed](#reading-list)

## Ek Kaynaklar

Bu kavramları ilginç bulduysanız, aşağıdaki kitapların keyfini çıkarabilirsiniz.

- [Extreme Programming Installed - Ron Jeffries, Ann Anderson, Chet Hendrikson](https://www.goodreads.com/en/book/show/67834) - Extreme Programming kavramının temel prensiplerini içerir.
- [The Mythical Man Month - Frederick P. Brooks Jr.](https://www.goodreads.com/book/show/13629.The_Mythical_Man_Month) - Yazılım mühendisliği klasiği sayılabilir. Brooks Yasası bu kitabın ana temasıdır.
- [Gödel, Escher, Bach: An Eternal Golden Braid - Douglas R. Hofstadter.](https://www.goodreads.com/book/show/24113.G_del_Escher_Bach) - Sınıflandırması zor bir kitap. Hofstadter Yasası bu kitaptan alıntıdır.
- [Dilbert Prensibi - Adam Scott](https://www.goodreads.com/book/show/85574.The_Dilbert_Principle) - Amerikadaki kurumsal hayata mizahi bir yaklaşım,  [Dilbert Prensibinin](#the-dilbert-principl) sahibinden.
- [The Peter Principle - Lawrence J. Peter](https://www.goodreads.com/book/show/890728.The_Peter_Principle) - Another comic look at the challenges of larger organisations and people management, the source of [The Peter Principle](#the-peter-principle).

## TODO

Selam!. Buraya ulaştıysanız, henüz yazmadığım bir konunun bağlantısını tıkladınız, bunun için üzgünüm - ve en kısa zamanda tamamlamaya çalışacağım!

Soru ve önerileriniz için [issue](https://github.com/dwmkerr/hacker-laws/issues) açabilirsiniz, ya da katkıda bulunmak isterseniz [Pull Request](https://github.com/dwmkerr/hacker-laws/pulls) açabilirsiniz.
