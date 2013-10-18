#Name:       Concrete Pyomo for formulation (2.2) with external data
#Purpose:    A concrete Pyomo model for formulation (2.2) with (a) external data declarations and (b) expressions
#            defined using Python's generator syntax
#Date:       10/18/2013 2:28 PM
#Author:     Vladimir Torres-Rivas


#Python import statement

from coopr.pyomo import *

#Data set

N = [1,2]
c = {1:1,2:2}
a = { (1,1):3, (2,1):4, (1,2):2, (2,2):5 }
b = {1:1,2:2}

#Create a Pyomo model object

model = ConcreteModel()

#Define model set and parameters 

#Define model variables

model.x = Var(N, within=NonNegativeReals)

#Define objective function

model.obj = Objective(expr= sum(c[i]*model.x[i] for i in N))

#Define constraints

model.con1 = Constraint(expr= sum(a[i,1]*model.x[i] for i in N) >= b[1])
model.con2= Constraint(expr= sum(a[i,2]*model.x[i] for i in N) >= b[2])
