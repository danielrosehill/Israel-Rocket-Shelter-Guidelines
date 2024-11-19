def determine_shelter(time_available, shelter_options, building_floors):
    def go_to_priority_1_shelter(shelter):
        # Instructions to reach and secure Priority 1 shelters
        return f"Go to {shelter}, close the door by turning the handle 90 degrees, and ensure both the steel window and inner glass window are closed."

    def go_to_inner_stairwell(building_floors):
        # Instructions to reach and secure an inner stairwell
        if building_floors > 3:
            return "Go to an inner stairwell with at least two floors above it, sit on the stairs, not in the floor space."
        else:
            return "Go to the middle floor stairwell, sit on the stairs, not in the floor space."

    def go_to_non_protected_room():
        # Instructions to reach and secure a non-protected room
        return "Go to a non-protected room with few outside walls and few openings, sit in an inner corner below the window line, not facing the door. Avoid kitchens, bathrooms, and toilets."

    # Check available shelter options based on priority
    if 'mamad' in shelter_options:
        return go_to_priority_1_shelter('Mamad (apartment’s designated protected space)')
    elif 'mamak' in shelter_options:
        return go_to_priority_1_shelter('Mamak (floor’s protected space)')
    elif 'mamam' in shelter_options:
        return go_to_priority_1_shelter('Mamam (institutional safe space)')
    elif 'miklat' in shelter_options:
        return go_to_priority_1_shelter('Public shelter (miklat tzi\'buri)')
    elif 'inner_stairwell' in shelter_options:
        return go_to_inner_stairwell(building_floors)
    else:
        return go_to_non_protected_room()

# Example usage
time_available = 5  # Example time available
