class Game {
    constructor(width, height) {
        this.canvas = document.getElementById('gameCanvas');
        this.context = this.canvas.getContext('2d');

        // Set canvas size dynamically
        this.canvas.width = width;
        this.canvas.height = height;

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
        // Handle keyboard and mouse events here
    }

    render() {
        this.context.clearRect(0, 0, this.canvas.width, this.canvas.height); // Clear screen

        // Draw a simple red square for testing
        this.context.fillStyle = "red";
        this.context.fillRect(50, 50, 100, 100);
    }
}

// Ensure the script runs after the page loads
window.onload = () => {
    new Game(800, 600);
};
