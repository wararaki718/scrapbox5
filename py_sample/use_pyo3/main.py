import use_pyo3


def main():
    result = use_pyo3.sum_as_string(5, 10)
    print(result)
    print("DONE")


if __name__ == "__main__":
    main()
