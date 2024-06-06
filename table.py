import pandas as pd

def createPandasDataframe(years, annualSalary, yearlyContributions ,amountSaved):

    dataFrame = pd.DataFrame({
        'Year': years,
        'Annual Salary': annualSalary,
        'Yearly Contributions': yearlyContributions,
        'Amount Saved': amountSaved
    })

    return dataFrame
