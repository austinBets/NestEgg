# Compound Interest Calculator for Nest Egg

## Overview

This program calculates the compound interest for a person's nest egg over a specified period. It takes into account annual contributions, a 3% yearly raise in a person's salary, and an average rate of return to provide an estimated final balance at retirement.

## Features

- **Annual Salary Increment:** Assumes a 3% annual raise in salary.
- **Annual Contributions:** Calculates the dollar value of yearly contributions based on a percentage of the annual salary.
- **Compound Interest:** Uses a 6.5% average return rate to compute the growth of the nest egg.
- **PDF Generate:** Once the compound Interest has been calculated a PDF will be generated contained a graph of the balance over time and table highlighting your salary, your yearly contributions and your end of year balance.

## Inputs

- **Current Age:** The current age of the individual.
- **Retirement Age:** The age at which the individual plans to retire.
- **Annual Salary:** The current annual salary of the individual.
- **Percent Contributed:** The percentage of the annual salary contributed to the nest egg each year.
- **Initial Amount:** How much the individual has saved so far.

## Output

The program will generate a PDF that contains the following:
1. **Line chart:** A line chart summarizing your nest eggs balance overtime.
2. **Table:** A table that will contain the following information:
   - **Year:** The year for each entry.
   - **Yearly Salary:** The estimated salary for each year, assuming a 3% raise.
   - **Yearly Contribution:** The dollar value contributed to the nest egg each year, based on the specified percentage of the salary.
   - **End of Year Balance:** The balance of the nest egg at the end of each year, accounting for contributions and the compound interest at a 6.5% return rate.

## Example Usage

To run the program, execute the `main.py` file. The program will prompt you to enter your age, expected retirement age, annual salary, percentage contribution, and initial balance.

```bash
$ python3 main.py
Please input your Age: 30
What age do you expect to retire? 65
What is your annual salary? 50000
What percentage of your yearly salary are you expecting to contribute (enter as a decimal): 0.05
How much have you saved so far? 10000
```
This summary provides a clear explanation of the program and includes instructions for running it using your `main.py` file, along with an example of the input prompts users will see.