import React, {useState} from "react";

var websocket = new WebSocket("ws://localhost:8000/ws");

const Chat = () => {
    const [message, setMessage] = useState("");
    const [messages, setMessages] = useState([]);

    websocket.onmessage = (event) => {
        setMessages(messages => [...messages, event.data]);
    };

    const handleChangeMessage = (event) => {
        setMessage(event.target.value);
    };

    const sendMessage = (event) => {
        if (message.length > 0) {
            websocket.send(message);
            setMessage("");
        }
        event.preventDefault();
    };

    return (
        <div>
            Chat
            <form>
                <input type="text" autoComplete="off" value={message} onChange={handleChangeMessage} />
                <button onClick={sendMessage}>send</button>
            </form>
            
            <ul>
                { messages.map(msg => (<li key={messages.length}>{msg}</li>)) }
            </ul>
        </div>
    );
};

export default Chat;
