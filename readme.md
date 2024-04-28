There is a lack of affordable access to many important medications in the Arab world. Some of these medications are available in neighboring countries at reasonable prices. If these medications can be distributed effectively taking advantage of existing transport between the countries, then these crucial medications can be made more plentiful and affordable. 
Our solution has three components.

# Part 1 - Mobile App

First, we developed an app that informs travelers of medications in need in the region and allows users in need of medication to make requests.

In this application, users are able to request medications that are unavailable or inaccessibly priced in their region.

![Image of the customer view](/images/customer_view.png)

Travelers who may have access to these medications are also able to register their flights so that our application can determine if there are any medications they could bring with them for those who need them. Travlers will be compensated for this assistance

![Image of the traveler view](/images/traveler_view.png)

Finally, the application takes all of the travelers and which medications they have access to as well as all of the customers and medications that they need and determines which medications travelers should pick up and how these can be optimally delivered to customers.

![Image of the customer view](/images/manager_view.png)

# Part 2 - Knapsack Problem

Next, there are many constraints on travelers on what medications they can travel with as well as space and weight constraints in terms of what they can add to luggage. Certain medications may also be needed more urgently than others. When there are many people in need of medication and many medications in the system, this optimization problem is complex. We can solve this problem as a knapsack problem on quantum hardware.

Additional details can be found in **multiple_knapsack.ipynb**

# Part 3 - Constrained Vehicle Routing Problem

Finally, to minimize the cost of medications and take advantage of this opportunity for arbitrage, transport of medications from airports to consumers must be as efficient as possible. We solve this problem as a vehicle routing problem where the objective is to minimize the overall cost of deliveries given a fleet of vehicles with limited capacities. We formulate this as a VQE algorithm which is solved using quantum annealing with D-Wave's superconducting hardware.

Additional details including a mathematical analysis can be found in **Vehicle Routing/vrp_constrained.ipynb**

# Additional 

Presentation: https://docs.google.com/presentation/d/1OoKNzceWWOMCj25XLEFtdThU6Msp-h_bmv9lNhq2nsM/edit#slide=id.p