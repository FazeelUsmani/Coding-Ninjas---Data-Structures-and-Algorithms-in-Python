from itertools import combinations,permutations
import pandas as pd

sudoku_matrix_list = [[9, 0, 0, 0, 2, 0, 7, 5, 0],
                      [6, 0, 0, 0, 5, 0, 0, 4, 0],
                      [0, 2, 0, 4, 0, 0, 0, 1, 0],
                      [2, 0, 8, 0, 0, 0, 0, 0, 0],
                      [0, 7, 0, 5, 0, 9, 0, 6, 0],
                      [0, 0, 0, 0, 0, 0, 4, 0, 1],
                      [0, 1, 0, 0, 0, 5, 0, 8, 0],
                      [0, 9, 0, 0, 7, 0, 0, 0, 4],
                      [0, 8, 2, 0, 4, 0, 0, 0, 6] ]

sudoku_matrix = pd.DataFrame(data=sudoku_matrix_list, columns=["c" + str(i) for i in range(1,10,1)], 
                             index=["r" + str(i) for i in range(1,10,1)] )


def sanity_check(sudoku_matrix): 
    # we do not check success in this fuction. 
    flag= True # sudoku matrix is healthy if flag is True. 
    # check duplicity of integers in regions:
    ################ 
    # 1) col regions
    for g in ["c" + str(i) for i in range(1,10,1)]:
        _ = sudoku_matrix.loc[:,g].value_counts()
        _ = _.drop(0) if 0 in _.index else _
        if (_.values != 1).sum() != 0:
            flag = False
            #print("there is inconsistency in " + str(g))
            return flag
    ################ 
    #2) row regions
    for g in ["r" + str(i) for i in range(1,10,1)]:
        _ = sudoku_matrix.loc[g,:].value_counts() 
        _ = _.drop(0) if 0 in _.index else _
        if (_.values != 1).sum() != 0:
            flag = False
            #print("there is inconsistency in " + str(g))
            return flag

    ################          
    # 3) box regions
    _ = sudoku_matrix.loc["r1":"r3","c1":"c3"].stack().value_counts()
    _ = _.drop(0) if 0 in _.index else _
    if (_.values != 1).sum() != 0:
        flag = False
        #print("there is inconsistency in r1:r3,c0:c3 ")
        return flag
        
    _ = sudoku_matrix.loc["r1":"r3","c4":"c6"].stack().value_counts()
    _ = _.drop(0) if 0 in _.index else _    
    if (_.values != 1).sum() != 0:
        flag = False
        #print("there is inconsistency in r1:r3,c4:c6 ")
        return flag
            
    _ = sudoku_matrix.loc["r1":"r3","c7":"c9"].stack().value_counts()
    _ = _.drop(0) if 0 in _.index else _
    if (_.values != 1).sum() != 0:
        flag = False
        #print("there is inconsistency in r1:r3,c7:c9 ")  
        return flag
        
    ######      
    _ = sudoku_matrix.loc["r4":"r6","c1":"c3"].stack().value_counts()
    _ = _.drop(0) if 0 in _.index else _
    if (_.values != 1).sum() != 0:
        flag = False
        #print("there is inconsistency in r4:r6,c0:c3 ")
        return flag
        
    _ = sudoku_matrix.loc["r4":"r6","c4":"c6"].stack().value_counts()
    _ = _.drop(0) if 0 in _.index else _
    if (_.values != 1).sum() != 0:
        flag = False
        #print("there is inconsistency in r4:r6,c4:c6 ")
        return flag
            
    _ = sudoku_matrix.loc["r4":"r6","c7":"c9"].stack().value_counts()
    _ = _.drop(0) if 0 in _.index else _
    if (_.values != 1).sum() != 0:
        flag = False
        #print("there is inconsistency in r4:r6,c7:c9 ") 
        return flag
    
   ######       
    _ = sudoku_matrix.loc["r7":"r9","c1":"c3"].stack().value_counts()
    _ = _.drop(0) if 0 in _.index else _
    if (_.values != 1).sum() != 0:
        flag = False
        #print("there is inconsistency in r7:r9,c0:c3 ")
        return flag
        
    _ = sudoku_matrix.loc["r7":"r9","c4":"c6"].stack().value_counts()
    _ = _.drop(0) if 0 in _.index else _
    if (_.values != 1).sum() != 0:
        flag = False
        #print("there is inconsistency in r7:r9,c4:c6 ")
        return flag
            
    _ = sudoku_matrix.loc["r7":"r9","c7":"c9"].stack().value_counts()
    _ = _.drop(0) if 0 in _.index else _
    if (_.values != 1).sum() != 0:
        flag = False
        #print("there is inconsistency in r7:r9,c7:c9 ") 
        return flag
    ######      
    return flag



def is_solved(sudoku_matrix):
    if sanity_check(sudoku_matrix):
        sudoku_matrix_stacked  = sudoku_matrix.stack()
        movement_places        = sudoku_matrix_stacked[sudoku_matrix_stacked == 0].index.to_list()
        if len(movement_places) == 0:
            return True
        else:
            return False
    else:
        return False    


def scan_the_matrix(sudoku_matrix):
    # we do not check success in this fuction. but if the sudoke is solved, the listt will be empty
    unsolvable_flag        = False
    sudoku_matrix_stacked  = sudoku_matrix.stack()
    movement_places        = sudoku_matrix_stacked[sudoku_matrix_stacked == 0].index.to_list()
    
    possiblities=[0,1,2,3,4,5,6,7,8,9]
    listt = []
    for i in movement_places: # is index of locations. 
        flags = {1:True,2:True,3:True,4:True,5:True,6:True,7:True,8:True,9:True}
        for j in possiblities:
            sudoku_matrix_stacked_    = sudoku_matrix_stacked.copy()
            sudoku_matrix_stacked_[i] = j
            sanity_status = sanity_check(sudoku_matrix_stacked_.unstack())
            if sanity_status == False:
                flags[j] = False

        flags_                   = pd.Series(data=flags)
        value_counts_of_flags_df = flags_.value_counts()
        #print(value_counts_of_flags_df)
        if True in value_counts_of_flags_df:
            possible_numbers_count = value_counts_of_flags_df[True]
        else:
            possible_numbers_count = 0
            unsolvable_flag  = True 
        
        listt.append([i, flags, possible_numbers_count])

        #if flags_.value_counts()[True] == 1:
        #    print("found")
    return listt, unsolvable_flag





def play_the_matrix_one_step( sudoku_matrix, listt):  # base case
    # sudoku_matrix is dataframe. so it is passed by reference. we do not need to return it. the changes we do in this function will remain outside the function.
    # list is a data structure which carries infos about the state of sudoku_matrix
    there_is_single_possible_number_for_at_least_one_location = False
    #sudoku_matrix_stacked        = sudoku_matrix.stack()
    
    for i in listt:  
        # exapmle listt: [[('r3', 'c1'), {1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: True, 9: False}, 1],[('r3', 'c3'), {1: False, 2: False, 3: False, 4: False, 5: True, 6: False, 7: True, 8: True, 9: False}, 3], ... ]      
        if i[2] == 1: 
            # we put the number to the location in the matrix. we are sure it is correct number. 
            there_is_single_possible_number_for_at_least_one_location = True
            location  = i[0]
            possibility_dict = i[1]
            for z in possibility_dict:
                if possibility_dict[z] == True:
                    number = z
            row=location[0]
            col=location[1]
            sudoku_matrix.loc[row,col]     = number    
            #sudoku_matrix_stacked[location] = number
            #print("i change the "+str(location))
    
    #sudoku_matrix = sudoku_matrix_stacked.unstack()
    # if there is not number to put for sure, we return False and we do not change the sudoku_matrix
    return there_is_single_possible_number_for_at_least_one_location






def play_the_matrix(sudoku_matrix):
    if is_solved(sudoku_matrix):
        return True
    if not sanity_check(sudoku_matrix):
        return False

    listt, unsolvable_flag = scan_the_matrix(sudoku_matrix)
    
    if unsolvable_flag:
        return False
    

    #there_is_single_possible_number_for_at_least_one_location = play_the_matrix_one_step(sudoku_matrix, listt)

    if play_the_matrix_one_step(sudoku_matrix, listt):
        #print(sudoku_matrix)
        return play_the_matrix(sudoku_matrix)
    else:
        print("there is no definite movement. we have to try now.")
        # we will traver the all possible numbers and try to reduce one possiblity at least in one location. if we cant then the sudoku is unsolvable with given information. there is not enough number in the sudoku.
        sudoku_matrix_2 = sudoku_matrix.copy()
        sudoku_matrix_stacked_2               = sudoku_matrix_2.stack()
        listt_2 = listt
        for enum,i in enumerate(listt_2):  
        # exapmle listt: [[('r3', 'c1'), {1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: True, 9: False}, 1],[('r3', 'c3'), {1: False, 2: False, 3: False, 4: False, 5: True, 6: False, 7: True, 8: True, 9: False}, 3], ... ]      
            """if i[2] == 2: 
                # we know that  i[2] == 1 and i[2] == 0 is not exist in this state. so we start the smallest possible number counts. we will look at the locations which has only two possible numbers."""

            location         = i[0]
            possibility_dict = i[1]
            possibility_dict_new=i[1]
            for z in possibility_dict:
                if possibility_dict[z] == True:
                    number = z
                    sudoku_matrix_stacked_2[location] = number
                    sudoku_matrix_2 = sudoku_matrix_stacked_2.unstack()
                    if play_the_matrix(sudoku_matrix_2):
                        sudoku_matrix = sudoku_matrix_2
                        return True    
                    else:
                        print("i am innn")
                        possibility_dict_new[z] = False
                    listt[enum][1] = possibility_dict_new

        # we update the listt. if we cannot solve the sudoku now, the given info is not enough to solve sudoku.
        if play_the_matrix_one_step(sudoku_matrix, listt):
            return play_the_matrix(sudoku_matrix)
        else:
            return False


      


print(sudoku_matrix)
print( play_the_matrix(sudoku_matrix) ) 

print(sudoku_matrix)
      

