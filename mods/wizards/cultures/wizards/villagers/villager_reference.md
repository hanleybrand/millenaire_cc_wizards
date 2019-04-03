### Villager tags in groups


##### construction
```
goal=getResourcesForBuild
goal=construction
goal=buildpath
goal=clearoldpath

```



### All the hardcoded tags sorted by type

```
// tags for everybody

// auto-added to all villagers
goal=sleep
```

```
// use as a default goal (it ensures the villager always has somethig to do)
goal=gorest
//go to buildings with the leisure tag
goal=gosocialise
// actually chat
goal=chat
```
```
/// = village defense - may or may not wish to pair with goal=raidvillage
goal=defendvillage
goal=huntmonster
// or 
//
goal=hide
```

```
//player economy
goal=beseller

// foreign merchants in a market
// requires building: tag=market and villager: tag=visitor tag=foreignmerchant chanceWeight=[integer]
goal=keepstall

//village economy
// local merchants
// merchants visit shops for import/export
goal=visitbuilding
// visit a building with tag=inn
goal=visitinn
```


```
//alchemy 
goal=plantwarts
goal=harvestwarts
// currently broken
goal=brewpotions
```

```
// construction 
goal=getResourcesForBuild
goal=construction
goal=buildpath
goal=clearoldpath
```

//// resource gathering //

// Gather items around the villager, if they are of a type declared for that villager.
goal=gathergoods

// lumberjack stuff
// requires a building with tag=grove
goal=choptrees
goal=plantsaplings

// mine at home (from source blocks?)
goal=mining

// at house, requires building with tag=pigs;tag=sheeps;tag=cattle;tag=chicken
goal=breed
goal=shearsheep

// from fishing holes at home or bulding with tag=fishingspot
goal=fish

//requires building with tag=brickkiln
goal=drybrick
goal=gatherbrick

//requires building tag=silkwormfarm
goal=gathersilk


//villager get from TH/shops - pair with goal=delivergoodshousehold
goal=getgoodshousehold
goal=delivergoodshousehold

// villager get from TH/villager home for shop - pair with goal=deliverresourcesshop
goal=gethousethresources
goal=deliverresourcesshop

// bring home resources in villager inventory produced by mining, crafting etc.
// is this case sensitive? 
goal=bringbackresourceshome


// items from a shop for villager's inventory (items in villagerconfig?)
goal=getitemtokeep


// at building with tag=sugarplantation
goal=plantsugarcane
goal=harvestsugarcane

// plant at home - no associate hardcoded building tag
goal=plantcocoa
goal=harvestcocoa

///// -- special case goals

// be a raider, see the world 

goal=raidvillage

// kid stuff
goal=becomeadult

///// -- specific culture goals

// fishing with boneblock 
goal=fishinuit

// get sacrificed
goal=bepujaperformer
// perform sacrifice
goal=performpujas


```

