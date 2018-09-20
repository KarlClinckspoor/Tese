    resultados_tot.write(f'{bom1.nome[:-4].replace(" ", ";")};{bom1.ponto};{bom2.ponto};'
                      f'{bom1.a};{bom1.aerr};'
                      f'{bom1.b};{bom1.berr};'
                      f'{bom1.c};{bom1.cerr};'
                      f'{bom1.R2};{media1l};{stdmedia1l};'
                      f'{bom2.a};{bom2.aerr};'
                      f'{bom2.b};{bom2.berr};'
                      f'{bom2.c};{bom2.cerr};'
                      f'{bom2.R2};{media2l};{stdmedia2l};{g1_1hz};{g2_1hz}\n')
    
    ##### Plotando os gráficos dos ajustes ######
    plt.figure()
    plt.plot(x, y1, 'ro', label="G'")
    plt.plot(x[:bom1.ponto], exp(x[:bom1.ponto], bom1.a, bom1.b, bom1.c) , 'r-', label="G' exp")
    plt.plot(x[:bom1l.ponto], linear(x[:bom1l.ponto], bom1l.a, bom1l.b), 'm--', label="G' lin")

    plt.plot(x, y2, 'bo', label="G''")
    plt.plot(x[:bom2.ponto], exp(x[:bom2.ponto], bom2.a, bom2.b, bom2.c) , 'b-', label="G'' exp")
    plt.plot(x[:bom2l.ponto], linear(x[:bom2l.ponto], bom2l.a, bom2l.b), 'm--', label="G'' lin")
    
    plt.xlabel('log(f/Hz)')
    plt.ylabel("log(G', G''/Pa)")

    try:
        plt.axvline(x[bom1.ponto-1], linestyle='--', color='r')
        plt.axvline(x[bom2.ponto-1], linestyle='--', color='b')
    except:
        print(x)
        break
    plt.legend(ncol=2)
    plt.title(file[:-4])
    plt.savefig(f'./ajustes_exp/{file[:-4]}.png')
    
    ####### Excluindo a figura para liberar memória ########
    plt.gcf().clf()
    plt.close()
    del df
    gc.collect()
    
    print(f'Tratado arquivo {j+1} de {len(files)}\r', end='')
    
resultados1.close()
resultados2.close()
resultados_tot.close()
log.close()