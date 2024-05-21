class DamageCalculator:
    """
    Class to calculate the total damage dealt
    """
    
    def __init__(self):
        """
        Constructor to initialize the time and seconds dictionary
        """
        self.time_and_seconds = {
            "second": 1,
            "minute": 60,
            "hour": 3600,
            "day": 86400,
            "week": 604800,
            "month": 2628000,
            "year": 31536000
        }
    
    def damage(self, damage: int, speed: int, time: str) -> int:
        """
        This method calculates the total damage dealt based on the amount of damage per second,
        the time the damage is dealt, and the time unit of the speed.

        Args:
            damage (int): The amount of damage per second.
            speed (int): The speed at which the damage is dealt.
            time (str): The time unit of the speed.

        Returns:
            int: The total damage dealt.

        Raises:
            ValueError: If either damage or speed is negative, or if time is not a valid time unit.
        """
        
        # The user could input the time in capital letters, so we convert it to lowercase
        time = time.lower()
        
        if damage < 0 or speed < 0:
            raise ValueError("Damage and speed must be non-negative.")
        
        if time not in self.time_and_seconds:
            raise ValueError(f"'{time}' is not a valid time unit. \nValid time units are: {', '.join(self.time_and_seconds.keys())}")
        
        return damage * speed * self.time_and_seconds[time]
        