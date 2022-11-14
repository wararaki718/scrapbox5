use std::collections::HashMap;
use qdrant_client::prelude::{Payload, QdrantClient, QdrantClientConfig};
use qdrant_client::qdrant::{
    CreateCollection,
    Distance,
    PointStruct,
    SearchPoints,
    Value,
    VectorsConfig,
    VectorParams
};
use qdrant_client::qdrant::vectors_config::Config;


#[tokio::main]
async fn main() {
    let config = QdrantClientConfig::from_url("http://localhost:6334");
    let client = QdrantClient::new(Some(config)).await.unwrap();

    let collections_list = client.list_collections().await.unwrap();
    println!("{:?}\n", collections_list);

    let collection_name = "test";
    client.delete_collection(collection_name).await.unwrap();

    client
        .create_collection(&CreateCollection {
            collection_name: collection_name.into(),
            vectors_config: Some(
                VectorsConfig {
                    config: Some(
                        Config::Params(
                            VectorParams {
                                size: 10,
                                distance: Distance::Cosine.into()
                            }
                        )
                    )
                }
            ),
            hnsw_config: None,
            on_disk_payload: None,
            optimizers_config: None,
            replication_factor: None,
            shard_number: None,
            timeout: None,
            wal_config: None,
            write_consistency_factor: None
        })
        .await.unwrap();

    let collection_info = client.collection_info(collection_name).await.unwrap();
    println!("collection info:");
    println!("{:?}\n", collection_info);

    let payload: Payload = vec![
        ("foo", "Bar".into()),
        ("bar", 12.into()),
    ].into_iter().collect::<HashMap<_, Value>>().into();

    let points = vec![
        PointStruct::new(0, vec![12.; 10], payload)
    ];
    client.upsert_points_blocking(collection_name, points).await.unwrap();

    let search_result = client
        .search_points(&SearchPoints {
            collection_name: collection_name.into(),
            vector: vec![11.; 10],
            filter: None,
            limit: 10,
            with_vectors: None,
            with_payload: None,
            params: None,
            score_threshold: None,
            offset: None,
            vector_name: None
        })
        .await.unwrap();
    
    println!("{:?}", search_result);
}
