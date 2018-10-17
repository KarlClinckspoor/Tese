Fontes interessantes de informação para espalhamento de MG

1. Livro; Giant Micelles, cap 6. "Scattering from Wormlike Micelles", escrito pelo Pedersen et al.
2. Artigo: "Scattering from polymer-like micelles", Lynn M. Walker.
3. Livro: Neutrons, X-Rays and Light, Cap 16 "Modelling of Small-Angle Scattering Data from Colloids and Polymer Systems".
4. Livro: Neutrons, X-Rays and Light, "Introduction to Scattering Experiments", P.N. Pusey
5. Livro: Scattering Methods and their Application in Colloid and Interface Science. Vários Capítulos interessantes
6. Livro: Soft Matter Characterization " Synchrotron Small-Angle X-Ray Scattering" Narayanan e " Basic Concepts – Scattering and Time Correlation Functions" Pecora
7. Material de aula do Pedersen

---
Basic Concepts, Pecora

---

O mecanismo de espalhamento de luz, neutrons e raios-X são diferentes, mas em comum, essas técnicas tem o conceito de interferência e a relação com a estrutura do meio.

Num experimento de espalhamento, é incidida radiação num volume da amostra que então espalha. É então medida a amplitude do espalhamento num detector a uma certa distância. O padrão depende da interferência entre as ondas espalhadas pelos diversos centros da amostra.

Detectores geralmente respondem ao sinal com o quadrado da amplitude da onda espalhada (provavelmente pq isso se torna intensidade).

A radiação que é espalhada por dois centros chega no detector com uma diferença na fase de suas ondas, devido à uma diferença na distância que elas tiveram que percorrer. A diferença é \delta = 2 \pi d / \lambda.

Os vetores ki e kf são os vetores no caminho da radiação incidente e espalhada, respectivamente. O valot do vetor q é dado por q = ki - kf. O comprimento dos vetores ki e kf é de 2 \pi / \lambda.

A diferença de fase pode ser representada por \delta = q \cdot (ri - rj) onde ri e rj são as posições dos centros espalhadores medidos em relação a um sistema de coordenadas arbitrário e o comprimento de q está relacionado com o ângulo do espalhamento. q = 4 \pi / lambda sin (\teta / 2)

Se o vetor q for multiplicado por h/2\pi, isso pode ser interpretado como o momento transferiro ao sistema pelos fótons.

As ondas emitidas possuem a forma de exp (i q \cdot ri - rj). Se essas ondas forem somadas, de todos os centros, temos a amplitude total de espalhamento. A Intensidade é obtida pela multiplicação de \psi por \psi\*, onde o asterisco significa o conjugado complexo.

O comprimento de onda da radiação incidida informa qual é a faixa aproximada de partículas que se pode estudar. 

---
Synchrotron Small-Angle X-Ray Scattering" Narayanan

---

O espalhamento de raios-X em baixos ângulos se origina de flutuações espaciais na densidade eletrônica dentro de um material. A quantidade de informação estrutural obtida de um experimento depende do grau de ordem supramolecular na amostra. Coisas mais ordenadas fornecem mais informações.

Ver ref Guinier, A. and Fournet, G. (1955) Small-Angle Scattering of X-rays. Wiley, New York, parece interessante.

O formalismo para espalhamento em baixos ângulos é similar para luz, neutrons e raios-X. A diferença importante é a interação da radiação com o meio espalhador. Luz origina de diferenças no índice de refração, já neutrons são espalhados por núcleos atômicos.

Um feixe é incidido na amostra, que espalha. Na direção para frente, é colocado um detector bidimensional, e tudo é colocado em vácuo para evitar espalhamento. O número de fótons é medido em função do ângulo de espalhamento. Para raios-X, o espalhamento se origina dos elétrons (espalhamento de Thomson), que é praticamente independente do comprimento de onda. O espalhamento é completamente elástico devido à alta energia da radiação em comparação com as excitações típicas da amostra. Dessa maneira, as amplitudes dos vetores incidente e espalhado são iguais, |ki| = |ks| = 2\pi/lambda e o índice de refração é próximo da unidade. A transferência de momento, ou vetor de espalhamento é dado por q = ks - ki = 4\pi/\lambda sin (\teta/2)

O q também informa os comprimentos tipicamente observados em SAXS, dado pelo inverso do q. Faixas de q de 0.006 a 6 nm-1 resulta em tamanhos de 1um a 1 nm.

Para sistemas diluídos contento N partículas por unidade de volume, com interações interpartículas sendo ignoradas, a intensidade de espalhamento depende basicamente do formato e tamanho das partículas. I(q) = N | F(q) | ^ 2. F(q) é a soma coerente das amplitudes de espalhamento dos centros individuais dentro da partícula dada pela transformação de Fourier da distribuição de densidade eletrônica.

O comprimento de espalhamento pode ser substituído pela densidade de comprimento de espalhamento, \rho = b_M / V_m onde b é a soma de todos os b átomos nas moléculas e Vm é o volume molecular. Se a densidade for uniforme,

\rho = (ne dM Na)/Mw * re

onde ne é o número de elétrons, dm é a densidade de massa (água é 1000 kg/m3), Na é o número de avogrado e Mw é a massa molar.

Caso a densidade eletrônica seja aproximadamente contínua, a amplitude de uma partícula pode ser expressa como 

F(q) = \int_v \rho_r e^(iqr) dV

Num solvente, temos a a densidade de comprimento de espalhamento relativa, ou o contraste (\Delta \rho = \rho - \rho_M).

Alterando a base dessa integral para r ao invés de V, uma partícula esférica temos que |F(q)|^2 (Intensidade) = V_s^2 \Delta \rho^2 P(q, R_s)

Para esferas, o padrão de espalhamento possui vários mínimos. Porém, amostras reais possuem desvios que estão relacionados com a polidispersidade. Para esferas, os mínimos estão nos pontos qRs = 4.5, 7.73, etc. (Tem algum padrão? Os zeros da Eq são obtidos como?) A função de polidispersidade D(R), onde \int D(R)dR = 1 com cutoff em R=0. Expressões analíticas de D(R) existem para vários tipos de distribuição diferentes. (acho legal fazer uma correlação com a determinação do tamanho das esferas com o mínimo da curva com a determinação da distância interlamelar pelo pico.)

O sinal I(q) possui duas regiões, no limite. Uma é a região de guinier, em valores bem pequenos de q onde a intensidade do sinal é dependente do raio de giro do polímero. Isso é válido somente para qRg < 1.

I(q) = NV^2\Delta\rho^2 \exp(-q^2R_g^2/3)

Esse tipo de relação é utilizado em gráficos ln I(q) vs q^2 para se determinar o raio de giro (seria a inclinação?)

Para o outro limite, onde qRg >> 1, o espalhamento observa a interface das partículas. Isso leva ao comportamento de Porod

I(q) = 2 \pi N \Delta\rho^2 S q^{-4}

Isso significa que existe uma interface abrupta (melhorar termo) entre a partícula e o meio. Variações da lei de potência de I(q) são comumente observadas em SAXS. Valores de q=4 é uma interface sharp, 3 <= p < 4, superfície fractal, 3 < p é um fractal de massa e p \approx 2 é uma cadeia polimérica gaussiana. Valores maiores que 4 podem ser observados em interfaces difusas não-fractais. Determinar esse valor precisa ser feito com muito cuidado, pois subtração errada do background, não linearidade do detector podem afetar a determinação precisa de p.

O valor d\Sigma/d\Omega é o "differential scattering cross section per unit volume", que contém informações sobre a estrutura e as interações no sistema sobre uma faixa de q, e é expresso em unidades de comprimento vezes ângulo sólido, recíproco (m-1 sterad-1). Para atingir um entendimento quantitativo das intensidades medidas, é necessário entender d\Sigma\d\Omega, que será chamado de I(q) e dado por comprimento recíproco. (Então, aquilo significa mesmo intensidade). (Ele chama em outro lugar de intensidade absoluta)

Quando o sistema está mais concentrado, surge um termo chamado fator estrutura S(q), que é uma função complexa de N e o potencial de interação U(r). S(q) \approx 1 em regime diluído. 

I(q) = NV^2\Delta\rho^2 P(q) S(q)

S(q) relaciona a intensidade espalhada com a microestrutura através de uma função de correlação de pares, g(r) que está relacionada com a probabilidade de se encontrar uma partícula a uma distância r de outra partícula.

S(q) = 1 + 4 \pi N \int_0^\inf (g(r) - 1) sin (qr) / qr r^2 dr

Para sistemas polidispersos, não é possível fazer uma completa separação de P(q) e S(q) e estão é necessário utilizar um fator estrutura efetivo Sm(q) que depende das amplitudes individuais de espalhamento.

Existem várias maneiras e várias aproximações para se descrever esses sistemas, tornando essa área bastante complicada. Existem outras técnicas, como o Generalized Indirect Fourier Transformation (GIFT), que usa um P(q) independente de modelo e um S(q) dependente. 

Muitas misturas de surfactantes e polímeros se associam formando fases lamelares e hexagonais. SAXS é utilizado para caracterizar a estrutura e o grau de ordem desses sistemas complexos. A posição e as intensidades relativas dos picos de Bragg permitem determinar as simetrias moleculares. São utilizados os índices de miller e tudo mais.

Esses picos de difração aparecem como pontos no detector, mas para uma amostra policristalina, aparecem como linhas nos raios específicos. A intensidade é descrita por:

I(q) = K_sf |F_hkl(q)|^2 m_hkl e^-2M F_ls(q)

925

A ref "Regenfuss, P., Clegg, R.M., Fulwyler, M.J., Barrantes, F.J., andJovin, T.M. (1985)Rev. Sci. Instrum., 56, 283" fala sobre stopped-flow.

---
Livro do Otto Glatter
Capítulo 1, Interferência, teoria de Rayleigh-Debye-Gans

---

Quando uma onda eletromagnética é enviada através de uma fatia fina de material, o campo elétrico da radiação irá introduzir uma polarização nos átomos, levando à formação de pequenos dipolos. O campo elétrico oscila com a frequência definida pelo comprimento de onda da radiação enviada para o material, então os dipolos irão oscilar num movimento forçado com a mesma frequência. Descrevendo esse modelo utilizando íons e osciladores harmônicos, um modelo clássico. Esse é conhecido com o modelo de Lorentz.

Uma onda não só é parcialmente absorvida pela matéria que passa por um corte fino de material (decaimento exponencial), mas também origina num campo de espalhamento, porque toda carga elétrica acelerada emite um campo elétrico com uma amplitude proporcional à aceleração.

Em experimentos espectroscópicos, ocorrem fenômenos de absorção, onde ocorre absorção dependente da frequência e se encontra a ressonância dos sistemas. Essa faixa está próxima ao limite de Lorentz. Em métodos de espalhamento, fica-se longe dessas frequências de ressonância \omega_0. Em frequências baixas, \omega << \omega_0, o limite de Rayleigh (luz visível). Para altas frequências, \omega >> \omega_0, estamos no limite de Thomson, que vale para raios-X. Em ambos os limites ocorre espalhamento por ondas emitidas pelos dipolos oscilantes.

Para matéria mole, estamos praticamente sempre longe do regime de ressonância. Além disso, a energia dos raios-X é grande o suficiente para polarizar todos os elétrons da amostra, inclusive aqueles das camadas mais internas dos átomos, então todos os elétrons no volume iluminado dão origem à onda espalhada.

Para o espalhamento de luz visível, ocorre somente polarização dos elétrons mais afastados, tipicamente de valência. A polarizabilidade é proporcional ao índice de refração do material. (Ver o capítulo 9, static light scattering, onde ele avança esse tema).

Deixando a onda atingir a partícula. Todas as ondas espalhadas são coerentes, isso é, tem uma relação de fase fixa entre a radiação incidente e espalhada, e ambas possuem a mesma frequência. Espalhamento incoerente (Compton) não é importante para SAXS, mas é importante para SANS.

As ondas terão uma diferença em suas fases de \theta, que depende da posição dos centros espalhadores de um em relação ao outro. A diferença de fase relativa a um feixe de referência arbitrário é dado pela diferença dos comprimentos de caminho multiplicados pelo número de onda k = 2 \pi / \lambda.

Definindo um vetor unitário que atinge um ponto O no corpo, s_0, a direção do feixe espalhado é dado por s. A diferença entre o feixe de referência e espalhado é a-b = rs_0 - r_s = -r (s - s_0)

Aí, podemos obter a diferença de fase multiplicando pelo número de onda. \phi = -(2\pi/\lambda) r (s-s_0). Introduzindo o vetor de espalhamento q como q = (2 \pi / \lambda) (s - s_0) obtemos \phi = -qr.

O vetor de diferença (s - s_0) está simetricamente ao incidente e espalhado, ou ortogonal ao "plano espelhado", e sua magnitude é 2\sin(\teta/2), onde \theta é o ângulo espalhado.

A amplitude do vetor de espalhamento q tem a mesma direção de (s - s_0) e sua magnitude é dada pela magnitude de (s - s_0), 2\sin(\teta/2) multiplicado pelo número de onda 2\pi/\lambda.

q = |q| = 4 \pi/\lambda \sin \teta/2

Para ângulos pequenos, é possível substituir \sin \teta/2 por \teta/2. A dimensão é o recíproco de comprimento. Usar o q torna as medidas independentes do comprimento de onda. A direção de q não é a direção do detector, mas aponta para a linha que bissecciona o feixe incidente e a direção do detector.

O produto vetorial escalar qr significa que somente a componente q na direção de q é relevante para a fase da onda. Isso implica que todos os pontos perpendiculares a q possuem a mesma fase. Isso origina a ideia de uma reflexão de um conjunto de planos, o que aparece nas teorias de cristalografia.

O campo espalhado total da partícula é calculada somando-se todas as ondas secundárias, considerando-se suas fazes. Isso é feito utilizando-se notação imaginária, onde um número de magnitude 1 e fase \phi é representado por e^i\phi. Como a fase é $qr$, então a onda é dada por $e^-iqr$. A densidade de elétrons é dada por \rho(r). Trocando soma por integração, temos que

E_s = \int_V \rho(r) e^(-iqr)dr

O espaço contendo os vetores de posição r é o espaço real e o espaço contendo q é o espaço recíproco. Os espaços estão conectados pela fase qr. Para manter os valores constantes, somente se r for aumentado e q for diminuído pelo mesmo fator. Então, partículas grandes (comparadas com o comprimento de onda) espalham principalmente em baixos ângulos (baixo q). Isso resulta em experimentos de SAXS e SANS.

A teoria de Rayleigh-Debye-Gans é bem complicado.

A Intensidade de luz espalhada é dado pelo quadrado da amplitude (field F). Para sistema diluídos, assumindo que não interações, é possível simplificar bastante as expressões de intensidade e amplitude. É possível relacionar a intensidade com:

I(q) = N<|F(q)|^2> = NF_0^2P_0(q) = NP(q)

O fator forma P0(q) normalizado e médio.

---
Livro do Otto Glatter
Capítulo 2, Teoremas gerais e casos especiais

---

Raio de Guinier

I(q) = I(0) * e^{-q^2R_g^2/3}

Dá para extrair o raio de guinier com um plot ln(I(q)) vs q^2.

F(q) = <F(\mathbf{q})> = 4\pi \int_0^\inf\Delta\rho(r) r^2 sin qr / qr dr.

Aí chegamos na expressão clássica de F(q) = sin qr - qr cos qr ... Isos é igual à função de Bessel de ordem 3/2 J_3/2(qR). 

Aí ele extrai as informações para outros sistemas.

Em princípio, não é possível determinar a distribuição de tamanho e o formato de partículas. Isso requer assumir muitas coisas sobre o sistema, e tem que ter dados muito precisos.

--- 
Livro do Otto Glatter
Capítulo 3 - O problema inverso de espalhamento

---

O problema do espalhamento envolve o cálculo de funções de espalhamento de partículas de tamanho, formato e estrutura interna conhecidas. Esse é o problema "fácil". O problema inverso é reconhecer detalhes eestruturais de partículas desconhecidas a partir do padrão de espalhamento delas.

Há duas maneiras para se resolver esse problema. O primeiro é uma avaliação livre de modelos, onde informações nas curvas são cuidadosamente avaliadas. A outra maneira é pelo ajuste de modelos, onde um modelo matemático é ajustado à curva utilizando o método dos mínimos quadrados. Ele fala que o melhor é primeiro utilizar uma avaliação livre de modelo, construir uma ideia de como o sistema deve ser, e depois desenvolver um modelo, preferencialmente aliado a técnicas adicionais.

---
Livro do Otto Glatter
Capítulo 4, Efeitos de concentração, interações

---

Até agora assumimos que os espalhadores são completamente sem correlacionados, i.e., que todas as partículas são reconhecidas como independentes com respeito a sua translação e orientação, assumindo que não há interações entre partículas.

I(q) = NF_0^2P(q)S(q)

Para sistemas diluídos, S(q) = 1

A intensidade de espalhamento como produto de P(q) x S(q) é essencialmente diferente do fator forma somente em valores de q pequenos, tipicamente no regime do máximo principal. Isso não é surpreendente especialmente porque as distâncias interpartículas são maiores do que as distâncias intrapartículas.

O potencial de esferas rígidas, também conhecido como potencial de volume excluído, é definido como:

u(r) = \infty r < (Ra + Rb)
     = 0 r > (Ra + Rb)

O potencial de Yukawa é parecido com o de esferas rígidas, mas coloca um valor de potencial eletrostático para o termo de r > 2R.

Quando começa a ter amostras com estruturação e polidispersas, há uma dependência entre os fatores e fica difícil de separá-los. O fator de estrutura efetivo não só depende das interações das partículas, mas também pelas amplitudes das formas.

Fases multilamelares mostram picos equidistantes superpostos com o fator forma das lamelas. Esses picos são consequência da ordem equidistante das pilhas, e estão relacionadas com a distância média das bicamadas. Na prática camadas lamelares possuem irregularidades fortes. O número de bicamadas espalhando coerentemente é relativamente baixo e polidisperso, as lamelas possuem flexibilidade considerável. Esses parâmetros dependem da estrutura molecular do anfífilo e fortemente na temperatura.

O I(q) de lamelas é o produto de um fator forma e um fator estrutura. O S(q) possui o formato de vários picos, que acabam sendo observados no I(q). O primeiro pico possui a intensidade mais alta, que vai diminuindo.

Resumo: Interações entre centros espalhadores levam a uma ordenação no sistema. Isso significa que a posição de uma partícula não é independente da posição de todas as outras partículas. Em termos de teoria de espalhamento, não há nenhum efeito novo. Ainda há onduletas secundárias que interferem umas com as outras. Porém, num sistema diluído, essas interações se cancelam devido à posição e orientação arbitrárias. No sistema concentrado, essas interações não podem ser ignoradas. Isso dá origem ao fator estrutura, que deve ser multiplicado pelo fator forma, para chegar à intensidade. Essas interações podem ser modeladas como esferas rígidas sem carga. Dependendo do sistema e do tipo de interação, o modelos de fator estrutura possuem de 2 a cinco parâmetros independentes, de natureza fortemente não linear e que fazem a determinação do fator forma e estrutura bastante complicado.

---
Livro do Otto Glatter
Capítulo 5: Variação de contraste

---

Contraste é a diferença na densidade dos centros espalhadores no objeto espalhador e o meio que o cerca (solvente). A densidade de centros espalhadores é expressa como o comprimento de espalhamento por volume. Os centros espalhadores, para raios-X, é igual ao número de elétrons na nuvem eletronica do átomo. O comprimento de espalhamento para raios-X de um átomo pode ser calculado pelo número atômico Z, de acordo com:

b = b_0Z = r_0Z. r_0 = 0.28179 x 10^-12 cm

O r_0 é o raio do elétron.

Para neutrons, o comprimento de espalhamento utilizado é o dos átomos, que depende do isótopo e seu estado de spin. O exemplo mais marcante é o hidrogênio, b=-0.374 x 10^-12 cm e deutério, b=+0.6674 x 10^-12 cm. Geralmente, eles minimizam a quantidade de hidrogênios para diminuir o espalhamento incoerente, o que resulta em amostras de moléculas hidrogenadas no solvente deuterado.

Para luz visível, o cálculo de espalhamento é diferente, porque uma subseção dos elétrons participa do espalhamento. O comprimento de espalhamento é dependente do índice de refração n. O comprimento de espalhamento no vácuo é dado por

b = \alpha k_0^2 onde \alpha é a polarizabilidade e k_0 é o comprimento de onda no vácuo (k_0 = 2 \pi / \lambda_0). A polarizabilidade pode ser descrita como dependente do índice de refração como:

\alpha = 3/4\pi V/N (n^2 - 1)/(n^2 + 2) \approx 1\4\pi (n^2-1) = 1/4\pi M\nu/N_A (n^2-1)

N/V é o número de partículas no meio. \nu é a densidade. N_a é o número de avogrado e M é a massa molar.

A intensidade de sinal é proporcional ao quadrado da diferença de densidade do meio. Além disso, a intensidade também é dependente do fluxo, e geralmente SAXS de síncrotrons possui um fluxo bastante alto em comparação com SANS, mas SLS geralmente tem um fluxo mais intenso ainda.

Ver ref 165 e 168.

O estudo de sistemas micelares em água por SAXS, geralmente há um problema bastante grande de contraste, que é baixo. A adição de sal, açúcar ou glicerol, que poderia aumentar o contraste, pode afetar a formação de micelas (! - pensava que iria piorar). Isso faz com que análises de micelas por SANS seja geralmente melhor.

As cabeças geralmente possuem um valor positivo de \Delta\rho e as cadeias alquílicas, por outro lado, possuem contraste negativo, o que resulta no final num contraste baixo. Por outro lado, o fator estrutura pode ter maior contribuição para o espalhamento do que o fator forma, tornando mais fácil detectá-lo por SAXS do que por SANS.

Espalhamento de luz de soluções relativamente concentradas pode ser melhorado adicionando-se glicerina ou açúcar. Isso diminui o contraste e evita espalhamento múltiplo.

---
Livro Otto
Capítulo 8, Métodos numéricos

---

Etapas:

1. Normalização, onde as intensidade são multiplicadas por ou um valor constante ou por um valor dependente de q.
2. Médias. Altamente recomendado, para mostrar a estabilidade do sistema, e permite obter uma boa estimativa da variância/desvio padrão, incluindo possíveis contribuição, não só estatísticas. Todas as curvas tem que ter a mesma abscissa, que a rotina tem que checar antes da média.
3. Binning ou funelamento. Detectores sensíveis a posição ou detectores de imageamento possuem uma limitação em sua construção. Geralmente, eles tem um espaçamento constante de pixeis pelo detector. Para ter um incremento pequeno o suficiente em baixo q, é necessário utilizar a maior resolução possível no detector todo, o que leva a um grande número de pontos experimentais e baixos valores de intensidade para q baixos. Isso pode ser resolvido juntando pontos (binning) dependendo dos valores de q para melhorar os resultados. A propagação de erro é feita acumulando-se os pontos experimentais e depois calculando os desvios padrões.
4. Subtração. Isso é feito subtraíndo-se o background do solvente (e port aamostra) da amostra (solvente + amostra).
5. Extrapolação para concentração zero. Isso é feito para garantir que não há influência interpartículas. (Deve ser aplicável a só um conjunto de casos)

Ele realmente gosta de obter a função de autocorrelação unidimensional (p(r) x r). Isso é feito aplicando-se uma transformação inversa de Fourier .