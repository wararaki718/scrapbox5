
var ws = null;
// var ws = new WebSocket("ws://localhost:8000/ws");

function selectChatRoom(event) {
    var room_id = 0;
    switch (event.target.value) {
        case "room1":
            room_id = 1;
            break;
        case "room2":
            room_id = 2;
            break;
        case "room3":
            room_id = 3;
            break
    }

    if (room_id === 0) {
        return;
    }
    
    ws = new WebSocket("ws://localhost:8000/ws/" + room_id.toString());
    ws.onmessage = function(event) {
        var messages = document.getElementById('messages')
        var message = document.createElement('li')
        var content = document.createTextNode(event.data)
        message.appendChild(content)
        messages.appendChild(message)
    };
}

function sendMessage(event) {
    var input = document.getElementById("messageText");
    ws.send(input.value);
    input.value = '';
    event.preventDefault();
}
