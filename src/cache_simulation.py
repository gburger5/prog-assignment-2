import sys
from fifo import fifo
from lru import lru
from optff import optff


def main():
    if len(sys.argv) != 2:
        print("Usage: python src/cache_sim.py <input_file>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        k, m = map(int, f.readline().split())
        requests = list(map(int, f.readline().split()))

    print(f"FIFO  : {fifo(k, requests)}")
    print(f"LRU   : {lru(k, requests)}")
    print(f"OPTFF : {optff(k, requests)}")


if __name__ == "__main__":
    main()
