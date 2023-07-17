def Y_location(n):
    locationY = (n % 4)
    if n % 4 == 0:
        return 4
    else:
        return locationY
    
print(Y_location(8))