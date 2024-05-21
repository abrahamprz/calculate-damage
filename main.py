from damage_calculator import DamageCalculator

def main():
    damage_calculator = DamageCalculator()
    
    print(damage_calculator.damage(40, 5, "second"))
    print(damage_calculator.damage(100, 1, "minute"))
    print(damage_calculator.damage(2, 100, "hour"))
    

if __name__ == "__main__":
    main()