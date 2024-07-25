def linear_regression(df=str, X_col=str, y_col=str):
    # Initialize the df
    df = pd.read_csv(df)

    # Set the X and Y
    X = df[X_col]
    y = df[y_col]

    # Performing linear regression
    slope, intercept, r_value, p_value, std_err = linregress(X, y)

    # Output the regression results
    print(f"Slope: {slope}")
    print(f"Intercept: {intercept}")
    print(f"R-squared: {r_value**2}")
    print(f"P-value: {p_value}")
    print(f"Standard Error: {std_err}")

    # Predicting using the regression model
    y_pred = intercept + slope * X
    
    # Scatter plot of the data points
    plt.scatter(X, y, color='blue', label='Data points')

    # Regression line
    plt.plot(X, y_pred, color='red', label='Regression line')

    # Adding labels and title
    plt.xlabel(X_col)
    plt.ylabel(y_col)
    plt.title(f'Linear Regression: {X_col} vs {y_col}')
    plt.legend()

    # Save and show the plot
    plt.savefig(f'../img/{X_col}_vs_{y_col}_linreg.png', bbox_inches='tight')
    plt.show()

def logistical_regression(df=str, y_col=str, X_list=list, multinomial=bool, y_need_cat=bool, y_cat_param=int):
    # Initialize the df
    df = pd.read_csv(df)
    
    # If set true, categorize the target var by user defined var
    if y_need_cat:
        df[y_col] = np.where(df[y_col] > y_cat_param, 1, 0)

    # If multinomial, assume the categorials are not dummified yet
    if multinomial:
        X = df
        y = df[y_col]

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create the multinomial model and train
        model = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=10000)
        model.fit(X_train, y_train)

        # Model predictions
        y_pred = model.predict(X_test)
        y_pred_prob = model.predict_proba(X_test)

    # Else, assume all categorials have been dummified already
    else:
        # Features and target variable
        X = df.drop(columns=[X_list])
        y = df[y_col]

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create the binomial model and train
        model = LogisticRegression(max_iter=1000)
        model.fit(X_train, y_train)

        # Model predictions
        y_pred = model.predict(X_test)
        y_prob = model.predict_proba(X_test)[:, 1]

        # Accuracy evaluation for binomial
        accuracy = accuracy_score(y_test, y_pred)

        # Print accuracy metric
        print(f"Accuracy: {accuracy}")

    # Model evaluation
    conf_matrix = confusion_matrix(y_test, y_pred)

    # Print evaluation metrics
    print("Confusion Matrix:")
    print(conf_matrix)

    # Initialize our visualization
    plt.figure()

    # Multinomial requires looping through each ROC
    if multinomial:
        # Binarize the output for ROC curve plotting
        y_test_bin = label_binarize(y_test, classes=X_list)

        # Plot ROC curves for each class
        plt.figure()
        for i in range(y_test_bin.shape[1]):
            fpr, tpr, _ = roc_curve(y_test_bin[:, i], y_pred_prob[:, i])
            roc_auc = auc(fpr, tpr)
            plt.plot(fpr, tpr, lw=2, label=f'{X_list[i]} (area = {roc_auc:.2f})')

    else:
        # Plotting ROC curve
        fpr, tpr, thresholds = roc_curve(y_test, y_prob)
        roc_auc = auc(fpr, tpr)

    plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc="lower right")
    plt.savefig('../img/df_logistical_regression.png', bbox_inches='tight')
    plt.show()

if __name__ == "__main__":

    # Imports
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.stats import linregress
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score, confusion_matrix, roc_curve, auc
    from sklearn.preprocessing import label_binarize
    import argparse