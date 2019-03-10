URL="https://nlp.stanford.edu/data/glove.6B.zip"
curl -Lo glove.6B.zip $URL

unzip glove.6B.zip
rm glove.6B.100d.txt glove.6B.200d.txt glove.6B.300d.txt glove.6B.zip
