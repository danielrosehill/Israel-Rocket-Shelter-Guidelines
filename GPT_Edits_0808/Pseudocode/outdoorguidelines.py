def determine_outdoor_shelter(context, location):
    def go_to_nearest_building():
        # Instructions for entering a nearby building
        return "Find the nearest building, enter the building, proceed to a shelter or stairwell, and stay away from building entrances."

    def lie_on_ground():
        # Instructions for lying on the ground in an open area
        return "Lie on the ground, protect your head with your hands, and stay in this position until the siren stops and it is safe to move. Be aware of the blast wave that can generate dangerous fragments."

    # Determine shelter options based on context and location
    if context == 'outdoors':
        if location == 'built_up_area':
            return go_to_nearest_building()
        elif location == 'open_area':
            return lie_on_ground()
        else:
            return "Invalid location. Please specify 'built_up_area' or 'open_area'."
    else:
        return "Invalid context. Please specify 'outdoors'."

# Example usage
context = 'outdoors'  # Example context
location = 'built_up_area'  # Example location

shelter_instruction = determine_outdoor_shelter(context, location)
print(shelter_instruction)

context = 'outdoors'  # Example context
location = 'open_area'  # Example location

shelter_instruction = determine_outdoor_shelter(context, location)
print(shelter_instruction)
