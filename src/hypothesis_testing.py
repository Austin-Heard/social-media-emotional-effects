# Unfinished, will return if time allows, focus is on getting Regressions completed
def test_hypothesis(df=object, columns=list, categorial=bool):
    cat_unique = []
    if categorial:
        cat_col = columns[0]
        cat_unique = df[cat_col].unique()

        cat_names_dict = {}
        for i in range(0, len(cat_unique)):
            cat_names_dict[cat_unique[i]] = i+1

        for value in cat_unique:
            # Assign to temp df and replace any emotion values that are not the currently selected with 0
            subset_df = df.copy()
            subset_df.loc[subset_df[cat_col] != value, 'Dominant_Emotion'] = 0
            subset_df.loc[subset_df[cat_col] == value, 'Dominant_Emotion'] = 1

                # Get dict key name for display later
            key_name = ""
            for key in cat_names_dict:
                if cat_names_dict[key] == value:
                    key_name = key

            # Check if there's enough data and variability
            if subset_df.shape[0] > 1:
                daily_usage_time = subset_df['Daily_Usage_Time (minutes)']
                
                # Make sure daily usage time is not all repeat or assumed values
                if daily_usage_time.nunique() > 1:
                    corr, p_val = pearsonr(daily_usage_time, subset_df[cat_col])
                    print(f'Value: {key_name}')
                    print(f'Correlation coefficient: {corr}')
                    print(f'P-value: {p_val}')
                else:
                    print(f'Value: {key_name} - {columns[2]} has no variance (constant values).')
            else:
                print(f'Value: {key_name} - Not enough data points.')
            print('-' * 30)
    pass

if __name__ == "__main__":
    pass