import sys
from string import Template

def plant_goals(crops=None):

    planting_goal = """
// BUILDING TAGS - use in [building].txt files for non-residential building to be used for tag
// initial.tag=$crop
// building.startinggood=$crop,8,4

// REQUIRED VILLAGER TAGS  - must be in [villager].txt file for this tag to work
// goal=plant$crop

// RECOMMENDED VILLAGER TAGS  - use in [villager].txt files
// goal=harvest$crop
// startinginv=$crop,8
// bringbackhomegood=$crop
// collectgood=$crop
// 

priority=50
//buildinglimit=$crop,64
//townhalllimit=$crop,64
//maxsimultaneousinbuilding=1

//tag a building must have for action to be possible. If absent, then the villager's house is used.
buildingTag=$crop

//specify if the label and sentences for this goal is not the name of the goal itself
sentencekey=plantcrop$crop
labelkey=plantcrop$crop

//objets tenus par le villageois -- Items they hold
heldItems=$crop

//Type de plante --Type of plant
croptype=$crop

soiltype=rustic:fertile_soil
seed=$crop

//goal.plantcrop$crop=planting $crop

    """  # type: str

    harvesting_goal = """
// BUILDING TAGS - use in [building].txt files for non-residential building to be used for tag
// initial.tag=$crop
// building.startinggood=$crop,8,4

// REQUIRED VILLAGER TAGS  - must be in [villager].txt file for this tag to work
// goal=harvest$crop

// RECOMMENDED VILLAGER TAGS  - use in [villager].txt files
// goal=plant$crop
// startinginv=$crop,8
// bringbackhomegood=$crop
// collectgood=$crop
// 


priority=40
// buildinglimit=$crop,64
// townhalllimit=$crop,64
// maxsimultaneousinbuilding=1

//tag a building must have for action to be possible. If absent, then the villager's house is used.
buildingTag=$crop

//specify if the label and sentences for this goal is not the name of the goal itself
sentencekey=harvest$crop
labelkey=harvest$crop

// (Minecraft ID of a block ('wheat')):Type of plant to harvest.
croptype = $crop

//(item, chance and (optional) required tag ('leather,50' or 'boudin,50,oven')):
//Item to be harvested, with chance.
harvestitem $crop,50

//  Boons for irrigated villages. (item (from itemlist.txt)):
irrigationbonuscrop = $crop

// Blockstate the crop must have to be harvested. If not set, must have a meta of 7.
// (a Minecraft blockstate ('red_flower;type=blue_orchid')):
harvestblockstate=$crop;age=3


    """  # type: str

    buildings = """
    
### CROP: $crop
**BUILDING TAGS** : use in [building].txt files for non-residential building to be used for tag
```
initial.tag=$crop
building.startinggood=$crop,8,4
```
    """

    villagers = """
    
### CROP: $crop

**REQUIRED VILLAGER TAGS** must be in [villager].txt file for this tag to work
```
goal=plant$crop
goal=harvest$crop
```

**RECOMMENDED VILLAGER TAGS** : use in [villager].txt files
```
startinginv=$crop,8
bringbackhomegood=$crop
collectgood=$crop
```
    """

    buildings_all = """
initial.tag=$crop
building.startinggood=$crop,8,4
        """

    villagers_all = """    
goal=plant$crop
goal=harvest$crop
startinginv=$crop,8
bringbackhomegood=$crop
collectgood=$crop
"""

    strings_md = """
goal.plant$crop=Planting $crop
goal.harvest$crop=Harvesting $crop
    """

    plantt = Template(planting_goal)
    harvt = Template(harvesting_goal)
    build = Template(buildings)
    vill = Template(villagers)
    villall = Template(villagers_all)
    buildall = Template(buildings_all)
    stringsfile = Template(strings_md)

    for cropname in crops:
        plant_filename = 'plant' + cropname + '.txt'
        harvest_filename = 'harvest' + cropname + '.txt'

        print 'saving ' + plant_filename
        with open(plant_filename, 'w') as f:
            f.writelines(plantt.substitute(crop=cropname))

        print 'saving ' + harvest_filename
        with open(harvest_filename, 'w') as fi:
            fi.writelines(harvt.substitute(crop=cropname))

    with open('_building_tag_list.md', 'w') as bt:
        print 'saving building_tag_list.txt'
        for cropname in crops:
            bt.writelines(build.substitute(crop=cropname))
        bt.write("""\n### All Tags \n ``` """)
        for cropname in crops:
            bt.writelines(buildall.substitute(crop=cropname))
        bt.write("""\n```\n""")


    with open('_villager_tag_list.md', 'w') as vt:
        print 'saving building_tag_list.txt'
        for cropname in crops:
            vt.writelines(vill.substitute(crop=cropname))
        vt.write("""\n### All Tags \n ``` """)
        for cropname in crops:
            vt.writelines(villall.substitute(crop=cropname))
        vt.write("""\n```\n""")

    with open('_strings.md', 'w') as st:
        print 'saving strings_list.txt'
        st.write("""\n### Copy these to languages/[lang]]/stings.txt \n ``` """)
        for cropname in crops:
            st.writelines(stringsfile.substitute(crop=cropname))
        st.write("""\n```\n""")

if __name__ == "__main__":

    crops = ['aloe_vera', 'blood_orchid', 'chamomile', 'chili_pepper', 'cloudsbluff', 'cohosh', 'core_root',
             'deathstalk_mushroom',  'ginseng',  'horsetail', 'marsh_mallow', 'mooncap_mushroom', 'wind_thistle']
    plant_goals(crops)