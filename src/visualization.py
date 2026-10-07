# src/visualization.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_binary(df, column, title=None, figsize=(6, 4)):
    
    counts = (
        df[column]
        .value_counts(dropna=False)
        .sort_index()
    )

    total = len(df)
    nulls = df[column].isna().sum()

    if title is None:
        title = column.replace('_', ' ').title()

    plt.figure(figsize=figsize)

    ax = sns.barplot(
        x=counts.index.astype(str),
        y=counts.values
    )

    ax.margins(y=0.15)

    for i, value in enumerate(counts.values):
        percentual = value / total * 100

        ax.text(
            i,
            value,
            f'{value:,}\n({percentual:.1f}%)',
            ha='center',
            va='bottom'
        )

    plt.title(
        f'{title}\n'
        f'N = {total:,} | Nulos = {nulls:,}'
    )

    plt.xlabel(column)
    plt.ylabel('Quantidade')

    plt.tight_layout()
    plt.show()

def plot_numeric(df, column, title=None, figsize=(12, 4), bins=30):

    data = df[column].dropna()

    if title is None:
        title = column.replace('_', ' ').title()

    total = len(df)
    validos = len(data)
    nulls = df[column].isna().sum()

    # Estatísticas
    mean = data.mean()
    q1 = data.quantile(0.25)
    median = data.median()
    q3 = data.quantile(0.75)

    iqr = q3 - q1

    lower_limit = q1 - 1.5 * iqr
    upper_limit = q3 + 1.5 * iqr

    outliers = (
        (data < lower_limit) |
        (data > upper_limit)
    ).sum()

    outliers_pct = outliers / validos * 100

    # Criação dos gráficos
    fig, axes = plt.subplots(
        1,
        2,
        figsize=figsize
    )

    # -------------------------
    # Histograma
    # -------------------------

    sns.histplot(
        data,
        bins=bins,
        kde=True,
        ax=axes[0]
    )

    axes[0].axvline(
        mean,
        color='red',
        linestyle='--',
        label=f'Média: {mean:,.2f}'
    )

    axes[0].axvline(
        median,
        color='green',
        linestyle=':',
        label=f'Mediana: {median:,.2f}'
    )

    axes[0].set_title('Distribuição')
    axes[0].set_xlabel(title)
    axes[0].set_ylabel('Frequência')
    axes[0].legend()

    # -------------------------
    # Boxplot
    # -------------------------

    sns.boxplot(
        x=data,
        ax=axes[1]
    )

    axes[1].axvline(
        mean,
        color='red',
        linestyle='--',
        label=f'Média: {mean:,.2f}'
    )

    axes[1].set_title('Boxplot')
    axes[1].set_xlabel(title)

    # Estatísticas
    stats_text = (
        f'Q1: {q1:,.2f}\n'
        f'Mediana: {median:,.2f}\n'
        f'Q3: {q3:,.2f}\n'
        f'Outliers IQR: {outliers:,} ({outliers_pct:.1f}%)'
    )

    axes[1].text(
        0.98,
        0.95,
        stats_text,
        transform=axes[1].transAxes,
        verticalalignment='top',
        horizontalalignment='right',
        bbox=dict(
            boxstyle='round',
            facecolor='white',
            alpha=0.8
        )
    )

    # -------------------------
    # Título geral
    # -------------------------

    fig.suptitle(
        f'{title}\n'
        f'N = {total:,} | Válidos = {validos:,} | Nulos = {nulls:,}',
        fontsize=14
    )

    plt.tight_layout()

    plt.show()