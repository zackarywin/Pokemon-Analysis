#import modules
import numpy as np
import pandas as pd
import matplotlib as plt

#import csv
poke = pd.read_csv('Pokemon.csv')
print(poke.head())

battles = pd.read_csv('pokemon-battles.csv')
print(battles.head())

#exploration and visualization
print(poke.describe())

