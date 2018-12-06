import glob
TR_dados = glob.glob('TR*dado*')
TR_ajustes = glob.glob('TR*ajuste*')
TR_dados.sort()
TR_ajustes.sort()

print(TR_dados)
print(TR_ajustes)

parte1 = r"""
\begin{figure}[h]
    \begin{subfigure}[t]{0.5\textwidth}
        \centering
        \includegraphics[width=\textwidth]{imagens/saxs/"""
        
parte2 = r"""}
        \caption{}
        \label{fig:saxs_tr_}
    \end{subfigure}%
    \begin{subfigure}[t]{0.5\textwidth}
        \centering
        \includegraphics[width=\textwidth]{imagens/saxs/"""

parte3 = r"""}
        \caption{}
        \label{fig:saxs_tr_}
    \end{subfigure}
    \caption{}
    \label{fig:}
\end{figure} 
"""

for dado, ajuste in zip(TR_dados, TR_ajustes):
    with open('figuras_tr_juntas.tex', 'a') as f:
        f.write(parte1 + dado + parte2 + ajuste + parte3)
