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
    * [Legge di Conway](#conways-law)
    * [Legge di Dunbar](#dunbars-number)
    * [Legge di Gall](#galls-law)
    * [Rasoio di Hanlon](#hanlons-razor)
    * [Legge di Hofstadter](#hofstadters-law)
    * [Legge di Hutber](#hutbers-law)
    * [Hype Cycle e Legge di Amara](#the-hype-cycle--amaras-law)
    * [Legge di Hyrum (Legge delle Interfacce Implicite)](#hyrums-law-the-law-of-implicit-interfaces)
    * [Legge di Moore](#legge-di-moore)
    * [Legge di Parkinson](#parkinsons-law)
    * [Ottimizzazione Prematura](#premature-optimization-effect)
    * [Legge di Putt](#putts-law)
    * [Legge di Conservazione della Complessità (Legge di Tesler)](#the-law-of-conservation-of-complexity-teslers-law)
    * [Legge dell'Astrazione Colabrodo](#the-law-of-leaky-abstractions)
    * [Legge di Banalità](#the-law-of-triviality)
    * [La Filosofia di Unix](#the-unix-philosophy)
    * [Il modello Spotify](#the-spotify-model)
    * [Legge di Wadler](#wadlers-law)
* [Principi](#principles)
    * [Il Principo di Pareto (La regola dell'80/20)](#the-pareto-principle-the-8020-rule)
    * [Il Principio di Robustezza (Legge di Postel's)](#the-robustness-principle-postels-law)
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

*(Crediti Immagine: Daniels220 su Wikipedia EN, Creative Commons Attribution-Share Alike 3.0 Unported, https://en.wikipedia.org/wiki/File:AmdahlsLaw.svg)*

Come si può vedere, anche un programma che è al 50% parallelizzabile beneficerà molto poco dell'aggiunta di più di 10 core di calcolo, mentre un programma che è parallelizzabile al 95% può raggiungere speedup significativi nella velocità di esecuzione anche oltre 1000 core di calcolo aggiunti.

Dal momento che [la legge di Moore](#legge-di-moore) sta rallentando, e l'aumento della velocità dei singoli core di calcolo diminuisce, parallelizzare diventa la chiave per migliorare le performance. Un eccellente esempio è la grafica computerizzata: con i moderni Shader, è possibile renderizzare in parallelo pixel e frammenti - questo è il motivo per cui le schede grafiche hanno migliaia di core di calcolo (GPU o Shader Unit)

Vedi anche:

- [Legge di Brook](#legge-di-brook)
- [Legge di Moore](#legge-di-moore)

### Brooks' Law

[Legge di Brooks su Wikipedia](https://it.wikipedia.org/wiki/Legge_di_Brooks)

> L'aggiunta di risorse umane ad un progetto di sviluppo software già in ritardo lo fa tardare ancora di più.

Questa legge suggerisce che in molti casi il tentativo di accelerare, tramite aggiunta di ulteriori persone a staff, la delivery di un progetto che è già in ritardo risulterà nell'aumento del ritardo progettuale. Brooks sottolinea che questo scenario è certamente molto semplificato, ma che tuttavia il ragionamento alla base è che il tempo necessario alle nuove risorse per diventare produttive e l'overhead di comunicazione introdotto causano una decrescita della velocità nel breve termine. Inoltre molti task risultano non suddivisibili o facilmente distribuibili tra più risorse, causando un corrispondente minor aumento nella velocità potenziale.

La famosa frase "Nove donne non fanno un figlio in un solo mese" è relativa alla Legge di Brook, in particolare al fatto che alcuni tipi di operazioni non sono suddivisibili o parallelizzabili.

Questo è un tema centrale del libro '[The Mythical Man Month](#reading-list)'.

Vedi anche:

- [Death March](#todo)
- [Reading List: The Mythical Man Month](#reading-list)

### Conway's Law

[Conway's Law on Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_law)

This law suggests that the technical boundaries of a system will reflect the structure of the organisation. It is commonly referred to when looking at organisation improvements, Conway's Law suggests that if an organisation is structured into many small, disconnected units, the software it produces will be. If an organisation is built more around 'verticals' which are orientated around features or services, the software systems will also reflect this.

See also:

- [The Spotify Model](#the-spotify-model)

### Dunbar's Number

[Dunbar's Number on Wikipedia](https://en.wikipedia.org/wiki/Dunbar%27s_number)

"Dunbar's number is a suggested cognitive limit to the number of people with whom one can maintain stable social relationships— relationships in which an individual knows who each person is and how each person relates to every other person." There is some disagreement to the exact number. "... [Dunbar] proposed that humans can comfortably maintain only 150 stable relationships." He put the number into a more social context, "the number of people you would not feel embarrassed about joining uninvited for a drink if you happened to bump into them in a bar." Estimates for the number generally lay between 100 and 250.

Like stable relationships between individuals, a developer's relationship with a codebase takes effort to maintain. When faced with large complicated projects, or ownership of many projects we lean on convention, policy, and modeled procedure to scale. Dunbar's number is not only important to keep in mind as an office grows, but also when setting the scope for team efforts or deciding when a system should invest in tooling to assist in modeling and automating logistical overhead. Putting the number into an engineering context, it is the number of projects (or normalized complexity of a single project) for which you would feel confident in joining an on-call rotation to support.

See also:

- [Conway's Law](#conways-law)

### Gall's Law

[Gall's Law on Wikipedia](https://en.wikipedia.org/wiki/John_Gall_(author)#Gall's_law)

> A complex system that works is invariably found to have evolved from a simple system that worked. A complex system designed from scratch never works and cannot be patched up to make it work. You have to start over with a working simple system.
>
> ([John Gall](https://en.wikipedia.org/wiki/John_Gall_(author)))

Gall's Law implies that attempts to _design_ highly complex systems are likely to fail. Highly complex systems are rarely built in one go, but evolve instead from more simple systems.

The classic example is the world-wide-web. In it's current state, it is a highly complex system. However, it was defined initially as a simple way to share content between academic institutions. It was very successful in meeting these goals and evolved to become more complex over time.

See also:

- [KISS (Keep It Simple, Stupid)](#TODO)

### Hanlon's Razor

[Hanlon's Razor on Wikipedia](https://en.wikipedia.org/wiki/Hanlon%27s_razor)

> Never attribute to malice that which is adequately explained by stupidity.
>
> Robert J. Hanlon

This principle suggests that actions resulting in a negative outcome were not a result of ill will. Instead the negative outcome is more likely attributed to those actions and/or the impact being not fully understood.

### Hofstadter's Law

[Hofstadter's Law on Wikipedia](https://en.wikipedia.org/wiki/Hofstadter%27s_law)

> It always takes longer than you expect, even when you take into account Hofstadter's Law.
>
> (Douglas Hofstadter)

You might hear this law referred to when looking at estimates for how long something will take. It seems a truism in software development that we tend to not be very good at accurately estimating how long something will take to deliver.

This is from the book '[Gödel, Escher, Bach: An Eternal Golden Braid](#reading-list)'.

See also:

- [Reading List: Gödel, Escher, Bach: An Eternal Golden Braid](#reading-list)

### Hutber's Law

[Hutber's Law on Wikipedia](https://en.wikipedia.org/wiki/Hutber%27s_law)

> Improvement means deterioration.
>
> ([Patrick Hutber](https://en.wikipedia.org/wiki/Patrick_Hutber))

This law suggests that improvements to a system will lead to deterioration in other parts, or it will hide other deterioration, leading overall to a degradation from the current state of the system.

For example, a decrease in response latency for a particular end-point could cause increased throughput and capacity issues further along in a request flow, effecting an entirely different sub-system.

### The Hype Cycle & Amara's Law

[The Hype Cycle on Wikipedia](https://en.wikipedia.org/wiki/Hype_cycle)

> We tend to overestimate the effect of a technology in the short run and underestimate the effect in the long run.
>
> (Roy Amara)

The Hype Cycle is a visual representation of the excitement and development of technology over time, originally produced by Gartner. It is best shown with a visual:

![The Hype Cycle](./images/gartner_hype_cycle.png)

*(Image Reference: By Jeremykemp at English Wikipedia, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=10547051)*

In short, this cycle suggests that there is typically a burst of excitement around new technology and its potential impact. Teams often jump into these technologies quickly, and sometimes find themselves disappointed with the results. This might be because the technology is not yet mature enough, or real-world applications are not yet fully realised. After a certain amount of time, the capabilities of the technology increase and practical opportunities to use it increase, and teams can finally become productive. Roy Amara's quote sums this up most succinctly - "We tend to overestimate the effect of a technology in the short run and underestimate in the long run".

### Hyrum's Law (The Law of Implicit Interfaces)

[Hyrum's Law Online](http://www.hyrumslaw.com/)

> With a sufficient number of users of an API,
> it does not matter what you promise in the contract:
> all observable behaviours of your system
> will be depended on by somebody.
>
> (Hyrum Wright)

Hyrum's Law states that when you have a _large enough number of consumers_ of an API, all behaviours of the API (even those not defined as part of a public contract) will eventually come to be depended on by someone. A trivial example may be non-functional elements such as the response time of an API. A more subtle example might be consumers who are relying on applying a regex to an error message to determine the *type* of error of an API. Even if the public contract of the API states nothing about the contents of the message, indicating users should use an associated error code, _some_ users may use the message, and changing the message essentially breaks the API for those users.

See also:

- [The Law of Leaky Abstractions](#the-law-of-leaky-abstractions)
- [XKCD 1172](https://xkcd.com/1172/)

### Moore's Law

[Moore's Law on Wikipedia](https://en.wikipedia.org/wiki/Moore%27s_law)

> The number of transistors in an integrated circuit doubles approximately every two years.

Often used to illustrate the sheer speed at which semiconductor and chip technology has improved, Moore's prediction has proven to be highly accurate over from the 1970s to the late 2000s. In more recent years, the trend has changed slightly, partly due to [physical limitations on the degree to which components can be miniaturised](https://en.wikipedia.org/wiki/Quantum_tunnelling). However, advancements in parallelisation, and potentially revolutionary changes in semiconductor technology and quantum computing may mean that Moore's Law could continue to hold true for decades to come.

### Parkinson's Law

[Parkinson's Law on Wikipedia](https://en.wikipedia.org/wiki/Parkinson%27s_law)

> Work expands so as to fill the time available for its completion.

In its original context, this Law was based on studies of bureaucracies. It may be pessimistically applied to software development initiatives, the theory being that teams will be inefficient until deadlines near, then rush to complete work by the deadline, thus making the actual deadline somewhat arbitrary.

If this law were combined with [Hofstadter's Law](#hofstadters-law), an even more pessimistic viewpoint is reached - work will expand to fill the time available for its completion and *still take longer than expected*.

See also:

- [Hofstadter's Law](#hofstadters-law)

### Premature Optimization Effect

[Premature Optimization on WikiWikiWeb](http://wiki.c2.com/?PrematureOptimization)

> Premature optimization is the root of all evil.
>
> [(Donald Knuth)](https://twitter.com/realdonaldknuth?lang=en)

In Donald Knuth's paper [Structured Programming With Go To Statements](http://wiki.c2.com/?StructuredProgrammingWithGoToStatements), he wrote: "Programmers waste enormous amounts of time thinking about, or worrying about, the speed of noncritical parts of their programs, and these attempts at efficiency actually have a strong negative impact when debugging and maintenance are considered. We should forget about small efficiencies, say about 97% of the time: **premature optimization is the root of all evil**. Yet we should not pass up our opportunities in that critical 3%."

However, _Premature Optimization_ can be defined (in less loaded terms) as optimizing before we know that we need to.

### Putt's Law

[Putt's Law on Wikipedia](https://en.wikipedia.org/wiki/Putt%27s_Law_and_the_Successful_Technocrat)

> Technology is dominated by two types of people, those who understand what they do not manage and those who manage what they do not understand.

Putt's Law is often followed by Putt's Corollary:

> Every technical hierarchy, in time, develops a competence inversion.

These statements suggest that due to various selection criteria and trends in how groups organise, there will be a number of skilled people at working levels of a technical organisations, and a number of people in managerial roles who are not aware of the complexities and challenges of the work they are managing. This can be due to phenomena such as [The Peter Principle](#TODO) or [Dilbert's Law](#TODO).

However, it should be stressed that Laws such as this are vast generalisations and may apply to _some_ types of organisations, and not apply to others.

See also:

- [The Peter Principle](#TODO)
- [Dilbert's Law](#TODO).


### The Law of Conservation of Complexity (Tesler's Law)

[The Law of Conservation of Complexity on Wikipedia](https://en.wikipedia.org/wiki/Law_of_conservation_of_complexity)

This law states that there is a certain amount of complexity in a system which cannot be reduced.

Some complexity in a system is 'inadvertent'. It is a consequence of poor structure, mistakes, or just bad modeling of a problem to solve. Inadvertent complexity can be reduced (or eliminated). However, some complexity is 'intrinsic' as a consequence of the complexity inherent in the problem being solved. This complexity can be moved, but not eliminated.

One interesting element to this law is the suggestion that even by simplifying the entire system, the intrinsic complexity is not reduced, it is _moved to the user_, who must behave in a more complex way.

### The Law of Leaky Abstractions

[The Law of Leaky Abstractions on Joel on Software](https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/)

> All non-trivial abstractions, to some degree, are leaky.
>
> ([Joel Spolsky](https://twitter.com/spolsky))

This law states that abstractions, which are generally used in computing to simplify working with complicated systems, will in certain situations 'leak' elements of the underlying system, this making the abstraction behave in an unexpected way.

An example might be loading a file and reading its contents. The file system APIs are an _abstraction_ of the lower level kernel systems, which are themselves an abstraction over the physical processes relating to changing data on a magnetic platter (or flash memory for an SSD). In most cases, the abstraction of treating a file like a stream of binary data will work. However, for a magnetic drive, reading data sequentially will be *significantly* faster than random access (due to increased overhead of page faults), but for an SSD drive, this overhead will not be present. Underlying details will need to be understood to deal with this case (for example, database index files are structured to reduce the overhead of random access), the abstraction 'leaks' implementation details the developer may need to be aware of.

The example above can become more complex when _more_ abstractions are introduced. The Linux operating system allows files to be accessed over a network but represented locally as 'normal' files. This abstraction will 'leak' if there are network failures. If a developer treats these files as 'normal' files, without considering the fact that they may be subject to network latency and failures, the solutions will be buggy.

The article describing the law suggests that an over-reliance on abstractions, combined with a poor understanding of the underlying processes, actually makes dealing with the problem at hand _more_ complex in some cases.

See also:

- [Hyrum's Law](#hyrums-law-the-law-of-implicit-interfaces)

Real-world examples:

- [Photoshop Slow Startup](https://forums.adobe.com/thread/376152) - an issue I encountered in the past. Photoshop would be slow to startup, sometimes taking minutes. It seems the issue was that on startup it reads some information about the current default printer. However, if that printer is actually a network printer, this could take an extremely long time. The _abstraction_ of a network printer being presented to the system similar to a local printer caused an issue for users in poor connectivity situations.

### The Law of Triviality

[The Law of Triviality on Wikipedia](https://en.wikipedia.org/wiki/Law_of_triviality)

This law suggests that groups will give far more time and attention to trivial or cosmetic issues rather than serious and substantial ones.

The common fictional example used is that of a committee approving plans for nuclear power plant, who spend the majority of their time discussing the structure of the bike shed, rather than the far more important design for the power plant itself. It can be difficult to give valuable input on discussions about very large, complex topics without a high degree of subject matter expertise or preparation. However, people want to be seen to be contributing valuable input. Hence a tendency to focus too much time on small details, which can be reasoned about easily, but are not necessarily of particular importance.

The fictional example above led to the usage of the term 'Bike Shedding' as an expression for wasting time on trivial details.

### The Unix Philosophy

[The Unix Philosophy on Wikipedia](https://en.wikipedia.org/wiki/Unix_philosophy)

The Unix Philosophy is that software components should be small, and focused on doing one specific thing well. This can make it easier to build systems by composing together small, simple, well-defined units, rather than using large, complex, multi-purpose programs.

Modern practices like 'Microservice Architecture' can be thought of as an application of this law, where services are small, focused and do one specific thing, allowing complex behaviour to be composed of simple building blocks.

### The Spotify Model

[The Spotify Model on Spotify Labs](https://labs.spotify.com/2014/03/27/spotify-engineering-culture-part-1/)

The Spotify Model is an approach to team and organisation structure which has been popularised by 'Spotify'. In this model, teams are organised around features, rather than technologies.

The Spotify Model also popularises the concepts of Tribes, Guilds, Chapters, which are other components of their organisation structure.

### Wadler's Law

[Wadler's Law on wiki.haskell.org](https://wiki.haskell.org/Wadler's_Law)

> In any language design, the total time spent discussing a feature in this list is proportional to two raised to the power of its position.
> 
> 0. Semantics
> 1. Syntax
> 2. Lexical syntax
> 3. Lexical syntax of comments
> 
> (In short, for every hour spent on semantics, 8 hours will be spent on the syntax of comments).

Similar to [The Law of Triviality](#the-law-of-triviality), Wadler's Law states what when designing a language, the amount of time spent on language structures is disproportionately high in comparison to the importance of those features.

See also:

- [The Law of Triviality](#the-law-of-triviality)

## Principles

Principles are generally more likely to be guidelines relating to design.

### The Pareto Principle (The 80/20 Rule)

[The Pareto Principle on Wikipedia](https://en.wikipedia.org/wiki/Pareto_principle)

> Most things in life are not distributed evenly.

The Pareto Principle suggests that in some cases, the majority of results come from a minority of inputs:

- 80% of a certain piece of software can be written in 20% of the total allocated time (conversely, the hardest 20% of the code takes 80% of the time)
- 20% of the effort produces 80% of the result
- 20% of the work creates 80% of the revenue
- 20% of the bugs cause 80% of the crashes
- 20% of the features cause 80% of the usage

In the 1940s American-Romanian engineer Dr. Joseph Juran, who is widely credited with being the father of quality control, [began to apply the Pareto principle to quality issues](https://en.wikipedia.org/wiki/Joseph_M._Juran).

This principle is also known as: The 80/20 Rule, The Law of the Vital Few and The Principle of Factor Sparsity.

Real-world examples:

- In 2002 Microsoft reported that by fixing the top 20% of the most-reported bugs, 80% of the related errors and crashes in windows and office would become eliminated ([Reference](https://www.crn.com/news/security/18821726/microsofts-ceo-80-20-rule-applies-to-bugs-not-just-features.htm)).

### The Robustness Principle (Postel's Law)

[The Robustness Principle on Wikipedia](https://en.wikipedia.org/wiki/Robustness_principle)

> Be conservative in what you do, be liberal in what you accept from others.

Often applied in server application development, this principle states that what you send to others should be as minimal and conformant as possible, but you should be aim to allow non-conformant input if it can be processed.

The goal of this principle is to build systems which are robust, as they can handle poorly formed input if the intent can still be understood. However, there are potentially security implications of accepting malformed input, particularly if the processing of such input is not well tested.

### SOLID

This is an acronym, which refers to:

* S: [The Single Responsibility Principle](#the-single-responsibility-principle)
* O: [The Open/Closed Principle](#the-openclosed-principle)
* L: [The Liskov Substitution Principle](#the-liskov-substitution-principle)
* I: [The Interface Segregation Principle](#the-interface-segregation-principle)
* D: [The Dependency Inversion Principle](#the-dependency-inversion-principle)

These are key principles in [Object-Oriented Programming](#todo). Design principles such as these should be able to aid developers build more maintainable systems.

### The Single Responsibility Principle

[The Single Responsibility Principle on Wikipedia](https://en.wikipedia.org/wiki/Single_responsibility_principle)

> Every module or class should have a single responsibility only.

The first of the '[SOLID](#solid)' principles. This principle suggests that modules or classes should do one thing and one thing only. In more practical terms, this means that a single, small change to a feature of a program should require a change in one component only. For example, changing how a password is validated for complexity should require a change in only one part of the program.

Theoretically, this should make the code more robust, and easier to change. Knowing that a component which is being changed has a single responsibility only means that _testing_ that change should be easier. Using the earlier example, changing the password complexity component should only be able to affect the features which relate to password complexity. It can be much more difficult to reason about the impact of a change to a component which has many responsibilities.

See also:

- [Object-Oriented Programming](#todo)
- [SOLID](#solid)

### The Open/Closed Principle

[The Open/Closed Principle on Wikipedia](https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle)

> Entities should be open for extension and closed for modification.

The second of the '[SOLID](#solid)' principles. This principle states that entities (which could be classes, modules, functions and so on) should be able to have their behaviour _extended_, but that their _existing_ behaviour should not be able to be modified.

As a hypothetical example, imagine a module which is able to turn a Markdown document into HTML. If the module could be extended to handle a newly proposed markdown feature, without modifying the module internals, then it would be open for extension. If the module could _not_ be modified by a consumer so that how existing Markdown features are handled, then it would be _closed_ for modification.

This principle has particular relevance for object-oriented programming, where we may design objects to be easily extended, but would avoid designing objects which can have their existing behaviour changed in unexpected ways.

See also:

- [Object-Oriented Programming](#todo)
- [SOLID](#solid)

### The Liskov Substitution Principle

[The Liskov Substitution Principle on Wikipedia](https://en.wikipedia.org/wiki/Liskov_substitution_principle)

> It should be possible to replace a type with a subtype, without breaking the system.

The third of the '[SOLID](#solid)' principles. This principle states that if a component relies on a type, then it should be able to use subtypes of that type, without the system failing or having to know the details of what that subtype is.

As an example, imagine we have a method which reads an XML document from a structure which represents a file. If the method uses a base type 'file', then anything which derives from 'file' should be able to be used in the function. If 'file' supports seeking in reverse, and the XML parser uses that function, but the derived type 'network file' fails when reverse seeking is attempted, then the 'network file' would be violating the principle.

This principle has particular relevance for object-oriented programming, where type hierarchies must be modeled carefully to avoid confusing users of a system.

See also:

- [Object-Oriented Programming](#todo)
- [SOLID](#solid)

### The Interface Segregation Principle

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

### The Dependency Inversion Principle

[The Dependency Inversion Principle on Wikipedia](https://en.wikipedia.org/wiki/Dependency_inversion_principle)

> High-level modules should not be dependent on low-level implementations.

The fifth of the '[SOLID](#solid)' principles. This principle states that higher level orchestrating components should not have to know the details of their dependencies.

As an example, imagine we have a program which read metadata from a website. We would assume that the main component would have to know about a component to download the webpage content, then a component which can read the metadata. If we were to take dependency inversion into account, the main component would depend only on an abstract component which can fetch byte data, and then an abstract component which would be able to read metadata from a byte stream. The main component would not know about TCP/IP, HTTP, HTML, etc.

This principle is complex, as it can seem to 'invert' the expected dependencies of a system (hence the name). In practice, it also means that a separate orchestrating component must ensure the correct implementations of abstract types are used (e.g. in the previous example, _something_ must still provide the metadata reader component a HTTP file downloader and HTML meta tag reader). This then touches on patterns such as [Inversion of Control](#todo) and [Dependency Injection](#todo).

See also:

- [Object-Oriented Programming](#todo)
- [SOLID](#solid)
- [Inversion of Control](#todo)
- [Dependency Injection](#todo)

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
