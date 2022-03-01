# CPSC535_SavvyTraveller

Team Members:

1. Shivangi Shakya shivangishakya@csu.fullerton.edu
2. Saoni Mustafi saonimustafi@csu.fullerton.edu
3. Nick Bidler Nbidler@csu.fullerton.edu

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

For city A, the probability to arrive on time from all other cities is = 0.8 (from B) + 0.7 (from C) + 0.9 (from D) + 0.504 (from E) + 0.63 (from F) + 0.72 (from G) + 0.648 (from H) = 4.902

For city B, the probability to arrive on time from all other cities is = 0.8 (from A) + 0.8 (from C) + 0.72 (from D) + 0.6 (from E) + 0.72 (from F) + 0.576 (from G) + 0.51 (from H) = 4.73

For city C, the probability to arrive on time from all other cities is = 0.7 (from A) + 0.8 (from B) + 0.63 (from D) + 0.72 (from E) + 0.9 (from F) + 0.63 (from G) + 0.63 (from H) = 5.01

For city D, the probability to arrive on time from all other cities is = 0.9 (from A) + 0.72 (from B) + 0.63 (from C) + 0.48 (from E) + 0.6 (from F) + 0.8 (from G) + 0.72 (from H) = 4.85

For city E, the probability to arrive on time from all other cities is = 0.504 (from A) + 0.6 (from B) + 0.72 (from C) + 0.48 (from D) + 0.8 (from F) + 0.56 (from G) + 0.6 (from H) = 4.264

For city F, the probability to arrive on time from all other cities is = 0.63 (from A) +0.72  (from B) + 0.9 (from C) + 0.6 (from D) + 0.8 (from E) + 0.7 (from G) + 0.7 (from H) = 5.05

For city G, the probability to arrive on time from all other cities is = 0.72 (from A) +0.576  (from B) + 0.63 (from C) + 0.8 (from D) + 0.56 (from E) + 0.7 (from F) + 0.9 (from H) = 4.886

For city H, the probability to arrive on time from all other cities is = 0.648 (from A) +0.5184  (from B) + 0.63 (from C) + 0.72 (from D) + 0.6 (from E) + 0.7 (from F) + 0.9 (from G) = 4.7164

From the above calculations, city F turns out to be the most reliable city with maximum probability of 5.05

So the output of (i) and (ii) are -
Output: path A-C-F, probability 0.63, and city F.
