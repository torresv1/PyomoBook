# Name:      Using a function to construct a concrete Pyromo Model
#Purpose:    A function that creates a concrete Pyomo model for Formulation (2.1) using only data provide in the argument list
#Date:       10/19/2013 1:04 AM
#Author:     Vladimir Torres-Rivas


#Python import statement

from coopr.pyomo import *

#Create a Pyomo model object

def create_model ( N = [], M = [], c = {}, a = {}, b = {} ):

    model = ConcreteModel()

#Define model variables

    model.x = Var ( N , within = NonNegativeReals )

#Define objective function

    model.obj = Objective ( expr = sum( c[i] * model.x[i] for i in N ) )

#Define constraints

    def con_rule( model, m ):
        return sum( a[i, m] * model.x[i] for i in N ) >= b[m]
    model.con = Constraint ( M, rule = con_rule )
    return model

#Define model set and parameters 

model = create_model (N = [1,2], M = [1,2], c = {1:1, 2:2}, a = {(1,1):3, (2,1):4, (1,2):2, (2,2):5}, b = {1:1,2:2}  )
