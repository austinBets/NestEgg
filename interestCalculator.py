from datetime import datetime

def interestCalculator(age, retirementAge, salary, percentContributed, interestRate, initialAmount=None):
    
    #declare a series of lists that will contain the values needed for our dataframe.
    years =[]
    annualSalary= []
    yearlyContributions = []
    endOfYearBalance = []
    duration = []

    yearsToInvest = retirementAge-age

    #setting current amount equal to the initial amount
    currentBalance = initialAmount

    currentYear = datetime.now().year

    for i in range(1,yearsToInvest+1):

        duration.append(i)
        #Add the current year to the years list, then increase the current year by 1.
        years.append(currentYear)
        currentYear = datetime.now().year + i

        #Calculate the yearly contribution by taking the person's yearly salary and multiplying it by the percentContributed 
        yearlyContribution = salary*percentContributed
        yearlyContributions.append(yearlyContribution)

        #Calculate the percon's yearly salary factoring a 3% raise at the beginning of each year and add them to each of the
        annualSalary.append(salary)
        salary *= 1.03

        #Update the current balance with the yearly contrivbution and compound interest
        currentBalance += yearlyContribution
        currentBalance *= (1+interestRate)
        #save the current balance to an end of year balance list
        endOfYearBalance.append(currentBalance)

    return years, annualSalary, yearlyContributions, endOfYearBalance, duration
