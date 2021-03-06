[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

### About the game

* a 2048-like tile game, in which you move and combine tiles to bigger ones
* goal is to build a castle (32768) at the center of the board
* implemented in python, with pygame framework
* usage
```
python ./src/main.py
```
### How to play
* The castle is the block in the middle, your goal is to upgrade to 2048 or higher!
* Move blocks with equal values to merge them
* To move the blocks, use these keys: 
  * <kbd>W</kbd> / <kbd>A</kbd> / <kbd>S</kbd> / <kbd>D</kbd>
  * <kbd>H</kbd> / <kbd>J</kbd> / <kbd>K</kbd> / <kbd>L</kbd>
  * <kbd>Up</kbd> / <kbd>Down</kbd> / <kbd>Left</kbd> / <kbd>Right</kbd>
* Bring up the option (help) menu: <kbd>F1</kbd> or <kbd>Esc</kbd>

### Changelog
* alpha 0.10: 2019-01-27: pretty much done with all the aspects of the gameplay
* alpha 0.11: 2019-01-30: added sound efffect and fixed frame rate
* alpha 0.12: 2019-02-02: better menu ui
* alpha 0.13: 2019-02-03: Added achievement system (trophy), with game save

### Todo list
* improve the win condition for castle
* implement the progression system (in option)
* better logger system
* `[partially implemented]` add a SAVE/LOAD/checkpoint system
* add ABOUT in game
* add top score / casle int othe SAVE/LOAD
* [high priority] fixed the trophy bug (two 512 icons)


### Off Todo list
* `[done at 1/27/2019]` implement the moving tiles                    
* `[done at 1/27/2019]` add a license                                 
* `[done at 1/29/2019]` replace the assets                            
* `[done at 1/30/2019]` move the textures from board to flag         
* `[done at 1/30/2019]` move the block shorten logic to ui.py        
* `[done at 1/30/2019]` numeral text with flexible font size         
  * (depends on block size)
* `[done at 1/30/2019]` add simple music                             
* `[done at 1/30/2019]` lock the frame rate                          
* `[done at 1/30/2019]` numeral text shown in the center of the block
* `[done at 1/30/2019]` limit the action space / key intput
* `[done at 1/31/2019]` make GameOver screen transparent
* `[done at 1/31/2019]` improve the status bar
* `[done at 2/03/2019]` improve the menu system
* `[done at 2/03/2019]` add in-game help
* `[done at 2/03/2019]` implement the tropy/achievement system
* `[done at 2/07/2019]` add screenshot into the readme
* `[done at 2/07/2019]` git tag and release


### Misc
Some of the assets are from the `dungeon crawl 32x32 tiles` ([OGA link](http://opengameart.org/content/dungeon-crawl-32x32-tiles))

### Contact
whoji (whoji@null.net)

### Screenshots

* Main menu:

![](./asset/screenshot/screenshot_0.png "main menu")

* Game view: 

![](./asset/screenshot/screenshot_1.png "game view")
