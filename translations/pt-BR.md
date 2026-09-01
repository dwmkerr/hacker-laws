# 💻📖 hacker-laws

Leis, teorias, princípios e padrões que desenvolvedores acharão úteis.

[Traduções](#translations): [🇨🇳](https://github.com/nusr/hacker-laws-zh) [🇫🇷](./translations/fr.md) [🇮🇹](./translations/it-IT.md) [🇱🇻](./translations/lv.md) [🇰🇷](https://github.com/codeanddonuts/hacker-laws-kr) [🇷🇺](https://github.com/solarrust/hacker-laws) [🇪🇸](./translations/es-ES.md) [🇹🇷](./translations/tr.md) [🇮🇩](./translations/id.md) [🇯🇵](./translations/jp.md) [🇵🇱](./translations/pl.md) [🇻🇳](./translations/vi.md)

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

E lá vamos nós!

### Princípio 90-9-1 (Regra do 1%)

[1% Rule on Wikipedia](https://en.wikipedia.org/wiki/1%25_rule_(Internet_culture))

O Princípio 90-9-1 sugere que em uma comunidade da internet, como uma wiki, 90% dos participantes apenas consomem o conteúdo, 9% editam ou modificam o conteúdo e 1% dos participantes adicionam novos conteúdos.

Exemplos do mundo real:

- Um estudo de 2014 de quatro redes sociais de saúde digital concluíram que 1% dos usuários criaram 73% das publicações, os próximos 9% foram responsáveis por cerca de ~25% e os 90% restantes por uma média de 2% ([Referência](https://www.jmir.org/2014/2/e33/))

Veja também:

- [O Princípio de Pareto (Regra do 80/20)](#o-princípio-de-pareto-regra-do-8020)

### Lei de Amdahl

[Lei de Amdahl na Wikipédia](https://pt.wikipedia.org/wiki/Lei_de_Amdahl)

> A lei de Amdahl, também conhecida como argumento de Amdahl, é usada para encontrar a máxima melhora esperada para um sistema em geral quando apenas uma única parte do mesmo é melhorada. Isto é frequentemente usado em computação paralela para prever o máximo speedup teórico usando múltiplos processadores. A lei possui o nome do Arquiteto computacional Gene Amdahl, e foi apresentada a AFIPS na Conferência Conjunta de Informática na primavera de 1967.

Fica mais fácil de entender com um exemplo prático. Se um programa é feito de duas partes, parte A, que é executada por um processador único, e parte B, que pode ser feito paralelamente com N processadores. Se adicionarmos mais processadores ao sistema, só vai ter aumento nas tarefas relacionadas à parte B do programa. A velocidade de A se mantém a mesma.

O diagrama abaixo mostra alguns exemplos de melhoria na velocidade:

![Diagram: Lei de Amadhl](../images/amdahls-law.svg)

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

[Lei de Brooks na Wikipedia](https://en.wikipedia.org/wiki/Brooks%27s_law)

> Adicionar recursos humanos em um projeto, de desenvolvimento de software, atrasado, faz ficar ainda mais atrasado.

Essa lei sugere que em muitos casos, na tentativa de acelerar uma entrega, que já está atrasada, adicionando mais pessoas atrasa ainda mais essa entrega. Brooks assume que essa afirmação é uma generalização excessiva, entretanto, o principal motivo para isso acontecer é dado pelo simples fato de adicionar pessoas requer um gasto com comunicação e construção de novos recursos para a equipe suportar novos membros. Logo, a curto prazo esse investimento não tem um retorno. Também existem tarefas que não podem ser dividias, portanto adicionar mais pessoas não vai fazer ela ser concluída mais rápido.

"Nove mulheres não podem parir uma criança em um mês" e "Dois pilotos não fazem o carro ir mais rápido" são frases relacionadas a Lei de Brooks, principalmente porque algumas tarefas não podem ser divididas.

Esse é um tema central do livro '[The Mythical Man Month](#lista-de-livros)'.

Veja também:

- [Death March](#em-progresso)
- [Livro: The Mythical Man Month](#lista-de-livros)

### Lei de Conway

[Lei de Conway na wikipedia](https://en.wikipedia.org/wiki/Conway%27s_law)

Essa lei sugere que limites técnicos de um sistema refletirão na estrutura da organização. Se uma organização é estruturada em pequenos setores, desconexas unidades, o software que ela produz sera assim também. Se uma organização é construída de forma vertical, em torno de funcionalidades e serviços, terá reflexo disso dentro do sistema.

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

Dunbar propôs que humanos só conseguem manter de forma confortável, 150 relacionamentos estáveis. Esse número está mais em um contexto social, "o número de pessoas que você não se sentiria sem graça para se juntar em uma bebida se esbarrasse com ela em um bar". Esse número geralmente está entra 100 e 250.

Esse número é uma sugestão cognitiva limite para o número de pessoas para qual consegue-se manter uma relação social estável.

Como uma relação entre pessoas, manter uma relação entre desenvolvedor e código requer esforço. É necessário usar politicas, padrões e procedimentos para encarar projetos complicados ou qualquer adversidade possível nesse tipo de relação. Número de Dunbar é importante em vários aspectos, não somente quando a empresa está em crescimento, mas também ao definir o escopo para os esforços da equipe ou decidir quando um sistema deve investir em ferramentas para auxiliar na sobrecarga da logística. Colocando em contexto de engrenharia, é o número de projetos para os quais você se sentiria confiante para ingressar em uma rotação de plantão de suporte.

Veja também:

- [Lei de Conway](#lei-de-conway)

### Lei de Gall

[Gall's Law on Wikipedia](https://en.wikipedia.org/wiki/John_Gall_(author)#Gall's_law)

> Um sistema complexo que funciona é invariavelmente encontrado para ter evoluído a partir de um sistema simples que trabalhou. Um sistema complexo projetado a partir do zero nunca funciona e não pode ser remendado para fazê-lo funcionar.

A Lei de Gall afirma que tentativas de projetar sistemas altamente complexos provavelmente falharão. Sistemas altamente complexos raramente são construídos em uma vez só, mas evoluem a partir de sistemas mais simples.

Um exemplo clássico é a world-wide-web. Em seu estado atual, ela é um sistema altamente complexo. Contudo, ela foi definida inicialmente como uma forma simples de compartilhar conteúdo entre instituições acadêmicas. Ela foi tão bem-sucedida em atingir esses objetivos que evoluiu para se tornar algo mais complexo ao longo do tempo.

Veja também:

- [KISS (Keep It Simple, Stupid)](#o-princípio-kiss)

### Lei de Goodhart

[The Goodhart's Law on Wikipedia](https://en.wikipedia.org/wiki/Goodhart's_law)

> Qualquer regularidade estatística observada tende a entrar em colapso quando a pressão é aplicada para fins de controle.
>
> _Charles Goodhart_


Também referenciada como:

> Quando uma medida torna-se uma meta (ou alvo), ela deixa de ser uma boa medida.
>
> _Marilyn Strathern_

A lei diz que otimizações orientadas por medidas podem levar à uma desvalorização do próprio resultado da medição. O conjunto de medidas excessivamente seletivo ([KPIs](https://en.wikipedia.org/wiki/Performance_indicator)) aplicado cegamente a um processo resulta em um efeito distorcido. As pessoas tentem a otimizar localmente "jogando com" o sistema para satisfazer métricas específicas ao invés de prestar atenção ao resultado holístico de suas ações.

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

Esse principio sugere que ações negativas não são sempre resultado de má vontade. Em vez disso, é mais provável que o resultado negativo seja atribuído à ações que não foram totalmente entendidas.

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

Essa lei sugere que melhorias em um sistema irão levar à deterioração em outras partes, ou elas ocultarão outras deteriorações, levando a uma degradação do estado atual do sistema.

Por exemplo, a diminuição na latência da resposta para um `end-point` particular pode causar um aumento na taxa de transferência e na capacidade ao longo de um fluxo de solicitação, afetando um subsistema totalmente diferente.


### O Ciclo Hype e Lei de Amara

[The ciclo Hype on Wikipedia](https://en.wikipedia.org/wiki/Hype_cycle)

> Nós tendemos a superestimar os efeitos da tecnologia em curto prazo e subestimar os efeitos a longo prazo.
>
> Roy Amara

O Ciclo Hype é uma representação visual da empolgação e desenvolvimento da tecnologia ao longo do tempo, originalmente produzida por Gartner.
![The Hype Cycle](../images/hype-cycle.svg)

*(Image Reference: By Jeremykemp at English Wikipedia, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=10547051)*

Em curto prazo, o ciclo sugere que acontece uma explosão de empolgação a cerca de uma nova tecnologia e seu impacto em potencial. Equipes geralmente entram juntas nessas tecnologias de forma rápida e em alguns casos ficam desapontadas com os resultados. Uma das possíveis causas para isso é o fato da tecnologia em questão não ser madura o suficiente, ou aplicações do mundo real que não estão totalmente prontas. Depois de um certo tempo, a capacidade da tecnologia aumenta e oportunidades práticas para uso dela aumentam, as equipes finalmente podem ser produtivas. A citação de Amara resume isso de forma sucinta - "Nós tendemos a superestimar os efeitos da tecnologia em curto prazo e subestimar os efeitos a longo prazo".


### Lei de Hyrum (Lei das Interfaces Implícitas)

[Lei de Hyrum site](http://www.hyrumslaw.com/)

> Com um número suficientes de clientes de uma API,
> não importa a sua pré-condição no contato:
> todos os comportamentos observáveis do seu sistema
> serão dependentes de alguém.
>
> Hyrum Wright

A lei de Hyrum sugere que quando você tem um número muito grande de consumidores de uma API, todos os comportamentos dessa API (mesmo aqueles que não estão definidos como parte de um contrato público) eventualmente irão depender de outra parte do sistema, ou outra API. Um exemplo trivial pode ser elementos não funcionais, como o tempo de resposta de uma API. Um exemplo mais sutil pode ser os consumidores que estão confiando em aplicar um regex a uma mensagem de erro para determinar o _tipo_ de erro de uma API. Mesmo que o contrato público da API não especifique nada sobre o conteúdo da mensagem, indicando que os usuários devem usar um código de erro associado, alguns usuários podem usar a mensagem e alterar a mensagem essencialmente interrompe a API para esses usuários.

Veja Também:

- [XKCD 1172](https://xkcd.com/1172/)


### Lei de Kernighan

> A depuração é duplamente mais difícil do que escrever o código em primeiro lugar. Portanto, se você escrever o código da maneira mais inteligente possível, por definição, você não é inteligente o suficiente para depurá-lo.
>
> Brian Kernighan

A Lei de Kerningham é nomeada por [Brian Kernighan](https://en.wikipedia.org/wiki/Brian_Kernighan) e derivada de uma citação de Kerningham no livro [The Elements of Programming Style](https://en.wikipedia.org/wiki/The_Elements_of_Programming_Style):

> Todo mundo sabe que depurar é duplamente mais difícil do que programar em primeiro lugar. Então, se você é o mais inteligente possível quando escreve, como você conseguirá depurar o código?

Enquanto hiperbólica, a Lei de Kerningham faz a argumentação de que código simples deve ser preferido ao invés de código complexo, porque depurar qualquer problema que poderá surgir em um código complexo pode ser custoso ou até mesmo inviável.

Veja também:

- [Princípio KISS](#o-princípio-kiss)
- [Filosofia Unix](#a-filosofia-unix)
- [Navalha de Occam](#navalha-de-occam)


### Lei de Metcalfe

[Metcalfe's Law on Wikipedia](https://en.wikipedia.org/wiki/Metcalfe's_law)

> Na teoria das redes, o valor de um sistema cresce aproximadamente o quadrado do número de usuários daquele sistema.

Esta lei é baseada no número de possíveis conexões pareadas dentro de um sistema e é relacionada com a [Lei de Reed](#lei-de-reed). Odlyzko e outros argumentaram que tanto a Lei de Reed e a Lei de Metcalfe exageram o valor do sistema, não levando em consideração os limites da cognição humana sobre os efeitos da rede; veja [Número de Dunbar](#número-de-dunbar).

Veja também:
- [Lei de Reed](#lei-de-reed)
- [Número de Dunbar](#número-de-dunbar)

### Lei de Moore

[Lei de Moore na Wikipedia](https://en.wikipedia.org/wiki/Moore%27s_law)

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

Essas 'leis' são geralmente utilizadas em um sentido cômico. Contudo, fenômenos como [_Confirmation Bias_](#TODO) e [_Selection Bias_](#TODO) podem levar as pessoas a enfatizarem demais essas leis (na maioria das vezes quando as coisas funcionam, elas passam desapercebidas, as falhas são mais perceptíveis e atraem mais discussões).

Veja também:

- [Confirmation Bias](#TODO)
- [Selection Bias](#TODO)

### Navalha de Occam

[Navalha de Occam on Wikipedia](https://en.wikipedia.org/wiki/Occam's_razor)

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

A lei de Parkinson foi publicada por Cyril Northcote Parkinson num artigo na revista The Economist em 1955, sendo depois reimpresso com outros artigos no livro Parkinson's Law: The Pursuit of Progress [A lei de Parkinson: a busca do progresso]. Em seu contexto original, essa Lei foi baseada em estudos de burocracia. E pode ser pessimisticamente aplicado a desenvolvimento de software, a teoria diz que equipes serão ineficientes até os prazos finais, quando irão dar o máximo até o prazo final.

### Efeito de Otimização Prematura

[Premature Optimization on WikiWikiWeb](http://wiki.c2.com/?PrematureOptimization)

> Otimização prematura é a raiz de todo o mal.
>
> [(Donald Knuth)](https://twitter.com/realdonaldknuth?lang=en)

No artigo de Donald Knuth, [Structured Programming With Go To Statements](http://wiki.c2.com/?StructuredProgrammingWithGoToStatements), ele escreve: "Programadores perdem grandes quantidades de tempo pensando ou se preocupando com a velocidade de partes não críticas de seus programas, e essas tentativas de eficiência possuem um forte impacto negativo quando depuração e manutenção são consideradas. Nós devemos esquecer essas pequenas eficiências, cerca de 97% das vezes: **otimização prematura é a raiz de todo o mal.** No entanto, não devemos perder a oportunidade nesses 3% críticos".

Contudo, _Otimização Prematura_ pode ser definida (em termos menos carregados) como otimizar antes de saber o que precisamos.

### Lei de Putt

[Lei de Putt na wikipedia](https://en.wikipedia.org/wiki/Putt%27s_Law_and_the_Successful_Technocrat)

> Tecnologia é dominada por dois tipos de pessoa. Aqueles que entendem o que não gerenciam e aqueles que gerenciam o que não entendem.

A Lei de Putt é frequentemente seguida pelo Corolário de Putt:

> Cada hierarquia técnica, no tempo, desenvolve uma inversão de competência.

Estas declarações sugerem que devido a vários critérios de seleção e tendências na forma como grupos se organizam, haverá um número de pessoas qualificadas nos níveis de trabalho de organizações técnicas, e um número de pessoas em funções gerenciais que não estão cientes das complexidades e desafios do trabalho que estão gerenciando. Isso pode ser devido a fenômenos como o [Princípio de Peter](#o-princípio-de-peter) ou o [Princípio Dilbert](#o-princípio-dilbert).

No entanto, deve-se enfatizar que leis como essa são vastas generalizações e podem ser aplicáveis a alguns tipos de organizações, mas não a outras.

Veja também:

- [Principio de Peter](#o-princípio-de-peter)
- [Princípio de Dilbert](#o-princípio-dilbert)

### Lei de Reed

[Reed's Law on Wikipedia](https://en.wikipedia.org/wiki/Reed's_law)

> A utilidade de grandes redes, particularmente redes sociais, escalam exponencialmente com o tamanho da própria rede.

Essa lei é baseada na teoria dos grafos, onde a utilidade é escalonada com o número de possíveis subgrupos, que é mais rápido que o número de participantes ou o número de possíveis conexões pareadas. Odlyzko e outros argumentam que a Lei de Reed exagera a utilidade de um sistema por não levar em conta os limites da cognição humana sobre os efeitos da rede; veja [Número de Dunbar](#número-de-dunbar).

Veja também:
- [Lei de Metcalfe](##lei-de-metcalfe)
- [Número de Dunbar](#número-de-dunbar)

### A Lei da Conservação da Complexidade (Lei de Tesler)

[A lei da Conservação de Complexidade na wikipedia](https://en.wikipedia.org/wiki/Law_of_conservation_of_complexity)

Essa lei sugere que em todos os sistemas sempre vai existir uma quantidade de complexidade que não pode ser reduzida.

Alguma complexidade em um sistema é "inadvertida". É uma consequência da estrutura deficiente, erros ou apenas má modelagem de um problema a ser resolvido. A complexidade inadvertida pode ser reduzida (ou eliminada). No entanto, alguma complexidade é "intrínseca" como consequência da complexidade inerente ao problema a ser resolvido. Essa complexidade pode ser movida, mas não eliminada.

Um elemento interessante para essa lei é a sugestão de que, mesmo simplificando todo o sistema, a complexidade intrínseca não é reduzida, ela é “movida para o usuário”, que deve se comportar de uma maneira mais complexa.

### A Lei das Abstrações Gotejantes

[The Law of Leaky Abstractions on Joel on Software](https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/)

>Todas as abstrações não triviais, até certo ponto, são vazadas

Essa lei afirma que abstrações, as quais são geralmente utilizadas na computação para simplificar um trabalho com sistemas complexos, em certas situações irão 'vazar' elementos do sistema subjacente, fazendo com que a abstração se comporte de maneira inesperada.

Um exemplo disso pode ser carregar um arquivo e ler o seu conteúdo. As APIs do sistema de arquivo são abstrações do kernel de nível inferior, que são uma abstração dos processadores físicos relacionados à alteração de dados no disco rígido (ou na memória flash em SSD). Na maioria dos casos, a abstração de tratar um arquivo como um fluxo de dados binários funcionará. Contudo, para um disco rígido, a leitura sequencial dos dados será significantemente mais rápida que o acesso aleatório (devido ao aumento da sobrecarga de falhas na página), mas para um disco SSD, essa sobrecarga não estará presente. Os detalhes subjacentes precisarão ser entendidos para lidar com esse caso (por exemplo, os arquivos índices de uma base de dados são estruturados para reduzir a sobrecarga do acesso aleatório), a abstração 'vaza' detalhes de implementação os quais o desenvolvedor precisa estar ciente.

O exemplo acima pode se tornar mais complexo quando _mais_ abstrações são introduzidas. O sistema operacional Linux permite que os arquivos sejam acessados por rede mas representados localmente como arquivos 'normais'. Essa abstração será 'vazada' se houverem falhas de rede. Se um desenvolvedor tratar esses arquivos como 'normais', sem considerar o fato de que eles podem estar sujeitos à latência e falhas na rede, as soluções serão incorretas.

Veja também:

- [Lei de Hyrum](#lei-de-hyrum-lei-das-interfaces-implícitas)

Exemplos do mundo real:

- [Photoshop Slow Startup](https://forums.adobe.com/thread/376152) - um problema que eu encontrei no passado. O Photoshop demorava para abrir, às vezes levando alguns minutos. Parecia que o problema era que, ao iniciar, o programa lia algumas informações sobre a impressora padrão. No entanto, se essa impressora fosse uma impressora de rede, isso demoraria tempo extremamente longo. A _abstração_ de uma impressora de rede ser mostrada ao sistema como uma impressora local causou um problema para usuários em situação de baixa conectividade.

### A Lei da Trivialidade

[The Law of Triviality on Wikipedia](https://en.wikipedia.org/wiki/Law_of_triviality)

Essa lei sugere que grupos irão dar maior atenção para problemas triviais ou cosméticos, do que para os problemas sérios e substanciais.

O exemplo fictício comum utilizado é o de um comitê aprovando planos para uma usina nuclear, que passam maior tempo discutindo a estrutura do bicicletário ao invés do design da própria usina que é muito mais importante. Pode ser difícil fornecer informações valiosas em discussões sobre tópicos muito grandes e complexos sem um alto grau de conhecimento ou preparação no assunto. No entanto, as pessoas querem ser vistas contribuindo com informações importantes. Daí uma tendência de concentrar muito tempo em pequenos detalhes, que podem ser facilmente explicados, mas necessariamente não são de importância particular.

O exemplo fictício acima levou ao uso do termo _'Bike Shedding'_ como uma expressão por gastar tempo em detalhes triviais.


### A Filosofia Unix

[The Unix Philosophy on Wikipedia](https://en.wikipedia.org/wiki/Unix_philosophy)

A Filosofia Unix prega que componentes de um software devem ser pequenos, e focados em fazer muito bem uma coisa específica. Isso torna mais fácil a construção de sistemas compondo unidades pequenas, simples e bem definidas, em vez de usar programas grandes, complexos e multiuso.

Práticas modernas como a 'Arquitetura de Microsserviços' podem ser pensadas como uma aplicação dessa lei, onde os serviços são pequenos, focados em uma tarefa específica, permitindo que um comportamento complexo seja composto de blocos de construção simples.

### O Modelo Spotify

[The Spotify Model on Spotify Labs](https://labs.spotify.com/2014/03/27/spotify-engineering-culture-part-1/)

O Modelo Spotify é uma abordagem para a organização de equipes que foi popularizado pelo 'Spotify'. Neste modelo, times são organizados por funcionalidades, não por tecnologias.

O Modelo Spotify também popularizou o conceito de Tribos, Guildas, Capítulos, que são outros componentes de sua estrutura organizacional.

### Lei de Wadler

[Wadler's Law on wiki.haskell.org](https://wiki.haskell.org/Wadler's_Law)

> Em qualquer design de linguagem, o tempo total gasto discutindo a uma funcionalidade nessa lista é proporcional a dois elevados à potência de sua posição.
>
> 0. Semântica
> 1. Sintaxe
> 2. Sintaxe léxica
> 3. Sintaxe léxica de comentários
>
> (Em resumo, para cada hora gasta em semântica, 8 horas serão gastas na sintaxe de comentários)

Semelhante à [Lei da Trivialidade](#a-lei-da-trivialidade), a Lei de Wadler afirma que quando projetamos uma linguagem, o tempo gasto em estruturas é desproporcionalmente maior do que a importância dessas funcionalidades.

Veja também:

- [The Law of Triviality](#the-law-of-triviality)

### Lei de Wheaton

[The Link](http://www.wheatonslaw.com/)

[The Official Day](https://dontbeadickday.com/)

> Não seja um babaca
>
> _Wil Wheaton_

Cunhada por Wil Wheaton (Star Trek: The Next Generation, The Big Bang Theory), esta lei simples, concisa e poderosa visa aumentar a harmonia e o respeito dentro de uma organização profissional. Ela pode ser aplicada ao conversar com colegas de trabalho, ao efetuar code reviews, contrariar outros pontos de vista, criticar, e, em linhas gerais, na maioria das interações que os humanos mantém entre si.

## Princípios

Os princípios são como diretrizes relacionadas à design.

### O Princípio Dilbert

[The Dilbert Principle on Wikipedia](https://en.wikipedia.org/wiki/Dilbert_principle)

> Empresas tendem a promover sistematicamente funcionários incompetentes para a gerência para tirá-los do fluxo de trabalho.
>
> _Scott Adams_

Um conceito de gerência desenvolvido por Scott Adams (criador da tirinha Dilbert), o Princípio de Dilbert é inspirado pelo [Princípio de Peter](#o-princípio-de-peter). Sob o Princípio de Dilbert, funcionários que nunca foram competentes são promovidos para a gerência, para limitar o estrago que eles podem causar. Adams explicou esse princípio pela primeira vez um artigo no Wall Street Journal, em 1995, e o expandiu para seu livro de negócios em 1996, o [The Dilbert Principle](#lista-de-leitura).

Veja também:

- [Princípio de Peter](#o-princípio-de-peter)
- [Lei de Putt](#lei-de-putt)

### O Princípio de Pareto (Regra do 80/20)

[The Pareto Principle on Wikipedia](https://en.wikipedia.org/wiki/Pareto_principle)

> A maioria das coisas na vida não são distribuídas de maneira uniforme.

O Princípio de Pareto sugere que em alguns casos, a maioria dos resultados vem de uma minoria de insumos:

- 80% de um certo pedaço de software pode ser escrito em 20% do tempo total alocado (inversamente, os 20% mais difíceis do código levam 80% do tempo)
- 20% do esforço produz 80% do resultado
- 20% do trabalho cria 80% da receita
- 20% dos bugs causam 80% das quebras
- 20% das funcionalidades causam 80% da utilização

Nos anos 40 o engenheiro americano-romeno Dr. Joseph Juran, reconhecido como pai do controle de qualidade, [começou a aplicar o Princípio de Pareto a questões de qualidade](https://en.wikipedia.org/wiki/Joseph_M._Juran).

Este princípio é também conhecido como: A Regra do 80/20, A Lei dos Poucos Vitais e O Princípio de Escassez do Fator.

Exemplos do mundo real:

- Em 2002 a Microsoft reportou que corrigindo 20% dos erros mais reportados, 80% dos erros e quebras relacionadas no Windows e no Office foram eliminados ([Referência](https://www.crn.com/news/security/18821726/microsofts-ceo-80-20-rule-applies-to-bugs-not-just-features.htm)).

### O Princípio de Peter

[The Peter Principle on Wikipedia](https://en.wikipedia.org/wiki/Peter_principle)

> Pessoas em uma hierarquia tentem a subir ao seu "nível de incompetência".
>
> _Laurence J. Peter_

Um conceito de gerenciamento desenvolvido por Laurence J. Peter, o Princípio de Peter observa que as pessoas que são boas em seu emprego são promovidas até um nível onde elas não são mais bem-sucedidas (o "nível de incompetência"). Neste ponto, à medida em que são mais seniores, é menos provável que elas sejam removidas da organização (a não ser que elas performem de maneira horrível) e irão continuar a permanecer em uma função na qual possuem poucas habilidades intrínsecas, pois as habilidades originais que as fizeram bem-sucedidas não são necessariamente as mesmas que o novo cargo exige.

Isso é de interesse particular para engenheiros - que inicialmente começam em funções técnicas mas tem uma carreira que leva ao _gerenciamento_ de outros engenheiros - o que requer um conjunto de habilidades fundamentalmente diferente.

Veja também:

- [The Dilbert Principle](#the-dilbert-principle)
- [Putt's Law](#putts-law)

### O Princípio da Robustez (Lei de Postel)

[The Robustness Principle on Wikipedia](https://en.wikipedia.org/wiki/Robustness_principle)

> Seja conservador naquilo que você faz, seja liberal naquilo que você aceita dos outros.

Geralmente aplicado no desenvolvimento de aplicativos para servidor, esse princípio afirma que o que você envia para outras pessoas deve ser o mínimo compatível possível, mas que você deve ter como objetivo permitir entradas fora de conformidade, se puderem ser processadas.

O objetivo desse princípio é construir sistemas que são robustos, pois eles conseguem lidar com dados mal formatados se a intenção ainda puder ser entendida. No entanto, há potenciais implicações de segurança na aceitação de entradas mal formatadas, principalmente se o processamento dessas entradas não for bem testado.

### SOLID

É um acrônimo para:

* S: [The Single Responsibility Principle](#the-single-responsibility-principle)
* O: [The Open/Closed Principle](#the-openclosed-principle)
* L: [The Liskov Substitution Principle](#the-liskov-substitution-principle)
* I: [The Interface Segregation Principle](#the-interface-segregation-principle)
* D: [The Dependency Inversion Principle](#the-dependency-inversion-principle)

Esses são os princípios-chave da [Programação Orientada a Objetos](#todo). Os princípios de design como esses devem ajudar os desenvolvedores a criarem sistemas mais sustentáveis.

### O Princípio da Responsabilidade Única

[The Single Responsibility Principle on Wikipedia](https://en.wikipedia.org/wiki/Single_responsibility_principle)

> Cada módulo ou classe deve possuir apenas uma única responsabilidade.

O primeiro dos princípios '[SOLID](#solid)'. Esse princípio sugere que módulos ou classes devem fazer apenas uma única coisa. Em termos mais práticos, isso significa que uma mudança simples a uma funcionalidade de um programa deve exigir uma mudança em apenas um componente. Por exemplo, mudar como uma senha é validada por complexidade deve exigir uma mudança em apenas uma parte do programa.

Teoricamente, isso deve tornar o código mais robusto, e fácil de ser mudado. Sabendo que um componente que está sendo alterado possui apenas uma responsabilidade significa que o _teste_ deverá ser mais fácil. Usando o exemplo anterior, trocar a complexidade do componente de senha deve afetar apenas as funcionalidades que são relacionadas com a complexidade de senha. Pode ser muito mais difícil argumentar sobre o impacto de uma alteração em um componente que tem muitas responsabilidades.

Veja também:

- [Object-Oriented Programming](#todo)
- [SOLID](#solid)

### O Princípio do Aberto/Fechado

[The Open/Closed Principle on Wikipedia](https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle)

> Entidades devem estar aberta para extensão e fechadas para modificação

O segundo princípio do '[SOLID](#solid)'. Esse princípio afirma que entidades (que podem ser classes, módulos, funções e afins) poderão ter seu comportamento _estendido_, mas que o comportamento já existente não poderá ser alterado.

Em um exemplo hipotético, imagine um módulo que converte um documento Markdown para HTML. Se o módulo pode ser estendido para aceitar uma nova funcionalidade do markdown, sem modificar a parte interna desse módulo, quer dizer que ele está aberto para extensões. Se o módulo _não_ pode ser modificado por um consumidor, de modo que as funcionalidades existentes do markdown sejam tratadas, então ele estará _fechado_ para modificações.

Esse princípio tem uma relevância particular na orientação a objetos, onde nós projetamos objetos para serem facilmente estendidos, mas evitamos projetar objetos onde o comportamento existente pode ser alterado de maneiras inesperadas.

Veja também:

- [Object-Oriented Programming](#todo)
- [SOLID](#solid)

### O Princípio da Substituição de Liskov

[The Liskov Substitution Principle on Wikipedia](https://en.wikipedia.org/wiki/Liskov_substitution_principle)

> Deve ser possível trocar um tipo por um subtipo, sem o sistema apresentar quebras.

O terceiro princípio '[SOLID](#solid)'. O princípio afirma que se um componente confia em um tipo, então ele deverá estar apto para utilizar subtipos daquele tipo, sem que o sistema falhe ou que ele conheça os detalhes daquele subtipo.

Como um exemplo, imagine que temos um método que lê um documento XML de uma estrutura que representa um arquivo. Se o método utiliza a base de um tipo 'arquivo', então qualquer coisa que seja derivada de 'arquivo' poderá ser utilizada na função. Se 'arquivo' suporta busca recursiva, e o interpretador de XML utiliza essa função, mas o tipo derivado 'arquivo de rede' falha quando tenta uma busca recursiva, então o tipo 'arquivo de rede' estaria violando o princípio.

Esse princípio tem uma relevância particular na orientação a objetos, onde as hierarquias de tipos precisam ser modeladas com cautela para evitar confusão entre usuários do sistema.

Veja também:

- [Object-Oriented Programming](#todo)
- [SOLID](#solid)

### O Princípio da Segregação de Interface

[The Interface Segregation Principle on Wikipedia](https://en.wikipedia.org/wiki/Interface_segregation_principle)

> Nenhum cliente deverá ser forçado a depender de métodos que ele não utilize.

O quarto princípio do '[SOLID](#solid)'. Esse princípio afirma que os consumidores de um componente não devem depender de funções daquele componente, as quais eles atualmente não usem.

Como um exemplo, imagine que um método lê um documento XML de uma estrutura que representa um arquivo. O método apenas precisa ler os bytes, ir para frente ou para trás no arquivo. Se esse método precisar ser atualizado porque um recurso não relacionado da estrutura do arquivo é alterado (como uma atualização no modelo de permissões utilizado para representar a segurança do arquivo), o princípio foi invalidado.

Esse princípio tem uma relevância particular na orientação a objetos, onde interfaces, hierarquias e tipos abstratos são utilizados para [minimizar o acoplamento](#todo) entre componentes diferentes. [Duck typing]() é uma metodologia que impõe esse princípio, eliminando interfaces explícitas.

Veja também:

- [Object-Oriented Programming](#todo)
- [SOLID](#solid)
- [Duck Typing](#todo)
- [Decoupling](#todo)

### O Princípio da Inversão de Dependência

[The Dependency Inversion Principle on Wikipedia](https://en.wikipedia.org/wiki/Dependency_inversion_principle)

> Módulos de alto nível não devem ser dependentes de implementações de baixo nível.

O quinto conceito do '[SOLID](#solid)'. Esse princípio afirma que componentes

Como um exemplo, imagine que temos um programa que lê os metadados de um website. Nós devemos assumir que o componente principal precisa conhecer um componente que irá baixar a página, depois um outro componente que irá ler os metadados. Se fôssemos levar a inversão de dependências em conta, o componente principal deveria depender apenas de um componente abstrato que pode buscar pelos bytes, e depois outro componente abstrato que irá ler os metadados de um fluxo de bytes. O componente principal não sabe nada sobre TCP/IP, HTTP, HTML, etc.

Esse princípio é complexo, pois pode "inverter" as dependências esperadas de um sistema (daí o nome). Na prática, isso também significa que um componente de orquestração separado deve garantir que as implementações corretas dos tipos abstratos sejam usadas (por exemplo, no caso anterior, _algo_ ainda deve fornecer ao componente de leitura dos de metadados um downloader de arquivos HTTP e um leitor de metatags HTML). Isso toca em padrões como [Inversão de controle](#todo) e [Injeção de dependência](#todo).

Veja também:

- [Object-Oriented Programming](#todo)
- [SOLID](#solid)
- [Inversion of Control](#todo)
- [Dependency Injection](#todo)

### O Princípio DRY

[The DRY Principle on Wikipedia](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)

> Cada pedaço de código deve possuir uma representação única, inequívoca e autoritária dentro de um sistema.

DRY é um acrônimo para _**D**on't **R**epeat **Y**ourself_ (Não repita você mesmo). Esse princípio ajuda os desenvolvedores a reduzir a repetição de código e manter a informação em um único lugar. Foi citado em 1999 por Andrew Hunt e Dave Thomas no livro [The Pragmatic Programmer](https://en.wikipedia.org/wiki/The_Pragmatic_Programmer).

> O oposto de DRY seria WET (Write Everything Twice or We Enjoy Typing) - (Escreva tudo duas vezes ou Nós gostamos de digitar).

Na prática, se você tem o mesmo pedaço de informação em dois (ou mais) lugares diferentes, você pode utilizar o DRY para centralizá-los em um único lugar, e reutilizar a informação onde necessário.

Veja também:

- [The Pragmatic Programmer](https://en.wikipedia.org/wiki/The_Pragmatic_Programmer)

### O Princípio KISS

[KISS on Wikipedia](https://en.wikipedia.org/wiki/KISS_principle)

> Mantenha simples, idiota

KISS é um acrônimo para _**K**eep **i**t **s**imple, **s**tupid_. O princípio afirma que a maioria dos sistemas trabalham melhor se eles são mantidos simples ao invés de complicados. Portanto, simplicidade deve ser um objetivo no design, e complexidades desnecessárias devem ser evitadas. Originada na Marinha Americana em 1960, a frase foi associada com o engenheiro de aeronaves Kelly Johnson.

O princípio é melhor exemplificado pela história de Johnson entregando a uma equipe de engenheiros de projeto algumas ferramentas, com o desafio de que as aeronaves a jato que estavam projetando deveriam ser reparadas por um mecânico comum em campo sob condições de combate apenas com essas ferramentas. Portanto, o "estúpido" refere-se à relação entre a maneira como as coisas quebram e a sofisticação das ferramentas disponíveis para repará-las, e não as capacidades dos próprios engenheiros.

Veja também:

- [Lei de Gall](#lei-de-gall)

### YAGNI

[YAGNI on Wikipedia](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it)

É um acrônimo para _**Y**ou **A**ren't **G**onna **N**eed **I**t_ - Você não vai precisar disto.

> Sempre implemente as coisas quando você de fato precisar delas, nunca quando você prevê que precisará delas.
>
> ([Ron Jeffries](https://twitter.com/RonJeffries)) (XP co-founder e autor do livro "Extreme Programming Installed")

Este princípio da _Extreme Programming_ (XP) sugere que os desenvolvedores apenas devem implementar funcionalidades quando elas forem necessárias, e evitar tentativas de prever o futuro e implementar uma funcionalidade que talvez seja necessária.

Aderir a esse princípio deve reduzir a quantidade de código não utilizado em um projeto, e evitar tempo e esforço sendo desperdiçados em funcionalidades que não agregam valor.

Veja também:

- [Reading List: Extreme Programming Installed](#lista-de-leitura)

### As Falácias da Computação Distribuída

[The Fallacies of Distributed Computing on Wikipedia](https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing)

Também conhecidas como as _Falácias da Computação em rede_, as Falácias são uma lista de conjecturas (ou crenças) sobre a computação distribuídas, que podem levar a falhas no desenvolvimento de software. As suposições são:

- A rede é confiável
- A latência é zero
- A largura de banda é infinita
- A rede é segura
- A topologia não muda
- Existe apenas um administrador
- Custo de transporte é zero
- A rede é homogênea

Os primeiro quatro itens foram listados por [Bill Joy](https://en.wikipedia.org/wiki/Bill_Joy) e [Tom Lyon](https://twitter.com/aka_pugs) por volta de 1991, e foram classificados por [James Gosling](https://en.wikipedia.org/wiki/James_Gosling) como as "Falácias da Computação de rede". [L. Peter Deutsch](https://en.wikipedia.org/wiki/L._Peter_Deutsch) adicionou os itens 5, 6 e 7. No final dos anos 90, Gosling adicionou o item 8.

O grupo foi inspirado pela situação que corria na época dentro da [Sun Microsystems](https://en.wikipedia.org/wiki/Sun_Microsystems).

Essas falácias devem ser consideradas com cuidado ao projetar um código que seja resiliente; supondo que qualquer uma dessas falácias possa levar a uma lógica defeituosa que falha em lidar com as realidades e complexidades dos sistemas distribuídos

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

- [Tip of the Day](https://tips.darekkay.com/html/hacker-laws-en.html) - Receba diariamente uma lei ou princípio hacker.
- [Hacker Laws CLI](https://github.com/umutphp/hacker-laws-cli) - Liste e visualize as leis de maneira aleatória no seu terminal!

## Contribuindo

Por favor, contribua! [Abra uma issue](https://github.com/dwmkerr/hacker-laws/issues/new) se você deseja ver aqui algum conteúdo novo, sugerir uma alteração/correção, ou então [abra uma pull request](https://github.com/dwmkerr/hacker-laws/compare) e proponha suas próprias modificações.

Certifique-se de ler as [Diretrizes de Contribuição](../.github/contributing.md) para saber sobre os padrões de texto, estilo etc. Esteja ciente do [Código de Conduta](../.github/CODE_OF_CONDUCT.md) ao participar de discussões sobre o projeto.

## Em construção

Olá! Se você parou aqui, clicou em um link para um tópico que não foi escrito ainda. Desculpe por isso, este trabalho está em andamento!

Sinta-se livre para [abrir uma issue](https://github.com/dwmkerr/hacker-laws/issues) solicitando mais detalhes, ou [abra uma pull request](https://github.com/dwmkerr/hacker-laws/compare) para submeter suas modificações.
