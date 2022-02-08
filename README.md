# CPSC535_SavyyTraveller

We all know that air travel is dense in the US, there are so many flights one may choose from in order to fly from one point to another, with one or more hops. Assuming that you know what probability each flight is on time, you would like to calculate (i) what route will maximize the probability to arrive on time between two given cities, and (ii) what city is the most reliable travel destination. To simplify, we consider that between two nodes, there is the same probability to travel from one to another. In the real world, these probabilities are not the same, but we could consider the average of each direction as the common value.
Given a graph and two cities, we need to compute the path with the highest probability of on-time arrival. If the path has a single edge, then it will be the probability of that edge. If the path has multiple edges, then multiply all the probabilities.

Given a graph, for any city we consider the sum of all probabilities of on-time arrivals from each other city.

For example:
Input: The graph below, the source =A and the destination=F,

<img width="456" alt="Screen Shot 2022-02-07 at 9 11 49 PM" src="https://user-images.githubusercontent.com/71597613/152922656-16937808-0800-4165-8ec2-da7a3c4ebd03.png">


We need to compute: 
(i) what route will maximize the probability to arrive on time between A and F, and 
(ii) what city among {A, B, C, D, E, F, G, H} is the most reliable travel destination.
We work to compute the output for (i):
Between A-F we have many options:
path A-D-F will have the probability 0.9*0.6=0.54
path A-B-C-F will have the probability 0.8*0.8*0.9=0.576 (better than above)
path A-C-F will have the probability 0.7*0.9=0.63 (better than above).
There is no other path with larger probability so the path A-C-F with probability 0.63 is the first half of the output.
We work to compute the output for (ii):
For city A, the probability to arrive on time from all other cities is = 0.8 (from B) + 0.7 (from C) + 0.9 (from D) + 0.504 (from E) + 0.63 (from F) + 0.72 (from G) + 0.648 (from H)
Similarly we compute for cities B, C, D, E, F, G, H and we select the city with the highest sum.
Output: path A-C-F, probability 0.63, and city B.
