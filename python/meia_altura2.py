    # ... continuação
    fig, ax = plt.subplots(1, 1, figsize=(9,6))
    
    h1 = ax.plot(abaixo['T'], abaixo['Q'], label='Aquecimento')
    h2 = ax.plot(acima['T'], acima['Q'], label='Resfriamento')
    ax.axhline(0, **dict_line)
    ax.text(x_pico_abaixo, y_pico_abaixo, 'x', **dict_text)
    ax.text(x_pico_acima, y_pico_acima, 'x', **dict_text)

    ax.axhline(meiaaltura_abaixo, **dict_line2)
    ax.axhline(meiaaltura_acima, **dict_line2)

    ax.plot(interesse_abaixo['T'], interesse_abaixo['Q'], linestyle='--', linewidth=3, label=None)
    ax.plot(interesse_acima['T'], interesse_acima['Q'], linestyle='--', linewidth=3, label=None)

    ax.text(primeiro_abaixo['T'], primeiro_abaixo['Q'], 'x', **dict_text)
    ax.text(primeiro_acima['T'], primeiro_acima['Q'], 'x', **dict_text)
    ax.text(ultimo_abaixo['T'], ultimo_abaixo['Q'], 'x', **dict_text)
    ax.text(ultimo_acima['T'], ultimo_acima['Q'], 'x', **dict_text)
    
    ax.set(xlabel='T/°C', ylabel='Fluxo de calor/W.g$^{-1}-$ linha base')
    ax.set_title(arquivo[:-4], loc='right')
    
    largura_meia_abaixo = ultimo_abaixo['T'] - primeiro_abaixo['T']
    largura_meia_acima = primeiro_acima['T'] - ultimo_acima['T']
    ax.legend([*h1, *h2], ['Aquecimento', 'Resfriamento'])
    print(f'Para a amostra {arquivo}, a largura a meia altura da subida é '
          f'{largura_meia_abaixo} e da descida é {largura_meia_acima}')
    if len(glob.glob('meias_alturas.txt')) == 0:
        fhand = open('meias_alturas.txt', 'w')
        fhand.write('Amostra;aquecimento;resfriamento\n')
    else:
        fhand = open('meias_alturas.txt', 'a')
    
    fhand.write(f'{arquivo};{largura_meia_abaixo};{largura_meia_acima}\n')
    fig.savefig(f'{arquivo[:-4] + "_meia_altura.png"}', dpi=150)
    fhand.close()