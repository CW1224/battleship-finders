## 4.1 Manual Testing

### 4.1.1 Question with one answer
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Pressing 1  | Will bring user to the next part of the game | Pass
Pressing a number that is not 1 | Invalid Data shows up and user has to try again| Pass
Press a non-number | Invalid Data shows up and user has to try again | Pass

![Question Passed 1](/assets/screenshots/Correct-answer-firstq.png)

### 4.1.2 Question with two answers

TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Pressing 1 and 0 | Will bring user to the next part of the game | Pass
Pressing a number that is not 1 or 0| Invalid Data shows up and user has to try again| Pass
Press a non-number | Invalid Data shows up and user has to try again | Pass

![Question enter again](/assets/screenshots/invalid-entry-no-num-second.png)

### 4.1.3 Question with four answers

TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Pressing 1, 2, 3 and | Will bring user to the next part of the game | Pass
Pressing a number that is not 1, 2, 3 or 4| Invalid Data shows up and user has to try again| Pass
Press a non-number | Invalid Data shows up and user has to try again | Pass

### 4.1.4 Inserting co-cordinates

TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Pressing co-ordinates within the grid length | The word you entered: _,_ shows up | Pass
Pressing co-ordinates out of the range of the grid length | Data out of range shows up and user has to try again | Pass
Pressing co-ordinates already entered | The comment: you have entered this co-cordinate already shows up, please try again shows up | Pass
Pressing 0 | The comment: 0 is not within the range, please try again shows up | Pass

![Co-ordinate Wrong](/assets/screenshots/coordinate-not-in-range.png)
![Co-ordinate Reenter](/assets/screenshots/coordinate-reentry.png)

### 4.1.5 Different comments at end of game

TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Hitting all opponent's ships | Message with congratulations show up | Pass
Using up all bullets | Too bad message shows up saying no more bullets are left | Pass
Computer sinks all ships | Too bad message shows up saying that the player should get revenge | Pass
### 4.1.6 Starting again

TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Pressing 1 at the last question | Brings user to the beginning of the programme| Pass
Pressing 0 at the last question | Brings up a final message | Pass

![Final Question](/assets/screenshots/paly-again-yes.png)
![Final Question 2](/assets/screenshots/play-again-no.png)

## 4.2 W3C Validator Tools

[Pep8](http://pep8online.com/) was used to validate the code. When the following shows up, this means that the code passes through with no problem.
![Code Successful](/assets/screenshots/Bug-finished.png)

Return to the original readme file, press this [button](README.md).