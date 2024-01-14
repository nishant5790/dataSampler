# This is a sample Python script for testing
import pandas as pd
from dataSampler.SampleSize import *
from dataSampler.SelectSampleData import *
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Example usage for selecting sample number :
    population_size = 100000
    ps = PopulationBasedSampleSize(population_size)
    print('The sample size is : ', ps.calculate_sample_size())

