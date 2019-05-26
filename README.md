# 💻📖 hacker-laws

Законы, теории, принципы и модели, которые полезно знать разработчикам.

- 🇺🇸 [English Version / Версия на Английском](https://github.com/dwmkerr/hacker-laws) - оригинальная версия о [Dave Kerr](https://github.com/dwmkerr).
- 🇨🇳 [中文 / Версия на Китайском](https://github.com/nusr/hacker-laws-zh) - спасибо [Steve Xu](https://github.com/nusr)!

---

<!-- vim-markdown-toc GFM -->

* [Вступление](#вступление)
* [Законы](#законы)
    * [Закон Амдала](#закон-амдала)
    * [Закон Брукса](#закон-брукса)
    * [Закон Конвея](#закон-конвея)
    * [Бритва Хэнлона](#бритва-хэнлона)
    * [Закон Хофштадтера](#закон-хофштадтера)
    * [Цикл хайпа и закон Амара](#цикл-хайпа-и-закон-амара)
    * [Закон Хайрама (Закон неявных интерфейсов)](#закон-хайрама-закон-неявных-интерфейсов)
    * [Закон Мура](#закон-мура)
    * [Закон Паркинсона](#закон-паркинсона)
    * [Putt's Law](#putts-law)
    * [The Law of Conservation of Complexity (Tesler's Law)](#the-law-of-conservation-of-complexity-teslers-law)
    * [Закон дырявых абстракций](#закон-дырявых-абстракций)
    * [The Law of Triviality](#the-law-of-triviality)
    * [The Unix Philosophy](#the-unix-philosophy)
    * [модель Спотифай](#модель-cпотифай)
    * [Wadler's Law](#wadlers-law)
* [Principles](#principles)
    * [The Pareto Principle (The 80/20 Rule)](#the-pareto-principle-the-8020-rule)
    * [The Robustness Principle (Postel's Law)](#the-robustness-principle-postels-law)
    * [SOLID](#solid)
    * [The Single Responsibility Principle](#the-single-responsibility-principle)
    * [The Open/Closed Principle](#the-openclosed-principle)
    * [The Liskov Substitution Principle](#the-liskov-substitution-principle)
    * [The Interface Segregation Principle](#the-interface-segregation-principle)
    * [The Dependency Inversion Principle](#the-dependency-inversion-principle)
    * [The DRY Principle](#the-dry-principle)
* [Список литературы](#список-литературы)
* [TODO](#todo)

<!-- vim-markdown-toc -->

---

## Вступление

Существует много законов, которые люди обсуждают, говоря о разработке. Этот репозиторий собрал в себе ссылки и обзоры наиболее распространённых. Пожалуйста, делитесь им и присылайте PR'ы!

❗: В этом репозитории содержатся объяснения некоторых законов, принципов и паттернов, но не _агитирует_ ни за один из них. Вопрос о том, стоит ли их применять, всегда будет предметом споров и в значительной степени ответ на него зависит от того, над чем вы работаете.

## Законы

Ну, поехали!

### Закон Амдала

[Закон Амдала в Википедии](https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%BA%D0%BE%D0%BD_%D0%90%D0%BC%D0%B4%D0%B0%D0%BB%D0%B0)

> Закон Амдала это формула, которая показывает потенциал увеличения скорости вычислительных задач, которого можно достичь путём увеличения ресурсов системы. Обычно используемый в параллельных вычислениях, он может предсказать фактическое преимущество увеличения числа процессоров, которое ограничено распараллеливанием программы. 

Лучше всего привести пример. Если программа состоит из двух частей, части А, которая должна выполняться одним процессором, и части Б, которая может выполняться параллельно, тогда мы увидим, что добавление нескольких процессоров в систему, может иметь ограниченное преимущество. Это потенциально может ускорить выполнение части Б, но скорость выполнения части А останется неизменной.

Диаграмма ниже показывает несколько примеров потенциального увеличения скорости:

![Диаграмма: Закон Амдала](./images/amdahls_law.png)

**(Источник изображения: авторство Daniels220, взято из Английской Википедии, Creative Commons Attribution-Share Alike 3.0 Unported, [https://en.wikipedia.org/wiki/File:AmdahlsLaw.svg](https://en.wikipedia.org/wiki/File:AmdahlsLaw.svg))**

Как можно видеть, программа с возможностью распараллеливания на 50% принесет очень мало пользы, всего 10 процессорных единиц, тогда как программа с возможностью распараллеливания на 95% может привести к значительному улучшению скорости на более чем тысячу процессорных единиц.

В то время как [Закон Мура](#закон-мура) замедляется, а скорость отдельных процессоров уменьшается, распараллеливание является ключом к повышению производительности. Графическое программирование является отличным примером — с современными вычислениями на основе шейдеров отдельные пиксели или фрагменты могут отображаться параллельно — вот почему современные графические карты часто имеют много тысяч процессорных ядер (графических процессоров или шейдерных блоков).

Читайте также:

- [Закон Брукса](#закон-брукса)
- [Закон Мура](#закон-мура)

-----

### Закон Брукса

[Закон Брукса в Википедии](https://ru.wikipedia.org/wiki/%D0%9C%D0%B8%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D1%87%D0%B5%D0%BB%D0%BE%D0%B2%D0%B5%D0%BA%D0%BE-%D0%BC%D0%B5%D1%81%D1%8F%D1%86#%D0%97%D0%B0%D0%BA%D0%BE%D0%BD_%D0%91%D1%80%D1%83%D0%BA%D1%81%D0%B0)

> Если проект не укладывается в сроки, то добавление рабочей силы задержит его ещё больше

Этот закон предполагает, что во многих случаях, попытка ускорить сдачу проекта, неукладывающегося в сроки, путём добавления людей в команду приведёт к ещё более позднему сроку сдачи. Брукс поясняет, что это излишнее упрощение, однако основное рассуждение заключается в том, что с учётом роста рабочего времени программистов и издержек коммуникации, в краткосрочной перспективе скорость значительно снижается.

Распространённое выражение «Девять женщин не могут выосить ребёнка за один месяц» отсылает нас как раз к закону Брука. В частности, к тому факту, что некоторые виды работ не могут быть поделены на части и запараллелены.

Эта мысль является центральной темой книги «[The Mythical Man Month](#список-литературы)».

Читайте также:

- [Death March](#todo)
- [Список литературы: The Mythical Man Month](#список-литературы)

---

### Закон Конвея

[Закон Конвея в Википедии](https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%BA%D0%BE%D0%BD_%D0%9A%D0%BE%D0%BD%D0%B2%D0%B5%D1%8F)

Этот закон предполагает, что технические рамки системы будут отражать структуру организации. Этот закон обычно упоминают в контексте улучшения организации. Закон Конвея предполагает, что если органиазция разделена на небольшие отдельные команды, то и программное обеспечение будет разделено подобным образом. Если организация выстроенна вокруг «вертикалей», которые ориентированны на улучшение и сервис, то система программного обеспечения будет отражать это.

Читайте также:

- [модель Спотифай](#модель-спотифай)

---

### Бритва Хэнлона

[Бритва Хэнлона в Википедии](https://ru.wikipedia.org/wiki/%D0%91%D1%80%D0%B8%D1%82%D0%B2%D0%B0_%D0%A5%D1%8D%D0%BD%D0%BB%D0%BE%D0%BD%D0%B0)

> Никогда не объясняйте злостью то, что адекватно объясняется глупостью.
>
> Роберт Джей Хэнлон

Этот принцип предполагает, что действие, приведшее к негативному результату, не является результатом злого умысла. В замен этого негативный результат скорее связан с тем, что это самое действие и/или его последствия были не до конца ясны.

---

### Закон Хофштадтера

[Закон Хофштадтера в Википедии](https://ru.wikipedia.org/wiki/%D0%A5%D0%BE%D1%84%D1%88%D1%82%D0%B0%D0%B4%D1%82%D0%B5%D1%80,_%D0%94%D1%83%D0%B3%D0%BB%D0%B0%D1%81#%D0%97%D0%B0%D0%BA%D0%BE%D0%BD_%D0%A5%D0%BE%D1%84%D1%88%D1%82%D0%B0%D0%B4%D1%82%D0%B5%D1%80%D0%B0)

> Любое дело всегда длится дольше, чем ожидается, даже если учесть закон Хофштадтера.
>
> Дуглас Хофштадтер

Кто-нибудь мог ссылаться на этот закон, глядя на оценку сроков выполнения чего-либо. Кажется трюизмом, что мы не очень хороши в оценке сроков разработки. 

Из книги «[Gödel, Escher, Bach: An Eternal Golden Braid](#список-литературы)».

Читайте также:

- [Список литературы: Gödel, Escher, Bach: An Eternal Golden Braid](#список-литературы)

---

### Цикл хайпа и закон Амара

[Цикл хайпа в Википедии](https://ru.wikipedia.org/wiki/Gartner#%D0%A6%D0%B8%D0%BA%D0%BB_%D1%85%D0%B0%D0%B9%D0%BF%D0%B0)

> Мы склонны переоценивать эффект от технологии в краткосрочной перспективе и недооценивать эффект в долгосрочной перспективе.
>
> Рой Амара

The Hype Cycle is a visual representation of the excitement and development of technology over time, originally produced by Gartner. It is best shown with a visual:

Цикл хайпа является визуализацией кривых волнения и развития технологии во времени. Впервые был представлен команией Gartner. Лучше показать на примере:

![Цикл хайпа](./images/gartner_hype_cycle.png)

**(Источник изображения: авторство Jeremykemp, взято из Английской Википедии, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=10547051)**

Если коротко, этот цикл предполагает что вкруг новой технологии обычно наблюдается взрыв ажиотажа относительно её потенциального воздействия. Команды часто поспешно _прыгают с головой_ в эту новую технологию, но в итоге оказываются разочаровываются результатом. Это может быть связанно с тем, что технология ещё не достаточно развита или приложения в реальном мире ещё не до конца реализованы. По прошествии времени возможности технологии возрастают и практическая польза от неё увеличивается. Что позволяет командам продуктивно использовать эту технологию. Рой Амара сформулировал это наиболее ёмко: «Мы склонны переоценивать эффект от технологии в краткосрочной перспективе и недооценивать эффект в долгосрочной перспективе».

---

### Закон Хайрама (Закон неявных интерфейсов)

[Закон Хайрама онлайн](http://www.hyrumslaw.com/)

> При достаточном количестве пользователей API
> не имеет особого значения что вы пишите в документации:
> любые наблюдаемые варианты поведения вашей системы
> будут на кого-то влиять.
>
> Хайрам Райт

Закон Хайрама гласит, что когда у вас есть _достаточно большое количество пользователей_ API, любое действия этого API (даже неопределеные в рамках публичной документации) в конечном итоге повлияют на кого-то. Тривиальный пример: нефункциональный элемент, такой, как время ответа API. Менее значительный пример: пользователи, которые опираются на использование регулярных выражений при определении **типа** ошибки API. Даже если публичная документация API не говорит ничего о тексте сообщения ошибки, явно указывая, что нужно смотреть на код ошибки, _некоторые_ пользователи могут использовать текст сообщения и изменение этого текста приводит к поломке API у таких юзеров.

Читайте также:

- [Закон дырявых абстракций](#закон-дырявых-абстракций)
- [XKCD 1172](https://xkcd.com/1172/)

---

### Закон Мура

[Закон Мура в Википедии](https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%BA%D0%BE%D0%BD_%D0%9C%D1%83%D1%80%D0%B0)

> Количество транзисторов в интегральной схеме удваивается примерно каждые два года

Часто используемый для иллюстрации стремительной скорости, с которой улучшаются технологии производства полупроводников и чипов, прогноз Мура был очень точен на отрезке с 1970 по 2000. В последние годы эта тенденция немного изменилась, в частности из-за [физических ограничений на степень миниатюризации компонентов](https://ru.wikipedia.org/wiki/%D0%A2%D1%83%D0%BD%D0%BD%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9_%D1%8D%D1%84%D1%84%D0%B5%D0%BA%D1%82). И тем не менее, достижения в области распараллеливания и потенциальные революционные изменения в технологии полупроводников, а также квантовые компьютеры могут означать, что закон Мура останеться актуальным на протяжении следующих десятелетий.

---

### Закон Паркинсона

[Закон Паркинсона в Википедии](https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%BA%D0%BE%D0%BD_%D0%9F%D0%B0%D1%80%D0%BA%D0%B8%D0%BD%D1%81%D0%BE%D0%BD%D0%B0)

> Работа заполняет время, отпущенное на неё

В оригинальном контексте этот закон был сформулирован в ходе изучения бюрократии. Это может иметь пессимистичный подтекст в случае приминения к области разработки программного обеспечения. Теория заключается в том, что команда будет неэффективна вплоть до близкого дедлайна. Затем будет стремиться закончить работу к крайнему сроку. 

Если этот закон совместить с [законом Хофштадтера](#закон-хофштадтера), то картина окажется ещё более пессимистичной — работа заполнит всё отведённое на неё время и **всё равно займёт больше времени, чем ожидалось**.

See also:

- [законом Хофштадтера](#закон-хофштадтера)

---

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

### Закон дырявых абстракций

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

[The Dependency Inversion Principle](https://en.wikipedia.org/wiki/Dependency_inversion_principle)

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

## Список литературы

Если вас заинтересовали перечисленные концепции, то вам могут понравиться следующие материалы:

- [Закон Амдала](http://ssd.sscc.ru/en/content/%D0%B7%D0%B0%D0%BA%D0%BE%D0%BD-%D0%B0%D0%BC%D0%B4%D0%B0%D0%BB%D0%B0), Supercomputer Software Department
- [Закон Амдала](https://medium.com/german-gorelkin/amdahls-law-79a8edb040e2), Герман Горелкин, 11 декабря 2018
- [The Mythical Man Month - Frederick P. Brooks Jr.](https://www.goodreads.com/book/show/13629.The_Mythical_Man_Month) - A classic volume on software engineering. [Brooks's Law](#brookss-law) is a central theme of the book.
- [Gödel, Escher, Bach: An Eternal Golden Braid - Douglas R. Hofstadter.](https://www.goodreads.com/book/show/24113.G_del_Escher_Bach) - This book is difficult to classify. [Hofstadter's Law](#hofstadters-law) is from the book.

## TODO

Hi! If you land here, you've clicked on a link to a topic I've not written up yet, sorry about this - this is work in progress!

Feel free to [Raise an Issue](https://github.com/dwmkerr/hacker-laws/issues) requesting more details, or [Open a Pull Request](https://github.com/dwmkerr/hacker-laws/pulls) to submit your proposed definition of the topic. 
