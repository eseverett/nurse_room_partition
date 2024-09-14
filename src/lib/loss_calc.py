import numpy as np
from sklearn.cluster import KMeans

class ClusterData:
    def __init__(self, acuity_list, coords_list, discharge_list, acuity_scaling_factor=1.0, discharge_scaling_factor=1.0, num_clusters=2):
        """
        Initializes the RoomClusterer with room data and scaling factors.
        
        Args:
            acuity_list (list): A list of acuity values.
            coords_list (list): A list of coordinates (tuples) for each room.
            discharge_list (list): A list of discharge status (True/False) for each room.
            acuity_scaling_factor (float): Factor to scale the importance of acuity in clustering.
            discharge_scaling_factor (float): Factor to scale the importance of discharge status.
            num_clusters (int): Number of clusters (nurses) for which the rooms will be grouped.
        """
        self.acuity_list = acuity_list
        self.coords_list = coords_list
        self.discharge_list = discharge_list
        self.acuity_scaling_factor = acuity_scaling_factor
        self.discharge_scaling_factor = discharge_scaling_factor
        self.num_clusters = num_clusters
        self.clusters = {}

    def cluster_rooms(self):
        """
        Clusters the rooms based on their coordinates, acuity, and discharge status.
        """
        room_features = np.array([
            [self.coords_list[i][0], self.coords_list[i][1], self.acuity_list[i], int(self.discharge_list[i])]
            for i in range(len(self.acuity_list))
        ])

        room_features[:, 2] *= self.acuity_scaling_factor
        room_features[:, 3] *= self.discharge_scaling_factor

        kmeans = KMeans(n_clusters=self.num_clusters, random_state=0).fit(room_features)

        for idx, label in enumerate(kmeans.labels_):
            if label not in self.clusters:
                self.clusters[label] = []
            self.clusters[label].append({
                'Acuity': self.acuity_list[idx],
                'coords': self.coords_list[idx],
                'Discharge': self.discharge_list[idx]
            })

        return self.clusters

    def calculate_cluster_loss(self, acuity_weight=2, discharge_penalty=10):
        """
        Calculates the total loss for each cluster.
        
        Args:
            acuity_weight (float): Weight for acuity in the loss calculation.
            discharge_penalty (float): Penalty for discharge status in the loss calculation.
        
        Returns:
            dict: A dictionary with cluster IDs as keys and their corresponding total loss as values.
        """
        cluster_losses = {}
        
        for cluster_id, cluster_rooms in self.clusters.items():
            total_loss = 0
            
            for i in range(len(cluster_rooms)):
                for j in range(i + 1, len(cluster_rooms)):
                    room1 = cluster_rooms[i]
                    room2 = cluster_rooms[j]
                    distance_loss = np.linalg.norm(np.array(room1['coords']) - np.array(room2['coords']))
                    total_loss += distance_loss
            
            for room in cluster_rooms:
                acuity_loss = room['Acuity'] * acuity_weight
                discharge_loss = discharge_penalty if room['Discharge'] else 0
                total_loss += acuity_loss + discharge_loss
            
            cluster_losses[cluster_id] = total_loss

        return cluster_losses
