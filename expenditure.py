def h_cost(nights):
    return 140*nights
def p_cost(city):
    if "Charlotte" == city:
        return 183
    elif "Tampa" == city:
        return 220
    elif "Pittsburgh" == city:
        return 222
    elif "Los Angeles" == city:
        return 475
def rental_car_cost(days):
    c= 40*days
    if days>=7:
        return c-50
    elif days>=3:
        return c-20
    else:
        return c
def trip_cost(city, days, spending_money):
    return h_cost(days)+p_cost(city)+rental_car_cost(days)+spending_money
print("Cost of car rental:" + str(rental_car_cost(5)))
print("Cost of hotel stay:" + str(h_cost(5)))
print("Cost of plane ticket:" + str(p_cost("Los Angeles")))
print("Total cost of trip:" + str(trip_cost("Los Angeles", 6, 500)))
print("Total cost of trip:" + str(trip_cost("Tampa", 6, 500)))