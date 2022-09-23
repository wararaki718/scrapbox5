from jaccard import jaccard
from minhash import MinHash


def main():
    m1 = MinHash()
    m2 = MinHash()
    m3 = MinHash()
    a = [1, 2, 3, 4, 5]
    b = [3, 4, 5, 6, 7]
    c = [1, 3, 4, 5, 6]

    byte_len = 4
    for i in a:
        m1.update(i.to_bytes(byte_len, byteorder="big"))
    
    for j in b:
        m2.update(j.to_bytes(byte_len, byteorder="big"))
    
    for k in c:
        m3.update(k.to_bytes(byte_len, byteorder="big"))
    
    result1 = jaccard(m1, m2)
    print(result1)
    result2 = jaccard(m1, m3)
    print(result2)
    print("DONE")


if __name__ == "__main__":
    main()
