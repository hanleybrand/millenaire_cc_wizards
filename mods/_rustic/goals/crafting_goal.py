import sys
import os.path as path
import csv
from string import Template
import re

mc_instance = '/Users/hanley/Documents/Curse/Minecraft/Instances/Millenaire dev'

shapeless_file = 'pmdumper/shapeless_recipes_2019-04-03_17-29-00.csv'
shaped_file = 'pmdumper/shaped_recipes_2019-04-03_17-28-38.csv'

shapeless_csv = path.join(mc_instance, shapeless_file)
shaped_csv = path.join(mc_instance, shaped_file)


class MillRec:
    def __init__(self, mod, item, inputs, outputs):
        self.mod = mod
        self.item = item
        self.inputs = inputs
        self.outputs = outputs
        self.input_list = []
        self.goal_template = """ 
priority=50
duration=5000
sentencekey=make$item
labelkey=make$item

heldItems=$heldlist

input=clay,1
output=$output,$outputcount

// townhalllimit=$output,512

sound=$sound
"""

        def make_in(self, item, count):
            return 'input=%s,%i' % (item, count)

        def make_out(self, item, count):
            return 'output=%s,%i' % (item, count)


goal_template = """ 
priority=50
duration=5000
sentencekey=make$item
labelkey=make$item

heldItems=$heldlist

input=clay,1
output=$output,$outputcount

// townhalllimit=$output,512

sound=$sound
"""


def make_in(item, count):
    return 'input=%s,%i\n' % (item, count)


def make_out(item, count):
    return 'output=%s,%i\n' % (item, count)


def get_count(in_out_put):
    pattern = re.compile(r'(?:.+)(\sx)(\d)')
    result = re.sub(pattern, "\2", in_out_put)


with open(shapeless_csv) as shapeless:
    reader = csv.DictReader(shapeless)
    recipe = {}

    for row in reader:
        # ID,Group,Input Ingredients,Output Item
        id = row['ID'].split(':')
        mod = id[0]
        item = id[1]
        group = row['Group']
        inputs = row['Input Ingredients'].split('\n')
        outputs = row['Output Item'].split('\n')

        if mod == 'rustic':

            if inputs.__len__() == 1 and inputs[0].__len__() == 0:
                continue

            input_lines = []
            held_items = []
            output_lines = []

            for lin in inputs:
                print('doing inputs')
                ln_splt = lin.split(' x')
                try:
                    print(int(ln_splt[-1]))
                    if int(ln_splt[-1]) > 1:
                        count = ln_splt[-1]
                        item = ln_splt[0]
                        input_lines.append(make_in(ln_splt[0], ln_splt[-1]))
                    else:
                        input_lines.append(make_in(ln_splt[0], 1))
                except ValueError:
                    input_lines.append(make_in(ln_splt[0], 1))

            for lin in outputs:
                print('doing outputs')
                ln_splt = lin.split(' x')
                try:
                    print(int(ln_splt[-1]))
                    if int(ln_splt[-1]) > 1:
                        count = ln_splt[-1]
                        item = ln_splt[0]
                        output_lines.append(make_out(ln_splt[0], ln_splt[-1]))
                    else:
                        input_lines.append(make_out(ln_splt[0], 1))
                except ValueError:
                    input_lines.append(make_out(ln_splt[0], 1))
                except TypeError:
                    input_lines.append(make_out(ln_splt[0], 1))

            recipe[row['ID']] = {'mod': id[0], 'item': id[1], 'inputs': input_lines, 'outputs': output_lines}
            rec = recipe[row['ID']]

            # print(rec)


#        for i in inputs:

#
# if id[0] == 'rustic':
#     print(id[1], input, output)

def herb_goals(herbs=None):
    crafting_home = """
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

// REQUIRED VILLAGER TAGS  - must be in [villager].txt file for this tag to work
// goal=gather$herb

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

villagelimit=$herb,64
maxsimultaneoustotal=2

sentencekey=gather${herb}
labelkey=gather${herb}

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
goal=gather${herb}home
// or
goal=gather${herb}
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
goal=gather${herb}
startinginv=$herb,8
bringbackhomegood=$herb
collectgood=$herb
"""

    strings_md = """
goal.gather${herb}home=Gathering $herb_print
goal.gather${herb}home=Gathering $herb_print
    """

    craft_home = Template(crafting_home)
    gath = Template(gathering)
    build = Template(buildings)
    vill = Template(villagers)
    villall = Template(villagers_all)
    buildall = Template(buildings_all)
    stringsfile = Template(strings_md)

    # for herb in herbs:  #     gather_home_filename = 'genericgatherblocks/gather' + herb + 'home.txt'  #     gather_filename = 'genericgatherblocks/gather' + herb + '.txt'  #  #     print 'saving ' + gather_home_filename  #     with open(gather_home_filename, 'w') as f:  #         f.writelines(craft_home.substitute(herb=herb))  #  #     print 'saving ' + gather_filename  #     with open(gather_filename, 'w') as fi:  #         fi.writelines(gath.substitute(herb=herb))  #  # with open('_building_tag_list.md', 'w') as bt:  #     print 'saving building_tag_list.txt'  #     for herb in herbs:  #         bt.writelines(build.substitute(herb=herb))  #     bt.write("""\n### All Tags \n ``` """)  #     for herb in herbs:  #         bt.writelines(buildall.substitute(herb=herb))  #     bt.write("""\n```\n""")  #  # with open('_villager_tag_list.md', 'w') as vt:  #     print 'saving building_tag_list.txt'  #     for herb in herbs:  #         vt.writelines(vill.substitute(herb=herb))  #     vt.write("""\n### All Tags \n ``` """)  #     for herb in herbs:  #         vt.writelines(villall.substitute(herb=herb))  #     vt.write("""\n```\n""")  #  # with open('_strings.md', 'w') as st:  #     print 'saving strings_list.txt'  #     st.write("""\n### Copy these to languages/[lang]]/stings.txt \n ``` """)  #     for herb in herbs:  #         herb_print = re.sub(r'([A-Za-z]+)(:?_*)([A-Za-z]*)', "\u\1 \u\3", herb)  #         # st.writelines(stringsfile.substitute(herb=herb, herb_print=herb_print))  #         st.writelines(stringsfile.substitute(herb=herb, herb_print=herb))  #     st.write("""\n```\n""")

# if __name__ == "__main__":
# herbs = ['aloe_vera', 'blood_orchid', 'chamomile', 'cloudsbluff', 'cohosh', 'core_root', 'deathstalk_mushroom',
#          'ginseng', 'horsetail', 'marsh_mallow', 'mooncap_mushroom', 'wind_thistle']
# herb_goals(herbs)
