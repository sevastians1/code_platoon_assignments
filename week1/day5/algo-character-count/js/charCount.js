exports.charCount = function(word) {

    word = word.replaceAll(' ', '')

    let dict = {}
    let result_arr = []

    for (let i = 0; i < word.length; i++) {
        if (word[i] in dict) {
            dict[word[i]] += 1
        } else {
            dict[word[i]] = 1
        }
    }


    for (let key in dict) {
        // console.log(dict[index])
        result_arr.push([key, dict[key]])
    }


    // result_arr.sort((a, b) => b[1] - a[1])
    // result_arr.sort((a, b) => b[0] - a[0])
    result_arr.sort((a, b) => a[0].localeCompare(b[0]))
    result_arr.sort((a, b) => b[1] - a[1])

    // console.log(result_arr)

    return result_arr

    // return result_arr.sort((a, b) => a - b)

};
