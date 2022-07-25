import { Player } from "./player.js";
import { TextCardView } from "./text-card-view.js";

class RoomView {
  constructor(game) {
    this.game = game;
    this.players = [];
  }

  draw() {
    this.game.container.textContent = "";
    let header = document.createElement("h1");
    header.textContent = "Drunk Pyrate room " + this.game.roomid;
    let playerList = document.createElement("div");
    playerList.innerHTML = `
      <table>
      <thead><tr>Players</tr></thead>
      <tbody>
      </tbody>
      </table>
    `;
    let button = document.createElement("button");
    button.textContent = "start";
    button.addEventListener(
      "click",
      () => {
        this.sendStart();
      },
      false
    );

    // add elements to container
    this.game.container.appendChild(header);
    this.game.container.appendChild(playerList);
    this.game.container.appendChild(button);
  }

  drawPlayers() {
    let tbody = document.getElementsByTagName('tbody')[0];
    tbody.textContent = "";
    this.players.forEach(player => {
      let row = document.createElement('tr');
      row.textContent = player.username;
      tbody.appendChild(row);
    });
  }

  sendStart() {
    this.game.socket.send(
      JSON.stringify({
        type: "start",
        content: {},
      })
    );
  }

  receive(message) {
    switch (message.type) {
      case "addPlayer":
        this.players.push(
          new Player(message.content.id, message.content.username)
        );
        this.drawPlayers();
        break;
      case "removePlayer":
        let i = this.players.length;
        while (i--) {
          if (this.players[i].id == message.content.id) {
            this.players.splice(i, 1);
          }
        }
        this.drawPlayers();
        break;
      case "newCard":
        switch (message.content.card_type) {
          case "text":
            this.game.update_view(new TextCardView(this.game, message.content.card_value));
            break;
        }
    }
  }
}

export { RoomView };
