exports.factorial = function(num) {

    if (num === 0) {
        return 1
    }

    let product = BigInt(1)
    
    while (num > 0) {
        product *= BigInt(num)
        num -= 1
    }

    result = parseInt(product)
    // console.log(result)

    return result

};

