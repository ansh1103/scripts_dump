"""
Problem
A city has N Tram stations numbered from 1 to N  that are connected to one another and form a circle. You are given an array ticket_cost  where ticket_cost[i] is the cost of a ticket between the stops number i and (i + 1) % N. The Tram can travel in both directions i.e. clockwise and anti-clockwise.

Return the minimum cost to travel between the given start and finish station.

You are given an integer N where N represents the total number of the tram stations, an integer start which represents the start station, and an integer finish which represents the finish station. You are given an array of positive integers  ticket_cost where ticket_cost[i] represents the ticket cost between the station number i and (i + 1) % N.

Task

Determine the minimum cost to travel between the given start and finish station.

Example

Assumptions

N = 4
start = 1
finish = 4
ticket_cost = [1, 2, 2, 4 ]
Approach

path1 -> 1------1-----> 2 -------2------> 3 -------2------> 4 . => 1+2+2 => 5

path2 -> 1------4------>4 . => 4

Path2 will give the minimum cost. Therefore return 4.

Function description

Complete the Solve() function provided in the editor below that takes the following arguments and finds the minimum cost to travel between the given start and finish station:

N: Represents the total number of tram stations
start: Represents the start station
finish: Represents the finish station
ticket_cost: Represents ticket_cost[i] denoting the ticket-cost between the station number i and (i + 1) %N
Input format

The first line contains an integer N denoting the total number of tram stations.
The second line contains an integer start denoting the start station.
The third line contains an integer finish denoting the finish station.
The fourth line contains an N space-separated integer array ticket_cost, ticket_cost[i] represents the ticket-cost between the station number i and (i + 1) %N.
Output format

Return the minimum cost to travel between the given start and finish station.
"""

def solve (N, start, finish, Ticket_cost):
    # clockwise
    clockwise_cost_from_start_to_finish = 0
    station = start
    while (station!=finish):
        if station == N:
            clockwise_cost_from_start_to_finish += Ticket_cost[station -1]
            station = 0
            continue
        clockwise_cost_from_start_to_finish += Ticket_cost[station]
        station += 1

    # anti-clockwise cost calculation
    anticlockwise_cost_from_start_to_finish = 0
    station = start - 1
    while (station!=finish-1):
        if station == 0:
            anticlockwise_cost_from_start_to_finish += Ticket_cost[-1]
            station = N-1
            continue
        anticlockwise_cost_from_start_to_finish += Ticket_cost[station-1]
        station -=1

    return min(clockwise_cost_from_start_to_finish, anticlockwise_cost_from_start_to_finish)


N = int(input())
start = int(input())
finish = int(input())
Ticket_cost = list(map(int, input().split()))

out_ = solve(N, start, finish, Ticket_cost)
print (out_)