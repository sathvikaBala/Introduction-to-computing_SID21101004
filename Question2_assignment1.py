tax_rate=0.2
standard_deduction=10000
deduction=3000 #dependant deduction

#inputs
gross_income=int(input('Enter gross income to the nearest penny'))
dependants=int(input('Enter number of dependants '))

#finding taxable income
taxable_income=gross_income-standard_deduction-(deduction*dependants)

#finding tax
tax=taxable_income*tax_rate
print('Tax=',tax)
