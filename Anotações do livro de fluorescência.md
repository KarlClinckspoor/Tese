Anotações do livro de fluorescência

* Luminescência é a emissão de luz por uma substância que ocorre de estados excitados. Dividida em duas partes, fluorescência e fosforescência.
* No estado excitado singlete, o elétron no orbital excitado está pareado com o elétron no ground state. Isso faz com que a transição seja permitida, e torna as velocidades altas.
* Os tempos de vida da fluorescência estão na ordem de 10 ns, com as taxas de emissão tipicamente em 10^8 s-1.
* Resolução temporal de estados excitados requer equipamentos muito sofisticados.
* Fosforescência, por outro lado, o elétron está paralelo ao elétron do estado padrão, e a transição é proibida, o que aumenta o tempo de vida para milisegundos até segundos.
* Raramente soluções aquosas em temperatura ambiente são fosforescêntes porque há muitos processos que conseguem relaxar/desativar, como decaimento não radiativo e processos de quenching. A diferença entre fluorescência e fosforescência nem sempre é clara, mas no caso deste trabalho, temos claramente fluorescência.
* Fluorescência ocorre tipicamente em moléculas com grupos aromáticos, como quinina. A intensidade de fluorescência é melhor observada a 90° ou utilizando um solvente menos polar, como etanol, que diminui a constante dielétrica.
* Átomos geralmente não são fluorescentes, mas há alguns lantanídeos que fluorescem devido à blindagem dos orbitais *f* pelos elétrons das camadas mais externas.


* Procurar o resumo por Berlman sobre fluoresceína. Parece muito interessante.

# Diagramas de Jablonski

* O diagrama de Jablonski é frequentemente utilizado para ilustrar os fenômenos de fluorescência e fosforescência. É possível ver também no diagrama que a intensidade da luz que excita a molécula não afeta muito a fluorescência, que sempre sai do nível mais baixo de energia do estado excitado.
* No diagrama de Jablonski, eles removeram os efeitos de quenching, transferência de energia e interações com o solvente.
* O eixo x do diagrama seria tempo? Não necessariamente.
* As transições entre estados ocorrem na ordem de 10^-15 s, muito rápido, mais rápido que o deslocamento dos núcleos. Esse é o princípio de Frank-Condon.
* O fato dos níveis excitados decaírem para o estado basal é porque a energia térmica ambiente geralmente não é o suficiente para mantê-los nessas energias altas.
* A conversão interna, que é o processo em que os elétrons do estado excitado decaem para o nível basal excitado, é bastante rápida, da ordem de 10^-12 s ou menos. Como a fluorescência ocorre em 10^-8s, isso dá tempo da conversão interna completar. O termo é "thermally equilibrated excited state"
* O retorno para o estado fundamental geralmente vai até um estado vibracional que não é o fundamental também. Essa é a razão de algumas moléculas possuírem uma estrutura vibracional em seu diagrama de emissão. Frequentemente, o espectro de emissão é um espelho do espectro de absorção, pois a excitação eletrônica não altera a geometria nuclear. Portanto o espaçamento dos estados vibracionais dos estados eletrônicos excitados e fundamentais são semelhantes. Algumas moléculas não possuem esse espelhamento, porque a transição do estado S2 para o estado S0 é muito pouco provável, sendo a transição S1->S0 mais provável. Logo, o espectro de emissão acaba sendo um espelho da transição S0->S1, não do espectro de emissão total.
* A conversão de spin de um elétron do estado S1 para o estado T1, chamado de cruzmento intersistema, resulta no fenômeno de fosforescência. A transição de T1 para o estado fundamental é proibida, então o processo é lento. Átomos com massas atômicas altas facilitam o cruzamento intersistemas e aumentam o rendimento quântico da fluorescência.

# Características da emissão de fluorescência

* A energia de emissão é geralmente menor do que a de absorção, o que pode ser visto pelo diagrama de Jablonski. Primeiro, frequentemente os elétrons são excitados para estados vibracionais mais energéticos do estado eletrônico excitado. Além disso, a fluorescência geralmente ocorre também para estados vibracionais excitados do estado fundamental, aumentando ainda mais a divergência de intensidade dos dois espectros. Isso é conhecido como deslocamento de Stokes.
* Lei de Kasha: O espectro de emissão são tipicamente independentes do comprimento de onda de excitação. Isso é devido à relaxação rápida ao estado vibracional fundamental do estado excitado.
* Uma das consequências do princípio de Frank-Condon, é que como as posições atõmicas não mudam, a ´probabilidade de uma transição 0->1 é igual à probabilidade da transição 1->0, o que possibilita os espectros serem espelhados.

# Tempos de vida de fluorescência e rendimentos quânticos

* Rendimento quântico é o número de fótons emitidos relativo ao número de fótons absorvidos. Rodaminas possuem rendimentos próximos de 1, e são bastante brilhantes. Os processos de decaimento não radiativos diminuem a eficiência quântica.
* O tempo de vida está relacionado com o tempo que um fluoróforo tem para interagir com o solvente e o meio, fornecendo mais informações sobre ele.

$\Gamma$: taxa de emissão do fluoróforo
$\k_{nr}$: taxa de emissão não radiativa.

$Q = \dfrac{\Gamma}{\Gamma + k_{nr}}$
$\tau = \dfrac{1}{\Gamma + k_{nr}}$

Q é o rendimento quântico e \tau é o tempo de vida. O processo de decaimento é aleatório, então o \tau representa somente um tempo médio. Para um decaimento exponencial, 63% das moléculas decaiu em t=\tau.

* Caso não haja processos não radiativos, o tempo de decaimento natural é a taxa de decaimento. Dá para calcular \Gamma utilizando uma integração, que é dependente do índice de refração do meio, o comprimento de onda médio (?) é a integral do espectro de absorção dividido pelo comprimento de onda, sobre o comprimento de onda.
* Quando \Gamma é alto, geralmente o rendimento quântico também é, porque não houve tmepo de ocorrer processos não radiativos.

# Quenching

O processo de quenching ocorre por vários mecanismos. Um deles é o quenching colisional, quando uma molécula no estado excitado bate na outra em solução e perde sua energia. Não há alteração química nas moléculas.
* Grupos que agem como quenchers: oxigênio, halogênios, aminas, moléculas deficientes em elétrons como acrilamidas. O mecanismo específico varia de acordo com os pares, como transferência eletrônica quando quencher é deficiente eletronicamente e acoplamento spin-órbita e cruzamento intersistemas com halogênios.
* Pode ocorrer a formação de complexos não fluorescentes, impedindo o processo de fluorescência bem no começo. Há também mecanismos não moleculares, como atenuação da luz incidente pelo fluoróforo ou outras espécies.
* Outro resultado do princípio de Frank-Condon é que o processo de absorção informa somente algo sobre o estado fundamental médio das moléculas, e somente informações das moléculas de solvente nas imediações. Já o processo de emissão, que é mais longo, consegue interagir com moléculas em solução. Isso é óbvio porque há a existência de quenchers. Os longos tempos de fluorescência permitem a observação de moléculas de oxigênio até 450\AA de distância.
* Outro fenômeno que acontece é a relaxação do solvente. Tipicamente as moléculas no estado excitado possuem uma polaridade diferente, geralmente tem dipolos maiores. As moléculas do solvente ao redor devem se orientar ao redor dessa novo dipolo. O processo de uma molécula ocorre na ordem de 40 ps ou menos. O processo total de relaxação ocorre em cerca de 10^-10 em soluções. Essa reorientação diminui a energia do sistema, e desloca os espectros para comprimentos de onda maiores (menos energéticos). Isso resulta na forte dependência do solvente, e sua polaridade, nos espectros de absorção. O deslocamento é conhecido como deslocamento de Stokes.

# Transferência de energia de ressonância (RET)

* Ocorre quando a miessão de um fluoróforo, chamado de doador, se sobrepõe ao espectro de absorção de outra molécula, o acceptor, que não precisa ser fluorescente. 

# Tipos de medidas de fluorescência

* Há fluorescência no estado estacionário e resolvida no tempo.
* Estacionário: Iluminação da amostra e observação constantes. Como os fenômenos de fluorescência são da escala de ns, a maior parte das medidas é no estado estacionário. Neste trabalho, os experimentos de fluorescência resolvida no tempo, na verdade, são fluorescência estacionária resolvida no tempo.
* Resolvida no tempo: Um pulso rápido é incidido na amostra, e a intensidade do decaimento de fluorescência é medida em função do tempo. A relevância dos experimentos resolvidos no tempo é que grande parte da informação é perdida durante a operação de média inerente da Fl. estacionária.

# Capítulo 2: Instrumentação

* Conversão de comprimento de onda para cm-1 é feito assim:

400 nm = (400 x 10 ^ -7 cm)^-1 = 25000 cm-1.

A vantagem é que número de onda tem uma escala linear com energia, mas os equipamentos geralmente mostram em comprimento de onda.

* Há algumas moléculas cuja fluorescência é dependente da viscosidade do meio devido à dependência de seu rendimento quântico com a viscosidade. CCVJ, soluções de etileno glicol/glicol.

* A maneira mais fácil de se determinar o rendimento quântico de um fluoróforo é compará-lo com padrões de rendimento conhecido. 

# Capítulo 3: Time-domain lifetime measurements

* A análise deve ser feita por mínimos quadrados não lineares.

Esse método assume que:

1. Toda a incerteza experimental está na variável dependente (eixo y)
2. As incertezas na variável dependente possuem uma distribuição Gaussiana, centrada no valor correto.
3. Não há erros sistemáticos na variável dependente ou independente.
4. A função de ajuste utilizada descreve matematicamente o sistema, corretamente. Modelos incorretos resultam em parâmetros incorretos.
5. Os pontos são todos observações independentes.
6. Há um número suficiente de pontos experimentais que os parâmetros são "overdetermined"

Quando os dados são transformados, por exemplo, para um plot linear, é possível que os erros não estejam mais distribuídos Gaussianamente ao redor dos pontos, o que invalida a aplicação de um método desses.

* O ajuste é feito minimizando-se o \chi^2, que é o valor medido menos o decaimento calculado assumindo-se os parâmetros da função.

\chi^2 = \sum_k 1/desvio_k^2 (N_medido - N_calc)^2

O desvio do ponto pode ser assumido como sendo igual se for uma medida espectroscópica por exemplo. Aí vira o número de contagens obtido, no demonimador.

O \chi^2 é dependente do número de pontos, então o \chi^2_red pode ser utilizado para julgar melhor.

\chi^2_red = \chi^2 / (n - p)

Onde n é o número de pontos e p é o número de parâmetros do ajuste.

* Erros sistemáticos podem dar a aparência de que é necessário utilizar um modelo mais complexo.

* O goodness of fit fala o quão bom o modelo é. Mas como ter certeza se o ajuste foi feito bem? Isso pode ser feito por métodos matemáticos e por experiência.

* Um método matemático é calcular a probabilidade do resultado ser devido a erros aleatórios.

O método matemático se baseia no uso de tabelas de distribuição. O exemplo do livro fala que se você tiver mais que 200 pontos experimentais e um \chi^2_red de 1.25, a probabilidade de ser devido a erro é de 0.01, ou 1%. Se o \chi^2_red for de 1.08, a probabilidade é de 20%, então não pode rejeitar o modelo. Não recomendam rejeitar um modelo se o desvio for maior que 5%. (É, não entendi intuitivamente, me parece que deveria ser o contrário. Acho que isso funciona comparativamente. Aquele que tiver uma chance maior de ser devido a erro deve ser descartado, se o outro tiver uma chance menor.)

# Efeito do solvente e ambiente químico

* Existem vários mecanismos que explicam mudanças de deslocamento de Stokes no espectro. Poucos sobre o aumento no rendimento quântico.
* Uma das origens do aumento quântico de uma molécula CCVJ num meio mais viscoso é que sua ligação no anticorpo previne a rotação ao redor da ligação de etileno, que contribuia para perda de fluorescência por processos não radiativos. Sem essa rotação, a fluorescência aumenta.

# Quenching

* Reações em estado excitado, formações de complexos no estado fundamental, rearranjos moleculares, transferência de energia e colisões.
* Há também quenching aparentes, onde a diminuição da fluorescência se deve a fenômenos triviais como turbidez.
* É estritamente necessário que haja contato entre o quencher e o fluoróforo, o que resulta em aplicações interessantes.
* Oxigênio é um dos quenchers mais bem conhecidos. Ele "quencha" a maior parte dos fluoróforos conhecidos. Dependendo da amostra, é necessário remover oxigênio dissolvido para obter medidas confiáveis dos rendimentos e tempos de vida de fluorescência. O mecanismo ainda é discutido, mas o mais provável é que o oxigênio paramagnético causa um cruzamento intersistema para o estado tripleto que, em solução, são completamente "quenchados" então não se observa fosforescência. Alguns estudos mostram que o quenching por oxigênio ocorre por diversos métodos, como cruzamento, transferência de carga e troca eletrõnica.
* Aminas aromáticas e alifáticas são quenchers bons tb. No caso de antracero e dietilanilina, é formado um complexo de transferência de carga excitado.
* Átomos pesados como iodeto e brometo também fazem quenching. Tricloroetanol e bromobenzeno agem como quenchers colisionais. Alguns halogênios maiores causam uma transição para o estado excitado tripleto, promovidos pelo acoplamento spin-órbita do singleto e o halogênio. E íons brometo, etc?

# Mecanismos de quenching

* Para quenching ocorrer, é necessário contato molecular, onde as nuvens eletrônicas de ambas as moléculas interagem. Essa distância é próxima ao raio de van der Waals das moléculas. Quando o quencher entra em contato com o fluoróforo excitado, o elétron no orbital LU retorna ao estado fundamental, logo o fluoróforo não consegue mais emitir e a energia é dissipada como calor. Dependendo do mecanismo, o quencher pode permanecer no estado fundamental como também pode subir para o estado excitado e depois relaxar.

* Há pelo menos três mecanismos para quenching

1. Cruzamento intersistemas ou o efeito do átomo pesado
2. Troca eletrônica ou interações de Dexter
3. Transferência eletrônica fotoinduzida.

* Cruzamento intersistemas já foi mencionado. Cruza, e depois quencha lentamente, raramente fosforece.

* Troca eletrônica: Há um doador, D e um acceptor, A. O doador possui um elétron excitado no orbital LU. Esse elétrons é transferido para o acceptor, que então transfere um elétron de volta para o doador. O elétrons transferido de volta vem do HO do acceptor, então o acceptor fica num estado excitado. Essa transferência pode ocorrer tanto uma depois da outra como concertadamente.

* Transferência eletrônica fotoinduzida (PET). No PET, um complexo é formado entre o doador eletrônico e o acceptor eletrônico, resultando num Dp+Ap-, e esse complexo pode voltar ao estado fundamental sem emissão, mas em alguns casos uma emissão do exciplex é observada. No final, o elétron é retornado. O fluoróforo pode ser tanto o acceptor quanto o doador.

# FRET. Utilidade para MG? Acho que não.