import urllib.request
import json
import webbrowser

def print_program_menu():
    print("\n--------")
    print("Welcome to Plot the ISS:")
    print("Option one and two both redirect to a map.")
    print("1. Where is the ISS?")
    print("2. Verify the location")
    print("3. Exit")

def get_iss_location():
    URL = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(URL)
    data = json.loads(response.read())
    return data["iss_position"]["latitude"], data["iss_position"]["longitude"]

def open_map_with_coordinates(lat, lon):
    open_map = "https://www.openstreetmap.org/?mlat=" + str(lat) + "&mlon=" + str(lon) + "#map=5/" + str(lat) + "/" + str(lon)
    webbrowser.open_new(open_map)

def open_nasa_tracking_map():
    open_NASA = "https://spotthestation.nasa.gov/tracking_map.cfm"
    webbrowser.open_new(open_NASA)

def main():
    done = False
    while not done:
        print_program_menu()
        user_option = input("Enter option: ")
        
        if user_option.isdigit() and 1 <= int(user_option) <= 3:
            numeric_option = int(user_option)
            
            if numeric_option == 1:
                lat, lon = get_iss_location()
                open_map_with_coordinates(lat, lon)
            elif numeric_option == 2:
                open_nasa_tracking_map()
            else:
                print("Thanks for using 'Plot the ISS'!")
                done = True
        else:
            print("Option invalid")

if __name__ == "__main__":
    main()
