# Programming Assignment 3 – Python Data Analysis

**Author:** ESMENDA, Francine Jasmine Guelle T.

**Course:** Advanced Computer Programming and Algorithms / ECE2112  

---

## Description  

This Jupyter Notebook demonstrates **data analysis using the Pandas library** in Python.  
It applies indexing, slicing, and subsetting techniques to explore and extract information from a dataset.  

The problems solved include:  
1. **Load Dataset** – Import a `.csv` file into a Pandas DataFrame.  
2. **Basic Exploration** – Display the first five and last five rows of the dataset.  
3. **Subsetting by Columns** – Select specific odd-numbered columns.  
4. **Row Selection by Condition** – Find details of specific car models.  
5. **Data Extraction** – Retrieve values of cylinders and gear types for selected car models.  

---

## Problems & Explanation
**PROBLEM 01**
```python
import pandas as pd

#Load CSV file into DataFrame
cars = pd.read_csv("cars.csv")

#Display first five and last five rows
print(cars.head())
print(cars.tail())
```
- pd.read_csv() → loads the dataset into a Pandas DataFrame.
- head() and tail() → preview the first and last rows of the dataset.
  
---

**PROBLEM 02**
```python
#Display first five rows with odd-numbered columns
print(cars.iloc[:5, ::2])
```
- iloc[:5, ::2] → selects the first 5 rows (:5) and every other column (::2).
  
```python
#Row containing model 'Mazda RX4'
print(cars[cars["Model"] == "Mazda RX4"])
```
- Uses a boolean filter to select the row where the Model is "Mazda RX4".
  
```python
#Cylinders of 'Camaro Z28'
print(cars.loc[cars["Model"] == "Camaro Z28", "cyl"])

#Cylinders and gear type of multiple models
models = ["Mazda RX4 Wag", "Ford Pantera L", "Honda Civic"]
print(cars.loc[cars["Model"].isin(models), ["Model","cyl", "gear"]])
```
- loc[] → selects rows and columns based on labels.
- isin() → filters multiple car models at once.

---

## Version History
- v1.0 – Initial notebook: loaded dataset and displayed head/tail rows.
- v1.1 – Added column subsetting and row filtering.
- v1.2 – Extracted specific values (cylinders, gear types).
- v1.3 – Improved explanations and comments.

  
