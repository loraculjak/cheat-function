#Q3.2P.9
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

def cheat (x):
    if x == "3.2P.5":
        print(
        "my_data = np.random.normal(loc=100, scale=10, size=1000) \n" 
        "def my_plots(x):"
        "if x == ""yay"":"
        "plt.violinplot(my_data)"
        "elif x== ""eww"":"
        "lt.plot(my_data)"
        "else:"
        "print(""You need to write yay or eww""))")
    elif x == "Q3.2P.4":
        print(
            "plt.subplot(1, 2, 1) \n "
              "heatmap = sns.heatmap(data.corr())"
              "plt.subplot(1, 2, 2)"
              "kdeplot = sns.kdeplot(x=data.alcohol, y=data.color_intensity)"
              "plt.tight_layout()")
    elif x == "Q3.2P.3":
        print("from sklearn.datasets import load_wine \n"
              "wine = load_wine()"
              "data=pd.DataFrame(data=np.c_[wine['data'],"
              "wine['target']],columns=wine['feature_names']+['target']) "
              "sns.regplot(x= data.malic_acid, y=data.alcohol)"
              "plt.xlabel('malic acid', fontsize=25)"
              "plt.ylabel('alcohol', fontsize=25)")
    elif x == "Q3.2P.2":
        print(" titanic = pd.read_csv" 
              "('https://raw.githubusercontent.com/hannesrosenbusch/schiphol_class/master/titanic.csv') \n"
              "titanic.head()"
              "titanic = sns.load_dataset('titanic').loc[:, ['sex', 'survived']]"
              "titanic_p = titanic.pivot_table(index='sex', columns=['survived'], aggfunc=len) #pivoting table"
              "titanic_p"
              "titanic_p.plot(kind='bar', stacked=True, ylabel='Counts', xlabel='Gender',"
              "title='Survival Status Count by Gender', rot=0))")
    else: print("Don't cheat!")

cheat("Q3.2P.11")