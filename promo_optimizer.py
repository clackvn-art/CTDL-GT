def fib_memo(n):
    memo = {}

    def dp(x):
        if x in memo:
            return memo[x]

        if x <= 1:
            return x

        memo[x] = dp(x - 1) + dp(x - 2)
        return memo[x]

    return dp(n)

def climb_stairs(n):
    # Trả về số cách leo n bậc.

    if n <= 2:
        return n

    dp = [0] * (n + 1)

    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

def demo_dp_basics():

    print("===== DYNAMIC PROGRAMMING BASICS =====")

    n = 10

    print(f"\nFib({n}) = {fib_memo(n)}")

    print()

    for i in range(1, 8):
        print(f"Climb Stairs({i}) = {climb_stairs(i)}")
demo_dp_basics()

def promo_knapsack(price, bonus_score, B):
    # price        : trọng lượng
    # bonus_score  : giá trị
    # B            : ngân sách

    n = len(price)

    dp = [[0]*(B+1) for _ in range(n+1)]

    for i in range(1, n+1):

        for w in range(B+1):

            # Không chọn sản phẩm
            dp[i][w] = dp[i-1][w]

            # Nếu đủ ngân sách
            if price[i-1] <= w:

                dp[i][w] = max(
                    dp[i][w],
                    bonus_score[i-1] +
                    dp[i-1][w-price[i-1]]
                )
    # Truy vết
    selected = []

    w = B

    for i in range(n,0,-1):

        if dp[i][w] != dp[i-1][w]:

            selected.append(i-1)

            w -= price[i-1]

    selected.reverse()

    return dp[n][B], selected

def demo_knapsack():

    products = [
        "Laptop",
        "Phone",
        "Mouse",
        "Keyboard"
    ]

    price = [4,3,2,5]

    bonus = [10,4,7,9]

    B = 8

    result = promo_knapsack(price, bonus, B)

    print("===== PROMO KNAPSACK =====")

    print("Products:", products)

    print("Price :", price)

    print("Bonus :", bonus)

    print("Budget:", B)

    print()

    print("Maximum Bonus =", result)
demo_knapsack()

def build_combo_dp_table(prices, scores, B):
    n = len(prices)

    # Khởi tạo bảng DP (n+1) x (B+1)
    dp = [[0] * (B + 1) for _ in range(n + 1)]

    # Xây bảng DP
    for i in range(1, n + 1):

        for b in range(B + 1):

            # Không chọn sản phẩm thứ i
            dp[i][b] = dp[i - 1][b]

            # Nếu đủ ngân sách thì xét chọn
            if prices[i - 1] <= b:

                dp[i][b] = max(
                    dp[i][b],
                    dp[i - 1][b - prices[i - 1]] + scores[i - 1]
                )

    return dp

def trace_combo_from_dp(dp, prices, scores, B):
    # Truy vết các sản phẩm được chọn từ bảng DP.

    selected_items = []
    i = len(prices)
    b = B


    while i > 0 and b > 0:

        # Nếu giá trị khác dòng trên -> sản phẩm được chọn
        if dp[i][b] != dp[i-1][b]:
            # không chọn item 
            i -= 1
        else:
            # chọn item
            selected_items.append(i-1)

            # Giảm ngân sách còn lại
            b -= prices[i-1]
            i -= 1

    selected_items.reverse()

    return selected_items

def demo_combo_knapsack_2d():


    print("===== COMBO KNAPSACK 0/1 =====")

    # Danh sách sản phẩm
    products = [
        "Laptop",
        "Phone",
        "Mouse",
        "Keyboard",
        "Headphone"
    ]

    # Giá sản phẩm
    prices = [4, 3, 2, 5, 1]

    # Điểm khuyến mãi
    scores = [10, 4, 7, 9, 2]

    # Ngân sách
    B = 8

    # Xây bảng DP
    dp = build_combo_dp_table(prices, scores, B)

    print("\nBảng DP:")

    for row in dp:
        print(row)

    # Truy vết sản phẩm
    selected = trace_combo_from_dp(dp, prices, scores, B)

    print("\n========== KẾT QUẢ ==========")

    print("Ngân sách:", B)
    print("Điểm tối đa:", dp[len(prices)][B])

    total_price = 0
    total_score = 0

    print("\nCác sản phẩm được chọn:")

    for i in selected:
        print(
            f"- {products[i]} "
            f"(Price={prices[i]}, Score={scores[i]})"
        )

        total_price += prices[i]
        total_score += scores[i]

    print("\nTổng giá:", total_price)
    print("Tổng điểm:", total_score)
demo_combo_knapsack_2d()

def combo_knapsack_1d(prices, scores, B):
    n = len(prices)

    # dp[b] = điểm tối đa với ngân sách b
    dp = [0] * (B + 1)

    for i in range(n):

        # Duyệt NGƯỢC
        for b in range(B, prices[i] - 1, -1):

            dp[b] = max(
                dp[b],
                dp[b - prices[i]] + scores[i]
            )

    return dp[B]

def demo_combo_knapsack_1d():

    print("===== DEMO KNAPSACK 1D =====")

    products = [
        "Laptop",
        "Phone",
        "Mouse",
        "Keyboard",
        "Headphone"
    ]

    prices = [4, 3, 2, 5, 1]
    scores = [10, 4, 7, 9, 2]

    B = 8

    # Phiên bản 2D
    dp2 = build_combo_dp_table(prices, scores, B)
    max_score_2d = dp2[len(prices)][B]

    # Phiên bản 1D
    max_score_1d = combo_knapsack_1d(prices, scores, B)

    print("Budget:", B)

    print("\nMax Score (2D):", max_score_2d)
    print("Max Score (1D):", max_score_1d)

    if max_score_1d == max_score_2d:
        print("\n✓ Hai phiên bản cho cùng kết quả.")
    else:
        print("\n✗ Có sự khác biệt.")
demo_combo_knapsack_1d()

