# Add in validation function making sure all columns have set, pre-defined answers for algorithmic learning


# Function identifying if the value can be converted into a integer or not
def can_convert_to_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
    
def cleaner(df=object, ml=bool):

    # Dropping any rows without full information, given how few columns there are, each value is important to have
    # Not many ways to fill in missing information accurately given many contributing factors
    df.dropna(inplace=True)

    # Condition to identify rows where values need to be swapped using above function
    condition = df.apply(lambda row: can_convert_to_int(row['Gender']), axis=1)

    # Using the specified condition, swap the values into the proper column
    df.loc[condition, ['Age', 'Gender']] = df.loc[condition, ['Gender', 'Age']].values

    # Remove the user_id column as it's only caused problems and is not helpful
    df.drop("User_ID", axis=1, inplace=True)

    # Check if dummy needs to be applied for categorial vars
    if ml:
        # Getting dummies for all categorial variables
        df = pd.get_dummies(df, columns=["Gender", "Platform", "Dominant_Emotion"])

    return df

# Function called to begin cleaning
def initial_clean(dataframe=str, output=str, split=bool, ml=bool):
    # Set csv file path to a pandas db
    df = pd.read_csv(dataframe)

    # Check if output was specified
    if output:
        pass
    else:
        output = os.path.dirname(dataframe)

    # Check if data needs split for train/test
    if split:
        # Split into train and test data
        train, test = train_test_split(df, test_size=0.2)

        # Clean the dataframes
        train_df = cleaner(train, ml)
        test_df = cleaner(test, ml)

        # Save the dataframes to the specified output as their respective files
        train_df.to_csv(f'{output}/clean_train.csv', index=False)
        test_df.to_csv(f'{output}/clean_train.csv', index=False)
    
    else: # If data doesn't need split, clean the df and save it to a generic csv
        df = cleaner(df, ml)
        df.to_csv(f'{output}/clean.csv', index=False)

if __name__ == '__main__':
    import argparse
    import pandas as pd
    import os
    from sklearn.model_selection import train_test_split
    parser = argparse.ArgumentParser(description="Clean a given dataset for social media study")
    parser.add_argument("db", type=str, help="the relative file path to the csv to be cleaned")  # Arguements
    parser.add_argument("ml", type=bool, nargs='?', const=False, help="Set false by default, true if used to train machine learning and need split categorial vars.")
    parser.add_argument("out", type=str, nargs='?', const="", help="the relative file path to the cleaned csv output")
    parser.add_argument("split", type=bool, nargs='?', const=False, help="Set false by default, true if data needs split.\n False if data already split.")
 
    args = parser.parse_args()  # Parses the arguements given into variables

    initial_clean(args.db, args.out, args.split, args.ml)