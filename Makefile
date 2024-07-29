download:
	cd data && wget https://www.mattmahoney.net/dc/enwik9.zip && wget https://www.mattmahoney.net/dc/enwik8.zip

decompress:
	cd data && unzip enwik8.zip && unzip enwik9.zip

compress:
	python scripts/compress.py