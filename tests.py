import pytest
import interestCalculator
import graphs
import table
import pandas as pd
from datetime import datetime

#test for the create panda's dataframe
def test_create_pandas_dataframe():
    # Test data
    years = [2020, 2021, 2022]
    annual_salary = [50000, 55000, 60000]
    yearly_contributions = [5000, 5500, 6000]
    amount_saved = [10000, 16500, 23500]

    # Expected DataFrame
    expected_df = pd.DataFrame({
        'Year': years,
        'Annual Salary': ["$50,000.00", "$55,000.00", "$60,000.00"],
        'Yearly Contributions': ["$5,000.00", "$5,500.00", "$6,000.00"],
        'End of Year Balance': ['$10,000.00', '$16,500.00', '$23,500.00']
    })

    # Call the function
    result_df = table.createPandasDataframe(years, annual_salary, yearly_contributions, amount_saved)
    

    # Check if the resulting DataFrame matches the expected DataFrame
    pd.testing.assert_frame_equal(result_df, expected_df, check_dtype=False)

#unit test for the interest calculator
def test_interest_calculator():
    # Test data
    age = 30
    retirementAge = 33
    salary = 50000
    percentContributed = 0.1
    interestRate = 0.05
    initialAmount = 10000

    # Expected output
    current_year = datetime.now().year
    expected_years = [current_year, current_year + 1, current_year + 2]
    expected_annual_salary = [50000, 51500, 53045]
    expected_yearly_contributions = [5000, 5150, 5304.5]
    expected_end_of_year_balance = [
        15750.0,21945.0, 28611.975000000002
    ]
    expected_end_of_year_balance_formatted = [
        f"${x:,.2f}" for x in expected_end_of_year_balance
    ]

    # Call the function
    years, annualSalary, yearlyContributions, endOfYearBalance, duration = interestCalculator.interestCalculator(
        age, retirementAge, salary, percentContributed, interestRate, initialAmount
    )

    # Verify the outputs
    assert years == expected_years
    assert annualSalary == expected_annual_salary
    assert yearlyContributions == expected_yearly_contributions
    print(endOfYearBalance)
    assert pytest.approx(endOfYearBalance, abs=100) == expected_end_of_year_balance  # Allowing small relative error

    # Use the output to create a DataFrame
    result_df = table.createPandasDataframe(years, annualSalary, yearlyContributions, endOfYearBalance)

    # Expected DataFrame
    expected_df = pd.DataFrame({
        'Year': expected_years,
        'Annual Salary': ["$50,000.00", "$51,500.00", "$53,045.00"],
        'Yearly Contributions': ["$5,000.00", "$5,150.00", "$5,304.50"],
        'End of Year Balance': expected_end_of_year_balance_formatted
    })

    # Check if the resulting DataFrame matches the expected DataFrame
    pd.testing.assert_frame_equal(result_df, expected_df, check_dtype=False)

if __name__ == '__main__':
    pytest.main()