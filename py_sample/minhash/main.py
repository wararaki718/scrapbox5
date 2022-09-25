from jaccard import jaccard
from lsh import LSH
from minhash import MinHash


def main():
    m1 = MinHash()
    m2 = MinHash()
    m3 = MinHash()
    a = [1, 3, 5, 6]
    b = [2, 3, 5, 6]
    c = [2, 4, 6, 7]

    byte_len = 4
    for i in a:
        m1.update(i.to_bytes(byte_len, byteorder="big"))
    
    for j in b:
        m2.update(j.to_bytes(byte_len, byteorder="big"))
    
    for k in c:
        m3.update(k.to_bytes(byte_len, byteorder="big"))
    
    s1 = jaccard(m1, m2)
    print(s1)
    s2 = jaccard(m1, m3)
    print(s2)
    
    
    lsh = LSH(threshold=0.5)
    lsh.insert("m2", m2)
    lsh.insert("m3", m3)

    result = lsh.query(m1)
    print(result)

    print("DONE")


if __name__ == "__main__":
    main()
