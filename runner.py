from k_means import *


class Runner:
    def __init__(self, seeds, k, points, num_iterations=10):
        self.seeds = list(range(seeds + 1))
        self.k = k
        self.num_iterations = num_iterations
        self.points = points
        self.SSE_list = []
        self.minimal_SSE = 0
        self.mean_SSE = 0
        self.maximal_SSE = 0

    def find_minimal(self):
        self.minimal_SSE = format(min(self.SSE_list), '.3f')

    def find_mean(self):
        self.mean_SSE = format(sum(self.SSE_list) / len(self.SSE_list), '.3f')

    def find_maximal(self):
        self.maximal_SSE = format(max(self.SSE_list), '.3f')

    def print_table(self):
        # print(f"{self.k} {self.maximal_SSE:.3f} {self.minimal_SSE:.3f} {self.mean_SSE:.3f}")
        print( str(self.k)+" "+self.maximal_SSE.rstrip("0")+" " + self.minimal_SSE.rstrip("0")+" " + self.mean_SSE.rstrip("0"))

    def start_running(self):
        km = KMeans(self.k, self.num_iterations)
        for seed in self.seeds:
            km.run(self.points, seed)
            self.SSE_list.append(km.SSE_state())
        self.find_minimal()
        self.find_mean()
        self.find_maximal()
        self.print_table()
