class TextCardView {
  constructor(game, text) {
    this.game = game;
    this.text = text;
  }

  draw() {
    this.game.container.textContent = "";
    let p = document.createElement('p');
    p.textContent = this.text;
    this.game.container.appendChild(p);
  }

  sendSkip() {
    this.game.socket.send(
      JSON.stringify({
        type: "skip",
        content: {},
      })
    );
  }

  receive(message) {
    switch (message.type) {
      case "newCard":
        break;
    }
  }
}

export { TextCardView };
