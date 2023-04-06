ALGORITHM Task1_Checkpoint 
VAR
    set1 : ARRAY_OF INTEGER[4];
    set2 : ARRAY_OF INTEGER[5];
    i,j: INTEGER;
    sum : INTEGER :=0;
BEGIN
    //Reading the two sets
    FOR i FROM 0 TO 3 STEP 1  DO // insert from user
        read (set1[i])
    END_FOR
    FOR j FROM 0 TO 4 STEP 1  DO // insert from user
        read (set1[j])
    END_FOR

   //comparing all the numbers in both sets, finding the distinct ones and adding them to the sum
FOR i FROM 0 TO 3 STEP 1  DO // insert from user
     FOR j FROM 0 TO 4 STEP 1  DO
        WHILE (set2[j]<>set1[i]) DO
            sum:=sum+set2[j];
        END_WHILE
     END_FOR
    END_FOR
    // Printing the sum of the disctinct elemenets betwenn both sets
write(sum)
END
