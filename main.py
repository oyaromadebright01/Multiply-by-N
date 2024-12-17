def multiply_single_iteration(N, M):
    return N * M

def multiply_n_iterations(N, M):
    result = 0
    for _ in range(N):
        result += M
    return result

# Example usage
N = 5
M = 3

single_iteration_result = multiply_single_iteration(N, M)
n_iterations_result = multiply_n_iterations(N, M)

print(f"Result using single iteration: {single_iteration_result}")
print(f"Result using N iterations: {n_iterations_result}")
