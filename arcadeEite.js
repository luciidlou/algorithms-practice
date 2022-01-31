/*
* Arcade Elite
? An arcade game player wants to climb to the top of the leaderboard and track their ranking. 
? The game uses Dense Ranking, so its leaderboard works like this:

! The player with the highest score is ranked number 1 on the leaderboard.

! Players who have equal scores receive the same ranking number, and the next 
! player(s) receive the immediately following ranking number.

* Example:
topFiveScores = [ 500, 450, 450, 300, 290, 270 ]
? The ranked players will have ranks 1, 2, 2, 3, 4 and 5, respectively. 
currentPlayerGameScores = [ 290, 400, 500 ]
? If the player's scores are 290, 400 and 500, their rankings after each game played would be 4, 3 and 1.

Return the current player's ranking.

* Function Description:
Your function should accept two inputs:
? An array of leaderboard scores as whole numbers
? An array of scores for the current player as whole numbers

! Your function should return an array of whole numbers, with each number representing the player's rank after each score.

* Constraints:
The number array for the leaderboard should contain numbers for only the top 5 scores.
The number array for the leaderboard should contain numbers in the following range: 10 ⩽ 𝓷 ⩽ 500
The number array for the player's game scores can contain 𝓷 numbers.
The number array for the player's game scores should contain numbers in the following range: 10 ⩽ 𝓷 ⩽ 500
If the player's score is not in the range of scores for the leaderboard, then there should be no ranking added to return array.
The existing leaderboard array numbers must be in descending order.
The player's scores array numbers must be in ascending order.

Example Input
[ 490, 450, 400, 320, 320, 290 ]
[ 50, 310, 480, 200, 350, 180 ]

Return value.
[ 5, 2, 4 ]

* Explanation of Results:
50 was not in the range of leaderboard scores, so rank was not added to return array.
310 would be the 5th ranked score, so a rank was added to the return array.
480 would be the 2nd ranked score, so a rank was added to the return array.
200 was not in the range of leaderboard scores, so rank was not added to return array.
350 would be the 4th ranked score, so a rank was added to the return array.
180 was not in the range of leaderboard scores, so rank was not added to return array.
*/

const arcadeElite = (currentTopScores, currentPlayerScores) => {
    let rankings = []
    for (const topScore of currentTopScores) {
        currentPlayerScores.sort((first, second) => { return first - second })
        for (const playerScore of currentPlayerScores) {
            if (playerScore >= topScore) {
                currentTopScores.push(playerScore)
                currentTopScores.sort((first, second) => { return second - first })
                currentTopScores.pop()
                let index = currentPlayerScores.findIndex(num => num === playerScore)
                currentPlayerScores.splice(index, 1)
                let rank = currentTopScores.findIndex(num => num === playerScore)
                rankings.push(rank + 1)
            }
        }
    }
    return rankings
}

const topScores = [490, 450, 400, 320, 320]
const playerScores = [50, 310, 480, 200, 350, 180]

const playerRankings = arcadeElite(topScores, playerScores)
console.log(playerRankings)