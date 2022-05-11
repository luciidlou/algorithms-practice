const solution = (array) => {
    let int = 0
    const sortedArr = array.sort((a, b) => {
        return a - b
    })
    for (let i = 0; i < sortedArr.length; i++) {
        const num1 = sortedArr[i] + 1
        const num2 = sortedArr[i + 1]
        if (num1 !== num2 && num1 > 0) {
            int = num1
            break
        }
        else {
            continue
        }
    }
    return int
}

const array = [-3, 0, 3, -1, 7, 5, 2, 1]

const output = solution(array)

console.log(output)