def Encoder_Func(data):

    mappings = {
        "City_Type": {
            "Suburban": 0,
            "Rural": 1,
            "Urban": 2
        },

        "Current_Car_Type": {
            "Sedan": 0,
            "SUV": 1,
            "Hatchback": 2,
            "Truck": 3
        },

        "Range_Anxiety_Level": {
            "Low": 0,
            "Medium": 1,
            "High": 2
        },

        "Gender": {
            "Male": 0,
            "Female": 1,
            "Other": 2
        },

        "Home_Charging_Possible": {
            "Yes": 1,
            "No": 0
        },

        "Subsidy_Available": {
            "Yes": 1,
            "No": 0
        }

    }

    for col, mapping in mappings.items():
        data[col] = data[col].map(mapping)

    return data
