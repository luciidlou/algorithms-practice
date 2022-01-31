/*
Palindrome Numbers:
? A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
! Find the largest palindrome made from the product of two 3-digit numbers.
*/

const palindromeNumbers = (start, stop) => {
    let palindromesArr = []
    for (let i = start; i < stop; i++) {
        for (let n = start; n < stop; n++) {
            let product = i * n
            let str = product.toString()
            let arr = str.split("")
            let reversedArr = arr.reverse()
            let reversedStr = reversedArr.join("")
            if (str === reversedStr) {
                palindromesArr.push(product)
            }
        }
    }
    const largestPalindrome = Math.max(...palindromesArr)
    return largestPalindrome
}

const answer = palindromeNumbers(100, 1000)
console.log(answer)
