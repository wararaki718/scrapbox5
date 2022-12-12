use mini_redis::{client, Result};


async fn say_world() {
    println!("world");
}


#[tokio::main]
async fn main() -> Result<()> {
    let url = "127.0.0.1:6379";
    let mut client = client::connect(url).await?;

    client.set("hello", "world".into()).await?;

    let result = client.get("hello").await?;

    println!("value: {:?}", result);
    println!("");


    let op = say_world();
    println!("hello");

    op.await;

    println!("DONE");



    return Ok(());
}
