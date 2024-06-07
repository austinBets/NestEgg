import pandas as pd

def createPandasDataframe(years, annualSalary, yearlyContributions ,amountSaved):

    dataFrame = pd.DataFrame({
        'Year': years,
        'Annual Salary': annualSalary,
        'Yearly Contributions': yearlyContributions,
        'End of Year Balance': amountSaved
    })

    #Format a each 
    dataFrame['Year'] = dataFrame['Year'].astype(int)
    dataFrame['Annual Salary'] = dataFrame['Annual Salary'].apply(lambda x: f"${x:,.2f}")  # Format as dollar values
    dataFrame['Yearly Contributions'] = dataFrame['Yearly Contributions'].apply(lambda x: f"${x:,.2f}")
    dataFrame['End of Year Balance'] = dataFrame['End of Year Balance'].apply(lambda x: f"${x:,.2f}")

    return dataFrame
