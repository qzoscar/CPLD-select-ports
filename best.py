
################################################################################################
# @author: Oscar Ding
# @date: 2016/9/26
# Select as many as possible widest gaps to divide the used_pins_list into several groups
################################################################################################


MAX_GROUP_NUM = 12
# Return a list that contains tuples(gap_index, gap_width) sorted by gap_width
def sort_gap(used_pins):
    gap_num = len(used_pins) - 1
    gap_width = {}
    for i in xrange(gap_num):
        gap_width[i] = used_pins[i+1]-used_pins[i]
    return sorted(gap_width.items(), key=lambda e:e[1], reverse=True)

# Return an index list of gaps that used for dividing
def gap_to_choose(sorted_gap_list):
    if(len(sorted_gap_list)>=11):
        under_select_gap = sorted_gap_list[:11]
    else:
        under_select_gap = sorted_gap_list
    choosed_gap_index = []
    # only remain gaps larger than 1 (less than 1 is useless)
    for gap in under_select_gap:
        if gap[1] > 1:
            choosed_gap_index.append(gap[0])
    return sorted(choosed_gap_index)

# MAIN METHOD: return the best division
def group_pins(used_pins_list):

    sorted_gap_list = sort_gap(used_pins_list)
    choosed_gap_index_list = gap_to_choose(sorted_gap_list)

    # group the final result
    division = []
    left = used_pins_list[0]
    for i in xrange(len(choosed_gap_index_list)):
        right = used_pins_list[choosed_gap_index_list[i]]
        division.append((left, right))
        left = used_pins_list[choosed_gap_index_list[i] + 1]
    division.append((left, max(used_pins_list)))
    return division

def count_used(division):
    count = 0
    for group in division:
        left = group[0]
        right = group[1]
        count = count + right - left + 1
    return count

# Test result:
used_pins_list = [2, 3, 8, 15, 16, 17, 18, 19, 20, 21, 40, 42, 49, 50, 57, 61, 67, 70, 73, 74, 75, 81, 83, 85, 87, 91]
# used_pins_list = [2, 3, 8, 15, 16, 17, 18, 19]
division = group_pins(used_pins_list)
print division, "is the best division."
print "Total used pins: ",count_used(division)



