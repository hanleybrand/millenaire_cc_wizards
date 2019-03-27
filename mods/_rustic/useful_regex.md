### create villager/building tags from itemlist (not useful in every case)

pattern and subs
`(\w+),\d+,\d+,\d+,\d+,\d+,(true|false),.*`

```
startinginv=$1,8
bringbackhomegood=$1
collectgood=$1

initial.tag=$1
building.startinggood=$1,8,4
```

``` python
import re
result = re.sub(r'(\w+),\d+,\d+,\d+,\d+,\d+,(true|false),.*', "startinginv=\1,8\nbringbackhomegood=\1\ncollectgood=\1\n\n\ninitial.tag=\1\nbuilding.startinggood=\1,8,4\n", searchText)
```

### block subs

pattern

```
(\w+);((\w+):(\w+));([\d+]|[=,\w]+);(true|false);([\d\/]+);*(([:\w]+);*(\d+);*(\d+))*
```


```
// just facing
$1_north;$2;facing=north;$6;$7$8 \r
$1_south;$2;facing=south;$6;$7$8 \r
$1_east;$2;facing=east;$6;$7$8 \r
$1_west;$2;facing=west;$6;$7$8 \r


// facing with top/bottom
// just facing
$1_north_top;$2;half=top,facing=north;$6;$7$8
$1_south_top;$2;half=top,facing=south;$6;$7$8
$1_east_top;$2;half=top,facing=east;$6;$7$8
$1_west_top;$2;half=top,facing=west;$6;$7$8
$1_north_bottom;$2;half=bottom,facing=north;$6;$7$8
$1_south_bottom;$2;half=bottom,facing=south;$6;$7$8
$1_east_bottom;$2;half=bottom,facing=east;$6;$7$8
$1_west_bottom;$2;half=bottom,facing=west;$6;$7$8

$1_north_top_inner_left;$2;half=top,shape=inner_left,facing=north;$6;$7$8
$1_south_top_inner_left;$2;half=top,shape=inner_left,facing=south;$6;$7$8
$1_east_top_inner_left;$2;half=top,shape=inner_left,facing=east;$6;$7$8
$1_west_top_inner_left;$2;half=top,shape=inner_left,facing=west;$6;$7$8
$1_north_bottom_inner_left;$2;half=bottom,shape=inner_left,facing=north;$6;$7$8
$1_south_bottom_inner_left;$2;half=bottom,shape=inner_left,facing=south;$6;$7$8
$1_east_bottom_inner_left;$2;half=bottom,shape=inner_left,facing=east;$6;$7$8
$1_west_bottom_inner_left;$2;half=bottom,shape=inner_left,facing=west;$6;$7$8
$1_north_top_inner_right;$2;half=top,shape=inner_right,facing=north;$6;$7$8
$1_south_top_inner_right;$2;half=top,shape=inner_right,facing=south;$6;$7$8
$1_east_top_inner_right;$2;half=top,shape=inner_right,facing=east;$6;$7$8
$1_west_top_inner_right;$2;half=top,shape=inner_right,facing=west;$6;$7$8
$1_north_bottom_inner_right;$2;half=bottom,shape=inner_right,facing=north;$6;$7$8
$1_south_bottom_inner_right;$2;half=bottom,shape=inner_right,facing=south;$6;$7$8
$1_east_bottom_inner_right;$2;half=bottom,shape=inner_right,facing=east;$6;$7$8
$1_west_bottom_inner_right;$2;half=bottom,shape=inner_right,facing=west;$6;$7$8
$1_north_top_outer_left;$2;half=top,shape=outer_left,facing=north;$6;$7$8
$1_south_top_outer_left;$2;half=top,shape=outer_left,facing=south;$6;$7$8
$1_east_top_outer_left;$2;half=top,shape=outer_left,facing=east;$6;$7$8
$1_west_top_outer_left;$2;half=top,shape=outer_left,facing=west;$6;$7$8
$1_north_bottom_outer_left;$2;half=bottom,shape=outer_left,facing=north;$6;$7$8
$1_south_bottom_outer_left;$2;half=bottom,shape=outer_left,facing=south;$6;$7$8
$1_east_bottom_outer_left;$2;half=bottom,shape=outer_left,facing=east;$6;$7$8
$1_west_bottom_outer_left;$2;half=bottom,shape=outer_left,facing=west;$6;$7$8
$1_north_top_outer_right;$2;half=top,shape=outer_right,facing=north;$6;$7$8
$1_south_top_outer_right;$2;half=top,shape=outer_right,facing=south;$6;$7$8
$1_east_top_outer_right;$2;half=top,shape=outer_right,facing=east;$6;$7$8
$1_west_top_outer_right;$2;half=top,shape=outer_right,facing=west;$6;$7$8
$1_north_bottom_outer_right;$2;half=bottom,shape=outer_right,facing=north;$6;$7$8
$1_south_bottom_outer_right;$2;half=bottom,shape=outer_right,facing=south;$6;$7$8
$1_east_bottom_outer_right;$2;half=bottom,shape=outer_right,facing=east;$6;$7$8
$1_west_bottom_outer_right;$2;half=bottom,shape=outer_right,facing=west;$6;$7$8


// half=top,shape=inner_left,facing=north
// bottom = true, false], 
// facing =[north, south, west, east]}, 
// mirror = [true, false]}, 
// top =[true, false]

$1_north_top_inner_left;$2;half=top,shape=inner_left,facing=north;$6;$7$8
$1_south_top_inner_left;$2;half=top,shape=inner_left,facing=south;$6;$7$8
$1_east_top_inner_left;$2;half=top,shape=inner_left,facing=east;$6;$7$8
$1_west_top_inner_left;$2;half=top,shape=inner_left,facing=west;$6;$7$8
$1_north_bottom_inner_left;$2;half=bottom,shape=inner_left,facing=north;$6;$7$8
$1_south_bottom_inner_left;$2;half=bottom,shape=inner_left,facing=south;$6;$7$8
$1_east_bottom_inner_left;$2;half=bottom,shape=inner_left,facing=east;$6;$7$8
$1_west_bottom_inner_left;$2;half=bottom,shape=inner_left,facing=west;$6;$7$8
$1_north_top_inner_right;$2;half=top,shape=inner_right,facing=north;$6;$7$8
$1_south_top_inner_right;$2;half=top,shape=inner_right,facing=south;$6;$7$8
$1_east_top_inner_right;$2;half=top,shape=inner_right,facing=east;$6;$7$8
$1_west_top_inner_right;$2;half=top,shape=inner_right,facing=west;$6;$7$8
$1_north_bottom_inner_right;$2;half=bottom,shape=inner_right,facing=north;$6;$7$8
$1_south_bottom_inner_right;$2;half=bottom,shape=inner_right,facing=south;$6;$7$8
$1_east_bottom_inner_right;$2;half=bottom,shape=inner_right,facing=east;$6;$7$8
$1_west_bottom_inner_right;$2;half=bottom,shape=inner_right,facing=west;$6;$7$8
$1_north_top_outer_left;$2;half=top,shape=outer_left,facing=north;$6;$7$8
$1_south_top_outer_left;$2;half=top,shape=outer_left,facing=south;$6;$7$8
$1_east_top_outer_left;$2;half=top,shape=outer_left,facing=east;$6;$7$8
$1_west_top_outer_left;$2;half=top,shape=outer_left,facing=west;$6;$7$8
$1_north_bottom_outer_left;$2;half=bottom,shape=outer_left,facing=north;$6;$7$8
$1_south_bottom_outer_left;$2;half=bottom,shape=outer_left,facing=south;$6;$7$8
$1_east_bottom_outer_left;$2;half=bottom,shape=outer_left,facing=east;$6;$7$8
$1_west_bottom_outer_left;$2;half=bottom,shape=outer_left,facing=west;$6;$7$8
$1_north_top_outer_right;$2;half=top,shape=outer_right,facing=north;$6;$7$8
$1_south_top_outer_right;$2;half=top,shape=outer_right,facing=south;$6;$7$8
$1_east_top_outer_right;$2;half=top,shape=outer_right,facing=east;$6;$7$8
$1_west_top_outer_right;$2;half=top,shape=outer_right,facing=west;$6;$7$8
$1_north_bottom_outer_right;$2;half=bottom,shape=outer_right,facing=north;$6;$7$8
$1_south_bottom_outer_right;$2;half=bottom,shape=outer_right,facing=south;$6;$7$8
$1_east_bottom_outer_right;$2;half=bottom,shape=outer_right,facing=east;$6;$7$8
$1_west_bottom_outer_right;$2;half=bottom,shape=outer_right,facing=west;$6;$7$8

```