import pandas as pd
import numpy as np

n = 1000

nc = 0

nE = 0

nTS = 0

import libDetDescr

from libDetDescr import EcalID, HcalID,EcalTriggerID


readerC = pd.read_csv("/Directory/EcalIDFile4.csv", chunksize=n)


for chunkC in readerC:
    nE = 0
    NRR = chunkC.shape[0]
    NC = chunkC.shape[1]
    readerE = pd.read_csv("/Directory/Energy4.csv", chunksize=n)
    for chunkE in readerE:
        nTS = 0
        if nE<nc:
            nE = nE+1
            continue
        elif nE>nc:
            break
        elif nE==nc:
            readerTS = pd.read_csv("TSPOS4.csv", chunksize=n)
            for chunkTS in readerTS:
                if nTS<nc:
                    nTS = nTS+1
                    continue
                elif nTS>nc:
                    break
                elif nTS == nc and nTS == nE:
                    if nc==0:
                        for j in range(n):
                            B = np.zeros((35,8,450))
                            for i in range(451):
                                if i == 0:
                                                    Y1 = int(chunkTS['{}'.format('y1')][j])
                                                    Y2 = int(chunkTS['{}'.format('y2')][j])
                                                    Y3 = int(chunkTS['{}'.format('y3')][j])
                                                    Y4 = int(chunkTS['{}'.format('y4')][j])
                                                    
                                                    X1 = int(chunkTS['{}'.format('x1')][j])
                                                    X2 = int(chunkTS['{}'.format('x2')][j])
                                                    X3 = int(chunkTS['{}'.format('x3')][j])
                                                    X4 = int(chunkTS['{}'.format('x4')][j])
                                                    
                                                    
                                                    if Y1 == Y3 and Y1==Y2 and Y1 == Y4 and X1==X3 and X1==X2 and X1==X4:
                                                        B[0][X1][Y1] = 1
                                                    elif Y1 == Y2 and Y3==Y4 and X1 == X2 and X3==X4:
                                                        B[0][X1][Y1] = 1
                                                        B[0][X3][Y3] = 1
                                                    elif Y1 == Y3 and Y2==Y4 and X1 == X3 and X2==X4:
                                                         B[0][X1][Y1] = 1
                                                         B[0][X2][Y2] = 1
                                                    elif Y1 == Y4 and Y2==Y3 and X1 == X4 and X2==X3:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X2][Y2] = 1
                                                    elif Y1 == Y2 and Y1==Y3 and X1 == X2 and X1==X3:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X4][Y4] = 1
                                                    elif Y1 == Y2 and Y1==Y4 and X1 == X2 and X1==X4:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X3][Y3] = 1
                                                    elif Y1 == Y3 and Y1==Y4 and X1 == X3 and X1==X4:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X2][Y2] = 1
                                                    elif Y2 == Y3 and Y2==Y1 and X2 == X3 and X2==X1:
                                                          B[0][X2][Y2] = 1
                                                          B[0][X4][Y4] = 1
                                                    elif Y2 == Y1 and Y2==Y4 and X2 == X1 and X2==X4:
                                                          B[0][X2][Y2] = 1
                                                          B[0][X3][Y3] = 1
                                                    elif Y2 == Y3 and Y2==Y4 and X2 == X3 and X2==X4:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X2][Y2] = 1
                                                    elif Y3 == Y1 and Y2==Y3 and X3 == X1 and X2==X3:
                                                          B[0][X3][Y3] = 1
                                                          B[0][X4][Y4] = 1
                                                    elif Y1 == Y3 and Y4==Y3 and X1 == X3 and X4==X3:
                                                          B[0][X2][Y2] = 1
                                                          B[0][X3][Y3] = 1
                                                    elif Y3 == Y2 and Y4==Y3 and X3 == X2 and X4==X3:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X3][Y3] = 1
                                                    elif Y4 == Y1 and Y4==Y2 and X4 == X1 and X4==X2:
                                                          B[0][X4][Y4] = 1
                                                          B[0][X3][Y3] = 1
                                                    elif Y4 == Y2 and Y4==Y3 and X4 == X2 and X4==X3:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X4][Y4] = 1
                                                    elif Y1 == Y2 and X1 == X2:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X3][Y3] = 1
                                                          B[0][X4][Y4] = 1
                                                    elif Y1 == Y3 and X1 == X3:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X2][Y2] = 1
                                                          B[0][X4][Y4] = 1
                                                    elif Y1 == Y4 and X1 == X4:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X2][Y2] = 1
                                                          B[0][X3][Y3] = 1
                                                    elif Y2 == Y3 and X2==X3:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X2][Y2] = 1
                                                          B[0][X4][Y4] = 1
                                                    elif Y2 == Y4 and X2 == X4:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X2][Y2] = 1
                                                          B[0][X3][Y3] = 1
                                                    elif Y3 == Y4 and X3 == X4:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X2][Y2] = 1
                                                          B[0][X3][Y3] = 1
                                                    else:
                                                        B[0][X1][Y1] = 1
                                                        B[0][X2][Y2] = 1
                                                        B[0][X3][Y3] = 1
                                                        B[0][X4][Y4] = 1
                                else:
                                    D = chunkC['{}'.format(i-1)][j]
                                    if pd.isna(D) == False and pd.isna(chunkE['{}'.format(i)][j])==False:
                                            DD = int(D)
                                            C = EcalID(DD).cell()
                                            M = EcalID(DD).module()
                                            L = EcalID(DD).layer()
                                            B[L+1][M][C] = chunkE['{}'.format(i)][j]
                            B = np.array(B)
                            np.savez_compressed('/Directory/CNN/ETSX/4e{}.npz'.format(nc), B)#Saves the array to a file named for example 1e1.npz in the NPZ file format.
                    elif NRR <n:
                        for j in range(nc*n,nc*n+NRR):
                            B = np.zeros((35,8,450))
                            for i in range(451):
                                if i == 0:
                                                    Y1 = int(chunkTS['{}'.format('y1')][j])
                                                    Y2 = int(chunkTS['{}'.format('y2')][j])
                                                    Y3 = int(chunkTS['{}'.format('y3')][j])
                                                    Y4 = int(chunkTS['{}'.format('y4')][j])
                                                    
                                                    X1 = int(chunkTS['{}'.format('x1')][j])
                                                    X2 = int(chunkTS['{}'.format('x2')][j])
                                                    X3 = int(chunkTS['{}'.format('x3')][j])
                                                    X4 = int(chunkTS['{}'.format('x4')][j])
                                                    
                                                    
                                                    if Y1 == Y3 and Y1==Y2 and Y1 == Y4 and X1==X3 and X1==X2 and X1==X4:
                                                        B[0][X1][Y1] = 1
                                                    elif Y1 == Y2 and Y3==Y4 and X1 == X2 and X3==X4:
                                                        B[0][X1][Y1] = 1
                                                        B[0][X3][Y3] = 1
                                                    elif Y1 == Y3 and Y2==Y4 and X1 == X3 and X2==X4:
                                                         B[0][X1][Y1] = 1
                                                         B[0][X2][Y2] = 1
                                                    elif Y1 == Y4 and Y2==Y3 and X1 == X4 and X2==X3:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X2][Y2] = 1
                                                    elif Y1 == Y2 and Y1==Y3 and X1 == X2 and X1==X3:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X4][Y4] = 1
                                                    elif Y1 == Y2 and Y1==Y4 and X1 == X2 and X1==X4:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X3][Y3] = 1
                                                    elif Y1 == Y3 and Y1==Y4 and X1 == X3 and X1==X4:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X2][Y2] = 1
                                                    elif Y2 == Y3 and Y2==Y1 and X2 == X3 and X2==X1:
                                                          B[0][X2][Y2] = 1
                                                          B[0][X4][Y4] = 1
                                                    elif Y2 == Y1 and Y2==Y4 and X2 == X1 and X2==X4:
                                                          B[0][X2][Y2] = 1
                                                          B[0][X3][Y3] = 1
                                                    elif Y2 == Y3 and Y2==Y4 and X2 == X3 and X2==X4:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X2][Y2] = 1
                                                    elif Y3 == Y1 and Y2==Y3 and X3 == X1 and X2==X3:
                                                          B[0][X3][Y3] = 1
                                                          B[0][X4][Y4] = 1
                                                    elif Y1 == Y3 and Y4==Y3 and X1 == X3 and X4==X3:
                                                          B[0][X2][Y2] = 1
                                                          B[0][X3][Y3] = 1
                                                    elif Y3 == Y2 and Y4==Y3 and X3 == X2 and X4==X3:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X3][Y3] = 1
                                                    elif Y4 == Y1 and Y4==Y2 and X4 == X1 and X4==X2:
                                                          B[0][X4][Y4] = 1
                                                          B[0][X3][Y3] = 1
                                                    elif Y4 == Y2 and Y4==Y3 and X4 == X2 and X4==X3:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X4][Y4] = 1
                                                    elif Y1 == Y2 and X1 == X2:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X3][Y3] = 1
                                                          B[0][X4][Y4] = 1
                                                    elif Y1 == Y3 and X1 == X3:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X2][Y2] = 1
                                                          B[0][X4][Y4] = 1
                                                    elif Y1 == Y4 and X1 == X4:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X2][Y2] = 1
                                                          B[0][X3][Y3] = 1
                                                    elif Y2 == Y3 and X2==X3:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X2][Y2] = 1
                                                          B[0][X4][Y4] = 1
                                                    elif Y2 == Y4 and X2 == X4:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X2][Y2] = 1
                                                          B[0][X3][Y3] = 1
                                                    elif Y3 == Y4 and X3 == X4:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X2][Y2] = 1
                                                          B[0][X3][Y3] = 1
                                                    else:
                                                        B[0][X1][Y1] = 1
                                                        B[0][X2][Y2] = 1
                                                        B[0][X3][Y3] = 1
                                                        B[0][X4][Y4] = 1
                                else:
                                    D = chunkC['{}'.format(i-1)][j]
                                    if pd.isna(D) == False and pd.isna(chunkE['{}'.format(i)][j])==False:
                                            DD = int(D)
                                            C = EcalID(DD).cell()
                                            M = EcalID(DD).module()
                                            L = EcalID(DD).layer()
                                            B[L+1][M][C] = chunkE['{}'.format(i)][j]
                            B = np.array(B)
                            np.savez_compressed('/Directory/CNN/ETSX/4e{}.npz'.format(nc), B)
                    else:
                        for j in range(nc*NRR,(nc+1)*NRR):
                            B = np.zeros((35,8,450))
                            for i in range(156):
                                if i == 0:
                                                    Y1 = int(chunkTS['{}'.format('y1')][j])
                                                    Y2 = int(chunkTS['{}'.format('y2')][j])
                                                    Y3 = int(chunkTS['{}'.format('y3')][j])
                                                    Y4 = int(chunkTS['{}'.format('y4')][j])
                                                    
                                                    X1 = int(chunkTS['{}'.format('x1')][j])
                                                    X2 = int(chunkTS['{}'.format('x2')][j])
                                                    X3 = int(chunkTS['{}'.format('x3')][j])
                                                    X4 = int(chunkTS['{}'.format('x4')][j])
                                                    
                                                    
                                                    if Y1 == Y3 and Y1==Y2 and Y1 == Y4 and X1==X3 and X1==X2 and X1==X4:
                                                        B[0][X1][Y1] = 1
                                                    elif Y1 == Y2 and Y3==Y4 and X1 == X2 and X3==X4:
                                                        B[0][X1][Y1] = 1
                                                        B[0][X3][Y3] = 1
                                                    elif Y1 == Y3 and Y2==Y4 and X1 == X3 and X2==X4:
                                                         B[0][X1][Y1] = 1
                                                         B[0][X2][Y2] = 1
                                                    elif Y1 == Y4 and Y2==Y3 and X1 == X4 and X2==X3:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X2][Y2] = 1
                                                    elif Y1 == Y2 and Y1==Y3 and X1 == X2 and X1==X3:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X4][Y4] = 1
                                                    elif Y1 == Y2 and Y1==Y4 and X1 == X2 and X1==X4:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X3][Y3] = 1
                                                    elif Y1 == Y3 and Y1==Y4 and X1 == X3 and X1==X4:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X2][Y2] = 1
                                                    elif Y2 == Y3 and Y2==Y1 and X2 == X3 and X2==X1:
                                                          B[0][X2][Y2] = 1
                                                          B[0][X4][Y4] = 1
                                                    elif Y2 == Y1 and Y2==Y4 and X2 == X1 and X2==X4:
                                                          B[0][X2][Y2] = 1
                                                          B[0][X3][Y3] = 1
                                                    elif Y2 == Y3 and Y2==Y4 and X2 == X3 and X2==X4:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X2][Y2] = 1
                                                    elif Y3 == Y1 and Y2==Y3 and X3 == X1 and X2==X3:
                                                          B[0][X3][Y3] = 1
                                                          B[0][X4][Y4] = 1
                                                    elif Y1 == Y3 and Y4==Y3 and X1 == X3 and X4==X3:
                                                          B[0][X2][Y2] = 1
                                                          B[0][X3][Y3] = 1
                                                    elif Y3 == Y2 and Y4==Y3 and X3 == X2 and X4==X3:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X3][Y3] = 1
                                                    elif Y4 == Y1 and Y4==Y2 and X4 == X1 and X4==X2:
                                                          B[0][X4][Y4] = 1
                                                          B[0][X3][Y3] = 1
                                                    elif Y4 == Y2 and Y4==Y3 and X4 == X2 and X4==X3:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X4][Y4] = 1
                                                    elif Y1 == Y2 and X1 == X2:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X3][Y3] = 1
                                                          B[0][X4][Y4] = 1
                                                    elif Y1 == Y3 and X1 == X3:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X2][Y2] = 1
                                                          B[0][X4][Y4] = 1
                                                    elif Y1 == Y4 and X1 == X4:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X2][Y2] = 1
                                                          B[0][X3][Y3] = 1
                                                    elif Y2 == Y3 and X2==X3:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X2][Y2] = 1
                                                          B[0][X4][Y4] = 1
                                                    elif Y2 == Y4 and X2 == X4:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X2][Y2] = 1
                                                          B[0][X3][Y3] = 1
                                                    elif Y3 == Y4 and X3 == X4:
                                                          B[0][X1][Y1] = 1
                                                          B[0][X2][Y2] = 1
                                                          B[0][X3][Y3] = 1
                                                    else:
                                                        B[0][X1][Y1] = 1
                                                        B[0][X2][Y2] = 1
                                                        B[0][X3][Y3] = 1
                                                        B[0][X4][Y4] = 1
                                else:
                                    D = chunkC['{}'.format(i-1)][j]
                                    if pd.isna(D) == False and pd.isna(chunkE['{}'.format(i)][j])==False:
                                            DD = int(D)
                                            C = EcalID(DD).cell()
                                            M = EcalID(DD).module()
                                            L = EcalID(DD).layer()
                                            B[L+1][M][C] = chunkE['{}'.format(i)][j]
                            B = np.array(B)
                            np.savez_compressed('/Directory/CNN/ETSX/4e{}.npz'.format(nc), B)
                    nTS = nTS+1
            nE = nE+1
    nc = nc+1
