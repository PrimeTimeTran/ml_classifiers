import os
import shutil
import pickle

base_dir = os.path.dirname(os.path.abspath(__file__))
save_dir = os.path.join(base_dir, '../../tmp/output')
logs_dir = os.path.join(base_dir, '../../tmp/logs')
data_dir = os.path.join(base_dir, '../../tmp/dataset')

def get_file_name(type, model_type):
    return os.path.join(save_dir, f'../matrices/{model_type}-confusion-matrix-for-{type}-data.png')

def setup_save_directory():
    if os.path.exists(save_dir):
        shutil.rmtree(save_dir)
    os.makedirs(save_dir, exist_ok=True)

def image_file_name(idx, value):
    return os.path.join(
        save_dir, f'{idx}-original-{value}-predict-{value}.png')

def create_log_file(name):
    return open(f'{logs_dir}/{name}', "w")


def create_pickle(clf, model_type):
    with open(f'tmp/models/{model_type}_MNIST.pickle', 'wb') as f:
        pickle.dump(clf, f)
    pickle_in = open(f'tmp/models/{model_type}_MNIST.pickle', 'rb')
    clf = pickle.load(pickle_in)
    return clf
