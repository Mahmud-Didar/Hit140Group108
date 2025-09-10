import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
import statsmodels.api as sm


pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.max_rows', None)     # Show all rows 
pd.set_option('display.width', None)        # No line-wrapping
pd.set_option('display.max_colwidth', None) # Show full content in cells

# To load Datasets

dataset1=None
dataset2=None

try:
    dataset1=pd.read_csv("dataset1.csv")
    print("Successfully loaded dataset1.")
except Exception as e:
    print("Error loading dataset1. ",e)

try:
    dataset2=pd.read_csv("dataset2.csv")
    print("\nSuccessfully loaded dataset2. ")
except Exception as e:
    print("Error loading dataset2. ",e)



# Display basic information

if dataset1 is not None:
    print("\nDataset 1: ")
    print(dataset1.head())
else:
    print("Dataset 1 is not loaded, cannot display head(). ")


if dataset2 is not None:
    print("\nDataset 2: ")
    print(dataset2.head())
else:
    print("Dataset 2 is not loaded, cannot display head(). ")


print("\n---------- Dataset 1 Info ----------")
dataset1.info()

print("\n---------- Dataset 1 Summary Statistics (Numberic) ---------- ")
print(dataset1.describe().transpose()) # Transpose for better readability 

print("\n---------- Dataset 2 Info ----------")
dataset2.info()

print("\n---------- Dataset 2 Summary Statistics (Numberic) ---------- ")
print(dataset2.describe().transpose()) # Transpose for better readability 


