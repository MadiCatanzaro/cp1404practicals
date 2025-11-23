"""
Band Class
"""


class Band:
    """Band class which represents a band object."""

    def __init__(self, name=""):
        """Initialise band class."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return string representation of band class."""
        return f"{self.name} ({self.musicians}))"  # Output of this line is in the incorrect format

    def add(self, musician):
        """Add a musician to the list of musicians."""
        self.musicians.append(musician)

    def play(self):
        """Display the instruments each musician plays, and whether the musician requires an instrument - if they do not
        already have one."""
        for musician in self.musicians:
            if not musician.instruments:
                print(f"{musician.name} needs an instrument!")
            else:
                print(f"{musician.name} is playing: {musician.instruments[0]}")
        return None
    # band.play() returns None in the console
