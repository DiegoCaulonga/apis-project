def group(x):
    return pd.DataFrame(wc1[wc1["FIFA code"]==x]["Group"])

def wins(x):
    return pd.DataFrame(wc1[wc1["FIFA code"]==x]["Wins"])

def draws(x):
    return pd.DataFrame(wc1[wc1["FIFA code"]==x]["Draws"])

def losses(x):
    return pd.DataFrame(wc1[wc1["FIFA code"]==x]["Losses"])

def goals(x):
     return pd.DataFrame(wc1[wc1["FIFA code"]==x]["Goals Scored"])

def received(x):
    return pd.DataFrame(wc1[wc1["FIFA code"]==x]["Goals Scored"])

def groupgoals(x):
    return wc1[wc1["Group"]==x]["Goals Scored"].sum()

def groupfouls(x):
    return wc1[wc1["Group"]==x]["Total Fouls"].sum()




