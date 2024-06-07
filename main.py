import graphs
import table
import report
import interestCalculator
import os


def main():
    age = int(input("Please input your Age: ")) #get the age from the user
    retirementAge = int(input("What age to you expect to retire? ")) #get the age they expect to retire
    yearlySalary = int(input("What is your annual salary? ")) #get how much money the user makes per year
    contributions = float(input("What percentage of your yearly salary are you expecting to contribute (enter as a decimal): ")) #get the percentage of their yearly salary they are expected to contribute
    initialBalance = int(input("How much have you saved so far? ")) #get how much money they initally have to invest
    estimatedInterestRate= .09 # estimated amount of return.

    years, annualSalary, yearlyContributions, endOfYearBalance, duration =interestCalculator.interestCalculator(age, retirementAge, yearlySalary, contributions, estimatedInterestRate, initialBalance)

    graphs.create_lineGraph(duration, endOfYearBalance)
    dataFrame = table.createPandasDataframe(years, annualSalary, yearlyContributions, endOfYearBalance)
    pdfName = 'Compound_intest.pdf'
    report.generate_pdf_report( pdfName,'plot.png', dataFrame, age, retirementAge)

    os.system(pdfName)
  

if __name__ == "__main__":
    main()