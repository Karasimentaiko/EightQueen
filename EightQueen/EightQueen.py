
import time
from collections import deque

field = [[str(x+(8*y)+1).zfill(2) for x in range(8)] for y in range(8)]

def print_field(field):
    #盤面を表示する
    print("    a  b  c  d  e  f  g  h   ")
    print("----------------------------")
    for i,j in enumerate(field):
        print(str(i) +" [ "+ " ".join(j) +" ] "  + str(i))
    print("----------------------------")
    print("    a  b  c  d  e  f  g  h   ")

def judge(field,que):
    while que:
        x,y = que.popleft()
        #print(x,y)
        #８方向探索
        for dx,dy in [(-1,0),(-1,-1),(0,-1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]:
            depth = 1
            for i in range(8):
                #検索対象の座標を設定する
                rx,ry = x+(dx*depth), y+(dy*depth)
                #fieldの範囲を超えていたら抜ける
                if any([rx<=-1, ry<=-1, 8<=rx, 8<=ry]):
                    break

                #ほかのクイーンにぶつかったら終わり
                if not str.isdigit(field[rx][ry]):
                    print(rx,ry)
                    return False
                
                depth+=1
    return True



que = deque()
queen_count = 1

while True:
    #入力処理
    print("----------------------------")
    print_field(field)
    print("#############################")
    print(str(queen_count)+"番目のクイーンの配置してください")
    select = input()
    print("----------------------------")
    time.sleep(1)

    #例外処理
    if not str.isdigit(select):
        print("半角で整数を入力してください")
        continue

    select = int(select)
    x,y = divmod(select-1,8)

    if x < 0 or 7 < x or y < 0 or 7 < y:
        print("そこは選べません")
        continue

    if not str.isdigit(field[x][y]):
        print("すでに配置されています")
        continue

    #クイーン配置
    field[x][y] = "*"+str(queen_count)
    que.append([x,y])
    
    queen_count+=1
    
    #8個設置したらループ終了
    if queen_count==9:
        print("8個配置しました")
        print_field(field)
        time.sleep(1)

        #成功判定
        if judge(field,que):
            print("クイーンが壊れませんでした!!　成功です")
        else:
            print("クイーンが壊れました...失敗です")
        break
