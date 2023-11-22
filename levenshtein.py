!sudo apt update
!sudo apt install enchant --fix-missing
!sudo apt install -qq enchant
!pip install pyenchant

import enchant

#enchant

def levenshteinDistance(A, B):
    # In-built function for calculating Levenshtein distance
    return enchant.utils.levenshtein(A, B)

if __name__ == '__main__':
    A = ["helo", "algorithm", "kitten", "gate"]
    B = ["hello", "rhythm", "sitting", "goat"]
    for i in range(len(A)):
        print("Levenshtein Distance between {} and {} = {}".format(A[i], B[i], levenshteinDistance(A[i], B[i])))


