#Name:       Concrete Pyomo for formulation (2.2) with constraint rules
#Purpose:    A concrete Pyomo model for formulation (2.2) using a constraint rule to create constraints con.
#Date:       10/18/2013 3:08 PM
#Author:     Vladimir Torres-Rivas


#Python import statement

from coopr.pyomo import *

#Data set

N = [1,2]
M = [1,2]
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

def con_rule(model,m):
    return sum(a[i,m]*model.x[i] for i in N) >= b[m]
model.con = Constraint (M, rule=con_rule)
