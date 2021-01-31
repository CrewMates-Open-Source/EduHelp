import numpy as np     
import networkx as nx 
import nltk 
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance

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
    
    
    def summarise_text(self, scores, sentences, th):
        summary = []
        max_len = len(sentences)
        #th = np.mean(scores)
        for i in range(max_len):
            if(scores[i]< th):
                continue
            summary.append(" ".join(sentences[i]))

        summary = ". ".join(summary)

        return summary
    
    def save_file(text):
        file1 = open("summary.txt","w")
        file1.write(text)
        file1.close()
    
    def summariser(self, text):
        #Breaking Down text to Sentences
        sentences = []
        in1 = text
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
        sum1 = 0
        for i, sentence in enumerate(sentences):
            sum1 += scores[i]
        # Sorting the Sentences with scores in descending order
        if(len(sentences)>0):
            mean = float(sum1)/len(sentences)
        else:
            mean = 0
        # ranked_sentences = sorted(((scores[i], sentence) for i, sentence in enumerate(sentences)), reverse=True)
        
        summary = self.summarise_text(scores, sentences, mean)
        
        if len(summary) < 1:
            save_file(in1)
            print('file Saved as summary.txt')
            return in1, scores
        print('file Saved as summary.txt')
        save_file(summary)
        return summary, scores