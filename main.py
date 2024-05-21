from damage_calculator import DamageCalculator

def main():
    damage_calculator = DamageCalculator()
    
    print(damage_calculator.damage(40, 5, "seconds"))
    print(damage_calculator.damage(100, 1, "mINUTE"))
    print(damage_calculator.damage(2, 100, "horas"))
    

if __name__ == "__main__":
    main()