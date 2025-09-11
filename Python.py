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





# -------------------------------------
# CrossTab
# -------------------------------------


# Cross tab for reward vs risk
reward_risk_ct = pd.crosstab(dataset1['risk'], dataset1['reward'], normalize="index")
print("\n Crosstab for Risk vs Reward")
print(reward_risk_ct.transpose())



# -------------------------------------
# T-test
# -------------------------------------

# T-test: seconds_after_rat_arrival
risk_takers = dataset1[dataset1['risk'] == 1]['seconds_after_rat_arrival'].dropna()
risk_avoiders = dataset1[dataset1['risk'] == 0]['seconds_after_rat_arrival'].dropna()

# Perform independent samples T-Test
t_stat, p_value = ttest_ind(risk_takers, risk_avoiders, equal_var=False)

# Display results
print("\nIndependent samples T-Test-1: seconds_after_rat_arrival ")
print(f"Risk-Takers (n={len(risk_takers)}), Risk-Avoiders (n={len(risk_avoiders)})")
print(f"T-statistic ={t_stat:.3f}")
print(f"P_value = {p_value:.4f}")

#Condition
alpha=0.05
if p_value < alpha :
    print("Result: reject null hypothesis. ")
else:
    print("Result: fail to reject null hypothesis. ")


# Define the time periods based on hours after sunset
dataset2['time_period']=pd.cut(dataset2['hours_after_sunset'],bins=[0, 2, 6], labels=['early', 'late'])

# Extract rat_minutes for each period
early_rats = dataset2[dataset2['time_period']=='early']['rat_minutes'].dropna()
late_rats = dataset2[dataset2['time_period'] == 'late']['rat_minutes'].dropna()

t_stat, p_value = ttest_ind(early_rats, late_rats, equal_var=False)

# Display the results
print("\n T-Test-2: rat_minutes: Early vs Late Night")
print(f"Early night  (n = {len(early_rats)}): Mean = {early_rats.mean():.2f}")
print(f"Late night   (n = {len(late_rats)}): Mean = {late_rats.mean():.2f}")
print(f"T-statistic = {t_stat:.3f}")
print(f"P-value     = {p_value:.4f}")

# Condition
alpha = 0.05
if p_value < alpha:
    print("Result: Reject null hypothesis. ")
else:
    print("Result: Fail to reject null hypothesis. ")


# -------------------------------------
# Visualizations
# -------------------------------------

# Plot: Landing times after sunset
plt.figure()
sns.histplot(dataset1['hours_after_sunset'], kde=True)
plt.title('Distribution of bat Landing After Sunset')
plt.xlabel('Hours After Sunset')
plt.ylabel('No. of bats landing ')

# Scatter: Food availability vs rat presence
plt.figure()
sns.scatterplot(x='rat_minutes', y='food_availability', data=dataset2)
plt.title('Food Availability vs Rat Presence')
plt.xlabel('Rat Minutes')
plt.ylabel('Food Availability')

# Scatter: Bat landings vs rat minutes
plt.figure()
sns.scatterplot(x='rat_minutes', y='bat_landing_number', data=dataset2)
plt.title('Bat Landings vs Rat Presence')
plt.xlabel('Rat Minutes')
plt.ylabel('Bat Landings')

# Proportion of risk-taking by season
season_risk = pd.crosstab(dataset1['season'], dataset1['risk'], normalize='index')

# Stacked bar plot for risk-taking proportion by season
season_risk.plot(kind='bar', stacked=True, colormap='viridis')
plt.title("Proportion of Risk-Taking by Season")
plt.ylabel("Proportion")
plt.xlabel("Season")
plt.legend(title="Risk Behavior (0 = Avoid, 1 = Take)", loc='upper right')
plt.tight_layout()