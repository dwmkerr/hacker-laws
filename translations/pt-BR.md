# 💻📖 hacker-laws

Leis, teorias, princípios e padrões que desenvolvedores acharão úteis.

[Traduções](#translations): [🇮🇩](./translations/pt-BR.md) [🇧🇷](./translations/pt-BR.md) [🇨🇳](https://github.com/nusr/hacker-laws-zh) [🇩🇪](./translations/de.md) [🇫🇷](./translations/fr.md) [🇬🇷](./translations/el.md) [🇮🇹](https://github.com/csparpa/hacker-laws-it) [🇱🇻](./translations/lv.md) [🇰🇷](https://github.com/codeanddonuts/hacker-laws-kr) [🇷🇺](https://github.com/solarrust/hacker-laws) [🇪🇸](./translations/es-ES.md) [🇹🇷](https://github.com/umutphp/hacker-laws-tr) [🇯🇵](./translations/jp.md)

Gostou deste projeto? Por favor, considere [me apoiar](https://github.com/sponsors/dwmkerr) e [apoiar os tradutores](#traduções).

---

<!-- vim-markdown-toc GFM -->

* [Introdução](#introdução)
* [Leis](#leis)
	* [Princípio 90-9-1 (Regra do 1%)](#princípio-90-9-1-regra-do-1)
    * [Lei de Amdahl](#lei-de-amdahl)
    * [Teoria das Janelas Quebradas](#teoria-das-janelas-quebradas)
    * [Lei de Brook](#lei-de-brook)
    * [Lei de Conway](#lei-de-conway)
    * [Lei de Cunningham](#lei-de-cunningham)
    * [Número de Dunbar](#número-de-dunbar)
    * [Lei de Gall](#lei-de-gall)
    * [Lei de Goodhart](#lei-de-goodhart)
    * [Navalha de Hanlon](#navalha-de-hanlon)
    * [Lei de Hofstadter](#lei-de-hofstadter)
    * [Lei de Hutber](#lei-de-hutber)
    * [O Ciclo Hype e Lei de Amara](#o-ciclo-hype-e-lei-de-amara)
    * [Lei de Hyrum (Lei das Interfaces Implícitas)](#lei-de-hyrum-lei-das-interfaces-implícitas)
    * [Lei de Kernighan](#lei-de-kernighan)
    * [Lei de Metcalfe](#lei-de-metcalfe)
    * [Lei de Moore](#lei-de-moore)
    * [Lei de Murphy / Lei de Sod](#lei-de-murphy--lei-de-sod)
    * [Navalha de Occam](#navalha-de-occam)
    * [Lei de Parkinson](#lei-de-parkinson)
    * [Efeito de Otimização Prematura](#efeito-de-otimização-prematura)
    * [Lei de Putt](#lei-de-putt)
    * [Lei de Reed](#lei-de-reed)
    * [A Lei da Conservação da Complexidade (Lei de Tesler)](#a-lei-da-conservação-da-complexidade-lei-de-tesler)
    * [A Lei das Abstrações Gotejantes](#a-lei-das-abstrações-gotejantes)
    * [A Lei da Trivialidade](#a-lei-da-trivialidade)
    * [A Filosofia Unix](#a-filosofia-unix)
    * [O Modelo Spotify](#o-modelo-spotify)
    * [Lei de Wadler](#lei-de-wadler)
    * [Lei de Wheaton](#lei-de-wheaton)
* [Princípios](#princípios)
	* [O Princípio Dilbert](#o-princípio-dilbert)
    * [O Princípio de Pareto (Regra do 80/20)](#o-princípio-de-pareto-regra-do-8020)
    * [O Princípio de Peter](#o-princípio-de-peter)
    * [O Princípio da Robustez (Lei de Postel)](#o-princípio-da-robustez-lei-de-postel)
    * [SOLID](#solid)
    * [O Princípio da Responsabilidade Única](#o-princípio-da-responsabilidade-única)
    * [O Princípio do Aberto/Fechado](#o-princípio-do-abertofechado)
    * [O Princípio da Substituição de Liskov](#o-princípio-da-substituição-de-liskov)
    * [O Princípio da Segregação de Interface](#o-princípio-da-segregação-de-interface)
    * [O Princípio da Inversão de Dependência](#o-princípio-da-inversão-de-dependência)
    * [O Princípio DRY](#o-princípio-dry)
    * [O Princípio KISS](#o-princípio-kiss)
    * [YAGNI](#yagni)
    * [As Falácias da Computação Distribuída](#as-falácias-da-computação-distribuída)
* [Lista de leitura](#lista-de-leitura)
* [Traduções](#traduções)
* [Projetos relacionados](#projetos-relacionados)
* [Contribuindo](#contribuindo)
* [Em construção](#em-construção)

<!-- vim-markdown-toc -->

## Introdução

Existem muitas leis sobre as quais as pessoas discutem quando falam sobre desenvolvimento. Este repositório é uma referência e uma visão global das mais comuns. Sinta-se a vontade para contribuir e compartilhar.

❗: Este repositório contém explicações sobre algumas leis, princípios e padrões, mas não _advoga_ nenhum. Se eles devem ser aplicados é uma questão de discussão, e depende diretamente no que você está trabalhando.

## Leis

E lá vamos nos!

### Princípio 90-9-1 (Regra do 1%)

[1% Rule on Wikipedia](https://en.wikipedia.org/wiki/1%25_rule_(Internet_culture))

The 90-9-1 principle suggests that within an internet community such as a wiki, 90% of participants only consume content, 9% edit or modify content and 1% of participants add content.

Exemplos do mundo real:

- A 2014 study of four digital health social networks found the top 1% created 73% of posts, the next 9% accounted for an average of ~25% and the remaining 90% accounted for an average of 2% ([Reference](https://www.jmir.org/2014/2/e33/))

Veja também:

- [Pareto principle](#the-pareto-principle-the-8020-rule)

### Lei de Amdahl

[Lei de Amdahl na Wikipédia](https://pt.wikipedia.org/wiki/Lei_de_Amdahl)

> A lei de Amdahl, também conhecida como argumento de Amdahl, é usada para encontrar a máxima melhora esperada para um sistema em geral quando apenas uma única parte do mesmo é melhorada. Isto é frequentemente usado em computação paralela para prever o máximo speedup teórico usando múltiplos processadores. A lei possui o nome do Arquiteto computacional Gene Amdahl, e foi apresentada a AFIPS na Conferência Conjunta de Informática na primavera de 1967. 

Fica mais fácil de entender com um exemplo prático. Se um programa é feito de duas partes, parte A, que é executada por um processador único, e parte B, que pode ser feito paralelamente com N processadores. Se adicionarmos mais processaores ao sistema, só vai ter aumento nas tarefas relacionadas à parte B do programa. A velocidade de A se mantém a mesma.

O diagrama abaixo mostra alguns exemplos de melhoria na velocidade:

![Diagram: Lei de Amadhl](../images/amdahls_law.png)

*(Image Reference: By Daniels220 at English Wikipedia, Creative Commons Attribution-Share Alike 3.0 Unported, https://en.wikipedia.org/wiki/File:AmdahlsLaw.svg)*

Como pode-se perceber, mesmo um programa que teve metade da sua implementação de forma paralela, o benefício é menos de 10 _processing units_. Porém, um programa 95% paralelo, o ganho pode passar de 20 _processing units_.

### Teoria das Janelas Quebradas

[The Broken Windows Theory on Wikipedia](https://en.wikipedia.org/wiki/Broken_windows_theory)

The Broken Windows Theory suggests that visible signs of crime (or lack of care of an environment) lead to further and more serious crimes (or further deterioration of the environment).

This theory has been applied to software development, suggesting that poor quality code (or [Technical Debt](#TODO)) can lead to a perception that efforts to improve quality may be ignored or undervalued, thus leading to further poor quality code. This effect cascades leading to a great decrease in quality over time.

Veja também:

- [Technical Debt](#TODO)

Examples:

- [The Pragmatic Programming: Software Entropy](https://pragprog.com/the-pragmatic-programmer/extracts/software-entropy)
- [Coding Horror: The Broken Window Theory](https://blog.codinghorror.com/the-broken-window-theory/)
- [OpenSource: Joy of Programming - The Broken Window Theory](https://opensourceforu.com/2011/05/joy-of-programming-broken-window-theory/)

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

### Lei de Cunnigham

[Cunningham's Law on Wikipedia](https://en.wikipedia.org/wiki/Ward_Cunningham#Cunningham's_Law)

> The best way to get the right answer on the Internet is not to ask a question, it's to post the wrong answer.

According to Steven McGeady, Ward Cunningham advised him in the early 1980s: "The best way to get the right answer on the Internet is not to ask a question, it's to post the wrong answer." McGeady dubbed this Cunningham's law, though Cunningham denies ownership calling it a "misquote." Although originally referring to interactions on Usenet, the law has been used to describe how other online communities work (e.g., Wikipedia, Reddit, Twitter, Facebook).

Veja também:

- [XKCD 386: "Duty Calls"](https://xkcd.com/386/)

### Número de Dunbar

[Número de Dunbar na Wikipedia](https://en.wikipedia.org/wiki/Dunbar%27s_number)

[Dumbar] propós que humanos só conseguem manter de forma confortável, 150 relacionamentos estáveis. Esse número está mais em um contexto social, "o número de pessoas que você não se sentiria sem graça para se juntar em uma bebiba se esbarrase com ela em um bar". Esse número geralmente está entra 100 e 250.

Esse número é uma sugestão cognitiva limite para o número de pessoass para qual consegue-se manter uma relação social estável.

Como uma relação entre pessoas, manter uma relação entre desenvolvedor e codigo requer esforço. É necessário usar politicas, padrões e procedimentos para encarar projetos complicados ou qualquer adversidade possível nesse tipo de relação. Número de Dunbar é importante em vários aspectos, não somente quando a empresa está em crescimento, mas também ao definir o escopo para os esforços da equipe ou decidir quando u msistema deve investir em ferramentas para axuliar na sobrecarga da logística. Colocando em contexto de engrenharia, é o número de projetos para os quais você se sentiria confiante para ingresssar em uma rotação de plantão de suporte.

Veja também:

- [Lei de Conwy](#lei-de-conway)

### Lei de Gall

[Gall's Law on Wikipedia](https://en.wikipedia.org/wiki/John_Gall_(author)#Gall's_law)

> A complex system that works is invariably found to have evolved from a simple system that worked. A complex system designed from scratch never works and cannot be patched up to make it work. You have to start over with a working simple system.
>
> ([John Gall](https://en.wikipedia.org/wiki/John_Gall_(author)))

Gall's Law implies that attempts to _design_ highly complex systems are likely to fail. Highly complex systems are rarely built in one go, but evolve instead from more simple systems.

The classic example is the world-wide-web. In its current state, it is a highly complex system. However, it was defined initially as a simple way to share content between academic institutions. It was very successful in meeting these goals and evolved to become more complex over time.

Veja também:

- [KISS (Keep It Simple, Stupid)](#the-kiss-principle)

### Lei de Goodhart

[The Goodhart's Law on Wikipedia](https://en.wikipedia.org/wiki/Goodhart's_law)

> Any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes.
>
> _Charles Goodhart_

Also commonly referenced as:

> When a measure becomes a target, it ceases to be a good measure.
>
> _Marilyn Strathern_

The law states that the measure-driven optimizations could lead to devaluation of the measurement outcome itself. Overly selective set of measures ([KPIs](https://en.wikipedia.org/wiki/Performance_indicator)) blindly applied to a process results in distorted effect. People tend to optimize locally by "gaming" the system in order to satisfy particular metrics instead of paying attention to holistic outcome of their actions.

Exemplos do mundo real:
- Assert-free tests satisfy the code coverage expectation, despite the fact that the metric intent was to create well-tested software.
- Developer performance score indicated by the number of lines committed leads to unjustifiably bloated codebase.

Veja também:
- [Goodhart’s Law: How Measuring The Wrong Things Drive Immoral Behaviour](https://coffeeandjunk.com/goodharts-campbells-law/)
- [Dilbert on bug-free software](https://dilbert.com/strip/1995-11-13)

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

### Lei de Hutber

[Hutber's Law on Wikipedia](https://en.wikipedia.org/wiki/Hutber%27s_law)

> Improvement means deterioration.
>
> ([Patrick Hutber](https://en.wikipedia.org/wiki/Patrick_Hutber))

This law suggests that improvements to a system will lead to deterioration in other parts, or it will hide other deterioration, leading overall to a degradation from the current state of the system.

For example, a decrease in response latency for a particular end-point could cause increased throughput and capacity issues further along in a request flow, affecting an entirely different sub-system.

### O Ciclo Hype e Lei de Amara


[The ciclo Hype on Wikipedia](https://en.wikipedia.org/wiki/Hype_cycle)

>Nós tendemos a superestimar os efeitos da tecnologia em curto prazo e subestimar os efeitos a longo prazo.
>
> Roy Amara

O Ciclo Hype é uma representação visual da empolgação e desenvolvimento da tecnologia ao longo do tempo, originalmente produzida por Gartner.
![The Hype Cycle](../images/gartner_hype_cycle.png)

*(Image Reference: By Jeremykemp at English Wikipedia, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=10547051)*

Em curto prazo, o ciclo sugere que acontece uma explosão de empolgação a cerca de uma nova tecnologia e seu impacto em potencial. Equipes geralmente entram juntas nessas tecnlogias de forma rápida e em alguns casos ficam desapontados com os resutados. Uma das possíveis causas para isso é o fato da tecnologia em questão não ser madura o suficiente, ou aplicações do mundo real que não estão totalmente prontas. Depois de um certo tempo, a capacidade da tecnologia aumenta e oportunidades práticas para uso dela aumentam, as equipes finalmente podem ser produtivas. A citação de Amara resume isso de forma sucinta - "Nós tendemos a superestimar os efeitos da tecnologia em curto prazo e subestimar os efeitos a longo prazo".


### Lei de Hyrum (Lei das Interfaces Implícitas)

[Lei de Hyrum site](http://www.hyrumslaw.com/)


>Com um número suficientes de clientes de uma API,
>não importa a sua pré-condição no contato:
>todos os comportamentos observáveis do seu sistema
>serão dependentes de alguém.
>
> (Hyrum Wright)

A lei de Hyrum sugere que quando você tem um número muito grande de consumidores de uma API, todos os comportamentos dessa API (mesmo aqueles que não estão definidos como parte de um contrato público) eventualmente irão dependender de outra parte do sistema, ou outra API. Um exemplo trivial pode ser elementos não funcionais, como o tempo de resposta de uma API. Um exemplo mais sutil pode ser os consumidores que estão confiando em aplicar um regex a uma mensagem de erro para determinar o _tipo_ de erro de uma API. Mesmo que o contrato público da API não especifique nada sobre o conteúdo da mensagem, indicando que os usuários devem usar um código de erro associado, alguns usuários podem usar a mensagem e alterar a mensagem essencialmente interrompe a API para esses usuários.

Veja Também:

- [XKCD 1172](https://xkcd.com/1172/)

### Lei de Kernighan

> Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it.
>
> (Brian Kernighan)

Kernighan's Law is named for [Brian Kernighan](https://en.wikipedia.org/wiki/Brian_Kernighan) and derived from a quote from Kernighan and Plauger's book [The Elements of Programming Style](https://en.wikipedia.org/wiki/The_Elements_of_Programming_Style):

> Everyone knows that debugging is twice as hard as writing a program in the first place. So if you're as clever as you can be when you write it, how will you ever debug it?

While hyperbolic, Kernighan's Law makes the argument that simple code is to be preferred over complex code, because debugging any issues that arise in complex code may be costly or even infeasible.

Veja também:

- [The KISS Principle](#the-kiss-principle)
- [The Unix Philosophy](#the-unix-philosophy)
- [Occam's Razor](#occams-razor)

### Lei de Metcalfe

[Metcalfe's Law on Wikipedia](https://en.wikipedia.org/wiki/Metcalfe's_law)

> In network theory, the value of a system grows as approximately the square of the number of users of the system.

This law is based on the number of possible pairwise connections within a system and is closely related to [Reed's Law](#reeds-law). Odlyzko and others have argued that both Reed's Law and Metcalfe's Law overstate the value of the system by not accounting for the limits of human cognition on network effects; see [Dunbar's Number](#dunbars-number).

Veja também:
- [Reed's Law](#reeds-law)
- [Dunbar's Number](#dunbars-number)

### Lei de Moore

[Lei de Moore na wikipedia](https://en.wikipedia.org/wiki/Moore%27s_law)

> O número de transistores dentro de um circuito integrado dobra a cada 2 anos, aproximadamente.


Até meados de 1965 não havia nenhuma previsão real sobre o futuro do hardware, quando Gordon E. Moore fez sua profecia, na qual o número de transistores dos chips teria um aumento de 100%, pelo mesmo custo, a cada período de 18 meses. Essa profecia tornou-se realidade e acabou ganhando o nome de Lei de Moore.

Esta lei serve de parâmetro para uma elevada gama de dispositivos digitais, além das CPUs. Na verdade, qualquer chip está ligado a lei de Gordon E. Moore, até mesmo o CCD de câmeras fotográficas digitais (sensor que capta a imagem nas câmeras nuclear; ou CNCL, sensores que captam imagens nas câmeras fotográficas profissionais).

Esse padrão continuou a se manter, e não se espera que pare até, no mínimo, 2021.

### Lei de Murphy / Lei de Sod

[Murphy's Law on Wikipedia](https://en.wikipedia.org/wiki/Murphy%27s_law)

> Anything that can go wrong will go wrong.

Related to [Edward A. Murphy, Jr](https://en.wikipedia.org/wiki/Edward_A._Murphy_Jr.) _Murphy's Law_ states that if a thing can go wrong, it will go wrong.

This is a common adage among developers. Sometimes the unexpected happens when developing, testing or even in production. This can also be related to the (more common in British English) _Sod's Law_:

> If something can go wrong, it will, at the worst possible time.

These 'laws' are generally used in a comic sense. However, phenomena such as [_Confirmation Bias_](#TODO) and [_Selection Bias_](#TODO) can lead people to perhaps over-emphasise these laws (the majority of times when things work, they go unnoticed, failures however are more noticeable and draw more discussion).

Veja também:

- [Confirmation Bias](#TODO)
- [Selection Bias](#TODO)

### Navalha de Occam

[Occam's Razor on Wikipedia](https://en.wikipedia.org/wiki/Occam's_razor)

> Entities should not be multiplied without necessity.
>
> William of Ockham

Occam's razor says that among several possible solutions, the most likely solution is the one with the least number of concepts and assumptions. This solution is the simplest and solves only the given problem, without introducing accidental complexity and possible negative consequences.

Veja também:

- [YAGNI](#yagni)
- [No Silver Bullet: Accidental Complexity and Essential Complexity](https://en.wikipedia.org/wiki/No_Silver_Bullet)

Example:

- [Lean Software Development: Eliminate Waste](https://en.wikipedia.org/wiki/Lean_software_development#Eliminate_waste)

### Lei de Parkinson

[Lei de Parkinson](https://en.wikipedia.org/wiki/Parkinson%27s_law)

>O trabalho se expande de modo a preencher o tempo disponível para a sua realização.

A lei de Parkinson foi publicada por Cyril Northcote Parkinson num artigo na revista The Economist em 1955, sendo depois reimpresso com outros artigos no livro Parkinson's Law: The Pursuit of Progress [A lei de Parkinson: a busca do progresso].Em seu contexto original, essa Lei foi baseada em estudos de burocracia. E pode ser pessimisticamente aplicado a desenvolvimento de software, a teoria diz que equipes serão ineficientes até os prazos finais, quando irão dar o máximo até o prazo final.

### Efeito de Otimização Prematura

[Premature Optimization on WikiWikiWeb](http://wiki.c2.com/?PrematureOptimization)

> Premature optimization is the root of all evil.
>
> [(Donald Knuth)](https://twitter.com/realdonaldknuth?lang=en)

In Donald Knuth's paper [Structured Programming With Go To Statements](http://wiki.c2.com/?StructuredProgrammingWithGoToStatements), he wrote: "Programmers waste enormous amounts of time thinking about, or worrying about, the speed of noncritical parts of their programs, and these attempts at efficiency actually have a strong negative impact when debugging and maintenance are considered. We should forget about small efficiencies, say about 97% of the time: **premature optimization is the root of all evil**. Yet we should not pass up our opportunities in that critical 3%."

However, _Premature Optimization_ can be defined (in less loaded terms) as optimizing before we know that we need to.

### Lei de Putt

[Lei de Putt na wikipedia](https://en.wikipedia.org/wiki/Putt%27s_Law_and_the_Successful_Technocrat)

> Tecnologia é dominada por dois tipos de pessoa. Aqueles que entendem o que não gerenciam e aqueles que gerenciam o que não entendem.

A Lei de Putt é frequentemente seguida pelo Corolário de Putt:

> Cada hierarquia técnica, no tempo, desenvolve uma inversão de competência.

Estas declarações sugerem que devido a vários critérios de seleção e tendências na forma como grupos se organizam, haverá um número de pessoas qualificadas nos níveis de trabalho de organizações técnicas, e um número de pessoas em funções gerenciais que não estão cientes das complexidades e desafios do trabalho que estão gerenciando. Isso pode ser devido a fenômenos como  (#em-progresso)

Veja também:

- [O Principio de Peter](#em-progresso)
- [Lei de Dilbert](#em-progresso).

### Lei de Reed

[Reed's Law on Wikipedia](https://en.wikipedia.org/wiki/Reed's_law)

> The utility of large networks, particularly social networks, scales exponentially with the size of the network.

This law is based on graph theory, where the utility scales as the number of possible sub-groups, which is faster than the number of participants or the number of possible pairwise connections. Odlyzko and others have argued that Reed's Law overstates the utility of the system by not accounting for the limits of human cognition on network effects; see [Dunbar's Number](#dunbars-number).

Veja também:
- [Metcalfe's Law](#metcalfes-law)
- [Dunbar's Number](#dunbars-number)

### A Lei da Conservação da Complexidade (Lei de Tesler)

[A lei da Conservação de Complexidade na wikipedia](https://en.wikipedia.org/wiki/Law_of_conservation_of_complexity)

Essa lei sugere que em todos sitemas sempre vai existir uma quantidade de complexidade que não pode ser reduzida.

Alguma complexidade em um sistema é "inadvertida". É uma consequência da estrutura deficiente, erros ou apenas má modelagem de um problema a ser resolvido. A complexidade inadvertida pode ser reduzida (ou eliminada). No entanto, alguma complexidade é "intrínseca" como consequência da complexidade inerente ao problema a ser resolvido. Essa complexidade pode ser movida, mas não eliminada.

Um elemento interessante para essa lei é a sugestão de que, mesmo simplificando todo o sistema, a complexidade intrínseca não é reduzida, ela é “movida para o usuário”, que deve se comportar de uma maneira mais complexa.

### A Lei das Abstrações Gotejantes

[The Law of Leaky Abstractions on Joel on Software](https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/)

>Todas as abstrações não triviais, até certo ponto, são vazadas

This law states that abstractions, which are generally used in computing to simplify working with complicated systems, will in certain situations 'leak' elements of the underlying system, this making the abstraction behave in an unexpected way.

An example might be loading a file and reading its contents. The file system APIs are an _abstraction_ of the lower level kernel systems, which are themselves an abstraction over the physical processes relating to changing data on a magnetic platter (or flash memory for an SSD). In most cases, the abstraction of treating a file like a stream of binary data will work. However, for a magnetic drive, reading data sequentially will be *significantly* faster than random access (due to increased overhead of page faults), but for an SSD drive, this overhead will not be present. Underlying details will need to be understood to deal with this case (for example, database index files are structured to reduce the overhead of random access), the abstraction 'leaks' implementation details the developer may need to be aware of.

The example above can become more complex when _more_ abstractions are introduced. The Linux operating system allows files to be accessed over a network but represented locally as 'normal' files. This abstraction will 'leak' if there are network failures. If a developer treats these files as 'normal' files, without considering the fact that they may be subject to network latency and failures, the solutions will be buggy.

The article describing the law suggests that an over-reliance on abstractions, combined with a poor understanding of the underlying processes, actually makes dealing with the problem at hand _more_ complex in some cases.

Veja também:

- [Hyrum's Law](#hyrums-law-the-law-of-implicit-interfaces)

Exemplos do mundo real:

- [Photoshop Slow Startup](https://forums.adobe.com/thread/376152) - an issue I encountered in the past. Photoshop would be slow to startup, sometimes taking minutes. It seems the issue was that on startup it reads some information about the current default printer. However, if that printer is actually a network printer, this could take an extremely long time. The _abstraction_ of a network printer being presented to the system similar to a local printer caused an issue for users in poor connectivity situations.

### A Lei da Trivialidade

[The Law of Triviality on Wikipedia](https://en.wikipedia.org/wiki/Law_of_triviality)

This law suggests that groups will give far more time and attention to trivial or cosmetic issues rather than serious and substantial ones.

The common fictional example used is that of a committee approving plans for nuclear power plant, who spend the majority of their time discussing the structure of the bike shed, rather than the far more important design for the power plant itself. It can be difficult to give valuable input on discussions about very large, complex topics without a high degree of subject matter expertise or preparation. However, people want to be seen to be contributing valuable input. Hence a tendency to focus too much time on small details, which can be reasoned about easily, but are not necessarily of particular importance.

The fictional example above led to the usage of the term 'Bike Shedding' as an expression for wasting time on trivial details.

### A Filosofia Unix

[The Unix Philosophy on Wikipedia](https://en.wikipedia.org/wiki/Unix_philosophy)

The Unix Philosophy is that software components should be small, and focused on doing one specific thing well. This can make it easier to build systems by composing together small, simple, well-defined units, rather than using large, complex, multi-purpose programs.

Modern practices like 'Microservice Architecture' can be thought of as an application of this law, where services are small, focused and do one specific thing, allowing complex behaviour to be composed of simple building blocks.

### O Modelo Spotify

[The Spotify Model on Spotify Labs](https://labs.spotify.com/2014/03/27/spotify-engineering-culture-part-1/)

The Spotify Model is an approach to team and organisation structure which has been popularised by 'Spotify'. In this model, teams are organised around features, rather than technologies.

The Spotify Model also popularises the concepts of Tribes, Guilds, Chapters, which are other components of their organisation structure.

### Lei de Wadler

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

Veja também:

- [The Law of Triviality](#the-law-of-triviality)

### Lei de Wheaton

[The Link](http://www.wheatonslaw.com/)

[The Official Day](https://dontbeadickday.com/)

> Don't be a dick.
>
> _Wil Wheaton_

Coined by Wil Wheaton (Star Trek: The Next Generation, The Big Bang Theory), this simple, concise, and powerful law aims for an increase in harmony and respect within a professional organization. It can be applied when speaking with coworkers, performing code reviews, countering other points of view, critiquing, and in general, most professional interactions humans have with each other.

## Princípios

Os princípios são como diretrizes relacionadas à design.

### O Princípio Dilbert

[The Dilbert Principle on Wikipedia](https://en.wikipedia.org/wiki/Dilbert_principle)

> Companies tend to systematically promote incompetent employees to management to get them out of the workflow.
>
> _Scott Adams_

A management concept developed by Scott Adams (creator of the Dilbert comic strip), the Dilbert Principle is inspired by [The Peter Principle](#the-peter-principle). Under the Dilbert Principle, employees who were never competent are promoted to management in order to limit the damage they can do. Adams first explained the principle in a 1995 Wall Street Journal article, and expanded upon it in his 1996 business book, [The Dilbert Principle](#reading-list).

Veja também:

- [The Peter Principle](#the-peter-principle)
- [Putt's Law](#putts-law)

### O Princípio de Pareto (Regra do 80/20)

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

Exemplos do mundo real:

- In 2002 Microsoft reported that by fixing the top 20% of the most-reported bugs, 80% of the related errors and crashes in windows and office would become eliminated ([Reference](https://www.crn.com/news/security/18821726/microsofts-ceo-80-20-rule-applies-to-bugs-not-just-features.htm)).

### O Princípio de Peter

[The Peter Principle on Wikipedia](https://en.wikipedia.org/wiki/Peter_principle)

> People in a hierarchy tend to rise to their "level of incompetence".
>
> _Laurence J. Peter_

A management concept developed by Laurence J. Peter, the Peter Principle observes that people who are good at their jobs are promoted, until they reach a level where they are no longer successful (their "level of incompetence"). At this point, as they are more senior, they are less likely to be removed from the organisation (unless they perform spectacularly badly) and will continue to reside in a role which they have few intrinsic skills at, as their original skills which made them successful are not necessarily the skills required for their new jobs.

This is of particular interest to engineers - who initially start out in deeply technical roles, but often have a career path which leads to _managing_ other engineers - which requires a fundamentally different skills-set.

Veja também:

- [The Dilbert Principle](#the-dilbert-principle)
- [Putt's Law](#putts-law)

### O Princípio da Robustez (Lei de Postel)

[The Robustness Principle on Wikipedia](https://en.wikipedia.org/wiki/Robustness_principle)

> Be conservative in what you do, be liberal in what you accept from others.

Often applied in server application development, this principle states that what you send to others should be as minimal and conformant as possible, but you should be aim to allow non-conformant input if it can be processed.

The goal of this principle is to build systems which are robust, as they can handle poorly formed input if the intent can still be understood. However, there are potentially security implications of accepting malformed input, particularly if the processing of such input is not well tested.

### SOLID

É um acrônimo para:

* S: [The Single Responsibility Principle](#the-single-responsibility-principle)
* O: [The Open/Closed Principle](#the-openclosed-principle)
* L: [The Liskov Substitution Principle](#the-liskov-substitution-principle)
* I: [The Interface Segregation Principle](#the-interface-segregation-principle)
* D: [The Dependency Inversion Principle](#the-dependency-inversion-principle)

These are key principles in [Object-Oriented Programming](#todo). Design principles such as these should be able to aid developers build more maintainable systems.

### O Princípio da Responsabilidade Única

[The Single Responsibility Principle on Wikipedia](https://en.wikipedia.org/wiki/Single_responsibility_principle)

> Every module or class should have a single responsibility only.

The first of the '[SOLID](#solid)' principles. This principle suggests that modules or classes should do one thing and one thing only. In more practical terms, this means that a single, small change to a feature of a program should require a change in one component only. For example, changing how a password is validated for complexity should require a change in only one part of the program.

Theoretically, this should make the code more robust, and easier to change. Knowing that a component which is being changed has a single responsibility only means that _testing_ that change should be easier. Using the earlier example, changing the password complexity component should only be able to affect the features which relate to password complexity. It can be much more difficult to reason about the impact of a change to a component which has many responsibilities.

Veja também:

- [Object-Oriented Programming](#todo)
- [SOLID](#solid)

### O Princípio do Aberto/Fechado

[The Open/Closed Principle on Wikipedia](https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle)

> Entities should be open for extension and closed for modification.

The second of the '[SOLID](#solid)' principles. This principle states that entities (which could be classes, modules, functions and so on) should be able to have their behaviour _extended_, but that their _existing_ behaviour should not be able to be modified.

As a hypothetical example, imagine a module which is able to turn a Markdown document into HTML. If the module could be extended to handle a newly proposed markdown feature, without modifying the module internals, then it would be open for extension. If the module could _not_ be modified by a consumer so that how existing Markdown features are handled, then it would be _closed_ for modification.

This principle has particular relevance for object-oriented programming, where we may design objects to be easily extended, but would avoid designing objects which can have their existing behaviour changed in unexpected ways.

Veja também:

- [Object-Oriented Programming](#todo)
- [SOLID](#solid)

### O Princípio da Substituição de Liskov

[The Liskov Substitution Principle on Wikipedia](https://en.wikipedia.org/wiki/Liskov_substitution_principle)

> It should be possible to replace a type with a subtype, without breaking the system.

The third of the '[SOLID](#solid)' principles. This principle states that if a component relies on a type, then it should be able to use subtypes of that type, without the system failing or having to know the details of what that subtype is.

As an example, imagine we have a method which reads an XML document from a structure which represents a file. If the method uses a base type 'file', then anything which derives from 'file' should be able to be used in the function. If 'file' supports seeking in reverse, and the XML parser uses that function, but the derived type 'network file' fails when reverse seeking is attempted, then the 'network file' would be violating the principle.

This principle has particular relevance for object-oriented programming, where type hierarchies must be modeled carefully to avoid confusing users of a system.

Veja também:

- [Object-Oriented Programming](#todo)
- [SOLID](#solid)

### O Princípio da Segregação de Interface

[The Interface Segregation Principle on Wikipedia](https://en.wikipedia.org/wiki/Interface_segregation_principle)

> No client should be forced to depend on methods it does not use.

The fourth of the '[SOLID](#solid)' principles. This principle states that consumers of a component should not depend on functions of that component which it doesn't actually use.

As an example, imagine we have a method which reads an XML document from a structure which represents a file. It only needs to read bytes, move forwards or move backwards in the file. If this method needs to be updated because an unrelated feature of the file structure changes (such as an update to the permissions model used to represent file security), then the principle has been invalidated. It would be better for the file to implement a 'seekable-stream' interface, and for the XML reader to use that.

This principle has particular relevance for object-oriented programming, where interfaces, hierarchies and abstract types are used to [minimise the coupling](#todo) between different components. [Duck typing](#todo) is a methodology which enforces this principle by eliminating explicit interfaces.

Veja também:

- [Object-Oriented Programming](#todo)
- [SOLID](#solid)
- [Duck Typing](#todo)
- [Decoupling](#todo)

### O Princípio da Inversão de Dependência

[The Dependency Inversion Principle on Wikipedia](https://en.wikipedia.org/wiki/Dependency_inversion_principle)

> High-level modules should not be dependent on low-level implementations.

The fifth of the '[SOLID](#solid)' principles. This principle states that higher level orchestrating components should not have to know the details of their dependencies.

As an example, imagine we have a program which read metadata from a website. We would assume that the main component would have to know about a component to download the webpage content, then a component which can read the metadata. If we were to take dependency inversion into account, the main component would depend only on an abstract component which can fetch byte data, and then an abstract component which would be able to read metadata from a byte stream. The main component would not know about TCP/IP, HTTP, HTML, etc.

This principle is complex, as it can seem to 'invert' the expected dependencies of a system (hence the name). In practice, it also means that a separate orchestrating component must ensure the correct implementations of abstract types are used (e.g. in the previous example, _something_ must still provide the metadata reader component a HTTP file downloader and HTML meta tag reader). This then touches on patterns such as [Inversion of Control](#todo) and [Dependency Injection](#todo).

Veja também:

- [Object-Oriented Programming](#todo)
- [SOLID](#solid)
- [Inversion of Control](#todo)
- [Dependency Injection](#todo)

### O Princípio DRY

[The DRY Principle on Wikipedia](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)

> Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.

DRY is an acronym for _Don't Repeat Yourself_. This principle aims to help developers reducing the repetition of code and keep the information in a single place and was cited in 1999 by Andrew Hunt and Dave Thomas in the book [The Pragmatic Developer](https://en.wikipedia.org/wiki/The_Pragmatic_Programmer)

> The opposite of DRY would be _WET_ (Write Everything Twice or We Enjoy Typing).

In practice, if you have the same piece of information in two (or more) different places, you can use DRY to merge them into a single one and reuse it wherever you want/need.

Veja também:

- [The Pragmatic Developer](https://en.wikipedia.org/wiki/The_Pragmatic_Programmer)

### O Princípio KISS

[KISS on Wikipedia](https://en.wikipedia.org/wiki/KISS_principle)

> Keep it simple, stupid

The KISS principle states that most systems work best if they are kept simple rather than made complicated; therefore, simplicity should be a key goal in design, and unnecessary complexity should be avoided.  Originating in the U.S. Navy in 1960, the phrase has been associated with aircraft engineer Kelly Johnson.

The principle is best exemplified by the story of Johnson handing a team of design engineers a handful of tools, with the challenge that the jet aircraft they were designing must be repairable by an average mechanic in the field under combat conditions with only these tools. Hence, the "stupid" refers to the relationship between the way things break and the sophistication of the tools available to repair them, not the capabilities of the engineers themselves. 

Veja também:

- [Gall's Law](#galls-law)

### YAGNI

[YAGNI on Wikipedia](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it)

This is an acronym for _**Y**ou **A**ren't **G**onna **N**eed **I**t_.

> Always implement things when you actually need them, never when you just foresee that you need them.
>
> ([Ron Jeffries](https://twitter.com/RonJeffries)) (XP co-founder and author of the book "Extreme Programming Installed")

This _Extreme Programming_ (XP) principle suggests developers should only implement functionality that is needed for the immediate requirements, and avoid attempts to predict the future by implementing functionality that might be needed later.

Adhering to this principle should reduce the amount of unused code in the codebase, and avoid time and effort being wasted on functionality that brings no value.

Veja também:

- [Reading List: Extreme Programming Installed](#reading-list)

### As Falácias da Computação Distribuída

[The Fallacies of Distributed Computing on Wikipedia](https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing)

Also known as _Fallacies of Networked Computing_, the Fallacies are a list of conjectures (or beliefs) about distributed computing, which can lead to failures in software development. The assumptions are:

- The network is reliable
- Latency is zero
- Bandwidth is infinite
- The network is secure
- Topology doesn't change
- There is one administrator
- Transport cost is zero
- The network is homogeneous

The first four items were listed by [Bill Joy](https://en.wikipedia.org/wiki/Bill_Joy) and [Tom Lyon](https://twitter.com/aka_pugs) around 1991 and first classified by [James Gosling](https://en.wikipedia.org/wiki/James_Gosling) as the "Fallacies of Networked Computing". [L. Peter Deutsch](https://en.wikipedia.org/wiki/L._Peter_Deutsch) added the 5th, 6th and 7th fallacies. In the late 90's Gosling added the 8th fallacy.

The group were inspired by what was happening at the time inside [Sun Microsystems](https://en.wikipedia.org/wiki/Sun_Microsystems).

These fallacies should be considered carefully when designing code which is resilient; assuming any of these fallacies can lead to flawed logic which fails to deal with the realities and complexities of distributed systems.

Veja também:

- [Foraging for the Fallacies of Distributed Computing (Part 1) - Vaidehi Joshi
 on Medium](https://medium.com/baseds/foraging-for-the-fallacies-of-distributed-computing-part-1-1b35c3b85b53)
- [Deutsch's Fallacies, 10 Years After](http://java.sys-con.com/node/38665)

## Lista de leitura


Se você achou esses conceitos interessantes, você provavelmente vai gostar dos seguintes livros.

- [Extreme Programming Installed - Ron Jeffries, Ann Anderson, Chet Hendrikson](https://www.goodreads.com/en/book/show/67834) - Cobre os principais princípios do Extreme Programming.
- [The Mythical Man Month - Frederick P. Brooks Jr.](https://www.goodreads.com/book/show/13629.The_Mythical_Man_Month) - Um volume clássico na engenharia de software. A [Lei de Brook](#brooks-law) é o tema central desse livro.
- [Gödel, Escher, Bach: An Eternal Golden Braid - Douglas R. Hofstadter.](https://www.goodreads.com/book/show/24113.G_del_Escher_Bach) - Esse livre é difícil de classificar. A [Lei de Hofstadter](#hofstadters-law) é desse livro.
- [The Dilbert Principle - Scott Adams](https://www.goodreads.com/book/show/85574.The_Dilbert_Principle) - Um olhar cômico sobre a América corporativa, do autor que criou o [Princípio Dilbert](#the-dilbert-principle).
- [The Peter Principle - Lawrence J. Peter](https://www.goodreads.com/book/show/890728.The_Peter_Principle) - Outro olhar cômico sobre os desafios de grandes organizações e sobre a gestão de pessoas, a fonte do [Princípio de Peter](#the-peter-principle).

## Traduções

Thanks to a number of wonderful contributors, Hacker Laws is available in a number of languages. Please consider sponsoring moderators!

| Idioma   | Moderador | Status |
|----------|-----------|--------|
| [🇮🇩 Bahasa Indonesia / Indonesian](./translations/pt-BR.md) | [arywidiantara](https://github.com/arywidiantara) | [![gitlocalized ](https://gitlocalize.com/repo/2513/id/badge.svg)](https://gitlocalize.com/repo/2513/id?utm_source=badge) |
| [🇧🇷 Português Brasileiro / Brazilian Portuguese](./translations/pt-BR.md) | [Eugênio Moreira](https://github.com/eugenioamn), [Leonardo Costa](https://github.com/leofc97) | [![gitlocalized ](https://gitlocalize.com/repo/2513/pt-BR/badge.svg)](https://gitlocalize.com/repo/2513/pt-BR?utm_source=badge) |
| [🇨🇳 中文 / Chinese](https://github.com/nusr/hacker-laws-zh) | [Steve Xu](https://github.com/nusr) | Parcialmente completa |
| [🇩🇪 Deutsch / German](./translations/de.md) | [Vikto](https://github.com/viktodergunov) | [![gitlocalized ](https://gitlocalize.com/repo/2513/de/badge.svg)](https://gitlocalize.com/repo/2513/de?utm_source=badge) |
| [🇫🇷 Français / French](./translations/fr.md) | [Kevin Bockelandt](https://github.com/KevinBockelandt) | [![gitlocalized ](https://gitlocalize.com/repo/2513/fr/badge.svg)](https://gitlocalize.com/repo/2513/fr?utm_source=badge) |
| [🇬🇷 ελληνικά / Greek](./translations/el.md) | [Panagiotis Gourgaris](https://github.com/0gap) | [![gitlocalized ](https://gitlocalize.com/repo/2513/el/badge.svg)](https://gitlocalize.com/repo/2513/el?utm_source=badge) |
| [🇮🇹 Italiano / Italian](https://github.com/csparpa/hacker-laws-it) | [Claudio Sparpaglione](https://github.com/csparpa) | Parcialmente completa |
| [🇯🇵 JP 日本語 / Japanese](./translations/jp.md) | [Fumikazu Fujiwara](https://github.com/freddiefujiwara)| [![gitlocalized ](https://gitlocalize.com/repo/2513/ja/badge.svg)](https://gitlocalize.com/repo/2513/ja?utm_source=badge) |
| [🇰🇷 한국어 / Korean](https://github.com/codeanddonuts/hacker-laws-kr) | [Doughnut](https://github.com/codeanddonuts) | Parcialmente completa |
| [🇱🇻 Latviešu Valoda / Latvian](./translations/lv.md) | [Arturs Jansons](https://github.com/iegik) | [![gitlocalized ](https://gitlocalize.com/repo/2513/lv/badge.svg)](https://gitlocalize.com/repo/2513/lv?utm_source=badge) |
| [🇷🇺 Русская версия / Russian](https://github.com/solarrust/hacker-laws) | [Alena Batitskaya](https://github.com/solarrust) | Parcialmente completa |
| [🇪🇸 Castellano / Spanish](./translations/es-ES.md) | [Manuel Rubio](https://github.com/manuel-rubio) ([Sponsor](https://github.com/sponsors/manuel-rubio)) | Parcialmente completa |
| [🇹🇷 Türkçe / Turkish](https://github.com/umutphp/hacker-laws-tr) | [Umut Işık](https://github.com/umutphp) | [![gitlocalized ](https://gitlocalize.com/repo/2513/tr/badge.svg)](https://gitlocalize.com/repo/2513/tr?utm_source=badge) |

Se você quer atualizar uma tradução, [abra uma pull request](https://github.com/dwmkerr/hacker-laws/compare). Se você quer adicionar um novo idioma, crie uma conta no [GitLocalize](https://gitlocalize.com/), depois abra uma issue pedindo ao administrador o idioma eu irei adicionar você no projeto! Seria muito útil se você conseguir abrir uma pull request que atualiza a tabela acima, adicionando link ao topo do arquivo.

## Projetos relacionados

- [Tip of the Day](https://tips.darekkay.com/html/hacker-laws-en.html) - Receba diaramente uma lei ou princípio hacker.
- [Hacker Laws CLI](https://github.com/umutphp/hacker-laws-cli) - Liste e visualize as leis de maneira aleatória no seu terminal!

## Contribuindo

Por favor, contribua! [Abra uma issue](https://github.com/dwmkerr/hacker-laws/issues/new) se você deseja ver aqui algum conteúdo novo, sugerir uma alteração/correção, ou então [abra uma pull request](https://github.com/dwmkerr/hacker-laws/compare) e proponha suas próprias modificações.

Certifique-se de ler as [Diretrizes de Contribuição](../.github/contributing.md) para saber sobre os padrões de texto, estilo etc. Esteja ciente do [Código de Conduta](../.github/CODE_OF_CONDUCT.md) ao participar de discussões sobre o projeto.

## Em construção

Olá! Se você parou aqui, clicou em um link para um tópico que não foi escrito ainda. Desculpe por isso, este trabalho está em andamento!

Sinta-se livre para [abrir uma issue](https://github.com/dwmkerr/hacker-laws/issues) solicitando mais detalhes, ou [abra uma pull request](https://github.com/dwmkerr/hacker-laws/compare) para submeter suas modificações.
