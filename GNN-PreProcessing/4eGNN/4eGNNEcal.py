import torch

from torch_geometric.utils import from_networkx

import pandas as pd

import numpy as np

import networkx as nx

import os

from zipfile import ZipFile

import zipfile

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
    D = []
    readerE = pd.read_csv("/Directory/Energy4.csv", chunksize=n)
    for chunkE in readerE:
        #nTS = 0
        if nE<nc:
            nE = nE+1
            continue
        elif nE>nc:
            break
        elif nE==nc:
            if nc == 0:
                for j in range(n):
                    C = []
                    M = []
                    L = []
                    E = []
                    for i in range(450):
                        if pd.isna(chunkC['{}'.format(i)][j]) == False and pd.isna(chunkE['{}'.format(i)][j])==False:
                            D = int(chunkC['{}'.format(i)][j])
                            C.append(EcalID(D).cell())
                            M.append(EcalID(D).module())
                            L.append(EcalID(D).layer())
                            E.append(chunkE['{}'.format(i)][j])
                    MNN = nx.Graph()
                    MNN.add_nodes_from([(k,{"pos":(float(C[k]),float(M[k]),float(L[k])),"x":[float(E[k]),float(C[k]),float(M[k]),float(L[k])]   }) for k in range(len(C))] )
                    Edges = nx.geometric_edges(MNN, radius=40)
                    MNN.add_edges_from(Edges)
                    MNN = from_networkx(MNN)
                    MNN["y"] = 3
                    torch.save(MNN,'/Directory/GNN/Ecal/4e{}.pt'.format(nc))
                    with zipfile.ZipFile('/Directory/GNN/Ecal/4e{}.zip'.format(nc), 'w', zipfile.ZIP_DEFLATED) as f:
                            f.write('/Directory/GNN/Ecal/4e{}.pt'.format(nc))
                    os.remove('/Directory/GNN/Ecal/4e{}.pt'.format(nc))
            elif NRR <n:
                for j in range(nc*n,nc*n+NRR):
                    C = []
                    M = []
                    L = []
                    E = []
                    for i in range(450):
                        if pd.isna(chunkC['{}'.format(i)][j]) == False and pd.isna(chunkE['{}'.format(i)][j])==False:
                            D = int(chunkC['{}'.format(i)][j])
                            C.append(EcalID(D).cell())
                            M.append(EcalID(D).module())
                            L.append(EcalID(D).layer())
                            E.append(chunkE['{}'.format(i)][j])
                    MNN = nx.Graph()
                    MNN.add_nodes_from([(k,{"pos":(float(C[k]),float(M[k]),float(L[k])),"x":[float(E[k]),float(C[k]),float(M[k]),float(L[k])]   }) for k in range(len(C))] )
                    Edges = nx.geometric_edges(MNN, radius=40)
                    MNN.add_edges_from(Edges)
                    MNN = from_networkx(MNN)
                    MNN["y"] = 3
                    torch.save(MNN,'/Directory/GNN/Ecal/4e{}.pt'.format(nc))
                    with zipfile.ZipFile('/Directory/GNN/Ecal/4e{}.zip'.format(nc), 'w', zipfile.ZIP_DEFLATED) as f:
                            f.write('/Directory/GNN/Ecal/4e{}.pt'.format(nc))
                    os.remove('/Directory/GNN/Ecal/4e{}.pt'.format(nc))
            else:
                for j in range(nc*NRR,(nc+1)*NRR):
                    C = []
                    M = []
                    L = []
                    E = []
                    for i in range(450):
                        if pd.isna(chunkC['{}'.format(i)][j]) == False and pd.isna(chunkE['{}'.format(i)][j])==False:
                            D = int(chunkC['{}'.format(i)][j])
                            C.append(EcalID(D).cell())
                            M.append(EcalID(D).module())
                            L.append(EcalID(D).layer())
                            E.append(chunkE['{}'.format(i)][j])
                    MNN = nx.Graph()
                    MNN.add_nodes_from([(k,{"pos":(float(C[k]),float(M[k]),float(L[k])),"x":[float(E[k]),float(C[k]),float(M[k]),float(L[k])]   }) for k in range(len(C))] )
                    Edges = nx.geometric_edges(MNN, radius=40)
                    MNN.add_edges_from(Edges)
                    MNN = from_networkx(MNN)
                    MNN["y"] = 3
                    torch.save(MNN,'/Directory/GNN/Ecal/4e{}.pt'.format(nc))
                    with zipfile.ZipFile('/Directory/GNN/Ecal/4e{}.zip'.format(nc), 'w', zipfile.ZIP_DEFLATED) as f:
                            f.write('/Directory/GNN/Ecal/4e{}.pt'.format(nc))
                    os.remove('/Directory/GNN/Ecal/4e{}.pt'.format(nc))
            nE = nE+1
    nc = nc+1
