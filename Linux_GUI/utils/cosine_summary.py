import numpy as np
import networkx as nx
import nltk
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance


# Summarize using Cosine Similarity
import numpy as np
import networkx as nx
import nltk
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance


# Summarize using Cosine Similarity

class cosine_summary:
    
    def extract_vector(self, sentence, all_words, stop_words):
        
        extracted_vector = [0] * len(all_words)
        for word in sentence:
            if word in stop_words:
                continue
            extracted_vector[all_words.index(word)] += 1
        return extracted_vector
    
    def sentence_similarity(self, s1, s2, stop_words):

        s1 = [word.lower() for word in s1]
        s2 = [word.lower() for word in s2]

        all_words = list(set(s1 + s2))

        v1 = self.extract_vector(s1, all_words, stop_words)
        v2 = self.extract_vector(s2, all_words, stop_words)

        return 1 - cosine_distance(v1, v2)
    
    
    def summarise_text(self, scores, sentences):
        summary = []
        max_len = len(sentences)

        for i in range(max_len):
            if(scores[i]< 0.01):
                continue
            summary.append(" ".join(sentences[i]))

        summary = ". ".join(summary)

        return summary
    
    
    
    def summariser(self, text):
        #Breaking Down text to Sentences
        sentences = []
        
        #STOP Words
        stop_words = stopwords.words('english')
        split_text = text.split(". ")
        
        for sentence in split_text:
            sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
        
        sentences.pop()
        
        #Similarity Matrix Building
        similarity_matrix = np.zeros((len(sentences), len(sentences)))

        for i1, sentence1 in enumerate(sentences):
            for i2, sentence2 in enumerate(sentences):
                if sentence1 == sentence2:
                    similarity_matrix[i1][i2] = 0
                    continue
                similarity_matrix[i1][i2] = self.sentence_similarity(sentence1, sentence2, stop_words)
                
        #Ranking sentences
        similarity_network = nx.from_numpy_array(similarity_matrix)
        scores = nx.pagerank(similarity_network)
        
        # Sorting the Sentences with scores in descending order
        i = 0
        # ranked_sentences = sorted(((scores[i], sentence) for i, sentence in enumerate(sentences)), reverse=True)
        
        summary = self.summarise_text(scores, sentences)
        
        return summary, ranked_sentences