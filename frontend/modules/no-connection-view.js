class NoConnectionView {
  constructor(game) {
    this.game = game;
  }

  draw() {
    this.game.container.textContent = "No connection. Reload this page to reconnect.";
  }

  receive(message) {

  }
}

export { NoConnectionView };
