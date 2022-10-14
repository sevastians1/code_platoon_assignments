def bottle_song(bottles):

    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} of beer.\nTake one down and pass it around, {bottles} bottles of beer on the wall.")
        bottles = bottles - 1

        if bottles == 1:
            print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.")
            bottles = bottles - 1

        if bottles == 0:
            print(f"No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.")

bottle_song(10)