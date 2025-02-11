class Vehicle:
    def __init__(self, vehicle_id, vehicle_name, vehicle_type):
        self.vehicle_id = vehicle_id
        self.vehicle_name = vehicle_name
        self.vehicle_type = vehicle_type

    def vehicle(self):
        print(f"Moje vozidlo ma SPZ: {self.vehicle_id}, jeho meno je {self.vehicle_name} a je to {self.vehicle_type}.")

vozidlo = Vehicle(vehicle_id="BL652GB",vehicle_name="Afto",vehicle_type="Skoda")
vozidlo.vehicle()
