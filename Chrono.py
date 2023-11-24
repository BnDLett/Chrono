from typing import override


class Chrono:
    """
    Represents a unit of time.

    Attributes:
        value (int | float): The numerical value of the time unit.
    """

    def __init__(self, value: int | float):
        """
        Constructs a `Chrono` object with the given value.

        Args:
            value (int | float): The numerical value of the time unit.
        """
        self.value = value


@override
class Hour(Chrono):
    """
    Represents a unit of time equal to 60 minutes.

    Attributes:
        value (int | float): The number of hours.
    """

    def __init__(self, value: int | float):
        """
        Constructs an `Hour` object with the given value.

        Args:
            value (int | float): The number of hours.
        """
        super().__init__(value)

    def to_minutes(self):
        """
        Converts the `Hour` object to a `Minute` object.
        """
        minutes = self.value * 60

        return Minute(minutes)

    def to_seconds(self):
        """
        Converts the `Hour` object to a `Second` object.
        """
        seconds = self.to_minutes().value * 60

        return Second(seconds)


@override
class Minute(Chrono):
    """
    Represents a unit of time equal to 60 seconds.

    Attributes:
        value (int | float): The number of minutes.
    """

    def __init__(self, value: int | float):
        """
        Constructs a `Minute` object with the given value.

        Args:
            value (int | float): The number of minutes.
        """
        super().__init__(value)

    def to_hours(self):
        """
        Converts the `Minute` object to an `Hour` object.
        """
        hours = self.value / 60

        return Hour(hours)

    def to_seconds(self):
        """
        Converts the `Minute` object to a `Second` object.
        """
        seconds = self.value * 60

        return Second(seconds)


@override
class Second(Chrono):
    """
    Represents a unit of time equal to 1/60th of a minute.

    Attributes:
        value (int | float): The number of seconds.
    """

    def __init__(self, value: int | float):
        """
        Constructs a `Second` object with the given value.

        Args:
            value (int | float): The number of seconds.
        """
        super().__init__(value)

    def to_minutes(self):
        """
        Converts the `Second` object to a `Minute` object.
        """
        minutes = self.value / 60

        return Minute(minutes)

    def to_hours(self):
        """
        Converts the `Second` object to an `Hour` object.
        """
        hours = self.to_minutes().value / 60

        return Hour(hours)


if __name__ == "__main__":
    hour = Hour(5)
    minute = hour.to_minutes()
    second = hour.to_seconds()

    print(f"Hours: {hour.value}\nMinutes: {minute.value}\nSeconds: {second.value}")
