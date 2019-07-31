# 💻📖 hacker-laws

Leggi, teorie, principi e pattern utili agli sviluppatori.

- 🇺🇸 [Traduzione in Inglese](https://github.com/dwmkerr/hacker-laws) - grazie [Dave Kerr](https://github.com/dwmkerr)!
- 🇨🇳 [中文 / Traduzione in Cinese](https://github.com/nusr/hacker-laws-zh) - grazie [Steve Xu](https://github.com/nusr)!
- 🇰🇷 [한국어 / Traduzione in Coreano](https://github.com/codeanddonuts/hacker-laws-kr) - grazie [Doughnut](https://github.com/codeanddonuts)!
- 🇷🇺 [Русская версия / Traduzione in Russo](https://github.com/solarrust/hacker-laws) - grazie [Alena Batitskaya](https://github.com/solarrust)!
- 🇹🇷 [Türkçe / Traduzione in Turco](https://github.com/umutphp/hacker-laws-tr) - grazie [Umut Işık](https://github.com/umutphp)!

---

<!-- vim-markdown-toc GFM -->

* [Introduzione](#introduzione)
* [Leggi](#leggi)
    * [Legge di Amdahl](#legge-di-amdahl)
    * [Legge di Brooks](#legge-di-brooks)
    * [Legge di Conway](#legge-di-conway)
    * [Numero di Dunbar](#numero-di-dunbar)
    * [Legge di Gall](#legge-di-gall)
    * [Rasoio di Hanlon](#rasoio-di-hanlon)
    * [Legge di Hofstadter](#legge-di-hofstadter)
    * [Legge di Hutber](#legge-di-hutber)
    * [Hype Cycle e Legge di Amara](#hype-cycle-e-legge-di-amara)
    * [Legge di Hyrum (Legge delle Interfacce Implicite)](#legge-di-hyrum-legge-delle-interfacce-implicite)
    * [Legge di Moore](#legge-di-moore)
    * [Legge di Parkinson](#legge-di-parkinson)
    * [Ottimizzazione Prematura](#effetto-di-ottimizzazione-prematura)
    * [Legge di Putt](#legge-di-putt)
    * [Legge di Conservazione della Complessità (Legge di Tesler)](#legge-di-conservazione-della-complessita-legge-di-tesler)
    * [Legge dell'Astrazione Fallata](#legge-dell-astrazione-fallata)
    * [Legge di Irrilevanza](#legge-di-irrilevanza)
    * [Filosofia Unix](#filosofia-unix)
    * [Il modello Spotify](#il-modello-spotify)
    * [Legge di Wadler](#legge-di-wadler)
* [Principi](#principi)
    * [Il Principo di Pareto (La regola dell'80/20)](#principio-di-pareto-regola-dell-80-20)
    * [Il Principio di Robustezza (Legge di Postel's)](#principio-di-robustezza-legge-di-postel)
    * [SOLID](#solid)
    * [Il Principio di Singola Responsabilità](#the-single-responsibility-principle)
    * [Il Principio dell'Aperto/Chiuso](#the-openclosed-principle)
    * [Il Principio di Sostituzione di Liskov](#the-liskov-substitution-principle)
    * [Il Principio di Segregazione delle Interfacce](#the-interface-segregation-principle)
    * [Il Principio di Inversione delle Dipendenze](#the-dependency-inversion-principle)
    * [Il Principio DRY](#the-dry-principle)
    * [YAGNI](#yagni)
* [Reading List](#reading-list)
* [TODO](#todo)

<!-- vim-markdown-toc -->

## Introduzione

Quando si parla di sviluppo software, si discute di tanti principi. Questo repository fornisce un riferimento e un'introduzione a quelli più comuni. I contributi sono sono ben accetti!


❗: Questo repo contiene la spiegazione di alcune leggi, principi e pattern, ma tuttavia non ne _sponsorizza_ nessuno. La loro applicabilità dovrebbe sempre essere discussa ed è sempre dipendente dal progetto specifico su cui state lavorando.

## Leggi

Si parte!

### Legge di Amdahl

[Legge di Amdahl su Wikipedia](https://it.wikipedia.org/wiki/Legge_di_Amdahl)

> La legge di Amdahl mostra lo _speedup potenziale_ che può essere raggiunto nell'esecuzione di un calcolo aumentando le risorse del sistema di calcolo. Di norma si usa nel calcolo parallelo e può stimare il beneficio atteso, limitato dalla porzione parallelizzabile del programma, e raggiungibile aumentando il numero di core di calcolo.

Ecco un esempio illustrativo. Se un programma è costituito da due parti - una parte A che deve essere eseguita da un singolo core di calcolo e una parte B che può essere parallelizzata - possiamo notare che aggiungere nuovi core al sistema di calcolo produce un beneficio limitato. L'aggiunta potenzia di molto la velocità di esecuzione della parte B - ma la velocità di esecuzione della parte A resterà la stessa.

Il diagramma sotto riportato illustra gli andamenti nel tempo della velocità di esecuzione in alcuni casi:

![Diagram: Amdahl's Law](./images/amdahls_law.png)

*(Crediti Immagine: Daniels220 su Wikipedia in lingua inglese, Creative Commons Attribution-Share Alike 3.0 Unported, https://en.wikipedia.org/wiki/File:AmdahlsLaw.svg)*

Come si può vedere, anche un programma che è al 50% parallelizzabile beneficerà molto poco dell'aggiunta di più di 10 core di calcolo, mentre un programma che è parallelizzabile al 95% può raggiungere speedup significativi nella velocità di esecuzione anche oltre 1000 core di calcolo aggiunti.

Dal momento che [la legge di Moore](#legge-di-moore) sta rallentando, e l'aumento della velocità dei singoli core di calcolo diminuisce, parallelizzare diventa la chiave per migliorare le performance. Un eccellente esempio è la grafica computerizzata: con i moderni Shader, è possibile renderizzare in parallelo pixel e frammenti - questo è il motivo per cui le schede grafiche hanno migliaia di core di calcolo (GPU o Shader Unit)

Vedi anche:

- [Legge di Brooks](#legge-di-brooks)
- [Legge di Moore](#legge-di-moore)

### Legge di Brooks

[Legge di Brooks su Wikipedia](https://it.wikipedia.org/wiki/Legge_di_Brooks)

> L'aggiunta di risorse umane ad un progetto di sviluppo software già in ritardo lo fa tardare ancora di più.

Questa legge suggerisce che in molti casi il tentativo di accelerare, tramite aggiunta di ulteriori persone a staff, la delivery di un progetto che è già in ritardo risulterà nell'aumento del ritardo progettuale. Brooks sottolinea che questo scenario è certamente molto semplificato, ma che tuttavia il ragionamento alla base è che il tempo necessario alle nuove risorse per diventare produttive e l'overhead di comunicazione introdotto causano una decrescita della velocità nel breve termine. Inoltre molti task risultano non suddivisibili o facilmente distribuibili tra più risorse, causando un corrispondente minor aumento nella velocità potenziale.

La famosa frase "Nove donne non fanno un figlio in un solo mese" è relativa alla Legge di Brook, in particolare al fatto che alcuni tipi di operazioni non sono suddivisibili o parallelizzabili.

Questo è un tema centrale del libro '[The Mythical Man Month](#reading-list)'.

Vedi anche:

- [Death March](#todo)
- [Reading List: The Mythical Man Month](#reading-list)

### Legge di Conway

[Legge di Conway su Wikipedia](https://it.wikipedia.org/wiki/Legge_di_Conway)

Questa legge indica che i confini di un sistema software riflettono la struttura dell'organizzazione che lo produce. Comunemente citata quando si parla di miglioramenti organizzativi, la legge di Conway afferma che se un'organizzazione è strutturata in tante piccole unità tra loro disconnesse, il software che essa produrrà avrà la stessa struttura. Se un'organizzazione invece è costruita attorno a "silo" verticali dedicati a funzionalità o servizi, i suoi sistemi software rifletteranno questa caratteristica.

Vedi anche:

- [Il modello Spotify](#il-modello-spotify)

### Numero di Dunbar

[Numero di Dunbar su Wikipedia](https://it.wikipedia.org/wiki/Numero_di_Dunbar)
"Il numero di Dunbar è stato suggerito come valore cognitivo che limita il numero di persone con cui un individuo riesce a mantenere relazioni sociali stabili - relazioni in cui l'individuo sa chi è ciascuna controparte e come tutte le controparti si relazionano tra di loro". Non c'è concordanza sull'esatto valore di questo limite. "... Dunbar ha affermato che un essere umano può mantenere solo 150 relazioni stabili". Egli ha inserito questa affermazione in un contesto più sociale: "il numero di persone con cui ti sentiresti a tuo agio a prendere un drink se entrassi in un bar e le incontrassi casualmente". Le stime per il numero generalmente stanno tra 100 e 250.

Come le relazioni stabili tra individui, le relazioni di uno sviluppatore con una codebase necessitano di impegno per essere mantenute. Quando ci troviamo di fronte a progetti grandi e complicati, o abbiamo la responsabilità di molti progetti, ci affidiamo a convenzioni, policy e procedure disegnate per scalare. Il numero di Dunbar non solo è importante da ricordare quando un ufficio cresce di dimensioni, ma anche quando si stabilisce il perimetro per l'operato di un team o quando si deve decidere se investire nella strumentazione per modellizzare e automatizzare l'overhead logistico. Inquadrando il numero di Dunbar in un contesto ingegneristico, esso rappresenta il numero di progetti (o la comoplessità normalizzata di un singolo progetto) sui quali un individuo si sentirebbe sicuro di lavorare a chiamata.

Vedi anche:

- [Legge di Conway](#legge-di-conway)

### Legge di Gall

[Legge di Gall su Wikipedia](https://en.wikipedia.org/wiki/John_Gall_(author)#Gall's_law)

> Un sistema di complessità elevata e che funziona è inevitabilmente evoluto a partire da un sistema più semplice che funzionava. Un sistema complesso disegnato da zero non funziona per definizione e non può essere modificato per funzionare: bisogna partire ripartire da un sistema semplice che funziona.
>
> ([John Gall](https://en.wikipedia.org/wiki/John_Gall_(author)))

La Legge di Gall implica che i tentativi di _disegnare_ un sistema ad alta complessità hanno alta probabilità di fallire. I sistemi complessi raramente sono costruiti in una sola iterazione, al contrario sono il risultato dell'evoluzione di sistemi più semplici.

Un classico esempio è il World Wide Web. Al suo stato attuale, è un sistema fortemente complesso. Tuttavia, inizialmente fu definito come un sistema semplice per condividere contenuti tra istituti accademici. Realizzò questo obiettivo con grande successo ed mutò nel tempo divenendo sempre più complesso al passare del tempo.

Vedi anche:

- [KISS (Keep It Simple, Stupid)](#TODO)

### Rasoio di Hanlon

[Rasoio di Hanlon su Wikipedia](https://it.wikipedia.org/wiki/Rasoio_di_Hanlon)

> Non attribuire mai a malafede quel che si può ragionevolmente spiegare con la stupidità.
>
> Robert J. Hanlon

Questo principio suggerisce che l'ottenimento di un risultato negativo con ogni probabilità non è dovuto alla volontà perversa di fallire quanto alla mancata comprensione (totale o parziale) dell'impatto delle proprie azioni.

### Legge di Hofstadter

[Legge di Hofstadter su Wikipedia](https://it.wikipedia.org/wiki/Legge_di_Hofstadter)

> Per fare una cosa ci vuole sempre più tempo di quanto si pensi, anche tenendo conto della Legge di Hofstadter.
>
> (Douglas Hofstadter)

Questa legge è citata quando si fanno le stime sulla durata di qualcosa. Nello campo dello sviluppo software sembra essere un assioma la tendenza ad essere poco bravi nello stimare con precisione quanto tempo verrà richiesto per le delivery.

La legge viene dal libro '[Gödel, Escher, Bach: An Eternal Golden Braid](#reading-list)'.

Vedi anche:

- [Reading List: Gödel, Escher, Bach: An Eternal Golden Braid](#reading-list)

### Legge di Hutber

[Legge di Hutber su Wikipedia](https://en.wikipedia.org/wiki/Hutber%27s_law)

> I miglioramenti spesso celano altri peggioramenti.
>
> ([Patrick Hutber](https://en.wikipedia.org/wiki/Patrick_Hutber))

La legge indica che i miglioramenti apportati ad una parte di un sistema porteranno ad un inevitabile deterioramento in altre sue parti, causando quindi un globale deterioramento nello stato corrente del sistema.

Per esempio, la diminuzione nella latenza di risposta di uno specifico end-point provoca un amumento nel throughput e problemi di capacity nel workflow di gestione delle richieste, impattando altri sottosistemi correlati.

### Hype Cycle e Legge di Amara

[Hype Cycle su Wikipedia](https://it.wikipedia.org/wiki/Hype_cycle)

> Tendiamo a sovrastimare l'impatto di una tecnologia sul breve termine e nel sottostimarlo sul lungo termine.
>
> (Roy Amara)

L'Hype Cycle è una rappresentazione visuale del clamore attorno allo sviluppo di una tecnologia nel tempo, originariamente ideata da Gartner. Un esempio:

![The Hype Cycle](./images/gartner_hype_cycle.png)

*(Crediti Immagine: Jeremykemp su Wikipedia in lingua inglese, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=10547051)*

In sintesi, il Cycle dice che tipicamente esiste un picco di frenesia quando nasce una nuova tecnologia riguardo i suoi potenziali impatti. I team di lavoro di solito adottano velocemente tali tecnologie e a volte si trovano scontenti del risultato. Ciò può essere dovuto all'immaturità della tecnologia, oppure alla mancanza di applicazioni reali significative. Dopo un certo periodo di tempo, le potenzialità della tecnologia aumentano e aumenta il numero delle opportunità concrete che essa offre, per cui i team di lavoro possono finalmente aumentare la loro produttività adottandola. La citazione di Roy Amara riassume in breve questa situazione - "Tendiamo a sovrastimare l'impatto di una tecnologia sul breve termine e nel sottostimarlo sul lungo termine".

### Legge di Hyrum (Legge delle Interfacce Implicite)

[Legge di Hyrum Online](http://www.hyrumslaw.com/)

> Dato un numero sufficientementa elevato di utenti di un'API,
> il contenuto del contratto di interfaccia non conta:
> tutti i comportamenti osservabili del sistema che espone l'API
> saranno utilizzati da questi utenti.
>
> (Hyrum Wright)

La lagge di Hyrum dice che quando un'API ha un _numero sufficientementa elevato di consumer_, tutti i comportamenti di essa (anche quelli non definiti come parte dell'interfaccia pubblica) prima o poi costituiranno una dipendenza lato consumer. Un esempio banale è quello degli aspetti non-funzionali come il tempo di risposta di un'API. Un esempio più profondo è quello di consumer che applicano una regex sui messaggi di errore dell'API per determinarne la *tipologia*. Anche se il contratto pubblico di interfaccia un'API non dice nulla riguardo al contenuto dei messaggi e suggerisce agli utentil'utilizzo dei codici di errore associati ai messaggi, _alcuni_ utenti possono comunque utilizzare i messaggi di errore a tal fine e dunque una modifica dei messaggi sostanzialmente rompe l'integrazione per questi utenti.

Vedi anche:

- [Legge dell'Astrazione Fallata](#legge-dell-astrazione-fallata)
- [XKCD 1172](https://xkcd.com/1172/)

### Legge di Moore

[Legge di Moore su Wikipedia](https://it.wikipedia.org/wiki/Legge_di_Moore)

> Il numero di transistor in un circuito integrato raddoppia approssimativamente ogni due anni.

Spesso utilizzata per illustrare il tasso con cui le tecnologie a semiconduttori e i chip migliorano nel tempo, la legge di Moore si è dimostrata molto accurata dagli anni Settanta fino alla fine dei Duemila. Più di recente il trend è lievemente cambiato, in parte a causa delle [limitazioni fisiche alla miniaturizzazione delle componenti elettroniche](https://it.wikipedia.org/wiki/Effetto_tunnel) ma tuttavia avanzamenti nel campo della parallelizzazione del calcolo e scoperte potenzialmente rivoluzionarie nel campo delle tecnologie a semiconduttori e nel quantum computing potrebbero portare la legge di Moore a valere anche nei prossimi decenni.

### Legge di Parkinson

[Legge di Parkinson su Wikipedia](https://it.wikipedia.org/wiki/La_legge_di_Parkinson)

> Il lavoro tende ad espandersi fino ad impiegare tutto il tempo disponibile per svolgerlo.

Nel suo contesto originale, questa legge era riferita agli studi sulla gestione della burocrazia. Può essere applicata in ottica pessimistica alle iniziative di sviluppo software, e in sostanza afferma che i team saranno inefficienti fino all'approssimarsi delle deadline e lavoreranno quindi di corsa per rispettare tali deadline rendendole, in un certo senso, arbitrarie.

Combinando la legge di Parkinson con la [Legge di Hofstadter](#legge-di-hofstadter), si ottiene una vista ancora più pessimistica: il lavoro tenderà ad espandersi fino ad impiegare tutto il tempo disponibile per svolgerlo e *in ogni caso richiederà più tempo di quanto previsto*.

Vedi anche:

- [Legge di Hofstadter](#legge-di-hofstadter)

### Effetto di Ottimizzazione Prematura

[Ottimizzazione Prematura su WikiWikiWeb](http://wiki.c2.com/?PrematureOptimization)

> L'ottimizzazione prematura è la radice di ogni male.
>
> [(Donald Knuth)](https://twitter.com/realdonaldknuth?lang=en)


Nella sua pubblicazione [Programmazione Strutturata con clausole Go To](http://wiki.c2.com/?StructuredProgrammingWithGoToStatements),
Donald Knuth scrisse: "I programmatori perdono un'enormità di tempo a preoccuparsi delle performance delle sezioni non critiche dei loro programmi, e i tentativi di efficientarle hanno in realtà un forte impatto negativo durante il debugging e la manutenzione. Dovremmo dimenticarci dei piccoli efficientamenti, che impattano circa il 97% del tempo di esecuzione: **l'ottimizzazione prematura è la radice di ogni male**. Di contro non dovremmo mai lasciarci sfuggire l'occasione di migliorare quel critico 3% del tempo di esecuzione."

L'_Ottimizzazione Prematura_ può essere definita (in termini meno coloriti) come l'attività di efficientamento fatta prima di avere evidenza della sua necessità.

### Legge di Putt

[Legge di Putt su Wikipedia](https://en.wikipedia.org/wiki/Putt%27s_Law_and_the_Successful_Technocrat)

> Il mondo della tecnologia è dominato da due tipi di persone: coloro che comprendono ciò che non gestiscono e coloro che gestiscono ciò che non comprendono.

La Legge di Putt è spesso accompagnata dal Corollario di Putt:

> Ogni gerarchia tecnica, genera un'inversione delle competenze con il passare del tempo.

Queste frasi suggeriscono che, a causa di svariati criteri di selezione e trend con cui i gruppi di lavoro si organizzano, ci sarà un certo numero di persone di vasta esperienza con ruoli tecnici operativi e un certo numero di ruoli manageriali che non sono in grado di comprendere la complessità e le sfide del contesto lavorativo che sono chiamati a gestire. Ciò si spiega con fenomeni come il [Principio di Peter](#TODO) o [La Legge di Dilbert](#TODO).

Tuttavia, è corretto specificare che Leggi come queste sono una grande generalizzazione e si applicano ad _alcuni_ tipi di organizzazione e non ad altri.

Vedi anche:

- [Principio di Peter](#TODO)
- [Legge di Dilbert](#TODO).


### Legge di Conservazione della Complessità (Legge di Tesler)

[Legge di Conservazione della Complessità su Wikipedia](https://en.wikipedia.org/wiki/Law_of_conservation_of_complexity)

Le Legge dice che in ogni sistema esiste un certo livello di complessità che non può essere ridotto.

Parte della complessità di un sistema è introdotta "inavvertitamente" ed è conseguenza della struttura imperfetta, degli errori o semplicemente di una modellizzazione errata del problema da risolvere. La complessità involontaria può essere ridotta (o eliminata). Tuttavia, parte della complessità è "intrinseca" ed è conseguenza della complessità inerente al problema da risolvere. Questa complessità può essere spostata ma non eliminata.

Un elemento interessante di questa Legge è che ci dice che anche semplificando l'intero sistema, la complessità intrinseca non viene ridotta ma viene _spostata sull'utente_, che deve di conseguenza interagire in modo più sofisticato con il sistema.


### Legge dell'Astrazione Fallata

[La Legge dell'Astrazione Fallata su Joel on Software](https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/)

> Tutte le astrazioni non banali sono in qualche modo fallate.
>
> ([Joel Spolsky](https://twitter.com/spolsky))

Questa legge afferma che le astrazioni generalmente usate in informatica per semplificare l'uso di sistemi complessi, in certe situazioni, lasceranno "trapelare" il dettaglio dei sistemi sottostanti facendo così funzionare l'astrazione in modo inaspettato.

Un esempio è l'apertura di un file e la lettura del suo contenuto. L'API di un file system è un'_astrazione_ del kernel di sistema, il quale è a sua volta un'astrazione dei processi fisici di modifica dei dati su un disco magnetico (o su una memoria flash nel caso di SSD). Nella maggior parte dei casi, l'astrazione di considerare il file come uno stream di dati binario funzionerà senza problemi. Tuttavia, nel caso di un disco magnetico, la lettura sequenziale dei dati sarà *significativamente* più veloce di un accesso random (per via dell'overhead dovuto ai page fault), ma nel caso di un disco SSD tale overhead non è presente. I dettagli implementativi dell'astrazione dovranno dunque essere compresi se si vuole gestire questo comportamento (ad esempio, i file indice di un database sono strutturati per ridurre l'overhead dell'accesso random), l'astrazione "fallata" lascerà trapelare questi dettagli che possono essere di interesse per il programmatore.

L'esempio di cui sopra può diventare anche più complesso quando vengono introdotte astrazioni _multiple_. Il sistema operativo Linux consente di accedere file attraverso una rete, rappresentandoli localmente come file "normali". Questa astrazione "farà acqua" se la rete verrà interrotta. Se uno sviluppatore trattasse questi file come file "noemali", senza considerare il fatto che possono essere soggetti alla latenza e alle interruzioni della rete, la soluzione sviluppata avrà un baco.

L'articolo che descrive questa Legge suggerisce che un'eccessiva fiducia nelle astrazioni, combinata con una scarsa comprensione del sistema sottostante, di fatto in alcuni casi _aumenta_ la complessità del problema da risolvere.

Vedi anche:

- [Legge di Hyrum (Legge delle Interfacce Implicite)](#legge-di-hyrum-legge-delle-interfacce-implicite)

Esempi dal mondo reale:

- [Partenza lenta di Photoshop](https://forums.adobe.com/thread/376152) - problema incontrato nel passato su Photoshop, che a volta impiegava minuti per avviarsi. Sembra che il problema fosse che all'avvio Photoshop leggeva informazioni sulla stampante di default. Tuttavia, se la stampante era una stampante di rete, questa lettura poteva impiegare un tempo molto lungo. L'_astrazione_ per cui la stampante di rete era presentata al sistema esattamente come una stampante locale causava quindi una situazione di estrema lentezza per gli utenti in condizioni di rete lenta.

### Legge di Irrilevanza

[Legge di Irrilevanza su Wikipedia](https://en.wikipedia.org/wiki/Law_of_triviality)

La Legge afferma che i team di lavoro tendono a dedicare molto più tempo e attenzione a dettagli irrilevanti o legati alla cosmesi del lavoro piuttosto che alle questioni serie e sostanziali.

Il tipico esempio fittizio usato per illustrare la Legge è quello di un comitato incaricato di approvare i piani per un impianto nucleare, che passa più tempo a discutere i dettagli del ripostiglio delle biciclette che a discutere il ben più importante design dell'impianto stesso. Può essere difficile a volte dare il giusto contributo quando si discute di argomenti grandi e complessi senza avere una preparazione o esperienza adeguata in merito. Tuttavia, le persone vogliono in genere mostrarsi attive nel collaborare fornendo input di valore. Da qui la tendenza a concentrarsi troppo sul dettaglio spiccio, che può essere discusso facilmente, ma non ha necessariamente rilevanza.

L'esempio fittizio ha portato all'utilizzo del termine "ripostiglio delle biciclette" come metafora della perdita di tempo sui dettagli di poca rilevanza. 

### Filosofia Unix

[La Filosofia Unix su Wikipedia](https://it.wikipedia.org/wiki/Filosofia_Unix)

La Filosofia Unix predica che le componenti software debbano essere piccole e mirate a implementare bene un solo scopo. Ciò rende più semplice costruire sistemi mediante composizione di unità piccole, semplici e ben definite, piuttosto che mediante composizione di programmi grossi, complessi e multi-purpose.

Le moderne prassi come le "Architettura a Microservizi" possono essere viste come applicazioni di questa Filosofia, per cui i servizi sono piccoli e focalizzati sul fare una cosa specifica, consentendo la creazione di comportamenti complessi mediante composizione di mattoni più semplici.

### Il modello Spotify

[Il modello Spotify su Spotify Labs](https://labs.spotify.com/2014/03/27/spotify-engineering-culture-part-1/)

Il modello Spotify è un approccio alla strutturazione del lavoro e dell'azienda che è stato reso popolare da Spotify. In questo modello, i team di lavoro sono organizzati attorno alle features invece che alle tecnologie.

Il modello Spotify rende inoltre popolari i concetti di Tribù, Gilda, Capitolo, che sono altre componenti della struttura organizzativa.


### Legge di Wadler

[Legge di Wadler su wiki.haskell.org](https://wiki.haskell.org/Wadler's_Law)

> Nella progettazione di qualsiasi linguaggio, il tempo totale impiegato a discutere un elemento di questa lista è proporzionale a 2 elevato alla potenza corrispondente alla posizione dell'elemento:
> 
> 0. Semantica
> 1. Sintassi
> 2. Sintassi lessicale
> 3. Sintassi lessicale dei commenti
> 
> (In breve: per ogni ora spesa a discutere della semantica, 8 ore saranno spese sulla sintassi dei commenti).

Similmente alla [Legge di Irrilevanza](#legge-di-irrilevanza), la Legge di Wadler afferma che nel design di un linguaggio di programmazione il tempo speso sulla discussione della struttura del linguaggio è sproporzionatamente alto se comparato con l'importanza delle feature discussa.

Vedi anche:

- [Legge di Irrilevanza](#legge-di-irrilevanza)

## Principi

I Principi sono in generale usabili come linee guida per il design.


### Principio di Pareto (regola dell'80-20)

[Il Principio di Pareto su Wikipedia](https://it.wikipedia.org/wiki/Principio_di_Pareto)

> Nella vita, la maggior parte delle cose non è distribuita equamente.

Il Principio di Pareto suggerisce che in alcuni casi, la maggior parte dei risultati è effetto di una minoranza degli input

- l'80% di un software è scrivibile nel 20% del tempo totale allocato per la sua scrittura (di contro, il 20% del codice, ossia le parti più complicate di esso, impiega l'80% del tempo)
- il 20% dell'effort produce l'80% del risultato
- il 20% del lavoro genera l'80% della revenue
- il 20% dei bachi genera l'80% dei crash
- il 20% delle features soddisfa l'80% degli utenti

Negli anni Quaranta l'ingegnere Americano-Rumeno Dr.Joseph Juran, che è riconosciuto universalmente come il padre del controllo di qualità, [iniziò ad applicare il Principio di Pareto alla quality assurance](https://en.wikipedia.org/wiki/Joseph_M._Juran)

Questo Principio è anche noto come: Regola dell'80/20, Legge dei Pochi ma Vitali e il Principio della Scarsità dei Fattori.

Esempi dal mondo reale:

- Nel 2002 la Microsoft riferì che sistemando il 20% dei bachi nella lista tra i più segnalati vennero sistemati l'80% degli errori e dei crash correlati su Windows e Office ([Riferimento](https://www.crn.com/news/security/18821726/microsofts-ceo-80-20-rule-applies-to-bugs-not-just-features.htm)).

### Principio di Robustezza (Legge di Postel)

[Il Principio di Robustezza su Wikipedia](https://en.wikipedia.org/wiki/Robustness_principle)

> Siate conservativi nelle vostre azioni, ma liberali in ciò che accettate dagli altri.

Spesso applicato allo sviluppo di applicazioni lato server, questo principio afferma che ciò viene inviato alle terze parti dovrebbe essere il più contenuto e standard possibile, e di contro si dovrebbe accettare anche input non-standard - fintanto che è processabile - in arrivo dalle terze parti.

L'obiettivo di questo principio è la costruzione di sistemi robusti in quanto possono gestire input malformato, a patto che l'intento degli input si possa ancora cogliere. Tuttavia l'accettazione di input malformati pone potenziali implicazioni a livello di sicurezza, soprattutto laddove non si testi a fondo l'ingestione di tali input.

### SOLID

SOLID è un acronimo:

* S: [Principio di Singola Responsabilità](#principio-di-singola-responsabilita)
* O: [Principio dell'Open Closed](#principio-dell-open-closed)
* L: [Principio di Sotituzione di Liskov](#principio-di-sostituzione-di-liskov)
* I: [Principio di Segregazione delle Interfacce](#principio-di-segregazione-delle-interfacce)
* D: [Principio di Inversione delle Dipendenze](#principio-di-inversione-delle-dipendenze)

These are key principles in [Object-Oriented Programming](#todo). Design principles such as these should be able to aid developers build more maintainable systems.

### Principio di Singola Responsabilità

[Principio di Singola Responsabilità su Wikipedia](https://it.wikipedia.org/wiki/Principio_di_singola_responsabilit%C3%A0)

> Ogni modulo o classe dovrebbe avere una sola responsabilità.

Il primo dei Principi '[SOLID](#solid)'. Afferma che i moduli o le classi software dovrebbero fare una e una sola cosa. In termini più pratici, ciò significa che una piccola modifica ad una feature di un programma dovrebbe richiedere la corrispondente modifica di una sola sua componente. Per esempio, cambiare il modo in cui la complessità di una password viene validata dovrebbe richiedere la modifica di una sola parte del programma.

In teoria, ciò dovrebbe garantire una maggiore robustezza del codice, con maggiore facilità di modifica. Sapere che un componente da cambiare ha una sola responsabilità ne semplifica grandemente il _testing_. Riprendendo l'esempio fatto prima, la modifica del componente che gestisce la validazione della password dovrebbe impattare solo le features di programma che sono correlate con la complessità della password. Di contro, testare un componente che ha svariate responsabilità diventa molto più difficoltoso.

Vedi anche:

- [Object-Oriented Programming](#todo)
- [SOLID](#solid)

### Principio dell'Open Closed

[Il Principio dell'Open Closed su Wikipedia](https://it.wikipedia.org/wiki/Principio_aperto/chiuso)

> Le entità software dovrebbero essere aperte all'estensione ma chiuse alla modifica.

Il secondo dei Principi '[SOLID](#solid)' afferma che le entità software (classi, moduli, funzioni) dovrebbero incoraggiare la possibilità di _estendere_ il proprio comportamento e scoraggiare la modifica del loro _comportamento esistente_

Ad esempio, si prenda un modulo in grado di trasformare un documento Markdown in HTML. Se il modulo può essere esteso per gestire una nuova feature proposta per il Markdown, senza doverne modificare il funzionamento interno, allora può definirsi aperto all'estensione. Se al contrario il modulo _non_ può essere modificato dai consumer nel modo in cui gestisce le feature correnti di Markdown, allora sarebbe _chiuso_ alla modifica.

Questo Principio è particolarmente rilevante nella programmazione orientata agli oggetti, dove è desiderabile progettare tipi di oggetti facilmente estendibili e il cui comportamento corrente non venga modificato in maniera inaspettata.

Vedi anche:

- [Object-Oriented Programming](#todo)
- [SOLID](#solid)

### Principio di Sotituzione di Liskov

[The Liskov Substitution Principle on Wikipedia](https://en.wikipedia.org/wiki/Liskov_substitution_principle)

> It should be possible to replace a type with a subtype, without breaking the system.

The third of the '[SOLID](#solid)' principles. This principle states that if a component relies on a type, then it should be able to use subtypes of that type, without the system failing or having to know the details of what that subtype is.

As an example, imagine we have a method which reads an XML document from a structure which represents a file. If the method uses a base type 'file', then anything which derives from 'file' should be able to be used in the function. If 'file' supports seeking in reverse, and the XML parser uses that function, but the derived type 'network file' fails when reverse seeking is attempted, then the 'network file' would be violating the principle.

This principle has particular relevance for object-oriented programming, where type hierarchies must be modeled carefully to avoid confusing users of a system.

See also:

- [Object-Oriented Programming](#todo)
- [SOLID](#solid)

### Principio di Segregazione delle Interfacce

[The Interface Segregation Principle on Wikipedia](https://en.wikipedia.org/wiki/Interface_segregation_principle)

> No client should be forced to depend on methods it does not use.

The fourth of the '[SOLID](#solid)' principles. This principle states that consumers of a component should not depend on functions of that component which it doesn't actually use.

As an example, imagine we have a method which reads an XML document from a structure which represents a file. It only needs to read bytes, move forwards or move backwards in the file. If this method needs to be updated because an unrelated feature of the file structure changes (such as an update to the permissions model used to represent file security), then the principle has been invalidated. It would be better for the file to implement a 'seekable-stream' interface, and for the XML reader to use that.

This principle has particular relevance for object-oriented programming, where interfaces, hierarchies and abstract types are used to [minimise the coupling](#todo) between different components. [Duck typing](#todo) is a methodology which enforces this principle by eliminating explicit interfaces.

See also:

- [Object-Oriented Programming](#todo)
- [SOLID](#solid)
- [Duck Typing](#todo)
- [Decoupling](#todo)

### Principio di Inversione delle Dipendenze

[Il Principio di Inversione delle Dipendenze su Wikipedia](https://it.wikipedia.org/wiki/Principio_di_inversione_delle_dipendenze)

> High-level modules should not be dependent on low-level implementations.

The fifth of the '[SOLID](#solid)' principles. This principle states that higher level orchestrating components should not have to know the details of their dependencies.

As an example, imagine we have a program which read metadata from a website. We would assume that the main component would have to know about a component to download the webpage content, then a component which can read the metadata. If we were to take dependency inversion into account, the main component would depend only on an abstract component which can fetch byte data, and then an abstract component which would be able to read metadata from a byte stream. The main component would not know about TCP/IP, HTTP, HTML, etc.

This principle is complex, as it can seem to 'invert' the expected dependencies of a system (hence the name). In practice, it also means that a separate orchestrating component must ensure the correct implementations of abstract types are used (e.g. in the previous example, _something_ must still provide the metadata reader component a HTTP file downloader and HTML meta tag reader). This then touches on patterns such as [Inversion of Control](#todo) and [Dependency Injection](#todo).

Vedi anche

- [Object-Oriented Programming](#todo)
- [SOLID](#solid)
- [Inversione del Controllo](#todo)
- [Iniezione delle Dipendenze](#todo)

### The DRY Principle

[The DRY Principle on Wikipedia](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)

> Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.

DRY is an acronym for _Don't Repeat Yourself_. This principle aims to help developers reducing the repetition of code and keep the information in a single place and was cited in 1999 by Andrew Hunt and Dave Thomas in the book [The Pragmatic Developer](https://en.wikipedia.org/wiki/The_Pragmatic_Programmer)

> The opposite of DRY would be _WET_ (Write Everything Twice or We Enjoy Typing).

In practice, if you have the same piece of information in two (or more) different places, you can use DRY to merge them into a single one and reuse it wherever you want/need.

See also:

- [The Pragmatic Developer](https://en.wikipedia.org/wiki/The_Pragmatic_Programmer)

### YAGNI

[YAGNI on Wikipedia](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it)

This is an acronym for _**Y**ou **A**ren't **G**onna **N**eed **I**t_.

> Always implement things when you actually need them, never when you just foresee that you need them.
>
> ([Ron Jeffries](https://twitter.com/RonJeffries)) (XP co-founder and author of the book "Extreme Programming Installed")

This _Extreme Programming_ (XP) principle suggests developers should only implement functionality that is needed for the immediate requirements, and avoid attempts to predict the future by implementing functionality that might be needed later.

Adhering to this principle should reduce the amount of unused code in the codebase, and avoid time and effort being wasted on functionality that brings no value.

See also:

- [Reading List: Extreme Programming Installed](#reading-list)


## Reading List

If you have found these concepts interesting, you may enjoy the following books.

- [Extreme Programming Installed - Ron Jeffries, Ann Anderson, Chet Hendrikson](https://www.goodreads.com/en/book/show/67834) - Covers the core principles of Extreme Programming.
- [The Mythical Man Month - Frederick P. Brooks Jr.](https://www.goodreads.com/book/show/13629.The_Mythical_Man_Month) - A classic volume on software engineering. [Brooks' Law](#brooks-law) is a central theme of the book.
- [Gödel, Escher, Bach: An Eternal Golden Braid - Douglas R. Hofstadter.](https://www.goodreads.com/book/show/24113.G_del_Escher_Bach) - This book is difficult to classify. [Hofstadter's Law](#hofstadters-law) is from the book.

## TODO

Hi! If you land here, you've clicked on a link to a topic I've not written up yet, sorry about this - this is work in progress!

Feel free to [Raise an Issue](https://github.com/dwmkerr/hacker-laws/issues) requesting more details, or [Open a Pull Request](https://github.com/dwmkerr/hacker-laws/pulls) to submit your proposed definition of the topic. 
