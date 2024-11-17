import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
file_path = 'data.csv'  # Replace with your actual file path
data = pd.read_csv(file_path)

# Strip any whitespace from column headers
data.columns = data.columns.str.strip()

def born_vs_age():
    # Convert 'year born' to numeric, coercing errors to NaN, then drop rows with NaN in 'year born'
    data['year born'] = pd.to_numeric(data['year born'], errors='coerce')
    data.dropna(subset=['year born'], inplace=True)

    # Ensure 'year born' is now integer
    data['year born'] = data['year born'].astype(int)

    # Check for columns based on the provided example headers
    if 'year born' in data.columns and 'age' in data.columns:
        # Plot Year Born vs Age
        plt.figure(figsize=(10, 6))
        plt.scatter(data['year born'], data['age'], alpha=0.7)
        plt.title('Year Born vs Age')
        plt.xlabel('Year Born')
        plt.ylabel('Age')
        plt.grid(True)
        
        # Set x-axis ticks to every 10 years
        start_year = int(data['year born'].min() // 10 * 10)  # Round down to nearest 10
        end_year = int(data['year born'].max() // 10 * 10) + 10  # Round up to nearest 10
        plt.xticks(range(start_year, end_year + 1, 10))

        plt.show()
    else:
        print("The CSV file does not contain the required columns: 'year born' and 'age'")
def born_vs_died():
    # Convert 'year born' to numeric, coercing errors to NaN, then drop rows with NaN in 'year born'
    data['year born'] = pd.to_numeric(data['year born'], errors='coerce')
    data.dropna(subset=['year born'], inplace=True)

    # Ensure 'year born' is now integer
    data['year born'] = data['year born'].astype(int)

    # Check for columns based on the provided example headers
    if 'year born' in data.columns and 'year died' in data.columns:
        # Plot Year Born vs Age
        plt.figure(figsize=(10, 6))
        plt.scatter(data['year born'], data['year died'], alpha=0.7)
        plt.title('Year Born vs Year Died')
        plt.xlabel('Year Born')
        plt.ylabel('Year Died')
        plt.grid(True)
        
        # Set x-axis ticks to every 10 years
        start_year = int(data['year born'].min() // 10 * 10)  # Round down to nearest 10
        end_year = int(data['year born'].max() // 10 * 10) + 10  # Round up to nearest 10
        plt.xticks(range(start_year, end_year + 1, 10))

        plt.show()
    else:
        print("The CSV file does not contain the required columns: 'year born' and 'year died'")

#born_vs_died()
born_vs_age()