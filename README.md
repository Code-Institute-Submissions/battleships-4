<h1 align="center">BattleShip</h1>

Live Website: <a href="https://battleship-project3.herokuapp.com/">Heroku Site</a>

GitHub Repository: <a href="https://github.com/cathalmc-dev/battleships">Github Repository</a>

## About

This application is based around the classic game Battleship. This version is for 1 player.

## Table of Contents
[User Experience (UX)](#ux)

[Features](#features)

[Debugging](#debugging)

[Technologies Used](#technologies)

[Testing](#testing)

[Deployment](#deployment)

[Known Bugs](#bugs)

[Credits](#credits)

<a name="ux"></a>
## User Experience (UX)

### User Stories
- #### As any player
  1. I want to easily be able to see what coordinates I have and have not hit.
  1. I don't wan't large amounts of text to distract from the game itself.
  1. I want to be able to alter the difficulty.

### Design
- The rows and columns are numbered and lettered respectively. I felt that this was the best way for the user to be able to keep track of what coordinates they were aiming at. Numbering both would lead to confusion and poor user experience.

### Existing Features
- [x] **Variable Amounts of Ships** - allows the user to have between 3 and 6 ships on the 25 square board. This allows the player to tailor their experience to their own taste.
- [x] **Clearly Labeled Axes** - Makes for a smooth user exerience by preventing confusion or squinting at the board.

### Future Features
- [ ] Variable grid size based on user choice.
- [ ] Variable ship sizes, between 2 and 5 units long and in numbers that suit the chosen grid size.
- [ ] Shot counter which the player can limit to thier preference.

<a name="debugging"></a>
## Debugging

Throughout the development of this project, there were some bugs and issues that needed to be resolved. Here are a few of the standout problems I faced.

- **Wrong Input Type Throwing ValueErrors**
    - Tried to nestle try, except block within an if statement and as a result the ValueErrors were not being handled properly.
    - Resolved by restructuring the logic gates. Try-except now dealt with first and then the outcome is handled by the if else statement.
    - I have used this same structure in a few different functions.

- **Input Check Function Infinite While Loop**
    - Tried to do all my checking on the input coordinate in 1 function through the use of a while loop but it became too complex and was prone to infinite looping.
    - Restructured the checking into multiple smaller functions.

- **Unable to draw the shot on the board**
    - Got confused and tried to build the board update function around the coordinate as a list of 2 list items.
    - Once I realised I decided to convert the guess input into 3 different forms, one for each use.
    - The guess the give back to the player, the converted 2 digit number which I add to the list of in use coordinates and the list the row and column as an item each for each of mapping.

    <a name="technologies"></a>
## Technologies Used

### Languages Used

- [Python](https://www.python.org/)

- [Git](https://git-scm.com/) - Git was used for version control.
- [GitPod](https://www.gitpod.io/) - GitPod, through GitHub, hosted the IDE used for the entirety of this project.
- [Github](https://github.com/) - GitHub is used to host the project files.
- [Heroku](https://www.heroku.com/) - Heroku is used to deploy the application.

<a name="deployment"></a>
## Deployment

    - To prep the application for deployment to Heroku I had to add a newline (\n) 
    character at the end of every input field for proper display.
    - I then went to Heroku itself and added the PORT: 8000 Config Var.
    - The buildpacks used for this application are Python and NodeJS, in that order.

### Build Log From Heroku

-----> Building on the Heroku-20 stack
-----> Using buildpacks:
       1. heroku/python
       2. heroku/nodejs
-----> Python app detected
-----> No Python version was specified. Using the same version as the last build: python-3.9.7
       To use a different version, see: https://devcenter.heroku.com/articles/python-runtimes
-----> No change in requirements detected, installing from cache
-----> Using cached install of python-3.9.7
-----> Installing pip 20.2.4, setuptools 47.1.1 and wheel 0.36.2
-----> Installing SQLite3
-----> Installing requirements with pip
-----> Node.js app detected
       
-----> Creating runtime environment
       
       NPM_CONFIG_LOGLEVEL=error
       NODE_VERBOSE=false
       NODE_ENV=production
       NODE_MODULES_CACHE=true
       
-----> Installing binaries
       engines.node (package.json):  unspecified
       engines.npm (package.json):   unspecified (use default)
       
       Resolving node version 14.x...
       Downloading and installing node 14.17.6...
       Using default npm version: 6.14.15
       
-----> Restoring cache
       - node_modules
       
-----> Installing dependencies
       Installing node modules (package.json)
       audited 9 packages in 0.33s
       found 4 vulnerabilities (3 low, 1 high)
         run `npm audit fix` to fix them, or `npm audit` for details
       
-----> Build
       
-----> Caching build
       - node_modules
       
-----> Pruning devDependencies
       audited 9 packages in 0.346s
       found 4 vulnerabilities (3 low, 1 high)
         run `npm audit fix` to fix them, or `npm audit` for details
       
-----> Build succeeded!
-----> Discovering process types
       Procfile declares types -> web
-----> Compressing...
       Done: 84.7M
-----> Launching...
       Released v7
       https://battleship-project3.herokuapp.com/ deployed to Heroku

<a name="credits"></a>
## Credits

### Content

- I based this project off of a YouTube tutorial (https://www.youtube.com/watch?v=7Ki_2gr0rsE) but then expanded on it to fit the brief criteria.
- I relied on my course notes and Stack Overflow when I ran into problems as well.

  ### Acknowledgments

- Thanks to my mentor, Maranatha Ilesanmi.
- Thanks to the team at Code Institute.