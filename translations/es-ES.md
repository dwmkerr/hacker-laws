# 💻📖 hacker-laws

Leyes, Teorías, Principios y Patrones que los desarrolladores encontrarán útiles.

[traducciones](#translations):  [🇧🇷](./translations/pt-BR.md) [🇨🇳](https://github.com/nusr/hacker-laws-zh) [🇫🇷](./translations/fr.md) [🇮🇹](./translations/it-IT.md) [🇱🇻](./translations/lv.md) [🇰🇷](https://github.com/codeanddonuts/hacker-laws-kr) [🇷🇺](https://github.com/solarrust/hacker-laws) [🇹🇷](./translations/tr.md) [🇮🇩](./translations/id.md) [🇯🇵](./translations/jp.md) [🇵🇱](./translations/pl.md) [🇻🇳](./translations/vi.md)

¿Te gusta este proyecto? Por favor, considera [Esponsorizarme](https://github.com/sponsors/dwmkerr)!

---

<!-- vim-markdown-toc GFM -->

* [Introducción](#introduccion)
* [Leyes](#leyes)
    * [Ley de Amdahl](#ley-de-amdahl)
    * [Ley de Brooks](#ley-de-brooks)
    * [Ley de Conway](#ley-de-conways)
    * [Ley de Cunningham](#ley-de-cunningham)
    * [Número de Dunbar](#numero-de-dunbar)
    * [Ley de Gall](#ley-de-gall)
    * [Cuchilla de Hanlon](#cuchilla-de-hanlon)
    * [Ley de Hofstadter](#ley-de-hofstadter)
    * [Ley de Hutber](#ley-de-hutber)
    * [El Ciclo de Sobreexpectación y la Ley de Amara](#el-ciclo-de-sobreexpectacion-y-la-ley-de-amara)
    * [Ley de Hyrum (La Ley de las Interfaces Implícitas)](#ley-de-hyrum-la-ley-de-las-interfaces-implicitas)
    * [Ley de Metcalfe](#ley-de-metcalfe)
    * [Ley de Moore](#ley-de-moore)
    * [Ley de Murphy / Ley de Sod](#ley-de-murphy--ley-de-sod)
    * [Ley de Parkinson](#ley-de-parkinson)
    * [Efecto de Optimización Prematura](#efecto-de-optimizacion-prematura)
    * [Ley de Putt](#ley-de-putt)
    * [Ley de Reed](#ley-de-reed)
    * [Ley de Conservación de Complejidad (Ley de Tesler)](#ley-de-conservacion-de-complejidad-ley-de-tesler)
    * [Ley de Abstracciones Permeables](#ley-de-abstracciones-permeables)
    * [Ley de la Trivialidad](#ley-de-la-trivialidad)
    * [Filosofía Unix](#filosofia-unix)
    * [El Modelo Spotify](#el-modelo-spotify)
    * [Ley de Wadler](#ley-de-wadler)
* [Principios](#principios)
    * [El Principio de Dilbert](#el-principio-de-dilbert)
    * [El Principio de Pareto (La Regla 80/20)](#el-principio-de-pareto-la-regla-8020)
    * [El Principio de Peter](#el-principio-de-peter)
    * [El Principio de la Robustez (Ley de Postel)](#el-principio-de-la-robustez-ley-de-postel)
    * [SOLID](#solid)
    * [El Principio de Única Responsabilidad](#el-principio-de-unica-responsabilidad)
    * [El Principio Abierto/Cerrado](#el-principio-abierto-cerrado)
    * [El Principio de Sustitución de Liskov](#el-principio-de-sustitucion-de-liskov)
    * [El Principio de Segregación de Interfaz](#el-principio-de-segregacion-de-interfaz)
    * [El Principio de Inversión de Dependencia](#el-principio-de-inversion-de-dependencia)
    * [El Principio DRY](#el-principio-dry)
    * [El Principio KISS](#el-principio-kiss)
    * [YAGNI](#yagni)
* [Lista de Lectura](#lista-de-lectura)
* [POR-HACER](#por-hacer)

<!-- vim-markdown-toc -->

## Introducción

Hay montones de leyes que la gente discute cuando habla sobre desarrollo. Este repositorio es una referencia y un resumen de algunos de los más conocidos. Por favor, ¡comparte y sube tus PRs!

❗: Este repositorio contiene una explicación sobre algunas leyes, principios y patrones, pero no _defendemos_ ninguno de ellos. Si estos pueden ser aplicados o no siempre será materia de debate y muy dependiente de en qué estés trabajando.

## Leyes

¡Y aquí vamos!

### Ley de Amdahl

[Ley de Amdahl en Wikipedia](https://es.wikipedia.org/wiki/Ley_de_Amdahl)

> La ley de Amdahl se puede interpretar de manera más técnica, pero en términos simples, significa que es el algoritmo el que decide la mejora de velocidad, no el número de procesadores. Finalmente se llega a un momento que no se puede paralelizar más el algoritmo.

Mejor lo ilustramos con un ejemplo. Si un programa se compone de dos partes, la parte A debe ser ejecutada en un solo procesador y la parte B puede ser paralelizada, entonces vemos que agregamos múltiples procesadores al sistema en ejecución ese programa puede solo tener un beneficio limitado. Este puede potencialmente mejorar mucho la velocidad de la parte B - pero la velocidad de la parte A se mantendrá sin cambios.

El diagrama de abajo muestra algunos ejemplos de mejoras potenciales en velocidad:

![Diagram: Amdahl's Law](./images/amdahls-law.svg)

*(Imagen de Referencia: Por Daniels220 en Wikipedia, Creative Commons Attribution-Share Alike 3.0 Unported, https://en.wikipedia.org/wiki/File:AmdahlsLaw.svg)*

Como podemos ver, incluso un programa el cual es un 50% paralelizable se beneficiará muy poco más allá de 10 unidades de procesamiento, mientras que un programa el cual es 95% paralelizable todavía puede alcanzar mejoras significativas de velocidad con más de mil unidades de procesamiento.

A medida que la [Ley de Moore](#ley-de-moore) se ralentiza y la aceleración de la velocidad del procesador individual disminuye, la paralelización es la clave para incrementar el rendimiento.La programación de gráficos es un excelente ejemplo: con la informática moderna basada en Shader, píxeles individuales o fragmentos pueden ser renderizados en paralelo. Este es el porqué las tarjetas gráficas modernas en ocasiones disponen de miles de núcleos de procesamiento (GPUs o Unidades de Shader).

Vea también:

- [Ley de Brooks](#ley-de-brooks)
- [Ley de Moore](#ley-de-moore)

### Ley de Brooks

[Ley de Brooks en Wikipedia](https://es.wikipedia.org/wiki/Ley_de_Brooks)

> Cuando se incorpora una persona en un proyecto, éste se ralentiza en lugar de acelerarse. Brooks también afirmó que "Nueve mujeres no pueden tener un bebé en un mes".

Esta ley sugiere que en muchos casos, intentar acelerar la entrega de un proyecto el cual ya va tarde, agregando más personas, hará que la entrega vaya aún más tarde. Brooks clarifica que esto es una simplificación, sin embargo, el razonamiento general es que el tiempo de aceleración de nuevos recursos y la sobrecarga de comunicación, en el inmediato corto plazo hace que la velocidad caiga. También, muchas tareas pueden no ser divisibles, es decir que pueden no ser fácilmente distribuibles entre más personas, significando que el potencial incremento de velocidad es incluso menor.

La frase común en entregas "Nueve mujeres no pueden tener un bebé en un mes" está relacionada a la Ley de Brooks, en particular, al hecho de que algunos tipos de trabajos no son divisibles ni paralelizables.

Este es el tema central del libro '[El Mítico Hombre Mes](#lista-de-lectura)'.

Vea también:

- [Marcha de la Muerte](#todo)
- [Lista de Lectura: El Mítico Hombre Mes](#reading-list)

### Ley de Conway

[La Ley de Conway en Wikipedia](https://es.wikipedia.org/wiki/Ley_de_Conway)

Esta ley sugiere que los límites técnicos de un sistema reflejan la estructura de la organización. Es comúnmente referido a cuando se observan mejoras de una organización, la Ley de Conway sugiere que si una organización es estructurada en muchas unidades pequeñas y desconectadas, el software que producirá será así. Si una organización es construída más entorno a soluciones 'verticales' las cuales están orientadas alrededor de características o servicios, los sistemas de software también reflejarán esto.

Vea también:

- [El Modelo Spotify](#el-modelo-spotify)

### Ley de Cunningham

[Ley de Cunningham en Wikipedia](https://meta.wikimedia.org/wiki/Cunningham%27s_Law/es)

> La mejor forma de obtener la respuesta correcta en Internet no es hacer una pregunta, es enviar la respuesta errónea.

Acorde a Steven McGeady, Ward Cunningham le aconsejó a principios de los 80: "La mejor forma de obtener la respuesta correcta en Internet no es hacer una pregunta, es enviar una respuesta incorrecta." McGeady lo llamó la Ley de Cunningham, sin embargo Cunningham niega su propiedad diciendo que es una cita errónea. Aunque originalmente se refiere a las interacciones en Usenet, la ley ha sido usada para describir como otras comunidades online funcionan (e.g., Wikipedia, Reddit, Twitter, Facebook).

Vea también:

- [XKCD 386: "Duty Calls" (El Deber Llama)](https://xkcd.com/386/)

### El Número de Dunbar

[El Número de Dunbar en Wikipedia](https://es.wikipedia.org/wiki/N%C3%BAmero_de_Dunbar)

"El número de Dunbar es un límite cognitivo sugerido sobre el número de personas con las que puedes mantener relaciones sociables estables- relaciones en las que un individuo sabe quien es la otra persona and cómo cada persona se relaciona con cada una de las otras personas." Hay algún desacuerdo sobre el número exacto. "... [Dunbar] propuso que los humanos pueden mantener cómodamente solo 150 relaciones estables." El puso el número dentro de un contexto más social, "el número de personas con las que no sentirías vergüenza de invitarlas a tomar una copa
"Dunbar's number is a suggested cognitive limit to the number of people with whom one can maintain stable social relationships— relationships in which an individual knows who each person is and how each person relates to every other person." There is some disagreement to the exact number. "... [Dunbar] proposed that humans can comfortably maintain only 150 stable relationships." He put the number into a more social context, "la cantidad de personas de las que no te sentirías avergonzado por unirte sin invitación a tomar una copa si te topas con ellas en un bar." Estima que el número puede rondar generalmente entre 100 y 250.

Al igual que relaciones estables entre individuos, la relación de un desarrollador con su código base toma esfuerzo mantenerla. Cuando afrontas un gran número de proyectos complicados o creas muchos proyectos, nos apoyamos en convenciones, políticas y modelamos procedimientos para escalar. El número de Dunbar no es solo importante para tener en mente como una oficina crece, también cuando configuramos el alcance de los esfuerzos de un equipo o decidimos cuando debemos invertir en herramientas para asistir en el modelado y automatizar el sobregasto logístico. Poniendo el número en el contexto de ingeniería, es el número de proyectos (o complejidad normalizada de un único proyecto) para los cuales podrías sentirte seguro de unirte para las rondas de soporte telefónico.

Vea también:

- [Ley de Conway](#ley-de-conway)

### Ley de Gall

[Ley de Gall en Wikipedia (inglés)](https://en.wikipedia.org/wiki/John_Gall_(author)#Gall's_law)

> Un sistema complejo que funciona ha sido evolucionado invariablemente desde un sistema simple que funcionaba. Un sistema complejo diseñado desde cero nunca funcionará y no puede ser arreglado para que funcione. Tienes que comenzar de nuevo con un sistema simple que funcione.
>
> ([John Gall](https://en.wikipedia.org/wiki/John_Gall_(author)))


La Ley de Gall implica que los intentos de _diseñar_ un sistema altamente complejo tenderán siempre a fallar. Sistemas altamente complejos son raramente construidos de una sola vez, estos suelen ser evoluciones de sistemas mucho más simples.

El ejemplo clásico es la World Wide Web (WWW). En su estado actual, es un sistema altamente complejo. Sin embargo, esta fue definida inicialmente como una forma simple de compartir contenido entre instituciones académicas. Esta fue un éxito cumpliendo sus objetivos y evolucionó para llegar a ser más compleja con el tiempo.

Vea también:

- [KISS (Keep It Simple, Stupid)](#el-principio-kiss)

### La Navaja de Hanlon

[La Navaja de Hanlon en Wikipedia](https://es.wikipedia.org/wiki/Principio_de_Hanlon)

> Nunca atribuyas a la malicia lo que puede ser adecuadamente explicado por la estupidez.
>
> Robert J. Hanlon

Este principio sugiere que las acciones resultantes en un resultado negativo no fueron resultado de una mala intención. En su lugar el resultado negativo es mejor atribuído a que esas acciones y/o el impacto no fueron completamente entendidos.

### Ley de Hofstadter

[Ley de Hofstadter en Wikipedia](https://es.wikipedia.org/wiki/Ley_de_Hofstadter)

> Siempre lleva más tiempo de lo que esperas, incluso si tienes en cuenta la Ley de Hofstadter.
>
> (Douglas Hofstadter)

Quizás hayas oído esta ley referida a cuando se busca estimar el tiempo que tomará algo. Esto parece una verdad absoluta en el desarrollo de software donde tendemos a no ser muy buenos estimando con precisión cuanto tiempo tomará entregar algo.

Esto proviene del libro '[Gödel, Escher, Bach: An Eternal Golden Braid](#lista-de-lectura)'.

Vea también:

- [Lista de lectura: Gödel, Escher, Bach: An Eternal Golden Braid](#lista-de-lectura)

### Ley de Hutber

[Ley de Hutber en Wikipedia (inglés)](https://en.wikipedia.org/wiki/Hutber%27s_law)

> Mejorar signfica deteriorar.
>
> ([Patrick Hutber (inglés)](https://en.wikipedia.org/wiki/Patrick_Hutber))

Esta ley sugiere que las mejoras realizadas en un sistema llevarán a su deterioro en otras partes, u ocultará otros deterioros, llevando a una degradación total del estado actual del sistema.

Por ejemplo, un decremento en la latencia de respuesta para un end-point particular podría causar problemas de rendimiento y capacidad de procesamiento más adelante en el flujo de peticiones, afectando a un subsistema completamente diferente.

### El Ciclo de Sobreexpectación y La Ley de Amara

[El Ciclo de Sobreexpectación](https://es.wikipedia.org/wiki/Ciclo_de_sobreexpectaci%C3%B3n)

> Tendemos a sobreestimar el efecto de una tecnología a corto plazo y subestimar su efecto a largo plazo.
>
> (Roy Amara)

El Ciclo de Sobreexpectación es una representación visual de la excitación y desarrollo de tecnología a lo largo del tiempo, originalmente producido por Gartner. Se explica mejor de forma visual:

![El Cico de Sobreexpectación](./images/hype-cycle.svg)

*(Referencia de Imagen: Por Jeremykemp en Wikipedia, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=10547051)*

En pocas palabras, el ciclo sugiere que hay una típica burbuja de excitación alrededor de cada nueva tecnología y su impacto potencial. Los equipos a veces saltan rápidamente a emplear estas tecnologías y a veces se encuentran a sí mismos decepcionados con los resultados. Esto puede ser porque la tecnología no es aún lo suficientemente madura, o las aplicaciones del mundo real no están completamente desarrolladas. Después de cierto tiempo, las capacidades de la tecnología se incrementan y las oportunidades de ser empleada de forma práctica aumentan permitiendo a los equipos ser finalmente productivos. La frase de Roy Amara resume este hecho de forma breve - "Tendemos a sobreestimar el efecto de una tecnología a corto plazo y subestimarla a largo plazo".

### Ley de Hyrum (La Ley de las Interfaces Implícitas)

[Ley de Hyrum (inglés)](http://www.hyrumslaw.com/)

> Con un número suficiente de usuarios de una API,
> no importa que prometas en el contrato:
> alguien dependerá de todos los comportamientos observables
> de tu sistema.
>
> (Hyrum Wright)

La Ley de Hyrum establece que cuando tienes un _número grande y suficiente de consumidores_ de una API, todos los comportamientos de la API (incluso aquellos no definidos como parte del contrato público) llegarán de forma eventual a ser dependencia de alguien. Un ejemplo trivial pueden ser los elementos no-funcionales como el tiempo de respuesta de una API. Un ejemplo más sutil puede ser qué consumidores están dependiendo en la aplicación de una expresión regular sobre un mensaje de error para determinar el *tipo* de error de una API. Incluso si el contrato público de la API no establece nada acerca del contenido del mensaje de error indicando a los usuarios que deben emplear un código de error, _algunos_ usuarios usarán el mensaje y cambiar el mensaje esencialmente romperá la API para estos usuarios.

Vea también:

- [La Ley de las Abstracciones Permeables](#la-ley-de-las-abstracciones-permeables)
- [XKCD 1172](https://xkcd.com/1172/)


### Ley de Metcalfe

[Ley de Metcalfe en Wikipedia (inglés)](https://en.wikipedia.org/wiki/Metcalfe's_law)

> En teoría de redes, el número en el que un sistema crece es aproximadamente el cuadrado del número de usuarios de ese sistema.

Esta ley está basada en el número de posibles conexiones por pares dentro de un sistema y está muy relacionado con [La Ley de Reed](#ley-de-reed). Odlyzko y otros han argumentado que ambas leyes (Reed y Metcalfe) exageran el valor de un sistema por no tener en cuenta los límites de la cognición humana en efectos de redes; vea [El Número de Dunbar](#numero-de-dunbar).

Vea también:
- [Ley de Reed](#ley-de-reed)
- [Número de Dunbar](#numero-de-dunbar)

### Ley de Moore

[Ley de Moore en Wikipedia](https://es.wikipedia.org/wiki/Ley_de_Moore)

> El número de transistores en un circuito integrado se dobla aproximadamente cada dos años.

A veces empleado para ilustrar la velocidad pura a la que un semiconductor y la tecnología de chips ha mejorado, la predicción de Moore probó ser altamente precisa desde los 70 hasta finales de la primera década de 2000. En los años recientes, la tendencia ha cambiado ligeramente, parcialmente debido a [las limitaciones físicas en el grado en el que los componentes pueden ser miniaturizados (inglés)](https://en.wikipedia.org/wiki/Quantum_tunnelling). Sin embargo, los avances en la paralelización y potencialmente los cambios revolucionarios en la tecnología de semiconductores y computación cuántica puedan significar que la Ley de Moore continúe siendo cierta en las siguientes décadas.

### Ley de Murphy / Ley de Sod

[Ley de Murphy en Wikipedia](https://es.wikipedia.org/wiki/Ley_de_Murphy)

> Si algo puede ir mal, irá mal.

Relacionado con [Edward A. Murphy, Jr](https://es.wikipedia.org/wiki/Edward_A._Murphy_Jr.) la _Ley de Murphy_ establece que si algo puede ir mal, irá mal.

Este dicho es muy común entre desarrolladores. A veces algo inesperado sucede cuando se desarrolla, se hacen pruebas o incluso en producción. Esto puede relacionarse también a la (más común en inglés británico) _Ley de Sod_:

> Si algo puede ir mal, irá mal, en el peor momento posible.

Estas leyes son generalmente empleadas en sentido cómico. Sin embargo, tales fenómenos como la [_Sesgo de Confirmación_](#por-hacer) y [_Sesgo de Selección_](#por-hacer) pueden llevar a la gente a sobre-enfatizar estas leyes (la mayoría de las veces cuando las cosas funcionan, estas pasan sin tenerse en cuenta, mientras que los fallos son muy notalbes y entran más en las conversaciones).

Vea también:

- [Sesgo de Confirmación](#por-hacer)
- [Sesgo de Selección](#por-hacer)

### Ley de Parkinson

[Ley de Parkinson en Wikipedia](https://es.wikipedia.org/wiki/Ley_de_Parkinson)

> El trabajo se expande hasta llenar el tiempo disponible para que se termine.

En su contexto original, esta Ley se basó en estudios de burocracias. Esta podía ser aplicada de forma pesimista a las iniciativas de desarrollo de software, la teoría sería que los equipos serán ineficientes hasta que la fecha de entrega esté cerca, entonces se apresurarán a completar el trabajo para la entrega, haciendo la fecha de entrega real de algún modo arbitraria.

Si esta ley se combina con la [Ley de Hofstadter](#ley-de-hofstadter), un punto de vista incluso más pesimista es alcanzado - el trabajo se expandirá hasta rellenar el tiempo disponible para su compleción y *aún tomará más tiempo del esperado*.

Vea también:

- [Ley de Hofstadter](#ley-de-hofstadter)

### Efecto de Optimización Prematura

[Optimización Prematura en Wikipedia](https://es.wikipedia.org/wiki/Optimizaci%C3%B3n_de_software#Cu%C3%A1ndo_optimizar)

> Debemos olvidar las pequeñas eficiencias, por ejemplo, el 97% del tiempo: la optimización prematura es la raíz de todos los males.
>
> [(Donald Knuth, diciembre de 1974)](https://twitter.com/realdonaldknuth)

En el documento de Donald Knuth titulado [Programación Estructurada con Mandatos Go To (inglés)](http://wiki.c2.com/?StructuredProgrammingWithGoToStatements), escribió: "Los programadores desperdician enormes cantidades de tiempo pensando o preocupándose acerca de la velocidad de partes no-críticas de sus programas, y esos intentos de eficiencia en realidad tienen un impacto negativo cuando consideramos la depuración o el mantenimiento. Debemos olvidar las pequeñas eficiencias, por ejemplo, el 97% del tiempo: **la optimización prematura es la raíz de todos los males**. Aunque no debemos dejar pasar nuestras oportunidades en ese crítico 3%."

Sin embargo, _Premature Optimization_ puede ser definido (en términos menos cargados) como nosotros sabemos lo que tenemos que hacer.

### Ley de Putt

[Ley de Putt (inglés)](https://en.wikipedia.org/wiki/Putt%27s_Law_and_the_Successful_Technocrat)

> La Tecnología es dominada por dos tipos de personas, aquellos quienes comprenden lo que no controlan y aquellos quienes controllan lo que no entienden.

La Ley de Putt a veces es seguida por el Corolario de Putt:

> Cada jerarquía técnica, con el tiempo, desarrolla una inversión de competencia.

Estos mandatos sugieren que debido a varios criterios de selección y tendencias en cómo los grupos se organizan, habrá un número de personas cualificadas en los niveles de trabajo de una organización técnica y una cantidad de personas en roles directivos que no son conscientes de las complejidades y desafíos del trabajo que están manejando. Esto puede ser debido al fenómenos tales como [El Principio de Peter](#el-principio-de-peter) o [El Principio de Dilbert](#el-principio-de-dilbert).

Sin embargo, debe enfatizarse que leyes como esta son generalizaciones amplias y pueden aplicarse a _algunos_ tipos de organizaciones y no a otras.

Vea también:

- [El Principio de Peter](#el-principio-de-peter)
- [El Principio de Dilbert](#el-principio-de-dilbert)

### La Ley de Reed

[La Ley de Reed en Wikipedia (inglés)](https://en.wikipedia.org/wiki/Reed's_law)

> La utilidad de redes grandes, particularmente redes sociales, escala exponencialmente con el tamaño de la red.

Esta ley está basada en la teoría de grafos, donde la utilidad escala como el número de posibles sub-grupos, el cuál es más rápido que el número de participantes o el número de posibles conexiones p
Esta ley se basa en la teoría de grafos, donde la utilidad se escala como el número de subgrupos posibles, que es más rápido que el número de participantes o el número de posibles conexiones por pares. Odlyzko y otros han argumentado que la Ley de Reed exagera la utilidad del sistema al no tener en cuenta los límites de la cognición humana sobre los efectos de la red; ver [El Número de Dunbar](#numero-de-dunbar).

See also:
- [La Ley de Metcalfe's Law](#metcalfes-law)
- [Número de Dunbar](#numero-de-dunbar)

### Ley de Conservación de Complejidad (Ley de Tesler)

[La Ley de Conservación de Complejidad en Wikipedia (inglés)](https://en.wikipedia.org/wiki/Law_of_conservation_of_complexity)

Esta ley establece que hay una cierta cantidad de complejidad en un sistema la cuál no puede ser reducida.

Cierta complejidad en un sistema puede ser 'involuntaria'. Es consecuencia de una estructura deficiente, errores o tan solo un mal modelo de un problema a resolver. La complejidad involuntaria puede ser reducida (o eliminada). Sin embargo, cierta complejidad es 'intrínseca' como consecuencia de la complejidad inherente de un problema que se está resolviendo. Esta complejidad puede ser desplazada, pero no eliminada.

Un elemento interesate de esta ley es la sugerencia de que incluso simplificando el sistema entero, la complejidad intrínseca no se reduce, esta se _desplaza hacia el usuario_, el cuál debe comportarse de una forma compleja.

### Ley de las Abstracciones Permeables

[La Ley de las Abstracciones Permeables en Joel on Software (inglés)](https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/)

> Toda abstracción no trivial, en algún grado, es permeable.
>
> ([Joel Spolsky](https://twitter.com/spolsky))

Esta ley establece que las abstracciones, las cuales son generalmente usadas en computación para simplificar el trabajo con sistemas complicados, en ciertas situaciones 'filtrarán' sus elementos a un sistema subyacente, haciendo que la abstracción se comporte de una forma inesperada.

Un ejemplo puede ser la carga de un fichero y lectura de sus contenidos. Las APIs del sistema de ficheros son una _abstracción_ del bajo nivel de los sistemas del kernel, los cuales son en sí mismos abstracciones de los procesos físicos relacionados con el cambio de información en un disco magnético (o memoria flash para un SSD). En la mayoría de los casos, funcionará la abstracción de tratar al fichero como un flujo de datos binarios. Sin embargo, para un disco magnético, leer datos secuenciales puede ser *significativamente* más rápido que los accesos aleatorios (debido al aumento de la sobrecarga de fallas), pero no para un disco SSD donde este aumento no estará presente. Los detalles subyacentes necesitarán ser entendidos para tratar cada caso (por ejemplo, índices de base de datos son estructurados para reducir la sobrecarga del acceso aleatorio), la abstracción 'filtra' detalles de la implementación al desarrollador que pueda necesitar tener en cuenta.

El ejemplo anterior puede llegar a ser aún más complejo cuando _más_ abstracciones sean introducidas. El sistema operativo Linux permite acceder a ficheros en red pero representados de forma local como ficheros 'normales'. Esta abstracción 'filtrará' si hay errores de red. Si un desarrollador trata estos ficheros como 'normales', sin considerar el hecho de que puedan estar sujetos a latencia de red y fallos, las soluciones serán defectuosas.

El artículo que describe esta ley sugiere que una dependenica excesiva de abstracciones, combinada con un entendimiento deficiente del proceso subyacente, en realidad hace que tratar con el problema sea _más_ complejo en algunos casos.

Vea también:

- [Ley de Hyrum](#ley-de-hyrum-la-ley-de-las-interfaces-implicitas)

Ejemplos del Mundo-Real:

- [Inicio lento en Photoshop (inglés)](https://forums.adobe.com/thread/376152) - un problema que encontré en el pasado. Photoshop podría tener un inicio lento, algunas veces tomando incluso minutos. Parece que el problema fue debido a que al inicio lee cierta información sobre la impresora por defecto. Sin embargo, si la impresora está en red, esto puede tomar mucho tiempo. La _abstracción_ de una impresora en red siendo presentada al sistema de forma similar a una impresora local causó un problema para usuarios en situaciones de conectividad de red deficiente.

### Ley de la Trivialidad

[Ley de la Trivialidad en Wikipedia (inglés)](https://en.wikipedia.org/wiki/Law_of_triviality)

Esta ley sugiere que los grupos invertirán mucho más tiempo y atención a problemas triviales y cosméticos que a problemas serios y sustanciales.

El ejemplo común y ficticio usado para ilustrarlo es que un comité aprobando planes para una planta nuclear invertirá la mayor parte del tiempo discutiendo la estructura del aparcamiento de bicicletas que diseños mucho más importantes para la planta nuclear en sí misma. Puede ser difícil hacer aportes valiosos en las discusiones sobre temas muy grandes y complejos sin un alto grado de experiencia y preparación en el tema. Sin embargo, la gente quiere ser vista contribuyendo de forma valiosa. De ahí la tendencia a enfocarse demasiado en detalles pequeños, los cuales pueden ser razonados fácilmente, pero no necesariamente de particular importancia.

El ejemplo ficticio de arriba nos lleva al uso del término 'Aparcamiento de Bicicletas' (Bike Shedding) como una expresión para el desperdicio del tiempo en detalles triviales.

### Filosofía Unix

[La Filosofía Unix en Altenwald](https://altenwald.org/2008/09/22/filosofia-unix/)

La Filosofía Unix es que los componentes de software debe ser pequeños y enfocados en hacer tan solo una cosa bien. Esto puede hacer más fácil construir sistemas a través de la composición conjunta de pequeñas, simples y bien definidas unidades mejor que usar programas grandes, complejos y multi-propósito.

Prácticas modernas como 'Arquitectura de Microservicios' pueden ser pensadas como una aplicación de esta ley, donde los servicios son pequeños, enfocados y hacen una cosa específica, permitiendo componer comportamientos más complejos compuestos de bloques de construcción simples.

### El Modelo Spotify

[El Modelo Spotify en Spotify Labs (inglés)](https://labs.spotify.com/2014/03/27/spotify-engineering-culture-part-1/)

El Modelo Spotify es un enfoque a una estructura de organización la cual ha sido popularizada por 'Spotify'. En este modelo, los equipos son organizados alrededor de características en lugar de tecnologías.

El Modelo Spotify también popularizó los conceptos de Tribus, Gremios y Capítulos, los cuales son otros componentes de su estructura de organización.

### Ley de Wadler

[Ley de Wadler en wiki.haskell.org (inglés)](https://wiki.haskell.org/Wadler's_Law)

> En cualquier diseño de lenguaje, el total de tiempo invertido en discutir una característica en su lista es proporcional a dos elevado a la potencia de su posición:
>
> 0. Semántica
> 1. Sintaxis
> 2. Sintaxis Léxica
> 3. Sintaxis Léxica de Comentarios
>
> (En pocas palabras, por cada hora invertida en semántica, 8 horas serán invertidas en la sintaxis de los comentarios).

Similar a [La Ley de la Trivialidad](#ley-de-la-trivialidad), la Ley de Walder establece que cuando un se diseña un lenguaje, la cantidad de horas invertida en las estructuras del lenguaje es desproporcionadamente alta en comparación a la importancia de estas características.

Vea también:

- [La Ley de la Trivialidad](#ley-de-la-trivialidad)

## Principios

Los Principios son generalmente más propensos a ser pautas relacionadas al diseño.

### El Principio de Dilbert

[El Principio de Dilbert en Wikipedia (inglés)](https://en.wikipedia.org/wiki/Dilbert_principle)

> Las compañías tienden sistémicamente a promocionar empleados incompetentes a dirección para eliminarlos del flujo de trabajo.
>
> _Scott Adams_

Un concepto de administración desarrollado por Scott Adams (creador de la tira cómica de Dilbert), el Principio de Dilbert está inspirado por [El Principio de Peter](#el-principio-de-peter). Bajo el Principio de Dilbert, los empleados que nunca fueron competentes son promocionados a cargos directivos para limitar el daño que pueden hacer. Adams primero explicó el principio en 1995 en un artículo del Wall Street Journal y lo expandió en su libro de negocios publicado en 1996, [The Dilbert Principle (inglés)](#lista-de-lectura).

Vea también:

- [El Principio de Peter](#el-principio-de-peter)
- [Ley de Putt](#ley-de-putt)

### El Principio de Pareto (La Regla 80/20)

[El Principio de Pareto en Wikipedia](https://es.wikipedia.org/wiki/Principio_de_Pareto)

> La mayoría de cosas en la vida no se distribuyen de forma uniforme.

El Principio de Pareto sugiere que en algunos casos, la mayoría de los resultados vienen de la minoría de entradas:

- El 80% de un cierto trozo de software puede ser escrito con el 20% del total de tiempo asignado (a la inversa, el 20% del código más difícil toma el 80% del tiempo).
- El 20% del esfuerzo produce el 80% del resultado
- El 20% del trabajo crea el 80% de los ingresos
- El 20% de los fallos causa el 80% de los problemas
- El 20% de las características se emplean 80% más que el resto

En los años 1940s el ingeniero americano-romaní Dr. Joseph Juran, quien es ampliamente reconocido por atribuírsele ser el padre del control de calidad, [comenzó a aplicar el principio de Pareto a problemas de calidad](https://es.wikipedia.org/wiki/Joseph_Juran).

Este principio es también conocido como: La Regla 80/20, La Ley de los Pocos Vitales y el Principio del Factor de Escasez.

Ejemplos del Mundo-Real:

- En 2002 Microsoft reportó que arreglando el 20% de los errores más reportados, 80% de los errores relacionados y los crashes en Windows y Office habían sido eliminados ([Referencia (en inglés)](https://www.crn.com/news/security/18821726/microsofts-ceo-80-20-rule-applies-to-bugs-not-just-features.htm)).

### El Principio de Peter

[El Principio de Peter en Wikipedia](https://es.wikipedia.org/wiki/Principio_de_Peter)

> La gente en una jerarquía tiende a ascender hasta su "nivel de incompetencia".
>
> _Laurence J. Peter_

Un concepto de administración de Laurence J. Peter, el Principio de Peter observa que la gente que es buena en sus trabajos es promocionada hasta llegar a un nivel donde ya no son tan exitosos (su "nivel de incompetencia"). En este punto, como ellos son más _senior_, son menos propensos a ser eliminados de la organización (a menos que su rendimiento sea espectacularmente malo) y continuarán en un rol en el que tienen pocas habilidades intrínsecas. Las habilidades que les hicieron exitosos no son necesariamente las habilidades requeridas para sus nuevos puestos.

Este es de particular interés para los ingenieros - quienes inicialmente comienzan en roles profundamente técnicos, pero a veces tienen una carrera la cual les guía a _administrar_ a otros ingenieros - los cuales requieren un conjunto fundamentalmente diferente de habilidades.

Vea también:

- [El Principio de Dilbert](#el-principio-de-dilbert)
- [La Ley de Putt](#ley-de-putt)

### El Principio de Robustez (Ley de Postel)

[El Principio de Robustez en Wikipedia (inglés)](https://en.wikipedia.org/wiki/Robustness_principle)

> Sé conservador en lo que haces y liberal con lo que recibes de otros.

A veces aplicado en desarrollo de aplicaciones de servidor, este principio establece que lo que tú envias a otros debe ser tan mínimo y consensuado como sea posible, pero lo que deberías tener como objetivo es permitir la entrada no consensuada si es que puede ser procesada.

El objetivo de este principio es construir sistemas los cuales sean robustos, tanto que puedan manejar entradas algo deficientes si aún pueden ser entendidas. Sin embargo, hay potenciales implicaciones de seguridad acerca de aceptar entradas mal formadas, particularmente si el procesamiento de tales entradas no ha sido bien testeado.

### SOLID

Este es un acrónimo el cual se refiere a:

* S: [El Principio de Responsabilidad Única](#principio-de-responsabilidad-unica) (S por _Single Responsability_ del inglés)
* O: [El Principio Abierto/Cerrado](#principio-abierto-cerrado) (O por _Open/Close_)
* L: [El Principio de Sustitución de Liskov](#principio-de-sustitucion-de-liskov) (L por _Liskov_)
* I: [El Principio de Segregación de Interfaces](#principio-de-segregacion-de-interfaces) (I por _Interfaces Segregation_)
* D: [El Principio de Inversión de Dependencia](#principio-de-inversion-de-dependencia)

Estos son los principios clave en la [Programación Orientada a Objetos](#por-hacer). Los principios de diseño tales como estos deben servir de ayuda a desarrolladores para construir sistemas más mantenibles.

### Principio de Responsabilidad Única

[El Principio de Responsabilidad Única en Wikipedia](https://es.wikipedia.org/wiki/Principio_de_responsabilidad_%C3%BAnica)

> Cada módulo o clase debe tener una tan solo una única responsabilidad.

El primero de los principios '[SOLID](#solid)'. Este principio sugiere que los módulos o clases deben hacer una única cosa y solo una. En términos más prácticos, esto quire decir que una único, pequeño cambio a una característica de un programa debe requerir un cambio en un solo componente. Por ejemplo, cambiar como una contraseña es validada por complejidad debe requerir un cambio en solo una parte del programa.

Teóricamente, esto debe hacer el código más robusto (sólido) y fácil de cambiar. Sabiendo que un componente el cual está siendo modificado tiene una única responsabilidad sólo significa que _comprobar_ ese cambio dede ser más fácil. Usando el ejemplo anterior, cambiar el componente de complejidad de la contraseña debe solo afectar a las características relacionadas con la complejidad de la contraseña. Puede ser mucho más difícil tener en cuenta el impacto de un cambio en un componente el cual tiene muchas responsabilidades.

Vea también:

- [Programación Orientada a Objetos](#por-hacer)
- [SOLID](#solid)

### Principio de Abierto/Cerrado

[Principio de Abierto/Cerrado](https://es.wikipedia.org/wiki/Principio_de_abierto/cerrado)

> Las entidades deben estar abiertas para ser extendidas y cerradas para ser modificadas.

El segundo de los principios '[SOLID](#solid). Este principio establece que las entidades (las cuales pueden ser clases, módulos, funciones u otras similares) deben tener la capacidad para ser _extendidas_ (ampliadas), pero de la misma forma debe _existir_ en su comportamiento la capacidad de no ser modificadas.

Como un ejemplo hipotético, imagina un módulo el cual es capaz de convertir un documento Markdown en uno HTML. Si el módulo puede ser ampliado para manejar nuevas características de Markdown, sin modificar el funcionamiento interno del módulo, entonces podemos decir que está abierto para ser ampliado para su extensión. Si el módulo _no_ pudiera ser modificado por un consumidor de manera que se manejen las características existentes de Markdown, entonces se_cierra_ para su modificación.

Este principio tiene una relevancia particular para la programación orientada a objetos, donde el diseño de objetos puede ser extendido (a través de la herencia), pero evitaríamos diseñar objetos los cuales puedan cambiar su comportamiento existente de formas inesperadas.

Vea también:

- [Programación Orientada a Objetos](#por-hacer)
- [SOLID](#solid)

### Principio de Sustitución de Liskov

[El Principio de Sustitución de Liskov en Wikipedia](https://es.wikipedia.org/wiki/Principio_de_sustituci%C3%B3n_de_Liskov)

> Debe ser posible reemplazar un tipo con un subtipo, sin romper el sistema.

El tercero de los principios '[SOLID](#solid)'. Este principio establece que si un componente se basa en un tipo, entonces debe ser capaz de usar subtipos de ese tipo, sin que el sistema falle o tenga constancia de los detalles de que es un subtipo.

Como un ejemplo, imagina que tenemos un método el cual lee un documento XML desde una estructura la cual representa un fichero. Si el método usa un tipo base 'fichero', entonces cualquiera que derive de 'fichero' debe ser capaz de ser usado en la función. Si 'fichero' soporta la búsqueda inversa, y el parseador de XML usa esa función, y entonces el tipo derivado 'fichero de red' falla cuando intenta una búsqueda inversa, el tipo derivado 'fichero de red' violaría el principio.

Este principio tiene particular relevancia en programación orientada a objetos, donde la jerarquía de tipos debe ser modelada con cuidado para evitar confundir a los usuarios de un sistema.

Vea también:

- [Programación Orientada a Objetos](#por-hacer)
- [SOLID](#solid)

### Principio de Segregación de Interfaces

[El Principio de la Segregación de Interfaces en Wikipedia](https://es.wikipedia.org/wiki/Principio_de_segregaci%C3%B3n_de_la_interfaz)

> Ningún cliente debe ser forzado a depender de métodos que no use.

El cuarto de los principios de '[SOLID](#solid)'. Este principio establece que los consumidores de un componente no deben depender en funciones de ese componente que no estén empleando.

Como un ejemplo, imagina que tenemos un método el cual lee un documento XML de una estructura la cual representa un fichero. Este solo necesita leer bytes, moverse adelante y atrás en el fichero. Si este método necesita ser actualizado porque una característica no relacionada al fichero cambia (tal como una actualización al modelo de permisos usado para representar la seguridad del fichero), entonces el principio queda invalidado. Sería mejor para el fichero implementar una interfaz 'flujo-con-búsqueda' y emplearla para el lector XML.

El principio tiene particular relevancia en programación orientada a objetos, donde las interfaces, jerarquías y abstracciones de tipos son usados para [minimizar el acoplamiento](#por-hacer) entre los diferentes componentes. [La tipificación dinámica](#por-hacer) (más conocida como _Duck typing_ en inglés) es una metodología que fuerza este principio eliminando las interfaces explícitas.

Vea también:

- [Programación Orientada a Objetos](#por-hacer)
- [SOLID](#solid)
- [Tipificación dinámica](#por-hacer) (_Duck typing_)
- [Desacoplado](#por-hacer)

### Principio de Inversión de Dependencia

[El Principio de Inversión de Dependencia en Wikipedia (inglés)](https://en.wikipedia.org/wiki/Dependency_inversion_principle)

> Módulos de alto-nivel no deben depender en implementaciones de bajo nivel.

El quinto de los principios '[SOLID](#solid)'. Este principio establece que la orquestación de componentes del más alto nivel deben no tener conocimiento de los detalles de sus dependencias.

Como un ejemplo, imagina que tenemos un programa que lee metadatos de un sitio web. Asumimos que el componente principal pueda tener que saber acerca de un componente de descarga del contenido de la página web y luego un componente que pueda leer los metadatos. Si tenemos la inversión de dependenicas en mente, el componente principal dependerá solo de un componente abstracto el cual obtendrá los bytes de datos y luego un componente abstracto que será capaz de leer los metadatos del flujo de bytes. El componente principal no sabrá nada acerca de TCP/IP, HTTP, HTML, etc.

Este principio es complejo, puede ser visto como 'inverso' a las dependencias esperadas de un sistema (de ahí el nombre). En la práctica, esto también significa que se separa la orquestación de un componente y debe asegurarse la implementación correcta de los tipos abstractos que son empleados (e.g. en el ejemplo anterior, _algo_ debe aún proporcionar el componente de lectura de los metadatos un descargador de ficheros HTTP y un lector de etiquetas meta de HTML). Este entonces toca patrones tales como [Inversión de Control](#por-hacer) y [Inyección de Dependencias](#por-hacer).

Vea también:

- [Programación Orientada a Objetos](#por-hacer)
- [SOLID](#solid)
- [Inversión de Control](#por-hacer)
- [Inyección de Dependencias](#por-hacer)

### Principio DRY

[El Principio DRY en Wikipedia](https://es.wikipedia.org/wiki/No_te_repitas)

> Cada pieza de conocimiento debe tener una representación única, no ambigua y autoritaria dentro de un sistema.

DRY es el acrónimo en inglés para _Don't Repeat Yourself_ (No te repitas). Este principio se enfoca en ayudar a los desarrolladores a reducir las repeticiones de código y mantener la información en un único lugar y fue citado en 1999 por Andrew Hunt y Dave Thomas en el libro [The Pragmatic Developer](https://en.wikipedia.org/wiki/The_Pragmatic_Programmer) (El Desarrollador Pragmático).

> Lo contrario a DRY sería _WET_ (Write Everthing Twice, escribe todo dos veces o We Enjoy Typing, disfrutamos escribiendo)

En la práctica, si tienes el mismo trozo de información en dos (o más) sitios diferentes, puedes usar DRY para mezclarlo en uno solo y reusarlo en cualquier lugar que lo quieras/necesites.

Vea también:

- [The Pragmatic Developer](https://en.wikipedia.org/wiki/The_Pragmatic_Programmer)

### Principio KISS

[KISS en Wikipedia](https://es.wikipedia.org/wiki/Principio_KISS)

> Keep it simple, stupid (Mantenlo simple, estúpido)

El principio KISS establece que la mayoría de los sistemas funcionan mejor si se mantienen simples en lugar de complejos; por lo tanto, simplicidad debe ser el objetivo clave en el diseño y la complejidad innecesaria debe ser evitada. Originado en las fuerzas armadas de los Estados Unidos (U.S. Navy) en 1960, la frase ha sido asociada con la ingeniera aérea Kelly Johnson.

El principio es mejor ejemplificado por la historia de Johnson manejando un equipo de ingenieros de diseño de herramientas, con el desafío del jet aircraft ellos debían diseñar sobretodo que fuese reparable por un mecánico medio en el campo y en condiciones de combate con solo esas herramientas. De aquí el "estúpido" refiriéndose a la relación entre la forma en que las cosas se rompen y la sofisticación de las herramientas disponibles para repararlas, no las capacidades de los ingenieros en sí mismos.

Vea también:

- [Ley de Gall](#ley-de-gall)

### YAGNI

[YAGNI en Wikipedia](https://es.wikipedia.org/wiki/YAGNI)

Este es un acrónimo para (en inglés) _**Y**ou **A**ren't **G**onna **N**eed **I**t_ o _No vas a necesitarlo_.

> Siempre implementar cosas cuando vayas a necesitarlas realmente, nunca cuando preveas que las necesitarás.
>
> ([Ron Jeffries](https://twitter.com/RonJeffries)) (XP co-fundador y autor del libro "Extreme Programming Installed")

Este principio de _Extreme Programming_ (XP) sugiere a los desarrolladores que deben solo implementar funcionalidad que es necesaria para los requisitos inmediatos y evitar los intentos de predecir el futuro implementando funcionalidades que podrían necesitarse luego.

Adherirse a este principio debe reducir la cantidad de código sin usar en la base de código y evitar tiempo y esfuerzo de ser malgastado en funcionalidades que no aportan valor.

Vea también:

- [Lista de lectura: Extreme Programming Installed](#lista-de-lectura)


## Lista de Lectura

Si has encontrado estos conceptos interesantes, puede que disfrutes estos libros:

- [Extreme Programming Installed - Ron Jeffries, Ann Anderson, Chet Hendrikson](https://www.goodreads.com/en/book/show/67834) - Covers the core principles of Extreme Programming.
- [El Mítico Hombre Mes](https://es.wikipedia.org/wiki/El_M%C3%ADtico_Hombre-Mes) - [The Mythical Man Month - Frederick P. Brooks Jr.](https://www.goodreads.com/book/show/13629.The_Mythical_Man_Month) - A classic volume on software engineering. [Brooks' Law](#brooks-law) is a central theme of the book.
- [Gödel, Escher, Bach: An Eternal Golden Braid - Douglas R. Hofstadter.](https://www.goodreads.com/book/show/24113.G_del_Escher_Bach) - This book is difficult to classify. [Hofstadter's Law](#hofstadters-law) is from the book.
- [The Dilbert Principle - Adam Scott](https://www.goodreads.com/book/show/85574.The_Dilbert_Principle) - A comic look at corporate America, from the author who created the [Dilbert Principle](#the-dilbert-principl).
- [The Peter Principle - Lawrence J. Peter](https://www.goodreads.com/book/show/890728.The_Peter_Principle) - Another comic look at the challenges of larger organisations and people management, the source of [The Peter Principle](#the-peter-principle).

## Por Hacer

¡Hola! Si llegaste aquí es porque hiciste clic en un enlace a un tema que aún no ha sido escrito, perdón por eso, ¡este es aún un trabajo en proceso!

Sé libre de [Abrir un _Issue_](https://github.com/manuel-rubio/hacker-laws/issues) para solicitar más detalles, o [abre una petición de cambio (_pull request_)](https://github.com/manuel-rubio/hacker-laws/pulls) para enviar tus definiciones propuestas acerca del asunto.
