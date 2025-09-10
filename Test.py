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