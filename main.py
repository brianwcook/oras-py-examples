import oras.client
import os
import argparse
import oras.utils


parser = argparse.ArgumentParser()
parser.add_argument('--file', dest='file_name', type=str, help='file to upload')
parser.add_argument('--config', dest='manifest_config', type=str, help='manifest config')
parser.add_argument('--target', dest='target', type=str, help='where to store the file')

args = parser.parse_args()

path = args.file_name.split('/')[0:-1]
path = "/".join(path)
file = args.file_name.split('/')[-1]
print(path, file)
os.chdir(path)

client = oras.client.OrasClient()
client.push(files=[file], target=args.target, do_chunked=True, chunk_size=1000000000)

