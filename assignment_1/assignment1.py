import pandas as pd

bodyfat2 = pd.read_csv('assignment_1/bodyfat2.csv') # please alter this to your path
bodyfat3 = pd.read_csv('assignment_1/bodyfat3.csv') # please alter this to your path

# Question 1a
print('Question 1a')

# Select columns from neck onwards till wrist (fat present in the body parts)
bodyfat2_compiled = bodyfat2.iloc[:, 5:15]

# Compute the mean, median, and sum, for each individual
bodyfat2_compiled_means = bodyfat2_compiled.mean(1) # 1 for columns
bodyfat2_compiled_medians = bodyfat2_compiled.median(1)
bodyfat2_compiled_sums = bodyfat2_compiled.sum(1)

# Create DataFrames for the top and bottom individuals
top_df = pd.DataFrame({
    'ID': [i for i in range(3)],
    'Mean': bodyfat2_compiled_means.head(3),
    'Median': bodyfat2_compiled_medians.head(3),
    'Sum': bodyfat2_compiled_sums.head(3)
})

bottom_df = pd.DataFrame({
    'ID': [i for i in range(47, 50)],
    'Mean': bodyfat2_compiled_means.tail(3),
    'Median': bodyfat2_compiled_medians.tail(3),
    'Sum': bodyfat2_compiled_sums.tail(3)
})

# Concatenate the DataFrames to fit within the 3 columns
bodyfat2_top_bottom_3 = pd.concat([top_df, bottom_df], ignore_index=True)

print(bodyfat2_top_bottom_3.to_string(header=True, index=False, col_space=10))
print()

# ------------------------------------------------------------------------
# Question 1b
print('Question 1b')
# Compute and store as series
bodyfat2_means = bodyfat2.mean()
bodyfat2_medians = bodyfat2.median()
bodyfat2_sums = bodyfat2.sum()

# Create data frames from the Series
means_df = pd.DataFrame({'feature': bodyfat2.columns, 'mean': bodyfat2_means})
medians_df = pd.DataFrame({'feature': bodyfat2.columns, 'median': bodyfat2_medians})
sums_df = pd.DataFrame({'feature': bodyfat2.columns, 'sum': bodyfat2_sums})

# Merge the data frames based on the 'feature' column
result_df = pd.merge(means_df, medians_df, on='feature')
result_df = pd.merge(result_df, sums_df, on='feature')

print(result_df.to_string(header=True, index=False, col_space=10))
print()

# ------------------------------------------------------------------------
# Question 1c
print('Question 1c')
import scipy.stats

# Compute geometric mean and harmonic mean for each body part
arithmetic_means = bodyfat2.iloc[:, 5:15].mean(axis=0)
geometric_means = scipy.stats.gmean(bodyfat2.iloc[:, 5:15], axis=0)
harmonic_means = scipy.stats.hmean(bodyfat2.iloc[:, 5:15], axis=0)

# Create a DataFrame to store the computed means
means_df = pd.DataFrame({
    'Body Part': bodyfat2.columns[5:15],
    'Arithmetic Mean': arithmetic_means,
    'Geometric Mean': geometric_means,
    'Harmonic Mean': harmonic_means
})

print(means_df.to_string(header=True, index=False, col_space=10))
print()

# ------------------------------------------------------------------------
# Question 2a
print('Question 2a')
# Remove age, weight and height
bodyfat2_without_age_weight_height_cols = bodyfat2.drop(columns=['age', 'weight', 'height'])

# For each feature, and combine them into a single data frame
print("Max and Min values for all features and associated IDs")
bodyfat2_features_max_and_min_values = pd.concat([bodyfat2_without_age_weight_height_cols.max(),
                                                  bodyfat2_without_age_weight_height_cols.idxmax(),
                                                  bodyfat2_without_age_weight_height_cols.min(),
                                                  bodyfat2_without_age_weight_height_cols.idxmin()], axis=1).set_axis(['Max value', 'Max ID', 'Min value', 'Min ID'], axis='columns').rename_axis('Feature')

print(bodyfat2_features_max_and_min_values.to_string(header=True, index=True, col_space=10))
print()

# ------------------------------------------------------------------------
# Question 2b
print('Question 2b')

# Identify individuals appearing more than once under Max ID
max_id_duplicates = bodyfat2_features_max_and_min_values[
    bodyfat2_features_max_and_min_values['Max ID'].duplicated(keep=False)
].drop(columns=['Min value', 'Min ID'])

# Identify individuals appearing more than once under Min ID
min_id_duplicates = bodyfat2_features_max_and_min_values[
    bodyfat2_features_max_and_min_values['Min ID'].duplicated(keep=False)
].drop(columns=['Max value', 'Max ID'])

print("Individuals appearing more than once under Max ID:")
print(max_id_duplicates)
print("\nIndividuals appearing more than once under Min ID:")
print(min_id_duplicates)
print()

# ------------------------------------------------------------------------
# Question 3
print('Question 3')
bodyfat2_stds = bodyfat2.std()
print("For each feature, the more values that lie within 10% of standard deviation from the centre, the tighter the spread")

within_10_percent_std_of_means = (bodyfat2 >= bodyfat2_means - 0.1 * bodyfat2_stds) & (bodyfat2 <= bodyfat2_means + 0.1 * bodyfat2_stds)
within_10_percent_std_of_medians = (bodyfat2 >= bodyfat2_medians - 0.1 * bodyfat2_stds) & (bodyfat2 <= bodyfat2_medians + 0.1 * bodyfat2_stds)

num_within_10_percent_std_of_means = within_10_percent_std_of_means.sum()
num_within_10_percent_std_of_medians = within_10_percent_std_of_medians.sum()

result_df = pd.DataFrame({
    'feature': bodyfat2.columns,  # Select the desired feature columns
    'number_mean': num_within_10_percent_std_of_means,  # Select the corresponding counts
    'number_median': num_within_10_percent_std_of_medians  # Select the corresponding counts
})

print(result_df.to_string(index=False))
print()

# ------------------------------------------------------------------------
# Question 4
print('Question 4')
print('The higher the number of missing data, the more incomplete the data for that particular feature')
print('Possible remedy: Features with too many missing values should be dropped')
print(pd.isna(bodyfat3).sum().to_string())
print()

# ------------------------------------------------------------------------
# Question 5a
print('Question 5a')
# Calculate the means of the available values in bodyfat3 dataset
bodyfat3_means = bodyfat3.mean()

# Fill missing values in bodyfat3 dataset with the calculated means
filled_data = bodyfat3.fillna(value=bodyfat3_means)

# Calculate means again, although they should be similar to bodyfat3_means
filled_data_means = filled_data.mean()

# Calculate the absolute difference in mean values for each feature
mean_difference = abs(bodyfat2_means - filled_data_means)

print("Absolute difference in mean values for each feature compared to the original mean from bodyfat2 dataset:")
print(mean_difference.to_string())
print()

# ------------------------------------------------------------------------
# Question 5b
print('Question 5b')
# Calculate the medians of the available values in bodyfat3 dataset
bodyfat3_medians = bodyfat3.median()

# Fill missing values in bodyfat3 dataset with the calculated medians
filled_data_with_medians = bodyfat3.fillna(value=bodyfat3_medians)

# Calculate medians again, although they should be similar to bodyfat3_medians
filled_data_with_medians_medians = filled_data_with_medians.median()

# Calculate the absolute difference in median values for each feature
median_difference = abs(bodyfat2_medians - filled_data_with_medians_medians)

print("Absolute difference in median values for each feature compared to the original median from bodyfat2 dataset:")
print(median_difference.to_string())
print()

# ------------------------------------------------------------------------
# Question 6a
print('Question 6a')
# Apply normalisation formula provided
bodyfat2_normalized = (bodyfat2 - bodyfat2_means) / bodyfat2_stds
print('Normalised features for first 3 individuals:')
print(bodyfat2_normalized.head(3).to_string())
print('Normalised features for last 3 individuals:')
print(bodyfat2_normalized.tail(3).to_string())
print()

# ------------------------------------------------------------------------
# Question 6b
print('Question 6b')
bodyfat2_normalized_means = bodyfat2_normalized.mean()

# Count the number of people who are above average for each feature
bodyfat2_normalized_greater_than_means_count = (bodyfat2_normalized > bodyfat2_normalized_means).sum()

print('Individuals above average for each feature:')
print(bodyfat2_normalized_greater_than_means_count.to_string())
