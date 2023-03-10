def sum():
    def local():
        sample="local sample"
    def non_local():
        nonlocal sample
        sample="nonlocal"
    def a_global():
        global sample
        sample="global"
    sample="default"
    local()
    non_local()
    a_global()
    print(sample)
sum()
print(sample)

