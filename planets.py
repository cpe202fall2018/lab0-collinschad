def weight_on_planets():
    weight = int(input("What do you weigh on earth? "))
    mars = weight * .38
    jupiter = weight * 2.34

    print("\nOn Mars you would weigh %.2f pounds." % mars)
    print("On Jupiter you would weigh %.2f pounds." % jupiter)



if __name__ == '__main__':
   weight_on_planets()
