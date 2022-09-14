def print_program_menu(): #this function was created to print the menu
    print("\n--------")
    print( "Welcome to the Plot the ISS:")
    print("Option one and two both redirect to a map.")
    print("1. Where is the ISS?")
    print("2. Verify the location")
    print("3. Exit")



def main():
    done = False
    while not done:
        print_program_menu()
        userOption = input("Enter option: ")
        if userOption.isdigit()== False or int(userOption) <=0 or int(userOption)>3:
          print()
          print("Option invalid")
        else:# This Verify that a number was input
         numericOption = int(userOption)
         if numericOption ==1:
            import urllib.request
            import json
            import webbrowser
            URL= "http://api.open-notify.org/iss-now.json"
            answer=urllib.request.urlopen(URL)
            obj = json.loads(answer.read())
            lat=obj["iss_position"]["latitude"]
            lon=obj["iss_position"]["longitude"]
            open_map="https://www.openstreetmap.org/?mlat=" + str(lat) + "&mlon=" + str(lon)+"#map=5/" + str(lat)+"/" + str(lon)
            webbrowser.open_new(open_map)
         if numericOption ==2:
            import urllib.request
            import webbrowser
            open_NASA="https://spotthestation.nasa.gov/tracking_map.cfm"
            webbrowser.open_new(open_NASA)

         elif numericOption == 3:
           print("Thanks for using 'Plot the ISS!")
           done=True

if __name__ == "__main__":
    main()

