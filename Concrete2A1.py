#Name:       Concrete Pyomo for formulation (2.2) using explicit variables 
#Purpose:    Practice
#Date:       10/18/2013 1:42 AM
#Author:     Vladimir Torres-Rivas


#Python import statement

from coopr.pyomo import *

#Create a Pyomo model object

model = ConcreteModel()

#Define model set and parameters 

#Define model variables

model.x_1 = Var(within=NonNegativeReals)
model.x_2 = Var(within=NonNegativeReals)

#Define objective function

model.obj = Objective(expr=model.x_1 + 2*model.x_2)

#Define constraints

model.con1 = Constraint(expr=3*model.x_1 + 4*model.x_2 >=1)
model.con2 = Constraint(expr=2*model.x_1 + 5*model.x_2 >=2)
