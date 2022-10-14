function deafGrandma() {

    let goodbye_count = 0;

    console.log('HEY KID!');

    while (goodbye_count < 2) {
        let usr_input = window.prompt();

        if (usr_input === '') {
            console.log('WHAT?!')
        } else if (usr_input === 'GOODBYE!' && goodbye_count === 0) {
            console.log('LEAVING SO SOON?')
            goodbye_count = goodbye_count + 1
        } else if (usr_input === 'GOODBYE!' && goodbye_count === 1) {
            console.log('LATER, SKATER')
            break
        } else if (usr_input.toUpperCase === usr_input && usr_input != 'GOODBYE!') {
            console.log('NO, NOT SINCE 1946!')
        } else {
            console.log('SPEAK UP, KID')
        }

    }

}

deafGrandma()