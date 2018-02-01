#// Input: [1,0,0,0,0,0,1,0,0]
#//
#//    3 => true
#//    4 => false
#//
#// Input: [1,0,0,1,0,0,1,0,0]
#//
#//    1 => true
#//    2 => false
#//
#// Input: [0]
#//
#//    1 => true
#//    2 => false

#public boolean canPlaceFlowers(List<Boolean> flowerbed, int numberToPlace) {
#    // Implementation here
#}

# [0, 0]

def canPlaceFlowers(bed, numToPlace):
  # assume bed is python sequence

  lastFlower = None

  for candidate, hasPlant in enumerate(bed):
    if hasPlant:
      lastFlower = candidate
      continue

    if (lastFlower is None or candidate - lastFlower >= 2) and
        (candidate == len(bed) - 1 or not bed[candidate + 1):

      lastFlower = candidate
      numToPlant -= 1
      if not numToPlant:
        break


    return numToPlace == 0
