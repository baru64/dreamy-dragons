class NoConnectionView {
  constructor(game) {
    this.game = game;
  }

  draw() {
    this.game.container.textContent = "";
    let p = document.createElement('p');
    p.textContent = "No connection. Reload this page to reconnect.";
    this.game.container.appendChild(p);
  }

  receive(message) {

  }
}

export { NoConnectionView };
