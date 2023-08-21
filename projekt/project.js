// 1.Deposit the money
// 2.Determine number of lines to bet on
// 3.Collect a bet amount
// 4.Spin the slot machine
// 5.Check if user won
// 6.Give user their winnings
// 7.Play again

const prompt = require("prompt-sync")();

const ROWS = 3;
const COLS = 3;

const SYMBOLS_COUNT = {
    "A": 3,
    "B": 5,
    "C": 7,
    "D": 8
};

const SYMBOLS_VALUES= {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
};


const deposit = () => {
    while (true){
        const depositAmmount = parseFloat(prompt("Enter your deposit: "));
        if (isNaN(depositAmmount) || depositAmmount <= 0){
            console.log('Invalid deposit amount, try again');
        }   else{
            return depositAmmount;
        }
    }   
};

const getNumberOfLines = () => {
    while (true){
        const lines = parseFloat(prompt("Enter number of lines to bet on (1-3): "));
        if (isNaN(lines) || lines <= 0 || lines > 3){
            console.log('Invalid number of lines');
        }   else{
            return lines;
        }
    }   
};

const getBet = (balance, lines) => {
    while (true){
        const bet = parseFloat(prompt("Enter the bet per line: "));
        if (isNaN(bet) || bet <= 0 || bet > balance / lines){
            console.log('Invalid bet, try again');
        }   else{
            return bet;
        }
    }   
};

const spin = () => {
    const symbols = [];
    for (const [symbol, count] of Object.entries(SYMBOLS_COUNT)){
        for (let i = 0; i < count; i++){
             symbols.push(symbol);
        }
    }

    const reels = [];
    for (let i = 0; i < COLS; i++){
        reels.push([]);
        const reelSymbols = [...symbols];
        for (let j = 0; j < ROWS; j++){
            const randomIndex = Math.floor(Math.random() * reelSymbols.length);
            reels[i].push(reelSymbols[randomIndex]);
            reelSymbols.splice(randomIndex, 1);
        }
    }

    return reels;
};

const transpose = (reels) => {
    const rows = [];

    for (let i = 0; i < ROWS; i++){
        rows.push([]);
        for (let j = 0; j < COLS; j++){
            rows[i].push(reels[j][i]);
        }
    }

    return rows;
};

const printrows = (rows) => {
     for (const row of rows){
        let rowString = "";
        for (const [i, symbol] of row.entries()){   //entries zwraca relacje key - vallue a w tym wypadku index - value
            rowString += symbol;
            if (i != row.length - 1){
                rowString += " | ";
            }
        }
        console.log(rowString);
     }
};

const getWinnings = (rows, bet, lines) => {
    let winnings = 0;

    for (let row = 0; row < lines; row++){
        const symbols = rows[row];
        let allSame = true;

        for (const symbol of symbols){
            if (symbol != symbols[0]){
                allSame = false;
                break;
            }
        }

        if (allSame){
            winnings += bet * SYMBOLS_VALUES[symbols[0]]
        }
    }
    return winnings;
};

const game = () => {
    let balance = deposit();

    while (true){
        console.log("You have a balance of $" + balance)
        const reels = spin();
        const lines = getNumberOfLines();
        const bet = getBet(balance, lines);
        balance -= bet * lines;
        const rows = transpose(reels);
        printrows(rows);
        const winnings = getWinnings(rows, bet, lines);
        balance += winnings;
        console.log(`You won $${winnings}`);
        if (balance <= 0){
            console.log("You ran out of money")
            break;
        }

        const playAgain = prompt("Do you want to play again (y/n)? ")
    }
};



game();