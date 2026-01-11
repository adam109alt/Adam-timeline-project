my_time = int(input('Enter the time in seconds '))

for x in range(my_time, 0 , -1): # and 0 in here meaning that in it the time is top bcs in range is [start:stop:step]
    
    seconds = x % 60
    minutes = int(x / 60 ) % 60
    hours = int(x / 3600)
    
    print(f'{hours:02}:{minutes:02}:{seconds:02}')
    time.sleep(1)
    
