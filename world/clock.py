class Clock:
    #One tick = one in-game minute.

    def __init__(self, day: int = 1, hour: int = 8, minute: int = 0):
        self.day = day
        self.hour = hour
        self.minute = minute

    def tick(self) -> None:
        #+ one minute.
        self.minute += 1

        if self.minute >= 60:
            self.minute = 0
            self.hour += 1

        if self.hour >= 24:
            self.hour = 0
            self.day += 1

    def current_time(self) -> str:
            return f"Day {self.day} - {self.hour:02}:{self.minute:02}"