// REMEMBER TO PSEUDOCODE
const pad = (array, minSize, value=null) => {
    
    if (array.length >= minSize) {
        // console.log('working')
        return array
    } else {
        let add_length = minSize - array.length
        // console.log(add_length)
        
        for (let i = 0; i < add_length; i++) {
            array.push(value)
        }
    }
    // console.log(array)
    return array




exports.pad = pad;
