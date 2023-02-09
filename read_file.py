import os.path
import pickle
import pandas as pd
import argparse
parser = argparse.ArgumentParser()

parser.add_argument('--dataset', type=str, default='ICEWS14', help="ICEWS14")
parser.add_argument('--file', type=str, choices=['ent_id', 'rel_id', 'ts_id'], help= "files of index")
args = parser.parse_args()
DATA_PATH = './data/'
mid_file = args.dataset + '/' + args.file
file_path  = os.path.join(DATA_PATH, mid_file)

id2name = pd.read_table(file_path, sep = '\t', header = None)
if args.file == 'ent_id':
    rename = 'id2ent'
elif args.file == 'rel_id':
    rename = 'id2rel'
elif args.file == 'ts_id':
    rename = 'id2time'
else:
    FileNotFoundError()

dict1 = dict(zip(id2name[1] , id2name[0]))
out = open(os.path.join(DATA_PATH + args.dataset, rename+'.pickle'), 'wb')
pickle.dump(dict1, out)
out.close()


