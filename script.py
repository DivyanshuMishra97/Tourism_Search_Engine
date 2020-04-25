destinations=["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cario, Egypt"]
test_traveler=['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
def get_destination_index(destination):
  destination_index=destinations.index(destination)
  return destination_index
print(get_destination_index("Los Angeles, USA"))


def get_traveler_location(traveler):
  traveler_destination=traveler[1]
  traveler_destination_index=get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index=get_traveler_location(test_traveler)
print(test_destination_index)

attractions=[[], [], [], [], []]
print(attractions)


#error-------------------------------------------------------------------------


def add_attraction(destination,attraction):
  try:
    destination_index=get_destination_index(destination)
    attractions_for_destination=attractions[destination_index]
    attractions_for_destination.append(attraction)
    return attraction_for_destination
  except ValueError:
    print("Error Caught")
    return
  
  add_attraction(['Venice Beach', ['beach']])
  print(attractions)









