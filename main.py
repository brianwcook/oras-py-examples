import oras.client

client = oras.client.OrasClient()
client.push(files=["random.txt"], target="quay.io/bcook/tuneablechunk:2", do_chunked=True, chunk_size=83886080)

# Successfully pushed localhost:5000/dinosaur/artifact:v1
# Out[4]: <Response [201]>
