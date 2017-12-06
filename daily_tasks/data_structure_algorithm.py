#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2017/11/13

import os


# 生成所有文件的路径
def get_all_task_url():
    all_path = []
    repo_url = 'https://github.com/keon/algorithms'
    repo_url2 = 'https://github.com/keon/algorithms/blob/master'
    local_path = '/Users/yaochao/python/github/algorithms'
    dirs = [os.path.join(local_path, x) for x in os.listdir(local_path)]
    for dir in dirs:
        dirs = [os.path.join(dir, x) for x in os.listdir(dir)]
        for dir in dirs:
            if '.' not in dir:
                dirs = [os.path.join(dir, x) for x in os.listdir(dir)]
                [all_path.append(x) for x in dirs]
            if '__init__' not in dir:
                all_path.append(dir)
    all_path = [x.replace(local_path, repo_url2) for x in all_path]
    return all_path


# 这是上面那个函数生成的数组
all_path = ['https://github.com/keon/algorithms/blob/master/tree/path_sum.py',
            'https://github.com/keon/algorithms/blob/master/tree/max_path_sum.py',
            'https://github.com/keon/algorithms/blob/master/tree/same_tree.py',
            'https://github.com/keon/algorithms/blob/master/tree/tree.py',
            'https://github.com/keon/algorithms/blob/master/tree/invert_tree.py',
            'https://github.com/keon/algorithms/blob/master/tree/is_balanced.py',
            'https://github.com/keon/algorithms/blob/master/tree/Segment_Tree/segment_tree.py',
            'https://github.com/keon/algorithms/blob/master/tree/binary_tree_paths.py',
            'https://github.com/keon/algorithms/blob/master/tree/pretty_print.py',
            'https://github.com/keon/algorithms/blob/master/tree/is_symmetric.py',
            'https://github.com/keon/algorithms/blob/master/tree/is_subtree.py',
            'https://github.com/keon/algorithms/blob/master/tree/bintree2list.py',
            'https://github.com/keon/algorithms/blob/master/tree/max_height.py',
            'https://github.com/keon/algorithms/blob/master/tree/min_height.py',
            'https://github.com/keon/algorithms/blob/master/tree/trie/add_and_search.py',
            'https://github.com/keon/algorithms/blob/master/tree/trie/trie.py',
            'https://github.com/keon/algorithms/blob/master/tree/traversal/inorder.py',
            'https://github.com/keon/algorithms/blob/master/tree/traversal/level_order.py',
            'https://github.com/keon/algorithms/blob/master/tree/traversal/zigzag.py',
            'https://github.com/keon/algorithms/blob/master/tree/lowest_common_ancestor.py',
            'https://github.com/keon/algorithms/blob/master/tree/path_sum2.py',
            'https://github.com/keon/algorithms/blob/master/tree/longest_consecutive.py',
            'https://github.com/keon/algorithms/blob/master/tree/deepest_left.py',
            'https://github.com/keon/algorithms/blob/master/tree/bst/kth_smallest.py',
            'https://github.com/keon/algorithms/blob/master/tree/bst/serialize_deserialize.py',
            'https://github.com/keon/algorithms/blob/master/tree/bst/unique_bst.py',
            'https://github.com/keon/algorithms/blob/master/tree/bst/predecessor.py',
            'https://github.com/keon/algorithms/blob/master/tree/bst/delete_node.py',
            'https://github.com/keon/algorithms/blob/master/tree/bst/array2bst.py',
            'https://github.com/keon/algorithms/blob/master/tree/bst/successor.py',
            'https://github.com/keon/algorithms/blob/master/tree/bst/bst_closest_value.py',
            'https://github.com/keon/algorithms/blob/master/tree/bst/lowest_common_ancestor.py',
            'https://github.com/keon/algorithms/blob/master/tree/bst/BSTIterator.py',
            'https://github.com/keon/algorithms/blob/master/tree/bst/is_bst.py',
            'https://github.com/keon/algorithms/blob/master/bit/count_ones.py',
            'https://github.com/keon/algorithms/blob/master/bit/reverse_bits.py',
            'https://github.com/keon/algorithms/blob/master/bit/single_number2.py',
            'https://github.com/keon/algorithms/blob/master/bit/power_of_two.py',
            'https://github.com/keon/algorithms/blob/master/bit/single_number.py',
            'https://github.com/keon/algorithms/blob/master/bit/subsets.py',
            'https://github.com/keon/algorithms/blob/master/bit/add_without_operator.py',
            'https://github.com/keon/algorithms/blob/master/bit/bytes_int_conversion.py',
            'https://github.com/keon/algorithms/blob/master/bit/find_missing_number.py',
            'https://github.com/keon/algorithms/blob/master/calculator/math_parser.py',
            'https://github.com/keon/algorithms/blob/master/dfs/count_islands.py',
            'https://github.com/keon/algorithms/blob/master/dfs/pacific_atlantic.py',
            'https://github.com/keon/algorithms/blob/master/dfs/all_factors.py',
            'https://github.com/keon/algorithms/blob/master/dfs/walls_and_gates.py',
            'https://github.com/keon/algorithms/blob/master/dfs/sudoku_solver.py',
            'https://github.com/keon/algorithms/blob/master/sort/quick_sort.py',
            'https://github.com/keon/algorithms/blob/master/sort/merge_sort.py',
            'https://github.com/keon/algorithms/blob/master/sort/insertion_sort.py',
            'https://github.com/keon/algorithms/blob/master/sort/bubble_sort.py',
            'https://github.com/keon/algorithms/blob/master/sort/selection_sort.py',
            'https://github.com/keon/algorithms/blob/master/sort/counting_sort.py',
            'https://github.com/keon/algorithms/blob/master/sort/wiggle_sort.py',
            'https://github.com/keon/algorithms/blob/master/sort/topsort.py',
            'https://github.com/keon/algorithms/blob/master/sort/sort_colors.py',
            'https://github.com/keon/algorithms/blob/master/sort/heap_sort.py',
            'https://github.com/keon/algorithms/blob/master/sort/comb_sort.py',
            'https://github.com/keon/algorithms/blob/master/sort/meeting_rooms.py',
            'https://github.com/keon/algorithms/blob/master/array/longest_non_repeat.py',
            'https://github.com/keon/algorithms/blob/master/array/flatten.py',
            'https://github.com/keon/algorithms/blob/master/array/plus_one.py',
            'https://github.com/keon/algorithms/blob/master/array/circular_counter.py',
            'https://github.com/keon/algorithms/blob/master/array/missing_ranges.py',
            'https://github.com/keon/algorithms/blob/master/array/summary_ranges.py',
            'https://github.com/keon/algorithms/blob/master/array/three_sum.py',
            'https://github.com/keon/algorithms/blob/master/array/rotate_array.py',
            'https://github.com/keon/algorithms/blob/master/array/two_sum.py',
            'https://github.com/keon/algorithms/blob/master/array/merge_intervals.py',
            'https://github.com/keon/algorithms/blob/master/array/garage.py',
            'https://github.com/keon/algorithms/blob/master/backtrack/permute.py',
            'https://github.com/keon/algorithms/blob/master/backtrack/subsets_unique.py',
            'https://github.com/keon/algorithms/blob/master/backtrack/array_sum_combinations.py',
            'https://github.com/keon/algorithms/blob/master/backtrack/anagram.py',
            'https://github.com/keon/algorithms/blob/master/backtrack/permute_unique.py',
            'https://github.com/keon/algorithms/blob/master/backtrack/general_solution.md',
            'https://github.com/keon/algorithms/blob/master/backtrack/letter_combination.py',
            'https://github.com/keon/algorithms/blob/master/backtrack/factor_combinations.py',
            'https://github.com/keon/algorithms/blob/master/backtrack/expression_add_operators.py',
            'https://github.com/keon/algorithms/blob/master/backtrack/subsets.py',
            'https://github.com/keon/algorithms/blob/master/backtrack/generate_parenthesis.py',
            'https://github.com/keon/algorithms/blob/master/backtrack/generate_abbreviations.py',
            'https://github.com/keon/algorithms/blob/master/backtrack/word_search.py',
            'https://github.com/keon/algorithms/blob/master/backtrack/pattern_match.py',
            'https://github.com/keon/algorithms/blob/master/backtrack/palindrome_partitioning.py',
            'https://github.com/keon/algorithms/blob/master/backtrack/combination_sum.py',
            'https://github.com/keon/algorithms/blob/master/linkedlist/rotate_list.py',
            'https://github.com/keon/algorithms/blob/master/linkedlist/reverse.py',
            'https://github.com/keon/algorithms/blob/master/linkedlist/delete_node.py',
            'https://github.com/keon/algorithms/blob/master/linkedlist/is_palindrome.py',
            'https://github.com/keon/algorithms/blob/master/linkedlist/linkedlist.py',
            'https://github.com/keon/algorithms/blob/master/linkedlist/add_two_numbers.py',
            'https://github.com/keon/algorithms/blob/master/linkedlist/is_cyclic.py',
            'https://github.com/keon/algorithms/blob/master/linkedlist/copy_random_pointer.py',
            'https://github.com/keon/algorithms/blob/master/linkedlist/kth_to_last.py',
            'https://github.com/keon/algorithms/blob/master/linkedlist/first_cyclic_node.py',
            'https://github.com/keon/algorithms/blob/master/linkedlist/remove_duplicates.py',
            'https://github.com/keon/algorithms/blob/master/linkedlist/swap_in_pairs.py',
            'https://github.com/keon/algorithms/blob/master/graph/markov_chain.py',
            'https://github.com/keon/algorithms/blob/master/graph/traversal.py',
            'https://github.com/keon/algorithms/blob/master/graph/find_path.py',
            'https://github.com/keon/algorithms/blob/master/graph/clone_graph.py',
            'https://github.com/keon/algorithms/blob/master/graph/graph.py',
            'https://github.com/keon/algorithms/blob/master/graph/minimum_spanning_tree.py',
            'https://github.com/keon/algorithms/blob/master/graph/find_all_cliques.py',
            'https://github.com/keon/algorithms/blob/master/graph/cycle_detection.py',
            'https://github.com/keon/algorithms/blob/master/graph/satisfiability.py',
            'https://github.com/keon/algorithms/blob/master/math/primes_sieve_of_eratosthenes.py',
            'https://github.com/keon/algorithms/blob/master/math/is_strobogrammatic.py',
            'https://github.com/keon/algorithms/blob/master/math/gcd.py',
            'https://github.com/keon/algorithms/blob/master/math/rsa.py',
            'https://github.com/keon/algorithms/blob/master/math/rabin_miller.py',
            'https://github.com/keon/algorithms/blob/master/math/prime_test.py',
            'https://github.com/keon/algorithms/blob/master/math/generate_strobogrammtic.py',
            'https://github.com/keon/algorithms/blob/master/math/extended_gcd.py',
            'https://github.com/keon/algorithms/blob/master/math/pythagoras.py',
            'https://github.com/keon/algorithms/blob/master/math/nth_digit.py',
            'https://github.com/keon/algorithms/blob/master/math/sqrt_precision_factor.py',
            'https://github.com/keon/algorithms/blob/master/search/first_occurance.py',
            'https://github.com/keon/algorithms/blob/master/search/binary_search.py',
            'https://github.com/keon/algorithms/blob/master/search/last_occurance.py',
            'https://github.com/keon/algorithms/blob/master/map/longest_common_subsequence.py',
            'https://github.com/keon/algorithms/blob/master/map/randomized_set.py',
            'https://github.com/keon/algorithms/blob/master/map/hashtable.py',
            'https://github.com/keon/algorithms/blob/master/map/valid_sudoku.py',
            'https://github.com/keon/algorithms/blob/master/heap/sliding_window_max.py',
            'https://github.com/keon/algorithms/blob/master/heap/merge_sorted_k_lists.py',
            'https://github.com/keon/algorithms/blob/master/heap/skyline.py',
            'https://github.com/keon/algorithms/blob/master/bfs/shortest_distance_from_all_buildings.py',
            'https://github.com/keon/algorithms/blob/master/bfs/word_ladder.py',
            'https://github.com/keon/algorithms/blob/master/union-find/count_islands.py',
            'https://github.com/keon/algorithms/blob/master/queue/queue.py',
            'https://github.com/keon/algorithms/blob/master/queue/reconstruct_queue.py',
            'https://github.com/keon/algorithms/blob/master/queue/max_sliding_window.py',
            'https://github.com/keon/algorithms/blob/master/queue/moving_average.py',
            'https://github.com/keon/algorithms/blob/master/queue/zigzagiterator.py',
            'https://github.com/keon/algorithms/blob/master/dp/rod_cut.py',
            'https://github.com/keon/algorithms/blob/master/dp/house_robber.py',
            'https://github.com/keon/algorithms/blob/master/dp/job_scheduling.py',
            'https://github.com/keon/algorithms/blob/master/dp/buy_sell_stock.py',
            'https://github.com/keon/algorithms/blob/master/dp/regex_matching.py',
            'https://github.com/keon/algorithms/blob/master/dp/knapsack.py',
            'https://github.com/keon/algorithms/blob/master/dp/max_subarray.py',
            'https://github.com/keon/algorithms/blob/master/dp/longest_increasing.py',
            'https://github.com/keon/algorithms/blob/master/dp/num_decodings.py',
            'https://github.com/keon/algorithms/blob/master/dp/max_product_subarray.py',
            'https://github.com/keon/algorithms/blob/master/dp/climbing_stairs.py',
            'https://github.com/keon/algorithms/blob/master/dp/word_break.py',
            'https://github.com/keon/algorithms/blob/master/dp/combination_sum.py',
            'https://github.com/keon/algorithms/blob/master/string/breaking_bad.py',
            'https://github.com/keon/algorithms/blob/master/string/license_number.py',
            'https://github.com/keon/algorithms/blob/master/string/reverse_string.py',
            'https://github.com/keon/algorithms/blob/master/string/reverse_words.py',
            'https://github.com/keon/algorithms/blob/master/string/roman_to_int.py',
            'https://github.com/keon/algorithms/blob/master/string/is_palindrome.py',
            'https://github.com/keon/algorithms/blob/master/string/encode_decode.py',
            'https://github.com/keon/algorithms/blob/master/string/rabin_karp.py',
            'https://github.com/keon/algorithms/blob/master/string/int_to_roman.py',
            'https://github.com/keon/algorithms/blob/master/string/word_squares.py',
            'https://github.com/keon/algorithms/blob/master/string/make_sentence.py',
            'https://github.com/keon/algorithms/blob/master/string/multiply_strings.py',
            'https://github.com/keon/algorithms/blob/master/string/one_edit_distance.py',
            'https://github.com/keon/algorithms/blob/master/string/group_anagrams.py',
            'https://github.com/keon/algorithms/blob/master/string/decode_string.py',
            'https://github.com/keon/algorithms/blob/master/string/add_binary.py',
            'https://github.com/keon/algorithms/blob/master/string/reverse_vowel.py',
            'https://github.com/keon/algorithms/blob/master/stack/valid_parenthesis.py',
            'https://github.com/keon/algorithms/blob/master/stack/stack.py',
            'https://github.com/keon/algorithms/blob/master/stack/simplify_path.py',
            'https://github.com/keon/algorithms/blob/master/stack/longest_abs_path.py',
            'https://github.com/keon/algorithms/blob/master/set/set_covering.py',
            'https://github.com/keon/algorithms/blob/master/set/randomized_set.py',
            'https://github.com/keon/algorithms/blob/master/tmp/temporary.md',
            'https://github.com/keon/algorithms/blob/master/matrix/search_in_sorted_matrix.py',
            'https://github.com/keon/algorithms/blob/master/matrix/matrix_rotation.txt',
            'https://github.com/keon/algorithms/blob/master/matrix/count_paths.py',
            'https://github.com/keon/algorithms/blob/master/matrix/sparse_mul.py',
            'https://github.com/keon/algorithms/blob/master/matrix/rotate_image.py',
            'https://github.com/keon/algorithms/blob/master/matrix/spiral_traversal.py',
            'https://github.com/keon/algorithms/blob/master/matrix/bomb_enemy.py',
            'https://github.com/keon/algorithms/blob/master/matrix/sparse_dot_vector.py',
            'https://github.com/keon/algorithms/blob/master/matrix/copy_transform.py']


def go():
    # 读取天数记录值
    a = ''
    with open('order.txt', 'r') as f:
        a = f.readlines()
        a = int(a[0])
    # 发送今日邮件：
    url = all_path[a+1]
    subject = '数据结构与算法 - 第{}天'.format(a)
    message = '<h1 color="red">每天进步一点点</h1><p>今天是第<font color="red">{}</font>天\n今天的数据结构与算法的联系题目: <a href="{}">{}</a></p><br>'.format(a, url, url)
    from daily_tasks.daily_mail import sendmail
    sendmail(subject=subject, message=message)
    # 天数记录值加一
    with open('order.txt', 'w') as f:
        f.write(str(a + 1))


if __name__ == '__main__':
    go()
