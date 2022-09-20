from datasketch import MinHash, MinHashLSH


def main():
    n_perm = 128
    v1 = [1, 3, 5, 6]
    v2 = [2, 3, 5, 6]
    v3 = [2, 4, 6, 7]
    m1 = MinHash(num_perm=n_perm)
    m2 = MinHash(num_perm=n_perm)
    m3 = MinHash(num_perm=n_perm)

    byte_length = 4
    for d in v1:
        m1.update(d.to_bytes(byte_length, byteorder="big"))
    for d in v2:
        m2.update(d.to_bytes(byte_length, byteorder="big"))
    for d in v3:
        m3.update(d.to_bytes(byte_length, byteorder="big"))
    
    lsh = MinHashLSH(threshold=0.5, num_perm=n_perm)
    lsh.insert("m2", m2)
    lsh.insert("m3", m3)
    result = lsh.query(m1)
    print(result)

    print("DONE")


if __name__ == "__main__":
    main()
