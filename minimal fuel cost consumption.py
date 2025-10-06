class RoadTrip:
    def __init__(self):
        # Read number of destinations
        self.n = int(input("Enter number of destinations: "))
        # Read distances as list of integers
        self.distances = list(map(int, input("Enter the distances: ").split()))

    def calculate_min_cost(self):
        # Compute total sum of distances
        total_distance = sum(self.distances)
        # Minimum coins needed to balance to zero
        min_cost = abs(total_distance)
        return min_cost

    def display_result(self):
        result = self.calculate_min_cost()
        print("Minimum cost (coins needed):", result)


# Create an object and run
trip = RoadTrip()
trip.display_result()
