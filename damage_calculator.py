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
    
    def damage(self, damage: int, speed: int, time: str) -> int | str:
        """
        This method calculates the total damage dealt based on the amount of damage per second,
        the time the damage is dealt, and the time unit of the speed.

        Args:
            damage (int): The amount of damage per second.
            speed (int): The time the damage is dealt.
            time (str): The time unit of the speed.

        Returns:
            int | str: The total damage dealt. Returns "Invalid" if either damage or speed is negative.
        """
        if damage < 0 or speed < 0:
            return "Invalid"
        
        return damage * speed * self.time_and_seconds[time]
        