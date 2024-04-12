import sys

def tokenize(TextFilePath) -> list:
    '''
    Runtime: O(n)
    O(n) to read each char 
    O(n) to change each char to lowercase

    '''
    tokens = list()
    try:
        with open(TextFilePath, 'r') as f:
            text = f.read()
            current = ''
            for c in text: 
                if (33 <= ord(c) <= 126):
                    current += c.lower()
                else:
                    if current:
                        tokens.append(current)
                        current = ''
            if current:
                tokens.append(current)
    except Exception as e:
        print(f"Error opening file from {TextFilePath}: {str(e)}")
    
    return tokens

def computeWordFrequencies(tokenList) -> dict:
    '''
    Runtime: O(n), iterates over n tokens
    '''
    freq = {}

    for token in tokenList:
        if token in freq:
            freq[token] += 1
        else:
            freq[token] = 1
    
    return freq
    

def printFrequencies(wordCount):
    '''
    Runtime: O(nlogn)
    O(n) to iterate through the tokens and print
    O(nlogn) to sort the dictionary
    '''
    sort_freq = sorted(wordCount.items(), key=lambda x: (-x[1], x[0]), reverse=False)
    for token, freq in sort_freq:
        print(f"{token} -> {freq}")

if __name__ == "__main__":
    file_path = sys.argv[1]
    tkns = tokenize(file_path)
    #print(tkns)
    tkn_dict = computeWordFrequencies(tkns)
    #print(tkn_dict)
    printFrequencies(tkn_dict)

        
