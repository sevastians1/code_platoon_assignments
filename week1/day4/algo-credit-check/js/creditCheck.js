exports.creditCheck = function(str) {

    let num_arr = []

    for (let i = 0; i < str.length; i++) {
        if (i % 2 === 0) {
            let product = Integer(str[i]) * 2

            let sum = 0

            if (product >= 10) {
                for (singleDigit in String(product)) {
                    sum += parseInt(singleDigit)
                }
            } else {
                num_arr.push(sum)
            }
        } else {
            num_arr.push(parseInt(str[i]))
        }
    }

    let result = 0

    for (num in num_arr) {
        result += parseInt(num)
    }
    
    console.log(result)

    if (result % 10 === 0) {
        return "The number is valid!"
    } else {
        return "The number is invalid!"
    }

}
