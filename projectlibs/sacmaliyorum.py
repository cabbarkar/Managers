s=[[1,2,3],[3,4,5],[4,5,6]]

# recursive

def func(a):
    for i in a:
        print(i)
        func(i)
        
func[a]