from Board import *


p=Board(10)

p.to_lines()

player=True
end=False

while end!=True :
    if player==True :
        print('Joueur 1 - Pions Blancs :')
    else :
        print('Joueur 2 - Pions Noirs :')

    p.possible_move(player)

    #p.move_piece()




    end=True






# TEST !