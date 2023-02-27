

def safety_condition(c, v, E):
    for w, z in E:
        if (w in c and z in c) and (w != v and z != v):
            return False
    return True




def divide_nodes(V, m, E):
    V.sort()
    classes = []

    for v in V:
        flag = True
        for c in classes:
            if safety_condition(c, v, E) and len(c) < m:
                c.append(v)
                flag = False
                break
        if flag:
            new_class = [v]
            classes.append(new_class)

    return classes