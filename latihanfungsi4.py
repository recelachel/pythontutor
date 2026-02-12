def countdown(n = 0):
    if n <= 0:
        print ("Done!")
    else :
        print(n)
        countdown(n-1)
    
countdown(5)