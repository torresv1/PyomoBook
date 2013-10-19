# Name:      Abstract Pyomo Model
# Purpose:    An abstract model for formulation (2.1)
# Date:       10/19/2013 2:34 AM
# Author:     Vladimir Torres-Rivas


# Python import statement

from coopr.pyomo import *

# Create a Pyomo model object

model = AbstractModel()

# Define model set and parameters

model.N = Set()
model.M = Set()
model.c = Param( model.N )
model.a = Param( model.N, model.M )
model.b = Param( model.M )

# Define model variables

model.x = Var ( model.N , within = NonNegativeReals )

# Define objective function

def obj_rule( model ):
    return sum( model.c[i] * model.x[i] for i in model.N )
model.obj = Objective( rule = obj_rule )

# Define constraints

def con_rule( model, m ):
    return sum( model.a[i, m] * model.x[i] for i in model.N ) >= model.b[m]
model.con = Constraint ( model.M, rule = con_rule )


