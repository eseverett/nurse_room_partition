from lib import load_data, loss_calc
import json

def main() -> None:
    dataloader = load_data.DataLoader("../data/fake_test_data.csv", "../conf/default_room_dict.json")
    
    dataloader.load_CSV()
    dataloader.load_JSON()

    dataloader.make_acuity_list()
    dataloader.make_room_list()
    dataloader.make_discharge_list()
    
    acuity_list = dataloader.get_acuity_list()
    room_list = dataloader.get_room_list()
    discharge_list = dataloader.get_discharge_list()
    
    rooms = {
    "29": [0, 0],
    "30": [2, 0],
    "31": [4, 0],
    "32": [6, 0],
    "33": [8, 0],
    "34": [10, 0],
    "35": [12, 0],
    "36": [14, 0],
    "37": [16, 0],
    "38": [18, 0],
    "39": [16, 6],
    "40": [16, 8],
    "41": [16, 10],
    "42": [16, 12],
    "43": [16, 14],
    "44": [14, 12],
    "45": [12, 12],
    "46": [10, 12],
    "47": [8, 12],
    "48": [6, 12],
    "49": [4, 12],
    "50": [2, 12],
    "51": [0, 12]
    }

    rooms_numbs = rooms.keys()
    coords_list = [rooms[room] for room in rooms_numbs if room in rooms]
    
    room_clusterer = loss_calc.ClusterData(
    acuity_list=acuity_list,
    coords_list=coords_list,
    discharge_list=discharge_list,
    acuity_scaling_factor=500,
    discharge_scaling_factor=2,
    num_clusters=4
    )

    clusters = room_clusterer.cluster_rooms()

    for cluster_id, cluster_rooms in clusters.items():
        print(f"Cluster {cluster_id + 1}:")
        for room in cluster_rooms:
            print(f"  Room with acuity {room['Acuity']} at {room['coords']}, Discharge: {room['Discharge']}")

    cluster_losses = room_clusterer.calculate_cluster_loss(acuity_weight=2, discharge_penalty=10)
    for cluster_id, loss in cluster_losses.items():
        print(f"Cluster {cluster_id + 1} Loss: {loss}")


if __name__ == "__main__":
    main()