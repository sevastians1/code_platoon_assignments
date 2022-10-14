exports.toRoman = function(num) {

    let result = []

    while (num > 0) {
        while(num >= 1000) {
            num -= 1000
            result.push('M')
        }
        
        if (num >= 900) {
            num -= 900
            result.push('CM')
        }

        if (num - 500 < 100 && num - 500 >= 0) {
            num -= 500
            result.push('D')
        }

        if (num - 400 < 100 && num - 400 >= 0) {
            num -= 400
            result.push('CD')
        }

        while (num >= 100 && num <= 399) {
            num -= 100
            result.push('C')
        }

        if (num >= 90) {
            num -= 90
            result.push('XC')
        }

        if (num - 50 < 10 && num - 50 >= 0) {
            num -= 50
            result.push('L')
        }

        if (num - 40 < 10 && num - 40 >= 0) {
            num -= 40
            result.push('XL')
        }

        while (num >= 10 && num <= 39) {
            num -= 10
            result.push('X')
        }

        if (num >= 9) {
            num -= 9
            result.push('IX')
        }

        if (num - 5 < 1 && num - 5 >= 0) {
            num -= 5
            result.push('V')
        }

        if (num - 4 < 1 && num - 4 >= 0) {
            num -= 4
            result.push('IV')
        }

        while (num >= 1 && num <= 3) {
            num -= 1
            result.push('I')
        }
        
    }

    return result.join('')
}

