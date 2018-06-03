import numpy as np

RUNS = 20
OUTPUTS = 10

def get_measures(csv_array, filename):
    # Separate into two different lists according to the direction
    dir_one_list = filter(lambda x: x[3] == 1, csv_array)
    dir_minus_one_list = filter(lambda x: x[3] == -1, csv_array)

    # Calculate the rate for each of the lists
    array_one_direction = calc_rate(dir_one_list)
    array_minus_one_direction = calc_rate(dir_minus_one_list)

    # Connect lists and create an array
    array_one_direction.extend(array_minus_one_direction)
    array_rate = np.asarray(array_one_direction)

    # Sort the array by the index column
    sorted_array = sorted(array_rate, key = lambda x:x[0])
    sorted_array = np.asarray(sorted_array)

    # get array without index column
    rate_array = sorted_array[:,1]

    # save to file
    np.savez_compressed(filename, rate_array)


def calc_rate(list):
    array_rate = []

    # for the last cell to 0 (not include 0) descending order
    for i in range(len(list)-1, 0, -1):
        calc = list[i][2] / (list[i][1] - list[i-1][1])
        array_rate.append([list[i][0], calc])
    return array_rate


def pre_process():
    in_format = 'data/run.{0}/out.{1}.csv'
    out_format = 'data/run.{0}/out.{1}.npz'
    for i in range(1, RUNS + 1):
        for j in range(1, OUTPUTS + 1):
            current_file = in_format.format(i, j)
            output = out_format.format(i, j)
            file = np.genfromtxt(current_file, delimiter=';')
            get_measures(file, output)

pre_process()
#file1=np.genfromtxt('data/run.1/out.1.csv', delimiter=';')
#get_measures(file1, 'data/run.1/out.1.youtube.com/1.youtube.npz' )
