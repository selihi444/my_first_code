num_line=int(input("entrer le numero des lines de votre piramid : "))
## number of lines #####
def the_pyramid(num_line):
    start=1 # start
    for i in range(num_line):
        print(" "*num_line+"#"*start)
        num_line-=1
        start+=2

(the_pyramid(num_line))