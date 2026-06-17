def build_graph(edge):
    graph = {}
    for u, v, cost in edge:
        # Nếu đỉnh chưa tồn tại thì tạo mới
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []

        # Thêm cạnh u -> v
        graph[u].append((v, cost))
        graph[v].append((u, cost))
    return graph

def dijkstra(graph, source):
    import heapq

    # Khởi tạo khoảng cách từ source đến tất cả đỉnh là vô cùng
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0
    parent = {vertex: None for vertex in graph}  # Lưu trữ đỉnh cha để truy vết đường đi
    # Sử dụng priority queue để lưu trữ các đỉnh theo khoảng cách ngắn nhất
    priority_queue = [(0, source)]  # (khoảng cách, đỉnh)
    visited = set()  # Tập hợp các đỉnh đã được xử lý

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Nếu khoảng cách hiện tại lớn hơn khoảng cách đã lưu, bỏ qua
        if current_distance > distances[current_vertex]:
            continue
        visited.add(current_vertex)

        # Duyệt qua các đỉnh kề của đỉnh hiện tại
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # Nếu tìm thấy đường đi ngắn hơn, cập nhật khoảng cách và thêm vào priority queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parent[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, parent

def shortest_route(graph, source, target):
    # Gọi Dijkstra
    dist, parent = dijkstra(graph, source)

    # Nếu không tìm thấy đường đi
    if dist[target] == float('inf'):
        return None, float('inf')
    
    # Truy vết đường đi từ target về source
    path = []
    current_vertex = target
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = parent[current_vertex]
    
    path.reverse()  # Đảo ngược để có đường đi từ source đến target
    return path, dist[target]

def demo_routing_shortest_path():
    # Tạo 1 đồ thị “mạng kho” (5–8 đỉnh: WH1, WH2, HCM, HN, DN…)
    edges = [
        ('WH1', 'HCM', 10),
        ('WH1', 'DN', 15),
        ('WH2', 'HCM', 5),
        ('WH2', 'HN', 20),
        ('HCM', 'DN', 10),
        ('DN', 'HN', 25)
    ]

    # Cho user nhập source, target.
    source = input("Nhập điểm xuất phát (WH1, WH2, HCM, HN, DN): ")
    target = input("Nhập điểm đích (WH1, WH2, HCM, HN, DN): ")

    # In: route + tổng chi phí.
    # Xây dựng đồ thị từ danh sách cạnh
    graph = build_graph(edges)
    path, cost = shortest_route(graph, source, target)
    if path:
        print(f"Đường đi ngắn nhất từ {source} đến {target}: {' -> '.join(path)} với tổng chi phí: {cost}")
    else:
        print(f"Không tìm thấy đường đi từ {source} đến {target}")
demo_routing_shortest_path()
    
# DSU (union-find)
def make_set(vertices):
    # Khởi tạo mỗi đỉnh là một tập riêng.

    parent = {}

    for v in vertices:
        parent[v] = v

    return parent


def find(parent, v):
    # Tìm gốc (root) của tập chứa v.

    while parent[v] != v:
        v = parent[v]

    return v


def union(parent, a, b):
   # Gộp hai tập chứa a và b.
    
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a != root_b:
        parent[root_b] = root_a


def kruskal_mst(vertices, edges):
    # Tìm cây khung nhỏ nhất (MST) bằng thuật toán Kruskal.

    # Bước 1: Sắp xếp các cạnh theo trọng số tăng dần.
    edges.sort(key=lambda x: x[0])  

    # Bước 2: Khởi tạo DSU
    parent = make_set(vertices)

    mst_edges = []  # Danh sách các cạnh trong MST
    total_cost = 0  # Tổng chi phí của MST

    # Bước 3: Duyệt qua các cạnh đã sắp xếp
    for u, v, cost in edges:
        root_u = find(parent, u)
        root_v = find(parent, v)

        # Nếu khác tập → thêm cạnh
        if root_u != root_v:

            mst_edges.append((u, v, cost))
            total_cost += cost

            union(parent, root_u, root_v)

        # Đủ |V|-1 cạnh thì dừng
        if len(mst_edges) == len(vertices) - 1:
            break

    return mst_edges, total_cost

def demo_kruskal_mst():
    # Dùng cùng tập kho như trên.
    edges = [
        ('WH1', 'HCM', 10),
        ('WH1', 'DN', 15),
        ('WH2', 'HCM', 5),
        ('WH2', 'HN', 20),
        ('HCM', 'DN', 10),
        ('DN', 'HN', 25)
    ]

    # Danh sách đường truyền được chọn. 
    vertices = ['WH1', 'WH2', 'HCM', 'HN', 'DN']

    # Tổng chi phí lắp đặt.
    mst_edges, total_cost = kruskal_mst(vertices, edges)
    print("Các cạnh trong cây khung nhỏ nhất (MST):")

    
    for u, v, cost in mst_edges:
        print(f"{u} -- {v} với chi phí: {cost}")
        print(f"Tổng chi phí lắp đặt: {total_cost}")
        print("Đây là bộ khung tối thiểu, các tuyến giao hàng chi tiết dùng Dijkstra trên mạng này.")
demo_kruskal_mst()


