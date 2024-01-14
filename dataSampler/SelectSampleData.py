import random
import statistics


class StatsSampling:
    ''' This is a class for statistical sampling '''
    def __init__(self, data_stream, k):
        # initializing variables
        self.data_stream = data_stream
        self.k = k

    def get_median_mad(self, freq_list):
        median = statistics.median(freq_list)
        mad = statistics.median([abs(x - median) for x in freq_list])
        return median, mad

    def run_sampler(self):
        # Step 1: Calculate the median and MAD
        freq_list = [freq for _, freq in self.data_stream]
        median, mad = self.get_median_mad(freq_list)
        within_range = []
        outside_range = []
        # Step 2: Classify items based on (median-MAD) and (median+MAD)
        for item, freq in self.data_stream:
            if median - mad <= freq <= median + mad:
                within_range.append((item, freq))
            else:
                outside_range.append((item, freq))
        # Calculate K1 and K2
        total_items = len(self.data_stream)
        k1 = round(len(within_range) / total_items * self.k)
        k2 = self.k - k1
        # Step 3: Apply reservoir sampling for both groups
        if k1 + k2 > self.k:
            if k1 > k2:
                k1 = k1 - ((k1 + k2) - self.k)
            else:
                k2 = k2 - ((k1 + k2) - self.k)
        if k1 + k2 < self.k:

            if k1 < k2:
                k1 = k1 + (self.k - (k1 + k2))
            else:
                k2 = k2 + (self.k - (k1 + k2))

        # print(f' value of k1 : {k1} \n value of k2 : {k2}\n')
        # Perform reservoir sampling for in-range and out-range item frequencies
        if len(within_range) >= len(outside_range):
            k_in_range = min(k1, k2)
            k_out_range = max(k1, k2)
        else:
            k_in_range = max(k1, k2)
            k_out_range = min(k1, k2)
        # print(f' value of k_in_range : {k_in_range} \n value of k_out_range : {k_out_range}\n')
        l1 = self.reservoir_sampling(within_range, k_in_range)
        l2 = self.reservoir_sampling(outside_range, k_out_range)
        # Step 4: Merge selected samples
        final_sample = l1 + l2
        return final_sample

    def reservoir_sampling(self, data, k):
        if len(data) <= k:
            return [(item, _) for item, _ in data]
        reservoir = [(item, _) for item, _ in data[:k]]
        # Start from the (k+1)th element
        for i, (item, _) in enumerate(data[k:], start=k):
            j = random.randrange(0, i + 1)
            if j < k:
                reservoir[j] = (item, _)
        return reservoir

import random

class SamplingAlgorithms:
    '''
algorithms share the common theme of selecting a random or probabilistic subset of items from a larger set,
making them useful in various applications like data streaming, sampling large datasets, and approximating results efficiently.

1. Weighted Reservoir Sampling:
A variant of reservoir sampling where each item has a weight, and the probability of selection is proportional to its weight.

2. Stream Sampling Algorithms:
Algorithms like Vitter's Algorithm R and Algorithm Z are designed for streaming data and maintain a sample of items from a data stream.

3. Randomized Sampling Algorithms:
Algorithms like random sampling with replacement or without replacement, which use randomness to select a subset of elements.

4. Min-wise Hashing:
Often used for estimating similarity between sets, it involves using a hash function to select a minimum element from each set.

5. Priority Sampling:
In situations where items have priority levels, priority sampling selects items with a probability proportional to their priority.

6. Reservoir Sampling for Multisets:
An extension of reservoir sampling for dealing with multisets, where elements can appear more than once.
'''
    def __init__(self):
        self.sample = []

    def reservoir_sampling(self, data_stream, k):
        for i, item in enumerate(data_stream):
            if i < k:
                self.sample.append(item)
            else:
                j = random.randint(0, i)
                if j < k:
                    self.sample[j] = item

    def weighted_reservoir_sampling(self, data_stream, k, weights):
        for i, item in enumerate(data_stream):
            if i < k:
                self.sample.append(item)
            else:
                j = random.choices(range(i + 1), weights=weights[:i + 1])[0]
                if j < k:
                    self.sample[j] = item

    def random_sampling(self, data_stream, k):
        self.sample = random.sample(data_stream, k)

    def priority_sampling(self, data_stream, k, priorities):
        priority_sum = sum(priorities)
        cumulative_probabilities = [sum(priorities[:i + 1]) / priority_sum for i in range(len(priorities))]

        for _ in range(k):
            rand_num = random.random()
            selected_index = next(i for i, p in enumerate(cumulative_probabilities) if p >= rand_num)
            self.sample.append(data_stream[selected_index])

    def min_wise_hashing(self, sets, num_hashes):
        hash_values = [float('inf')] * len(sets)
        for _ in range(num_hashes):
            hash_functions = [random.randint(0, 10**9) for _ in range(len(sets))]
            for i, s in enumerate(sets):
                for item in s:
                    hash_values[i] = min(hash_values[i], hash(item) ^ hash_functions[i])
        return hash_values

    def reservoir_sampling_multiset(self, multisets, k):
        for multiset in multisets:
            for i, item in enumerate(multiset):
                if i < k:
                    self.sample.append(item)
                else:
                    j = random.randint(0, i)
                    if j < k:
                        self.sample[j] = item



