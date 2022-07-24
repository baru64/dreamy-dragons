import { RoomView } from "./room-view.js";

class JoinRoomView {
  constructor(game) {
    this.game = game;
  }

  draw() {
    this.game.container.innerHTML = `
    <h1>Drunk Pyrate</h1>
    <p>
    Username:
    <input type="text" id="username-input"/>
    </p>
    <p>
    Room id:
    <input type="text" id="room-input"/>
    </p>
    `;
    let button = document.createElement("button");
    button.textContent = "join";
    button.addEventListener(
      "click",
      function () {
        console.log(this);
        this.join();
      },
      false
    );
    this.game.container.appendChild(button);
  }

  join() {
    let username = document.getElementById("username-input").value;
    let roomid = document.getElementById("room-input").value;
    this.game.socket.send(
      JSON.stringify({
        type: "joinRequest",
        content: {
          username: username,
          roomid: roomid,
        },
      })
    );
    this.game.roomid = roomid;
  }

  receive(message) {
    switch (message.type) {
      case "joinResponse":
        this.game.update_view(new RoomView(this.game));
        break;
    }
  }
}

export { JoinRoomView };
