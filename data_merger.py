import pickle
import numpy as np


def merge_data(data_paths):
    '''
    merge datasets into one big dataset
    :param data_paths: list of paths to the data
    :return: combined dataset in numpy nd array
    '''
    datasets = []
    for path in data_paths:
        datasets.append(pickle.load(open(path, 'rb')))
    return np.concatenate(datasets, axis=0)