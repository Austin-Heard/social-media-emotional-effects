def label_matching(labels=list, graph_size=int):
    # Check graph size vs label list size 
    if graph_size == len(labels):
        plt.xticks(ticks=np.arange(len(labels)) + 0.5, labels=labels, rotation=45, ha='right')
        plt.yticks(ticks=np.arange(len(labels)) + 0.5, labels=labels, rotation=0)
    else:
        print("The number of custom labels does not match the number of columns/rows in the correlation matrix.")
        print(f"Number provided: {len(labels)}")
        print(f"Length required: {graph_size}")

def dummy_df_corr(df=object, dummy_columns=list):
    # Get dummies from specified columns and return the correlations of the entire df
    dummy_df = pd.get_dummies(df, dummy_columns)
    return dummy_df.corr()

def make_corr_heatmap(df=object, columns=list, labels=list, saveto=str):
    # Retrieve the correlation matrix
    matrix_df = dummy_df_corr(df, columns)

    # Mask upper portion of repetitive data 
    mask = np.triu(matrix_df)

    # Create heatmap with or without specified labels, including annotation overlay
    sns.heatmap(matrix_df, annot=True, cmap='crest', mask=mask, annot_kws={"size": 7});
    if labels:
        label_matching(labels, matrix_df.shape[0])

    # Save and display the image
    if saveto:
        plt.savefig(f'../img/{saveto}.png', bbox_inches='tight')
    else:
        plt.savefig(f'../img/Unnamed_Heatmap.png', bbox_inches='tight')

    plt.show()

def make_cat_from_int(df=object, column=str, iterator=int):
    # Create bins starting at 0, iterating at the user specified interval (default is 1)
    bins = range(0, df[column].max()+iterator, iterator)

    # Create labels based on the bins created
    labels = [f'{i}-{i+5}' for i in bins[:-1]]

    # Replace the categorized column with the new labels defined by the bins
    df[column] = pd.cut(df[column], bins=bins, labels=labels, right=False)

    # Return the entire dataframe
    return df

def make_stack(df=object, cat=bool, iterator=1, x_column=str, color=str, overlay=bool, saveto=str):
    # Identify given columns
    columns = list(df.columns)

    # Check if user wants to make categories
    if cat:
        df = make_cat_from_int(df, x_column, iterator)

    # Group by categorized column and count the amount of entries, filtering out any that are empty
    counts = df.groupby(columns).size().unstack()
    counts = counts.loc[(counts.sum(axis=1) > 0)]

    # Setting the user's color palette
    color_palette = sns.set_palette(color)

    # Display the count in a stacked bar chart
    ax = counts.plot(kind='bar', stacked=True, figsize=(8, 7), color=color_palette)
    plt.xlabel(f'{x_column}')
    plt.ylabel('Number of Entries')
    plt.title(f'Number of Entries by {columns[0]} in Each {columns[1]}')

    if overlay:
        # Display the counts over each segment
        for w in counts.index:
            for z in counts.columns:
                count = counts.at[w, z]
                if count > 0:
                    x = counts.index.get_loc(w)
                    y = counts.loc[w].cumsum().shift(1).fillna(0)[z] + count / 2
                    ax.text(x, y, str(int(count)), ha='center', va='center', color='white')
    
    # Save and display image
    if saveto:
        plt.savefig(f'../img/{saveto}.png', bbox_inches='tight')
    else:
        plt.savefig('../img/Unnamed_Stacked_Bar_Chart.png', bbox_inches='tight')

    plt.show()

def categorial_count_bar(db, cat_col, colors):
    default_colors = ['olive', 'orange', 'purple', 'brown', 'indigo', 'violet']
    if colors:
        pass
    else:
        values = db[cat_col].unique()
        while len(values) > len(default_colors):
            default_colors.append(default_colors)
        colors = [default_colors[i] for i in range(len(values))]

    db[cat_col].value_counts().plot(kind='bar', figsize=(7, 7), color=colors)
    plt.ylabel(f"{cat_col} Total Counts")
    plt.xlabel(f"{cat_col} Reported")
    plt.xticks(rotation=45)
    plt.savefig('../img/Category_Totals_Bar.png', bbox_inches='tight')
    plt.show() 

if __name__ == "main":
    # Import only if called directly from the file
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    import argparse

    # Room here for argparse arguements later
    pass