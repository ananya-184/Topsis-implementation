import pandas as pd
print(pd.__version__)



# Extract the data matrix (excluding the first column)
d = mydata.iloc[:, 1:].to_numpy()

# Weights and ideal/anti-ideal solutions
w = np.array([1, 1, 1, 1])
i = np.array(["+", "+", "-", "+"])

# Calculate ideal and anti-ideal distances
ideal_distances = np.sqrt(np.sum((d - np.max(d, axis=0))**2, axis=1))
anti_ideal_distances = np.sqrt(np.sum((d - np.min(d, axis=0))**2, axis=1))

# Calculate TOPSIS scores
topsis_scores = ideal_distances / (ideal_distances + anti_ideal_distances)

# Calculate ranks
ranks = np.argsort(topsis_scores)[::-1] + 1

# Combine data with TOPSIS score and rank
combined_data = pd.DataFrame(np.hstack((mydata.values, topsis_scores[:, None], ranks[:, None])),
                             columns=list(mydata.columns) + ['Topsis Score', 'Rank'])

# Save the result to a CSV file
combined_data.to_csv('topsis_results.csv', index=False)

