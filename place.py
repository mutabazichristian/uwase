class Place:
    def __init__(self, name, country, priority, visited):
        self.name = name
        self.country = country
        self.priority = priority
        self.visited = visited

    def __str__(self):
        return f"{self.name} in {self.country}, priority {self.priority} {'visited' if self.visited else '(not visited)'}"

    # mark_visited
    def mark_visited(self):
        self.visited = True

    # mark_unvisited
    def mark_unvisited(self):
        self.visited = False

    # is_important
    def is_important(self):
        return self.priority <= 2

    def __l__(self, other):
        return self.priority < other.priority
