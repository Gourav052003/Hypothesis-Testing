# chi2 goodness of fit

# importing packages 
import scipy.stats as stats 
import numpy as np 
  
# no of hours a student studies 
# in a week vs expected no of hours 
observed_data = [8, 6, 10, 7, 8, 11, 9] 
expected_data = [9, 8, 11, 8, 10, 7, 6] 
  
  
# Chi-Square Goodness of Fit Test 
chi_square_test_statistic, p_value = stats.chisquare( 
    observed_data, expected_data) 
  
# chi square test statistic and p value 
print('chi_square_test_statistic is : ' +
      str(chi_square_test_statistic)) 
print('p_value : ' + str(p_value)) 
  
  
# find Chi-Square critical value 
print(stats.chi2.ppf(1-0.05, df=6)) 