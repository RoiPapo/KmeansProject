from sys import argv
import os
from point import Point
from k_means import KMeans
from runner import Runner


def load_data(input_path):
    """
    Loads data from given csv
    :param input_path: path to csv file
    :return: returns data as list of Point
    """
    points = []
    with open(input_path, 'r') as f:
        for row in f.readlines():
            row = row.strip()
            values = row.split(' ')
            points.append(Point(values[0], values[1:]))
    return points


def run_kmeans():
    if len(argv) < 4:
        print('Not enough arguments provided. Please provide 3 arguments: K, num_iterations, path_to_input')
        exit(1)
    k = int(argv[1])
    num_iterations = int(argv[2])
    input_path = argv[3]
    if len(argv) == 5:
        random_seed = int(argv[4])
    else:
        random_seed = 9

    if k <= 1 or num_iterations <= 0:
        print('Please provide correct parameters')
        exit(1)
    if not os.path.exists(input_path):
        print('Input file does not exist')
        exit(1)

    points = load_data(input_path)
    if k >= len(points):
        print('Please set K less than size of dataset')
        exit(1)
        print("K max min mean")
    runner1 = Runner(9, 3, points, 10)
    runner2 = Runner(9, 4, points, 10)
    runner3 = Runner(9, 5, points, 10)
    runner_list = [runner1, runner2, runner3]
    for runner in runner_list:
        runner.start_running()





    # runner = KMeans(k, num_iterations)
    # runner.run(points, random_seed)
    # runner.print_results()



if __name__ == '__main__':
    run_kmeans()
