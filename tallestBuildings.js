/*
! Your job is to count how many buildings currently are the highest.

Example:
const buildings = [ 1250, 800, 600, 1250, 750 ]
The current maximum height buildings are 1250 meters high. There are 2 of them, so return 2 from the function.

Function Description
The function should accept an array of numbers as input.

Returns
The number of buildings that are tallest.
*/



const buildings = [1150, 3023, 2020, 3023, 3023]

const tallestBuildings = (arr) => {
    let highestArr = []
    const highest = Math.max(...arr)
    for (const num of arr) {
        if (num === highest) {
            highestArr.push(num)
        }
    }
    return highestArr.length
}


const answer = tallestBuildings(buildings)

console.log(answer)