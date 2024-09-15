from flask import Flask, request, jsonify
from flask_cors import CORS
import cohere
import numpy as np
import os
from dotenv import load_dotenv
import re

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def index():
    return 'Server is running!'


class Aura:
    def __init__(self) -> None:
        self.positive_aura = []
        self.negative_aura = []
        self.co = cohere.Client(os.environ["COHERE"])
        self.load_phrases()

    def load_phrases(self):
        positive_path = os.path.join(os.path.dirname(__file__), "positive_aura.txt")
        negative_path = os.path.join(os.path.dirname(__file__), "negative_aura.txt")
        
        with open(positive_path) as f:
            self.positive_aura = [line.strip() for line in f]

        with open(negative_path) as f:
            self.negative_aura = [line.strip() for line in f]

    def get_positive_aura_embeddings(self):
        return np.array(self.co.embed(texts=self.positive_aura, input_type='classification').embeddings[0])

    def get_negative_aura_embeddings(self):
        return np.array(self.co.embed(texts=self.negative_aura, input_type='classification').embeddings[0])
    
    def embedding_comparison(self, input_text):
        pos_aura_embed = self.get_positive_aura_embeddings()
        neg_aura_embed = self.get_negative_aura_embeddings()
        input_embed = np.array(self.co.embed(texts=[input_text], input_type='classification').embeddings[0])

        pos_cosine_similarity = np.dot(pos_aura_embed, input_embed) / (np.linalg.norm(pos_aura_embed) * np.linalg.norm(input_embed))
        neg_cosine_similarity = np.dot(neg_aura_embed, input_embed) / (np.linalg.norm(neg_aura_embed) * np.linalg.norm(input_embed))

        return pos_cosine_similarity, neg_cosine_similarity
    
@app.route('/analyze_transcript', methods=['POST'])
def analyze_transcript():
    try:
        data = request.json
        transcript = data['transcript']
        print("Full Transcript: " + transcript)
        
        words = transcript.split()
        chunks = [words[i:i + 25] for i in range(0, len(words), 25)]
        sentences = [" ".join(chunk) for chunk in chunks]

        aura = Aura()
        score = 0

        for idx, sentence in enumerate(sentences):
            
            pos_sim, neg_sim = aura.embedding_comparison(sentence)

            print("Sentence #" + (str)(idx+1) + ":")
            print("Positive Cosine Similarity: " + str(pos_sim))
            print("Negative Cosine Similarity: " + str(neg_sim))

            if pos_sim > neg_sim:
                score += 1
            elif neg_sim >= pos_sim:
                score -= 1

        return jsonify({'score': score})

    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(port=5001)
