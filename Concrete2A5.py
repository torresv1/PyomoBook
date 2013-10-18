#Name:       Concrete Pyomo for formulation (2.2) with abstract component declarations
#Purpose:    A concrete Pyomo model for formulation (2.2) that uses "rule" and "initialize" arguments for all modeling componets
#Date:       10/18/2013 3:18 PM
#Author:     Vladimir Torres-Rivas


#Python import statement

from coopr.pyomo import *

#Create a Pyomo model object

model = ConcreteModel()


#Initializing arguments
def N_rule(model):
    return [1,2]
model.N = Set(rule=N_rule)

#Define model set and parameters 

model.M = Set (initialize=[1,2])
model.c = Param (model.N, initialize={1:1,2:2})
model.a = Param (model.N, model.M, initialize={(1,1):3,(2,1):4,(1,2):2,(2,2):5})
model.b = Param (model.M, initialize={1:1,2:2})
   
#Define model variables

model.x = Var (model.N, within=NonNegativeReals)  

#Define objective function

def obj_rule(model):
    return sum( model.c[i] * model.x[i] for i in model.N )
model.obj = Objective (rule=obj_rule)

#Define constraints

def con_rule(model,m):
    return sum(model.a[i,m]*model.x[i] for i in model.N) >= model.b[m]
model.con = Constraint (model.M, rule=con_rule)
