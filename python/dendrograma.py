from scipy.cluster.hierarchy import dendrogram, linkage, set_link_color_palette
labels = dados_ME['Composto'] + ' ' + dados_ME['Concentração (% m/m)'].apply(str) + '%'
labels[0] = 'Água'

linked = linkage(X_AS, method='complete', metric='euclidean')
set_link_color_palette(['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6'])

plt.figure(figsize=(9, 9))  
dn = dendrogram(linked, orientation='right', labels=labels.tolist(), show_leaf_counts=True, color_threshold=2.5, above_threshold_color='lightSlateGray')

ax = plt.gca()
ax.set_xlim(0,4.9)
xticks = ax.get_xticks()
ax.set_xticks( np.linspace(0, 4.8, 6) )
xticklabels = np.arange(1, -0.2, -0.2)
xticklabels = [f'{i:.1f}'.replace('.',',') for i in xticklabels]
ax.set_xticklabels(xticklabels)

ax.axvline(x=2.5, color='k', ls='--')
yticklabels = ax.get_yticklabels()
for lab in yticklabels:
    lab.set_fontsize(12)
    comp = lab.get_text().split(' ')[0]
    lab.set_color(Cores[comp])
ax.grid(axis='x')