
import sys  
from string import Template


# cropname = sys.argv[1] | 'chamomile'
#cropname = 'chamomile'
#print cropname

crops = ['aloe_vera', 'apple_seeds', 'bee', 'beeswax', 'blood_orchid', 'chamomile', 'chili_pepper', 
'chili_pepper_seeds', 'cloudsbluff', 'cohosh', 'core_root', 'deathstalk_mushroom', 
'dust_tiny_iron', 'ginseng', 'grape_stem', 'grapes', 'honeycomb', 'horsetail', 
'ironberries', 'marsh_mallow', 'mooncap_mushroom', 'olives', 'wildberries', 
'wildberry_bush', 'wind_thistle', 'tallow', 'tomato', 'tomato_seeds', 
'sapling_olive', 'sapling_ironwood', 'sapling_apple']

s = """
priority=50

//tag a building must have for action to be possible. If absent, then the villager's house is used.
buildingTag=$crop

//specify if the label and sentences for this goal is not the name of the goal itself
sentencekey=plantcrop$crop
labelkey=plantcrop$crop

//objets tenus par le villageois
heldItems=rustic:$crop

//Type de plante
//Type of plant
croptype=$crop

soiltype=rustic:fertile_soil
seed=$crop
"""

t = Template(s)

for cropname in crops:
    filename = 'plant' + cropname + '.txt'
    print 'saving ' + filename

    with open(filename, 'w') as f:
       f.writelines(t.substitute(crop=cropname))
   
