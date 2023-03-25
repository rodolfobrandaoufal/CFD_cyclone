# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

vortex_Zcoord_over = [0.340000,0.260000,0.460000,0.540000,0.260000,0.340000,0.540000,0.460000,0.260000,0.340000,0.540000,0.460000,0.340000,0.260000,0.450000,0.540000,0.400000,0.400000,0.400000,0.400000,0.200000,0.600000,0.400000,0.400000,0.320000,0.480000,0.400000]

vortex_Zcoord_under = [ -0.300000, -0.700000, -0.300000, -0.700000, -0.300000, -0.700000, -0.300000, -0.700000, -0.300000, -0.700000, -0.300000, -0.700000, -0.300000, -0.700000, -0.300000, -0.700000, -0.480000, -0.480000, -0.490000, -0.490000, -0.490000, -0.490000, -0.090000, -0.890000, -0.490000, -0.490000, -0.490000]


root_folder = '/home/n002/Documents/multi_cyclone/'

for i in range(1,28,1):
    try:
        folder_foam = f'/home/n002/Documents/multi_cyclone/{i}/cyclone_laminar.foam'
        # create a new 'OpenFOAMReader'
        cyclone_laminarfoam = OpenFOAMReader(registrationName='cyclone_laminar.foam', FileName=folder_foam)
        cyclone_laminarfoam.MeshRegions = ['internalMesh']
        cyclone_laminarfoam.CellArrays = ['U.air', 'U.particles', 'alpha.air', 'alpha.particles','p']

        # create a new 'Slice'
        inlet_slice = Slice(registrationName='Slice1', Input=cyclone_laminarfoam)
        inlet_slice.SliceType = 'Plane'
        inlet_slice.HyperTreeGridSlicer = 'Plane'
        inlet_slice.SliceOffsetValues = [0.0]

        # init the 'Plane' selected for 'SliceType'
        inlet_slice.SliceType.Origin = [0.140, 0.180, 0]

        # init the 'Plane' selected for 'HyperTreeGridSlicer'
        inlet_slice.HyperTreeGridSlicer.Origin = [0.02500149980187416, 5.2500516176223755e-05, -0.07999999821186066]


        # create a new 'Slice' overflow
        overflow_slice = Slice(registrationName='Slice1', Input=cyclone_laminarfoam)
        overflow_slice.SliceType = 'Plane'
        overflow_slice.HyperTreeGridSlicer = 'Plane'
        overflow_slice.SliceOffsetValues = [0.0]

        # init the 'Plane' selected for 'SliceType'
        overflow_slice.SliceType.Origin = [0, 0, vortex_Zcoord_over[i-1]]

        # init the 'Plane' selected for 'HyperTreeGridSlicer'
        overflow_slice.HyperTreeGridSlicer.Origin = [0.02500149980187416, 5.2500516176223755e-05, -0.07999999821186066]

        overflow_slice.SliceType.Normal = [0.0, 0.0, 1.0]


        # create a new 'Slice' underflow
        underflow_slice = Slice(registrationName='Slice1', Input=cyclone_laminarfoam)
        underflow_slice.SliceType = 'Plane'
        underflow_slice.HyperTreeGridSlicer = 'Plane'
        underflow_slice.SliceOffsetValues = [0.0]

        # init the 'Plane' selected for 'SliceType'
        underflow_slice.SliceType.Origin = [0, 0, vortex_Zcoord_under[i-1]]

        # init the 'Plane' selected for 'HyperTreeGridSlicer'
        underflow_slice.HyperTreeGridSlicer.Origin = [0.02500149980187416, 5.2500516176223755e-05, -0.07999999821186066]

        underflow_slice.SliceType.Normal = [0.0, 0.0, 1.0]


        dataovertime_inlet = PlotDataOverTime(registrationName='PlotDataOverTime1', Input=inlet_slice)
        dataovertime_overflow = PlotDataOverTime(registrationName='PlotDataOverTime2', Input=overflow_slice)
        dataovertime_underflow = PlotDataOverTime(registrationName='PlotDataOverTime3', Input=underflow_slice)

        name_file1 = '/home/n002/Documents/multi_cyclone/'+str(i)+'/dados_inlet_'+str(i)+'.csv'
        name_file2 = '/home/n002/Documents/multi_cyclone/'+str(i)+'/dados_overflow_'+str(i)+'.csv'
        name_file3 = '/home/n002/Documents/multi_cyclone/'+str(i)+'/dados_underflow_'+str(i)+'.csv'
        
        
        SaveData(name_file1, proxy=dataovertime_inlet, RowDataArrays=['avg(U.air (Magnitude))', 'avg(U.particles (Magnitude))', 'avg(alpha.air)', 'avg(alpha.particles)', 'avg(p)'],
            FieldAssociation='Row Data')
            
        SaveData(name_file2, proxy=dataovertime_overflow, RowDataArrays=['avg(U.air (Magnitude))', 'avg(U.particles (Magnitude))', 'avg(alpha.air)', 'avg(alpha.particles)', 'avg(p)'],
        FieldAssociation='Row Data')

        SaveData(name_file3, proxy=dataovertime_underflow, RowDataArrays=['avg(U.air (Magnitude))', 'avg(U.particles (Magnitude))', 'avg(alpha.air)', 'avg(alpha.particles)', 'avg(p)'],
        FieldAssociation='Row Data')
    
        print(f"Simulação {i} finalizada")
    except:
        print(f"Simulação {i} deu erro")



