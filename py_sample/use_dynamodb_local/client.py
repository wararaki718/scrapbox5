import boto3
from boto3.dynamodb.table import TableResource

from config import TableConfig
from item import Item


class DBClient:
    def __init__(self, url: str="http://localhost:8000") -> None:
        self._dynamodb = boto3.resource(
            service_name="dynamodb",
            endpoint_url=url,
            aws_access_key_id="",
            aws_secret_access_key="",
            region_name=""
        )
        self._table = None

    def create_table(self, table_name: str, table_config: TableConfig) -> None:
        self._table = self._dynamodb.create_table(
            TableName=table_name,
            KeySchema=table_config.key_schema,
            AttributeDefinitions=table_config.attribute_definitions,
            ProvisionedThroughput=table_config.provisioned_throughput
        )

    def insert(self, item: Item) -> None:
        self._table.put_item(Item=item.to_dict())
    
    def get(self, key: dict) -> dict:
        response = self._table.get_item(
            Key=key
        )
        return response["Item"]

    def delete_table(self) -> None:
        self._table.delete()
