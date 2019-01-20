## Bellman-Ford Algorithm

- Shortest path from one node to all other nodes.
- It works with negative edge weights, Dijkstra doesn't. Both doesn't work on negative cycles.
- Examine each node in every iteration and update the cost.
- Dijkstra is a greedy algorithm, Bellman-Ford doesn't.
- Time complexty is O(v*e), where v is the number of vertices and e is the number of edges.
- We need v-1 iterations to find the result, where v is the number of vertices.
- https://www.youtube.com/watch?v=obWXjtg0L64
