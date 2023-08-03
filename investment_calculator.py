import math

initial_investment=int(input('Enter the initial investment: '))
require_investment=int(input('Require return you want : '))

rate=int(input('Enter your interest rate per annum: '))

total_time_needed=(math.log(require_investment/initial_investment)/math.log(1+rate/100))
time=(round(total_time_needed*12))
time_years=time/12
print(time_years,f'years OR', time,'months Approx.')


