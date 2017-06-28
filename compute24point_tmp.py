def print_if_24(n):
    for i in range(0, len(n)):
        for j in range(i+1, len(n)):
            a = n[i]
            b = n[j]
            lost = []
            for t in range(0, len(n)):
                if t!=i and t!=j:
                    lost.append(n[t])
                    
            z1 = a+b
            z2 = a*b
            z3 = a-b
            z4 = b-a
            if b != 0:
                z5 = a/b
            if a != 0:
                z6 = b/a
            
            if len(lost) == 0:
                if -0.001 < z1 - 24 < 0.001:
                    print str(a) + '+' + str(b)
                    return True
                elif -0.001 < z2 - 24 < 0.001:
                    print str(a) + '*' + str(b)
                    return True
                elif -0.001 < z3 - 24 < 0.001:
                    print str(a) + '-' + str(b)
                    return True
                elif -0.001 < z4 - 24 < 0.001:
                    print str(b) + '-' + str(a)
                    return True
                elif b != 0 and -0.001 < z5 - 24 < 0.001:
                    print str(a) + '/' + str(b)
                    return True
                elif a != 0 and -0.001 < z6 - 24 < 0.001:
                    print str(b) + '/' + str(a)
                    return True
                return False
            else:
                lost.append(z1)
                if print_if_24(lost):
                    print lost
                    return True
                lost.pop()
                lost.append(z2)
                if print_if_24(lost):
                    print lost
                    return True
                lost.pop()
                lost.append(z3)
                if print_if_24(lost):
                    print lost
                    return True
                lost.pop()
                lost.append(z4)
                if print_if_24(lost):
                    print lost
                    return True
                lost.pop()
                lost.append(z5)
                if print_if_24(lost):
                    print lost
                    return True
                lost.pop()
                lost.append(z6)
                if print_if_24(lost):
                    print lost
                    return True
                

n = [11.0, 11.0, 2.0, 2.0]
print_if_24(n)
