from typing import List

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class QuestionST:
    BASE_MODEL = "bert-base-nli-mean-tokens"

    def __init__(self, base_model: str = BASE_MODEL):
        self.base_model = base_model
        self.model = SentenceTransformer(self.base_model)

    def encode(self, sentences: List[str]):
        sen_embs = self.model.encode(sentences)
        return sen_embs

    @staticmethod
    def similarity(embeddings: List):
        return cosine_similarity(
            [embeddings[0]],
            embeddings[1:]
        )

    @staticmethod
    def zip_data(data: List, scores: List, sort_key: str = 'similarity') -> List:
        r_data = []
        for (datum, score) in zip(data, scores):
            r_data.append({
                'similarity': score,
                'faq': datum
            })
        r_data = sorted(r_data, key=lambda d: d[sort_key], reverse=True)
        return r_data

    def rank(self, target: List, data: List, top_n: int = 5):
        q_list = [faq.question_str for faq in data]
        sen_emb = self.model.encode(target + q_list)
        sim_score = self.similarity(sen_emb)
        print(data, sim_score)
        return self.zip_data(data, sim_score[0])[:top_n]
