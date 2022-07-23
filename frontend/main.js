const socket = new WebSocket("ws://localhost:3000/ws");

socket.addEventListener("open", () => {
  // send a message to the server
  socket.send(JSON.stringify({
    type: "hello",
    content: "hello from client"
  }));
});

// receive a message from the server
socket.addEventListener("message", ({ data }) => {
  const message = JSON.parse(data);

  switch (message.type) {
    case "hello":
      let container = document.getElementById("container");
      container.innerHTML = message.content;
      break;
  }
});
