### Goal

Input closet -> Run algorithm -> Get outfits for the day

### Basic algorithm

1. Create nodes for all clothing items
2. Calculate weights based on ruleset
3. Generate paths of complete fits using Dijkstra's graph algorithm

### Ex:

```
The weather is 57 degrees - warm enough for most clothes. I recommend one of the following:
Stussy Our Legacy T Shirt, 517 Orange Tabs, Nike White Air Forces
Yeezy Gap Black Hoodie, Black Blank T Shirt, Dickies Black Double Knee, Suicoke Mura-V Slides
Helmut Lang Lava Logo Hoodie, White Blank T Shirt, Dickies Black Double Knee, Doc Marten Black 1461
```

### Formatting

The main files to format are rotation.txt (which is where the items you want to input live) and
ruleset.txt (where the rules of the way you dress are listed to determine the weight of the nodes).
Ruleset was separated in design to allow the user to import different rulesets easily. For instance, if you were
to trust my judgment, my ruleset could easily be fit into your rotation.txt file.

#### rotation.txt Format

Take a look at the file there by default (my current rotation) to see the basic formatting. </br>
Generally:

```
<Category>
"Clothing Item Name in Quotes" PrimaryColor/SecondaryColor Brand1,Brand2 Cold,Warm
```

Note that you can have only one color, brand, or only either cold or warm. </br>
You cannot have more than two colors (for now), and a collaboration can only be up to two pieces. </br>
All items are to use a capitalized letter followed by lowercase, and in the case that a brand has a space,
simply negate that space. </br>
In a future version - this will be fixed to make it easier to load data in. </br>
Also note that the order of the colors matters, Black/White is different from White/Black.

There are five categories currently accepted:

HAT </br>
Item 1 ... </br>
Item 2 ... </br>

OUTERWEAR </br>

TOP </br>

PANT </br>

SHOES </br>

#### ruleset.txt Format

To be written...
