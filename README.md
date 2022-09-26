# General Knowledge Quiz

Welcome to the readme file of my project.

## Introduction

This programme is designed to test the user's luck. Annoying Battleship is programmed to test the user's patience as well as their luck for the day.

You can find a link to my website [here]()

# Table of Contents
[1.User Experience(UX)](#1-user-experience)
- 1.1 User Goals
- 1.2 User Expectations
- 1.3 Visual Images
- 1.4 Brainstorm

[2.Features](#2-features)
- 2.1 Four Grid Sizes
- 2.2 Questions answered with only 1
- 2.3 Questions answered with 1 and 0
- 2.4 Questions answered with 1, 2, 3 and 4
- 2.5 Co-ordinate entry
- 2.6 Letter change
- 2.7 Bullet change

[3.Technology](#3-technology)

[4.Testing](#4-testing)

[5.Bugs](#5-bugs)

[6.Deployment](#6-deployment)

[7.Project Completion](#7-project-completion)

[8.Improvements](#8-improvements)

[9.Acknowledgements](#9-acknowledgements)

# 1. User Experience

## 1.1 User Goals

[Return to the Table of Contents](#table-of-contents)

My goal in creating this programme is to allow users to check their luck for the day. Will they be able to sink all their opponents' ship using bullets that wouldn't cover the whole grid? Will they lose to the computer? Or will they be so frustratingly close that the idea would bother them for the whole day? Try the game and find out.

## 1.2 User Expectations

[Return to the Table of Contents](#table-of-contents)

The following are expected of the website:

* Should be easily accessible.
* The language should be in simple English.
* The instructions of how to continue should be set out clearly.
* Information on how to play should be clearly set out for first-time players.
* For returning players, an option to skip the instructions for the game has to be available.
* Ships should be generated at different areas in different games.
* At the end of the game, an option should be available to the user to start the game again.

## 1.3 Visual Images

[Return to the Table of Contents](#table-of-contents)

The grid in which the player and computer plays is shown in the image below.

![Grid with letters](/assets/screenshots/x-s-e--.png)

The horizontal lines represent a co-ordinate on the grid and it would change to S, E, or X depending on the situation.

## 1.4 Brainstorm

[Return to the Table of Contents](#table-of-contents)

This is the flowchart that shows how the game goes initially.

![Flowchart](/assets/screenshots/Flowchart.png)

The only changes that I made to the initial flowchart is the number of grid sizes and the final question. The final question in this programme actually brings the user back to the very first question, not the difficulty level.

# 2. Features

[Return to the Table of Contents](#table-of-contents)

## 2.1 Four Grid Sizes

There are four sizes altogether in which the player can choose from. 
There is the 5 x 5 grid:

There is the 6 x 6 grid:

There is the 7 x 7 grid:

There is the 8 x 8 grid:

## 2.2 Questions answered with only 1

This question can only be answered with 1:

## 2.3 Questions answered with 1 and 0

This question can only be answered with 1 or 0:

## 2.4 Questions answered with 1, 2, 3 and 4

This question can be answered with 1, 2, 3 or 4 but nothing else:

## 2.5 Co-ordinate entry

The programme would first ask for the horizontal co-ordinate:

Then it would ask for the vertical co-ordinate:

Then it would display the co-ordinate with both the horizontal and vertical side-by-side:

## 2.6 Letter change

Initially, the location of the ships on the player's board is represented with S and everything else is represented as '-':

The '-' would change to X if the user or computer guesses wrong.
Before:

After:

The S would change to E if the computer guesses correctly.
Before:

After:

The '-'  would change to E if the player guesses correctly.
Before:

After:

## 2.7 Bullet change

The number of bullets would decrease with every valid aim the player makes:


# 3. Technology

[Return to the Table of Contents](#table-of-contents)

* [MD](https://en.wikipedia.org/wiki/Markdown) (Markdown) was used to create this readme file.

* [Gitpod](https://www.gitpod.io/) was used for the code input and edit for this project.

* [Github](https://github.com/) was used to store my repository and code when it is not in use.

* [Slack](https://slack.com/intl/en-ie/) was used for communications when I was having trouble creating code.

* [Pep8 Validator](http://pep8online.com/) was used to check for bugs in my code.

* [LucidChart](https://www.lucidchart.com/pages/landing?utm_source=google&utm_medium=cpc&utm_campaign=_chart_en_tier1_mixed_search_brand_exact_&km_CPC_CampaignId=1490375427&km_CPC_AdGroupID=55688909257&km_CPC_Keyword=lucid%20chart&km_CPC_MatchType=e&km_CPC_ExtensionID=&km_CPC_Network=g&km_CPC_AdPosition=&km_CPC_Creative=442433236001&km_CPC_TargetID=kwd-55720648523&km_CPC_Country=1007850&km_CPC_Device=c&km_CPC_placement=&km_CPC_target=&gclid=CjwKCAjwm8WZBhBUEiwA178UnIKD1nNXqMld8VwU2N7Uh-eMW5N9fjfiwSQNyh_CJa7_GYS7DTp-uhoCWDoQAvD_BwE) was used to create my flowchart.

* [Heroku](https://id.heroku.com/login) was used to deploy my project.

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) was used to create the programme.

# 4. Testing

[Return to the Table of Contents](#table-of-contents)

The contents of the testing section can be find [here](testing.md).

# 5. Bugs

[Return to the Table of Contents](#table-of-contents)

![Initial Bug](/assets/screenshots/Initial-bug-1.png)
![Initial Bug 2](/assets/screenshots/Initial-bug-2.png)
![Initial Bug 3](/assets/screenshots/Initial-bug-3.png)

These are the initial bugs that popped up when I passed my code through the validator. I understood that the red ones meant that the code was a major problem and the orange ones are less severe.

I got rid of the red ones by adjusting my code. I added a white space after commas and operators. I changed the length of my code to accommodate the preferences of python. This was done by either placing my code on separate lines or by shortening the name of my variables and I indented my code so that it does not start at the same place as the next logical operation.

![Second Bug](/assets/screenshots/Bug-solving.png)

This is what the validator showed me after a modified my code for the first time. In order to get rid of the orange set of problems, I deleted the white spaces that were located on blank lines. Another problem were the trailing white spaces behind my code. I got rid of them as well. I also added a new line after my final line to satisfy the final error. This ahowed up after the next validation.

![Resolved Bugs](/assets/screenshots/Bug-finished.png)

# 6. Deployment

[Return to the Table of Contents](#table-of-contents)

The site was deployed to Heroku using the following steps:

- If necessary, the packages that were added to the file on this project were placed in the requirements.txt file.
- Before deploying the project, a heroku account had to be made.
- First, heroku will ask for the user's basic information.
- This includes their first and last name, their email address, their role and the primary development language.
- A statement would then pop up asking for the user to accept their terms and conditions.
- The account has been created.
- On the heroku dashboard, the create new app button is clicked.
- A name which hasn't been used before has to be given to the app.
- Choose a region, which is Europe in my case.
- Complete the settings tab first.
- Press the button that says settings on the navigation bar.
- If the user has any sensitive or personal data, it should be placed in the Config Vars section.
- Press the reveal config vars button.
- Add in the name of the file that should be placed in capital letters in the first blank space.
- Add in the actual code in the file named above into the second blank space.
- Press add.
- Then press the buildpack button below.
- Select python from the selection given to you and press save changes.
- Press buildpack again and this time select nodejs and save changes.
- Make sure the python is on top of the nodejs.
- After this, press the deploy button on the navigation bar.
- Select Github from the three options give.
- Press connect to Github.
- Type in the name of the Github account the user is working with.
- Type in the name of the repository.
- Click Search.
- Click connect which would connect the github code to the heroku app.
- Make sure the branch is the main branch.
- Press deploy branch.
- If you want heroku to automatically build your code after pushing it to github each time, press enable automatic deploy.
- Your pogramme has now been deployed.
- Press view to view your programme.

# 7. Project Completion

[Return to the Table of Contents](#table-of-contents)

This is the complete version of my programme.


# 8. Improvements

[Return to the Table of Contents](#table-of-contents)

* Color could be added to the letterings depending on whether the answer is correct or incorrect.
* The length of the ship should change to make the game more dependent on strategy rather than luck.
* The programme should clear itself to allow the user to always see the grid.

# 9. Acknowledgements

[Return to the Table of Contents](#table-of-contents)

* Credits is given to [iKelvv](https://github.com/iKelvvv/MS3) for given me some code to be used in the programme. This is the code that was implemented into my programme in which I modified.
    - for x in range(7):
    """
    Generates the size of the playing board
    """
    board.append(["-"] * 7)
    cpu_board.append(["_"] * 7) 
    - def location_col(board):
        """
        Generate a random column for the computer's ship
        """
        return randint(0, len(board) - 1)


    - def location_row(board):
        """
        Generate a random row for the computer's ship
        """
        return randint(0, len(board) - 1)


    - def cpu_location_col(cpu_board):
        """
        Generate a random row for the player's ship
        """
        return randint(0, len(cpu_board) - 1)


    - def cpu_location_row(cpu_board):
        """
        Generate a random column for the player's ship
        """
        return randint(0, len(cpu_board) - 1)
* Credits is given to the LoveSandwich walkthrough tutorial for the validation section of my programme.
    - def validate_data(values):

        try: 
            [int(value) for value in values]
            if len(values) != 6:
                raise ValueError(
                    f"Exactly 6 values required, you provided {len(values)}"
                )
            
        except ValueError as e:
            print(f"Invalid Data: {e}, please try again\n")
            return False

        return True
* For the Readme file, I took the structure from my previous Readme file and used it here. Reference is given to https://github.com/dhakal79/Portfolio-project-MS1 which is the readme file I took into consideration when I was doing my first one.
* The ideas and code I implemented into this project were taught to me by Code Institute.
* My mentor Marcel Mulders supported me throughout the whole project. I couldn't have done it without his help.