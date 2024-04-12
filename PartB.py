from PartA import tokenize, computeWordFrequencies
import sys

def countCommonTokens(file1_path, file2_path):
    '''
    Runtime: O(n)
    '''
    tkns1 = computeWordFrequencies(tokenize(file1_path))
    tkns2 = computeWordFrequencies(tokenize(file2_path))

    common_tkns = set(tkns1.keys()) & set(tkns2.keys())
    print(common_tkns)
    return len(common_tkns)

if __name__ == "__main__":
    print(countCommonTokens(sys.argv[1], sys.argv[2]))