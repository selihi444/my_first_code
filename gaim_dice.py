 ###### specifier nombers of players ! #########
while True:
    num_of_players = int(input("entrer le nombere des players (entre 2 er 4) : "))
    if num_of_players!= 2 or num_of_players!= 4 or num_of_players!= 1:
        break
########## inisialisation des scores of players ###########
score_players={}
for i in range(num_of_players):
    name_of_player=str(input("entrer votre nome: "))
    score_players[name_of_player]=0

# ###### game loop ##########
import random as r
cond=True

while cond:
    for key,v in score_players.items():
        print("for :",key,"> ")
        input(" press yes or enter to start! : ")
        random_nb=r.randint(1,6)
        print("vous avez ",random_nb, " points")
        t9mira_yes_no=input("pour garder les points press < yes > et pour continuer press < no >")
        if t9mira_yes_no=="yes":
            score_players[key]+=random_nb
            if score_players[key]>7:
                cond=False
                break
        else:
            while t9mira_yes_no=="no":
                t9mira=int(input("appelex un numero!! : "))
                random_nb=r.randint(1,6)
                print("le numero est :",random_nb)
                if t9mira==random_nb:
                    score_players[key]+=random_nb
                    if score_players[key]>7:
                        cond=False
                        break
                    t9mira_yes_no=input("pour garder les points press < yes > et pour continuer press < no >")
                    
                else:
                    score_players[key]=0
                    break
   
                   
for k,v in score_players.items():
        if v>7:
            print(k,"winnnnnnnnnnnnner")
            break
        