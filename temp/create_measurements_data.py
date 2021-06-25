#this gives priority to measurements so it will show the larger one in the grocery list
#second item in list is the unit in cups

measurements = {}
measurements[1] = [['gallon'], 16]
measurements[3] = [['quart'], 4]
measurements[4] = [['pint'], 2]
measurements[2] = [['cup', 'c', 'cups'], 1]
measurements[5] = [['oz', 'ounce', 'ounces'], .125]
measurements[6] = [['tbsp', 'tablespoon', 'tablespoons'], .0625]
measurements[7] = [['tsp', 'teaspoon', 'teaspoons'], .0208]