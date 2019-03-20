def length_conversion(meters):
    inches = meters*100/2.54
    foot = inches/12
    yard = foot/3
    mile = yard/1760
    return (inches, foot, yard, mile)

print (length_conversion(640))