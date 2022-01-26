const sumOfMultiples = () => {
    let nums = []
    for (let i = 0; i <= 1000; i++) {
        if (i % 3 === 0 || i % 5 === 0) {
            nums.push(i)
        }
    }

    const getSum = (total, num) => {
        return total + Math.round(num);
    }

    const sum = nums.reduce(getSum, 0)
    return sum
}

const answer = sumOfMultiples()

console.log(answer)