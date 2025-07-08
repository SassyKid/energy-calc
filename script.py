class EnergyTracker:
    def __init__(self):
        # Appliance consumption in kWh (average values)
        self.appliance_consumption = {
            'ac': {'window': 1.5, 'split': 0.8, 'central': 3.0},
            'refrigerator': 1.5,
            'washing_machine': 0.5,
            'tv': {'led': 0.1, 'lcd': 0.15, 'plasma': 0.3},
            'water_heater': 2.0,
            'lights': 0.015  # per bulb
        }
        self.house_types = ['apartment', 'independent_house', 'villa']
        self.ac_types = ['window', 'split', 'central']

    def get_user_input(self):
        print("\n=== Welcome to Energy Consumption Tracker ===")

        # Personal information
        self.name = input("Enter your name: ")
        self.area = input("Enter your area/city: ")
        self.age = int(input("Enter your age: "))

        # Housing information
        print("\n--- Housing Information ---")
        while True:
            print(f"Available house types: {', '.join(self.house_types)}")
            self.house_type = input("Enter your house type: ").lower()
            if self.house_type in self.house_types:
                break
            print("Invalid house type. Please try again.")

        self.num_bhk = int(input("Enter number of BHK: "))

        # AC information
        print("\n--- AC Information ---")
        self.has_ac = input("Do you have AC? (yes/no): ").lower() == 'yes'
        if self.has_ac:
            while True:
                print(f"Available AC types: {', '.join(self.ac_types)}")
                self.ac_type = input("Enter AC type: ").lower()
                if self.ac_type in self.ac_types:
                    break
                print("Invalid AC type. Please try again.")
            self.ac_hours = float(input("Enter average daily AC usage (hours): "))

        # Appliances
        print("\n--- Appliance Information ---")
        self.has_refrigerator = input("Do you have a refrigerator? (yes/no): ").lower() == 'yes'
        self.has_washing_machine = input("Do you have a washing machine? (yes/no): ").lower() == 'yes'

        # TV information
        self.has_tv = input("Do you have a TV? (yes/no): ").lower() == 'yes'
        if self.has_tv:
            self.tv_type = input("Enter TV type (LED/LCD/Plasma): ").lower()
            self.tv_hours = float(input("Enter average daily TV usage (hours): "))

        # Water heater
        self.has_water_heater = input("Do you have a water heater? (yes/no): ").lower() == 'yes'
        if self.has_water_heater:
            self.heater_hours = float(input("Enter average daily water heater usage (hours): "))

        # Lighting
        self.num_bulbs = int(input("Enter number of light bulbs in your house: "))
        self.light_hours = float(input("Enter average daily lighting usage (hours): "))

    def calculate_consumption(self):
        daily_consumption = 0

        # AC calculation
        if self.has_ac:
            ac_power = self.appliance_consumption['ac'][self.ac_type]
            daily_consumption += ac_power * self.ac_hours

        # Refrigerator (always on)
        if self.has_refrigerator:
            daily_consumption += self.appliance_consumption['refrigerator'] * 24

        # Washing machine (assuming 1 hour per day)
        if self.has_washing_machine:
            daily_consumption += self.appliance_consumption['washing_machine'] * 1

        # TV
        if self.has_tv and self.tv_type in ['led', 'lcd', 'plasma']:
            tv_power = self.appliance_consumption['tv'][self.tv_type]
            daily_consumption += tv_power * self.tv_hours

        # Water heater
        if self.has_water_heater:
            daily_consumption += self.appliance_consumption['water_heater'] * self.heater_hours

        # Lighting
        daily_consumption += self.appliance_consumption['lights'] * self.num_bulbs * self.light_hours

        monthly_consumption = daily_consumption * 30
        annual_consumption = daily_consumption * 365

        return {
            'daily': daily_consumption,
            'monthly': monthly_consumption,
            'annual': annual_consumption
        }

    def display_results(self, consumption):
        print("\n=== Energy Consumption Results ===")
        print(f"\nPersonal Information:")
        print(f"- Name: {self.name}")
        print(f"- Area: {self.area}")
        print(f"- Age: {self.age}")

        print("\nHousing Information:")
        print(f"- House Type: {self.house_type}")
        print(f"- Number of BHK: {self.num_bhk}")
        print(f"- Has AC: {'Yes' if self.has_ac else 'No'}")

        print("\nAppliance Usage:")
        print(f"- Refrigerator: {'Present' if self.has_refrigerator else 'None'}")
        print(f"- Washing Machine: {'Present' if self.has_washing_machine else 'None'}")
        print(f"- TV: {self.tv_type.upper() if self.has_tv else 'None'}")
        print(f"- Water Heater: {'Present' if self.has_water_heater else 'None'}")

        print("\nConsumption:")
        print(f"- Daily Consumption: {consumption['daily']:.2f} kWh")
        print(f"- Monthly Consumption: {consumption['monthly']:.2f} kWh")
        print(f"- Annual Consumption: {consumption['annual']:.2f} kWh")

    def run(self):
        self.get_user_input()
        consumption = self.calculate_consumption()
        self.display_results(consumption)


if __name__ == "__main__":
    tracker = EnergyTracker()
    tracker.run()
