#traffic signal
while True:
    ts= input("Watch The Light : (RED/YELLOW/GREEN)::")
    if ts == 'RED':
        print("Stop wait for light to turn green")       
    elif ts == 'YELLOW':
        print("Have patience wait for it to turn green")     
    elif ts == 'GREEN':
        print("Thank you for your patience, you can go now.")
        break
    else:
        print("Enter the Valid Option!!")
            