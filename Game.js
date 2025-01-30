class Game {
    constructor(width, height) {
        this.canvas = document.getElementById('gameCanvas');
        this.context = this.canvas.getContext('2d');
        this.running = true;
        this.lastTime = 0;
        this.update = this.update.bind(this);
        this.render = this.render.bind(this);
        this.handleEvents = this.handleEvents.bind(this);
        window.addEventListener('beforeunload', () => this.running = false);
        this.run();
    }

    run() {
        requestAnimationFrame(this.update);
    }

    update(timestamp) {
        if (!this.running) return;
        this.handleEvents();
        this.render();
        this.lastTime = timestamp;
        requestAnimationFrame(this.update);
    }

    handleEvents() {
        // Klavye ve fare olaylarını burada işleyebilirsin
    }

    render() {
        this.context.clearRect(0, 0, this.canvas.width, this.canvas.height); // Ekranı temizle
        // Oyun nesnelerini burada çiz
    }
}

window.onload = () => {
    new Game(800, 600);
};
