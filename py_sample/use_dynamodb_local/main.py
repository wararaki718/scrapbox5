from client import DBClient
from config import TableConfig
from item import Item


def main():
    client = DBClient()

    table_name = "example"
    table_config = TableConfig(
        key_schema=[
            {
                "AttributeName": "username",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "last_name",
                "KeyType": "RANGE"
            }
        ],
        attribute_definitions=[
            {
                "AttributeName": "username",
                "AttributeType": "S"
            },
            {
                "AttributeName": "last_name",
                "AttributeType": "S"
            },
        ],
        provisioned_throughput={
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5
        }
    )
    client.create_table(table_name, table_config)
    print(f"create table: {table_name}")

    item = Item(
        username="janedoe",
        first_name="Jane",
        last_name="Doe",
        age=25,
        account_type="standard_user"
    )
    client.insert(item)
    print("data inserted")

    key = {
        "username": "janedoe",
        "last_name": "Doe"
    }
    result = client.get(key)
    print(result)

    client.delete_table()
    print("delete table")

    print("DONE")


if __name__ == "__main__":
    main()
