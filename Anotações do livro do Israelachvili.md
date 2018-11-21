Anotações do livro do Israelachvili

# Definições

**Amphiphile** Molecules such as surfactants and lipids where one part is hydrophilic (the “headgroup”) and the other is hydrophobic, usually a long hydrocarbon chain.
**Colloid** A colloid is a dispersion of particles in solution. The size of colloidal particles is in themicroscopic regime, ranging from 0.005 to 100 m m. Only one dimension of a particle needsto be in this range to qualify it as a colloidal particle—for example, a 5 nm thick lipid bilayerof macroscopic area. Particles in the size range from 1 to 100 nm are now referred to asnanoparticles, this being the range of sizes where atomic properties make the transition tomicroscopic or macroscopic properties.

# As forças entre átomos e moléculas

* Existem quatro forças distintas na natureza. Elas são: as forças *fracas* e *fortes* entre neutrons, prótons, elétrons, etc, que agem em distâncias menores que 10^-5 nm. As outras duas são as forças eletromagnéticas e interações gravitacionais, que agem entre moléculas (e partículas elementares). As forças eletromagnéticas são a origem de todas as interações intermoleculares.
* A nomenclatura de força, energia, etc deve ser bem conceituada. Por exemplo, uma ligação pode ter alta energia, mas uma força baixa é necessária para quebrá-la.
* Potenciais de interação \(w(r)\), resulta numa força \(F(r)\):
    * w(r) = -Cm_1m_2/r^n  (de forma geral: potencial w(r) = -C/r^n)
    * F(r) = -dw(r)/dr = -nCm_1m_2/r^{n+1}
    * Para forças intermoleculares, achava-se que n era entre 4 e 5. Elas deveriam ser maiores que 3 porque agiam somente em distâncias curtas. Se n é menor que 3, é necessário levar em consideração o sistema como um todo, como na força gravitacional.
    * Forças entre dipolos magnéticos ou elétricos em n=3, e estão na região entre curta e longa. A energia de interação decai como log r, que continua a crescer, mas lentamente, à medida que r atinge o infinito. Por essa razão é que vemos dipolos magnéticos se alinhando na mesma direção num material magnético.
    * Se a dimensionalidade do meio é menor, como numa superfície, o n limite entre curto e longo muda. Para bicamadas, se torna 2.
* Mie propôs uma equação geral que tem um potencial atrativo e um repulsivo.
    * w(r) = -A/r^n + B/r^m
    * Lennard Jones ocorre quando n = 6 (v.d.W) e m = 12. A=10^-77J B=10^-134J.
* Thomas Young notou que a tensão superficial e a energia coesiva ou calor latente do material U estavam relacionadas por meio do comprimento das forças intermoleculares e/ou o tamanho molecular.
    * U \approx 6 w(\sigma) / (4 \pi r^3 / 3)
    * \gamma \approx 3 w(\sigma) / 2 (\pi r^2)
    * r \approx 3 \gamma / U.
* Não há uma receita para derivar as propriedades de fases condensadas dos potenciais de pares intermoleculares.
* *Teorema de Hellman-Feynman* diz que uma vez que se conhece a distribuição das nuvens eletronicas calculada pela Eq. de Schrödinger, as forças intermoleculares podem ser calculadas com base em eletrostática clássica direta.
    * Resolver a Eq. de Schrödinger é muito difícil. Por isso, acabaram sendo criadas várias denominações de interações intermoleculares que tem a mesma origem no fundo.

## Aspectos termodinâmicos e estatísticos de forças intermoleculares

* Potencial de interação de pares, w(r), ou energia livre/disponível.
* Vários efeitos aparecem quando interações ocorrem fora do vácuo. Isso torna o problema essencialmente do tipo de interação de muitos corpos.
    * O potencial de pares inclui as interações diretas soluto-soluto, mas também mudanças nas energias de interação solvente-solvente e solvente-soluto. Dessa maneira, duas partículas que se atraem no vácuo podem se repelir caso a energia necessária para deslocar o solvente excede a energia da aproximação das moléculas.
    * Moléculas de soluto frequentemente perturbam a ordenação local ou estrutura das moléculas de solvente. Se essa energia livre associada à perturbação varia com a distância entre duas moléculas dissolvidas, há uma força de solvatação ou estrutural adicional.
    * Interações soluto-solvente podem mudar as propriedades das moléculas dissolvidas, como o momento de dipolo e carga. Logo, diferentes meios resultam em diferentes comportamentos.
    * Quando uma molécula inividual é introduzida a um meio condensado, é necessário  considerar a energia de cavidade gasta pelo meio que é utilizada para acomodar a molécula hóspede. Logo, adicionar uma molécula de soluto implica necessariamente em afetar interações solvente-solvente.
* w(r) = -C/r^n; w(r) = \infty se r < \sigma (raio das moléculas). w(\sigma) é a energia de ligação "bond energy".
* Introduzir uma molécula de soluto induz a quebra de 6 interações solvente-solvente entre 12 moléculas, num *close packing*. 
* Distribuição de Boltzmann e potencial químico:
    * X_1 = X_2 \exp \left[ -(\mu_1^i - \mu_2^i)/kT ]
* kT possui um significado bastante importante na partição de moléculas em diferentes níveis energéticos. Essa magnitude também é utilizada como indicador da força de interação. Se a força for maior que kT, ela "vencerá" o efeito oposto, que desorganiza as moléculas, o movimento térmico.
* A energia necessária para condensar moléculas em um líquido é uma relação da energia de interação (ou coesiva) e o ponto de ebulição.
    * \mu_{gas}^i + kT \log X_{gas} = \mu_{liq}^i + kT \log X_{liq}
    * Aproximando \mu_{gas}^i - \mu_{liq}^i  por -\mu_{liq}^i, temos que \mu_liq^{i} \approx 7kT.
    * \mu_liq^i \approx 7 kT_b, onde T_b é o ponto de ebulição.
    * Isso chega na regra de Trouton, que diz que o valor latente de vaporização sobre a temperatura de ebulição é constante, dando 80 J.K-1.mol-1. Isso significa que a energia por ligação é próxima de 3/2kT, e 9kT por molécula. Logo, utilizar ~3/2kT para julgar os valores de w(r) é uma boa prática, mas somente a 1atm.
    * Isso não significa que as moléculas ganham 3/2kT quando vão para a fase vapor. Essa energia cinética não desaparece no líquido ou sólido, somente fica restrita à uma região menor ao redor de um mínimo de energia potencial.
* Classificação de forças: é melhor sempre classificá-las com base na origem, não em opostos
    1. Puramente eletrostáticas, ou Coulômbicas. Entre cargas, íons, dipolos permanentes, quadrupolos, interações de polarização. Todas as interações eletrostáticas num solvente envolvem efeitos de polarização. As forças eletrostáticas entre moléculas neutras ou agregados que estão rotacionalmente livres são geralmente atrativas, e ocorrem até mesmo a 0 K.
    2. Origem puramente entrópica, que surgem do comportamento coletivo de moléculas em temperaturas finitas, e não podem ser descritas em termos de potenciais de pares. A pressão da equação p=nrt/v é uma força entrópica repulsiva, pois as moléculas obedecem estatística Bolztmanniana. As forças osmóticas e de flutuação térmica estão nessa categoria.
    3. Natureza mecânico quântica, que resultam em ligações covalentes, ligações químicas (incluindo forças de dispersão de van der Waals, ácido-base e interações de transferência de carga) e forças estéricas repulsivas que contrabalanceiam as forças atrativas a distâncias muito curtas, devido ao princípio de exclusão de Pauli.
    * As forças de interação de v.d.W. não podem ser classificadas sem ambiguidade.
    * As forças eletrostáticas num meio não podem ser calculadas simplesmente dividindo a força no vácuo pela constante dielétrica. Tem que considerar forças entrópicas tb.

Tipos de interação e os potenciais:
+----------------------------+-------------------------------------------------------------------+
| carga-carga                | +q_1q_2/4 \pi \varepsilon_0 r                                     |
| carga-dipolo               | -Qu \cos \theta / 4 \pi \varepsilon_o r^2                         |
| carga-dipolo livre         | -Q^2u^2/6 (4 \pi \varepsilon_0)^2 kTr^4                           |
| dipolo-dipolo livres       | -u_1^2u_2^2 / 3 (4 \pi \varepsilon_0)^2 kTr^6 (energia de Keesom) |
| Carga-não polar            | -Q^2\alpha / 2 (4 \pi \varepsilon_0)^2 r^4                        |
| Dipolo-não polar livre     | -u^2 \alpha (4 \pi \varepsilon_0)^2 r^6 (energia de Debye)        |
| Duas moléculas não polares | -3/4 h\nu\alpha^2 / (4 \pi \varepsilon_0)^2 r^6                   |
| Ligação de hidrogênio      | Complicada, -1/r^2                                                |
+----------------------------+-------------------------------------------------------------------+

* Uma das grandes dificuldades de se estabelecer potenciais de pares em sistemas multicomponentes e multimoleculares é como lidar com o meio suspenso sem tratá-lo como um contínuo sem estruturação, definido somente por suas propriedades do bulk, como densidade, ou constante dielétrica.
    * É possível atacar isso partindo do contínuo para o meio molecular, assumindo que algumas propriedades se mantém mesmo em dimensões moleculares.
    * É possível começando pelas interações ocorrendo em níveis atômicos e moleculares e depois tentando construir as propriedades do sistema.

## Forças intermoleculares fortes: Interações covalentes e coulombicas

* Ligações covalentes ligam moléculas e cristais, e geralmente não é possível derreter sem quebrar essas ligações, então tendem a vaporizar, decompor ou reagir com a temperatura.
* Ligações físicas não tem a especificidade, estequiometria e direcionalidade das ligações covalentes, então são bons candidatos para ligar moléculas em líquidos, já que as moléculas conseguem mover e rodar mas ainda permanecerem ligadas uma à outra. As ligações físicas podem ser tão fortes quanto as quimicas, e até as forças mais fracas são capazes de juntar átomos e moléculas em sólidos e líquidos, em agregados coloidais e biológicos.
* O campo elétrico a uma distância r de uma carga q_1 é dada por
    * E_1 = \dfrac{Q_1}{4\pi\varepsilon_o\varepsilon r^2}
* A força é dada por F(r) = Q_2 E_1
* A energia livre de interação Coulombica é dada por:
    * w(r) = \int_\infty^r -F(r)dr = z_1z_2e^2 / 4\pi\varepsilon_0\varepsilon r (traz elas do infinito para perto, pois no infinito não tem interação)
* A permissividade dielétrica é função da frequência, então deveria ser escrita como \varepsilon(\nu). Em frequência zero (condições estáticas), ela se chama constante dielétrica e é denominada \varepsilon(0) ou simplesmente \varepsilon.

# Interações envolvendo moléculas polares (4)

* A maioria das moléculas não possuem carga total, mas possuem um dipolo elétrico.
* Momento de dipolo u = ql, onde q é a carga e l é a distância entre as cargas + e -. A unidade é o Debye, D, 1D = 3.336 x 10^-30 C.m.
* Em água, a energia de interação diminui por um fator de 80, mas mesmo assim é bastante grande para íons pequenos que pode exceder kT.
* Para uma molécula de água alinhada (a = 0.14nm, u=1.85D, \theta=0), e um íon de Na+ (z = 1, a = 0.095), a energia de interação (máxima) é: 
    * w(r, \theta = 0) = - (1.602x10^-19) * (1.85 x 3.336 x 10^-30) / 4 * \pi * (8.854 x 10^-12)(0.235x10^-9) ^2 = 1.6x10^-19J = 39kT \approx 96kJ.mol-1.
* As forças atrativas fortes entre íons e água é responsável para promover a nucleação de gotas de chuva ao redor de íons que são liberados após um raio em uma nuvem. Em outros tipos de nuvens, a nucleação da água ocorre ao redor de partículas sem carga, moléculas ou grupos moleculares que possuem, de qualquer forma, uma forte afinidade pela água.
* A energia livre de interação de um íon em água não se deve somente ao processo de levar uma molécula de água de longe do íon para perto, porque isso não resultaria numa alteração do sistema. O que acontece é que as moléculas de água tem dipolos. Longe, os dipolos estão totalmente aleatórios, mas perto, elas se orientam, e isso é a origem dessa energia.
* O número de hidratação é o número de moléculas de água presas por eles, que não estão totalmente imobilizadas mas trocam com o solvente, porém mais lentamente. Íons menores geram um campo mais forte, que faz com que mais moléculas de água se coordenem. Isso faz com que seus raios hidrodinâmicos sejam maiores.
* O tempo de correlação rotacional de moléculas de água livre é de cerca de 10^-11s. Perto de íons, esses tempos podem variar de 10^-11s até vários horas. Para íons fracamente solvatados (como trimetilamônio), esses tempos são próximos da água, mas podem ser até mais curtos (hidratação negativa). Quando esses tempos ficam bastante curtos (Cr3+ é de segundos a horas), acabam gerando complexos de coordenação de estequimetria fixa.
* Alguns tipos de interação podem levar a uma modificação da ordenação molecular ao redor das moléculas de soluto e superfícies, cujos efeitos decaem exponencialmente com a distância, até alguns diâmetros moleculares. Essa região de estrutura diferenciada é a zona de solvatação, onde as propriedades do solvente são significativamente diferentes às do bulk.
* Moléculas dipolares frequentemente não são esféricas, mas possuem alguma assimetria, então a melhor conformação para elas, ao invés de alinhadas, é paralelas.
* O tamanho pequeno do átomo de H depletado de elétrons na molécula de água permite que outros átomos eletronegativos se aproximem bastante e experienciar um campo particularmente forte. A ligação resultante é uma ligação de hidrogênio, que é moderadamente direcional e fortemente atrativa. Esse tipo de ligação nada mais é do que um tipo bastante forte de interação dipolo-dipolo direcional.
* A energia livre de interação é menor do que a energia interna total de dois dipolos interagindo, porque um pouco de energia é gasta alinhando os dois dipolo na medida em que se aproximam.
* A contribuição entrópica da orientação de moléculas de água ao redor de íons é negativa (-1.36 a 25°C), o que significa que a solvatação de íons é acompanhada por uma diminuição na entropia, o que indica que as moléculas de água se tornam restritas rotacional e translacionalmente. Por outro lado, quando dois íons de cargas opostas se aproximam, a entropia aumenta, porque ocorre a liberação de íons.

## Interações envolvendo a polarização de moléculas

* A constante dielétrica de um meio é consequência da maneiras que as moléculas são polarizadas pelo campo elétrico.
* Todos os átomos e moléculas são polarizáveis. A *polarizabilidade* (dipolo) \alpha é definida de acordo com a força do momento de dipolo induzido u_ind que adquirem em um campo E,
    * u_ind = \alpha E
* Para uma molécula não polar, a polarizabilidade surge do deslocamento de sua nuvem eletrônica negativamente carregada em relação ao seu núcleo positivamente carregado por influência de um campo elétrico externo.
* A polarizabilidade pode ser calculada pela soma das polarizabilidades individuais das ligações e átomos, com bastante precisão. Falha para moléculas com delocalização eletrônica.
* Um dipolo induzido aparece como reação a um campo inicial, que pode tanto aumentar ou diminuir a força desse campo, dependendo da localização. Num meio condensado, esses pequenos dipolos são somados, resultando num campo de resposta, E_r, que sempre se opõe ao campo inicial E. Logo, há sempre dois campos, E, dentro e fora, e E_r, só dentro, que depende das moléculas do meio.
* Logo, a força eletrostática resultante é resultado da interação das cargas com esses dois campos, que resulta num campo efetivo E_eff. Quanto a polarização é alta, E_eff \to 0, então as forças eletrostáticas diminuem bastante de intensidade.
* Também faz sentido que a polarização depende da polarizabilidade das moléculas. Quanto maior é \alpha, maior seria o campo, maior \varepsilon. Porém, em meios condensados há fatores adicionais que contribuem para a polarização, além da polarização discreta e não cooperativa. Numa fase condensada, as cargas podem ser deslocadas (polarizadas) por distâncias significativamente mais longas que os tamanhos das moléculas. Por exemplo, através de elétrons ou prótons pulando por redes de ligações de hidrogênio, como ocorre na água.
* Sobre moléculas
 num meio, suas interações se devem a polarizabilidades de excesso, isso é, propriedades que elas tem de diferente do meio. Caso o soluto fosse igual ao solvente, não haveria interação, elas seriam indistinguíveis. Uma maneira de se tratar isso é considerar a molécula de soluto como sendo uma região de polarizabilidade diferente.
* Equação geral do potencial de interação, considerando carga, polarizabilidade, etc
    * w(r)= - \left[ \frac{Q_{1}^{2}}{8\pi\varepsilon_{0}\varepsilonr^{4}} + \frac{3kT}{r^{6}} \left(\frac{\varepsilon_{1}-\varepsilon}{\varepsilon_{1}+2\varepsilon}\right) a_{1}^{3} \right] \left(  \frac{\varepsilon_{2}-\varepsilon}{\varepsilon_{2}+2\varepsilon}  \right)a_{2}^{3}
    * A força de interação entre moléculas dissolvidas ou partículas pequenas pode ser zero, atrativa ou repulsiva, dependendo das magnitudes de \varepsilon_1, \varepsilon_2, \varepsilon.
    * Íons serão atraídos para moléculas dissolvidas com alta constante dielétrica (moléculas altamente polares), mas repelidas de moléculas com baixa constante dielétrica.
    * A interação entre duas moléculas idênticas sem carga é sempre atrativa independente da natureza do meio de suspensão. Interessantemente, duas bolhas de ar se atraem num líquido.
* A força de atração dipolar efetiva é dependente não do momento de dipolo, u, mas do momento de dipolo por unidade de volume.

## Forças de van der Waals: a força dispersiva

* As forças de dispersão existem em todas as moléculas e átomos. O nome vem da dispersão da luz nas regiões do visívle e UV.
* Das 3 partes que compõem as forças de v.d.W agem em adesão, tensão superficial, adsorção física, molhamento, propriedades de gases, líquidos e filmes fil,es nas forças de sólidos, floculação de partículas em líquidos, estruturas de moléculas condensadas como proteínas e polímeros.
* Características:
    1. Longa distância, e podem ser efetivas de > 10nm até pouco, 0.2nm.
    2. Essas forças podem ser repulsivas ou atrativas, e de forma geral a força dispersiva entre duas moléculas não segue uma lei de potência.
    3. Não só as forças dispersivas tendem a juntar moléculas, mas também as alinha e orienta, apesar de que o efeito orientador ser mais fraco do que em interações dipolares.
    4. As forças dispersivas não são aditivas. A força entre dois corpos é afetado pela presença de outros corpos na proximidade.
* A origem dessas forças é mecanico-quântica, tratamento mais rigoroso seria na eletrodinâmica quântica. Porém, a interação é essencialmente eletrostática.
* Para um átomo não polar, o momento de dipolo médio temporal é zero, mas para qualquer instante os elétrons estão em posições específicas e portanto existe um momento de dipolo. Esse momento de dipolo gera um campo elétrico que polariza qualquer átomo neutro próximo, induzindo um dipolo, que gera uma atração entre esses átomos. A média temporal dessa atração é finita.
* O momento de dipolo instantÂneo em um átomo de hidrogênio de Bohr é da ordem de a_0e \approx 2.5D, que não é pequena.
* A força dispersiva depende, como a dipolar, em polarizabilidade total por volume, (\alpha/\sigma^3)^2. Porém, esse fator é praticamente constante, então à medida que uma molécula se torna maior, a contribuição dispersiva se torna mais importante do que a dipolar.
* Equação das forças de van der waals:
   * w_{\mathrm{VDW}}(r) = -C_{\mathrm{VDW}}/r^{6} = 
   -\left[C_{\mathrm{ind}}+C_{\mathrm{orient}}+C_{\mathrm{disp}}\right]/r^{6}
   * w_{\mathrm{VDW}}(r) = - \left[ \left( u_{1}^{2}\alpha_{02} + u_{2}^{2}\alpha_{01} \right)   + \frac{u_{1}^{2}u_{2}^{2}}{3kT} + \frac{3\alpha_{01}\alpha_{02}h\nu_{1}\nu_{2}}{2\left(\nu_{1} + \nu_{2}\right)}\right]/\left(4\pi\varepsilon_{0}\right)^{2}r^{6}
* Propriedades das interações de v.d.W:
    1. Dominância das forças de dispersão. Exceto para moléculas fortemente polares, as forças de dispersão geralmente excedem as forças de indução e orientação dependentes de dipolos.
    2. Há uma notável similaridade dos valores teóricos e os experimentais.
    3. O coeficiente C_VDW entre duas moléculas dissimilares A e B é geralmente a média geométrica dos coeficientes A-A e B-B. Para moléculas fortemente polares, como água, isso quebra.
* A teoria de London possui duas falhas notáveis. Ela assume que os átomos e moléculas possuem somente um potencial de ionização (uma frequência de absorção), e ela não consegue lidar com interações das moléculas num solvente. MacLachlan propôs uma expressão que consegue lidar com moléculas 1 e 2 num meio 3, através de uma série.
* A energia livre de interação de v.d.w. para duas moléculas idênticas 1 num meio 3 é dado por:
    * w ( r ) = w ( r ) _ { \nu = 0 } + w ( r ) _ { \nu > 0 } \approx - \left[ 3 k T \left( \frac { \varepsilon _ { 1 } ( 0 ) - \varepsilon _ { 3 } ( 0 ) } { \varepsilon _ { 1 } ( 0 ) + 2 \varepsilon _ { 3 } ( 0 ) } \right) ^ { 2 } + \frac { \sqrt { 3 } h \nu _ { e } } { 4 } \frac { \left( n _ { 1 } ^ { 2 } - n _ { 3 } ^ { 2 } \right) ^ { 2 } } { \left( n _ { 1 } ^ { 2 } + 2 n _ { 3 } ^ { 2 } \right) ^ { 3 / 2 } } \right] \frac { a _ { 1 } ^ { 6 } } { r ^ { 6 } }
* Conclusões dessa equação:
    * Como h\nu_e \gg kT, a contribuição da dispersão em frequência > 0 é geralmente, mas nem sempre, do que a contribuição dipolar \nu=0.
    * A força de v.d.W é muito reduzida num meio com solvente
    * A força de v.d.w. é relativamente parecida com o resultado de London, para a parte com \nu>0. Dá pra fazer o resultado ser igual, só precisa usar as relações de Clausius-Mossoti-Lorenz-Lorentz.
    * A força dispersiva entre moléculas similares é sempre atrativa, e para moléculas dissimilares, pode ser tanto atrativa como repulsiva. Isso ocorre quando n_3 possui um valor entre n_1 e n_2. Entre moléculas identicas, é sempre atrativa. Quanto menor for a diferença n_1 - n_3, menor é a atração entre as moléculas. O termo real é (n_1^2 - n_3^2)^2, que pode ser escrito como \left[ \sqrt { \left( n _ { 1 } ^ { 2 } - 1 \right) ^ { 2 } } - \sqrt { \left( n _ { 3 } ^ { 2 } - 1 \right) ^ { 2 } } \right] ^ { 2 }, que no final vira:
        * w(\sigma) \propto \propto \left[ \sqrt { U _ { 1 } } - \sqrt { U _ { 3 } } \right] ^ { 2 }, que é justamente o parâmetro de Hildebrand. Quando as diferenças nos índices de refração forem muito grandes, as moléculas vão tender a separar de fase. Isso não funciona quando há outros fatores adicionais, como o efeito hidrofóbico.
    * Em alguns casos, a força dispersiva entre duas moléculas num solvente é bastante pequena, e nesse caso a contribuição de frequência zero domina. Isso acontece quando hidrocarbonetos pequenos ou fluorocarbonetos interagem com água. A equação acaba se reduzindo a algo puramente entrópico. A atração de hidrocarbonetos em água nesses caso resulta num aumento da entropia (devido às moléculas de água).
* A polarizabilidade paralela e perpendicular são diferentes, e uma consequência disso é que existe uma anisotropia das forças de dispersão, então elas acabam sendo dependentes da orientação das moléculas. Em fases líquidas isso geralmente não importa porque elas estão rotacionando muito, mas em fases mais rígidas, como cristais líquidos, o efeito aparece.
* A não additividade das forças de van der Waals significa que para saber a energia de interação de uma molécula com outras, não basta somar todos os potenciais das moléculas individuais. Isso ocorre porque o campo emanando de uma molécula atinge uma segunda molécula diretamente, mas também por "reflexão" por outras moléculas, que foram polarizadas e acabam polarizando também. Isso depende das posições, pode ser negativo ou positivo, então o efeito total é geralmente pequeno quando se trata de moléculas, mas se torna importante quando se fala sobre um meio.
* A força de interação demora um tempo para percorrer o espaço, então é possível que uma molécula perca a conformação ideal no tempo que o campo elétrico demora para chegar. Isso aumenta o fator de distância, de -1/r^6 para -1/r^7. Isso é chamado de efeito de retardação. Se torna importante quando há corpos macroscópidos ou superfícies interagindo num meio líquido.

## Forças estéricas repulsivas, potenciais de par intermolecular total, estrutura líquida

* Em sólidos a 0K, a posição dos átomos na redondeza é bem definida. Quando a temperatura aumenta, essas posições se tornam menos definidas, começa a aparecer uma distribuição de posições. Em líquidos, essa distribuição está muito larga, e geralmente oscila gradativamente até atingir o valor do bulk. As propriedades de um líquido perto de uma interface não são as mesmas de um contínuo sem estruturação do bulk.

## Interações especiais: ligações de hidrogenio, interações hidrofílicas e hidrofóbicas

* As duas interações especiais da água são: *ligação de hidrogênio* e *efeito hidrofóbico*.
* A cte dielétrica da maior parte das moléculas diminui quando ela se solidifica. Já a água é o contrário, fica maior quando vira gelo. A condutividade protônica é maior em gelo do que no líquido, possivelmente pelo mecanismo de "proton hopping".
* A distância O-H é de 0.10 nm, e a distância intermolecular O...H é de 0.176 nm, menor do que o raio de 0.26 nm, obtido pela soma dos raios de v.d.W. Isso indicaria que há uma contribuição covalente à ligação de hidrogênio. Porém, as contribuições mais recentes falam que é uma interação predominantemente eletrostática (Coulombica). Com raras exceções, o átomo de hidrogênio não é dividido, e se manter mais perto e covalentemente ligado ao átomo pai. Não há uma equação de energia livre, mas a tendência é uma queda em 1/r^2.
* O valor da força da ligação de hidrogênio é de 10-40 kJ.mol-1, 5-10kT a 298K.
* Muitos modelos já foram propostos para descrever a distribuição de carga dentro da molécula de água, mas nenhum consegue prever corretamente todas as propriedades em todas as fases. Geralmente a molécula de água é representada como centrada no oxigênio, duas cargas positivas nos H e duas negativas nos pares eletrônicos.
* Em gelo, há uma média de 4 moléculas de água ao redor de uma, formando uma rede de tetraedros com O nos vértices e as linhas possuem um H no meio. O-H...O. Na água, esse número cai para 3.5, e os tempos de vida são de cerca de 10^-11s.
* A formação de uma rede de ligações de hidrogênio causa a tendência na formação de mais ligações de hidrogênio. Uma possível explicação para isso é a maior entropia dada ao sistema pela facilidade da movimentação de prótons.
* Apenas moléculas com 4 ou mais ligações podem formar estruturas tridimensionais, 3 ligações geram somente estruturas 2D.
* A forte inclinação da água em fazer ligações de hidrogênio influencia sua capacidade de interagir com moléculas incapazes de fazer lig. de H. Quando entram em contato com essas moléculas, não importa que direção as molécula de água se direcione, uma ou mais das quatro cargas vai ter que apontar para o soluto inerte.
    * Para fazer isso, elas se organizam ao redor desses solutos. Se a molécula for pequena, as moléculas de água conseguem se arranjar ao redor do soluto sem perder ligações.
    * Em superfícies, as moléculas de água se ordenam paralelamente, e a parte com o oxigênio, maior, aponta para a superfície com maior frequência. As moléculas vizinhas tem que se ordenar para conseguir fazer essas ligações. O resultante é um potencial negativo de -15 a -40 mV em interfaces água-ar e hidrocarboneto-água. pag 159
    * Estudos teóricos e experimentais dizem que a estruturação de água ao redor de solutos hidrofóbicos ou superfícies é bastante entropicamente desfavorável, já que rompe a estrutura existente e impõe uma nova estrutura mais ordenada às moléculas de água ao redor.
* O termo -T\DeltaS para n-butano em água é de 28.7 kJ.mol-1, e o \DeltaG_transfer é de +24.5kJ.mol-1.
* Essa energia é de cerca de 41 mJ.mol-2, próxima à energia livre interfacial de interfaces água-hidrocarboneto, da ordem de 40-50 mJ.m-2.
* A imiscibilidade de substâncias inertes em água, e a natureza principalmente entrópica dessa incompatibilidade, é conhecido como o efeito hidrofóbico.
* Relacionado ao efeito hidrofóbico está a interação hidrofóbica, que descreve a atração inusitadamente forte entre moléculas hidrofóbicas e superfícies em água, frequentemente muito mais fortes do que no espaço livre. Isso ocorre pelo rearranjo das moléculas de água quando as duas espécies se aproximam e as zonas de solvatação se sobrepõem.
* Medidas da força hidrofóbica mostraram que a força caía exponencialmente com a distância, com um comprimento de decaimento de 1 nm. Para moléculas com diâmetro de 0.5nm, a força da interação hidrofóbica cai para menos de kT a uma dist. de 2nm. É sete vezes maior que o comprimento dos potenciais de interação de v.d.W. para hidrocarbonetos. É importante para descrever as dinâmicas de auto-associação de moléculas anfifílicas.
    * Há ainda estudos que estão tentando entender essa força; Seria uma força estrutural (devido à estrutura da água ou uma força de depleção), atração de v.d.W. reforçada (devido a dipolos flutuantes gigantes) ou uma força capilar por "bridging" de bolhas de vapor.
* Interações hidrofílicas: quando as moléculas preferem interagir com água do que com elas mesmo. São conhecidas como higroscópicas. Grupos polar não são necessariamente hidrofílicos e grupos não-polares não são necessariamente hidrofóbicos.
* Algumas moléculas, quando dissolvidas na água, possuem um efeito drástico em outros solutos, que pode se dever à sua capacidade de alterar ou romper a estrutura da água local. Ureia pode causar o desenovelamento de proteínas. Tentaram classificar essas moléculas como "structure makers" e "structure breakers". Tais moléculas como a ureia são chamadas de "chaotropic agents" ou "chaotropes", termo cunhado como referência ao caos que essas moléculas causam ao desestruturar a água.
* Aparentemente, interações hidrofílicas e hidrofóbicas são interdepententes e não aditivas.

## Interações fora do equilíbrio e dependentes do tempo

* Transferência de energia (dissipação) durante colisões moleculares: o número de Deborah. Essa parte fala de interações, e energias que são perdidas ou armazenadas.
* Quando De = 1, ocorre o máximo de transferência de energia possível.

-------

# Forças entre partículas e superfícies

## Unificando conceitos de forças intermoleculares e interpartículas

* Sempre há uma atração efetiva entre moléculas ou partículas semelhantes numa mistura binária.
* A interação entre duas molécula de soluto A num solvente B está intimamente acoplada à força da interação solvente-solvente.
* A energia interfacial é definida positiva por convenção.
* A energia para trazer duas superfícies A em contato adesivo num meio B é o dobro da tensão interfacial entre A e B.
* Para estimar a tensão interfacial AB a partir das energias de superfície/tensões superficiais dos líquidos puros A e B, dá para estimar com:
    * \gamma _ { \mathrm { AB } } = \gamma _ { \mathrm { A } } + \gamma _ { \mathrm { B } } - 2 \sqrt { \gamma _ { \mathrm { A } } \gamma _ { \mathrm { B } } } = \left( \sqrt { \gamma _ { \mathrm { A } } } - \sqrt { \gamma _ { \mathrm { B } } } \right) ^ { 2 }
* Num meio com 3 compostos, A e B num meio C, a energia de interação pode ser tanto positiva quanto negativa.
    * Para visualizar isso, é bom considerar o princípio de Arquimedes aplicado a forças intermoleculares. No caso de forças gravitacionais, ferro afunda enquanto madeira flutua em água. Então, a madeira está sentindo efetivamente uma repulsão da terra quando está na água. Se a madeira fosse colocada no fundo, um volume igual de água seria deslocado para cima. Como água é mais densa, ela é mais atraída para a terra do que a madeira, então esse é um estado desfavorável.
    * Caso C seja intermediário, ocorrerá repulsão entre A e B. As propriedades de A e B podem ser índice de refração e cte dielétrica.
    * Com *n* partículas, podemos observar o mesmo. Há sempre uma atração efetiva entre moléculas ou partículas iguais, e pode haver atração ou repulsão entre partículas diferentes.
* Interações com interfaces podem resultar em três fenômenos:
    1. Adsorção: a partícula é atraída pela interface de qualquer um dos lados
    2. Desorção: a partícula é repelida da interface de qualquer lado
    3. *Engulfing*: A partícula é atraída de um lado mas repelida pelo outro
    * Se as propriedades da partícula C são intermediárias entre os solventes A e B, a partícula se aloja na interface. Esse é o caso de surfactantes em superfícies água-hidrocarboneto.
    * As combinações de propriedades entre A, B e C resultam em que a repulsão de C pelos dois lados da interface é impossível, e ocorre ou adsorção ou *engulfing*. Por isso que superfícies são tão passivas de adsorver moléculas ou partículas do vapor ou solução.
    * Para ocorrer engulfing, \gamma _ { \mathrm { BC } } + \gamma _ { \mathrm { AC } } > \gamma _ { \mathrm { AB } }

## Contraste entre forças intermoleculares, interpartículas e intersuperfícies

* Curtas distâncias: perto ou próximo de contato molecular (< 1 nm). Longa distância: > 100 nm (0.1\mu m)
* As propriedades de gases e forças coesivas de fases condensadas são determinadas principalmente pelas energias de interação em contato, w(\sigma).
* Já as interações de partículas e superfícies macroscópicas, as interações mais importantes são as de longo alcance.
    1. A energia total de interação é proporcional ao tamanho das partículas, >>kT mesmo a 100 nm de distância ou mais.
    2. O decaimento de energia e força é muito menor em relação à distância de separação absoluta, mas muito mais rápido quando comparado com o tamanho das partículas
    3. A cinética de interação macromolecular e interpartículas pode ser muito diferente, geralmente mais lento, que auqelas entre átomos pequenos e moléculas. De forma geral, quanto maior for a força de interação (adesão ou energia de *binding*), mais tempo o sistema demora para equilibrar. Isso é por causa dos potenciais de energia.
    * Essas características fazem as interações entre macromoléculas, nanopartículas e partículas coloidais quantitativamente e qualitativamente diferentes daquelas de moléculas pequenas.
* As interações de partículas moles são particularmente sutis devido à interdependência das forças intrapartícula e interpartícula. Os tamanhos e formatos dos agregados são regulados por interações intrapartícula de curta distância, que são sensíveis ao eletrólito, concentração, pH. Por outro lado, as interações interpartícula, de longa distância, são sensíveis às mesmas variáveis. 
* A aproximação de Derjaguin diz que a interação entre duas esferas grandes a uma boa distância pode ser aproximada pela interação de duas paredes.
    * A dependência da força entre duas superfícies curvas pode ser bastante diferente dquela entre duas superfícies planas, mesmo que o tipo de interação entre elas seja a mesma.
* Pág 219 tem uma tabela de tipos de interação, distâncias, se são atrativas ou repulsivas, muito boa.
* Forças de corpo e forças de superfície:
    * Para determinar se uma força é de corpo ou de superfície, pense no que acontece quando parte do corpo é removido. Se duas esferas interagindo por v.d.W. e vc remove o corpo delas, a interação cai, então é uma força de corpo. Se forem duas esferas carregadas e vc remove o corpo, mantendo as cargas, a interação permanece, então é uma força de superfície.

## Técnicas para medida de força

* Dados termodinâmicos e físicos de gases, líquidos e sólidos (como pontos de ebulição, viscosidade, espalhamento, diagramas de fase, solubilidade) mostram somente interações de curta distância.

## Forças de v.d.W. entre partículas e superfícies

* Assumindo que a interação é não-retardada e aditiva.
* Constante de Hamaker:
    * A = \pi^2C\rho_1\rho_2
    * C vem de: w(r) = - C/r^6, de potencial interatômico de v.d.W.
* Valores para A são da ordem de 10^-19J no vácuo.
* A constante de Hamaker para três compostos (hidrocarboneto, CCl4 e H2O) são parecidas, não por coincidencia. Isso ocorre porque o coeficinete C é aproximadamente proporcional ao quadrado da polarizabilidade \alpha, que por sua vez é proporcional ao volume v de um átomo. Como \rho \propto 1/v, A \propto C\rho^2 \propto \alpha^2\rho^2 \propto v^2/v^2 \propto constante. A cte de Hamaker para a maior parte das fases condensadas varia de 0.4-4 x 10^-19 J.
* Pág 255 tem uma tabela com as energias de interação e forças de interação expressas em função da constante de Hamaker. Tem para cilindros paralelos e perpendiculares.
* Essas equações anteriores assumem incorretamente que há aditividade. Isso não é válido, pois há reflexões múltiplas, afetando a polarização dos átomos diferentemente.
* O problema da additividade foi resolvido pela teoria de Lifshitz, onde a estrutura atômica é ignorada e as forças entre corpos grandes, agora tratadas como meios contínuas, são derivadas em termos de propriedades do bulk, como constantes dielétricas e índices de refração. As equações anteriores permanecem, muda somente o jeito que a constante de Hamaker é calculada.
* Juntando-se as equações de energia livre de interação de dipolos e cargas, e fazendo algumas considerações de simetria, é possível chegar a uma equação que relaciona a polarizabilidade de um meio dielétrico planar 2 em um meio 3 puramente por propriedades macroscópicas:
    * \rho _ { 2 } \alpha _ { 2 } = 2 \varepsilon _ { 0 } \varepsilon _ { 3 } \left( \varepsilon _ { 2 } - \varepsilon _ { 3 } \right) / \left( \varepsilon _ { 2 } + \varepsilon _ { 3 } \right)
* Usando a equação de McLachlan (que melhorava a de London, com mais termos), é possível descrever então a constante de Hamaker por meio da teoria de Lifshitz.
    * A \approx \frac { 3 } { 4 } k T \left( \frac { \varepsilon _ { 1 } - \varepsilon _ { 3 } } { \varepsilon _ { 1 } + \varepsilon _ { 3 } } \right) \left( \frac { \varepsilon _ { 2 } - \varepsilon _ { 3 } } { \varepsilon _ { 2 } + \varepsilon _ { 3 } } \right) + \frac { 3 h } { 4 \pi } \int _ { v _ { 1 } } ^ { \infty } \left( \frac { \varepsilon _ { 1 } ( i \nu ) - \varepsilon _ { 3 } ( i \nu ) } { \varepsilon _ { 1 } ( i \nu ) + \varepsilon _ { 3 } ( i \nu ) } \right) \left( \frac { \varepsilon _ { 2 } ( i \nu ) - \varepsilon _ { 3 } ( i \nu ) } { \varepsilon _ { 2 } ( i \nu ) + \varepsilon _ { 3 } ( i \nu ) } \right) \mathrm { d } \nu
    * \varepsilon(i\nu) são os valores de \varepsilon em frequências imaginárias, v _ { n } = ( 2 \pi k T / h ) n = 4 \times 10 ^ { 13 } n \mathrm { s } ^ { - 1 } a 300K.
    * O primeiro termo fornece a energia de v.d.W. de frequência zero e inclui as contribuições de Keesom e Debye, dipolares. O segundo termo fornece as energias dispersivas e incli a contribuição da energia de London.
* \nu _ { 1 } \approx 4 \times 10 ^ { 13 } \mathrm { s } ^ { - 1 } \gg \nu _ { \mathrm { rot } }
* Expressão geral da cte de Hamaker:
    * A _ { \mathrm { total } } = A _ { \nu = 0 } + A _ { \nu > 0 } \approx \frac { 3 } { 4 } k T \left( \frac { \varepsilon _ { 1 } - \varepsilon _ { 3 } } { \varepsilon _ { 1 } + \varepsilon _ { 3 } } \right) \left( \frac { \varepsilon _ { 2 } - \varepsilon _ { 3 } } { \varepsilon _ { 2 } + \varepsilon _ { 3 } } \right) + \frac { 3 h v _ { \mathrm { e } } } { 8 \sqrt { 2 } } \frac { \left( n _ { 1 } ^ { 2 } - n _ { 3 } ^ { 2 } \right) \left( n _ { 2 } ^ { 2 } - n _ { 3 } ^ { 2 } \right) } { \left( n _ { 1 } ^ { 2 } + n _ { 3 } ^ { 2 } \right) ^ { 1 / 2 } \left( n _ { 2 } ^ { 2 } + n _ { 3 } ^ { 2 } \right) ^ { 1 / 2 } \left\{ \left( n _ { 1 } ^ { 2 } + n _ { 3 } ^ { 2 } \right) ^ { 1 / 2 } + \left( n _ { 2 } ^ { 2 } + n _ { 3 } ^ { 2 } \right) ^ { 1 / 2 } \right\} }
* Para duas partículas iguais:
    * A = \frac { 3 } { 4 } k T \left( \frac { \varepsilon _ { 1 } - \varepsilon _ { 3 } } { \varepsilon _ { 1 } + \varepsilon _ { 3 } } \right) ^ { 2 } + \frac { 3 h v _ { \mathrm { e } } } { 16 \sqrt { 2 } } \frac { \left( n _ { 1 } ^ { 2 } - n _ { 3 } ^ { 2 } \right) ^ { 2 } } { \left( n _ { 1 } ^ { 2 } + n _ { 3 } ^ { 2 } \right) ^ { 3 / 2 } }
* Quatro observações podem ser notadas:
    1. As forças de v.d.W. entre dois corpos idênticos são sempre atrativas (A positivo), enquanto que para corpos diferentes podem ser atrativas ou repulsivas (A negativo)
    2. A força de v.d.W. entre dois corpos condensados no vácuo ou ar é sempre atrativa.
    3. A cte de Hamaker para dois meios similares interagindo através de outro meio permanece igual se os meios são intertrocados. Portanto, se não há outras forças operando, um filme líquido em ar sempre tenderá a ser fino pela influencia das forças atrativas de v.d.W. entre as duas superfícies ou, em outras palavras, as fases gasosas.
    4. A contribuição da energia dispersiva pode ser bastante alta quando um dos meios tem um índice de refração alto, p.e. n1 \gg n3. Porém, a contribuição entrópica de frequencia zero nunca excede 3/4kT. Para algumas interações, a contribuição de frequencia zero pode dominar sobre a contribuição dispersiva.
* A teoria de Lifshitz é uma teoria do contínuo e só pode ser usada quando as superfícies interagentes estão mais longe do que dimensões moleculares.
* A figura 13.4 mostra um gráfico da permissividade em função da frequência para a água. Mostra claramente os valores altos em freq. baixas (cte dielétrica) e valores em torno de 2 para a região do visível.
    * \varepsilon _ { \mathrm { w } } ( i \nu ) = 1 + \left( n _ { \mathrm { W } } ^ { 2 } - 1 \right) / \left( 1 + \nu ^ { 2 } / \nu _ { \mathrm { e } } ^ { 2 } \right)
* A água possui fortes absorções em frequências baixas e consequentemente tem uma cte dielétrica estática alta de 80. Em contraste, a cte dielétrica de hidrocarbonetos permanece a mesma até frequencias baixas, onde \varepsilon = n^2 \approx 2.0. Isso faz com que a primeira contribuição da cte de Hamaker entre água e hidrocarboneto seja alta (freq zero). Logo, a interação entre hidrocarbonetos através da água é dominada pelo termo entrópico.
* A interação de hidrocarbonetos em água é a mesma que água em hidrocarbonetos.
* A contribuição de frequência zero à força de v.d.W. é essencialmente eletrostática. Em qualquer meio contendo cargas livres, os campos se tornam blindados devido à polarização dessas cargas. Esses campos decaem exponencialmente (+-) com a distância, e^-kD, onde k-1 é o comprimento de decaimento característico, o comprimento de Debye de blindagem. Os valores de k são de ~1nm em uma solução 0.1M (Eq. 14.37 -- ver). Logo, dá para escrever a eq. de Hamaker utilizando esse decaimento:
     * A \approx A _ { \nu = 0 } e ^ { - \kappa D } + A _ { \nu > \nu _ { 1 } }
     * A blindagem de A \nu=0 é análoga à retardação, mas geralmente aparece somente em comprimentos muito menores. Numa solução 0.1M de NaCl, acima de 2nm as interações são basicamente de origem dispersiva.
* É possível combinar valores de cte de Hamaker, mas só vale para meios onde as interações são predominantemente dispersivas.
* É possível estimar a cte de Hamaker para líquidos sem ligação de hidrogênio por suas tensões superficiais/energias superficiais: A \approx 2.1x10^-21 \gamma (em mJ.m-2).


## Forças eletrostáticas entre superfícies em Líquidos

* Se as interações em nós fossem compostas somente de forças de v.d.W., as partículas se aglomerariam e precipitariam de solução, devido às suas atrações. Isso não acontece pq partículas em meios com alta cte dielétrica são carregadas e não se algomeram devido às forças eletrostáticas repulsivas. Forças estéricas e de solvatação também impedem.
* A carga em superfícies ocorre de três maneiras:
    1. Ionização ou dissociação de grupos superficiais (COOH -> -COO- + H+)
    2. Adsorção ou ligação de íons da solução à uma superfície previamente descarregada, como a adsorção de grupos OH- à interface água-ar, a ligação de Ca2+ a grupos zwitterionicos de bicamadas de lipídeos. Essas superfícies onde isso ocorre são superfícies *ion exchangeable*. Esse processo pode demorar bastante tempo.
    3. Quando duas superfícies dissimilares estão muito próximas, cargas, em geral prótons ou elétrons, pulam de uma superfície à outra e gera uma atração eletrostática entre as duas superfícies de carga oposta. Mecanismo de troca de carga, do tipo "ácido-base".
* A carga superficial de co-íons é contrabalanceada por uma região de contraíons. Alguns desses contraíons estão ligados, transientemente, na superfície chamada camada de Stern ou Helmholz. Outros íons formam uma admosfera de íons em rápido movimento térmico perto da superfície, chamada de dupla camada elétrica difusa.
* Camadas de mesma carga geralmente se repelem, mas podem se atrair em separações curtas. Superfícies zwitterionicas interagem eletrostaticamente uma com a outra, apesar de não terem carga formal, e geralmente essa força é atrativa.
* Superfícies carregadas, "somente contraíons", são os casos de micelas onde os contraíons presentes vieram somente das superfícies.
* A maior parte dos contraíons que efetivamente balanceiam a carga superficial (quando não há eletrólito adicionado), estão muito perto, nos primeiros angstroms da superfície. 
* Quando duas superfícies de mesma carga estão num meio sem solvente, não há um campo entre elas. Os contraíons introduzidos na região intermediária não experienciam uma força eletrostática atrativa para cada superfície (pq não há campo). A razão da acumulação dos contraíons é simplesmente a repulsão mútua dos íons, similar ao acúmulo de cargas móveis na superfície de qualquer material condutor. 
* A origem da repulsão entre duas superfícies carregadas num solvente com contraíons é entrópica (osmótica), não eletrostática. A contribuição eletrostática é geralmente atrativa. O que ocorre é que quando as superfícies são colocadas num solvente, e os contraíons se dissociam, eles tendem à migrar para a solução por efeitos osmóticos, de entropia conformacional, porque senão eles se atrairiam à superfície. Ao aproximar essas duas superfícies, os íons são forçados a voltar às superfícies, contrariando a força osmótica.
* A existÊncia de um "bulk reservoir" de íons de eletrólito tem um efeito profundo não só no potencial eletrostático mas também nas forças entre as superfícies carregadas. 
* A concentração de excesso de íons na superfície depende somente na densidade superficial de carga, portanto é independente da concentração de eletrólito no bulk, e a magnitude é suficiente para equilibrar muito da carga superficial.
* Quando se fala em dissociações de íons H+, pode-se utilizar tanto a definição de concentração (densidade numérica) quanto atividade. Porém, no equilíbrio, as atividades são iguais, pois são igualadas aos potenciais químicos dos prótons. Vemos diferenças na concentração somente.
* A presena de mM de Ca2+ é capaz de neutralizar a carga superficial, e La3+ é capaz inclusive de reverter carga.
* O comprimento de Debye pode ser calculado por:
    * \kappa = \left( \sum _ { i } \rho _ { \infty i } e ^ { 2 } z _ { i } ^ { 2 } / \varepsilon _ { 0 } \varepsilon k T \right) ^ { 1 / 2 } \mathrm { m } ^ { - 1 }
    * O comportamento da dupla camada elétrica é similar ao de um capacitor carregado.
    * O comprimento de Debye depende somente das propriedades da solução, e não da superfície, como sua carga ou potencial. Para um eletrólito monovalente (z=1), o comprimento de Debye é:
    * \kappa ^ { - 1 } = \left( \varepsilon _ { 0 } \varepsilon k T / 2 \rho _ { \infty } e ^ { 2 } \right) ^ { 1 / 2 } = \left( \frac { 8.854 \times 10 ^ { - 12 } \times 78.4 \times 1.381 \times 10 ^ { - 23 } \times 298 } { 2 \times 6.022 \times 10 ^ { 26 } \times \left( 1.602 \times 10 ^ { - 19 } \right) ^ { 2 } M } \right) ^ { 1 / 2 } = 0.304 \times 10 ^ { - 9 } / \sqrt { M } \mathrm { m }
    * Para 1:1, 1/k = 0.304/\sqrt{[NaCl]}, 2:2, 1/k = 0.176/\sqrt{[CaCl2]}, ...
* O comprimento de Bjerrum é a distância na qual a energia Coulombica, w(r) = e^2/e\pi\varepsilon\varepsilon_0r = kT.
    * \lambda _ { \mathrm { B } } = e ^ { 2 } / 4 \pi \varepsilon _ { 0 } \varepsilon k T
    * \lambda_\textrm{B} = 0.72nm em água a 25°C.
    * É possível expressar o comprimento de Debye pelo comprimento de Bjerrum: \sum _ { i } \left( 4 \pi \lambda _ { \mathrm { B } } \rho _ { \infty } i z _ { i } ^ { 2 } \right) ^ { 1 / 2 }
* Em casos onde a concentração de íons saindo de superfícies é próximo à concentração de íons no background, já presentes no sistema, as forças de interação se tornam muito mais complicadas e é necessário utilizar soluções aproximadas, numéricas. Por exemplo, o comprimento de Debye para uma solução micelar acima da cmc:
    * \kappa ^ { 2 } = \frac { e ^ { 2 } } { \varepsilon _ { 0 } \varepsilon k T } \left[ 2 X _ { \mathrm { cmc } } + \left( N X _ { \operatorname { mic } } - X _ { \mathrm { cmc } } \right) f \right], onde N é o número de agregação, f é a fração ionizada, Xcmc e Xmic são a concentração de surfactantes separados e micelizados.

### Forças de v.d.W. e de dupla camada elétrica agindo simultaneamente: a teoria DLVO.
* A atração total entre duas superfícies deve incluir tanto a teoria de v.d.W. e eletrostática. v.d.W. é praticamente indiferente à concentração de elétrólito e pH, então pode ser considerada como fixa numa primeira aproximação.
* A atração de v.d.W. deve sempre exceder a repulsão de dupla camada em distâncias curtas já que sua interação segue uma lei de potência, já a energia de dupla camada permanece finita e aumenta muito mais lentamente à medida que D \to 0. 
* Dependendo da concentração de elétrólito e densidade de carga superficial ou potencial, uma das seguintes coisas poe ocorrer:
    * Para superfícies com alta carga superficial e eletrólito diluido (comprimento de Debye alto), há uma repulsão forte a longa distância que atinge um máximo a uma distância específica, geralmente entre 1 e 5 nm, na *barreira de energia*, que geralmente é alta, muitos kT.
    * Em soluções de eletrólitos mais concentrada, há um mínimo secundário significativo, geralmente além de 3nm, conhecido como o mínimo primário. Apesar do estado mais estável termodinamicamente ser esse mínimo primário, a barreira energética pode ser alta demais para as partículas conseguirem passar num tempo razoável. Então, as partículas ficam no mínimo secundáriom, mais fraco, e  permanecem totalmente dispersas em solução. Esse é o caso de coloides cineticamente estáveis.
    * Para superfícies com baixa carga superficial, a barreira será menor. Isso leva a uma agregação lenta, conhecida como coagulação ou floculação. Abaixo de uma carga ou potencial específico, chamado de concentração crítica de coagulação, a barreira de energia cai para baixo de W=0, e as partículas coagulam rapidamente, e o coloide é *instável*.
    * À medida que a carga superficial se aproxima do zero, a curva de interação se aproxima à curva pura de v.d.W., e as duas superfícies se atraem fortemente em todas as separações.
    * Potencial: W ( D ) = \left( 64 \pi k T R \rho _ { \infty } \gamma ^ { 2 } / \kappa ^ { 2 } \right) e ^ { - \kappa D } - A R / 12 D
* É possível que, devido à posição diferente de origem das interações de v.d.W. e eletrostáticas (antes e depois da superfície), é possível que alguns sistemas exibam repeptização, estabilidade coloidal e inchamento em altas concentrações iônicas.
* A teoria eletrostática possui várias aproximações um pouco gritantes, mas funciona muito bem. Um motivo para isso é que essas aproximações introduzem erros que acabam se cancelando mutuamente.

## Forças de solvatação, estruturais e hidratação

* Quando duas superfícies ou partículas se aproximam mais perto do que alguns nm, as teorias de contínuo de v.d.W. e de dupla camada repulsiva frequentemente falham, por uma ou ambas as teorias não conseguem descrever direito em separações pequenas porque outras forças não DLVO aparecem. Elas podem ser monotonicamente repulsivas, atrativas, ou oscilatórias, e podem ser muito mais fortes que as DLVO em pequenas separações.
* Polímeros adsorvidos ou interações específicas de algumas superfícies são um exemplo.
* A força de solvatação pode se dever à partículas de solvente grudadas nas superfícies. Também, se a superfície for inerte, há uma camada de solvatação que dificulta a aproximação. Isso é parte da força de solvatação.
* As forças de solvatação surgem quando interações de curta distância entre partículas e uma superfície extendida aparecem. São chamadas de forças de solvatação, ou estruturais, e quando meio é água, forças de hidratação.
* Em interações parede sólida-líquido, há uma estruturação em camadas quase discretas, o que induz uma oscilação no perfil de densidade.
* A principal força de solvatação é a força oscilatória. Essa força surge do ordenamento das partículas perto da superfície. A aproximação de outra superfície vai forçar a mudança da posição dessas partículas, o que não é muito favorável. Porém, esses tipos de interação são utilizados para descrever superfícies rígidas. Micelas e blobs de polímeros não tem nada disso, são superfícies muito mais rugosas.
* As forças de hidratação foram propostas para explicar a estabilidade inesperada de grandes partículas coloidais sem carga, como "coavervados" (vesículas gigantes) em solução. Há dois tipos, aqueles entre superfícies fluidas de amfífilos e rígidas
    * Forças muito fortes de curta distancias e monotonicamente repulsivas foram medidas em bicamadas sem carga. A força repulsiva entre as superfícies hidrofílicas é essencialmente entrópica, surgindo da confinação das cadeias térmicamente excitadas e as cabeças saindo das superfícies à medidas que elas se aproximam.
* Uma explicação para mica em altas concentrações de sal, acima de uma concentração, os cátios se ligam à superfície aniônica da mica, mantendo um pouco de sua água de hidratação. Isso dificulta a aproximação.
* Forças "hidrofóbicas" surgiram da aparente atração aumentada de hidrocarbonetos em água.
* A força de depleção possui esse nome porque determina a adesão final da última camada de moléculas é finalmente "depletada" das duas superfícies.
* **Graus de hidrofobicidade**, que pode ser definida pela energia interfacial, a magnitude e distância da força hidrofóbica e o Ângulo de contato da água com a superfície, que é a medida mais utilizada, apesar de depender da rugosidade superficial e de algumas características aquímicas.
* A natureza das forças hidrofóbicas ainda não é muito clara, e não se sabe se deveria ser considerada uma força de solvatação ou algum tipo de interação de longa distância, do tipo eletrostática ou de v.d.W. Há três mecanismos propostos:
    * Pontes de vapor, devido à atração capilar (pressão de Laplace) entre bolhas nanoscópicas.
    * Estrutura da água, como uma força de solvatação atrativa associada a mudanças na densidade e ordenamento da água entre duas superfícies hidrofóbicas se aproximando
    * Eletrostática, relacionando forças do tipo v.d.W. entre cargas correlatas e dipolos na superfície.

## Forças estéricas (mediadas por polímeros) e de flutuação térmica

* Até agora, assumiu-se que as interfaces são bem definidas, rígidas e lisas. Porém, quando se fala de sistemas onde há regiões difusas, as interações dependem de como essas regiões se sobrepõem. Por difuso não significa áspera, mas também com grupos térmicamente lábeis da superfície. Micelas são desse tipo.
* Em alguns casos as protusões podem ser bastante pronunciadas. Quando duas superfícies se aproximam, na falta de qualquer outra interação, forças repulsivas aparecem devido à organização induzida, e são chamadas de forças de "flutuação térmica", "entropicamente levadas" ou de "protusão".
* Outro tipo de interfaces térmicamente difusivas ocorrem quando cadeias de moléculas estão ligadas nas interfaces. Quando as superfícies se aproximam, as cadeias penduradas acabam tendo que ser confinadas e aparece uma força entrópica repulsiva, chamada de repulsão "estérica" ou de "sobreposição".
* Há polímeros que não são atraídos ou repelidos pelas superfícies. Nesse caso, acaba acontecendo até uma atração entre as superfícies por forças de depleção atrativas.
* As oscilações térmicas são conhecidas também como forças de ondulação (que o Hoffmann mencionava nos artigos).
* As forças de protusão de curta distância ocorrem quando duas superfícies hidrofílicas entram em contato e as protusões na escala molecular se sobrepõem (overlap). Essa força é análoga À força de repulsão estérica. Essas forças são especialmente importantes entre superfícies anfifílicas em líquidos aquosos. A protusão pode ter sua energia definida e obtido um comprimento de decaimento de protusão.
* As forças de ondulação são de longa distância e aparecem do confinamento entrópico das ondas undulantes na medida que duas membranas se aproximam.
* O ângulo de contato é sempre medido na fase líquida.

# Estruturas de auto associação e sistemas biológicos

* Termodinâmica do equilíbrio exige que todas as moléculas idênticas em todos os agregados possuam o mesmo potencial químico
    * \mu = \mu _ { N } = \mu _ { N } ^ { \circ } + \frac { k T } { N } \log \left( \frac { X _ { N } } { N } \right) = \mathrm { constant }
    * \mu_N é o potencial químico médio de uma molécula no agregado de número de agregação N, \mu_N^0 é a parte padrão do potencial químico (energia livre de interação média por molécula), X_N é a concentração (ou atividade) das moléculas nos agregados de número N. N=1 se refere aos monômeros. A energia por agregado é N\mu_N^0.
* Através das equações de cinética, podemos chegar à forma equivalente:
    * X _ { N } = N \left\{ \left( X _ { M } / M \right) \exp \left[ M \left( \mu _ { M } ^ { \circ } - \mu _ { N } ^ { 0 } \right) / k T \right] \right\} ^ { N / M }
    * onde M é um estado de referência dos agregados (ou monômeros) com número de agregação M (ou 1).
* Dependendo de se as energia livres forem definidas como concentrações sem dimensão, X_N pode ser expresso em fração volumétrica ou fração molar. Essas equações assumem sistemas diluídos sem interação entre eles (não é o meu caso...)
* Para formar agregados \mu_N^\circ < \mu_1^\circ para algum valor(es) de N. A variação de \mu_N^0 com N determina as propriedades físicas dos agregados, como tamanho e polidispersidade.
* A dependência de \mu_N^\circ depende do formato geométrico do agregado.
* Para as estruturas com os formatos mais simples, a energia livre de interação das moléculas pode ser expressa como:
    * \mu _ { N } ^ { 0 } = \mu _ { \infty } ^ { \circ } + \alpha k T / N ^ { \mathrm { p } }
    * p depende do formato do agregado e \alpha é uma constante positiva dependente da força das interações intermoleculares.
* Há uma concentração onde o termo do monômero livre não pode mais aumentar, e chega-se na concentração micelar crítica.    
    * \left( X _ { 1 } \right) _ { \mathrm { crit } } = \mathrm { CMC } \approx \exp \left[ - \left( \mu _ { 1 } ^ { \mathrm { o } } - \mu _ { N } ^ { \mathrm { o } } \right) / k T \right]
    * Meis simples, utilizando \mu_N^\circ dado por outra equação: \left( X _ { 1 } \right) _ { \mathrm { crit } } = \mathrm { CMC } \approx e ^ { - \alpha }
pag 521
* A energia da borda de um agregado 2D é desfavorável, e essa energia é chamada de tensão de linha.
* Geralmente, pensa-se que a polidispersidade não é um defeito, mas como um estado termodinâmico natural, determinado por uma conbinação de equações termodinâmicas e as forças intermoleculares entre as moléculas dentro dos agregados. 
* Quando há forças eletrostáticas, estéricas e de hidratação fortes, e repulsivas, entre os agregados, a aproximação dos mesmos é desfavorável. Se os surfactantes se rearranjam, de micelas para cilindros, as distâncias entre os agregados são menores, e lamelas estarão ainda mais distantes. Essas transições surgem de forças repulsivas inter-agregados, e as fases tentam ficar cada vez mais longe possível uma da outra para preencher o volume inteiro. Isso também ocorre devido À forças intra-agregado, surgindo das propriedades de empacotamento molecular.
* Quando transições estruturais são causadas por forças interagregados atrativas, as estruturas grandes agora conseguem se separar, ou coexistir, com os agregados menores ou monômeros em solução. 

## Estruturas moles e biológicas

* Para entender a formação dos agregados, é necessário entender a termodinâmica de formação e as forças intraagregados.
* É possível que existam picos na distribuição de tamanhos, então podem existir micelas em coexistência com vesículas, tudo num sistema com uma fase. A definição de uma fase requer somente que as propriedades da fase sejam homogêneas em sua extensão. 
* As forças que governam a auto-associação de amfífilos em estruturas bem definidas, devivam da atração hidrofóbica na interface hidrocarboneto-agua, que induz as moléculas a se asosciarem, e as repulsões hidrofílicas, iônicas ou estéricas das cabeças, que impõe um contato oposto com a água. Essas duas forças opostas agem principalmente na área interfacial.
* O termo atrativo vem da tensão hidrofóbica ou interfacial da superfície hidrocarboneto-água. Esse valor pode ser de 50 mJm^-2 ou até 20 mJ.m-2. O termo repulsivo é muito complexo e difícil de ser formulado explicitamente. Tem contribuições estéricas, de força de hidratação e dupla camada elétrica, se eles forem carregados.
* O conceito de forças opostas introduz a noção de uma área óptima por cabeça, onde a energia total de interação por molécula de surfactante está num mínimo. A área óptima não deve ser dependente do comprimento ou número de cadeias, o que foi visto.
* As considerações de empacotamento geométrico consideram a área óptima, o volume *v* da cadeia/cadeias de hidrocarboneto, que assume-se que são fluidas porém incompressíveis, e o comprimento máximo efetivo que as cadeias podem assumir, l_c. l_c é geralmente da mesma ordem, mas um pouco menor, que o comprimento máximo das cadeias. De acordo com Tanford, a área pode ser calculada por:
    * l_n \leq l_max \approx (0.154 + 0.1265n) nm. O volume pode ser calculado por:
    * v \approx (27.4 + 26.9n) x 10^-3 nm^3.
* O parâmetro v/a_0l_c é chamado de parâmetro ou fator de empacotamento. Esses são formatos limite, então as moléculas podem se associar em estruturas com um formato cômico menor (para a direita), porque dá para diminuir l, mas não podem assumir estruturas mais cônicas.
* Estruturas diferentes podem safistazer o mesmo parâmetro de empacotamento, porém as estruturas favorecidas são aquelas com a maior entropia, ou seja, o menor número de agregação. 
* Em sistemas concentrados, as estruturas preferidas também são determinadas pelas interações entre os agregados, que causam transições para estruturas de mesofase ordenadas. Devido à forças repulsivas de curta distância entre os agregados, com o aumento da concentração de amfífilo (diminuindo a concentração de água), a área óptima diminui, e as estruturas são levadas para valores maiores de P, e se tornam mais ordenados.
* Mesofases é uma fase normal no sentido termodinâmico, mas são estruturalmente mais complexas que um líquido simples ou fase sólida. Podem conter vários agregados moleculares pequenos que podem ser monodispersos ou polidispersos, podem ser estruturas tridimensionais que se extendem indefinidamente pela fase. 
* As propriedades pouco usuais de micelas cilíndricas são totalmente devido a efeitos nas pontas. Em cada ponta, as moléculas são forçadas a se empacotar em capas hemisféricas, então a > a_0. Á medida que a_0 diminui, a desfavorabilidade aumenta. Essa energia pode ser recuperada se duas pontas se juntarem, mas aí se perde entropia configuracional e energia de dobra.
* Bicamadas são formadas por amfífilos que não conseguem se empacotar em micelas, porque a_0 é muito pequeno ou pq as cadeias são grandes demais para caber numa micela. 
* O tempo de residência de moléculas de surfactante em micelas é da ordem de 10^-4s, mas em bicamadas, 10^+4 s. Esses tempos dependem das moléculas, não das estruturas. Então, se uma lamela possi um surfactante de uma cadeia, o tempo de residência dele vai ser muito menor.
* São formadas vesículas quando é mais favorável que as pontas desfavoráveis forem eliminadas numa distância finita, ao invés de infinita, o que também é entropicamente favorável. É possível calcular um raio limite para as vesículas de modo que a_0 não seja excedido.
* Efeitos:
    1. Área da cabeça. Cabeças menores formam vesículas maiores, bicamadas menos encurvadas ou fases micelares inversas. Isso pode ser feito aumentando a concentração de sal ou diminuindo o pH.
    2. Empacotamento das cadeias. Introduzindo ramificações e insaturações, particularmente de insat. cis, l_c diminui. O mesmo acontece quando o volume efetivo v é aumentado devido à penetração de moléculas orgânicas como alcanos de baixa MM. 
    3. Temperatura. Os efeitos são mais sutis e menos entendidos. As áreas das cabeças geralmente aumentam com T devido ao aumento da repulsão estérica entre eles, o que diminui P. Isso vale para surf. ionico.
    4. Misturas de lipídios. De início, pode-se tratar das estruturas por um P medio. 

