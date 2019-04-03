import sys
from string import Template
import re

def herb_goals(herbs=None):

    gathering_home = """
// BUILDING TAGS - use in [building].txt files for home gathering
// building.startinggood=$herb,1,8,4

// REQUIRED VILLAGER TAGS  - must be in [villager].txt file for this tag to work
// goal=gather${herb}home

// RECOMMENDED VILLAGER TAGS  - use in [villager].txt files
// startinginv=$herb,8
// bringbackhomegood=$herb
// collectgood=$herb
// 
priority=80
range=2

gatherBlockState=rustic:$herb;age=3
resultingBlockState=rustic:$herb;age=0

helditems=$herb

harvestitem=$herb,100
harvestitem=$herb,100

buildinglimit=$herb,128
maxsimultaneousinbuilding=2
collectInBuilding=true

sentencekey=gather${herb}home
labelkey=gather${herb}home

duration=4000

    """  # type: str

    gathering = """
// BUILDING TAGS - use in [building].txt files for non-residential building to be used for tag
// initial.tag=$herb
// building.startinggood=$herb,1,8,4

// REQUIRED VILLAGER TAGS  - must be in [villager].txt file for this tag to work
// goal=harvest$herb

// RECOMMENDED VILLAGER TAGS  - use in [villager].txt files
// goal=gather$herb
// startinginv=$herb,8
// bringbackhomegood=$herb
// collectgood=$herb
// 

priority=80
range=2
//tag a building must have for action to be possible. If absent, then the villager's house is used.

buildingTag=$herb

gatherBlockState=rustic:$herb;age=3
resultingBlockState=rustic:$herb;age=0

helditems=$herb

harvestitem=$herb,100
harvestitem=$herb,100

buildinglimit=$herb,128
maxsimultaneousinbuilding=2
collectInBuilding=true

sentencekey=gather${herb}home
labelkey=gather${herb}home

duration=4000
    """  # type: str

    buildings = """
    
### HERB: $herb
**BUILDING TAGS** : use in [building].txt files for non-residential building to be used for tag
```
initial.tag=$herb
building.startinggood=$herb,1,8,4
```
    """

    villagers = """
    
### HERB: $herb

**REQUIRED VILLAGER TAGS** must be in [villager].txt file for this tag to work
```
goal=plant$herb
goal=harvest$herb
```

**RECOMMENDED VILLAGER TAGS** : use in [villager].txt files
```
startinginv=$herb,8
bringbackhomegood=$herb
collectgood=$herb
```
    """

    buildings_all = """
initial.tag=$herb
building.startinggood=$herb,1,8,4
        """

    villagers_all = """    
goal=gather${herb}home
gather${herb}
startinginv=$herb,8
bringbackhomegood=$herb
collectgood=$herb
"""

    strings_md = """
goal.gather${herb}home=Gathering $herb_print
goal.gather${herb}home=Gathering $herb_print
    """

    gath_home = Template(gathering_home)
    gath = Template(gathering)
    build = Template(buildings)
    vill = Template(villagers)
    villall = Template(villagers_all)
    buildall = Template(buildings_all)
    stringsfile = Template(strings_md)

    for herb in herbs:

        gather_home_filename = 'genericgatherblocks/gather' + herb + 'home.txt'
        gather_filename = 'genericgatherblocks/harvest' + herb + '.txt'

        print 'saving ' + gather_home_filename
        with open(gather_home_filename, 'w') as f:
            f.writelines(gath_home.substitute(herb=herb))

        print 'saving ' + gather_filename
        with open(gather_filename, 'w') as fi:
            fi.writelines(gath.substitute(herb=herb))

    with open('_building_tag_list.md', 'w') as bt:
        print 'saving building_tag_list.txt'
        for herb in herbs:
            bt.writelines(build.substitute(herb=herb))
        bt.write("""\n### All Tags \n ``` """)
        for herb in herbs:
            bt.writelines(buildall.substitute(herb=herb))
        bt.write("""\n```\n""")


    with open('_villager_tag_list.md', 'w') as vt:
        print 'saving building_tag_list.txt'
        for herb in herbs:
            vt.writelines(vill.substitute(herb=herb))
        vt.write("""\n### All Tags \n ``` """)
        for herb in herbs:
            vt.writelines(villall.substitute(herb=herb))
        vt.write("""\n```\n""")

    with open('_strings.md', 'w') as st:
        print 'saving strings_list.txt'
        st.write("""\n### Copy these to languages/[lang]]/stings.txt \n ``` """)
        for herb in herbs:
            herb_print = re.sub(r'([A-Za-z]+)(:?_*)([A-Za-z]*)', "\u\1 \u\3", herb)
            st.writelines(stringsfile.substitute(herb=herb, herb_print=herb_print))
        st.write("""\n```\n""")

if __name__ == "__main__":

    herbs = ['aloe_vera', 'blood_orchid', 'chamomile', 'cloudsbluff', 'cohosh', 'core_root',
             'deathstalk_mushroom',  'ginseng',  'horsetail', 'marsh_mallow', 'mooncap_mushroom', 'wind_thistle']
    herb_goals(herbs)