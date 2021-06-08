from zipfile import ZipFile
import os
import numpy as np
import tensorflow as tf
from tensorflow import keras

class Pretrained:
    def __init__(self, dim, dataset):
        self.dim = dim
        self.file_path = self._data_lookup[dataset]['path'] + self._dimension_files[str(dim)] + '.txt'
        self.url = self._data_lookup[dataset]['url']
        self.cache = self._data_lookup[dataset]['cache_name']
        self.embeddings_index = {}
        
    dataset_path = '/root/.keras/datasets'
    
    _data_lookup = {
        'glove6b': {'cache_name': 'glove6b', 'url': "http://nlp.stanford.edu/data/glove.6B.zip", 'path': 'glove.6B.'},
        'glove27b': {'cache_name': 'glove27b', 'url': "http://nlp.stanford.edu/data/glove.twitter.27B.zip", 'path': 'glove.twitter.27B.'}
    }
    
    _dimension_files = {
        '50' : '50d',
        '100': '100d',
        '200': '200d',
        '300': '300d'
    }
    
    def create_from_file(self, file):
        # TODO: modify self vars with upload
        #   attempt to modify init variables given the file path name
        try:
            with open(file) as f:
                for line in f:
                    word, coefs = line.split(maxsplit=1)
                    coefs = np.fromstring(coefs, 'f', sep=' ')
                    self.embeddings_index[word] = coefs
        except IOError:
            print("File doesn't exist on disk. Try running download_from_url()")
            
    
    def download_from_url(self):
        zip_path = os.path.join(self.dataset_path, self.cache)
        file_path = os.path.join(self.dataset_path, self.file_path)
        
        if os.path.isfile(zip_path):
            print('Unzipping from cache')
            with ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extract(self.file_path, self.dataset_path)
                
            print('Creating embedding dictionary')
            self.create_from_file(file_path)
        else:
            print('Dowloading from {}'.format(self.url))
            keras.utils.get_file(
                self.cache,
                self.url,
                extract=True
            )
            self.create_from_file(file_path)