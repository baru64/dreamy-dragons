class Game {
  constructor(container, socket) {
    this.view = undefined; // game state
    this.container = container;
    this.socket = socket;
    this.roomid = undefined;
  }

  receive(message) {
    this.view.receive(this, message);
  }

  send() {

  }

  update_view(new_view) {
    this.view = new_view;
    this.view.draw();
  }
}

export { Game };
