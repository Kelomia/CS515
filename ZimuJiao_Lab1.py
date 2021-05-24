
def driving_cost(miles,price):
	rate=price/miles
	print(rate*10,rate*50,rate*400)
	return

def CBDW(age,weight,heart_rate,time):
	result_male=((age*0.2017)-(weight*0.09036)+(heart_rate*0.6309)-55.0969)*time/4.184
	result_female=((age*0.074)-(weight*0.05741)+(heart_rate*0.4472)-20.4022)*time/4.184
	print("Men:",result_male," calories.")
	print("Women:",result_female," calories.")
	return