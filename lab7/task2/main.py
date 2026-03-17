from models import Car, ElectricCar, Motorcycle, Vehicle


def demonstrate_vehicles():
    vehicles = [
        Car("Toyota", "Corolla", 2023, mileage=14500),
        ElectricCar("Tesla", "Model Y", 2025, mileage=8200, battery_capacity_kwh=75.0),
        Motorcycle("Yamaha", "MT-07", 2024, mileage=3200, engine_cc=689),
        ElectricCar("Hyundai", "Ioniq 5", 2024, 18500, battery_capacity_kwh=72.6),
    ]
    
    print("=== Vehicle Fleet Demonstration ===\n")
    
    for v in vehicles:
        print(v)
        print(f"  Purpose : {v.describe_purpose()}")
        print(f"  Start   : {v.start_engine()}")
        
        if isinstance(v, Car):
            print(f"  Honk    : {v.honk()}")
        if isinstance(v, Motorcycle):
            print(f"  Trick   : {v.wheelie()}")
        if isinstance(v, ElectricCar):
            print(f"  Charge  : {v.charge(92)}")
            print(f"  Charge  : {v.charge(120)}")
        
        print(f"  Stop    : {v.stop_engine()}")
        print("-" * 65)


if __name__ == "__main__":
    demonstrate_vehicles()