#  Capstone #1 Project Proposal

# City of Boston Payroll Analysis

### What is the problem you want to solve?

I’d like to focus on the following questions:

1. Is total payroll increasing and what are the reasons for this? This information would be helpful in forecasting budgets and identifying opportunities for cost reduction. Examples of positive factors are cost of living increases, promotions, increase of better paying job titles and increased overtime. Examples of negative factors could be employee attrition, increase of lower paying job titles and reduction in overtime pay
2. Are there any social trends that Boston residents would care about? For example, which zip codes are home to the highest and lowest average paid employees? Can we identify geographic clusters of certain professions? 

### Who is your client and why do they care about this problem? In other words, what will your client DO or DECIDE based on your analysis that they wouldn’t have otherwise?

My primary clients are Boston taxpayers who are interested in the return on investment for their tax dollar. Analysis of the data could identify opportunities for cost savings which could result in lower taxes or a redirection of tax dollars for other purposes.

Since the city office is as much a political entity as it is a business, many residents are also interested in social issues such as gender pay-gap, racial divide and wealth segregation. Analysis could possibly inform a political debate for social change.

### What data are you going to use for this? How will you acquire this data?

https://data.boston.gov/dataset/employee-earnings-report

Earnings data is available for City of Boston employees from 2011 to 2016 as annual “CSV” files or accessible through an API. The entries are classified into the following columns:

'name' = Full name of city employee
'department' = Department name
'title' = Job title
'regular' = Base earnings (salary) as total of pay for a given year
'retro' = Retroactive payments for a given year
'other' = Additional payments categorized as “other”
'overtime' = Overtime pay
'injured'  = payment issued for qualified employees who are not working due 					to injuries
'detail’ = ???
'quinn' = Education incentive specifically for police department
'total' = Numerical sum of prior columns
'zip' = Zip code of employee’s primary residence


### In brief, outline your approach to solving this problem (knowing that this might change later).

Descriptive statistics and categorization of data will be used to understand trends in payroll. Regression analysis could be useful in analyzing some of the social questions. 

Gender and race are not given in the database. If this becomes an important question, it might be possible to parse given names and categorize based on probability from other data sources.

Some questions might benefit from comparison to additional data sources, e.g. earnings reports from other cities/states and real estate data. 

### What are your deliverables? Typically, this would include code, along with a paper and/or a slide deck.

Jupyter notebook, presentation slide deck with commentary.
