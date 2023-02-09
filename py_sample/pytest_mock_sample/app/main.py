from modules import Item, Shop


def main():
    shop = Shop()

    items = [
        Item(id=1, name="apple", price=100),
        Item(id=2, name="orenge", price=200),
        Item(id=3, name="peach", price=300),
        Item(id=4, name="banana", price=400),
    ]

    for item in items:
        shop.set_item(item)
    
    for i, _ in enumerate(items):
        item = shop.get_item(i)
        print(item)
    
    print("DONE")


if __name__ == "__main__":
    main()
