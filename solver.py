import heapq       # need this for A* sorting

def md(state):
    # calc manhattan dist
    dist=0
    for i in range(9):
        if state[i]==0:
            continue
        # target pos (1-8)
        tx=(state[i]-1)%3
        ty=(state[i]-1)//3
        
        # curr pos
        cx=i%3
        cy=i//3
        
        dist+= abs(tx-cx) + abs(ty-cy)
    return dist

def get_nbrs(state):
    # find valid moves for 0
    nbrs=[]
    emp_idx=state.index(0)
    x=emp_idx%3
    y=emp_idx//3
    
    moves=[(-1,0),(1,0),(0,-1),(0,1)] 
    for dx,dy in moves:
        nx,ny=x+dx,y+dy
        if 0<=nx<3 and 0<=ny<3:
            new_idx=ny*3+nx
            new_st=list(state)
            new_st[emp_idx],new_st[new_idx]=new_st[new_idx],new_st[emp_idx]
            nbrs.append(tuple(new_st))
    return nbrs

def solve(start_st):
    # A* search
    goal_st = (1,2,3,4,5,6,7,8,0)
    
    if start_st == goal_st:
        return [start_st]
        
    front=[]
    cnt=1 
    heapq.heappush(front,(md(start_st),0,start_st,[start_st]))
    
    g_score= {start_st:0}
    
    while front:
        _,_,curr_st,path=heapq.heappop(front)
        
        if curr_st== goal_st:
            return path
            
        for nbr in get_nbrs(curr_st):
            temp_g=g_score[curr_st]+1
            
            if nbr not in g_score or temp_g<g_score[nbr]:
                g_score[nbr]=temp_g
                f_score =temp_g+md(nbr)
                heapq.heappush(front,(f_score,cnt,nbr,path+[nbr]))
                cnt+=1
                
    return None
