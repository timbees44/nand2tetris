def or8way(in_arr):
    a = in_arr[0] | in_arr[1]
    b = in_arr[2] | in_arr[3]
    c = in_arr[4] | in_arr[5]
    d = in_arr[6] | in_arr[7]
    
    e = a | b 
    f = c | d 

    out = e | f 

    return out

in_arr = [0, 1, 1, 0, 0, 0, 1, 0]

output = or8way(in_arr)
print(output)
