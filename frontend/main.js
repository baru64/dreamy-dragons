import { Game } from './modules/game.js';
import { NoConnectionView } from './modules/no-connection-view.js';
import { JoinRoomView } from './modules/join-room-view.js';

const socket = new WebSocket("ws://localhost:3000/ws");
const container = document.getElementById("container");
const game = new Game(container, socket);

socket.addEventListener("open", () => {
  // connection opens
  game.update_view(new JoinRoomView(game));
});

socket.addEventListener("close", () => {
  // connection closes
  game.update_view(new NoConnectionView(game));
});

// receive a message from the server
socket.addEventListener("message", ({ data }) => {
  const message = JSON.parse(data);
  game.view.receive(message);
});
