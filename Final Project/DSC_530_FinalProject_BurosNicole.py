# Nicole Buros
# 6/4/22
# DSC 530 Final Project


import pandas
import matplotlib.pyplot as plt
import thinkstats2
import thinkplot
import statsmodels.formula.api as smf

 
def AnimalType(df):
    # Creating plot and variable for Animal Type
    animal_type = df['Animal_Type']
    plt.hist(animal_type)
    age = df['Age_upon_Outcome']
    thinkplot.Scatter(animal_type, age, alpha = 1)
    thinkplot.Config(xlabel= 'Animal Type', ylabel = 'Age')
    
def Outcome(df):
    # Creating plot and variable for Outcome Type
    outcome = df['Outcome_Type']
    plt.hist(outcome)
    
def Breed(df):
    # Creating plot and variable for Breed
    breed = df['Breed']
    plt.hist(breed)
    
def Age(df):
    # Creating plot and variable for Age
    age = df['Age_upon_Outcome']
    young = df[df.Age_upon_Outcome <= 2]
    older = df[df.Age_upon_Outcome > 2]
    print(age.mean())
    plt.hist(age)
    young_pmf = thinkstats2.Pmf(young)
    older_pmf = thinkstats2.Pmf(older)
    thinkplot.PrePlot(2, cols=2)
    thinkplot.Hist(young_pmf, align='right')
    thinkplot.Hist(older_pmf, align='left')
    thinkplot.Config(xlabel = 'Age', ylabel = 'Probability')
    cdf = thinkstats2.Cdf(df.Age_upon_Outcome)
    print(cdf)
    print(cdf.Prob(.5))
    print(cdf.Prob(5))
   
def Sex(df):    
    # Creating plot and variable for Sex
    sex = df['Sex_upon_Outcome']
    plt.hist(sex)
    age = df['Age_upon_Outcome']
    thinkplot.Scatter(sex, age, alpha = 1)
    thinkplot.Config(xlabel= 'Sex', ylabel = 'Age')   
    
def RegressionResults(df):
    formula = 'Outcome_Type ~ Age_upon_Outcome'
    results = smf.ols(formula, data = df).fit()
    print(results.summary())
  
def main():
    df = pandas.read_csv('Austin_Animal_Center_OutcomesNB.csv')
    df.head()
    Sex(df)
    Age(df)
    Outcome(df)
    AnimalType(df)
    Breed(df)
    Sex(df)
    RegressionResults(df)

if __name__ == '__main__':
    main()