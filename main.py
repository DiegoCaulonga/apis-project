
WorldCup = pd.read_csv("Output/wc1.csv")
import requests
import numpy as np
import collections
from pandas.io.json import json_normalize
import regex as re
import seaborn as sns
import matplotlib.pyplot as plt
import argparse



parser=argparse.ArgumentParser(description="group of the team")
parser.add_argument("-g", "--group", type=str, help="code of the team")
args=parser.parse_args()

def group(x):
    return pd.DataFrame(wc1[wc1["FIFA code"]==x]["Group"])

if __name__ == "__main__":
     print (group(args.group))   




parser=argparse.ArgumentParser(description="goals scored by the team")
parser.add_argument("-w", "--wins", type=str, help="code of the team")
args=parser.parse_args()

def wins(x):
    return pd.DataFrame(wc1[wc1["FIFA code"]==x]["Wins"])

if __name__ == "__main__":
     print (group(args.group))  






parser=argparse.ArgumentParser(description="total goals scored in the entire group matches")
parser.add_argument("-t", "--total", type=str, help="code of the Group")
args=parser.parse_args()

def groupgoals(x):
    return wc1[wc1["Group"]==x]["Goals Scored"].sum()

if __name__ == "__main__":
     print (group(args.total))  







parser=argparse.ArgumentParser(description="Boxplot of the column")
parser.add_argument("-b", "--boxplot", type=str, help="name of the column")
args=parser.parse_args()

def boxplot(x):
    return sns.boxplot(x,data=wc1)

if __name__ == "__main__":
     print (group(args.boxplot))  




parser=argparse.ArgumentParser(description="Jointplot of two columns against other column")
parser.add_argument("-W", "--winratio", type=str, help="Win Ratio column")
parser.add_argument("-t", "--ontarget", type=str, help="Total Shots on Target")
parser.add_argument("-b", "--blocked", type=str, help="Total Shots Blocked")
args=parser.parse_args()

def scatterplot(x,y,c):
    return sns.scatterplot(x,y,data=wc1) and sns.scatterplot(x,c,data=wc1)

if __name__ == "__main__":
     print (group(args.winratio,args.ontarget,args.blocked))  








     