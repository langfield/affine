#srun -w osmium -c 20 --mem 30000 -J affine python3 transform.py ../geo-emb/pretrained-embeddings/top_10000_emb.txt Word2Vec
srun -w osmium -c 20 --mem 30000 -J affine python3 transform.py ../geo-emb/pretrained-embeddings/GoogleNews-vectors-negative300.bin Word2Vec
#srun -w osmium -c 20 --mem 30000 -J affine python3 transform.py ../geo-emb/pretrained-embeddings/first-100__source--GoogleNews-vectors-negative300.txt Word2Vec
