"""
Created on Sunday Nov 5 

@author: Nuray Can

"""
import pandas as pd


def calculate_average_inflation_adjusted_gross(data, grouping_col, action_col):
    """
    Calculate the average inflation-adjusted gross earnings for each genre in the provided movie data.

    Parameters
    ----------
    data : pandas.core.frame.DataFrame
        A DataFrame containing movie data, including 'genre' and 'inflation_adjusted_gross' columns.

    grouping_col : str
        The column to group the data on
    action_col : str
        After grouping, the column to applying action to

    Returns
    -------
    pandas.core.frame.DataFrame
        A DataFrame with two columns: 'genre' and 'average_inflation_adjusted_gross'.
        It contains the average inflation-adjusted gross earnings for each genre.

    Examples
    --------
    >>> data = pd.DataFrame({
    >>>     'genre': ['Musical', 'Adventure', 'Musical', 'Comedy'],
    >>>     'inflation_adjusted_gross': [1000000, 2000000, 1500000, 800000]
    >>> })
    >>> result = calculate_average_inflation_adjusted_gross(data,'genre')
    >>> print(result)
           genre  average_inflation_adjusted_gross
    0  Adventure                         2000000.0
    1    Comedy                         800000.0
    2   Musical                         1250000.0

    Raises
    ------
    TypeError
        If the input argument data is not of type pandas.core.frame.DataFrame
    TypeError
        If the input argument grouping_col is not in the data columns
    """

    # Checks if a DataFrame is the type of object being passed into the data argument
    if not isinstance(data, pd.DataFrame):
        raise TypeError("The data argument is not of type DataFrame")

    # Tests that the the grouping column is in the dataframe
    assert (
        grouping_col in data.columns
    ), "The grouping column does not exist in the dataframe"

    # Tests that the the action column is in the dataframe
    assert (
        action_col in data.columns
    ), "The action column does not exist in the dataframe"

    # Compute the average inflation-adjusted gross
    average_inflation_adjusted_gross = (
        data.groupby(grouping_col)[action_col].mean().reset_index()
    )

    return average_inflation_adjusted_gross


def calculate_genre_counts(dataframe, grouping):
    """
    Calculate the count of movies for each genre in the provided movie data.

    Parameters
    ----------
    dataframe : pandas.core.frame.DataFrame
                A DataFrame containing movie data
    grouping : str
               The column to group the data on

    Returns
    -------
    pandas.core.frame.DataFrame
        A DataFrame with two columns: 'genre' and 'counts', containing the count of movies for each genre.

    Examples
    --------
    >>> disney_movie_gross = pd.read_csv('data/disney_movies_total_gross.csv')  # Load your Disney movie data
    >>> genre_count = calculate_genre_counts(disney_movie_gross)
    >>> print(genre_count)

    Raises
    ------
    TypeError
        If the input argument data is not of type pandas.core.frame.DataFrame
    """
    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("The input 'dataframe' must be of type pandas.DataFrame.")

    # Tests that the the grouping  is in the dataframe
    assert (
        grouping in dataframe.columns
    ), "The grouping column does not exist in the dataframe"

    genre_count = dataframe.groupby([grouping]).size().reset_index(name="counts")

    return genre_count
