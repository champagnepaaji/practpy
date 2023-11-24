print('option1: cm to m')
print('option2: m to cm')
print('option3: cm to inches')
print('option4: inches to cm')
while True:
    unit = int(input('Select the conversion you want: ')) # -> 1
    value = float(input('Enter the value you want to convert: '))

    import unitconverter as uc 
    def r1(a,f1):
        getattr(uc.uc(a),f1)()
    if unit==1:
        r1(value,'cm_to_m')
    elif unit==2:
        r1(value,'m_to_cm')
    elif unit==3:
        r1(value,'cm_to_inches')
    elif unit==4:
        r1(value,'inches_to_cm')
    else:
        print('Enter a valid option:')
        
'''               
if unit==1:
    u1=uc.uc(value)
    u1.cm_to_m()
elif unit==2:
    u1=uc.uc(value)
    u1.m_to_cm()
elif unit==3:
    u1=uc.uc(value)
    u1.cm_to_inches()
elif unit==4:
    u1=uc.uc(value)
    u1.inches_to_cm()
else:
    print('Enter a valid option:')
'''