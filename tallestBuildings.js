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