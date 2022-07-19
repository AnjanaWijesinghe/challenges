'''Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.'''

def generate_brackets(n, opens, closes, data, dataset):
    if opens == closes == n:
        #print(data)
        dataset.append(data)
        return
    if opens < n:
        generate_brackets(n, opens + 1, closes, data + '(', dataset)
    if opens > closes:
        generate_brackets(n, opens, closes + 1, data + ')', dataset)
    

amount = 3
dataset = []
generate_brackets(amount, 0, 0, '', dataset)

print(dataset)
