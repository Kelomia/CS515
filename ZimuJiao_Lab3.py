def driving_cost(miles,price):
        rate=price/miles
        cost_10=rate*10
        cost_50=rate*50
        cost_100=rate*100

        print(cost_10,cost_50,cost_100)
        return


driving_cost(20.0,3.1599)