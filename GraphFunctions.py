def jointplot(x,y):
    return sns.jointplot(x,y,wc1)

def boxplot(x):
    return sns.boxplot(x,data=wc1)

def scatterplot(x,y,c):
    return sns.scatterplot(x,y,data=wc1) and sns.scatterplot(x,c,data=wc1)
    