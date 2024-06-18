# General components of the VRP problem

from dimod import (
    Binary,
    BinaryQuadraticModel,
)

class VehicleRoutingProblem:
    def construct_objective(num_locations, distances, num_vehicles):
        """Returns the set of binary variables and the objective function"""

        M = num_vehicles
        N = num_locations

        # Create all the variables: one for each vehicle/location/position combo
        # k is timestep, j is vertex, i is vehicle
        x = {(i, j, k): Binary(str(i) + "_" + str(j) + "_" + str(k)) for k in range(N) for j in range(N+1) for i in range(M)}

        # Define the unconstrained binary optimization problem
        obj = BinaryQuadraticModel(vartype="BINARY")

        # The cost of going from the depot to the first stop
        for m in range(M):
            for n in range(N):
                obj += x[m, n, 0] * distances[N][n]

        # The cost of going from the last stop to the depot
        for m in range(M):
            for n in range(N):
                obj += x[m, n, N-1] * distances[n][N]

        # The cost of going between all stops in the middle
        for m in range(M):
            for n in range(N-1):
                for i in range(N+1):
                    for j in range(N+1):
                        obj += x[m, i, n] * x[m, j, n + 1] * distances[i][j]

        return x, obj