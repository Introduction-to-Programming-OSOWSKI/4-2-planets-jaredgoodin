def planets(p): 

    for i in range(0, len(planet)):
        if p == planet[i]:
            return i
        
    return p + "is not a planet"
    
    
    
planet = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]
print (planets("earth"))