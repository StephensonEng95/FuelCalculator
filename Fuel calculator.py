import pandas as pd
import time

def table(fuel,result):
    list=[fuel,result]
    df=pd.DataFrame(list,columns=['Fuel','Result'])
    return df

def fuel_calculator(fuel):
    
    current_fuel=0
    current_fuel += fuel
    result1=current_fuel/3
    result2=result1-2
    total=result1+result2
    resultFinal= round(total,2)
    return resultFinal

while("Enter"!=0):
    print("                Welcome to STEPHENSONENG95 FUEL CALCULATOR"          )
    print("-------------------------------------------------------------------------" )
    print('Enter how much fuel you topped up today')
    new_fuel=float(input()) 
    print("Topped up fuel is: ", new_fuel)
    time.sleep(2)
    print('calculating fuel consumption...')
    time.sleep(3)
    b=fuel_calculator(new_fuel)
    print(b)
    time.sleep(2)
    c=table(new_fuel,b)
    print('-------------------------------------------------------------------------' )
    time.sleep(5)
    if "Enter"==0:
        break

