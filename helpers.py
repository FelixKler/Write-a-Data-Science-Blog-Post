import pandas as pd

def create_bins(df, column, bins, labels):
    '''
    create bins for desired dataframe with continous values
    '''
    new_df = pd.DataFrame(pd.cut(df[column],
                          bins=bins,
                          labels=labels,
                          precision=0).value_counts()).reset_index()
    new_df.columns=['category', 'quantity']
    new_df.sort_values(by=['category'], inplace=True)
    
    return new_df


def set_visuals(ax):
    '''
    set some style options to ax
    '''
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_edgecolor((0.3,0.3,0.3))
    ax.spines['bottom'].set_edgecolor((0.3,0.3,0.3))
    ax.tick_params(labelcolor=(0.3,0.3,0.3), grid_color=(0.3,0.3,0.3))