
import pandas as pd
from shorttext.utils import standard_text_preprocessor_1
from shorttext.clustering import KMeansClusterer

# load the data
def load_data(file_path):
    return pd.read_csv(file_path)

# preprocess text
def preprocess_text(text):
    preprocessor = standard_text_preprocessor_1()
    return preprocessor(text)

# function to perform clustering on the aspects
def cluster_aspects(data, num_clusters=5):
    # preprocess the aspects
    data['processed_aspect'] = data['aspect'].apply(preprocess_text)
    
    # extract unique aspects
    unique_aspects = data['processed_aspect'].unique()
    
    # clustering
    clusterer = KMeansClusterer(num_clusters)
    labels = clusterer.cluster(unique_aspects, verbose=False)
    
    # create a mapping of aspect to cluster
    aspect_cluster_mapping = dict(zip(unique_aspects, labels))
    return aspect_cluster_mapping

# main function to load data, process it, and cluster aspects
def main(file_path):
    data = load_data(file_path)
    
    # cluster the aspects
    aspect_cluster_mapping = cluster_aspects(data)
    
    # print the aspect to cluster mapping
    for aspect, cluster in aspect_cluster_mapping.items():
        print(f'Aspect: {aspect}, Cluster: {cluster}')

if __name__ == '__main__':
    file_path = 'path_to_your_file.csv'  
    main(file_path)
