# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 21:42:00 2021

@author: user
"""
import sys
import numpy as np
import math


def read(userReadTime, allUsersReadMean):
    score = 0
    if userReadTime >= allUsersReadMean:
        score = 7
    else:
        score = 7/allUsersReadMean*userReadTime
    
    return score



def duration(userDuration, allUsersDurationMean):
    score = 0
    if userDuration>= allUsersDurationMean:
        score = 7
    else:
        score = 7/math.log(allUsersDurationMean)*math.log(userDuration)
    
    return score


def save(ifSave):
    if ifSave:
        score = 7
    else:
        score = 0
    return score


def share(userShareTime, allUsersShareMean):
    score = 0
    if allUsersShareMean >0:
        if userShareTime>= allUsersShareMean:
            score = 8
        elif userShareTime >0:
            score = 7 + userShareTime/allUsersShareMean
    else:
        if userShareTime> allUsersShareMean:
            score = 8
    return score



def comment(userCommentTime, allUsersCommentMean):
    score = 0
    if allUsersCommentMean >0:
        if userCommentTime>= allUsersCommentMean:
            score = 8
        elif userCommentTime >0:
            score = 7 + userCommentTime/allUsersCommentMean
    else:
        if userCommentTime> allUsersCommentMean:
            score = 8
    return score



def userArticleScore(userArray):
    ifRead = userArray[0]
    
    if ifRead == True:
        userReadTime = userArray[1]
        userDuration = userArray[2]
        ifSave = userArray[3]
        userShareTime = userArray[4]
        userCommentTime = userArray[5]
        
        allUsersReadMean = userArray[6]
        allUsersDurationMean = userArray[7]
        allUsersShareMean = userArray[8]
        allUsersCommentMean = userArray[9]
    

        scoreArray = []
        scoreArray.append(read(userReadTime, allUsersReadMean))
        scoreArray.append(duration(userDuration ,allUsersDurationMean))
        if userShareTime > 0:
            scoreArray.append(share(userShareTime,allUsersShareMean))
        if userCommentTime > 0:
            scoreArray.append(comment(userCommentTime ,allUsersCommentMean))
        if ifSave:
            scoreArray.append(7)

        print(scoreArray)
        print(np.mean(scoreArray))
        
        if np.mean(scoreArray) >7:
            return 7
        else:
            return np.mean(scoreArray)
        
        
def main(argv):
    userArray = []
    for i in range(1,len(argv)):
        if argv[i].lower() =='true' :
            userArray.append(True)
        elif argv[i].lower() =='false':
            userArray.append(False)
        else:
            userArray.append(float(argv[i]))
            
    print("userArray: ", userArray)
    
    score = round(userArticleScore(userArray),2)
    print("score: ", score)
    return score


if __name__ == '__main__':
    main(sys.argv)