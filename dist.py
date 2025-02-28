import math
import copy

input_map = [
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
]

# input_map_copy = copy.deepcopy(input_map)

locations = {
    "1": (3, 10),
    "1x": (2, 5),
    "2": (4, 2),
    "2x": (1, 9),
    "3": (2, 3),
    "3x": (1, 1),
    "4": (3, 5),
    "4x": (2, 6),
    "5": (2, 10),
    "5x": (5, 10),
    "6": (1, 11),
    "6x": (5, 6),
    "7": (2, 1),
    "7x": (3, 8),
    "8": (1, 2),
    "8x": (3, 3),
}

start_points = [
    (3, 10),
    (4, 2),
    (2, 3),
    (3, 5),
    (2, 10),
    (1, 11),
    (2, 1),
    (1, 2),
]

end_points = [
    (2, 5),
    (1, 9),
    (1, 1),
    (2, 6),
    (5, 10),
    (5, 6),
    (3, 8),
    (3, 3),
]

for k, v in locations.items():
    input_map[v[0]][v[1]] = k

for i in input_map:
    print("\t".join(i))

output_map = copy.deepcopy(input_map)


def surrounding_cells(ip):
    op = []
    for k in range(3):
        for l in range(3):
            row = max(0, min(ip[0] + (k - 1), 5))
            # row = ip[0] + (k - 1)
            # if row > 5:
            #     row = 5
            # elif row < 0:
            #     row = 0
            tp = tuple((row, (ip[1] + (l - 1)) % 12))
            # if tp == ip:
            #     continue
            op.append(tp)
    return op


def dist_list(st_list, en, dir=""):
    op = [100, 100, 100, 100, 100, 100, 100, 100]
    fw_list = [1, 6, 2, 4, 7]
    bk_list = [1, 6, 0, 3, 5]
    for ind, st_t in enumerate(st_list):
        # print((st_t[0], st_t[1]))
        cell = output_map[st_t[0]][st_t[1]]
        if cell != "-" or st_t == current_cell:
            continue
        if dir == "fw" and ind in fw_list:
            op[ind] = (st_t[0] - en[0]) ** 2 + (st_t[1] - en[1]) ** 2
        elif dir == "bk" and ind in bk_list:
            bk_col = 12 - (st_t[1] - en[1])
            op[ind] = (st_t[0] - en[0]) ** 2 + bk_col**2
    return op


def fw_dist(st, en):
    return abs(en[1] - st[1])


def bk_dist(fw_dist):
    return 12 - fw_dist


for i, start in enumerate(start_points):
    end = end_points[i]
    if start[1] > end[1]:
        st = end
        en = start
    else:
        st = start
        en = end

    fw = fw_dist(st, en)
    bk = bk_dist(fw)
    initial_dist = math.sqrt(min(fw, bk) ** 2 + (st[0] - en[0]) ** 2)

    if fw < bk:
        dir = "fw"
    else:
        dir = "bk"

    print(f"SP:{st}, EP:{en}, ID: {initial_dist}, DIR: {dir}")
    st_glyph = input_map[st[0]][st[1]]
    current_cell = st

    while current_cell != en:
        surround = surrounding_cells(current_cell)
        dists = dist_list(surround, en, dir)
        min_dist = min(dists)
        min_ind = dists.index(min_dist)
        # min_dist = math.sqrt(min_dist)
        current_cell = surround[min_ind]
        print(current_cell)
        output_map[current_cell[0]][current_cell[1]] = f"{st_glyph}o"

    for i in output_map:
        print("\t".join(i))

# for i in output_map:
#     print("\t".join(i))
