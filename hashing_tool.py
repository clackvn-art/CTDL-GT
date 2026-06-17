class OrderHashTable:
    def __init__(self, size=10):
        # Khởi tạo hash table với số bucket = size.
        self.size = size
        self.table = [[] for _ in range(size)]   # Separate Chaining

    def _hash(self, order_id):
        # Hàm băm.
        return hash(order_id) % self.size

    def insert(self, order_id, order_data):
        # Thêm hoặc cập nhật đơn hàng.

        index = self._hash(order_id)
        bucket = self.table[index]

        # Nếu đã tồn tại thì cập nhật
        for i, (key, value) in enumerate(bucket):
            if key == order_id:
                bucket[i] = (order_id, order_data)
                return

        # Chưa có thì thêm mới
        bucket.append((order_id, order_data))

    def get(self, order_id):
        # Lấy thông tin đơn hàng.

        index = self._hash(order_id)
        bucket = self.table[index]

        for key, value in bucket:
            if key == order_id:
                return value

        return None

    def remove(self, order_id):
        # Xóa đơn hàng.

        index = self._hash(order_id)
        bucket = self.table[index]

        for i, (key, value) in enumerate(bucket):
            if key == order_id:
                del bucket[i]
                return True

        return False

    def display(self):
        # Hiển thị toàn bộ Hash Table.
      
        print("===== HASH TABLE =====")
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")

def demo_order_hash_table():
    print("===== DEMO ORDER HASH TABLE =====")

    # Khởi tạo Hash Table
    orders = OrderHashTable(size=10)

    # Thêm các đơn hàng mẫu
    orders.insert("OD001", {
        "customer": "Nguyen Van A",
        "product": "Laptop",
        "total": 1500
    })

    orders.insert("OD002", {
        "customer": "Tran Thi B",
        "product": "Phone",
        "total": 800
    })

    orders.insert("OD003", {
        "customer": "Le Van C",
        "product": "Headphone",
        "total": 200
    })

    print("\n1. Sau khi insert:")
    orders.display()

    # Test get
    print("\n2. Get đơn hàng OD002:")
    order = orders.get("OD002")

    if order:
        print(order)
    else:
        print("Không tìm thấy đơn hàng.")

    # Test remove
    print("\n3. Remove đơn hàng OD002:")
    if orders.remove("OD002"):
        print("Xóa thành công.")
    else:
        print("Không tìm thấy đơn hàng.")

    print("\n4. Hash Table sau khi remove:")
    orders.display()
demo_order_hash_table()

def group_coupon_anagrams(codes):
    # Nhóm các mã coupon là anagram của nhau.
    groups = {}

    for code in codes:
        # Tạo key bằng cách sắp xếp ký tự
        key = "".join(sorted(code))

        if key not in groups:
            groups[key] = []

        groups[key].append(code)

    return list(groups.values())

def demo_group_coupon_anagrams():

    codes = [
        "SAVE10",
        "AVES10",
        "VEAS10",
        "WELCOME",
        "COMEWEL",
        "HELLO",
        "OLLEH",
        "DISCOUNT"
    ]

    groups = group_coupon_anagrams(codes)

    print("===== GROUP COUPON ANAGRAMS =====\n")

    for i, group in enumerate(groups, start=1):
        print(f"Nhóm {i}:")
        print(group)
        print()
demo_group_coupon_anagrams()

def longest_consecutive_days(days):
    # Tìm chuỗi ngày liên tiếp dài nhất.
    if not days:
        return [], 0

    day_set = set(days) #parameter

    longest_sequence = []
    max_length = 0

    for day in day_set:

        # Chỉ bắt đầu nếu day là đầu chuỗi
        if day - 1 not in day_set:

            current = day
            sequence = []

            while current in day_set:
                sequence.append(current)
                current += 1

            if len(sequence) > max_length:
                max_length = len(sequence)
                longest_sequence = sequence

    return longest_sequence, max_length

def demo_longest_consecutive_days():

    days = [8, 2, 3, 7, 4, 20, 1, 5, 30, 31]

    sequence, length = longest_consecutive_days(days)

    print("===== LONGEST CONSECUTIVE DAYS =====")

    print("Days:")
    print(days)

    print("\nPhát hiện chuỗi ngày hệ thống có nhiều đơn hàng liên tiếp.:")
    print(sequence)

    print("Length:", length)
demo_longest_consecutive_days()

def count_revenue_windows(revenues, k):
    prefix_sum = 0
    count = 0

    # Hash Map lưu số lần xuất hiện của prefix_sum
    prefix_count = {0: 1}

    for revenue in revenues:

        prefix_sum += revenue

        # Nếu đã có prefix_sum - k
        if (prefix_sum - k) in prefix_count:
            count += prefix_count[prefix_sum - k]

        # Cập nhật prefix_sum
        prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

    return count

def demo_count_revenue_windows():

    print("===== SUBARRAY SUM = K =====")

    tests = [
        ([1, 1, 1], 2),
        ([1, 2, 3], 3),
        ([2, 3, 1, 2, 4], 6),
        ([3, 4, 7, 2, -3, 1, 4, 2], 7)
    ]

    for revenues, k in tests:

        print("\nRevenue:", revenues)
        print("Target :", k)

        result = count_revenue_windows(revenues, k)

        print("Số khoảng doanh thu =", result)
demo_count_revenue_windows()

def rolling_hash_search(text, pattern):
    # Tìm tất cả vị trí xuất hiện của pattern trong text bằng thuật toán Rabin-Karp (Rolling Hash).
    if not pattern or len(pattern) > len(text):
        return []

    base = 256          # số ký tự ASCII
    mod = 101           # số nguyên tố

    m = len(pattern)
    n = len(text)

    pattern_hash = 0
    window_hash = 0

    h = 1

    # h = base^(m-1) % mod
    for _ in range(m - 1):
        h = (h * base) % mod

    # Hash ban đầu
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % mod
        window_hash = (base * window_hash + ord(text[i])) % mod

    result = []

    # Trượt cửa sổ
    for i in range(n - m + 1):

        # Nếu hash giống nhau
        if pattern_hash == window_hash:

            # So sánh lại để tránh collision
            if text[i:i+m] == pattern:
                result.append(i)

        # Rolling Hash
        if i < n - m:

            window_hash = (
                base * (window_hash - ord(text[i]) * h)
                + ord(text[i + m])
            ) % mod

            if window_hash < 0:
                window_hash += mod

    return result

def demo_rolling_coupon_search():

    text = (
        "User A used SAVE10 today. "
        "User B used DISCOUNT20. "
        "User C tried SAVE10 again. "
        "WELCOME coupon was also applied."
    )

    patterns = [
        "SAVE10",
        "WELCOME",
        "DISCOUNT20",
        "FREE50"
    ]

    print("===== ROLLING HASH =====")
    print("\nLog:")
    print(text)

    for pattern in patterns:

        positions = rolling_hash_search(text, pattern)

        print(f"\nPattern: {pattern}")

        if positions:
            print("Found at positions:", positions)
        else:
            print("Not found.")
demo_rolling_coupon_search()

