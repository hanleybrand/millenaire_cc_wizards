```csv
wizard_hat_lightning, wizard_robe_lightning, wizard_boots_lightning, wizard_leggings_lightning, 
wizard_hat_sorcery, wizard_robe_sorcery, wizard_boots_sorcery, wizard_leggings_sorcery, 
wizard_hat_fire, wizard_robe_fire, wizard_boots_fire, wizard_leggings_fire, 
wizard_hat_ice, wizard_robe_ice, wizard_boots_ice, wizard_leggings_ice, 
wizard_hat_necromancy, wizard_robe_necromancy, wizard_boots_necromancy, wizard_leggings_necromancy, 
wizard_hat_earth, wizard_robe_earth, wizard_boots_earth, wizard_leggings_earth, 
wizard_hat_healing, wizard_robe_healing, wizard_boots_healing, wizard_leggings_healing


scroll_of_ice_lance,magic_wand, bottle, netherwart, akwardpotion,

dirtwall, pathdirt, pathgravel, pathslabs, sand, gold, wool_orange, wool_magenta, wool_lightblue, wool_yellow, wool_green, wool_cyan, wool_purple, wool_blue, wool_red, wool_limegreen

sapling_appletree, seeds, wheat, feather

beefraw, porkchops, chickenmeat, bone

dye_white
dye_lightblue
dye_yellow
dye_red
carpet_blue
tapestry

tripes
boudin
ciderapple
wah
udon
ikayaki
souvlaki
feta
```

cider is listed as a foreign good but is sold by the culture in shop: tavern

replace item list paste
Item list regex
((\w+):(\w+))\s(\d+)\s+(.+)\s
$3;$1;$4;000/000/000;$5

((\w+):(\w+))\s+(\d)\s+({[\w:\{\[,\]}]+\s}|\s)((\w+\s*)+)
$3;$1;$4;222/222/222;$6

import re
result = re.sub(r'((\w+):(\w+))\s(\d+)\s+(.+)\s', "\3;\1;\4;000/000/000;\5\n", searchText)

// replace unknown Block{} messages

(Block{)((\w+):(\w+))}\/(\d+)\/(?:-\d+|\d+)
$4;$2;$5;false;237/237/333
sed -E 's/((\w+):(\w+))\s(\d+)\s+(.+)\s/\3;\1;\4;000\/000\/000;\5\n/g'

// process entities with a facing=n/s/e/w value string
//  e.g. brewing_barrel;rustic:brewing_barrel;0;false;237/237/333 => 

(\w+);((\w+):(\w+));([\d+]|[=,\w]+);(true|false);([\d\/]+);*(([:\w]+);*(\d+);*(\d+))*

$1_north;$2;facing=north;$6;$7$8
$1_south;$2;facing=south;$6;$7$8
$1_east;$2;facing=east;$6;$7$8
$1_west;$2;facing=west;$6;$7$8


import re
result = re.sub(r'(\w+);((\w+):(\w+));([\d+]|[=,\w]+);(true|false);([\d\/]+);*(([:\w]+);*(\d+);*(\d+))*', "\1_north;\2;facing=north;\6;\7\8\n\1_south;\2;facing=south;\6;\7\8\n\1_east;\2;facing=east;\6;\7\8\n\1_west;\2;facing=west;\6;\7\8", searchText)