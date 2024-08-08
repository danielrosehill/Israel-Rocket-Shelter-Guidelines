def determine_private_transport_shelter(can_reach_building, can_leave_vehicle):
    def reach_building():
        # Instructions for reaching a building
        return "Stop the vehicle safely, exit quickly, and find and enter the nearest shelter or stairwell."

    def move_away_from_vehicle():
        # Instructions for moving away from the vehicle
        return "Stop the vehicle safely, exit the vehicle, move away to the side of the road or separation fence, lie down, and cover your head with your hands."

    def stay_in_vehicle():
        # Instructions for staying in the vehicle
        return "Stop the vehicle safely, and bend down below the window line."

    # Determine shelter options based on the situation
    if can_reach_building:
        return reach_building()
    elif can_leave_vehicle:
        return move_away_from_vehicle()
    else:
        return stay_in_vehicle()

# Example usage
can_reach_building = True  # Example scenario where you can reach a building
can_leave_vehicle = False  # Example scenario where you cannot leave the vehicle

shelter_instruction = determine_private_transport_shelter(can_reach_building, can_leave_vehicle)
print(shelter_instruction)

can_reach_building = False  # Example scenario where you cannot reach a building
can_leave_vehicle = True  # Example scenario where you can leave the vehicle

shelter_instruction = determine_private_transport_shelter(can_reach_building, can_leave_vehicle)
print(shelter_instruction)

can_reach_building = False  # Example scenario where you cannot reach a building
can_leave_vehicle = False  # Example scenario where you cannot leave the vehicle

shelter_instruction = determine_private_transport_shelter(can_reach_building, can_leave_vehicle)
print(shelter_instruction)
