import pandas as pd
data = pd.read_excel('data.xlsx')

applicant_income = data['Applicant_Income']
loan_amount = data['Loan_Amount']
age = data['Age']
print(applicant_income.mean())
print(loan_amount.mean())
print(age.mean())


#2  Compute the five-number summary (minimum, first quartile, median, third quartile, maximum) for the CIBIL_Score column. What does this tell you about the creditworthiness distribution of applicants?
cibil_score = data['CIBIL_Score'] 
five_number_summary = cibil_score.describe()[['min', '25%', '50%', '75%', 'max']]
print("Five-number summary for CIBIL_Score:")
print(five_number_summary)



# Calculate the coefficient of variation (CV) for:
# Applicant_Income
# Annual_Household_Income

#3 Which income measure is more stable? Justify statistically.
applicant_income_cv = (applicant_income.std() / applicant_income.mean()) * 100
annual_household_income = data['Annual_Household_Income']
annual_household_income_cv = (annual_household_income.std() / annual_household_income.mean()) * 100
print(f"Applicant Income CV: {applicant_income_cv}")
print(f"Annual Household Income CV: {annual_household_income_cv}")
if applicant_income_cv < annual_household_income_cv:
    print("Applicant Income is more stable.")
else:
    print("Annual Household Income is more stable.")



# Probability Fundamentals
# Q4. If an applicant is selected at random, calculate the probability that:
# The loan is approved


# The applicant has a good credit history


# The loan is approved and the applicant has a good credit history
total_applicants = len(data)
loan_approved = len(data[data['Loan_Status'] == 'Y'])
good_credit_history = len(data[data['Credit_History'] == 1])
loan_approved_prob = loan_approved / total_applicants
good_credit_history_prob = good_credit_history / total_applicants
loan_approved_and_good_credit = len(data[(data['Loan_Status'] == 'Y') & (data['Credit_History'] == 1)])
loan_approved_and_good_credit_prob = loan_approved_and_good_credit / total_applicants
print(f"Probability of loan approval: {loan_approved_prob}")
print(f"Probability of good credit history: {good_credit_history_prob}")
print(f"Probability of loan approval and good credit history: {loan_approved_and_good_credit_prob}")

