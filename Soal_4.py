def swap(a,b):
    return (b,a)

def sort_array(data):
    #sort multi-array data dengan insertion sort yang dimodifikasi
    n=len(data)
    for i in range(n):
        for j in range (i):
            if len(data[i])<len(data[j]):
                (data[i],data[j])=swap(data[i],data[j])
            elif len(data[i])==len(data[j]):
                for k in range(len(data[i])):
                    if ord(data[i][k])<ord(data[j][k]):
                        (data[i],data[j])=swap(data[i],data[j])
    return data
