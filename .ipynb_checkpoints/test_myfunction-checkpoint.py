"""
Created on Sunday Nov 5 

@author: Nuray Can

This function creates a helper data to test the sample script created for 
the sample solution to the Python Programmign for Data Science project.
"""
import pandas as pd

from myfunction import calculate_average_inflation_adjusted_gross


def test_calculate_average_inflation_adjusted_gross():

    # Create helper data and write tests for the function
    raw = {
        "id": [1873, 4913, 4801, 4540, 3581, 4534, 1934, 4944, 1983, 1266],
        "name": [
            "English Oak",
            "Higan Cherry",
            "Willow Oak",
            "Yoshino Cherry",
            "Red Oak",
            "Kindred Spirit Oak",
            "Garry Oak",
            "Accolade Cherry",
            "Snow Goose Cherry",
            "Evergreen Oak",
        ],
        "neighbourhood": [
            "Sunset",
            "West end",
            "Kitsilano",
            "Sunset",
            "Arbutus-ridge",
            "Arbutus-ridge",
            "Kitsilano",
            "West end",
            "Kitsilano",
            "Arbutus-ridge",
        ],
        "type": [
            "Oak",
            "Cherry",
            "Oak",
            "Cherry",
            "Oak",
            "Oak",
            "Oak",
            "Cherry",
            "Cherry",
            "Oak",
        ],
        "diameter": [9.0, 27.0, 3.0, 22.0, 3.0, 6.5, 12.0, 18.0, 8.5, 23.0],
    }

    helper_data = pd.DataFrame.from_dict(raw)

    res = calculate_average_inflation_adjusted_gross(helper_data, "type", "diameter")

    assert res.shape == (2, 2), "The dataframe is not of the expected dimensions"
    assert list(res["diameter"]) == [18.875, 9.416666666666666]
    assert list(res["type"]) == ["Cherry", "Oak"]
    assert sorted(list(res.columns))[0:2] == [
        "diameter",
        "type",
    ], "Your dataframe contains the incorrect columns.Are you reading in the correct dataframe?"
    return

from myfunction import calculate_genre_counts

def test_calculate_genre_counts():
    # Create corrected helper data with more rows
    data = {
        'Name': ['Joseph ', 'James ', 'Thomas', 'Buzz ', 'Andrew ','Mary','Jane','Angel','Sam','Jack'],
        'Year': [2004,1984,1987,1963,1987,2000,2001,2002,2003,2005],
        'Group': [19,10,12,3,12,19,10,12,3,3],
        'Gender': ['Male','Male','Male','Male','Male','Female','Female','Female','Male','Male'],
        'Graduate Major': ['Geology',' Engineering',' Mathemetics','Astronautics','Business Administration','Accounting','Physics','Geology',' Engineering',' Mathemetics']
    }
    helper_data = pd.DataFrame.from_dict(data)
    #Test sample_dataframe(xx) function
    test_result1=calculate_genre_counts(helper_data, 'Group')
    test_result2=calculate_genre_counts(helper_data, 'Gender')
 
    
    #Test 1: Check if the returned DataFrame has the correct number of rows 
    assert test_result1.shape[0]==4,"incorrect rows"
    
    
    #Test 2: Check if the returned DataFrame is empty for N=1
    assert test_result2.shape[0]==2,"incorrect rows"
    
    #Test 4: Check if the function returns a DataFrame
    assert isinstance(calculate_genre_counts(helper_data, 'Group'), pd.DataFrame), "It's not a dataframe"

    # Return statement (no values)
    return
