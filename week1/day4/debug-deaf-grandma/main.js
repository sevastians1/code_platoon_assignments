function deafGrandma() {

    let program_continue = true

    let goodbyes = 0

    while ( program_continue ) {

        let userInput = window.prompt()

        if ( userInput === "" ) {
            alert("WHAT!?")
        }
        else if ( userInput.toUpperCase() === userInput && userInput != 'GOODBYE!' ) {
            alert('NO, NOT SINCE 1946!')
        }
        else if ( userInput == "GOODBYE!" ) {

            if ( goodbyes === 0 ) {
                alert("LEAVING SO SOON?")
                goodbyes += 1
            }
            else if ( goodbyes === 1 ) {
                alert("LATER, SKATER!")
                program_continue = false
            }
        } else {
            alert("SPEAK UP, KID!")
        }

    }
}

deafGrandma()