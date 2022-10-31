

const addToList = () => {

    let input_value = document.getElementById('input-list')

    console.log(input_value.value)

    let testing = document.getElementById('to-do-list')
    testing.innerHTML += 
        `<li class="list-group-item">
            <input class="form-check-input me-1" type="checkbox" value="" id="thirdCheckboxStretched">
            <label class="form-check-label stretched-link" for="thirdCheckboxStretched">${input_value}</label>
        </li> `


    return testing.innerHTML
}

const getInputValue = () => {

    let newElement = document.createElement("li");
    let inputValue = document.getElementById("myInput").value;
    let newNode = document.createTextNode(inputValue);
    newElement.appendChild(newNode);
}