# Vehicle Routing for Medical Supply Chain Optimization

## Introduction

There is a lack of affordable access to many important medications in the Arab world. Some of these medicationsa are available in neighboring countries at reasonable prices. If these medications can be distributed effectively taking advantage of existing transport between the countries, then these crucial medications can be made more plentiful and affordable. To minimize the cost of medications and take advantage of this opportunity for arbitrage, transport of medications from airports to consumers must be as efficient as possible. We solve this problem as a vehicle routing problem where the objective is to minimize the overall cost of deliveries given a fleet of vehicles with limited capacities. We formulate this as a quantum constrained binary optimization problem which is solved using quantum annealing with D-Wave's superconducting hardware.

## QUBO Objective

First, consider the case where there is a single airport where medication can be delivered and the medication must be delivered at the lowest cost possible by a fleet of delivery vehicles. These vehicles are limited in capacity and how far they can travel in one day. To solve this problem efficiently with VQE, we first formalize it as a constrained optimization problem:

Consider when there are $M$ vehicles and $N$ delivery locations. 

Let $x_{i, j, k}$ be an indicator variable such that $x_{i, j, k} = 1$ if vehicle $i$ visits dropoff location $j$ at stop number $k$ on its route and $x_{i, j, k} = 0$ otherwise.

Number each of the delivery locations $1$ to $N+1$ where the final location is the airport where the vehicles must start and end.

Since each vehicle must start at the airport, the cost for all vehicles to go to the first destination is 
$$\sum\limits_{m=1}^M\sum\limits_{n=1}^N x_{m,n,1}C_{N+1, n}$$
the cost of each vehicle to go from its final destination back to the airport is
$$\sum\limits_{m=1}^M\sum\limits_{n=1}^N x_{m,n,N}C_{n, N+1}$$
and the cost of the vehicle to go between all of its destinations in the middle is
$$\sum\limits_{m=1}^M\sum\limits_{n=1}^{N-1}\sum\limits_{i=1}^{N+1}\sum\limits_{j=1}^{N+1} x_{m,i,n}x_{m,j,n+1}C_{i,j}$$

By combining these terms, we can achieve the objective function for this problem:
$$\sum\limits_{m=1}^M\sum\limits_{n=1}^N x_{m,n,1}C_{N+1, n} + \sum\limits_{m=1}^M\sum\limits_{n=1}^N x_{m,n,N}C_{n, N+1} + \sum\limits_{m=1}^M\sum\limits_{n=1}^{N-1}\sum\limits_{i=1}^{N+1}\sum\limits_{j=1}^{N+1} x_{m,i,n}x_{m,j,n+1}C_{i,j}$$

## Constraints

However, we must also include practical constraints. First, we want the vehicles to drop off all of the medication, which means that each vertex must be visited at least once. Since the input to this method is a fully connected graph that follows the triangle inequality, it follows that each vertex should only be visited only once. Thus we add the constraint

$$\forall j \in [N+1], \sum\limits_{m=1}^M\sum\limits_{k=1}^{N+1} x_{m,j,k} = 1$$

Next, it is only feasible for a vehicle to be in one location at a time. This constraint can be represented as

$$\forall i \in [M], k \in [N+1], \sum\limits_{j=1}^{N+1} x_{i, j, k} == 1$$

Finally, vehicles are constrained in how far they can drive in one trip. If vehicle $i$ can travel at must $d_i$, this constraint can be expressed as

$$\forall i \in [M], \sum\limits_{a=1}^{N+1}\sum\limits_{b=1}^{N+1}\sum\limits_{k=1}^N x_{i,a,k}x_{i,b,k+1}C_{i,j} \leq d_i$$