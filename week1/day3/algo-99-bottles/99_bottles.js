function bottleSong(bottles) {

  while (bottles > 1) {

    console.log(`${bottles} bottles of beer on the wall, ${bottles} of beer.\nTake one down and pass it around, ${bottles} bottles of beer on the wall.`)
    bottles = bottles - 1
    
  }

  if (bottles === 1) {
    console.log(`${bottles} bottle of beer on the wall, ${bottles} bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.`)
    bottles = bottles - 1
  }

  if (bottles === 0) {
    console.log(`No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.`)
  }


};

bottleSong(10);