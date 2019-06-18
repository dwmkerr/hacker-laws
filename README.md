# 💻📖 hacker-laws-Brasil

Leis, Teorias, Principios e Padrões que desenvolvedores acham úteis.

- 🇨🇳 [中文 / Versão Chinesa ](https://github.com/nusr/hacker-laws-zh) - Obrigado [Steve Xu](https://github.com/nusr)!
- 🇰🇷 [한국어 / Versão Koreana](https://github.com/codeanddonuts/hacker-laws-kr) - Obrigado [Doughnut](https://github.com/codeanddonuts)!
- 🇷🇺 [Русская версия / Versão Russa](https://github.com/solarrust/hacker-laws) - Obrigado [Alena Batitskaya](https://github.com/solarrust)!
- 🇹🇷 [Türkçe / Versão Turka](https://github.com/umutphp/hacker-laws-tr) - Obrigado [Umut Işık](https://github.com/umutphp)

---

<!-- vim-markdown-toc GFM -->

* [Introdução](#Introdução)
* [Leis](#laws)
    * [Lei de Amdahl](#lei-de-amdahl)
    * [Lei de Brooks](#lei-de-brooks)
    * [Lei de Conway](#lei-de-conway)
    * [Numero de Dunbar](#lei-de-dunbar)
    * [Navalha de Hanlon](#lei-de-hanlon)
    * [Lei do Hofstadter](#lei-de-hofstadter)
    * [O Ciclo Hype & Lei de Amara](#o-ciclo-hype-e-lei-de-amara)
    * [Lei de Hyrum(A lei de interfaces implicitas)](#lei-de-hyrum-interfaces-implicitas)
    * [Lei de Moore](#lei-de-moore)
    * [Leo de Parkinson](#lei-de-parkinson)
    * [Lei de Putt](#lei-de-putt)
    * [A lei da Conservação de Complexidade (Lei de Tesler)](#lei-da-conservação-de-complexidade)
    * [A lei das Abstrações gotejantes](#lei-das-abstrações-gotejantes)
    * [A lei da Trivialidade](#lei-da-trivilidade)
    * [A Filosofia Unix](#filosofia-unix)
    * [O Modelo Spotify](#modelo-spotify)
    * [Lei do Wadler](#lei-de-wadler)
* [Principíos](#princípios)
    * [O Princípio de Pareto(A lei 80/20)](#principio-de-pareteo)
    * [O Princípio da Robustez (Lei de Postel)](#principio-da-robustez)
    * [SOLID](#solid)
    * [O Princípio da Responsabilidade Única](#principio-da-responsabilidade-unica)
    * [O Princípio Aberto/Fechado](#principio-aberto-fechado)
    * [O Princípio da Substituição Liskov ](#principio-da-substituição-Liskov)
    * [O Princípio da segregação de Interface](#principio-da-segregação-de-Interface)
    * [O Princípio da Inversão de Dependência](#principio-da-inversão-de-dependências)
    * [O princípio DRY](#principio-dry)
    * [YAGNI](#yagni)
* [Livros Recomendados](#lista-de-livros)
* [Em progresso](#em-progresso)

<!-- vim-markdown-toc -->

## Introdução

Existem muitas leis que as pessoas discutem quando falam sobre desenvolvimento. Esse repositório é uma referencia e uma visão global dos mais comuns. Sinta-se a vontade para contribuir e compartilhar.

<!--There are lots of laws which people discuss when talking about development. This repository is a reference and overview of some of the most common ones. Please share and submit PRs! <!-->

❗: Esse repositório comtém explicações sobre algumas léis, pincípios e padrões, mas não _advoca_ para nenhum. Se eles devem ser aplicados sempre é uma questão de debate, e depende diretamente no que você está trabalhando.

## Leis

Lá vamos nós!!

### Lei De Amdahl

[Lei de Amdahl na Wikipedia](https://pt.wikipedia.org/wiki/Lei_de_Amdahl)

> A lei de Amdahl, também conhecida como argumento de Amdahl, é usada para encontrar a máxima melhora esperada para um sistema em geral quando apenas uma única parte do mesmo é melhorada. Isto é frequentemente usado em computação paralela para prever o máximo speedup teórico usando múltiplos processadores. A lei possui o nome do Arquiteto computacional Gene Amdahl, e foi apresentada a AFIPS na Conferência Conjunta de Informática na primavera de 1967. 

Fica mais fácil de entender com um exemplo prático. Se um programa é feito de duas partes, parte A, que é executada por um processador único, e parte B, que pode ser feito paralelamente com N processadores. Se adicionarmos mais processaores ao sistema, só vai ter aumento nas tarefas relacionadas à parte B do programa. A velocidade de A se mantém a mesma.

O diagrama abaixo mostra alguns exemplos de melhoria na velocidade:

![Diagram: Lei de Amadhl](./images/amdahls_law.png)

*(Image Reference: By Daniels220 at English Wikipedia, Creative Commons Attribution-Share Alike 3.0 Unported, https://en.wikipedia.org/wiki/File:AmdahlsLaw.svg)*

Como pode-se perceber, mesmo um programa que teve metade da sua implementação de forma paralela, o benefício é menos de 10 _processing units_. Porém, um programa 95% paralelo, o ganho pode passar de 20 _processing units_.

### Lei de Brook

[Lei de Brooks na Wikipeia](https://en.wikipedia.org/wiki/Brooks%27s_law)


> Adicionar recursos humanos em um projeto, de desenvolvimento de sotware, atrasado, faz ficar ainda mais atrasado. 

Essa lei sugere que em muitos casos, na tentativa de acelerar uma entrega, que já está atrasada, adcionando mais pessoas atrasa ainda mais essa entrega. Brooke assume que essa afirmação é uma generalização excessiva, entretanto, o principal motivo para isso acontecer é dado pelo simples fato de adicionar pessoas requer um gasto com comunicação e construção de novos recursos para a equipe suportar novos membros. Logo, a curto prazo esse investimento não tem um retorno. Também existem tarefas que não podem ser dividias, portanto adicionar mais pessoas não vai fazer ela ser concluida mais rápido. 

"Nove mulheres não podem parir uma criança em um mês" e "Dois pilotos não fazem o carro ir mais rápido" são frases relacionadas a Lei de Brooke, principalmente porque algumas tarefas nao podem ser divididas.


Esse é um tema central do livro'[The Mythical Man Month](#lista-de-livros)'.

Veja também:

- [Death March](#em-progresso)
- [Livro: The Mythical Man Month](#lista-de-livros)

### Lei de Conway

[Lei de Conway na wikipedia](https://en.wikipedia.org/wiki/Conway%27s_law)

Essa lei sugere que limites técnicos de um sistema refletirão na estrutura da organização. Se uma organização é estruturada em pequenos setores, desconexas unidades, o sofware que ela produz sera assim também. Se uma organização é construida de forma vertical, em torno de funcionalidades e serviços, terá reflexo disso dentro do sistema.

Veja também:

- [Modelo do Spotify](#modelo-spotify)

### Número de Dunbar

[Número de Dunbar na Wikipedia](https://en.wikipedia.org/wiki/Dunbar%27s_number)

[Dumbar] propós que humanos só conseguem manter de forma confortável, 150 relacionamentos estáveis. Esse número está mais em um contexto social, "o número de pessoas que você não se sentiria sem graça para se juntar em uma bebiba se esbarrase com ela em um bar". Esse número geralmente está entra 100 e 250.

Esse número é uma sugestão cognitiva limite para o número de pessoass para qual consegue-se manter uma relação social estável.

Como uma relação entre pessoas, manter uma relação entre desenvolvedor e codigo requer esforço. É necessário usar politicas, padrões e procedimentos para encarar projetos complicados ou qualquer adversidade possível nesse tipo de relação. Número de Dunbar é importante em vários aspectos, não somente quando a empresa está em crescimento, mas também ao definir o escopo para os esforços da equipe ou decidir quando u msistema deve investir em ferramentas para axuliar na sobrecarga da logística. Colocando em contexto de engrenharia, é o número de projetos para os quais você se sentiria confiante para ingresssar em uma rotação de plantão de suporte.

Veja também:

- [Lei de Conwy](#lei-de-conway)

### Navalha de Hanlon

[Navalha de Hanlon na wikipedia](https://en.wikipedia.org/wiki/Hanlon%27s_razor)

> Nunca atribua à malícia aquilo que é adequadamente explicado por estupidez.
>
> Robert J. Hanlon

Esse principio sugeste que ações negativas não são sempre resultado de má vontade. Em vez disso, é mais provável que o resultado negativo seja atribuido à ações que não foram totalmente entendidas.



### Lei de Hofstadter

[Lei de Hofstadter na Wikipedia](https://en.wikipedia.org/wiki/Hofstadter%27s_law)


> Sempre leva mais tempo do que esperado, mesmo quando se leva em conta a lei do Hofstadter.
>
> Douglas Hofstadter

Você já deve ter ouvido sobre essa lei quando se fala em estimar tempo para fazer algo. Quando se fala em desenvolvimento de software parece obvio que nós tendemos a não sermos muitos precisos em estimar quando tempo levará para entregar alguma coisa.

This is from the book '[Gödel, Escher, Bach: An Eternal Golden Braid](#lista-de-livros)'.


### O Ciclo Hype e Lei de Amara


[The ciclo Hype on Wikipedia](https://en.wikipedia.org/wiki/Hype_cycle)

>Nós tendemos a superestimar os efeitos da tecnologia em curto prazo e subestimar os efeitos a longo prazo.
>
> Roy Amara

O Ciclo Hype é uma representação visual da empolgação e desenvolvimento da tecnologia ao longo do tempo, originalmente produzida por Gartner.
![The Hype Cycle](./images/gartner_hype_cycle.png)

*(Image Reference: By Jeremykemp at English Wikipedia, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=10547051)*

Em curto prazo, o cilco sugere que acontece uma explosão de empolgação a cerca de uma nova tecnologia e seu impácto em potencial. Equipes geralmente entram juntas nessas tecnlogias de forma rápida e em alguns casos ficam desapontados com os resutados. Uma das possíveis causas para isso é o fato da tecnologia em questão não ser madura o suficiente, ou aplicações do mundo real não estão totalmente prontas. Depois de um certo tempo, a capacidade da tecnologia aumenta e oportunidades práticas para uso dela aumentam, as equipes finalmente podem ser produtivos. A citação de Amara resume isso de forma sucinta - "Nós tendemos a superestimar os efeitos da tecnologia em curto prazo e subestimar os efeitos a longo prazo".


### Lei de Hyrum (A lei de interfaces implicitas)

[Lei de Hyrum site](http://www.hyrumslaw.com/)


>Com um número suficientes de clientes de uma API,
>não importa a sua pré-condição no contato:
>todos os comportamentos observáveis do seu sistema
>serão dependentes de alguém.
>
> (Hyrum Wright)

A lei de Hyrum sugere que quando voce tem um número muito grande de consumidores de uma API, todos os comportamentos dessa API(mesmo aqueles que não estão definidos como parte de um contrato público) eventualmente irão dependender de outra parte do sistema, ou outra API. Um exemplo trivial pode ser elementos não funcionais, como o tempo de resposta de uma API. Um exemplo mais sutil pode ser os consumidores que estão confiando em aplicar um regex a uma mensagem de erro para determinar o * tipo * de erro de uma API. Mesmo que o contrato público da API não especifique nada sobre o conteúdo da mensagem, indicando que os usuários devem usar um código de erro associado, _alguns usuários podem usar a mensagem e alterar a mensagem essencialmente interrompe a API para esses usuários.

Veja Também:

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
> (Joel Spolsky)

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


## Lista de Livros

If you have found these concepts interesting, you may enjoy the following books.

- [Extreme Programming Installed - Ron Jeffries, Ann Anderson, Chet Hendrikson](https://www.goodreads.com/en/book/show/67834) - Covers the core principles of Extreme Programming.
- [The Mythical Man Month - Frederick P. Brooks Jr.](https://www.goodreads.com/book/show/13629.The_Mythical_Man_Month) - A classic volume on software engineering. [Brooks' Law](#brooks-law) is a central theme of the book.
- [Gödel, Escher, Bach: An Eternal Golden Braid - Douglas R. Hofstadter.](https://www.goodreads.com/book/show/24113.G_del_Escher_Bach) - This book is difficult to classify. [Hofstadter's Law](#hofstadters-law) is from the book.

## TODO

Hi! If you land here, you've clicked on a link to a topic I've not written up yet, sorry about this - this is work in progress!

Feel free to [Raise an Issue](https://github.com/dwmkerr/hacker-laws/issues) requesting more details, or [Open a Pull Request](https://github.com/dwmkerr/hacker-laws/pulls) to submit your proposed definition of the topic. 
