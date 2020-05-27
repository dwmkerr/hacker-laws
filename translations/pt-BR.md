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
    * [Lei de Kernighan](#lei-de-kerni






ghan)
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

E lá vamos nós!

### Princípio 90-9-1 (Regra do 1%)

[1% Rule on Wikipedia](https://en.wikipedia.org/wiki/1%25_rule_(Internet_culture))

O Princípio 90-9-1 sugere que em uma comunidade da internet, como uma wiki, 90% dos participantes apenas consomem o conteúdo, 9% editam ou modificam o conteúdo e 1% dos participantes adicionam novos conteúdos.

Exemplos do mundo real:

- Um estudo de 2014 de quatro redes sociais de saúde digital concluíram que 1% dos usuários criaram 73% das publicações, os próximos 9% foram responsáveis por cerca de ~25% e os 90% restantes por uma média de 2% ([Referência](https://www.jmir.org/2014/2/e33/))

Veja também:

- [O Princípio de Pareto (Regra do 80/20)](#the-pareto-principle-the-8020-rule)

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

A Teoria das Janelas Quebradas sugere que sinais visíveis de crimes (ou a falta de cuidado por um ambiente) leva a crimes mais sérios (ou mais deterioração do ambiente).

Essa teoria tem sido aplicada no desenvolvimento de software, sugerindo que a baixa qualidade do código (ou o [Débito Técnico](#TODO)) podem levar a percepção de que esforços para melhorar a qualidade talvez sejam ignorados ou desvalorizados, mantendo a baixa qualidade. Esse efeito de cascata leva a uma grande diminuição na qualidade através do tempo.

Veja também:

- [Débito Técnico](#TODO)

Exemplos:

- [The Pragmatic Programming: Software Entropy](https://pragprog.com/the-pragmatic-programmer/extracts/software-entropy)
- [Coding Horror: The Broken Window Theory](https://blog.codinghorror.com/the-broken-window-theory/)
- [OpenSource: Joy of Programming - The Broken Window Theory](https://opensourceforu.com/2011/05/joy-of-programming-broken-window-theory/)

### Lei de Brook

[Lei de Brooks na Wikipeia](https://en.wikipedia.org/wiki/Brooks%27s_law)


> Adicionar recursos humanos em um projeto, de desenvolvimento de sotware, atrasado, faz ficar ainda mais atrasado. 

Essa lei sugere que em muitos casos, na tentativa de acelerar uma entrega, que já está atrasada, adcionando mais pessoas atrasa ainda mais essa entrega. Brooke assume que essa afirmação é uma generalização excessiva, entretanto, o principal motivo para isso acontecer é dado pelo simples fato de adicionar pessoas requer um gasto com comunicação e construção de novos recursos para a equipe suportar novos membros. Logo, a curto prazo esse investimento não tem um retorno. Também existem tarefas que não podem ser dividias, portanto adicionar mais pessoas não vai fazer ela ser concluida mais rápido. 

"Nove mulheres não podem parir uma criança em um mês" e "Dois pilotos não fazem o carro ir mais rápido" são frases relacionadas a Lei de Brooke, principalmente porque algumas tarefas nao podem ser divididas.


Esse é um tema central do livro '[The Mythical Man Month](#lista-de-livros)'.

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

> A melhor forma de obter a resposta correta na Internet não é fazer a pergunta, mas postar a resposta errada.

De acordo com Steven McGeady, Ward Cunningham o aconselhou no início dos anos 80: "A melhor forma de ter a resposta correta na Internet não é fazer a pergunta, mas postar a resposta errada." McGeady apelidou essa lei de "Lei de Cunningham", mesmo que Cunningham negue sua propriedade chamando-a de "citação". Mesmo originalmente se referindo a interações na Usenet, a lei tem sido utilizada para descrever como comunidades online funcionam (e.x.: Wikipedia, Reddit, Twitter, Facebook).

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

> Um sistema complexo que funciona é invariavelmente encontrado para ter evoluído a partir de um sistema simples que trabalhou. Um sistema complexo projetado a partir do zero nunca funciona e não pode ser remendado para fazê-lo funcionar.

A Lei de Gall afirma que tentativas de projetar sistemas altamente complexos provavelmente falharão. Sistemas altamente complexos raramente são construídos em uma vez só, mas evoluem a partir de sistemas mais simples.

Um exemplo clássico é a world-wide-web. Em seu estado atual, ela é um sistema altamente complexo. Contudo, ela foi definida inicialmente como uma forma simples de compartilhar conteúdo entre instituições acadêmicas. Ela foi tão bem-sucedida em atingir esses objetivos que evoluiu para se tornar algo mais complexo ao longo do tempo.

Veja também:

- [KISS (Keep It Simple, Stupid)](#the-kiss-principle)

### Lei de Goodhart

[The Goodhart's Law on Wikipedia](https://en.wikipedia.org/wiki/Goodhart's_law)

> Qualquer regularidade estatística observada tende a entrar em colapso quando a pressão é aplicada para fins de controle.
>
> _Charles Goodhart_


Também referenciada como:

> Quando uma medida torna-se uma meta (ou alvo), ela deixa de ser uma boa medida.
>
> _Marilyn Strathern_

A lei diz que otimizações orientadas por medidas podem levar à uma desvalorização do próprio resultado da medição. O conjunto de medidas excessivamente seletivo ([KPIs](https://en.wikipedia.org/wiki/Performance_indicator)) aplicado cegamenta a um processo resulta em um efeito distorcido. As pessoas tentem a otimizar localmente "jogando com" o sistema para satisfazer métricas específicas ao invés de prestar atenção ao resultado holístico de suas ações.

Exemplos do mundo real:
- Testes sem `assertions` atendem à cobertura de código esperada, apesar do objetivo da métrica era criar software bem testado
- A pontuação do desempenho de desenvolvedores é indicada pelo número de linhas `commitadas` leva a uma base de código injustificadamente inchada.

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

> Melhoria significa deterioração.
>
> _([Patrick Hutber](https://en.wikipedia.org/wiki/Patrick_Hutber))_

Essa lei sugere que melhorias em um sistema irão levar à deterioração em outras partes, ou ela ocultarão outras deteriorações, levando a uma degradação do estado atual do sistema.

Por exemplo, a diminuição na latência da resposta para um `end-point` particular pode causar um aumento na taxa de transferência e na capacidade ao longo de um fluxo de solicitação, afetando um subsistema totalmente diferente.

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

> A depuração é duplamente mais difícil do que escrever o código em primeiro lugar. Portanto, se você escrever o código da maneira mais inteligente possível, por definição, você não é inteligente o sufiencte para depurá-lo.
>
> (Brian Kernighan)

A Lei de Kerningham é nomeada por [Brian Kernighan](https://en.wikipedia.org/wiki/Brian_Kernighan) e devivada de uma citação de Kerningham no livro [The Elements of Programming Style](https://en.wikipedia.org/wiki/The_Elements_of_Programming_Style):

> Todo mundo sabe que depurar é duplamente mais difícil do que programar em primeiro lugar. Então, se você é o mais inteligente possível quando escreve, como você conseguirá depurar o código?

Enquanto hiperbólica, a Lei de Kerningham faz a argumentação de que código simples deve ser preferido ao invés de código complexo, porque depurar qualquer problema que poderá surgir em um código complexo pode ser custoso ou até mesmo inviável.

Veja também:

- [The KISS Principle](#the-kiss-principle)
- [The Unix Philosophy](#the-unix-philosophy)
- [Occam's Razor](#occams-razor)

### Lei de Metcalfe

[Metcalfe's Law on Wikipedia](https://en.wikipedia.org/wiki/Metcalfe's_law)

> Na teoria das redes, o valor de um sistema cresce aproximadamente o quadrado do número de usuários daquele sistema.

Esta lei é baseada no número de possíveis conexões pareadas dentro de um sistema e é relacionada com a [Lei de Reed](#reeds-law). Odlyzko e outros argumentaram que tanto a Lei de Reed e a Lei de Metcalfe exageram o valor do sistema, não levando em consideração os limites da cognição humana sobre os efeitos da rede; veja [Dunbar's Number](#dunbars-number).

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

> Tudo que poderá dar errado, irá dar errado.

Relacionada com [Edward A. Murphy, Jr](https://en.wikipedia.org/wiki/Edward_A._Murphy_Jr.), a _Lei de Murphy_ diz que se algo pode dar errado, isso dará errado.

Isso é um ditado comum entre desenvolvedores. Muitas vezes o inesperado ocorre durante o desenvolvimento, testes ou até mesmo em produção. Essa lei também pode ser relacionada a Lei de Sod (mais comum no inglês britânico):

> Se algo pode dar errado, dará errado, no pior momento possível.

Essas 'leis' são geralmente utilizadas em um sentido cômico. Contudo, fenômenos como [_Confirmation Bias_](#TODO) e [_Selection Bias_](#TODO) podem pevar as pessoas a enfatizarem demais essas leis (na maioria das vezes quando as coisas funcionam, elas passam desapercebidas, as falhas são mais perceptíveis e atraem mais discussões).

Veja também:

- [Confirmation Bias](#TODO)
- [Selection Bias](#TODO)

### Navalha de Occam

[Occam's Razor on Wikipedia](https://en.wikipedia.org/wiki/Occam's_razor)

> Entidades não devem ser multiplicadas sem necessidade.
>
> William of Ockham

A Navalha de Occam diz que em meio a várias possíveis soluções, a solução mais provável é aquela com menor número de conceitos e suposições. Essa solução é a mais simples e envolve apenas o problema em questão, sem introduzir complexidades acidentais e possíveis consequências negativas.

Veja também:

- [YAGNI](#yagni)
- [No Silver Bullet: Accidental Complexity and Essential Complexity](https://en.wikipedia.org/wiki/No_Silver_Bullet)

Exemplo:

- [Lean Software Development: Eliminate Waste](https://en.wikipedia.org/wiki/Lean_software_development#Eliminate_waste)

### Lei de Parkinson

[Lei de Parkinson](https://en.wikipedia.org/wiki/Parkinson%27s_law)

>O trabalho se expande de modo a preencher o tempo disponível para a sua realização.

A lei de Parkinson foi publicada por Cyril Northcote Parkinson num artigo na revista The Economist em 1955, sendo depois reimpresso com outros artigos no livro Parkinson's Law: The Pursuit of Progress [A lei de Parkinson: a busca do progresso].Em seu contexto original, essa Lei foi baseada em estudos de burocracia. E pode ser pessimisticamente aplicado a desenvolvimento de software, a teoria diz que equipes serão ineficientes até os prazos finais, quando irão dar o máximo até o prazo final.

### Efeito de Otimização Prematura

[Premature Optimization on WikiWikiWeb](http://wiki.c2.com/?PrematureOptimization)

> Otimização prematura é a raiz de todo o mal.
>
> [(Donald Knuth)](https://twitter.com/realdonaldknuth?lang=en)

No artigo de Donald Knuth, [Structured Programming With Go To Statements](http://wiki.c2.com/?StructuredProgrammingWithGoToStatements), ele escreve: "Programadores perdem grandes quantidades de tempo pensando ou se preocupando com a velocidade de partes não críticas de seus programas, e essas tentativas de eficiência possuem um forte impacto negativo quando depuração e manutenção são consideradas. Nós devemos esquecer essas pequenas eficiências, cerca de 97% das vezes: **otimização prematura é a raiz de todo o mal.** No entando, não devemos perder a oportunidade nesses 3% críticos".

Contudo, _Otimização Prematura_ pode ser definida (em termos menos carregados) como otimizar antes de saber o que precisamos.

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

> A utilidade de grandes redes, particularmente redes sociais, escalam exponencialmente com o tamanho da própria rede.

Essa lei é baseada na teoria dos grafos, onde a utilidade é escalonada com o número de possíveis subgrupos, que é mais rápido que o número de participantes ou o número de possíveis conexões pareadas. Odlyzko e outros argumentam que a Lei de Reed exagera a utilidade de um sistema por não levar em conta os limites da cognição humana sobre os efeitos da rede; veja [Dunbar's Number](#dunbars-number).

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

Essa lei afirma que abstrações, as quais são geralmente utilizadas na computação para simplificar um trabalho com sistemas complexos, em certas situações irão 'vazar' elementos do sistema subjacente, fazendo com que a abstração se comporte de maneira inesperada.

Um exemplo disso pode ser carregar um arquivo e ler o seu conteúdo. As APIs do sistema de arquivo são abstrações do kernel de nível inferior, que são uma abstração dos processadores físicos relacionados à alteração de dados no disco rígido (ou na memória flash em SSD). Na maioria dos casos, a abstração de tratar um arquivo como um fluxo de dados binários funcionará. Contudo, para um disco rígido, a leitura sequencial dos dados será significamente mais rápida que o acesso aleatório (devido ao aumento da sobrecarga de falhas na página), mas para um disco SSD, essa sobrecarga não estará presente. Os detalhes subjacentes precisarão ser entendidos para lidar com esse caso (por exemplo, os arquivos índices de uma base de dados são estruturados para reduzir a sobrecarga do acesso aleatório), a abstração 'vaza' detalhes de implementação os quais o desenvolvedor precisa estar ciente.

O exemplo acima pode se tormar mais complexo quando _mais_ abstrações são introduzidas. O sistema operacional Linux permite que os arquivos sejam acessados por rede mas representados localmente como arquivos 'normais'. Essa abstração será 'vazada' se houverem falhas de rede. Se um desenvolvedor tratar esses arquivos como 'normais', sem considerar o fato de que eles podem estar sujeitos à latência e falhas na rede, as soluções serão incorretas.

Veja também:

- [Hyrum's Law](#hyrums-law-the-law-of-implicit-interfaces)

Exemplos do mundo real:

- [Photoshop Slow Startup](https://forums.adobe.com/thread/376152) - um problema que eu encontrei no passado. O Photoshop demorava para abrir, às vezes levando alguns minutos. Parecia que o problema era que, ao iniciar, o programa lia algumas informações sobre a impressora padrão. No entando, se essa impressora fosse uma impressora de rede, isso demoraria tempo extremamente longo. A _abstração_ de uma impressora de rede ser mostrada ao sistema como uma impressora local causou um problema para usuários em situação de baixa conectividade. 

### A Lei da Trivialidade

[The Law of Triviality on Wikipedia](https://en.wikipedia.org/wiki/Law_of_triviality)

Essa lei sugere que grupos irão dar maior atenção para problemas triviais ou cosméticos, do que para os problemas sérios e substanciais.

O exemplo fictício comum utilizado é o de um comitê aprovando planos para uma usina nuclear, que passam maior tempo discutindo a estrutura do bicicletário ao invés do design da própria usina que é muito mais importante. Pode ser difícil fornecer informações valiosas em discussões sobre tópicos muito grandes e complexos sem um alto grau de conhecimento ou preparação no assunto. No entando, as pessoas querem ser vistas contribuindo com informações importantes. Daí uma tendência de concentrar muito tempo em pequenos detalhes, que podem ser facilmente explicados, mas necessariamente não são de importância particular.

O exemplo fictício acima levou ao uso do termo _'Bike Shedding'_ como uma expressão por gastar tempo em detalhes triviais.


### A Filosofia Unix

[The Unix Philosophy on Wikipedia](https://en.wikipedia.org/wiki/Unix_philosophy)

A Filosofia Unix prega que componentes de um software devem ser pequenos, e focados em fazer muito bem uma coisa específica. Isso torna mais fácil a construção de sistemas compondo unidades pequenas, simples e bem definidas, em vez de usar programas grandes, complexos e multiuso.

Práticas modernas como a 'Arquitetura de Microsserviços' podem ser pensadas como uma aplicação dessa lei, onde os serviços são pequenos, focados em uma tarefa específica, permitindo que um comportamento complexo seja composto de blocos de construção simples.

### O Modelo Spotify

[The Spotify Model on Spotify Labs](https://labs.spotify.com/2014/03/27/spotify-engineering-culture-part-1/)

O Modelo Spotify é uma abordagem para a organização de equipes que foi popularizado pelo 'Spotify'. Neste modelo, times são organizados por funcionalidades, não por tecnologias.

O Modelo Spotify também popularizou o conteido de Tribos, Guildas, Capítulos, que são outros componentes de sua estrutura organizacional.

### Lei de Wadler

[Wadler's Law on wiki.haskell.org](https://wiki.haskell.org/Wadler's_Law)

> Em qualquer design de linguagem, o tempo total gasto discutindo a uma funcionalidade nessa lista é proporcional a dois elevados à potência de sua posição.
> 
> 0. Semantics
> 1. Syntax
> 2. Lexical syntax
> 3. Lexical syntax of comments
>
> (Em resumo, para cada hora gasta em semântica, 8 horas serão gastas na sintaxe de comentários)

Semelhante à [Lei da Trivialidade](), a Lei de Wadler afirma que quando projetamos uma linguagem, o tempo gasto em estruturas é desproporcionalmente maior do que a imporância dessas funcionalidades.

Veja também:

- [The Law of Triviality](#the-law-of-triviality)

### Lei de Wheaton

[The Link](http://www.wheatonslaw.com/)

[The Official Day](https://dontbeadickday.com/)

> Não seja um babaca
>
> _Wil Wheaton_

Cunhada por Wil Wheaton (Star Trek: The Next Generation, The Big Bang Theory), esta lei simples, concisa e poderosa visa aumentar a harmonia e o respeito dentro de uma organização profissional. Ela pode ser aplicada ao conversar com colegas de trabalho, ao efetuar code reviews, contrariar outros ponto de vista, criticar, e, em linhas gerais, na maioria das interações que os humanos mantém entre si.

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

Graças a contribuidores maravilhosos, Hacker Laws está disponível em vários idiomas. Por favor, considere em patrocinar os moderadores!

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
