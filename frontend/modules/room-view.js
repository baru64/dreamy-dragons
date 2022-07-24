class RoomView {
  constructor(game) {
    this.game = game;
  }

  draw() {
    this.game.container.textContent = "";
    let header = document.createElement('h1');
    header.textContent = "Drunk Pyrate room " + this.game.roomid;
    let playerList = document.createElement('div');
    playerList.textContent = `
      <table>
      <thead><tr>Players</tr></thead>
      <tbody>
      </tbody>
      </table>
    `
    let button = document.createElement('button');
    button.textContent = "start";
    button.onclick = this.sendStart();

    // add elements to container
    this.game.container.appendChild(header);
    this.game.container.appendChild(playerList);
    this.game.container.appendChild(button);
  }

  sendStart() {

  }

  receive(message) {
    switch (message.type) {
      case "playersUpdate":
        break;
    }
  }
}

export { RoomView };
