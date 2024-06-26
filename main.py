import argparse

from src.model import Model
from src.cnn import CNN

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-s", "--strategy", type=str, default='knn')
    ap.add_argument("-m", "--method", type=str, default='train')
    args = vars(ap.parse_args())
    strategy = args['strategy']
    method = args['method']

    model = Model(strategy)

    if strategy == 'cnn':
      model = CNN()
      model.train()
    elif method == 'train':
      model.train()
    elif method == 'init_trained_model':
      model.init_trained_model()
