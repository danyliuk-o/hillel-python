const readline = require("readline");

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

rl.question("Enter a number of seconds (0 <= n < 8640000): ", (answer) => {
    const secondsInput = parseInt(answer, 10);

    const days = Math.floor(secondsInput / (24 * 60 * 60));
    let remainder = secondsInput % (24 * 60 * 60);

    const hours = Math.floor(remainder / (60 * 60));
    remainder = remainder % (60 * 60);

    const minutes = Math.floor(remainder / 60);
    const seconds = remainder % 60;

    let dayWord;
    if (days % 10 === 1 && days % 100 !== 11) {
        dayWord = "день";
    } else if ([2, 3, 4].includes(days % 10) && !(days % 100 >= 11 && days % 100 <= 14)) {
        dayWord = "дні";
    } else {
        dayWord = "днів";
    }

    const pad = (n) => String(n).padStart(2, "0");

    console.log(`${days} ${dayWord} ${pad(hours)}:${pad(minutes)}:${pad(seconds)}`);

    rl.close();
});
