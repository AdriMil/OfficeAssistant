# All_data_in_tableau = [[1, 'ADRIEN MILLOT.png', 'C:/Users/Adrie/Pictures/ADRIEN MILLOT.png'], [2, 'Retouche.png', 'C:/Users/Adrie/Pictures/Retouche.png'], [3, 'Screenshot_2017-07-23-20-05-02.png', 'C:/Users/Adrie/Pictures/Screenshot_2017-07-23-20-05-02.png']]
# print(All_data_in_tableau)

def ChangePlaceUp(All_data_in_tableau,index):
    if(index!=0):
        Sauvegarde_temporaire_element = All_data_in_tableau[index-1]
        All_data_in_tableau[index-1] = All_data_in_tableau[index-2]
        All_data_in_tableau[index-2] = Sauvegarde_temporaire_element

        Sauvegarde_Numero_temporaire = All_data_in_tableau[index-1][0]
        All_data_in_tableau[index-1][0] = All_data_in_tableau[index-2][0]
        All_data_in_tableau[index-2][0] = Sauvegarde_Numero_temporaire

def ChangePlaceDown(All_data_in_tableau,index):
    if(index!=len(All_data_in_tableau)):
        Sauvegarde_temporaire_element = All_data_in_tableau[index-1]
        All_data_in_tableau[index-1] = All_data_in_tableau[index]
        All_data_in_tableau[index] = Sauvegarde_temporaire_element

        Sauvegarde_Numero_temporaire = All_data_in_tableau[index-1][0]
        All_data_in_tableau[index-1][0] = All_data_in_tableau[index][0]
        All_data_in_tableau[index][0] = Sauvegarde_Numero_temporaire

def DeleteSelectedLine(All_data_in_tableau, index):
    All_data_in_tableau.pop(index)
    print(All_data_in_tableau)
    for i in range(0,len(All_data_in_tableau)):
        All_data_in_tableau[i][0] = i + 1

