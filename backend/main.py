import cohere
import numpy as np
import os
from dotenv import load_dotenv
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min

load_dotenv()

class Aura:
    def __init__(self) -> None:
        self.positive_aura = []
        self.negative_aura = []
        self.co = cohere.Client(os.environ["COHERE"])
        self.load_phrases()

    def load_phrases(self):
        for line in open("positive_aura.txt"):
            self.positive_aura.append(line.strip())

        for line in open("negative_aura.txt"):
            self.negative_aura.append(line.strip())

    def get_positive_aura_embeddings(self):
        embed = np.array(self.co.embed(texts=self.positive_aura, input_type='classification').embeddings)
        return KMeans(n_clusters=10, n_init='auto').fit(embed)

    def get_negative_aura_embeddings(self):
        embed = np.array(self.co.embed(texts=self.negative_aura, input_type='classification').embeddings)
        return KMeans(n_clusters=10, n_init='auto').fit(embed)
    
    def embedding_comparison(self):
        input_embed = np.array(self.co.embed(texts=["Aura game too strong"], input_type='classification').embeddings)
        pos_aura_embed = self.get_positive_aura_embeddings()
        pos_aura_centroid = pos_aura_embed.cluster_centers_
        pos_aura_closest, pos_aura_distance = pairwise_distances_argmin_min(input_embed, pos_aura_centroid)

        neg_aura_embed = self.get_negative_aura_embeddings()
        neg_aura_centroid = neg_aura_embed.cluster_centers_
        neg_aura_closest, neg_aura_distance = pairwise_distances_argmin_min(input_embed, neg_aura_centroid)

        print(pos_aura_distance)
        print(neg_aura_distance)

        # Calculating the aura points assigned to each person
        if pos_aura_distance > neg_aura_distance:
            return self.aura_point_assignment(pos_aura_distance, neg_aura_distance)
        elif neg_aura_distance < pos_aura_distance:
            return self.aura_point_assignment(neg_aura_distance, pos_aura_distance)
        else:
            return 0

    def aura_point_assignment(self, greater_distance, smaller_distance):
        pass

if __name__ == '__main__':
    aura = Aura()
    aura.embedding_comparison()
