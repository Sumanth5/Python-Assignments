/* Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, 
and most affordable experience shipping their packages. In this project, you’ll build a program that will take the weight of a package and determine the 
cheapest way to ship that package using Sal’s Shippers.
Sal’s Shippers has several different options for a customer to ship their package. They have ground shipping, which is a small flat charge plus a rate based 
on the weight of your package. Premium ground shipping, which is a much higher flat charge, but you aren’t charged for weight. They recently also implemented drone shipping,
which has no flat charge, but the rate based on weight is triple the rate of ground shipping. */

def cost_ground(weight):
  if(weight <= 2):
    cost = 1.50*weight + 20;
    return cost;
  elif(weight > 2 and weight <= 6):
    cost = 3*weight + 20;
    return cost;
  elif(weight > 6 and weight <= 10):
    cost = 4*weight + 20;
    return cost;
  elif(weight > 10):
    cost = 4.75*weight + 20;
    return cost;

cost_premium = 125;

def cost_drone(weight):
  if(weight <= 2):
    cost = 4.50*weight;
    return cost;
  elif(weight > 2 and weight <= 6):
    cost = 9*weight;
    return cost;
  elif(weight > 6 and weight <= 10):
    cost = 12*weight;
    return cost;
  elif(weight > 10):
    cost = 14.25*weight;
    return cost;

def final(weight):
  if(cost_ground(weight) > cost_drone(weight) and cost_premium > cost_drone(weight)):
    print("drone is cheapest " + str(cost_drone(weight)));
  elif(cost_ground(weight) < cost_drone(weight) and cost_premium > cost_ground(weight)):
    print("ground is cheapest " + str(cost_ground(weight)))
  elif(cost_ground(weight) > cost_premium):
    print("premium is cheapest 125")
  elif(cost_drone(weight) > cost_premium):
    print("premium is cheapest 125")
  
print(final(17))
print(final(41.5))
  
