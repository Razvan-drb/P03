
# 2024-03-22 - 10h00 - Code Review

## Updated 
- Add conftest
- Add new 4 players 
- rename fixture
- change curent round number at 0 when status change to in progress

# 2024-03-15 - 17h00 - Code Review


## Problem
- When i try to update the current round, the round is not updated in the tournament (in database )

- Example usage 
    - Supose we have a tournament with 3 rounds, 4 players, curent_id_round = 0
    - Suppose we have defaults score results at -1
    - Supose we have a new_res to push
    - t.update_current_round(new_res) => no update in the tournament DATABASE

    -  the proble is here : ```t.update_current_round(new_res)```   

## Todo
- Fix this 
- Start Front app / views and Controlers 
- Write print  functions to display the  menu / option how to read user input to store values for players in a dict




# 2024-03-15 - 09h00 - Code Review

## Todo
- Tackle update  tournament problem => we want score OK 1/0 not -1 -1 in the rounds.json !!!! Check
- What about computing results by player ???? get score Check
- write proto AND OR code about thi feature

## Updated
- MAJ classe Tournament with search pb
- Added code test for all 3 rounds all matches 
- Added test update tournament 
- clean code 

# 2024-03-08 - Code Review

## Todo
- [x] continue debug class Player to pass tests and run entire Tournament from creation to end

## Updated
- [x] Fix files errors 
- [x] Reset DB
- [x] Debug tets and Models

# 2024-03-01 - Code Review

## Todo

## Updated

# 2024-02-01 - Code Review

## Todo
- 

## Updated
- addded search to tournament
- moove attributes and methods of tournament to be more consistent with the other classes
- fix get current round and update curent round
- fix _add_round() in tournament => .create()
- upadate requirements.txt = > pycln isort black mypy and other staict code checkers

# 2024-01-22 - Code Review

## Updated
- fix / restructure test policy 
- fix/update Tournament class
- test_players PASSES
- test_tournaments PASSES

## Todo 
- specify librairies versions in requirements.txt - done
- update README.md : - done
    - add a section "About"
    - add a section "Install"
- read about tests and understand WHY, WHAT, HOW we want to use the code
- fix class Tournament 
- fix tournament. get_current_round,-(j'ai essayé une version) 
- update_current_round - (j'ai essayé)
- update 
- fix the Round class


# 2024-01-12 - Mentoring
## Validated
- 

## Updated
- Add pytest to utils
- Update test for tournaments 
- Update methods in tournament 
- Test policy 
- get_current_round_number
- next_round
- update_status
- added search, search_by, create, update to all 3 classes
## Todo

### MUST HAVE
- calculer les scores des jouers
- sortir le classement 
- maj la round en cours et passer a la round suivante
- update trounament must work 
- finish change status 
- validate round creattion when strat a tournament 
- add fucntionality to update each round for the tournament + method update_round

### NICE TO HAVE
- class testPlayer
- add verification that the player is not already in the tournament
- add verification that the player is not already in the Player DB Table
- Add verification that the player is not already in the Player DB Table
------------------------------------------------------------------------------------------------
get_current_round_id:
    self.list_id_round
    Round.search id recuperer la round
    return la round
    pouvoir consulter la round en cours 
update_current_round:
    modifier la round
    get la round. round.match list == new match list
    round.update
PYTEST COMMAND 
pytest -vvx --capture=tee-sys --log-cli-level=INFO tests/models

