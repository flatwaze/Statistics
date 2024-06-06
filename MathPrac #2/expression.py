def roc_auc(probabilities, y_true):
    n = len(probabilities)
    tmp = 0
    ans = 0
    sub = 0

    for i in range(n):
        for j in range(n):
            tmp = 0
            if y_true[i] < y_true[j]:
                tmp += 1
                sub += 1
                
            if probabilities[i] == probabilities[j]:
                tmp *= 0.5
            elif probabilities[i] < probabilities[j]:
                tmp *= 1
            else:
                tmp = 0
            
            ans += tmp
    
    return ans/sub