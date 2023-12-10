import math

with open("day8/data/input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

sequence = data.pop(0)
len_seq = len(sequence)

nodes = {}
for line in data:
    if line == "":
        continue
    node, directions = line.replace(")", "").replace("(", "").split("=")
    node = node.strip()
    directions = directions.replace(" ", "").split(",")

    directions = dict(zip(["L", "R"], directions))
    nodes[node] = directions

starting_nodes = [node for node in nodes if node.endswith("A")]

# loops = {}
loop_lens = []
for node in starting_nodes:
    starting_node = node
    configs_visited = []
    i = 0
    visited_config = starting_node, i
    while True:
        order = sequence[i]
        if visited_config in configs_visited:
            # input_offset = configs_visited.index(visited_config)
            loop_len = len(configs_visited) - i
            # loops[starting_node] = {"loop_len": loop_len}
            loop_lens.append(loop_len)
            break

        configs_visited.append(visited_config)
        i = (i + 1) % len_seq
        node = nodes[node][order]
        visited_config = node, i

print(math.lcm(*loop_lens))
