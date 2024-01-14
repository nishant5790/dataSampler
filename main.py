# This is a sample Python script for testing
import pandas as pd
from tqdm import tqdm
tqdm.pandas()
from dataSampler.SampleSize import *
from dataSampler.SelectSampleData import *

if __name__ == '__main__':

    # Reading the data
    
    for idx,df_data in tqdm(enumerate(pd.read_csv('data/exp_ln_data.csv',chunksize=10000000))):
        print('Reading the data...')
    
        population_size = len(df_data)
        # print(df_data.head())
        # print(df_data.shape)
        
        print('Formatting the data...')
        data_format_list = list(zip(df_data['desc_md5_cs'],df_data['doc_occur_count']))
        # print(f'Formatted data is :\n {data_format_list[:10]}\n')
        
        # Example usage for selecting sample number :
        print('Selecting sample size...')
        ps = PopulationBasedSampleSize(population_size)
        sample_k = ps.calculate_sample_size()
        # print(f'The sample size is :{sample_k}\n' )

        # Example usage for selecting sample data :
        
        print('Selecting sample data...')
        ss = StatsSampling(data_format_list, sample_k)
        sampled_data = ss.run_sampler()
        
        df_sample = pd.DataFrame(sampled_data, columns =['desc_md5_cs','doc_occur_count'])
        # print(f'The sample data is :\n' )
        # print(f'Size of sampled data : {df_sample.shape}')
        print('Saving sample... ')
        output_file = f'data/sampleData/sample_data_{str(idx)}.csv' 
        df_sample.to_csv(output_file,index=False)
