import cohere
import numpy as np
import os
from dotenv import load_dotenv

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
        return np.array(self.co.embed(texts=self.positive_aura, input_type='classification').embeddings[0])

    def get_negative_aura_embeddings(self):
        return np.array(self.co.embed(texts=self.negative_aura, input_type='classification').embeddings[0])
    
    def embedding_comparison(self):
        pos_aura_embed = self.get_positive_aura_embeddings()
        neg_aura_embed = self.get_negative_aura_embeddings()
        input_embed = np.array(self.co.embed(texts=["Aura game too strong"], input_type='classification').embeddings[0])

        pos_cosine_similarity = np.dot(pos_aura_embed, input_embed) / (np.linalg.norm(pos_aura_embed) * np.linalg.norm(input_embed))
        neg_cosine_similarity = np.dot(neg_aura_embed, input_embed) / (np.linalg.norm(neg_aura_embed) * np.linalg.norm(input_embed))

        print(pos_cosine_similarity)
        print(neg_cosine_similarity)

if __name__ == '__main__':
    aura = Aura()
    aura.embedding_comparison()
