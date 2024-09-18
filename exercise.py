def computepay(hours, rate):
    if hours > 40:
        overtime_hours = hours - 40
        normal_pay = 40 * rate
        overtime_pay = overtime_hours * (rate * 1.5)
        pay = normal_pay + overtime_pay
    else:
        pay = hours * rate
    return pay

hours = input('Enter Hours:\n')
try:
    hours = float(hours)
except:
    print('ERROR', hours, 'is not a valid number')
    quit()
rate = input('Enter Rate:\n')
try:
    rate = float(rate)
    
except:
    print('EROR', rate, 'is not a valid number')
    quit()



print('Your pay:', computepay(hours, rate))
print('Thank you!')
