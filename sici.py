"""
Created by Snehashish Laskar
Email: snehashish.laskar@gmail.com
Created on 10-03-2021
This is just a basic simple and compound intrest calculator
"""
def SimpleIntrest(principle,rate,time):
	intrest = (int(principle)+int(rate)+int(time)) / 100
	amount = int(principle) + int(intrest)
	print(f" You'r money will amount to {amount} and the intrest you are paying/getting is {intrest}")

def CompoundIntrest(principle, rate, time):
	amount = int(principle)*((1 + int(rate))**int(time))
	intrest = int(amount)-int(principle)
	print(f" You'r money will amount to {amount} and the intrest you are paying is {intrest}")

