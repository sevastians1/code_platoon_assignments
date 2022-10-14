exports.palindrome = function(word) {

    new_str = String(word).toLowerCase()

    regex = /[^a-z0-9]/gi

    filtered_str = new_str.replace(regex, '')

    // console.log(filtered_str)

    reversed_string = filtered_str.split('').reverse().join('')

    if (filtered_str === reversed_string) {
        return true
    }

    return false

};
