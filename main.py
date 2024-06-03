import oras.client
import os

file_name="disk.qcow2.gz"
file_stats=os.stat(file_name)
file_size=file_stats.st_size
print("file size:", str(file_size))

client = oras.client.OrasClient()
client.push(files=["disk.qcow2.gz"], target="quay.io/bcook/tuneablechunks-b:2", do_chunked=True, chunk_size=100000000)

