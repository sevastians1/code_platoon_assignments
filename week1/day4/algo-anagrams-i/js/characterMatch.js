exports.isCharacterMatch = function(string1, string2) {

    let string_dict = {}

    string1 = string1.toLowerCase().replaceAll(' ', '')
    string2 = string2.toLowerCase().replaceAll(' ', '')

    // console.log(string1)
    // console.log(string2)

    for (let i = 0; i < string1.length; i++) {
        if (string1[i] in string_dict) {
            string_dict[string1[i]] += 1
        } else {
            string_dict[string1[i]] = 1
        }
    }

    for (let i = 0; i < string2.length; i++) {
        if (string2[i] in string_dict) {
            string_dict[string2[i]] -= 1
        } else {
            return false
        }
    }

    for (let i = 0; i < string_dict.length; i++) {
        if (string_dict[i] > 0) {
            return false
        }
    }

    return true

    console.log(string_dict)

};
