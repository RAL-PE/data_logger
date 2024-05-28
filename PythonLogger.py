"""
Example Data Logger Code
"""

from sense_hat import SenseHat 
# import sense hat function including sensors
sense = SenseHat()

from datetime import datetime
import time


# Define a workbook name for the logger
workbookname = str(input("what should the workboook be called?"))

# Take configuration inputs
timelen    = int(input("how long would you like the experiment to run? (In minutes) "))  
readingnum = int(input("and how many reading you you like to tke during this time? ")) 
delay      = ((timelen*60)-(0.00165*readingnum))/readingnum 

if delay < 0: 
    print("experiment will overun because there are too many readings in too short duration") 
    delay = 0 
    #turns the delay off

# Setup spreadsheet column headers
headers = "time lapsed,current time,humidity,temperature,pressure/n"
contents = ""

start_time = datetime.now()

try:
    for loop in range(readingnum): #while loop for experiment
        row = []
        current_lapsed = datetime.now()
        time_lapsed    = (current_lapsed-start_time).total_seconds()

        # Always write two significant figures.
        row.append(f'{time_lapsed:.2f}')
        
        # Also write current time
        current_time = current_lapsed.strftime("%H:%M:%S")
        row.append(current_time)
        row.append(f'{sense.get_humidity():.2f}')
        row.append(f'{sense.get_temperature_from_humidity():.2f}')
        row.append(f'{sense.get_pressure():.2f}')

        time.sleep(delay) #delay to create requested experiment length
        contents += ','.join(row) + '/n'

except:
    # catch errors here
    pass

with open(workbookname+'.csv','w') as f:
    f.write(str(headers+contents))

