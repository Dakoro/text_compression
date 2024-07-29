import mmap
import timeit
import gzip

def mmap_io(filename: str):
    with open(filename, mode="r", encoding="utf8") as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
            text = mmap_obj.read()
    return text

def main():
    path = "/home/dakoro/Github/text_compression/data/.ready4cmix"
    text = mmap_io(path)
    text_compress = gzip.compress(text)
    print(100 * len(text_compress)/len(text))

if __name__ == "__main__":
    main()
    timeit.timeit("main()", number=5)