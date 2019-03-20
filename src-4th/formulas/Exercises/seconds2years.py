def secons2years(seconds):
    years = seconds/(60*60*24*365.25)
    return years

print (secons2years(10e9))