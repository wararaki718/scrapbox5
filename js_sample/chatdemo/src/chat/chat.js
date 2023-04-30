import React, {useState} from "react";

var websocket = new WebSocket("ws://localhost:8000/ws");

const Chat = () => {
    const [message, setMessage] = useState("");
    const [messages, setMessages] = useState([]);

    websocket.onmessage = (event) => {
        setMessages([...messages, event.data]);
        event.preventDefault();
    };

    const handleChangeMessage = (event) => {
        setMessage(event.target.value);
        event.preventDefault();
    };

    const sendMessage = (event) => {
        websocket.send(message);
        setMessage("");
        event.preventDefault();
    };

    return (
        <div>
            Chat
            <form action="" onSubmit={sendMessage}>
                <input type="text" autocomplete="off" value={message} onChange={handleChangeMessage} />
                <button>send</button>
            </form>
            
            <ul>
                { messages.map(msg => (<li key={Date.now()}>{msg}</li>)) }
            </ul>
        </div>
    );
};

export default Chat;
