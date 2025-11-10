class Knight:
    def __init__(self, name):
        self._name = name
        self._title = None
        self._favorite_color = None
        self._quest = None
        self._comment = None

        # Read the knight data from file
        try:
            with open("knights.txt", "r") as f:
                for line in f:
                    parts = [p.strip() for p in line.strip().split(",")]
                    if len(parts) != 5:
                        continue  # skip invalid lines
                    n, t, color, quest, comment = parts
                    if n.lower() == name.lower():
                        self._title = t
                        self._favorite_color = color
                        self._quest = quest
                        self._comment = comment
                        break
        except FileNotFoundError:
            raise FileNotFoundError("knights.txt not found. Please provide the data file.")

        # If knight not found
        if self._title is None:
            raise ValueError(f"No knight found with name '{name}'")

    # Read-only properties
    @property
    def name(self):
        return self._name

    @property
    def title(self):
        return self._title

    @property
    def favorite_color(self):
        return self._favorite_color

    @property
    def quest(self):
        return self._quest

    @property
    def comment(self):
        return self._comment
