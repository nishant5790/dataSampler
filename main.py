# This is a sample Python script for testing
import pandas as pd
from dataSampler.SampleSize import *
from dataSampler.SelectSampleData import *
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Example usage for selecting sample number :
    print('Example usage for selecting sample number \n')
    population_size = 100000
    ps = PopulationBasedSampleSize(population_size)
    print(f'The sample size is :{ps.calculate_sample_size()} \n' )

    # Example usage for selecting sample data :
    df_data = pd.read_csv('data/sample.csv')
    print('Example usage for selecting sample data \n')
    sample_list = []
    for idx, data in df_data.iterrows():
        sample_list.append((data['desc_md5_cs'], data['doc_occur_count']))
    ss = StatsSampling(sample_list, 20)
    print(f'The sample data is :\n {ss.run_sampler()} \n' )

