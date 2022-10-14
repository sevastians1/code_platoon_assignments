exports.calculateMode = function(list) {

    let dict = {}
    let result = []

    for (i in list) {
        if (list[i] in dict) {
            dict[list[i]] += 1
        } else {
            dict[list[i]] = 1
        }
    }

    // console.log(dict)

    let top_count = 0

    for (key in dict) {
        if (dict[key] > top_count) {
            top_count = dict[key]
        }
    }

    for (key in dict) {
        if (dict[key] === top_count) {
            result.push(key)
        }
    }

    

    console.log(result)

    return result

}
