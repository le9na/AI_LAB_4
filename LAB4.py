# Lab 4

class DFS:
    def __init__(self, size=12):
        self.N = size
        self.Acc = [False] * self.N  # A visited array to mark which vertices have been visited while doing the DFS
        self.parent = [None] * self.N  # To track the path
        self.queue = []
        self.setup_graph(size)
        print("+-----------------------------------------+")
        print()

    def setup_graph(self, size):
        self.G = [[False] * self.N for _ in range(self.N)]
        edges = [
            (0, 1), 
            (0, 8), 
            (0, 4),
            (1, 2), 
            (1, 3),
            (2, 6),
            (3, 4), 
            (3, 5),
            (6, 7),
            (8, 9),
            (9, 10),
            (10, 11)
        ]
        for u, v in edges:
            self.G[u][v] = self.G[v][u] = True

    # Perform a DFS starting at node start
    def dfs(self, start, goal):
        self.queue.append(start)
        self.Acc[start] = True
        print("Queue: ")
        print(f"[ {self.ret_city(self.queue[-1])} ]")
        print()

        while self.queue:
            current = self.queue.pop()

            if goal == current:
                print(f"\nThe goal is {self.ret_city(goal)}, it has been reached\n\n")
                self.print_path(start, goal)
                return

            print(f"\t\t+--  Now in: {self.ret_city(current)}  --+")
            add_to_q = f"{self.ret_city(current)} is not the goal, \n[ "

            for i in range(self.N):
                if not self.Acc[i] and self.G[current][i]:
                    self.queue.append(i)
                    self.Acc[i] = True
                    self.parent[i] = current  # Track the parent
                    add_to_q += f"{self.ret_city(i)} "

            add_to_q += "] are added to the queue.\n"
            print("+-----------------------------------------+")
            print(add_to_q)

            print("The Queue: \n")
            for i in self.queue:
                print(f"{self.ret_city(i)}\n")
            print("+-----------------------------------------+")

    # Method to print the path from start to goal
    def print_path(self, start, goal):
        path = []
        current = goal
        while current is not None:
            path.append(current)
            current = self.parent[current]
        path.reverse()  # Reverse the path to get it from start to goal

        print("Path from start to goal:")
        for node in path:
            print(f"{self.ret_city(node)}", end=" > ")
        print("Goal reached")

    @staticmethod
    def ret_city(i):
        cities = ["Buraydah", "Unayzah", "AlZulfi", "Al-Badai",
                  "Riyadh-Alkhabra", "AlRass", "UmSedrah", "Shakra",
                  "Al-Bukayriyah", "Sheehyah", "Dhalfa", "Mulida"]
        return cities[i]


if __name__ == "__main__":
    print("\nChoose a city number to start: \n")
    for i in range(12):
        print(f"{DFS.ret_city(i)} city[{i}]")
    print("\nInput: ", end="")
    choosen_city = int(input())

    print("\nChoose a city number for the goal: ")
    print("\nInput: ", end="")
    goal = int(input())

    choice = DFS()  # Size
    choice.dfs(choosen_city, goal)
