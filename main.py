import oras.client

client = oras.client.OrasClient()
client.push(files=["random.txt"], target="quay.io/bcook/tuneablechunks-b:1", do_chunked=True, chunk_size=10000000)

# Successfully pushed localhost:5000/dinosaur/artifact:v1
