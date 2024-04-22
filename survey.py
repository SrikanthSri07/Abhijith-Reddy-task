survey_details = {
    "District1": {
        "Taluk1": {
            "Village1": ["Survey1", "Survey2", "Survey3"],
            "Village2": ["Survey4", "Survey5"]
        },
        "Taluk2": {
            "Village3": ["Survey6", "Survey7"],
            "Village4": ["Survey8"]
        }
    },
    "District2": {
        "Taluk3": {
            "Village5": ["Survey9", "Survey10"],
            "Village6": ["Survey11"]
        },
        "Taluk4": {
            "Village7": ["Survey12", "Survey13"]
        }
    }
}

def get_survey_details():
    district = input("Enter district: ")
    taluk = input("Enter taluk: ")
    village = input("Enter village: ")
    survey = input("Enter survey number: ")

    try:
        survey_list = survey_details[district][taluk][village]
        if survey in survey_list:
            print(f"Survey number {survey} details:")
            # Add your code to provide details of the survey number here
        else:
            print("Survey number not found in the specified district, taluk, and village.")
    except KeyError:
        print("Invalid district, taluk, or village.")
get_survey_details()