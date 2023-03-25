# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
import numpy as np
import matplotlib.pyplot as plt
from vtk.util.numpy_support import vtk_to_numpy

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

z_overflow = [330,250,450,530,250,330,530,450,250,330,530,450,330,250,450,530,390,390,390,390,190,590,390,390,310,470,390] #mm
z_underflow = [-0.299,-0.699,-0.299,-0.699,-0.299,-0.699,-0.299,-0.699,-0.299,-0.699,-0.299,-0.699,-0.299,-0.699,-0.299,-0.699,-0.499,-0.499,-0.499,-0.499,-0.499,-0.499,-0.099,-0.899,-0.499,-0.499,-0.499]

diametro_overflow = [60,60,60,60,60,60,60,60,100,100,100,100,100,100,100,100,40,120,80,80,80,80,80,80,80,80,80] #mm
diametro_underflow = [40, 40, 40, 40, 80, 80, 80, 80, 40, 40, 40, 40, 80, 80, 80, 80, 60, 60, 20, 100, 60, 60 , 60, 60, 60 , 60, 60] #mm

vtk_files = ['/home/n002/Documents/multi_cyclone/27/VTK/27_28443.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_31722.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_35026.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_38337.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_41683.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_45071.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_48429.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_51764.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_55144.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_58521.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_61890.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_65252.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_68587.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_71941.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_75340.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_78730.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_82070.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_85446.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_88856.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_92267.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_95631.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_98958.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_102360.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_105759.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_109130.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_112473.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_115880.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_119281.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_122644.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_126027.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_129426.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_132836.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_136251.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_139644.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_143025.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_146397.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_149740.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_153094.vtk', '/home/n002/Documents/multi_cyclone/27/VTK/27_156505.vtk']

for i in range(len(vtk_files)):
    # LENDO O VTK NO TEMPO i
    dados = LegacyVTKReader(FileNames=vtk_files[i])

    # CRIANDO O SLICE NO OVERFLOW
    slice_overflow = Slice(registrationName='slice_overflow', Input=dados)
    slice_overflow.SliceType = 'Plane'
    slice_overflow.HyperTreeGridSlicer = 'Plane'
    slice_overflow.SliceOffsetValues = [0.0]

    slice_overflow.SliceType.Origin = [0, 0, z_overflow[-1]/1000] # mudar o indice

    slice_overflow.SliceType.Normal = [0.0, 0.0, 1.0]

    # CRIANDO O SLICE NO INLET
    slice_inlet = Slice(registrationName='slice_inlet', Input=dados)
    slice_inlet.SliceType = 'Plane'
    slice_inlet.HyperTreeGridSlicer = 'Plane'
    slice_inlet.SliceOffsetValues = [0.0]

    slice_inlet.SliceType.Origin = [0.14, 0.18, 0]

    slice_inlet.SliceType.Normal = [1.0, 0.0, 0.0]

    # CRIANDO O SLICE NO UNDEFLOW
    slice_underflow = Slice(registrationName='slice_underflow', Input=dados)
    slice_underflow.SliceType = 'Plane'
    slice_underflow.HyperTreeGridSlicer = 'Plane'
    slice_underflow.SliceOffsetValues = [0.0]
    60
    slice_underflow.SliceType.Origin = [0.0, 0.0, z_underflow[-1]] # mudar esse indice

    slice_underflow.SliceType.Normal = [0.0, 0.0, 1.0]

    # EXTRAINDO OS DADOS DOS SLICES - U.PARTICLES
    Uparticles_inlet = vtk_to_numpy(servermanager.Fetch(slice_inlet).GetCellData().GetArray('U.particles'))
    Uparticles_overflow = vtk_to_numpy(servermanager.Fetch(slice_overflow).GetCellData().GetArray('U.particles'))
    Uparticles_underflow = vtk_to_numpy(servermanager.Fetch(slice_underflow).GetCellData().GetArray('U.particles'))

    alphaParticles_inlet = vtk_to_numpy(servermanager.Fetch(slice_inlet).GetCellData().GetArray('alpha.particles'))
    alphaParticles_overflow = vtk_to_numpy(servermanager.Fetch(slice_overflow).GetCellData().GetArray('alpha.particles'))
    alphaParticles_underflow = vtk_to_numpy(servermanager.Fetch(slice_underflow).GetCellData().GetArray('alpha.particles'))


    # EXTRAINDO A NORMAL DE U
    mean_Uparticles_inlet = np.mean(Uparticles_inlet[:,0])
    mean_Uparticles_overflow = np.mean(Uparticles_overflow[:,2])
    mean_Uparticles_undeflow = np.mean(Uparticles_underflow[:,2])

    # EXTRAINDO A NORMA DOS VETORES U
    alphaParticlesTotal_inlet = np.mean(alphaParticles_inlet)
    alphaParticlesTotal_overflow = np.mean(alphaParticles_overflow)
    alphaParticlesTotal_underflow = np.mean(alphaParticles_underflow)

    # CALCULANDO AS AREAS DAS SUPERFICIES
    area_overflow = np.pi*((diametro_overflow[-1]/(1000))**2)/4
    area_underflow = np.pi*((diametro_underflow[-1]/(1000))**2)/4
    area_inlet = np.pi*(0.04**2)/4

    '''print(f'alpha.particles do inlet: {alphaParticlesTotal_inlet*100}')
    print(f'alpha.particles do overflow: {alphaParticlesTotal_overflow*100}')
    print(f'alpha.partciles do undeflow: {alphaParticlesTotal_underflow*100}')'''

    # VAZAO MASSICA DAS PARTICULAS NAS SUPERFICIES

    vMassica_overflow = area_overflow*800*mean_Uparticles_overflow*alphaParticlesTotal_overflow
    vMassica_inlet = area_inlet*800*mean_Uparticles_inlet*alphaParticlesTotal_inlet
    vMassica_underflow = area_underflow*800*mean_Uparticles_undeflow*alphaParticlesTotal_underflow

    '''print(vMassica_inlet)
    print(vMassica_overflow)
    print(vMassica_underflow)'''

    print(f'{(np.abs(vMassica_inlet) - np.abs(vMassica_underflow) - np.abs(vMassica_overflow))*100/np.abs(vMassica_inlet)}')

