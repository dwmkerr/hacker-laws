# 💻📖 prawa-hakerskie

Prawa, teorie, zasady i wzorce, które programiści uznają za przydatne.

[Tłumaczenia](#translations): [🇮🇩](./translations/id.md) [🇧🇷](./translations/pt-BR.md) [🇨🇳](https://github.com/nusr/hacker-laws-zh) [🇩🇪](./translations/de.md) [🇫🇷](./translations/fr.md) [🇬🇷](./translations/el.md) [🇮🇹](https://github.com/csparpa/hacker-laws-it) [🇱🇻](./translations/lv.md) [🇰🇷](https://github.com/codeanddonuts/hacker-laws-kr) [🇵🇱](./translations/pl.md) [🇷🇺](https://github.com/solarrust/hacker-laws) [🇪🇸](./translations/es-ES.md) [🇹🇷](https://github.com/umutphp/hacker-laws-tr) [🇯🇵](./translations/jp.md) [🇺🇦](./translations/uk.md)

Podoba Ci się ten projekt? Proszę rozważyć [sponsorowanie mnie](https://github.com/sponsors/dwmkerr) i [tłumaczy](#translations) . Sprawdź również ten podcast na [The Changelog - Laws for Hackers to Live By,](https://changelog.com/podcast/403) aby dowiedzieć się więcej o projekcie! Możesz także [pobrać najnowszy e-book w formacie PDF](https://github.com/dwmkerr/hacker-laws/releases/latest/download/hacker-laws.pdf) . Sprawdź [Przewodnik](./.github/contributing.md) dla twórców, jeśli chcesz wnieść swój wkład!

---

<!-- vim-markdown-toc GFM -->

- [Wstęp](#wstęp)
- [Prawa](#prawa)
    - [Zasada 90-9-1 (zasada 1%)](#zasada-90-9-1-zasada-1)
    - [Prawo Amdahla](#prawo-amdahla)
    - [Teoria zepsutych okien](#teoria-zepsutych-okien)
    - [Prawo Brooksa](#prawo-brooksa)
    - [Twierdzenie CAP (Twierdzenie Brewera)](#twierdzenie-cap-twierdzenie-brewera)
    - [Prawo Conwaya](#prawo-conwaya)
    - [Prawo Cunninghama](#prawo-cunninghama)
    - [Numer Dunbara](#numer-dunbara)
    - [Efekt Dunninga-Krugera](#efekt-dunninga-krugera)
    - [Prawo Fittsa](#prawo-fittsa)
    - [Prawo Galla](#prawo-galla)
    - [Prawo Goodharta](#prawo-goodharta)
    - [Brzytwa Hanlona](#brzytwa-hanlona)
    - [Prawo Hicka (Prawo Hicka-Hymana)](#prawo-hicka-prawo-hicka-hymana)
    - [Prawo Hofstadtera](#prawo-hofstadtera)
    - [Prawo Hutbera](#prawo-hutbera)
    - [Cykl szumu i prawo Amary](#cykl-szumu-i-prawo-amary)
    - [Prawo Hyruma (prawo niejawnych interfejsów)](#prawo-hyruma-prawo-niejawnych-interfejsów)
    - [Prawo Kernighana](#prawo-kernighana)
    - [Prawo Linusa](#prawo-linusa)
    - [Prawo Metcalfego](#prawo-metcalfego)
    - [prawo Moore'a](#prawo-moorea)
    - [Prawo Murphy'ego / Prawo Soda](#prawo-murphyego--prawo-soda)
    - [Brzytwa Ockhama](#brzytwa-ockohama)
    - [Prawo Parkinsona](#prawo-parkinsona)
    - [Przedwczesny efekt optymalizacji](#przedwczesny-efekt-optymalizacji)
    - [Prawo Putta](#prawo-putta)
    - [Prawo Reeda](#prawo-reeda)
    - [Prawo zachowania złożoności (prawo Teslera)](#prawo-zachowania-złożoności-prawo-teslera)
    - [Prawo Demeter](#prawo-demeter)
    - [Prawo nieszczelnych abstrakcji](#prawo-nieszczelnych-abstrakcji)
    - [Prawo trywialności](#prawo-trywialności)
    - [Filozofia Uniksa](#filozofia-uniksa)
    - [Zasada Skauta](#zasada-skauta)
    - [Model Spotify](#model-spotify)
    - [Zasada dwóch pizzy](#zasada-dwóch-pizzy)
    - [Prawo Wadlera](#prawo-wadlera)
    - [Prawo Wheatona](#prawo-wheatona)
- [Zasady](#zasady)
    - [Wszystkie modele są błędne (prawo George'a Boxa)](#wszystkie-modele-są-błędne-prawo-georgea-boxa)
    - [Płot Chestertona](#płot-chestertona)
    - [Efekt Morza Martwego](#efekt-morza-martwego)
    - [Zasada Dilberta](#zasada-dilberta)
    - [Zasada Pareto (Zasada 80/20)](#zasada-pareto-zasada-8020)
    - [Zasada Shirky](#zasada-shirky)
    - [Zasada Piotra](#zasada-piotra)
    - [Zasada solidności (prawo Postela)](#zasada-solidarności-prawo-postela)
    - [SOLID](#solid)
    - [Zasada pojedynczej odpowiedzialności](#zasada-pojedynczej-odpowiedzialności)
    - [Zasada otwarcia/zamknięcia](#zasada-otwarcia-zamknięcia)
    - [Zasada substytucji Liskov](#zasada-substytucji-liskov)
    - [Zasada segregacji interfejsów](#zasada-segregacji-interfejsów)
    - [Zasada odwrócenia zależności](#zasada-odwrócenia-zależności)
    - [Zasada DRY](#zasada-dry)
    - [Zasada KISS](#zasada-kiss)
    - [YAGNI](#yagni)
    - [Błędy przetwarzania rozproszonego](#błędy-przetwarzania-rozproszonego)
- [Lista rzeczy do przeczytania](#lista-rzeczy-do-przeczytania)
- [Zasoby online](#zasoby-online)
- [eBook w formacie PDF](#ebook-w-formacie-pdf)
- [Podcast](#podcast)
- [Tłumaczenia](#tłumaczenia)
- [Powiązane projekty](#powiązane-projekty)
- [Przyczynianie się](#przyczynianie-się)
- [DO ZROBIENIA](#do-zrobienia)

<!-- vim-markdown-toc -->

## Wstęp

Istnieje wiele praw, o których ludzie dyskutują, mówiąc o rozwoju. To repozytorium jest odniesieniem i przeglądem niektórych z najczęstszych. Podziel się i prześlij PR!

Odpowiedź: To repozytorium zawiera wyjaśnienie niektórych praw, zasad i wzorców, ale nie *zaleca* żadnego z nich. To, czy należy je zastosować, zawsze będzie kwestią dyskusyjną i w dużej mierze zależy od tego, nad czym pracujesz.

## Prawa

No to zaczynamy!

### Zasada 90-9-1 (zasada 1%)

[Reguła 1% na Wikipedii](https://en.wikipedia.org/wiki/1%25_rule_(Internet_culture))

Zasada 90-9-1 sugeruje, że w społeczności internetowej, takiej jak wiki, 90% uczestników tylko korzysta z treści, 9% edytuje lub modyfikuje treść, a 1% uczestników dodaje treść.

Przykłady ze świata rzeczywistego:

- Badanie z 2014 roku czterech cyfrowych portali społecznościowych poświęconych zdrowiu wykazało, że 1% najpopularniejszych tworzy 73% postów, kolejne 9% stanowiło średnio ~25%, a pozostałe 90% stanowiło średnio 2% ( [Odniesienie](https://www.jmir.org/2014/2/e33/) )

Zobacz też:

- [Zasada Pareto](#the-pareto-principle-the-8020-rule)

### Prawo Amdahla

[Prawo Amdahla na Wikipedii](https://pl.wikipedia.org/wiki/Prawo_Amdahla)

> Prawo Amdahla to wzór pokazujący *potencjalne przyspieszenie* zadania obliczeniowego, które można osiągnąć zwiększając zasoby systemu. Zwykle używany w obliczeniach równoległych, może przewidzieć rzeczywiste korzyści ze zwiększenia liczby procesorów, co jest ograniczone przez możliwość równoległości programu.

Najlepiej zilustrowane przykładem. Jeśli program składa się z dwóch części, części A, która musi być wykonywana przez pojedynczy procesor, i części B, która może być zrównoleglona, to widzimy, że dodanie wielu procesorów do systemu wykonującego program może mieć tylko ograniczoną korzyść . Potencjalnie może znacznie poprawić prędkość części B - ale prędkość części A pozostanie niezmieniona.

Poniższy diagram pokazuje kilka przykładów potencjalnej poprawy szybkości:

<img width="480px" alt="Schemat: Prawo Amdahla" src="/images/amdahls_law.png" />

*(Odniesienie do obrazu: Daniels219 z angielskiej Wikipedii, Creative Commons Attribution-Share Alike 3.0 Unported, https://en.wikipedia.org/wiki/File:AmdahlsLaw.svg)*

Jak widać, nawet program, który można zrównoleglać w 50%, przyniesie niewiele korzyści poza 10 jednostkami przetwarzania, podczas gdy program, który można zrównolelizować w 95%, nadal może osiągnąć znaczną poprawę szybkości przy ponad tysiącu jednostek przetwarzania.

Ponieważ [prawo Moore'a](#moores-law) zwalnia, a przyspieszenie szybkości poszczególnych procesorów zwalnia, równoległość jest kluczem do poprawy wydajności. Programowanie graficzne jest doskonałym przykładem - przy nowoczesnych obliczeniach opartych na Shader, pojedyncze piksele lub fragmenty mogą być renderowane równolegle - dlatego współczesne karty graficzne często mają wiele tysięcy rdzeni przetwarzających (GPU lub Shader Units).

Zobacz też:

- [Prawo Brooksa](#brooks-law)
- [prawo Moore'a](#moores-law)

### Teoria zepsutych okien

[Teoria rozbitycg okien na Wikipedii](https://pl.wikipedia.org/wiki/Teoria_rozbitych_okien)

Teoria rozbitych okien sugeruje, że widoczne oznaki przestępczości (lub braku dbałości o środowisko) prowadzą do kolejnych i poważniejszych przestępstw (lub dalszego pogorszenia stanu środowiska).

Teoria ta została zastosowana do rozwoju oprogramowania, co sugeruje, że kod niskiej jakości (lub [dług techniczny](#TODO) ) może prowadzić do przekonania, że wysiłki na rzecz poprawy jakości mogą być ignorowane lub niedoceniane, co prowadzi do dalszej złej jakości kodu. Ten efekt kaskadowo prowadzi do znacznego spadku jakości z biegiem czasu.

Zobacz też:

- [Dług techniczny](#TODO)

Przykłady:

- [Programowanie pragmatyczne: entropia oprogramowania](https://flylib.com/books/en/1.315.1.15/1/)
- [Horror kodowania: teoria rozbitego okna](https://blog.codinghorror.com/the-broken-window-theory/)
- [OpenSource: Radość z programowania — teoria rozbitego okna](https://opensourceforu.com/2011/05/joy-of-programming-broken-window-theory/)

### Prawo Brooksa

[Prawo Brooksa na Wikipedii](https://pl.wikipedia.org/wiki/Prawo_Brooksa)

> Dodanie zasobów ludzkich do spóźnionego projektu rozwoju oprogramowania sprawia, że jest to później.

Prawo to sugeruje, że w wielu przypadkach próba przyspieszenia realizacji projektu, który jest już spóźniony, poprzez dodanie większej liczby osób, spowoduje, że realizacja będzie jeszcze późniejsza. Brooks nie ma wątpliwości, że jest to nadmierne uproszczenie, jednak ogólne rozumowanie jest takie, że biorąc pod uwagę czas narastania nowych zasobów i ogólne koszty komunikacji, w krótkim czasie prędkość spada. Ponadto wiele zadań może nie być podzielnych, tj. łatwo rozdzielonych między więcej zasobów, co oznacza, że potencjalny wzrost prędkości jest również mniejszy.

Powszechne zdanie przy porodzie „Dziewięć kobiet nie może spłodzić dziecka w ciągu jednego miesiąca” odnosi się do prawa Brooksa, w szczególności do faktu, że niektóre rodzaje pracy nie są podzielne ani równoległe.

Jest to tematem przewodnim książki „ [Miesiąc mitycznego człowieka](#reading-list) ”.

Zobacz też:

- [Marsz śmierci](#todo)
- [Lista lektur: Miesiąc Mitycznego Człowieka](#reading-list)

### Twierdzenie CAP (Twierdzenie Brewera)

Twierdzenie CAP (zdefiniowane przez Erica Brewera) stwierdza, że w przypadku rozproszonego magazynu danych można uzyskać tylko dwie z trzech następujących gwarancji (co najwyżej):

- Spójność: podczas odczytu danych każde żądanie otrzymuje *najnowsze* dane lub zwracany jest błąd
- Dostępność: podczas odczytu danych każde żądanie otrzymuje *odpowiedź* bez błędu, bez gwarancji, że są to *najnowsze* dane
- Tolerancja partycji: gdy dowolna liczba żądań sieciowych między węzłami nie powiedzie się, system nadal działa zgodnie z oczekiwaniami

Sedno rozumowania jest następujące. Nie można zagwarantować, że partycja sieciowa nie wystąpi (zobacz [The Fallacies of Distributed Computing](#the-fallacies-of-distributed-computing) ). Dlatego w przypadku partycji możemy albo anulować operację (zwiększając spójność i zmniejszając dostępność) albo kontynuować (zwiększając dostępność, ale zmniejszając spójność).

Nazwa pochodzi od pierwszych liter gwarancji (spójność, dostępność, tolerancja partycji). Należy pamiętać, że bardzo ważne jest, aby mieć świadomość, że *nie* dotyczy to [*ACID*](#TODO) , który ma inną definicję spójności. Niedawno [opracowano](#TODO) twierdzenie PACELC, które dodaje ograniczenia dotyczące opóźnień i spójności, gdy sieć *nie* jest podzielona na partycje (tj. gdy system działa zgodnie z oczekiwaniami).

Większość nowoczesnych platform bazodanowych potwierdza to twierdzenie pośrednio, oferując użytkownikowi bazy danych opcję wyboru między operacją o wysokiej dostępności (która może obejmować „brudny odczyt”) a operacją wysoce spójną (na przykład „zapis z potwierdzeniem kworum ').

Przykłady ze świata rzeczywistego:

- [Wewnątrz Google Cloud Spanner i twierdzenia CAP](https://cloud.google.com/blog/products/gcp/inside-cloud-spanner-and-the-cap-theorem) – omawia szczegóły działania Cloud Spanner, które na pierwszy rzut oka wydaje się platformą, która ma *wszystkie* gwarancje CAP, ale pod maską jest zasadniczo system CP.

Zobacz też:

- [KWAS](#TODO)
- [Błędy przetwarzania rozproszonego](#the-fallacies-of-distributed-computing)
- [PACELC](#TODO)

### Prawo Conwaya

[Prawo Conwaya na Wikipedii](https://en.wikipedia.org/wiki/Conway%27s_law)

Prawo to sugeruje, że granice techniczne systemu będą odzwierciedlać strukturę organizacji. Często mówi się o tym, gdy patrzymy na ulepszenia organizacji. Prawo Conwaya sugeruje, że jeśli organizacja jest podzielona na wiele małych, niepowiązanych ze sobą jednostek, tak będzie tworzone oprogramowanie. Jeśli organizacja jest zbudowana bardziej wokół „branż”, które są zorientowane na funkcje lub usługi, systemy oprogramowania również to odzwierciedlą.

Zobacz też:

- [Model Spotify](#the-spotify-model)

### Prawo Cunninghama

[Prawo Cunninghama na Wikipedii](https://en.wikipedia.org/wiki/Ward_Cunningham#Cunningham's_Law)

> Najlepszym sposobem na uzyskanie prawidłowej odpowiedzi w Internecie nie jest zadawanie pytań, ale zamieszczenie błędnej odpowiedzi.

Według Stevena McGeady'ego Ward Cunningham poradził mu na początku lat 80.: „Najlepszym sposobem na uzyskanie prawidłowej odpowiedzi w Internecie jest nie zadawanie pytań, ale zamieszczenie złej odpowiedzi”. McGeady nazwał to prawo Cunninghama, chociaż Cunningham zaprzecza własności, nazywając to „błędem”. Chociaż pierwotnie odnosiło się do interakcji w Usenecie, prawo zostało użyte do opisania działania innych społeczności internetowych (np. Wikipedia, Reddit, Twitter, Facebook).

Zobacz też:

- [XKCD 386: „Wezwania do służby”](https://xkcd.com/386/)

### Numer Dunbara

[Numer Dunbara na Wikipedii](https://en.wikipedia.org/wiki/Dunbar%27s_number)

„Liczba Dunbara jest sugerowanym limitem poznawczym liczby osób, z którymi można utrzymywać stabilne relacje społeczne – relacje, w których jednostka wie, kim jest każda osoba i jak każda osoba odnosi się do każdej innej osoby”. Istnieje pewna niezgodność co do dokładnej liczby. „... [Dunbar] zaproponował, że ludzie mogą wygodnie utrzymywać tylko 150 stabilnych związków”. Umieścił tę liczbę w bardziej społecznym kontekście, „liczbę osób, których nie czulibyście się zawstydzeni dołączeniem do nieproszonych drinków, gdybyście wpadli na nich w barze”. Szacunki dotyczące liczby wahają się od 100 do 250.

Podobnie jak w przypadku stabilnych relacji między jednostkami, utrzymanie relacji programisty z bazą kodu wymaga wysiłku. W obliczu dużych, skomplikowanych projektów lub posiadania wielu projektów opieramy się na konwencji, zasadach i modelowanych procedurach w celu skalowania. Liczba Dunbar jest ważna nie tylko w miarę rozwoju biura, ale także przy ustalaniu zakresu działań zespołu lub decydowaniu, kiedy system powinien zainwestować w narzędzia, które pomogą w modelowaniu i automatyzacji ogólnych kosztów logistycznych. Umieszczając liczbę w kontekście inżynierskim, jest to liczba projektów (lub znormalizowana złożoność pojedynczego projektu), w przypadku których możesz czuć się pewnie, dołączając do rotacji na wezwanie, aby wesprzeć.

Zobacz też:

- [Prawo Conwaya](#conways-law)

### Efekt Dunninga-Krugera

[Efekt Dunninga-Krugera na Wikipedii](https://en.wikipedia.org/wiki/Dunning%E2%80%93Kruger_effect)

> Jeśli jesteś niekompetentny, nie możesz wiedzieć, że jesteś niekompetentny... Umiejętności potrzebne do uzyskania prawidłowej odpowiedzi to dokładnie te umiejętności, których potrzebujesz, aby rozpoznać, jaka jest właściwa odpowiedź.
>
> ( [Dawid Dunning](https://en.wikipedia.org/wiki/David_Dunning) )

Efekt Dunninga-Krugera to teoretyczne zniekształcenie poznawcze, które zostało opisane przez Davida Dunninga i Justina Krugera w badaniu psychologicznym i artykule z 1999 roku. Badanie sugeruje, że osoby o niskim poziomie umiejętności w zadaniu prawdopodobnie przeceniają swoją zdolność do zadania. Proponowaną przyczyną tego nastawienia jest to, że *wymagana jest wystarczająca świadomość* złożoności problemu lub dziedziny, aby osoba była w stanie wyrobić sobie świadomą opinię na temat swojej zdolności do pracy w tej dziedzinie.

Efekt Dunninga-Krugera był czasami używany do opisania powiązanego, ale niekoniecznie dorozumianego efektu, który można opisać jako „Im mniej dana osoba rozumie daną dziedzinę, tym bardziej prawdopodobne jest, że uwierzy, że może łatwo rozwiązać problemy w tej dziedzinie, ponieważ są bardziej skłonni do postrzegania domeny jako *prostej* ”. Ten bardziej ogólny efekt jest bardzo istotny w technologii. Sugerowałoby to, że ludzie mniej zaznajomieni z daną domeną, na przykład nietechniczni członkowie zespołu lub mniej doświadczeni członkowie zespołu, częściej *nie doceniają* wysiłku wymaganego do rozwiązania problemu w tej przestrzeni.

Wraz ze wzrostem zrozumienia i doświadczenia danej osoby w danej domenie, może ona napotkać inny efekt, który polega na tym, że mają tendencję do *przeceniania* zdolności *innych* lub *niedoceniania* własnych zdolności, ponieważ są tak doświadczeni w tej domenie. We wszystkich przypadkach skutki te są *zniekształceniami poznawczymi* . Podobnie jak w przypadku każdego uprzedzenia, zrozumienie, że może ono być obecne, często wystarczy, aby uniknąć wyzwań – ponieważ gdy istnieje świadomość uprzedzenia, można uwzględnić więcej danych wejściowych i opinii, aby spróbować wyeliminować te uprzedzenia. Ściśle pokrewnym jest nastawienie [iluzorycznej wyższości](https://pl.wikipedia.org/wiki/Z%C5%82udzenie_ponadprzeci%C4%99tno%C5%9Bci) .

Przykłady ze świata rzeczywistego:

- [Apple kontra FBI: Dlaczego ten Anti-Terror Hawk zmienił strony](https://fortune.com/2016/03/10/apple-fbi-lindsay-graham/) – w 2016 roku senator Lindsey Graham zmienił swoje stanowisko wobec Apple, tworząc „tylne drzwi” w szyfrowaniu urządzeń. Początkowo Graham był krytyczny wobec Apple kwestionującego prośbę o stworzenie „tylnych drzwi”, które uważał za konieczne do zbadania potencjalnych spisków terrorystycznych. Jednak, jak sam przyznał Graham, gdy dowiedział się więcej o technicznej złożoności tej domeny, zdał sobie sprawę, że założył, iż jest ona o wiele prostsza, niż sądził, i że takie tylne drzwi mogą mieć poważne negatywne konsekwencje. Potencjalnie można to uznać za przykład efektu Dunninga-Krugera – ekspert ds. cyberbezpieczeństwa prawdopodobnie natychmiast zrozumie, w jaki sposób można wykorzystać takie tylne drzwi, ponieważ mają dogłębne zrozumienie domeny, laik może założyć, że zabezpieczenia telefonu są bardziej podobne do *bezpieczeństwa fizycznego,* gdzie praktyka posiadania „klucza głównego” dla organów ścigania jest możliwa, ale ta analogia nie ma wystarczającego zastosowania do opisania współczesnego szyfrowania w cyberbezpieczeństwie.

### Prawo Fittsa

[Prawo Fittsa na Wikipedii](https://pl.wikipedia.org/wiki/Prawo_Fittsa)

Prawo Fittsa przewiduje, że czas potrzebny do przemieszczenia się do obszaru docelowego jest funkcją odległości do celu podzielonej przez szerokość celu.

<img width="300px" alt="Schemat: Prawo dopasowania" src="/images/Fitts_Law.svg">

*(Odniesienie do obrazu: Foobar628 z angielskiej Wikipedii, Creative Commons Attribution-Share Alike 3.0 Unported, https://en.wikipedia.org/wiki/Fitts%27s_law#/media/File:Fitts_Law.svg)*

Konsekwencje tego prawa nakazują, aby przy projektowaniu UX czy UI elementy interaktywne były jak największe, a odległość między obszarem uwagi użytkownika a elementem interaktywnym była jak najmniejsza. Ma to konsekwencje dla projektu, takie jak grupowanie zadań, które są często używane blisko siebie.

Formalizuje również koncepcję „magicznych rogów”, rogów ekranu, do których użytkownik może „przesuwać” myszą, aby łatwo trafić – czyli tam, gdzie można umieścić kluczowe elementy interfejsu użytkownika. Przycisk Start systemu Windows znajduje się w magicznym rogu, co ułatwia wybór, a jako interesujący kontrast, przycisk „zamknij okno” systemu MacOS *nie* znajduje się w magicznym rogu, co utrudnia przypadkowe trafienie.

Zobacz też:

- [Zdolność informacyjna układu ruchu człowieka w sterowaniu amplitudą ruchu.](https://www.semanticscholar.org/paper/The-information-capacity-of-the-human-motor-system-Fitts/634c9fde5f1c411e4487658ac738dcf18d98ea8d)

### Prawo Galla

[Prawo Galla na Wikipedii](https://en.wikipedia.org/wiki/John_Gall_(author)#Gall's_law)

> Niezmiennie okazuje się, że złożony system, który działa, wyewoluował z prostego systemu, który działał. Złożony system zaprojektowany od podstaw nigdy nie działa i nie można go załatać, aby działał. Musisz zacząć od nowa z działającym prostym systemem.
>
> ( [John Gall](https://en.wikipedia.org/wiki/John_Gall_(author)) )

Prawo Galla sugeruje, że próby *zaprojektowania* bardzo złożonych systemów mogą się nie powieść. Bardzo złożone systemy rzadko są budowane za jednym razem, ale zamiast tego ewoluują z prostszych systemów.

Klasycznym przykładem jest sieć ogólnoświatowa. W obecnym stanie jest to bardzo złożony system. Jednak początkowo został zdefiniowany jako prosty sposób udostępniania treści między instytucjami akademickimi. Odniósł duży sukces w realizacji tych celów i z czasem ewoluował, by stać się bardziej złożony.

Zobacz też:

- [KISS (Keep It Simple, Stupid)](#the-kiss-principle)

### Prawo Goodharta

[Prawo Goodharta na Wikipedii](https://en.wikipedia.org/wiki/Goodhart's_law)

> Jakakolwiek zaobserwowana prawidłowość statystyczna będzie miała tendencję do załamania się, gdy zostanie na nią nałożona presja w celach kontrolnych.
>
> *Karola Goodharta*

Również powszechnie określany jako:

> Kiedy miara staje się celem, przestaje być dobrą miarą.
>
> *Marilyn Strathern*

Prawo stanowi, że optymalizacje oparte na pomiarach mogą prowadzić do dewaluacji samego wyniku pomiaru. Nadmiernie selektywny zestaw miar ( [KPI](https://en.wikipedia.org/wiki/Performance_indicator) ) zastosowany na ślepo do procesu powoduje zniekształcony efekt. Ludzie mają tendencję do optymalizacji lokalnie, „ogrywając” system w celu spełnienia określonych wskaźników, zamiast zwracać uwagę na całościowy wynik swoich działań.

Przykłady ze świata rzeczywistego:

- Testy bez asertywności spełniają oczekiwania dotyczące pokrycia kodu, mimo że intencją metryki było stworzenie dobrze przetestowanego oprogramowania.
- Wynik wydajności programisty wskazywany przez liczbę zatwierdzonych wierszy prowadzi do nieuzasadnionego rozdęcia bazy kodu.

Zobacz też:

- [Prawo Goodharta: jak mierzenie niewłaściwych rzeczy prowadzi do niemoralnych zachowań](https://coffeeandjunk.com/goodharts-campbells-law/)
- [Dilbert o oprogramowaniu wolnym od błędów](https://dilbert.com/strip/1995-11-13)

### Brzytwa Hanlona

[Brzytwa Hanlona na Wikipedii](https://en.wikipedia.org/wiki/Hanlon%27s_razor)

> Nigdy nie przypisuj złośliwości tego, co adekwatnie tłumaczy się głupotą.
>
> Robert J. Hanlon

Zasada ta sugeruje, że działania prowadzące do negatywnych skutków nie były wynikiem złej woli. Zamiast tego negatywny wynik jest bardziej prawdopodobnie przypisywany tym działaniom i/lub wpływowi, który nie jest w pełni zrozumiały.

### Prawo Hicka (Prawo Hicka-Hymana)

[Prawo Hicka na Wikipedii](https://en.wikipedia.org/wiki/Hick%27s_law)

> Czas podejmowania decyzji rośnie logarytmicznie wraz z liczbą opcji do wyboru.
>
> William Edmund Hick i Ray Hyman

W poniższym równaniu `T` to czas na podjęcie decyzji, `n` to liczba opcji, a `b` to stała określona na podstawie analizy danych.

![Prawo Hicksa](/images/hicks_law.svg)

*(Odniesienie do obrazu: Creative Commons Attribution-Share Alike 3.0 Unported, https://en.wikipedia.org/wiki/Hick%27s_law)*

To prawo ma zastosowanie tylko wtedy, gdy liczba opcji jest *uporządkowana* , na przykład alfabetycznie. Jest to implikowane w logarytmie o podstawie dwa, co oznacza, że osoba podejmująca decyzje zasadniczo przeprowadza *wyszukiwanie binarne* . Jeśli opcje nie są dobrze uporządkowane, eksperymenty pokazują, że czas potrzebny jest liniowy.

Ma to znaczący wpływ na projektowanie interfejsu użytkownika; zapewnienie, że użytkownicy mogą łatwo przeszukiwać opcje, prowadzi do szybszego podejmowania decyzji.

W prawie Hicka wykazano również korelację między IQ a czasem reakcji, jak pokazano w [Speed of Information Processing: Developmental Change and Links to Intelligence](https://www.sciencedirect.com/science/article/pii/S0022440599000369) .

Zobacz też:

- [Prawo Fittsa](#fitts-law)

### Prawo Hofstadtera

[Prawo Hofstadtera na Wikipedii](https://en.wikipedia.org/wiki/Hofstadter%27s_law)

> Zawsze trwa to dłużej niż się spodziewasz, nawet biorąc pod uwagę prawo Hofstadtera.
>
> (Douglas Hofstadter)

Możesz usłyszeć to prawo, o którym mowa, patrząc na szacunki, jak długo coś potrwa. Wydaje się truizmem w tworzeniu oprogramowania, że nie jesteśmy zbyt dobrzy w dokładnym szacowaniu, ile czasu zajmie dostarczenie czegoś.

To jest z książki ' [Gödel, Escher, Bach: Wieczny złoty warkocz](#reading-list) '.

Zobacz też:

- [Lista lektur: Gödel, Escher, Bach: wieczny złoty warkocz](#reading-list)

### Prawo Hutbera

[Prawo Hutbera na Wikipedii](https://en.wikipedia.org/wiki/Hutber%27s_law)

> Poprawa oznacza pogorszenie.
>
> ( [Patryk Hutber](https://en.wikipedia.org/wiki/Patrick_Hutber) )

To prawo sugeruje, że ulepszenia systemu doprowadzą do pogorszenia innych części lub ukryją inne pogorszenie, prowadząc ogólnie do degradacji obecnego stanu systemu.

Na przykład, zmniejszenie opóźnienia odpowiedzi dla określonego punktu końcowego może spowodować dalsze problemy z przepustowością i pojemnością w przepływie żądań, wpływając na zupełnie inny podsystem.

### Cykl szumu i prawo Amary

[Cykl szumu na Wikipedii](https://en.wikipedia.org/wiki/Hype_cycle)

> Mamy tendencję do przeceniania wpływu technologii na krótką metę i niedoceniania jej na dłuższą metę.
>
> (Roy Amara)

Hype Cycle to wizualna reprezentacja ekscytacji i rozwoju technologii na przestrzeni czasu, pierwotnie wyprodukowana przez firmę Gartner. Najlepiej pokazać to za pomocą wizualizacji:

![Cykl szumu](/images/gartner_hype_cycle.png)

*(Odniesienie do obrazu: Jeremykemp z angielskiej Wikipedii, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=10547051)*

Krótko mówiąc, ten cykl sugeruje, że nowa technologia i jej potencjalny wpływ zwykle budzi ogromne zainteresowanie. Zespoły często szybko wskakują w te technologie i czasami są rozczarowane wynikami. Może to być spowodowane tym, że technologia nie jest jeszcze wystarczająco dojrzała lub aplikacje w świecie rzeczywistym nie są jeszcze w pełni zrealizowane. Po pewnym czasie zwiększają się możliwości technologii i praktyczne możliwości jej wykorzystania, a zespoły mogą wreszcie stać się produktywne. Cytat Roya Amary podsumowuje to w najbardziej zwięzły sposób: „Mamy tendencję do przeceniania wpływu technologii na krótką metę i niedoceniania na dłuższą metę".

### Prawo Hyruma (prawo niejawnych interfejsów)

[Prawo Hyruma w Internecie](http://www.hyrumslaw.com/)

> Przy wystarczającej liczbie użytkowników API nie ma znaczenia, co obiecujesz w kontrakcie: wszystkie obserwowalne zachowania Twojego systemu będą przez kogoś zależne.
>
> (Hyrum Wright)

Prawo Hyrum stanowi, że gdy masz *wystarczająco dużą liczbę konsumentów* API, wszystkie zachowania API (nawet te, które nie są zdefiniowane jako część umowy publicznej) w końcu staną się przez kogoś zależne. Trywialnym przykładem mogą być elementy niefunkcjonalne, takie jak czas odpowiedzi API. Bardziej subtelnym przykładem mogą być konsumenci, którzy polegają na zastosowaniu wyrażenia regularnego do komunikatu o błędzie w celu określenia *typu* błędu interfejsu API. Nawet jeśli kontrakt publiczny interfejsu API nie mówi nic o zawartości komunikatu, wskazując, że użytkownicy powinni użyć powiązanego kodu błędu, *niektórzy* użytkownicy mogą korzystać z komunikatu, a zmiana komunikatu zasadniczo przerywa interfejs API dla tych użytkowników.

Zobacz też:

- [Prawo nieszczelnych abstrakcji](#the-law-of-leaky-abstractions)
- [XKCD 1172](https://xkcd.com/1172/)

### Prawo Kernighana

> Debugowanie jest dwa razy trudniejsze niż pisanie kodu. Dlatego, jeśli piszesz kod tak sprytnie, jak to tylko możliwe, z definicji nie jesteś wystarczająco sprytny, aby go debugować.
>
> (Brian Kernighan)

Prawo Kernighana zostało nazwane na cześć [Briana Kernighana](https://en.wikipedia.org/wiki/Brian_Kernighan) i pochodzi z cytatu z książki Kernighana i Plaugera „ [Elementy stylu programowania”](https://en.wikipedia.org/wiki/The_Elements_of_Programming_Style) :

> Każdy wie, że debugowanie jest dwa razy trudniejsze niż pisanie programu. Więc jeśli jesteś tak sprytny, jak potrafisz, kiedy to piszesz, jak możesz to kiedykolwiek debugować?

Choć hiperboliczne, prawo Kernighana przedstawia argument, że prosty kod ma być lepszy od kodu złożonego, ponieważ debugowanie wszelkich problemów pojawiających się w kodzie złożonym może być kosztowne lub nawet niemożliwe.

Zobacz też:

- [Zasada KISS](#the-kiss-principle)
- [Filozofia Uniksa](#the-unix-philosophy)
- [Brzytwa Ockhama](#occams-razor)

### Prawo Linusa

[Prawo Linusa na Wikipedii](https://en.wikipedia.org/wiki/Linus%27s_law)

> Biorąc pod uwagę wystarczającą liczbę gałek ocznych, wszystkie błędy są płytkie.
>
> *Eric S. Raymond*

To prawo po prostu mówi, że im więcej ludzi widzi problem, tym większe prawdopodobieństwo, że ktoś już wcześniej widział i rozwiązał problem lub coś bardzo podobnego.

Chociaż pierwotnie był używany do opisywania wartości modeli open-source dla projektów, może być zaakceptowany dla każdego rodzaju projektu oprogramowania. Można go również rozszerzyć na procesy - więcej przeglądów kodu, więcej statycznej analizy i wielobranżowe procesy testowe sprawią, że problemy będą bardziej widoczne i łatwiejsze do zidentyfikowania.

Bardziej formalnym oświadczeniem może być:

> Mając wystarczająco dużą bazę beta-testerów i programistów, prawie każdy problem zostanie szybko scharakteryzowany i może zostać rozwiązany przez kogoś, kto już wcześniej spotkał się z podobnym problemem.

Prawo to zostało nazwane na cześć [Linusa Torvaldsa](https://en.wikipedia.org/wiki/Linus_Torvalds) w książce Erica S. Raymonda „ [Katedra i bazar](https://en.wikipedia.org/wiki/The_Cathedral_and_the_Bazaar) ”.

### Prawo Metcalfego

[Prawo Metcalfe'a na Wikipedii](https://en.wikipedia.org/wiki/Metcalfe's_law)

> W teorii sieci wartość systemu rośnie w przybliżeniu do kwadratu liczby użytkowników systemu.

Prawo to opiera się na liczbie możliwych połączeń parami w systemie i jest ściśle związane [z prawem Reeda](#reeds-law) . Odlyzko i inni argumentowali, że zarówno prawo Reeda, jak i prawo Metcalfe'a zawyżają wartość systemu, nie uwzględniając granic ludzkiego poznania na efektach sieciowych; zobacz [Numer Dunbara](#dunbars-number) .

Zobacz też:

- [Prawo Reeda](#reeds-law)
- [Numer Dunbara](#dunbars-number)

### prawo Moore'a

[Prawo Moore'a na Wikipedii](https://en.wikipedia.org/wiki/Moore%27s_law)

> Liczba tranzystorów w układzie scalonym podwaja się mniej więcej co dwa lata.

Prognozy Moore'a, często używane do zilustrowania szybkości, z jaką poprawiła się technologia półprzewodników i chipów, okazały się bardzo dokładne w okresie od lat 70. do późnych lat 2000. W ostatnich latach trend nieznacznie się zmienił, częściowo ze względu na [fizyczne ograniczenia dotyczące stopnia miniaturyzacji komponentów](https://en.wikipedia.org/wiki/Quantum_tunnelling) . Jednak postępy w zrównoleglaniu i potencjalnie rewolucyjne zmiany w technologii półprzewodnikowej i obliczeniach kwantowych mogą oznaczać, że prawo Moore'a może nadal obowiązywać przez dziesięciolecia.

### Prawo Murphy'ego / Prawo Soda

[Prawo Murphy'ego na Wikipedii](https://en.wikipedia.org/wiki/Murphy%27s_law)

> Wszystko, co może pójść nie tak, pójdzie nie tak.

Powiązane z [Edwardem A. Murphym, Jr](https://en.wikipedia.org/wiki/Edward_A._Murphy_Jr.) *Murphy's Law* stwierdza, że jeśli coś może pójść nie tak, to pójdzie nie tak.

To powszechne powiedzenie wśród programistów. Czasami nieoczekiwane dzieje się podczas tworzenia, testowania, a nawet produkcji. Może to być również związane z (bardziej powszechnym w brytyjskim angielskim) *Prawie Soda* :

> Jeśli coś może pójść nie tak, to w najgorszym możliwym momencie.

Te „prawa” są na ogół używane w komicznym sensie. Jednak zjawiska takie jak błąd [*potwierdzenia*](#TODO) i błąd [*selekcji*](#TODO) mogą skłaniać ludzi do nadmiernego podkreślania tych praw (w większości przypadków, gdy coś działa, pozostają niezauważone, jednak niepowodzenia są bardziej zauważalne i wywołują więcej dyskusji).

Zobacz też:

- [Błąd potwierdzenia](#TODO)
- [Odchylenie selekcji](#TODO)

### Brzytwa Ockhama

[Brzytwa Ockhama na Wikipedii](https://en.wikipedia.org/wiki/Occam's_razor)

> Nie należy mnożyć jednostek bez konieczności.
>
> Wilhelm z Ockhama

Brzytwa Ockhama mówi, że spośród kilku możliwych rozwiązań najbardziej prawdopodobnym rozwiązaniem jest to, które ma najmniejszą liczbę koncepcji i założeń. To rozwiązanie jest najprostsze i rozwiązuje tylko zadany problem, bez wprowadzania przypadkowych złożoności i ewentualnych negatywnych konsekwencji.

Zobacz też:

- [YAGNI](#yagni)
- [Brak srebrnej kuli: przypadkowa złożoność i zasadnicza złożoność](https://en.wikipedia.org/wiki/No_Silver_Bullet)

Przykład:

- [Rozwój oprogramowania szczupłego: eliminuj marnotrawstwo](https://en.wikipedia.org/wiki/Lean_software_development#Eliminate_waste)

### Prawo Parkinsona

[Prawo Parkinsona na Wikipedii](https://en.wikipedia.org/wiki/Parkinson%27s_law)

> Praca rozwija się tak, aby wypełnić czas dostępny na jej wykonanie.

W swoim pierwotnym kontekście ustawa ta opierała się na badaniach biurokracji. Można to pesymistycznie zastosować do inicjatyw rozwoju oprogramowania, zgodnie z teorią, że zespoły będą nieefektywne do czasu, gdy zbliżają się terminy, a następnie spieszą się, aby ukończyć pracę w terminie, co sprawia, że rzeczywisty termin jest nieco arbitralny.

Gdyby to prawo zostało połączone z prawem [Hofstadtera](#hofstadters-law) , osiągnięto jeszcze bardziej pesymistyczny punkt widzenia - praca rozszerzy się, aby wypełnić czas dostępny na jej ukończenie i *nadal będzie trwać dłużej niż oczekiwano* .

Zobacz też:

- [Prawo Hofstadtera](#hofstadters-law)

### Przedwczesny efekt optymalizacji

[Przedwczesna optymalizacja na WikiWikiWeb](http://wiki.c2.com/?PrematureOptimization)

> Przedwcześnie optymalizacja jest źródłem wszelkiego zła.
>
> [(Donald Knuth)](https://twitter.com/realdonaldknuth?lang=en)

W artykule Donald Knuth's [Structured Programming with Go To Statements](http://wiki.c2.com/?StructuredProgrammingWithGoToStatements) napisał: „Programiści marnują ogromne ilości czasu na myślenie lub martwienie się o szybkość niekrytycznych części swoich programów, a te próby wydajności mają naprawdę silny negatywny wpływ podczas debugowania i konserwacja są brane pod uwagę. Powinniśmy zapomnieć o małych wydajnościach, powiedzmy w 97% przypadków: **przedwczesna optymalizacja jest źródłem wszelkiego zła** . Jednak nie powinniśmy przepuszczać naszych możliwości w tych krytycznych 3%.”

Jednak *przedwczesną optymalizację* można zdefiniować (w mniej obciążonych terminach) jako optymalizację, zanim zorientujemy się, że jest to konieczne.

### Prawo Putta

[Prawo Putta na Wikipedii](https://en.wikipedia.org/wiki/Putt%27s_Law_and_the_Successful_Technocrat)

> Technologia jest zdominowana przez dwa typy ludzi, tych, którzy rozumieją to, czym nie zarządzają, i tych, którzy zarządzają tym, czego nie rozumieją.

Po prawie Putta często następuje następstwo Putta:

> Każda hierarchia techniczna z czasem rozwija inwersję kompetencji.

Stwierdzenia te sugerują, że ze względu na różne kryteria selekcji i trendy w organizacji grup, na szczeblach pracy organizacji technicznych znajdzie się pewna liczba wykwalifikowanych osób oraz pewna liczba osób na stanowiskach kierowniczych, które nie są świadome złożoności i wyzwań związanych z pracę, którą zarządzają. Może to być spowodowane zjawiskami takimi jak [Zasada Petera](#the-peter-principle) lub [Zasada Dilberta](#the-dilbert-principle) .

Należy jednak podkreślić, że takie przepisy są szerokimi uogólnieniami i mogą mieć zastosowanie do *niektórych* typów organizacji, a nie do innych.

Zobacz też:

- [Zasada Piotra](#the-peter-principle)
- [Zasada Dilberta](#the-dilbert-principle)

### Prawo Reeda

[Prawo Reeda na Wikipedii](https://en.wikipedia.org/wiki/Reed's_law)

> Użyteczność dużych sieci, w szczególności sieci społecznościowych, rośnie wykładniczo wraz z rozmiarem sieci.

Prawo to opiera się na teorii grafów, gdzie użyteczność skaluje się jako liczba możliwych podgrup, czyli szybciej niż liczba uczestników lub liczba możliwych połączeń parami. Odlyzko i inni argumentowali, że prawo Reeda zawyża użyteczność systemu, nie uwzględniając ograniczeń ludzkiego poznania w zakresie efektów sieciowych; zobacz [Numer Dunbara](#dunbars-number) .

Zobacz też:

- [Prawo Metcalfego](#metcalfes-law)
- [Numer Dunbara](#dunbars-number)

### Prawo zachowania złożoności (prawo Teslera)

[Prawo zachowania złożoności na Wikipedii](https://en.wikipedia.org/wiki/Law_of_conservation_of_complexity)

Prawo to mówi, że w systemie występuje pewna złożoność, której nie można zredukować.

Pewna złożoność systemu jest „nieumyślna”. Jest to konsekwencja złej struktury, błędów lub po prostu złego zamodelowania problemu do rozwiązania. Przypadkową złożoność można zmniejszyć (lub wyeliminować). Jednak pewna złożoność jest „wewnętrzna” jako konsekwencja złożoności nieodłącznie związanej z rozwiązywanym problemem. Tę złożoność można przenieść, ale nie można jej wyeliminować.

Ciekawym elementem tego prawa jest sugestia, że nawet uproszczenie całego systemu nie zmniejsza wewnętrznej złożoności, lecz *przenosi się na użytkownika* , który musi zachowywać się w bardziej złożony sposób.

### Prawo Demeter

[Prawo Demeter na Wikipedii](https://en.wikipedia.org/wiki/Law_of_Demeter)

> Nie rozmawiaj z nieznajomymi.

Prawo Demeter, znane również jako „zasada najmniejszej wiedzy”, jest zasadą projektowania oprogramowania, szczególnie istotną w językach obiektowych.

Stwierdza, że jednostka oprogramowania powinna rozmawiać tylko ze swoimi bezpośrednimi współpracownikami. Obiekt `A` z odwołaniem do obiektu `B` może wywoływać swoje metody, ale jeśli `B` ma odwołanie do obiektu `C` , `A` nie powinien wywoływać `C` s. Tak więc, jeśli `C` ma `doThing()` , `A` nie powinien wywoływać jej bezpośrednio; `B.getC().doThis()` .

Przestrzeganie tej zasady ogranicza zakres zmian, czyniąc je łatwiejszymi i bezpieczniejszymi w przyszłości.

### Prawo nieszczelnych abstrakcji

[Prawo nieszczelnych abstrakcji dotyczących Joela na oprogramowaniu](https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/)

> Wszystkie nietrywialne abstrakcje są do pewnego stopnia nieszczelne.
>
> ( [Joel Spolsky](https://twitter.com/spolsky) )

Prawo to stanowi, że abstrakcje, które są zwykle używane w obliczeniach w celu uproszczenia pracy ze skomplikowanymi systemami, w pewnych sytuacjach „wyciekają” elementy systemu bazowego, co powoduje, że abstrakcja zachowuje się w nieoczekiwany sposób.

Przykładem może być wczytanie pliku i odczytanie jego zawartości. Interfejsy API systemu plików są *abstrakcją* systemów jądra niższego poziomu, które same w sobie są abstrakcją fizycznych procesów związanych ze zmianą danych na talerzu magnetycznym (lub pamięci flash w przypadku dysku SSD). W większości przypadków zadziała abstrakcja traktowania pliku jako strumienia danych binarnych. Jednak w przypadku dysku magnetycznego sekwencyjny odczyt danych będzie *znacznie* szybszy niż dostęp losowy (ze względu na zwiększony narzut błędów stron), ale w przypadku dysku SSD ten narzut nie będzie obecny. Aby poradzić sobie z tym przypadkiem, należy zrozumieć podstawowe szczegóły (na przykład pliki indeksu bazy danych są skonstruowane tak, aby zmniejszyć obciążenie losowego dostępu), szczegóły implementacji „przecieków” abstrakcji, o których programista może być świadomy.

Powyższy przykład może stać się bardziej złożony, gdy zostanie wprowadzonych *więcej abstrakcji.* System operacyjny Linux umożliwia dostęp do plików przez sieć, ale reprezentowane lokalnie jako „normalne” pliki. Ta abstrakcja „przecieka” w przypadku awarii sieci. Jeśli programista traktuje te pliki jako „normalne” pliki, nie biorąc pod uwagę faktu, że mogą one podlegać opóźnieniom i awariom sieci, rozwiązania będą zawierały błędy.

Artykuł opisujący prawo sugeruje, że nadmierne poleganie na abstrakcjach w połączeniu ze słabym zrozumieniem procesów leżących u ich podstaw w rzeczywistości sprawia, że radzenie sobie z danym problemem w niektórych przypadkach *staje się bardziej złożone.*

Zobacz też:

- [Prawo Hyruma](#hyrums-law-the-law-of-implicit-interfaces)

Przykłady ze świata rzeczywistego:

- [Powolne uruchamianie programu Photoshop](https://forums.adobe.com/thread/376152) — problem, który napotkałem w przeszłości. Photoshop uruchamiałby się wolno, czasami zajmując kilka minut. Wydaje się, że problem polegał na tym, że podczas uruchamiania odczytuje informacje o bieżącej domyślnej drukarce. Jeśli jednak ta drukarka jest w rzeczywistości drukarką sieciową, może to zająć bardzo dużo czasu. *Abstrakcja* drukarki sieciowej prezentowanej systemowi podobnie do drukarki lokalnej powodowała problem dla użytkowników w sytuacjach słabej łączności.

### Prawo trywialności

[Prawo trywialności na Wikipedii](https://en.wikipedia.org/wiki/Law_of_triviality)

To prawo sugeruje, że grupy będą poświęcać znacznie więcej czasu i uwagi błahym lub kosmetycznym kwestiom niż poważnym i istotnym.

Powszechnie używanym fikcyjnym przykładem jest komitet zatwierdzający plany elektrowni jądrowej, który spędza większość czasu na omawianiu struktury szopy na rowery, a nie na znacznie ważniejszym projekcie samej elektrowni. Wniesienie wartościowego wkładu w dyskusje na bardzo duże, złożone tematy może być trudne bez wysokiego poziomu wiedzy merytorycznej lub przygotowania. Jednak ludzie chcą być postrzegani jako wnoszący cenny wkład. Stąd tendencja do skupiania zbyt dużej ilości czasu na drobnych szczegółach, które można łatwo wytłumaczyć, ale niekoniecznie mają one szczególne znaczenie.

Powyższy fikcyjny przykład doprowadził do użycia terminu „Zrzucanie rowerów” jako wyrażenia marnowania czasu na błahe szczegóły. Pokrewnym terminem jest „ [golenie](https://en.wiktionary.org/wiki/yak_shaving) jaka”, które oznacza pozornie nieistotną czynność, która jest częścią długiego łańcucha warunków wstępnych do głównego zadania.

### Filozofia Uniksa

[Filozofia Uniksa na Wikipedii](https://en.wikipedia.org/wiki/Unix_philosophy)

Filozofia Uniksa polega na tym, że komponenty oprogramowania powinny być małe i skoncentrowane na robieniu jednej konkretnej rzeczy dobrze. Może to ułatwić budowanie systemów poprzez komponowanie małych, prostych, dobrze zdefiniowanych jednostek, zamiast używania dużych, złożonych, wielozadaniowych programów.

Nowoczesne praktyki, takie jak „architektura mikrousług”, można traktować jako zastosowanie tego prawa, w którym usługi są małe, skoncentrowane i wykonują jedną konkretną rzecz, umożliwiając złożone zachowanie złożone z prostych elementów konstrukcyjnych.

### Zasada Skauta

[Reguła Skauta na O'Reilly](https://www.oreilly.com/library/view/97-things-every/9780596809515/ch08.html)

> Zawsze zostawiaj kod lepszy, niż go znalazłeś.
>
> (Robert C. Martin (Wujek Bob))

Oparta na „Zasadze Zwiadowcy”, która mówi, że „zawsze zostawiaj pole kempingowe czystsze, niż go znalazłeś”, zasada zwiadu w programowaniu to po prostu „zawsze pozostawiaj kod czystszy, niż go znalazłeś”.

Zostało to wprowadzone w pierwszym rozdziale książki [Czysty kod](https://www.goodreads.com/book/show/3735293-clean-code) autorstwa Boba Martina. Reguła sugeruje, że programiści powinni przeprowadzać „optymistyczne refaktoryzację”, co oznacza dążenie do poprawy ogólnej jakości kodu podczas pracy nad nim. Jeśli zauważysz błąd, spróbuj go naprawić lub wyczyść. Jednak przy wprowadzaniu zmian w kodzie, który wydaje się niepoprawny, warto pamiętać [o płocie Chestertona](#chestertons-fence) !

Zobacz też:

- [Lista lektur: czysty kod](#reading-list)
- [Płot Chestertona](#chestertons-fence)
- [Teoria zepsutych okien](#broken-windows-theory)

https://www.amazon.sg/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882

### Model Spotify

[Model Spotify w Spotify Labs](https://labs.spotify.com/2014/03/27/spotify-engineering-culture-part-1/)

Model Spotify to podejście do struktury zespołu i organizacji spopularyzowane przez „Spotify”. W tym modelu zespoły są zorganizowane wokół funkcji, a nie technologii.

Model Spotify popularyzuje również koncepcje plemion, gildii, oddziałów, które są innymi elementami ich struktury organizacyjnej.

Członkowie organizacji opisali, że rzeczywiste znaczenie tych grup zmienia się, ewoluuje i jest ciągłym eksperymentem. Fakt, że model jest *procesem w ruchu* , a nie stałym modelem, nadal prowadzi do różnych interpretacji struktury, które mogą opierać się na prezentacjach wygłaszanych przez pracowników na konferencjach. Oznacza to, że „migawki” mogą być „przepakowywane” przez osoby trzecie w *stałą strukturę* , co powoduje utratę dynamiki modelu.

### Zasada dwóch pizzy

> Jeśli nie możesz nakarmić drużyny dwiema pizzami, jest za duża.
>
> (Jeff Bezos)

Ta zasada sugeruje, że niezależnie od wielkości firmy, zespoły powinny być na tyle małe, aby mogły je nakarmić dwie pizze. Przekonanie to, przypisywane Jeffowi Bezosowi i Amazonowi, sugeruje, że duże zespoły są z natury nieefektywne. Potwierdza to fakt, że wraz ze wzrostem liczebności zespołu liniowo, powiązania między ludźmi rosną kwadratowo; w ten sposób koszt koordynacji i komunikacji również rośnie kwadratowo. Jeśli ten koszt koordynacji jest zasadniczo kosztowny, należy preferować mniejsze zespoły.

Liczbę powiązań między ludźmi można wyrazić jako `n(n-1)/2` gdzie n = liczba osób.

<img width="200px" alt="Kompletny wykres; Powiązania między ludźmi" src="/images/complete_graph.png">

### Prawo Wadlera

[Prawo Wadlera na wiki.haskell.org](https://wiki.haskell.org/Wadler's_Law)

> W każdym projekcie językowym całkowity czas poświęcony na omawianie funkcji z tej listy jest proporcjonalny do dwóch podniesionych do potęgi jej pozycji.
>
> 1. Semantyka
> 2. Składnia
> 3. Składnia leksykalna
> 4. Składnia leksykalna komentarzy
>
> (W skrócie, na każdą godzinę spędzoną na semantyce, 8 godzin zostanie poświęconych na składnię komentarzy).

Podobnie jak [Prawo](#the-law-of-triviality) trywialności, Prawo Wadlera mówi, że przy projektowaniu języka ilość czasu poświęcanego na struktury językowe jest nieproporcjonalnie duża w porównaniu z wagą tych cech.

Zobacz też:

- [Prawo trywialności](#the-law-of-triviality)

### Prawo Wheatona

[Połączenie](http://www.wheatonslaw.com/)

[Dzień Oficjalny](https://dontbeadickday.com/)

> Nie bądź kutasem.
>
> *Wila Wheatona*

Ukute przez Wila Wheatona (Star Trek: The Next Generation, The Big Bang Theory), to proste, zwięzłe i potężne prawo ma na celu zwiększenie harmonii i szacunku w profesjonalnej organizacji. Może być stosowany podczas rozmów ze współpracownikami, przeprowadzania przeglądów kodu, przeciwstawiania się innym punktom widzenia, krytykowania i ogólnie większości profesjonalnych interakcji między ludźmi.

## Zasady

Zasady są zazwyczaj bardziej prawdopodobne jako wytyczne dotyczące projektowania.

### Wszystkie modele są złe (prawo George'a Boxa)

[Wszystkie modele są złe](https://en.wikipedia.org/wiki/All_models_are_wrong)

> Wszystkie modele są błędne, ale niektóre są przydatne.
>
> *George Box*

Zasada ta sugeruje, że wszystkie modele systemów są wadliwe, ale dopóki nie są *zbyt* wadliwe, mogą być użyteczne. Zasada ta ma swoje korzenie w statystyce, ale odnosi się również do modeli naukowych i obliczeniowych.

Podstawowym wymaganiem większości oprogramowania jest modelowanie pewnego rodzaju systemu. Niezależnie od tego, czy modelowany system jest siecią komputerową, biblioteką, wykresem powiązań społecznościowych czy jakimkolwiek innym systemem, projektant będzie musiał określić odpowiedni poziom szczegółowości modelowania. Nadmierna szczegółowość może prowadzić do zbyt dużej złożoności, zbyt mała szczegółowość może uniemożliwić funkcjonowanie modelu.

Zobacz też:

- [Prawo nieszczelnych abstrakcji](#the-law-of-leaky-abstractions)

### Płot Chestertona

[Płot Chestertona na Wikipedii](https://en.wikipedia.org/wiki/Wikipedia:Chesterton%27s_fence)

> Nie należy przeprowadzać reform, dopóki nie zrozumie się uzasadnienia istniejącego stanu rzeczy.

Ta zasada jest istotna w inżynierii oprogramowania przy usuwaniu długu technicznego. Każda linia programu została z jakiegoś powodu napisana przez kogoś. Chesterton's Fence sugeruje, że należy starać się w pełni zrozumieć kontekst i znaczenie kodu przed jego zmianą lub usunięciem, nawet jeśli na pierwszy rzut oka wydaje się on zbyteczny lub niepoprawny.

Nazwa tej zasady pochodzi od opowiadania [GK Chestertona](https://en.wikipedia.org/wiki/G._K._Chesterton) . Mężczyzna natrafia na płot przecinający środek drogi. Skarży się burmistrzowi, że to bezużyteczne ogrodzenie przeszkadza i prosi o jego usunięcie. Burmistrz pyta, dlaczego w ogóle jest tam ogrodzenie. Kiedy mężczyzna mówi, że nie wie, burmistrz mówi: „Jeśli nie znasz jego przeznaczenia, na pewno nie pozwolę ci go usunąć. to."

### Efekt Morza Martwego

[Wpływ Morza Martwego na Bruce'a F. Webstera](http://brucefwebster.com/2008/04/11/the-wetware-crisis-the-dead-sea-effect/)

> „... [Z]iętniej utalentowani i skuteczni inżynierowie IT najczęściej odchodzą – by wyparować… [ci, którzy mają tendencję do pozostawania] w tyle [są] „pozostałościami” — najmniej utalentowanymi i skutecznymi inżynierami IT ”.
>
> *Bruce F. Webster*

„Efekt Morza Martwego” sugeruje, że w każdej organizacji umiejętności/talent/skuteczność inżynierów są często odwrotnie proporcjonalne do ich czasu w firmie.

Zazwyczaj wysoko wykwalifikowani inżynierowie łatwo znajdują zatrudnienie gdzie indziej i są to pierwsi. Inżynierowie, którzy mają przestarzałe lub słabe umiejętności, zwykle pozostają w firmie, ponieważ znalezienie pracy w innym miejscu jest trudne. Jest to szczególnie widoczne, jeśli w ciągu swojego czasu w firmie uzyskali dodatkowe podwyżki płac, ponieważ uzyskanie ekwiwalentnego wynagrodzenia w innym miejscu może być trudne.

### Zasada Dilberta

[Zasada Dilberta na Wikipedii](https://en.wikipedia.org/wiki/Dilbert_principle)

> Firmy mają tendencję do systematycznego awansowania niekompetentnych pracowników do kierownictwa, aby wydostać ich z przepływu pracy.
>
> *Scott Adams*

Koncepcja zarządzania opracowana przez Scotta Adamsa (twórcę komiksu Dilberta), Zasada Dilberta jest inspirowana [Zasadą Petera](#the-peter-principle) . Zgodnie z Zasadą Dilberta pracownicy, którzy nigdy nie byli kompetentni, są awansowani na stanowiska kierownicze w celu ograniczenia szkód, jakie mogą wyrządzić. Adams po raz pierwszy wyjaśnił tę zasadę w artykule Wall Street Journal z 1995 r., a następnie rozwinął ją w swojej książce biznesowej z 1996 r. [„Zasada Dilberta”](#reading-list) .

Zobacz też:

- [Zasada Piotra](#the-peter-principle)
- [Prawo Putta](#putts-law)

### Zasada Pareto (Zasada 80/20)

[Zasada Pareto na Wikipedii](https://en.wikipedia.org/wiki/Pareto_principle)

> Większość rzeczy w życiu nie jest rozłożona równomiernie.

Zasada Pareto sugeruje, że w niektórych przypadkach większość wyników pochodzi z mniejszości danych wejściowych:

- 80% określonego fragmentu oprogramowania można napisać w 20% całkowitego przydzielonego czasu (odwrotnie, najtrudniejsze 20% kodu zajmuje 80% czasu)
- 20% wysiłku daje 80% rezultatu
- 20% pracy tworzy 80% przychodów
- 20% błędów powoduje 80% awarii
- 20% funkcji powoduje 80% użytkowania

W latach czterdziestych amerykańsko-rumuński inżynier dr Joseph Juran, powszechnie uważany za ojca kontroli jakości, [zaczął stosować zasadę Pareto do kwestii jakości](https://en.wikipedia.org/wiki/Joseph_M._Juran) .

Ta zasada jest również znana jako: Reguła 80/20, Prawo Niewielu Witalnych oraz Zasada Rzadkości Czynników.

Przykłady ze świata rzeczywistego:

- W 2002 roku Microsoft poinformował, że naprawienie 20% najczęściej zgłaszanych błędów pozwoli wyeliminować 80% powiązanych błędów i awarii w Windows i Office ( [Reference](https://www.crn.com/news/security/18821726/microsofts-ceo-80-20-rule-applies-to-bugs-not-just-features.htm) ).

### Zasada Shirky

[Wyjaśnienie zasady Shirky](https://kk.org/thetechnium/the-shirky-prin/)

> Instytucje będą starały się zachować problem, którego są rozwiązaniem.
>
> *Glina Shirky*

Zasada Shirky sugeruje, że złożone rozwiązania – firma, branża lub technologia – mogą być tak skoncentrowane na problemie, który rozwiązują, że mogą nieumyślnie utrwalać sam problem. Może to być celowe (firma dążąca do znalezienia nowych niuansów problemu, które uzasadniają dalsze opracowywanie rozwiązania) lub nieumyślne (niezdolność lub niechęć do zaakceptowania lub zbudowania rozwiązania, które całkowicie rozwiąże problem lub go ominie).

Związany z:

- Słynny wiersz Uptona Sinclaira: *„Trudno jest sprawić, by człowiek coś zrozumiał, kiedy jego pensja zależy od tego, czy tego nie rozumie!”*
- *Dylemat innowatora* Claya Christensena

Zobacz też:

- [Zasada Pareto](#the-pareto-principle-the-8020-rule)

### Zasada Piotra

[Zasada Piotra na Wikipedii](https://en.wikipedia.org/wiki/Peter_principle)

> Ludzie w hierarchii mają tendencję do wznoszenia się do swojego „poziomu niekompetencji”.
>
> *Laurence J. Peter*

Koncepcja zarządzania opracowana przez Laurence'a J. Petera, Zasada Petera, wskazuje, że ludzie, którzy są dobrzy w swojej pracy, są awansowani, dopóki nie osiągną poziomu, na którym nie odnoszą już sukcesów (ich „poziom niekompetencji”). W tym momencie, ponieważ są bardziej starsi, jest mniej prawdopodobne, że zostaną usunięci z organizacji (chyba że osiągają spektakularnie złe wyniki) i nadal będą pełnić rolę, w której mają niewiele wrodzonych umiejętności, ponieważ ich oryginalne umiejętności, które ich uczyniły sukces niekoniecznie są umiejętnościami wymaganymi w nowej pracy.

Jest to szczególnie interesujące dla inżynierów – którzy początkowo zaczynają od głęboko technicznych ról, ale często mają ścieżkę kariery, która prowadzi do *zarządzania* innymi inżynierami – co wymaga zasadniczo innego zestawu umiejętności.

Zobacz też:

- [Zasada Dilberta](#the-dilbert-principle)
- [Prawo Putta](#putts-law)

### Zasada solidności (prawo Postela)

[Zasada solidności na Wikipedii](https://en.wikipedia.org/wiki/Robustness_principle)

> Bądź konserwatywny w tym, co robisz, bądź liberalny w tym, co akceptujesz od innych.

Zasada ta, często stosowana w tworzeniu aplikacji serwerowych, mówi, że to, co wysyłasz do innych, powinno być jak najmniejsze i zgodne, ale powinieneś dążyć do umożliwienia niezgodnych danych wejściowych, jeśli można je przetworzyć.

Celem tej zasady jest zbudowanie systemów, które są solidne, ponieważ mogą poradzić sobie ze źle sformułowanymi danymi wejściowymi, jeśli intencje mogą być nadal zrozumiałe. Jednak akceptowanie zniekształconych danych wejściowych może wiązać się z potencjalnymi implikacjami bezpieczeństwa, szczególnie jeśli przetwarzanie takich danych wejściowych nie jest dobrze przetestowane. Te implikacje i inne kwestie zostały opisane przez Erica Allmana w [Reconsidered The Robustness Principle Reconsidered](https://queue.acm.org/detail.cfm?id=1999945) .

Dopuszczenie niezgodnych danych wejściowych z czasem może osłabić zdolność protokołów do ewolucji, ponieważ realizatorzy będą w końcu polegać na tej liberalności w budowaniu swoich funkcji.

Zobacz też:

- [Prawo Hyruma](#hyrums-law-the-law-of-implicit-interfaces)

### SOLID

To jest akronim, który odnosi się do:

- S: [Zasada pojedynczej odpowiedzialności](#the-single-responsibility-principle)
- O: [Zasada otwarcia/zamknięcia](#the-openclosed-principle)
- L: [Zasada substytucji Liskov](#the-liskov-substitution-principle)
- I: [Zasada segregacji interfejsów](#the-interface-segregation-principle)
- D: [Zasada odwrócenia zależności](#the-dependency-inversion-principle)

Są to kluczowe zasady [programowania zorientowanego obiektowo](#todo) . Zasady projektowania, takie jak te, powinny być w stanie pomóc programistom w tworzeniu systemów łatwiejszych w utrzymaniu.

### Zasada pojedynczej odpowiedzialności

[Zasada pojedynczej odpowiedzialności na Wikipedii](https://en.wikipedia.org/wiki/Single_responsibility_principle)

> Każdy moduł lub klasa powinna mieć tylko jedną odpowiedzialność.

Pierwsza z zasad „ [SOLID](#solid) ”. Ta zasada sugeruje, że moduły lub klasy powinny robić jedną rzecz i tylko jedną rzecz. W bardziej praktycznym ujęciu oznacza to, że pojedyncza, niewielka zmiana w funkcji programu powinna wymagać zmiany tylko w jednym komponencie. Na przykład zmiana sposobu sprawdzania poprawności hasła pod kątem złożoności powinna wymagać zmiany tylko w jednej części programu.

Teoretycznie powinno to sprawić, że kod będzie bardziej niezawodny i łatwiejszy do zmiany. Wiedza, że zmieniany komponent ma tylko jedną odpowiedzialność, oznacza tylko, że *testowanie* tej zmiany powinno być łatwiejsze. Korzystając z wcześniejszego przykładu, zmiana składnika złożoności hasła powinna mieć wpływ tylko na funkcje związane ze złożonością hasła. O wiele trudniejsze może być uzasadnienie wpływu zmiany na element, który ma wiele obowiązków.

Zobacz też:

- [Programowanie obiektowe](#todo)
- [SOLID](#solid)

### Zasada otwarcia/zamknięcia

[Zasada otwarcia/zamknięcia na Wikipedii](https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle)

> Encje powinny być otwarte na rozszerzenie i zamknięte na modyfikację.

Druga z zasad „ [SOLID](#solid) ”. Zasada ta stwierdza, że encje (które mogą być klasami, modułami, funkcjami itd.) powinny mieć możliwość *rozszerzenia* ich zachowania, ale ich *istniejące* zachowanie nie powinno być modyfikowane.

Jako hipotetyczny przykład wyobraź sobie moduł, który jest w stanie zamienić dokument Markdown w HTML. Teraz wyobraź sobie, że do specyfikacji Markdown dodano nową składnię, która dodaje obsługę równań matematycznych. Moduł powinien być *otwarty do rozbudowy w* celu wdrożenia nowej składni matematycznej. Jednak istniejące implementacje składni (takie jak akapity, punktory itp.) powinny zostać *zamknięte przed modyfikacją* . Już działają, nie chcemy, żeby ludzie je zmieniali.

Ta zasada ma szczególne znaczenie w przypadku programowania obiektowego, w którym możemy projektować obiekty tak, aby można je było łatwo rozszerzać, ale unikamy projektowania obiektów, których istniejące zachowanie może zostać zmienione w nieoczekiwany sposób.

Zobacz też:

- [Programowanie obiektowe](#todo)
- [SOLID](#solid)

### Zasada substytucji Liskov

[Zasada substytucji Liskov na Wikipedii](https://en.wikipedia.org/wiki/Liskov_substitution_principle)

> Powinna istnieć możliwość zamiany typu na podtyp bez naruszania systemu.

Trzecia z zasad „ [SOLID](#solid) ”. Ta zasada mówi, że jeśli komponent opiera się na typie, powinien móc używać podtypów tego typu, bez awarii systemu lub konieczności poznania szczegółów tego podtypu.

Jako przykład wyobraźmy sobie, że mamy metodę, która odczytuje dokument XML ze struktury reprezentującej plik. Jeśli metoda używa typu podstawowego „plik”, to wszystko, co pochodzi od „plik”, powinno być możliwe do użycia w funkcji. Jeśli „plik” obsługuje wyszukiwanie wsteczne, a parser XML korzysta z tej funkcji, ale typ pochodny „plik sieciowy” nie powiedzie się podczas próby wyszukiwania wstecznego, wówczas „plik sieciowy” narusza tę zasadę.

Zasada ta ma szczególne znaczenie w przypadku programowania obiektowego, w którym hierarchie typów muszą być starannie modelowane, aby uniknąć dezorientacji użytkowników systemu.

Zobacz też:

- [Programowanie obiektowe](#todo)
- [SOLID](#solid)

### Zasada segregacji interfejsów

[Zasada segregacji interfejsów w Wikipedii](https://en.wikipedia.org/wiki/Interface_segregation_principle)

> Żaden klient nie powinien być zmuszany do polegania na metodach, których nie używa.

Czwarta z zasad „ [SOLID](#solid) ”. Zasada ta stanowi, że konsumenci komponentu nie powinni zależeć od funkcji tego komponentu, z którego faktycznie nie korzysta.

Jako przykład wyobraźmy sobie, że mamy metodę, która odczytuje dokument XML ze struktury reprezentującej plik. Musi tylko czytać bajty, przesuwać się do przodu lub do tyłu w pliku. Jeśli ta metoda wymaga aktualizacji z powodu zmiany niepowiązanej cechy struktury pliku (takiej jak aktualizacja modelu uprawnień używanego do reprezentowania bezpieczeństwa plików), zasada została unieważniona. Byłoby lepiej, gdyby plik zaimplementował interfejs „przeszukiwanego strumienia” i aby czytnik XML go używał.

Zasada ta ma szczególne znaczenie dla programowania obiektowego, w którym interfejsy, hierarchie i typy abstrakcyjne są używane w celu [zminimalizowania sprzężenia](#todo) między różnymi komponentami. [Wpisywanie kaczki](#todo) to metodologia, która wymusza tę zasadę, eliminując jawne interfejsy.

Zobacz też:

- [Programowanie obiektowe](#todo)
- [SOLID](#solid)
- [Pisanie kaczki](#todo)
- [Oddzielenie](#todo)

### Zasada odwrócenia zależności

[Zasada odwrócenia zależności na Wikipedii](https://en.wikipedia.org/wiki/Dependency_inversion_principle)

> Moduły wysokopoziomowe nie powinny być zależne od implementacji niskopoziomowych.

Piąta z zasad „ [SOLID](#solid) ”. Ta zasada stanowi, że komponenty orkiestrujące wyższego poziomu nie powinny znać szczegółów ich zależności.

Jako przykład wyobraź sobie, że mamy program, który odczytuje metadane ze strony internetowej. Przyjęlibyśmy, że główny komponent musiałby wiedzieć o komponencie, aby pobrać zawartość strony internetowej, a następnie komponent, który może odczytać metadane. Gdybyśmy wzięli pod uwagę inwersję zależności, główny składnik zależałby tylko od abstrakcyjnego komponentu, który może pobierać dane bajtowe, a następnie od abstrakcyjnego komponentu, który byłby w stanie odczytać metadane ze strumienia bajtów. Główny komponent nie wiedziałby o TCP/IP, HTTP, HTML itp.

Ta zasada jest złożona, ponieważ może się wydawać, że „odwraca” oczekiwane zależności systemu (stąd nazwa). W praktyce oznacza to również, że oddzielny składnik orkiestracji musi zapewniać prawidłowe implementacje typów abstrakcyjnych (np. w poprzednim przykładzie *coś* musi nadal zapewniać składnik czytnika metadanych — narzędzie do pobierania plików HTTP i czytnik metatagów HTML). Następnie dotyka wzorców, takich jak [Inversion of Control](#todo) i [Dependency Injection](#todo) .

Zobacz też:

- [Programowanie obiektowe](#todo)
- [SOLID](#solid)
- [Odwrócenie sterowania](#todo)
- [Wstrzykiwanie zależności](#todo)

### Zasada DRY

[Zasada DRY na Wikipedii](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)

> Każda wiedza musi mieć jedną, jednoznaczną, autorytatywną reprezentację w ramach systemu.

DRY to akronim od *Don't Repeat Yourself* . Ta zasada ma na celu pomóc programistom w zmniejszeniu powtarzalności kodu i utrzymaniu informacji w jednym miejscu i została przytoczona w 1999 roku przez Andrew Hunta i Dave'a Thomasa w książce [The Pragmatic Developer](https://en.wikipedia.org/wiki/The_Pragmatic_Programmer)

> Przeciwieństwem DRY byłoby *WET* (Write Everything Twice lub We Enjoy Typing).

W praktyce, jeśli masz tę samą informację w dwóch (lub więcej) różnych miejscach, możesz użyć DRY, aby połączyć je w jedną i ponownie wykorzystać w dowolnym miejscu.

Zobacz też:

- [Pragmatyczny programista](https://en.wikipedia.org/wiki/The_Pragmatic_Programmer)

### Zasada KISS

[KISS na Wikipedii](https://en.wikipedia.org/wiki/KISS_principle)

> Niech to będzie możliwie proste

Zasada KISS stwierdza, że większość systemów działa najlepiej, jeśli są proste, a nie skomplikowane; dlatego prostota powinna być kluczowym celem w projektowaniu i należy unikać niepotrzebnej złożoności. Pochodzące z US Navy w 1960 r. wyrażenie kojarzone jest z inżynierem lotniczym Kelly Johnson.

Zasadę tę najlepiej ilustruje historia Johnsona przekazującego zespołowi konstruktorów garść narzędzi, z wyzwaniem, że projektowany przez nich samolot odrzutowy musi być naprawiany przez przeciętnego mechanika w terenie w warunkach bojowych za pomocą tylko tych narzędzi. Stąd „głupia” odnosi się do związku między sposobem, w jaki rzeczy się psują, a wyrafinowaniem dostępnych narzędzi do ich naprawy, a nie możliwościami samych inżynierów.

Zobacz też:

- [Prawo Galla](#galls-law)

### YAGNI

[YAGNI na Wikipedii](https://en.wikipedia.org/wiki/You_ain%27t_gonna_need_it)

Jest skrótem dla ***Y** Ou **A** in't **G** onna **N** Id **i** t.*

> Zawsze wdrażaj rzeczy, kiedy naprawdę ich potrzebujesz, nigdy tylko wtedy, gdy tylko przewidujesz, że ich potrzebujesz.
>
> ( [Ron Jeffries](https://twitter.com/RonJeffries) ) (współzałożyciel XP i autor książki „Zainstalowane programowanie ekstremalne”)

Ta *zasada Extreme Programming* (XP) sugeruje, że programiści powinni wdrażać tylko te funkcje, które są potrzebne do natychmiastowych wymagań i unikać prób przewidywania przyszłości poprzez implementację funkcji, które mogą być potrzebne później.

Przestrzeganie tej zasady powinno zmniejszyć ilość niewykorzystanego kodu w kodzie i uniknąć marnowania czasu i wysiłku na funkcjonalność, która nie przynosi żadnej wartości.

Zobacz też:

- [Lista lektur: Zainstalowano ekstremalne programowanie](#reading-list)

### Błędy przetwarzania rozproszonego

[Błędy przetwarzania rozproszonego na Wikipedii](https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing)

Znane również jako *Błędy Przetwarzania w Sieci* , Błędy to lista przypuszczeń (lub przekonań) na temat przetwarzania rozproszonego, które mogą prowadzić do niepowodzeń w rozwoju oprogramowania. Założenia to:

- Sieć jest niezawodna
- Opóźnienie wynosi zero
- Przepustowość jest nieskończona
- Sieć jest bezpieczna
- Topologia się nie zmienia
- Jest jeden administrator
- Koszt transportu wynosi zero
- Sieć jest jednorodna

Pierwsze cztery pozycje zostały wymienione przez [Billa Joya](https://en.wikipedia.org/wiki/Bill_Joy) i [Toma Lyona](https://twitter.com/aka_pugs) około 1991 roku i po raz pierwszy sklasyfikowane przez [Jamesa Goslinga](https://en.wikipedia.org/wiki/James_Gosling) jako „Fallacies of Networked Computing”. [L. Peter Deutsch](https://en.wikipedia.org/wiki/L._Peter_Deutsch) dodał błędy 5, 6 i 7. Pod koniec lat 90. Gosling dodał ósmy błąd.

Grupa została zainspirowana tym, co działo się w tym czasie w [Sun Microsystems](https://en.wikipedia.org/wiki/Sun_Microsystems) .

Te błędy powinny być uważnie brane pod uwagę podczas projektowania kodu, który jest odporny; zakładając, że którykolwiek z tych błędów może prowadzić do wadliwej logiki, która nie radzi sobie z rzeczywistością i złożonością systemów rozproszonych.

Zobacz też:

- [Poszukiwanie mitów rozproszonego przetwarzania (część 1) — Vaidehi Joshi na Medium](https://medium.com/baseds/foraging-for-the-fallacies-of-distributed-computing-part-1-1b35c3b85b53)

## Lista rzeczy do przeczytania

Jeśli te koncepcje Cię zainteresowały, mogą Ci się spodobać następujące książki.

- [Czysty kod - Robert C. Martin](https://www.goodreads.com/book/show/3735293-clean-code) - Jedna z najbardziej szanowanych książek o tym, jak pisać czysty, łatwy w utrzymaniu kod.
- [Zainstalowane programowanie ekstremalne — Ron Jeffries, Ann Anderson, Chet Hendrikson](https://www.goodreads.com/en/book/show/67834) — Obejmuje podstawowe zasady programowania ekstremalnego.
- [Gödel, Escher, Bach: wieczny złoty warkocz - Douglas R. Hofstadter.](https://www.goodreads.com/book/show/24113.G_del_Escher_Bach) - Ta książka jest trudna do sklasyfikowania. [Prawo Hofstadtera](#hofstadters-law) pochodzi z książki.
- [Struktura i interpretacja programów komputerowych — Harold Abelson, Gerald Jay Sussman, Julie Sussman](https://www.goodreads.com/book/show/43713) — Jeśli byłeś studentem informatyki lub inżynierii elektrycznej na MIT lub Cambridge, było to twoje wprowadzenie do programowania. Powszechnie opisywany jako punkt zwrotny w życiu ludzi.
- [Katedra i Bazar - Eric S. Raymond](https://en.wikipedia.org/wiki/The_Cathedral_and_the_Bazaar) - zbiór esejów na temat open source. Ta książka była źródłem [Prawa Linusa](#linuss-law) .
- [Zasada Dilberta — Scott Adams](https://www.goodreads.com/book/show/85574.The_Dilbert_Principle) — Komiczne spojrzenie na korporacyjną Amerykę autorstwa autora, który stworzył [Zasadę Dilberta](#the-dilbert-principle) .
- [Miesiąc Mitycznego Człowieka — Frederick P. Brooks Jr.](https://www.goodreads.com/book/show/13629.The_Mythical_Man_Month) — Klasyczny tom poświęcony inżynierii oprogramowania. [Prawo Brooksa](#brooks-law) jest centralnym tematem książki.
- [Zasada Petera — Lawrence J. Peter](https://www.goodreads.com/book/show/890728.The_Peter_Principle) — Kolejne komiksowe spojrzenie na wyzwania większych organizacji i zarządzania ludźmi, źródło [Zasady Petera](#the-peter-principle) .

## Zasoby online

Kilka przydatnych zasobów i lektur.

- [CB Insights: 8 praw prowadzących do sukcesu w technologii: zasada 2 pizzy Amazona, zasada 80/20 i inne](https://www.cbinsights.com/research/report/tech-laws-success-failure) – interesujący opis niektórych praw, które miały duży wpływ na technologię.

## eBook w formacie PDF

Projekt jest dostępny jako eBook PDF, [pobierz najnowszy eBook PDF za pomocą tego linku](https://github.com/dwmkerr/hacker-laws/releases/latest/download/hacker-laws.pdf) lub sprawdź [stronę wydania](https://github.com/dwmkerr/hacker-laws/releases) starszych wersji.

Nowa wersja eBooka jest tworzona automatycznie po przekazaniu znacznika nowej wersji.

## Podcast

Hacker Laws pojawił się w [The Changelog](https://changelog.com/podcast/403) , możesz sprawdzić odcinek podcastu, korzystając z poniższego linku:

<a href="https://changelog.com/podcast/403" target="_blank"></a>

## Tłumaczenia

Dzięki wielu wspaniałym współpracownikom, Hacker Laws jest dostępny w wielu językach. Proszę rozważyć sponsorowanie moderatorów!

Język | Moderator | Status
--- | --- | ---
[🇮🇩 Bahasa Indonezja / indonezyjski](./translations/pt-BR.md) | [arywidiantara](https://github.com/arywidiantara) | [](https://gitlocalize.com/repo/2513/id?utm_source=badge)
[🇧🇷 Brasileiro/Brazylijski](./translations/pt-BR.md) | [Eugênio Moreira](https://github.com/eugenioamn) , [Leonardo Costa](https://github.com/leofc97) | [](https://gitlocalize.com/repo/2513/pt-BR?utm_source=badge)
[🇨🇳 中文 / chiński](https://github.com/nusr/hacker-laws-zh) | [Steve Xu](https://github.com/nusr) | Częściowo ukończony
[🇩🇪 Niemiecki / Niemiecki](./translations/de.md) | [Wiktor](https://github.com/viktodergunov) | [](https://gitlocalize.com/repo/2513/de?utm_source=badge)
[🇫🇷 francuski / francuski](./translations/fr.md) | [Kevin Bockelandt](https://github.com/KevinBockelandt) | [](https://gitlocalize.com/repo/2513/fr?utm_source=badge)
[🇬🇷 ελληνικά / grecki](./translations/el.md) | [Panagiotis Gourgaris](https://github.com/0gap) | [](https://gitlocalize.com/repo/2513/el?utm_source=badge)
[🇮🇹 Włoski/Włoski](https://github.com/csparpa/hacker-laws-it) | [Claudio Sparpaglione](https://github.com/csparpa) | Częściowo ukończony
[🇯🇵 JP 日本語 / japoński](./translations/jp.md) | [Fumikazu Fujiwara](https://github.com/freddiefujiwara) | [](https://gitlocalize.com/repo/2513/ja?utm_source=badge)
[🇰🇷 한국어 / koreański](https://github.com/codeanddonuts/hacker-laws-kr) | [Pączek](https://github.com/codeanddonuts) | Częściowo ukończony
[🇱🇻 Latviešu Valoda / łotewski](./translations/lv.md) | [Artur Jansons](https://github.com/iegik) | [](https://gitlocalize.com/repo/2513/lv?utm_source=badge)
[🇵🇱 Polski / Polish](./translations/pl.md) | [Mariusz Kogen](https://github.com/k0gen) | [](https://gitlocalize.com/repo/2513/pl?utm_source=badge)
[🇷🇺 Русская версия / rosyjski](https://github.com/solarrust/hacker-laws) | [Alena Batitskaja](https://github.com/solarrust) | Częściowo ukończony
[🇪🇸 Castellano / hiszpański](./translations/es-ES.md) | [Manuel Rubio](https://github.com/manuel-rubio) ( [Sponsor](https://github.com/sponsors/manuel-rubio) ) | Częściowo ukończony
[🇹🇷 Turecki / Turecki](https://github.com/umutphp/hacker-laws-tr) | [Umut Işik](https://github.com/umutphp) | [](https://gitlocalize.com/repo/2513/tr?utm_source=badge)
[🇺🇦 українська мова / ukraiński](./translations/uk.md) | [Nazar](https://github.com/troyane) , [Helga Łastiwka](https://github.com/HelgaLastivka) | [](https://gitlocalize.com/repo/2513/uk?utm_source=badge)

Jeśli chcesz zaktualizować tłumaczenie, postępuj zgodnie z [Przewodnikiem dla współtwórców tłumaczy](https://github.com/dwmkerr/hacker-laws/blob/main/.github/contributing.md#translations) .

## Powiązane projekty

- [Porada dnia](https://tips.darekkay.com/html/hacker-laws-en.html) — otrzymuj codzienne przepisy/zasady hakerskie.
- [Hacker Laws CLI](https://github.com/umutphp/hacker-laws-cli) - Lista, przeglądanie i oglądanie losowych przepisów z terminala!
- [Działanie na podstawie przepisów hakerskich](https://github.com/marketplace/actions/hacker-laws-action) — dodaje losowe prawo hakerskie do żądania ściągnięcia jako drobny prezent dla współtwórcy, dzięki [Umut Işık](https://github.com/umutphp)

## Przyczynianie się

Prosimy o wkład! [Zgłoś problem,](https://github.com/dwmkerr/hacker-laws/issues/new) jeśli chcesz zasugerować dodanie lub zmianę, lub [Otwórz żądanie ściągnięcia,](https://github.com/dwmkerr/hacker-laws/compare) aby zaproponować własne zmiany.

[Koniecznie przeczytaj Wytyczne dotyczące wkładu](./.github/contributing.md) , aby poznać wymagania dotyczące tekstu, stylu i tak dalej. Prosimy o zapoznanie się z [Kodeksem postępowania](./.github/CODE_OF_CONDUCT.md) podczas dyskusji na temat projektu.

## DO ZROBIENIA

Cześć! Jeśli wylądujesz tutaj, kliknąłeś link do tematu, którego jeszcze nie napisałem, przepraszam za to - prace w toku!

Możesz [zgłosić problem,](https://github.com/dwmkerr/hacker-laws/issues) prosząc o więcej szczegółów lub [otworzyć pull request,](https://github.com/dwmkerr/hacker-laws/pulls) aby przesłać proponowaną definicję tematu.
