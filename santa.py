import random

# names = ['Linda', 'Jake', 'Alex', "Moana", "Jess"]
snowy_tree_with_snow = '''
       *        .       *        .
  .        .       *        .        *
        .       *       .        .
    *         *        .       *
       *        .       *         .
                  *
         .       /_\\     .        .
      *      .  /___\\   *       .
   .        *  /_____\\     .       *
      *    .  /_______\\  .       *
  .        . /_________\\    *
        *        ||         .       .
   *       .     ||    .       *
      .      *         *      .       .
         *        .       *        .
'''
print(snowy_tree_with_snow)

print("Welcome to Linda's secret santa simulator.\nWhat's your name?")
userName = input()
print("Hello, " + userName)
snow_scene = '''
       .     *       .        .  *      *
   .       .    *         .       . *       .
      *     .     *  .     *      .        *
 .       *     .      *         .    .        *
      *      .  *      .    *         *
  .        .        * .        .  *       .  
      *      .        * .   .        *       
    *   .     .  *       .        *      .
'''
print(snow_scene)

print("Enter the names of the people you want to pair.")
names = input()
names=[name.strip() for name in names.split(",")]

def pairPeople(names):
    # print("Participant names:", names)
    pairs={name:None for name in names}
    # print("Initial Pairs", pairs)
    possiblePairs = {name:[] for name in names}

    for name in pairs: 
        val = pairs[name]
        # print(f"\n\nName: {name}, Val: {val}")
        # print(f"\n\n{name}")
        if val == None:
            # print("Nobody assigned yet")
            for n in names:
                if n != name:
                    # print("Possible pair:",name, n)
                    possiblePairs[name].append(n)
    # print("Possible pairs:" ,possiblePairs)

    #while each name isn't assigned exactly once:

    uniqueVals = len(set(pairs.values()))#there has to be same num unique values as # participants 
    # print(uniqueVals)

    count = 0 
    while uniqueVals != len(names): 
        for name in pairs:
            # print(name)
            possible = possiblePairs[name]
            # print(possible)
            random.shuffle(possible)
            # print(possible)
            
            pairs[name] = possible[0]
        uniqueVals = len(set(pairs.values()))
        count +=1
    # print("COUNT: ", count)
    print(snow_scene,"\n\n\nFinal pairs:")
    return pairs

j=pairPeople(names)
print(j)