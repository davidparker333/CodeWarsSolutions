// Let's play! You have to return which player won! In case of a draw return Draw!.

// Examples:

// rps('scissors','paper') // Player 1 won!
// rps('scissors','rock') // Player 2 won!
// rps('paper','paper') // Draw!

const rps = (p1, p2) => {
  let winner;
  const rpsMap = {
    rock: "scissors",
    paper: "rock",
    scissors: "paper",
  };
  if (rpsMap[p1] === p2) {
    winner = "1";
  } else if (rpsMap[p2] === p1) {
    winner = "2";
  }
  return winner ? `Player ${winner} won!` : "Draw!";
};

console.log(rps("scissors", "rock"));
