def CalculationPixelsArea(x,y,Zoomincrementation,PixelsArea):
    if(Zoomincrementation==-2):
        PixelsArea[0].append([x,y])
        PixelsArea[1].append([x*2,y*2])
        PixelsArea[2].append([x*4,y*4])
        PixelsArea[3].append([x*8,y*8])
        PixelsArea[4].append([x*16,y*16])
    elif(Zoomincrementation==0):
        PixelsArea[0].append([x//2,y//2])
        PixelsArea[1].append([x,y])
        PixelsArea[2].append([x*2,y*2])
        PixelsArea[3].append([x*4,y*4])
        PixelsArea[4].append([x*8,y*8])
    elif(Zoomincrementation==2):
        PixelsArea[0].append([x//4,y//4])
        PixelsArea[1].append([x//2,y//2])
        PixelsArea[2].append([x,y])
        PixelsArea[3].append([x*2,y*2])
        PixelsArea[4].append([x*4,y*4])
    elif(Zoomincrementation==4):
        PixelsArea[0].append([x//8,y//8])
        PixelsArea[1].append([x//4,y//4])
        PixelsArea[2].append([x//2,y//2])
        PixelsArea[3].append([x,y])
        PixelsArea[4].append([x*2,y*2])
    elif(Zoomincrementation==6):
        PixelsArea[0].append([x//16,y//16])
        PixelsArea[1].append([x//8,y//8])
        PixelsArea[2].append([x//4,y//4])
        PixelsArea[3].append([x//2,y//2])
        PixelsArea[4].append([x,y])
    
    # print("pixel Area Fonction 1 :",PixelsArea)
    return PixelsArea