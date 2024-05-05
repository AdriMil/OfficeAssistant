def ChangePlaceUp(All_Data_In_Table,index):
    if(index!=0):
        Store_Value_Temporary = All_Data_In_Table[index-1]
        All_Data_In_Table[index-1] = All_Data_In_Table[index-2]
        All_Data_In_Table[index-2] = Store_Value_Temporary

        Store_Number_Temporary = All_Data_In_Table[index-1][0]
        All_Data_In_Table[index-1][0] = All_Data_In_Table[index-2][0]
        All_Data_In_Table[index-2][0] = Store_Number_Temporary

def ChangePlaceDown(All_Data_In_Table,index):
    if(index!=len(All_Data_In_Table)):
        Store_Value_Temporary = All_Data_In_Table[index-1]
        All_Data_In_Table[index-1] = All_Data_In_Table[index]
        All_Data_In_Table[index] = Store_Value_Temporary

        Store_Number_Temporary = All_Data_In_Table[index-1][0]
        All_Data_In_Table[index-1][0] = All_Data_In_Table[index][0]
        All_Data_In_Table[index][0] = Store_Number_Temporary

def DeleteSelectedLine(All_Data_In_Table, index):
    All_Data_In_Table.pop(index)
    print(All_Data_In_Table)
    for i in range(0,len(All_Data_In_Table)):
        All_Data_In_Table[i][0] = i + 1

