import math
import random
class PopulationBasedSampleSize:
    """
    Calculate the sample size using the population size.

    Args:
        population_size (int): The size of the population.

    Returns:
        None
    """
    def __init__(self, population_size):
        """
        Initializes an instance of the class with the given population size.

        Parameters:
            population_size (int): The size of the population.

        Returns:
            None
        """
        self.population_size = population_size
    def calculate_sample_size(self):
        """
        Calculate the sample size using the population size.

        Parameters:
            self.population_size (int): The size of the population.

        Returns:
            float: The calculated sample size.
        """
        if self.population_size <= 100:
            return 0.25*self.population_size
        return math.ceil(math.sqrt(self.population_size) * math.log(self.population_size, 10)*10)
class MarginOfErrorSampleSize:
    ''''''
    def __init__(self, confidence_level, margin_of_error, population_proportion):
        self.confidence_level = confidence_level
        self.margin_of_error = margin_of_error
        self.population_proportion = population_proportion

    def calculate_sample_size(self):
        """
        Calculates the sample size needed for a given population proportion and margin of error.

        Parameters:
            self (object): The instance of the class.

        Returns:
            int: The calculated sample size rounded to the nearest whole number.
        """
        z_score = 1.96  # For 95% confidence level
        p = self.population_proportion
        e = self.margin_of_error

        sample_size = (z_score**2 * p * (1 - p)) / e**2
        return round(sample_size)

class StratifiedSampleSize:
    def __init__(self, strata_sizes, population_size):
        """
        Initializes the instance with the given strata_sizes and population_size.

        Parameters:
            strata_sizes (list): A list of strata sizes.
            population_size (int): The total population size.

        Returns:
            None
        """
        self.strata_sizes = strata_sizes
        self.population_size = population_size

    def calculate_sample_size(self, total_sample_size):
        """
        Calculate the sample sizes for each stratum based on the total sample size and the population size.

        Parameters:
            total_sample_size (int): The total sample size to be allocated across strata.

        Returns:
            list: A list of sample sizes for each stratum.
        """
        sample_sizes = [round(total_sample_size * size / self.population_size) for size in self.strata_sizes]
        return sample_sizes


class SimpleRandomSampleSize:
    def __init__(self, population_size):
        self.population_size = population_size

    def calculate_sample_size(self):
        n = self.population_size / (1 + (self.population_size - 1) / self.population_size)
        return round(n)


class FixedPercentageSampleSize:
    def __init__(self, dataset_size, percentage):
        self.dataset_size = dataset_size
        self.percentage = percentage

    def calculate_sample_size(self):
        sample_size = round(self.dataset_size * self.percentage)
        return sample_size

class TimeBasedSampleSize:
    def __init__(self, start_time, end_time, total_time, dataset_size):
        self.start_time = start_time
        self.end_time = end_time
        self.total_time = total_time
        self.dataset_size = dataset_size

    def calculate_sample_size(self):
        time_fraction = (self.end_time - self.start_time) / self.total_time
        sample_size = round(self.dataset_size * time_fraction)
        return sample_size

class ClusterSampleSize:
    def __init__(self, total_clusters, clusters_in_sample, elements_per_cluster):
        self.total_clusters = total_clusters
        self.clusters_in_sample = clusters_in_sample
        self.elements_per_cluster = elements_per_cluster

    def calculate_sample_size(self):
        total_elements = self.total_clusters * self.elements_per_cluster
        sample_size = self.clusters_in_sample * self.elements_per_cluster
        return sample_size if sample_size <= total_elements else total_elements



