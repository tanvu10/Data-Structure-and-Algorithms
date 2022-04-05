import heapq

num_testcase = int(input())
for _ in range(num_testcase):
    num_vertex, num_oneway, num_twoway, begin, destination  = map(int, input().split())
    graph = [[] for _ in range(num_vertex+1)]
    two_way_list = []
    for _ in range(num_oneway):
        start, stop , cost = map(int, input().split())
        graph[start].append((stop, cost))
    for _ in range(num_twoway):
        start, stop , cost = map(int, input().split())
        two_way_list.append((start, stop , cost))

    min_cost = 10e9
    for sta, sto, co in two_way_list:
        graph[sta].append((sto, co))
        heap = []
        dist = [10e9]*(num_vertex+1)
        dist[begin] = 0
        heapq.heappush(heap,(dist[begin], begin))
        while len(heap) > 0:
            current_weight, current_point = heapq.heappop(heap)
            if current_weight != dist[current_point]:
                continue
            for next_point, next_weight in graph[current_point]:
                if dist[current_point] + next_weight < dist[next_point]:
                    dist[next_point] = dist[current_point] + next_weight
                    heapq.heappush(heap, (dist[next_point], next_point))
        min_cost = min(min_cost, dist[destination])
        graph[sta].remove((sto, co))



    if min_cost == 10e9:
        print(-1)
    else:
        print(min_cost)