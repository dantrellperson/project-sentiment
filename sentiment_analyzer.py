import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk


# create datafrane by loading any and all csv files in resources folder using glob, and concatenating them
df = pd.concat(map(pd.read_csv, "resources/*.csv"))


# import english stopwords from nltk
stopwords = nltk.corpus.stopwords.words("english")
