
import os

import matplotlib.pyplot as pyplot
import matplotlib.mlab as mlab
from matplotlib import cm
from matplotlib.ticker import MultipleLocator
import matplotlib.patches as patches
import scipy.interpolate as interpolate
import numpy

from Safeguards import Collect, Graphics, MC

global Collections
global FiguresPath

global PNARColl
global CIPNColl
global DNColl
global DDSIColl
global DDAColl

def savefig(Name, ext=['pdf', 'png']):
    path = os.path.join(FiguresPath, Name)
    for e in ext:
        pyplot.savefig(path+'.%s' %e, transparent=True, bbox_inches='tight')
    return path

def CollName(Coll):
    """
    CollName will return a consistent string for the name of particular
    results.
    """
    C = Coll[0]
    if   C.get('DN') == -1:   return 'DNH2O'
    elif C.get('CIPN') == -1: return 'CIPNH2O'
    elif C.get('DDA') == -1:  return 'DDAH2O'
    elif C.get('PNAR') == -1: return 'PNARH2O'
    elif C.get('DDSI') == -1: return 'DDSIBH2O'
    else: return None

def PlainPlots():
    PlainPath = 'Plain'

    for Coll in Collections:
        Name = CollName(Coll)
        print(Coll[0])
        print(Name)
        print()

        Fig = Graphics.PlotData(Coll, yData='CR', xData='PuEff Mass', 
                xLabel='Assembly Attribute', yLabel='Detector Response')
        ax = Fig.axes[0]
#       ax.yaxis.set_minor_locator(MultipleLocator(0.01))
#       pyplot.grid()
        savefig(os.path.join(PlainPath, CollName(Coll)))

def MCPlot(Coll, m=None, sd=None, N=1E5, Limits=[None, None, None], plotSmudge=False,
        xData='PuEff Mass', yData='CR HEU', loc='best', PlotData=True, 
        alpha=1.0, DataLegend=True, Figure=None, meanLine=True, smudgeColor='k',
        GaussColor='k', Gaussls='-', Gausslw=2, GaussLabel=None):
    if not m:
        C = Coll[Collect.StandardAssembly]
        m = C.get('CR')
        sd = C.get('CR SD')

    mc = MC.MC(Coll, ['Burnup', 'Enrichment', 'Cooling'], 
            xData=xData, yData=yData, N=N, mean=m, sd=sd, 
            Limits=Limits, cutoff=0.0)

    if not Figure:
        Fig = pyplot.figure()
        ax1 = Fig.add_subplot(111)
        ax2 = ax1.twinx()
    else:
        Fig = Figure
        ax1, ax2 = Fig.axes

    if PlotData:
        Graphics.PlotData(Coll, yData=yData, xData=xData, Axes=ax1, alpha=alpha)
        if DataLegend: Graphics.MakeLegend(loc=loc, fig=ax1, ncol=2)

    if plotSmudge: mc.Plot(ax1, color=smudgeColor)

    b, E = mc.PlotGaussian(ax2, B=50, color=GaussColor, ls=Gaussls, 
            lw=Gausslw, label=GaussLabel)

    ax2.set_ylabel('P Probability')
    if meanLine:
        ax2.axvline(mc.xMean, color='r', ls='-', lw=2)
    print("Monte Carlo: mean  = %f, sd = %f" %(mc.xMean, mc.xSD))

    ax1.set_xlabel('Assembly Attribute')
    ax1.set_ylabel('Detector Response')

    return Fig

def MCPNAR(L):
    print("PNAR")
    C = PNARColl[Collect.StandardAssembly]
    m = C.get('CR')
    sd = m*0.01
    print("mean: %.4f, sd: %.4f" %(m, sd))
    print("mean: %.4G, sd: %.4G" %(C.get('PuEff Mass'), C.get('PuEff Mass Sd')))
    MCPlot(PNARColl, m=m, sd=sd, plotSmudge=True, yData='CR', loc='lower right')
    savefig('PNARFull')
    MCPlot(PNARColl, m=m, sd=sd, Limits=L, plotSmudge=True, yData='CR', 
            loc='lower right')
    savefig('PNARLimited')

def MCCIPN(L):
    print("CIPN")
    C = CIPNColl[Collect.StandardAssembly]
    m = C.get('CR')
    sd = m*0.01
    print("mean: %.4f, sd: %.4f" %(m, sd))
    print("mean: %.4G, sd: %.4G" %(C.get('PuEff Mass'), C.get('PuEff Mass SD')))
    MCPlot(CIPNColl, m=m, sd=sd, plotSmudge=False, yData='CR', loc='lower right')
    savefig('CIPNFull')
    MCPlot(CIPNColl, m=m, sd=sd, Limits=L, plotSmudge=False, yData='CR', 
            loc='lower right')
    savefig('CIPNLimited')

def MCDN(L):
    print("DN")
    C = DNColl[Collect.StandardAssembly]
    m = C.get('CR')
    sd = m*0.01
    print("mean: %.4f, sd: %.4f" %(m, sd))
    print("mean: %.4G, sd: %.4G" %(C.get('PuEff Mass'), C.get('PuEff Mass SD')))
    MCPlot(DNColl, m=m, sd=sd, plotSmudge=False, yData='CR', loc='lower right')
    savefig('DNFull')
    MCPlot(DNColl, m=m, sd=sd, Limits=L, plotSmudge=False, yData='CR', 
            loc='lower right')
    savefig('DNLimited')

def MCDDSI(L):
    print("DDSI")
    C = DDSIColl[Collect.StandardAssembly]
    m = C.get('CR')
    sd = m*0.01
    print("mean: %.4f, sd: %.4f" %(m, sd))
    print("mean: %.4G, sd: %.4G" %(C.get('PuEff Mass'), C.get('PuEff Mass SD')))
    MCPlot(DDSIColl, m=m, sd=sd, plotSmudge=False, yData='CR', loc='lower right')
    savefig('DDSIFull')
    MCPlot(DDSIColl, m=m, sd=sd, Limits=L, plotSmudge=False, yData='CR', 
            loc='lower right')
    savefig('DDSILimited')

def MCDDA(L):
    print("DDA")
    C = DDAColl[Collect.StandardAssembly]
    m = C.get('CR')
    sd = m*0.01
    print("mean: %.4f, sd: %.4f" %(m, sd))
    print("mean: %.4G, sd: %.4G" %(C.get('PuEff Mass'), C.get('PuEff Mass SD')))
    MCPlot(DDAColl, m=m, sd=sd, plotSmudge=False, yData='CR', loc='lower right')
    savefig('DDAFull')
    MCPlot(DDAColl, m=m, sd=sd, Limits=L, plotSmudge=False, yData='CR', 
            loc='lower right')
    savefig('DDALimited')

def MCSINRD(L):
    print("SINRD")
    C = SINRDColl[Collect.StandardAssembly]
    m = C.get('NORM (Gd+Hf-Cd)')
    sd = m*0.01
    print("mean: %.4f, sd: %.4f" %(m, sd))
    print("mean: %.4G, sd: %.4G" %(C.get('Pu239 Mass'), C.get('Pu239 Mass SD')))
    MCPlot(SINRDColl, m=m, sd=sd, plotSmudge=False, yData='NORM (Gd+Hf-Cd)', 
            xData='Pu239 Mass', loc='upper left')
    savefig('SINRDFull')
    MCPlot(SINRDColl, m=m, sd=sd, Limits=L, plotSmudge=False, yData='NORM (Gd+Hf-Cd)',
            xData='Pu239 Mass', loc='lower left')
    savefig('SINRDLimited')

def CheckAlternateAssemblies(L):
    def _MakePlot(C, Lim):
        Figure = pyplot.figure()
        ax1 = Figure.add_subplot(111)
        ax2 = ax1.twinx()

        m = C.get('CR')
        sd = m*0.01
        print("mean: %.4f, sd: %.4f" %(m, sd))
        print("mean: %.4G, sd: %.4G" %(C.get('PuEff Mass'), C.get('PuEff Mass SD')))
        MCPlot(PNARColl, m=m, sd=sd, N=N, Limits=Lim, plotSmudge=False, yData='CR',
                DataLegend=False, meanLine=False, Figure=Figure)

        color = C.PlotColor()
        markerStyle = C.MarkerStyle()

        x = C.get('PuEff Mass')
        y = m
        print("{:.4f}, {:.4f}".format(x,y))
        ax1.plot(x, y, color=color, marker=markerStyle, markersize=10,
                markeredgecolor='k', markeredgewidth=2)

    print("CheckAlternateAssemblies")
    N=1E5
    Coll = PNARColl.limit('Enrichment', 4).limit('Cooling', 5)
    for C in Coll:
        print("\nC: {}".format(C))

        B = C.get('Burnup')
        L[0] = (B, B*0.05)

        print("\nFull")
        _MakePlot(C, [None, None, None])
        name = "AlternateAssemblies/Burnup{:.0f}Full".format(B)
        savefig(name)

        print("\nLimited")
        _MakePlot(C, L)
        name = "AlternateAssemblies/Burnup{:.0f}Limited".format(B)
        savefig(name)

def Check(L):
    print("Check")
    C = PNARColl[Collect.StandardAssembly]
    Coll = PNARColl.exclude('Burnup', 45)
    m = C.get('CR')
    sd = m*0.01
    print("mean: %.4f, sd: %.4f" %(m, sd))
    print("mean: %.4G, sd: %.4G" %(C.get('PuEff Mass'), C.get('PuEff Mass SD')))
    MCPlot(Coll, m=m, sd=sd, plotSmudge=False, yData='CR', loc='lower right')
    savefig('CheckFull')
    MCPlot(Coll, m=m, sd=sd, Limits=L, plotSmudge=False, yData='CR', 
            loc='lower right')
    savefig('CheckLimited')

def CheckManyN(L):
    def _MakePlot(L=[None, None, None]):
        Figure = pyplot.figure()
        ax1 = Figure.add_subplot(111)
        ax2 = ax1.twinx()

        for N, color in zip(Ns[:3], colors[:3]):
            print("\nN = {0:.0E}".format(N))
            print("mean: %.4f, sd: %.4f" %(m, sd))
            print("mean: %.4G, sd: %.4G" %(C.get('PuEff Mass'), 
                C.get('PuEff Mass SD')))
            MCPlot(PNARColl, m=m, sd=sd, N=N, Limits=L, plotSmudge=False, 
                yData='CR', DataLegend=False, meanLine=False, Figure=Figure, GaussColor=color,
                GaussLabel='{0}'.format(N))

            ax2.legend(['{0:.0E}'.format(n) for n in Ns], loc='upper left', 
                title='# of Trials')

            ax1.set_xlim((2000, 11000))

    print("Check Many N")
    C = PNARColl[Collect.StandardAssembly]
    Coll = PNARColl.exclude('Burnup', 45)
    m = C.get('CR')
    sd = m*0.05

    Ns = [1E2, 1E4, 1E6, 1E5]
    colors = ['g', 'r', 'b', 'k']

    print("\n-----------\nFull\n-----------")
    _MakePlot()
    savefig('CheckManyNFull')

    print("\n-----------\nLimited\n-----------")
    _MakePlot(L)
    savefig('CheckManyNLimited')

def CheckManyUncertainty(L):
    """
    CheckManyUncertainty will make a plot with the "measured" detector response estimated
    at 0.1, 1.0, and 10%.
    """
    def _MakePlot(L=[None, None, None]):
        Figure = pyplot.figure()
        ax1 = Figure.add_subplot(111)
        ax2 = ax1.twinx()

        for s, color in zip(SDs[:3], colors[:3]):
            print("\n{0}".format(s))
            sd = m*s
            print("mean: %.4f, sd: %.4f" %(m, sd))
            print("mean: %.4G, sd: %.4G" %(C.get('PuEff Mass'), C.get('PuEff Mass Sd')))

            if s == 0.01: PD = True
            else: PD = False

            Figure = MCPlot(PNARColl, m=m, sd=sd, Limits=L, plotSmudge=False, 
                yData='CR', loc='lower right', PlotData=PD, alpha=0.25, 
                meanLine=False, DataLegend=False, Figure=Figure, 
                GaussColor=color, smudgeColor=color, GaussLabel='%s' %s)

        ax2.legend(['%s' %s for s in SDs], loc='upper left', 
                title='Measured Uncertainty')

    print("PNAR")
    C = PNARColl[Collect.StandardAssembly]
    m = C.get('CR')

    SDs = [0.1, 0.05, 0.01, 0.001]
    colors = ['b', 'g', 'k', 'r']
    _MakePlot()
    savefig('CheckManyUncertaintyFull')

    print("\n-----------\nLimited\n-----------\n")
    _MakePlot(L)
    savefig('CheckManyUncertaintyLimited')

if __name__ == "__main__":
    print("\nI'm making figures for MCPNAR.tex")

    FiguresPath = 'Figures'

    # Prepare Collections
    DNColl =   Collect.ReadCSV('Data/DNH2O.csv')
    CIPNColl = Collect.ReadCSV('Data/CIPNH2O.csv')
    DDAColl = Collect.ReadCSV('Data/DDAH2O.csv')
    PNARColl = Collect.ReadCSV('Data/PNARH2O.csv')
    DDSIColl = Collect.ReadCSV('Data/DDSIBH2O.csv')
    SINRDColl = Collect.ReadCSV('Data/SINRDBH2O.csv')
    Collections = [DNColl, CIPNColl, DDAColl, PNARColl, DDSIColl]

#   PlainPlots()

    # Monte Carlo simulations
    L = [(45, 2.25), (4, 0.2), (5, 1)]
#   MCPNAR(L)
#   Check(L)
#   MCCIPN(L)
#   MCDN(L)
#   MCDDA(L)
#   MCDDSI(L)
#   MCSINRD(L)
#   CheckManyUncertainty(L)
#   CheckManyN(L)
    CheckAlternateAssemblies(L)


