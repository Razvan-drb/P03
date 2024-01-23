# 204-01-22 - Code Review

## Updated
- fix / restructure test policy 
- fix/update Tournament class

## Todo 
- specify librairies versions in requirements.txt
- update README.md : 
    - add a section "About"
    - add a section "Install"
- read about tests and uderstand WHY, WHAT, HOW we want to use the code
- fix class Tournamanent 
- fix tournament. get_curent_round, update_current_round, update
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
- 
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
    

