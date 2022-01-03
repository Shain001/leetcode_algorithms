import json


def graph_parser(file_path, output_graph, traffic_name):
    f = open(output_graph, 'w')
    f2 = open(traffic_name, 'w')
    # Opening JSON file
    with open(file_path) as json_file:
        data = json.load(json_file)
        for i in range(0, 632899):
            node_id = i + 1
            edge_info = data[i]['e']
            for edge in edge_info:
                neighbor_id = edge['i'] + 1
                weight = edge['w']
                speed = edge['s']
                f.write(str(node_id) + ' ' + str(neighbor_id) + ' ' + str(weight) + ' ' + str(speed) + '\n')
            traffic = 1 if data[i]['tr'] is True else 0
            f2.write(str(traffic) + '\n')


    f.close()
    f2.close()


graph_parser('test1121.json', 'graph1124.txt', 'signal1124.txt')