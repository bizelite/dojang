def shortest(lst):
    for pair in zip(lst, lst[1:]):
        dist_list = []
        dist_list.append(pair[1] - pair[0])
    return dist_list
        



    
    


        

if __name__ == '__main__':
    s = [1, 3, 4, 8, 13, 17, 20]
    print(shortest(s))
