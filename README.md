# Height Comparison Program in Python

This Python program calculates and compares the average heights of two groups: boys and girls. It sorts the names of the individuals in each group, computes the average height for each group, and then determines the difference between the two averages along with the percentage difference.

## Features

- **Data Structure**: The program uses lists of dictionaries to store names and heights for boys and girls.
- **Sorting**: Names are sorted alphabetically for both groups.
- **Average Calculation**: The program calculates the average height for boys and girls.
- **Difference Calculation**: It computes the absolute difference between the two averages and the percentage difference relative to the boys' average height.
- **Formatted Output**: The program prints the names and heights of individuals, along with the calculated averages, differences, and percentage differences in a user-friendly format.

## Code Explanation

1. **Data Initialization**: Two lists, `m` and `f`, are initialized with dictionaries containing names and heights of boys and girls, respectively.

2. **Sorting**: The lists are sorted alphabetically by name using the `sort()` method with a lambda function as the key.

3. **Average Calculation**:
   - The average height for boys (`mm`) is calculated by summing the heights and dividing by the number of boys.
   - The average height for girls (`mf`) is calculated similarly.

4. **Difference Calculation**:
   - The absolute difference (`d`) between the two averages is computed.
   - The percentage difference (`pd`) is calculated based on the boys' average height.

5. **Rounding**: The averages, difference, and percentage difference are rounded to two decimal places for better readability.

6. **Output**: The program prints the sorted names and heights, along with the calculated averages, difference, and percentage difference.

## How to Run

1. **Install Python**: Ensure you have Python installed on your machine (version 3.6 or higher).

2. **Save the Code**: Copy the code into a file named `height_comparison.py`.

3. **Run the Program**:
   ```bash
   python height_comparison.py
