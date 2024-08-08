def determine_public_transport_shelter(transport_type):
    def intercity_bus_or_student_transport():
        # Instructions for intercity buses or student transportation
        driver_actions = "Driver stops the vehicle at the side of the road and opens the doors."
        passenger_actions = "Passengers bend below the window line and protect their heads with their hands."
        return driver_actions + " " + passenger_actions

    def city_bus():
        # Instructions for city buses
        driver_actions = "Driver stops on the side of the road and opens the doors for passengers to disembark."
        passenger_actions = ("Passengers enter a nearby building. "
                             "If unable to reach a building, bend below the window line and protect their heads with their hands.")
        return driver_actions + " " + passenger_actions

    def train():
        # Instructions for trains
        driver_actions = "Driver slows down to a speed of 30 KM/H for 10 minutes."
        passenger_actions = "Passengers bend below the window line in the carriages and protect their heads with their hands."
        return driver_actions + " " + passenger_actions

    # Determine shelter options based on type of transport
    if transport_type == 'intercity_bus' or transport_type == 'student_transportation':
        return intercity_bus_or_student_transport()
    elif transport_type == 'city_bus':
        return city_bus()
    elif transport_type == 'train':
        return train()
    else:
        return "Invalid transport type. Please specify 'intercity_bus', 'student_transportation', 'city_bus', or 'train'."

# Example usage
transport_type = 'intercity_bus'  # Example transport type
shelter_instruction = determine_public_transport_shelter(transport_type)
print(shelter_instruction)

transport_type = 'city_bus'  # Example transport type
shelter_instruction = determine_public_transport_shelter(transport_type)
print(shelter_instruction)

transport_type = 'train'  # Example transport type
shelter_instruction = determine_public_transport_shelter(transport_type)
print(shelter_instruction)
