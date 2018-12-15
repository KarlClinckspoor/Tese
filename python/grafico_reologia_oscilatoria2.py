    if i not in valid_is: # Remover esta condição para gerar todas as imagens
        continue

    y_tau_elast = tau(tau_elast, omega, 0, t)
    y_tau_visc = tau(tau_visc, omega, -np.pi/2, t)
    y_tau_tot = y_tau_elast + y_tau_visc
    
    ax4.set_title(title)
    
    ax1.plot(t, y_gamma, color='purple', label=r'$\gamma$')
    ax4.plot(t, y_tau_tot, color='k', label=r'$\tau_{tot}$')
    ax4.plot(t, y_tau_elast, color='blue', label=r'$\tau_{elast}$', linestyle='--')
    ax4.plot(t, y_tau_visc, color='green', label=r'$\tau_{visc}$', linestyle='--')
    
    ax1.set_ylabel(r'$\gamma$')
    
    ax4.set_ylabel(r'$\tau$')
    ax4.set_xlabel('t')
    ax4.axhline(y=0, linestyle='--', c='red')
    ax4.axvline(x= 5 * np.pi/(2 * omega), linestyle='--', c='red')
    ax4.set_xlim(3 * np.pi/(2 * omega), 7 * np.pi/(2 * omega))
    ax4.set_ylim(-1.5, 1.5)

    zeros = 0
    for j, val in enumerate(y_tau_tot):
        try:
            if y_tau_tot[j] > 0 and y_tau_tot[j+1] < 0:
                zeros = (t[j] + t[j+1])/2
        except:
            pass
        
    ax4.axvline(x=zeros, linestyle='--', c='red', ymax = 0.5)
    if i > 4 and i < 196:
        ax4.arrow(5 * np.pi/(2 * omega), -tau0/2, -(5 * np.pi/(2 * omega) - zeros) + 0.01, 
                  0, head_width=0.01, head_length=0.01, fc='k', ec='k')
        ax4.arrow(-tau0/2, 5 * np.pi/(2 * omega), -(5 * np.pi/(2 * omega) - zeros) + 0.01, 
                  0, head_width=0.01, head_length=0.01, fc='k', ec='k')
        textpos = ((5 * np.pi/(2 * omega)) + (5 * np.pi/(2 * omega) + -(5 * np.pi/(2 * omega) - zeros) + 0.01))/2
        ax4.text(textpos, 4*(-tau0/6), r'$\frac{\theta}{\omega}$', horizontalalignment='center', verticalalignment='center')
    
    lines = (*ax1.get_lines(), *ax4.get_lines()[0:3])
    labels = [i.get_label() for i in lines]
    fig.legend(lines, labels, loc=(0.62, 0.59), fontsize='small')
    
    framenum = f'frame{i:04d}'
    destpath = os.path.join(os.getcwd(), framenum)
    fig.savefig(destpath+'.png')
    
    ax4.clear()
    ax1.clear()