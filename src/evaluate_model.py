import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_feature_importance(model, features):

    importance = model.feature_importances_

    feature_df = pd.DataFrame({
        'Feature': features,
        'Importance': importance
    })

    feature_df = feature_df.sort_values(by='Importance', ascending=False)

    plt.figure(figsize=(10, 6))
    sns.barplot(x='Importance', y='Feature', data=feature_df)
    plt.title('Feature Importance')
    plt.savefig('../images/feature_importance.png')
    plt.show()