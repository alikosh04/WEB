from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, make, model, year, mileage=0.0):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self._is_running = False
    
    def start_engine(self):
        if self._is_running:
            return f"The {self.make} {self.model} is already running."
        self._is_running = True
        return f"The {self.make} {self.model}'s engine has started."
    
    def stop_engine(self):
        if not self._is_running:
            return f"The {self.make} {self.model} is already off."
        self._is_running = False
        return f"The {self.make} {self.model}'s engine has stopped."
    
    @abstractmethod
    def describe_purpose(self):
        pass
    
    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.mileage:.1f} km) - Running: {self._is_running}"


class Car(Vehicle):
    def __init__(self, make, model, year, mileage=0.0, num_doors=4, fuel_type="gasoline"):
        super().__init__(make, model, year, mileage)
        self.num_doors = num_doors
        self.fuel_type = fuel_type
    
    def honk(self):
        return "Beep beep!"
    
    def describe_purpose(self):
        return "Personal transportation and family commuting"
    
    def __str__(self):
        return f"{super().__str__()} | {self.num_doors}-door {self.fuel_type} car"


class ElectricCar(Car):
    def __init__(self, make, model, year, mileage=0.0, num_doors=4, battery_capacity_kwh=60.0):
        super().__init__(make, model, year, mileage, num_doors, "electric")
        self.battery_capacity_kwh = battery_capacity_kwh
        self._charge_level = 85.0
    
    def charge(self, percentage):
        if percentage < 0 or percentage > 100:
            return "Invalid charge percentage."
        self._charge_level = min(100.0, max(0.0, percentage))
        return f"Charged to {self._charge_level:.1f}%"
    
    def describe_purpose(self):
        return "Environmentally friendly personal transportation & commuting"
    
    def __str__(self):
        return f"{super().__str__()} | {self.battery_capacity_kwh} kWh battery ({self._charge_level:.1f}% charged)"


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, mileage=0.0, engine_cc=600):
        super().__init__(make, model, year, mileage)
        self.engine_cc = engine_cc
    
    def start_engine(self):
        if self._is_running:
            return f"The {self.make} {self.model} is already alive!"
        self._is_running = True
        return f"VROOOM! {self.make} {self.model} ({self.engine_cc}cc) roars to life!"
    
    def describe_purpose(self):
        return "Fast, agile urban and sport riding"
    
    def wheelie(self):
        if not self._is_running:
            return "Start the engine first!"
        return "↗️ Wheelie! Hold on tight!"
    
    def __str__(self):
        return f"{super().__str__()} | {self.engine_cc}cc motorcycle"