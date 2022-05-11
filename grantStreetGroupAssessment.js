function solution(S) {
    const letterArr = S.split("")
    const N = letterArr.length
    let answer = 0

    for (let i = 0; i < N; i++) {
        const letter1 = letterArr[i]
        const letter2 = letterArr[i + 1]
        const letter3 = letterArr[i + 2]
        if (letter1 === letter2) {
            continue
        }
        else {
            if (letter2 === letter3) {
                continue
            }
            else {
                answer += 1
            }
        }
    }
    return answer
}



const string = "babaa"

const output = solution(string)

console.log(output)