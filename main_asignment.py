from routing import (demo_routing_shortest_path, demo_kruskal_mst)
from hashing_tool import (
    demo_order_hash_table,
    demo_group_coupon_anagrams,
    demo_longest_consecutive_days,
    demo_count_revenue_windows,
    demo_rolling_coupon_search
)

from promo_optimizer import (
    demo_dp_basics,
    demo_combo_knapsack_2d,
    demo_combo_knapsack_1d
)


def menu():
    while True:

        print("\n" + "=" * 50)
        print("        POLY SHIP - ALGORITHM DEMO")
        print("=" * 50)

        print("1. Demo Routing - Shortest Path")
        print("2. Demo MST - Minimum Spanning Tree")
        print("3. Demo Hash Table đơn hàng")
        print("4. Demo Hashing")
        print("5. Demo Rolling Hash")
        print("6. Demo Dynamic Programming cơ bản")
        print("7. Demo Combo Khuyến mãi (Knapsack)")
        print("8. Thoát")

        choice = input("\nChọn chức năng: ")

        # -----------------------
        if choice == "1":
            print("\n===== ROUTING =====")
            demo_routing_shortest_path()

        # -----------------------
        elif choice == "2":
            print("\n===== MST =====")
            demo_kruskal_mst()

        # -----------------------
        elif choice == "3":
            print("\n===== ORDER HASH TABLE =====")
            demo_order_hash_table()

        # -----------------------
        elif choice == "4":

            print("\n===== GROUP ANAGRAMS =====")
            demo_group_coupon_anagrams()

            print("\n===== LONGEST CONSECUTIVE DAYS =====")
            demo_longest_consecutive_days()

            print("\n===== SUBARRAY SUM = K =====")
            demo_count_revenue_windows()

        # -----------------------
        elif choice == "5":

            print("\n===== ROLLING HASH =====")
            demo_rolling_coupon_search()

        # -----------------------
        elif choice == "6":

            print("\n===== DP BASICS =====")
            demo_dp_basics()

        # -----------------------
        elif choice == "7":

            print("\n===== KNAPSACK 2D =====")
            demo_combo_knapsack_2d()

            print("\n===== KNAPSACK 1D =====")
            demo_combo_knapsack_1d()

        # -----------------------
        elif choice == "8":

            print("\nCảm ơn bạn đã sử dụng chương trình!")
            break

        # -----------------------
        else:
            print("\nLựa chọn không hợp lệ. Vui lòng chọn lại.")
menu()