import time
import random
import typing

def log_sorting_performance(
    sorting_algo1: typing.Callable[[list], list], 
    sorting_algo2: typing.Callable[[list], list], 
    input_generator: typing.Callable[[], list], 
    num_trials: int = 10
) -> dict:
    """
    Compare performance of two sorting algorithms across multiple trials.
    
    Args:
        sorting_algo1 (callable): First sorting algorithm to compare
        sorting_algo2 (callable): Second sorting algorithm to compare
        input_generator (callable): Function to generate input lists for sorting
        num_trials (int, optional): Number of performance trials to run. Defaults to 10.
    
    Returns:
        dict: Performance comparison results with timing and details
    """
    # Input validation
    if not callable(sorting_algo1) or not callable(sorting_algo2):
        raise ValueError("Both sorting algorithms must be callable functions")
    
    if num_trials < 1:
        raise ValueError("Number of trials must be at least 1")
    
    # Performance tracking variables
    results = {
        "algorithm1": {
            "name": sorting_algo1.__name__,
            "total_time": 0,
            "times": []
        },
        "algorithm2": {
            "name": sorting_algo2.__name__,
            "total_time": 0,
            "times": []
        },
        "num_trials": num_trials
    }
    
    # Run performance trials
    for _ in range(num_trials):
        # Generate input list
        input_list = input_generator()
        
        # Deep copy input for fair comparison
        input_list1 = input_list.copy()
        input_list2 = input_list.copy()
        
        # Time first algorithm
        start_time = time.time()
        sorted_result1 = sorting_algo1(input_list1)
        end_time = time.time()
        algo1_time = end_time - start_time
        results["algorithm1"]["times"].append(algo1_time)
        results["algorithm1"]["total_time"] += algo1_time
        
        # Time second algorithm
        start_time = time.time()
        sorted_result2 = sorting_algo2(input_list2)
        end_time = time.time()
        algo2_time = end_time - start_time
        results["algorithm2"]["times"].append(algo2_time)
        results["algorithm2"]["total_time"] += algo2_time
        
        # Verify sorting correctness
        if sorted_result1 != sorted_result2:
            raise ValueError("Sorting algorithms produce different results")
    
    # Calculate average times
    results["algorithm1"]["avg_time"] = results["algorithm1"]["total_time"] / num_trials
    results["algorithm2"]["avg_time"] = results["algorithm2"]["total_time"] / num_trials
    
    return results