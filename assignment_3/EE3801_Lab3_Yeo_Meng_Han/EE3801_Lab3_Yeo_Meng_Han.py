import pandas as pd
import sys # Question 2g

# Question 2
print("Question 2")
# Question 2a - creating function with 3 inputs
def lab3(csv_file, item, element):
    # Question 2b - reading the new csv file and turning into dataframe
    try:
        df = pd.read_csv(csv_file, encoding="unicode_escape")
        # print(df) # debug

        # Question 2c - df that filter for 'item' and 'element'
        filtered_df = df[(df['Item'] == item) & (df['Element'] == element)]
        # display(filtered_df) # debug

        # Question 2d - list countries that has nan as values
        countries_with_nan = filtered_df[filtered_df['Value'].isna()]['Area'].drop_duplicates()
        print("List of each country from filtered_df with NAN values:")
        print(countries_with_nan.to_frame().to_string(index=False))

        # Question 2e
        # Removing rows with NaN values in the 'Value' column
        filtered_df = filtered_df[~filtered_df['Area'].isin(countries_with_nan)]

        # for each element / item, find the largest value and return the year

        # Finding the year with the maximum value and the median value
        output_df = filtered_df.groupby('Area').agg(
            max_value=('Value', 'max'),
            median_value=('Value', 'median')
        ).reset_index()

        max_years = filtered_df.loc[filtered_df.groupby('Area')['Value'].idxmax()]['Year'].reset_index(drop=True)
        output_df['max_year'] = max_years
        output_df = output_df[['Area', 'max_year', 'max_value', 'median_value']]
        output_df = output_df.reset_index().rename(columns={'max_year': 'Year', 'max_value': 'Maximum Values', 'median_value': 'Median'})

        # Question 2f: save df with file name ‘output_<Item>_<Element>.csv’.
        output_csv_filename = f"output_{item.replace(' ', '_')}_{element.replace(' ', '_')}.csv"
        output_df.to_csv(output_csv_filename, index=False)

        # Returning the output DataFrame so it can be used later if necessary
        return output_df
    except Exception as e:
        print(f"An error occurred: {e}")


# Calling the function
# lab3('FAOSTAT_Lab3_Original.csv', 'Apples', 'Production') # debug

if __name__ == "__main__":
    # Grabbing the command line arguments and passing them to the function
    script, csv_file, item, element = sys.argv
    lab3(csv_file, item, element)
