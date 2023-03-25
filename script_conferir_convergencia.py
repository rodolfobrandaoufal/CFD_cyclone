# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

vortex_Zcoord = [0.340000,0.260000,0.460000,0.540000,0.260000,0.340000,0.540000,0.460000,0.260000,0.340000,0.540000,0.460000,0.340000,0.260000,0.460000,0.540000,0.400000,0.400000,0.400000,0.400000,0.200000,0.600000,0.400000,0.400000,0.320000,0.480000,0.400000]

root_folder = '/home/n002/Documents/multi_cyclone/'
for i in range(6,7,1):
	
	sim_name = root_folder + str(i)+ '/cyclone_laminar.foam'
	
	# create a new 'OpenFOAMReader'
	cyclone_laminarfoam = OpenFOAMReader(registrationName='cyclone_laminar.foam', FileName=sim_name)


	cyclone_laminarfoam.MeshRegions = ['internalMesh']
	cyclone_laminarfoam.CellArrays = ['T.air', 'T.particles', 'Theta.particles', 'U.air', 'U.particles', 'alpha.air', 'alpha.particles', 'alphat.particles', 'nuFric.particles', 'nut.particles', 'p', 'p_rgh']

	# create a new 'Slice'
	slice1 = Slice(registrationName='Slice1', Input=cyclone_laminarfoam)
	slice1.SliceType = 'Plane'
	slice1.HyperTreeGridSlicer = 'Plane'
	slice1.SliceOffsetValues = [0.0]

	# init the 'Plane' selected for 'SliceType'
	slice1.SliceType.Origin = [0 , 0, vortex_Zcoord[i-1]]

	# init the 'Plane' selected for 'HyperTreeGridSlicer'
	slice1.HyperTreeGridSlicer.Origin = [0.02500149980187416, 5.2500516176223755e-05, -0.07999999821186066]

	# Properties modified on slice1.SliceType
	slice1.SliceType.Normal = [0.0, 0.0, 1.0]

	# create a new 'Plot Data Over Time'
	fracao_massica_overtime = PlotDataOverTime(registrationName='PlotDataOverTime1', Input=slice1)

	# Create a new 'Quartile Chart View'
	quartileChartView1 = CreateView('QuartileChartView')

	# show data in view
	quartileChartView1 = CreateView('QuartileChartView')

	# show data in view
	plotDataOverTime1Display = Show(fracao_massica_overtime, quartileChartView1, 'QuartileChartRepresentation')

	# trace defaults for the display properties.
	plotDataOverTime1Display.AttributeType = 'Row Data'
	plotDataOverTime1Display.UseIndexForXAxis = 0
	plotDataOverTime1Display.XArrayName = 'Time'
	plotDataOverTime1Display.SeriesVisibility = ['alpha.air ( block=1)', 'alpha.particles ( block=1)', 'alphat.particles ( block=1)', 'nuFric.particles ( block=1)', 'nut.particles ( block=1)', 'p ( block=1)', 'p_rgh ( block=1)', 'T.air ( block=1)', 'T.particles ( block=1)', 'Theta.particles ( block=1)', 'U.air (Magnitude) ( block=1)', 'U.particles (Magnitude) ( block=1)']
	plotDataOverTime1Display.SeriesLabel = ['alpha.air ( block=1)', 'alpha.air ( block=1)', 'alpha.particles ( block=1)', 'alpha.particles ( block=1)', 'alphat.particles ( block=1)', 'alphat.particles ( block=1)', 'nuFric.particles ( block=1)', 'nuFric.particles ( block=1)', 'nut.particles ( block=1)', 'nut.particles ( block=1)', 'p ( block=1)', 'p ( block=1)', 'p_rgh ( block=1)', 'p_rgh ( block=1)', 'T.air ( block=1)', 'T.air ( block=1)', 'T.particles ( block=1)', 'T.particles ( block=1)', 'Theta.particles ( block=1)', 'Theta.particles ( block=1)', 'U.air (0) ( block=1)', 'U.air (0) ( block=1)', 'U.air (1) ( block=1)', 'U.air (1) ( block=1)', 'U.air (2) ( block=1)', 'U.air (2) ( block=1)', 'U.air (Magnitude) ( block=1)', 'U.air (Magnitude) ( block=1)', 'U.particles (0) ( block=1)', 'U.particles (0) ( block=1)', 'U.particles (1) ( block=1)', 'U.particles (1) ( block=1)', 'U.particles (2) ( block=1)', 'U.particles (2) ( block=1)', 'U.particles (Magnitude) ( block=1)', 'U.particles (Magnitude) ( block=1)', 'X ( block=1)', 'X ( block=1)', 'Y ( block=1)', 'Y ( block=1)', 'Z ( block=1)', 'Z ( block=1)', 'N ( block=1)', 'N ( block=1)', 'Time ( block=1)', 'Time ( block=1)', 'vtkValidPointMask ( block=1)', 'vtkValidPointMask ( block=1)']
	plotDataOverTime1Display.SeriesColor = ['alpha.air ( block=1)', '0', '0', '0', 'alpha.particles ( block=1)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'alphat.particles ( block=1)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'nuFric.particles ( block=1)', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'nut.particles ( block=1)', '0.6', '0.3100022888532845', '0.6399938963912413', 'p ( block=1)', '1', '0.5000076295109483', '0', 'p_rgh ( block=1)', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'T.air ( block=1)', '0', '0', '0', 'T.particles ( block=1)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Theta.particles ( block=1)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'U.air (0) ( block=1)', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'U.air (1) ( block=1)', '0.6', '0.3100022888532845', '0.6399938963912413', 'U.air (2) ( block=1)', '1', '0.5000076295109483', '0', 'U.air (Magnitude) ( block=1)', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'U.particles (0) ( block=1)', '0', '0', '0', 'U.particles (1) ( block=1)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'U.particles (2) ( block=1)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'U.particles (Magnitude) ( block=1)', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'X ( block=1)', '0.6', '0.3100022888532845', '0.6399938963912413', 'Y ( block=1)', '1', '0.5000076295109483', '0', 'Z ( block=1)', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'N ( block=1)', '0', '0', '0', 'Time ( block=1)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'vtkValidPointMask ( block=1)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207']
	plotDataOverTime1Display.SeriesPlotCorner = ['alpha.air ( block=1)', '0', 'alpha.particles ( block=1)', '0', 'alphat.particles ( block=1)', '0', 'nuFric.particles ( block=1)', '0', 'nut.particles ( block=1)', '0', 'p ( block=1)', '0', 'p_rgh ( block=1)', '0', 'T.air ( block=1)', '0', 'T.particles ( block=1)', '0', 'Theta.particles ( block=1)', '0', 'U.air (0) ( block=1)', '0', 'U.air (1) ( block=1)', '0', 'U.air (2) ( block=1)', '0', 'U.air (Magnitude) ( block=1)', '0', 'U.particles (0) ( block=1)', '0', 'U.particles (1) ( block=1)', '0', 'U.particles (2) ( block=1)', '0', 'U.particles (Magnitude) ( block=1)', '0', 'X ( block=1)', '0', 'Y ( block=1)', '0', 'Z ( block=1)', '0', 'N ( block=1)', '0', 'Time ( block=1)', '0', 'vtkValidPointMask ( block=1)', '0']
	plotDataOverTime1Display.SeriesLabelPrefix = ''
	plotDataOverTime1Display.SeriesLineStyle = ['alpha.air ( block=1)', '1', 'alpha.particles ( block=1)', '1', 'alphat.particles ( block=1)', '1', 'nuFric.particles ( block=1)', '1', 'nut.particles ( block=1)', '1', 'p ( block=1)', '1', 'p_rgh ( block=1)', '1', 'T.air ( block=1)', '1', 'T.particles ( block=1)', '1', 'Theta.particles ( block=1)', '1', 'U.air (0) ( block=1)', '1', 'U.air (1) ( block=1)', '1', 'U.air (2) ( block=1)', '1', 'U.air (Magnitude) ( block=1)', '1', 'U.particles (0) ( block=1)', '1', 'U.particles (1) ( block=1)', '1', 'U.particles (2) ( block=1)', '1', 'U.particles (Magnitude) ( block=1)', '1', 'X ( block=1)', '1', 'Y ( block=1)', '1', 'Z ( block=1)', '1', 'N ( block=1)', '1', 'Time ( block=1)', '1', 'vtkValidPointMask ( block=1)', '1']
	plotDataOverTime1Display.SeriesLineThickness = ['alpha.air ( block=1)', '2', 'alpha.particles ( block=1)', '2', 'alphat.particles ( block=1)', '2', 'nuFric.particles ( block=1)', '2', 'nut.particles ( block=1)', '2', 'p ( block=1)', '2', 'p_rgh ( block=1)', '2', 'T.air ( block=1)', '2', 'T.particles ( block=1)', '2', 'Theta.particles ( block=1)', '2', 'U.air (0) ( block=1)', '2', 'U.air (1) ( block=1)', '2', 'U.air (2) ( block=1)', '2', 'U.air (Magnitude) ( block=1)', '2', 'U.particles (0) ( block=1)', '2', 'U.particles (1) ( block=1)', '2', 'U.particles (2) ( block=1)', '2', 'U.particles (Magnitude) ( block=1)', '2', 'X ( block=1)', '2', 'Y ( block=1)', '2', 'Z ( block=1)', '2', 'N ( block=1)', '2', 'Time ( block=1)', '2', 'vtkValidPointMask ( block=1)', '2']
	plotDataOverTime1Display.SeriesMarkerStyle = ['alpha.air ( block=1)', '0', 'alpha.particles ( block=1)', '0', 'alphat.particles ( block=1)', '0', 'nuFric.particles ( block=1)', '0', 'nut.particles ( block=1)', '0', 'p ( block=1)', '0', 'p_rgh ( block=1)', '0', 'T.air ( block=1)', '0', 'T.particles ( block=1)', '0', 'Theta.particles ( block=1)', '0', 'U.air (0) ( block=1)', '0', 'U.air (1) ( block=1)', '0', 'U.air (2) ( block=1)', '0', 'U.air (Magnitude) ( block=1)', '0', 'U.particles (0) ( block=1)', '0', 'U.particles (1) ( block=1)', '0', 'U.particles (2) ( block=1)', '0', 'U.particles (Magnitude) ( block=1)', '0', 'X ( block=1)', '0', 'Y ( block=1)', '0', 'Z ( block=1)', '0', 'N ( block=1)', '0', 'Time ( block=1)', '0', 'vtkValidPointMask ( block=1)', '0']
	plotDataOverTime1Display.SeriesMarkerSize = ['alpha.air ( block=1)', '4', 'alpha.particles ( block=1)', '4', 'alphat.particles ( block=1)', '4', 'nuFric.particles ( block=1)', '4', 'nut.particles ( block=1)', '4', 'p ( block=1)', '4', 'p_rgh ( block=1)', '4', 'T.air ( block=1)', '4', 'T.particles ( block=1)', '4', 'Theta.particles ( block=1)', '4', 'U.air (0) ( block=1)', '4', 'U.air (1) ( block=1)', '4', 'U.air (2) ( block=1)', '4', 'U.air (Magnitude) ( block=1)', '4', 'U.particles (0) ( block=1)', '4', 'U.particles (1) ( block=1)', '4', 'U.particles (2) ( block=1)', '4', 'U.particles (Magnitude) ( block=1)', '4', 'X ( block=1)', '4', 'Y ( block=1)', '4', 'Z ( block=1)', '4', 'N ( block=1)', '4', 'Time ( block=1)', '4', 'vtkValidPointMask ( block=1)', '4']

	# get layout
	layout1 = GetLayoutByName("Layout #1")

	quartileChartView1 = CreateView('QuartileChartView')

	# show data in view
	plotDataOverTime1Display = Show(fracao_massica_overtime, quartileChartView1, 'QuartileChartRepresentation')

	# trace defaults for the display properties.
	plotDataOverTime1Display.AttributeType = 'Row Data'
	plotDataOverTime1Display.UseIndexForXAxis = 0
	plotDataOverTime1Display.XArrayName = 'Time'
	plotDataOverTime1Display.SeriesVisibility = ['alpha.air ( block=1)', 'alpha.particles ( block=1)', 'alphat.particles ( block=1)', 'nuFric.particles ( block=1)', 'nut.particles ( block=1)', 'p ( block=1)', 'p_rgh ( block=1)', 'T.air ( block=1)', 'T.particles ( block=1)', 'Theta.particles ( block=1)', 'U.air (Magnitude) ( block=1)', 'U.particles (Magnitude) ( block=1)']
	plotDataOverTime1Display.SeriesLabel = ['alpha.air ( block=1)', 'alpha.air ( block=1)', 'alpha.particles ( block=1)', 'alpha.particles ( block=1)', 'alphat.particles ( block=1)', 'alphat.particles ( block=1)', 'nuFric.particles ( block=1)', 'nuFric.particles ( block=1)', 'nut.particles ( block=1)', 'nut.particles ( block=1)', 'p ( block=1)', 'p ( block=1)', 'p_rgh ( block=1)', 'p_rgh ( block=1)', 'T.air ( block=1)', 'T.air ( block=1)', 'T.particles ( block=1)', 'T.particles ( block=1)', 'Theta.particles ( block=1)', 'Theta.particles ( block=1)', 'U.air (0) ( block=1)', 'U.air (0) ( block=1)', 'U.air (1) ( block=1)', 'U.air (1) ( block=1)', 'U.air (2) ( block=1)', 'U.air (2) ( block=1)', 'U.air (Magnitude) ( block=1)', 'U.air (Magnitude) ( block=1)', 'U.particles (0) ( block=1)', 'U.particles (0) ( block=1)', 'U.particles (1) ( block=1)', 'U.particles (1) ( block=1)', 'U.particles (2) ( block=1)', 'U.particles (2) ( block=1)', 'U.particles (Magnitude) ( block=1)', 'U.particles (Magnitude) ( block=1)', 'X ( block=1)', 'X ( block=1)', 'Y ( block=1)', 'Y ( block=1)', 'Z ( block=1)', 'Z ( block=1)', 'N ( block=1)', 'N ( block=1)', 'Time ( block=1)', 'Time ( block=1)', 'vtkValidPointMask ( block=1)', 'vtkValidPointMask ( block=1)']
	plotDataOverTime1Display.SeriesColor = ['alpha.air ( block=1)', '0', '0', '0', 'alpha.particles ( block=1)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'alphat.particles ( block=1)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'nuFric.particles ( block=1)', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'nut.particles ( block=1)', '0.6', '0.3100022888532845', '0.6399938963912413', 'p ( block=1)', '1', '0.5000076295109483', '0', 'p_rgh ( block=1)', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'T.air ( block=1)', '0', '0', '0', 'T.particles ( block=1)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Theta.particles ( block=1)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'U.air (0) ( block=1)', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'U.air (1) ( block=1)', '0.6', '0.3100022888532845', '0.6399938963912413', 'U.air (2) ( block=1)', '1', '0.5000076295109483', '0', 'U.air (Magnitude) ( block=1)', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'U.particles (0) ( block=1)', '0', '0', '0', 'U.particles (1) ( block=1)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'U.particles (2) ( block=1)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'U.particles (Magnitude) ( block=1)', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'X ( block=1)', '0.6', '0.3100022888532845', '0.6399938963912413', 'Y ( block=1)', '1', '0.5000076295109483', '0', 'Z ( block=1)', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'N ( block=1)', '0', '0', '0', 'Time ( block=1)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'vtkValidPointMask ( block=1)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207']
	plotDataOverTime1Display.SeriesPlotCorner = ['alpha.air ( block=1)', '0', 'alpha.particles ( block=1)', '0', 'alphat.particles ( block=1)', '0', 'nuFric.particles ( block=1)', '0', 'nut.particles ( block=1)', '0', 'p ( block=1)', '0', 'p_rgh ( block=1)', '0', 'T.air ( block=1)', '0', 'T.particles ( block=1)', '0', 'Theta.particles ( block=1)', '0', 'U.air (0) ( block=1)', '0', 'U.air (1) ( block=1)', '0', 'U.air (2) ( block=1)', '0', 'U.air (Magnitude) ( block=1)', '0', 'U.particles (0) ( block=1)', '0', 'U.particles (1) ( block=1)', '0', 'U.particles (2) ( block=1)', '0', 'U.particles (Magnitude) ( block=1)', '0', 'X ( block=1)', '0', 'Y ( block=1)', '0', 'Z ( block=1)', '0', 'N ( block=1)', '0', 'Time ( block=1)', '0', 'vtkValidPointMask ( block=1)', '0']
	plotDataOverTime1Display.SeriesLabelPrefix = ''
	plotDataOverTime1Display.SeriesLineStyle = ['alpha.air ( block=1)', '1', 'alpha.particles ( block=1)', '1', 'alphat.particles ( block=1)', '1', 'nuFric.particles ( block=1)', '1', 'nut.particles ( block=1)', '1', 'p ( block=1)', '1', 'p_rgh ( block=1)', '1', 'T.air ( block=1)', '1', 'T.particles ( block=1)', '1', 'Theta.particles ( block=1)', '1', 'U.air (0) ( block=1)', '1', 'U.air (1) ( block=1)', '1', 'U.air (2) ( block=1)', '1', 'U.air (Magnitude) ( block=1)', '1', 'U.particles (0) ( block=1)', '1', 'U.particles (1) ( block=1)', '1', 'U.particles (2) ( block=1)', '1', 'U.particles (Magnitude) ( block=1)', '1', 'X ( block=1)', '1', 'Y ( block=1)', '1', 'Z ( block=1)', '1', 'N ( block=1)', '1', 'Time ( block=1)', '1', 'vtkValidPointMask ( block=1)', '1']
	plotDataOverTime1Display.SeriesLineThickness = ['alpha.air ( block=1)', '2', 'alpha.particles ( block=1)', '2', 'alphat.particles ( block=1)', '2', 'nuFric.particles ( block=1)', '2', 'nut.particles ( block=1)', '2', 'p ( block=1)', '2', 'p_rgh ( block=1)', '2', 'T.air ( block=1)', '2', 'T.particles ( block=1)', '2', 'Theta.particles ( block=1)', '2', 'U.air (0) ( block=1)', '2', 'U.air (1) ( block=1)', '2', 'U.air (2) ( block=1)', '2', 'U.air (Magnitude) ( block=1)', '2', 'U.particles (0) ( block=1)', '2', 'U.particles (1) ( block=1)', '2', 'U.particles (2) ( block=1)', '2', 'U.particles (Magnitude) ( block=1)', '2', 'X ( block=1)', '2', 'Y ( block=1)', '2', 'Z ( block=1)', '2', 'N ( block=1)', '2', 'Time ( block=1)', '2', 'vtkValidPointMask ( block=1)', '2']
	plotDataOverTime1Display.SeriesMarkerStyle = ['alpha.air ( block=1)', '0', 'alpha.particles ( block=1)', '0', 'alphat.particles ( block=1)', '0', 'nuFric.particles ( block=1)', '0', 'nut.particles ( block=1)', '0', 'p ( block=1)', '0', 'p_rgh ( block=1)', '0', 'T.air ( block=1)', '0', 'T.particles ( block=1)', '0', 'Theta.particles ( block=1)', '0', 'U.air (0) ( block=1)', '0', 'U.air (1) ( block=1)', '0', 'U.air (2) ( block=1)', '0', 'U.air (Magnitude) ( block=1)', '0', 'U.particles (0) ( block=1)', '0', 'U.particles (1) ( block=1)', '0', 'U.particles (2) ( block=1)', '0', 'U.particles (Magnitude) ( block=1)', '0', 'X ( block=1)', '0', 'Y ( block=1)', '0', 'Z ( block=1)', '0', 'N ( block=1)', '0', 'Time ( block=1)', '0', 'vtkValidPointMask ( block=1)', '0']
	plotDataOverTime1Display.SeriesMarkerSize = ['alpha.air ( block=1)', '4', 'alpha.particles ( block=1)', '4', 'alphat.particles ( block=1)', '4', 'nuFric.particles ( block=1)', '4', 'nut.particles ( block=1)', '4', 'p ( block=1)', '4', 'p_rgh ( block=1)', '4', 'T.air ( block=1)', '4', 'T.particles ( block=1)', '4', 'Theta.particles ( block=1)', '4', 'U.air (0) ( block=1)', '4', 'U.air (1) ( block=1)', '4', 'U.air (2) ( block=1)', '4', 'U.air (Magnitude) ( block=1)', '4', 'U.particles (0) ( block=1)', '4', 'U.particles (1) ( block=1)', '4', 'U.particles (2) ( block=1)', '4', 'U.particles (Magnitude) ( block=1)', '4', 'X ( block=1)', '4', 'Y ( block=1)', '4', 'Z ( block=1)', '4', 'N ( block=1)', '4', 'Time ( block=1)', '4', 'vtkValidPointMask ( block=1)', '4']

	# get layout
	layout1 = GetLayoutByName("Layout #1")

	# add view to a layout so it's visible in UI
	AssignViewToLayout(view=quartileChartView1, layout=layout1, hint=0)

	# Properties modified on plotDataOverTime1Display# add view to a layout so it's visible in UI
	AssignViewToLayout(view=quartileChartView1, layout=layout1, hint=0)

	# Properties modified on plotDataOverTime1DisplayplotDataOverTime1Display = Show(plotDataOverTime1, quartileChartView1, 'QuartileChartRepresentation')

	# trace defaults for the display properties.
	plotDataOverTime1Display.AttributeType = 'Row Data'
	plotDataOverTime1Display.UseIndexForXAxis = 0
	plotDataOverTime1Display.XArrayName = 'Time'
	plotDataOverTime1Display.SeriesVisibility = ['alpha.air ( block=1)', 'alpha.particles ( block=1)', 'alphat.particles ( block=1)', 'nuFric.particles ( block=1)', 'nut.particles ( block=1)', 'p ( block=1)', 'p_rgh ( block=1)', 'T.air ( block=1)', 'T.particles ( block=1)', 'Theta.particles ( block=1)', 'U.air (Magnitude) ( block=1)', 'U.particles (Magnitude) ( block=1)']
	plotDataOverTime1Display.SeriesLabel = ['alpha.air ( block=1)', 'alpha.air ( block=1)', 'alpha.particles ( block=1)', 'alpha.particles ( block=1)', 'alphat.particles ( block=1)', 'alphat.particles ( block=1)', 'nuFric.particles ( block=1)', 'nuFric.particles ( block=1)', 'nut.particles ( block=1)', 'nut.particles ( block=1)', 'p ( block=1)', 'p ( block=1)', 'p_rgh ( block=1)', 'p_rgh ( block=1)', 'T.air ( block=1)', 'T.air ( block=1)', 'T.particles ( block=1)', 'T.particles ( block=1)', 'Theta.particles ( block=1)', 'Theta.particles ( block=1)', 'U.air (0) ( block=1)', 'U.air (0) ( block=1)', 'U.air (1) ( block=1)', 'U.air (1) ( block=1)', 'U.air (2) ( block=1)', 'U.air (2) ( block=1)', 'U.air (Magnitude) ( block=1)', 'U.air (Magnitude) ( block=1)', 'U.particles (0) ( block=1)', 'U.particles (0) ( block=1)', 'U.particles (1) ( block=1)', 'U.particles (1) ( block=1)', 'U.particles (2) ( block=1)', 'U.particles (2) ( block=1)', 'U.particles (Magnitude) ( block=1)', 'U.particles (Magnitude) ( block=1)', 'X ( block=1)', 'X ( block=1)', 'Y ( block=1)', 'Y ( block=1)', 'Z ( block=1)', 'Z ( block=1)', 'N ( block=1)', 'N ( block=1)', 'Time ( block=1)', 'Time ( block=1)', 'vtkValidPointMask ( block=1)', 'vtkValidPointMask ( block=1)']
	plotDataOverTime1Display.SeriesColor = ['alpha.air ( block=1)', '0', '0', '0', 'alpha.particles ( block=1)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'alphat.particles ( block=1)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'nuFric.particles ( block=1)', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'nut.particles ( block=1)', '0.6', '0.3100022888532845', '0.6399938963912413', 'p ( block=1)', '1', '0.5000076295109483', '0', 'p_rgh ( block=1)', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'T.air ( block=1)', '0', '0', '0', 'T.particles ( block=1)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Theta.particles ( block=1)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'U.air (0) ( block=1)', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'U.air (1) ( block=1)', '0.6', '0.3100022888532845', '0.6399938963912413', 'U.air (2) ( block=1)', '1', '0.5000076295109483', '0', 'U.air (Magnitude) ( block=1)', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'U.particles (0) ( block=1)', '0', '0', '0', 'U.particles (1) ( block=1)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'U.particles (2) ( block=1)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'U.particles (Magnitude) ( block=1)', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'X ( block=1)', '0.6', '0.3100022888532845', '0.6399938963912413', 'Y ( block=1)', '1', '0.5000076295109483', '0', 'Z ( block=1)', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'N ( block=1)', '0', '0', '0', 'Time ( block=1)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'vtkValidPointMask ( block=1)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207']
	plotDataOverTime1Display.SeriesPlotCorner = ['alpha.air ( block=1)', '0', 'alpha.particles ( block=1)', '0', 'alphat.particles ( block=1)', '0', 'nuFric.particles ( block=1)', '0', 'nut.particles ( block=1)', '0', 'p ( block=1)', '0', 'p_rgh ( block=1)', '0', 'T.air ( block=1)', '0', 'T.particles ( block=1)', '0', 'Theta.particles ( block=1)', '0', 'U.air (0) ( block=1)', '0', 'U.air (1) ( block=1)', '0', 'U.air (2) ( block=1)', '0', 'U.air (Magnitude) ( block=1)', '0', 'U.particles (0) ( block=1)', '0', 'U.particles (1) ( block=1)', '0', 'U.particles (2) ( block=1)', '0', 'U.particles (Magnitude) ( block=1)', '0', 'X ( block=1)', '0', 'Y ( block=1)', '0', 'Z ( block=1)', '0', 'N ( block=1)', '0', 'Time ( block=1)', '0', 'vtkValidPointMask ( block=1)', '0']
	plotDataOverTime1Display.SeriesLabelPrefix = ''
	plotDataOverTime1Display.SeriesLineStyle = ['alpha.air ( block=1)', '1', 'alpha.particles ( block=1)', '1', 'alphat.particles ( block=1)', '1', 'nuFric.particles ( block=1)', '1', 'nut.particles ( block=1)', '1', 'p ( block=1)', '1', 'p_rgh ( block=1)', '1', 'T.air ( block=1)', '1', 'T.particles ( block=1)', '1', 'Theta.particles ( block=1)', '1', 'U.air (0) ( block=1)', '1', 'U.air (1) ( block=1)', '1', 'U.air (2) ( block=1)', '1', 'U.air (Magnitude) ( block=1)', '1', 'U.particles (0) ( block=1)', '1', 'U.particles (1) ( block=1)', '1', 'U.particles (2) ( block=1)', '1', 'U.particles (Magnitude) ( block=1)', '1', 'X ( block=1)', '1', 'Y ( block=1)', '1', 'Z ( block=1)', '1', 'N ( block=1)', '1', 'Time ( block=1)', '1', 'vtkValidPointMask ( block=1)', '1']
	plotDataOverTime1Display.SeriesLineThickness = ['alpha.air ( block=1)', '2', 'alpha.particles ( block=1)', '2', 'alphat.particles ( block=1)', '2', 'nuFric.particles ( block=1)', '2', 'nut.particles ( block=1)', '2', 'p ( block=1)', '2', 'p_rgh ( block=1)', '2', 'T.air ( block=1)', '2', 'T.particles ( block=1)', '2', 'Theta.particles ( block=1)', '2', 'U.air (0) ( block=1)', '2', 'U.air (1) ( block=1)', '2', 'U.air (2) ( block=1)', '2', 'U.air (Magnitude) ( block=1)', '2', 'U.particles (0) ( block=1)', '2', 'U.particles (1) ( block=1)', '2', 'U.particles (2) ( block=1)', '2', 'U.particles (Magnitude) ( block=1)', '2', 'X ( block=1)', '2', 'Y ( block=1)', '2', 'Z ( block=1)', '2', 'N ( block=1)', '2', 'Time ( block=1)', '2', 'vtkValidPointMask ( block=1)', '2']
	plotDataOverTime1Display.SeriesMarkerStyle = ['alpha.air ( block=1)', '0', 'alpha.particles ( block=1)', '0', 'alphat.particles ( block=1)', '0', 'nuFric.particles ( block=1)', '0', 'nut.particles ( block=1)', '0', 'p ( block=1)', '0', 'p_rgh ( block=1)', '0', 'T.air ( block=1)', '0', 'T.particles ( block=1)', '0', 'Theta.particles ( block=1)', '0', 'U.air (0) ( block=1)', '0', 'U.air (1) ( block=1)', '0', 'U.air (2) ( block=1)', '0', 'U.air (Magnitude) ( block=1)', '0', 'U.particles (0) ( block=1)', '0', 'U.particles (1) ( block=1)', '0', 'U.particles (2) ( block=1)', '0', 'U.particles (Magnitude) ( block=1)', '0', 'X ( block=1)', '0', 'Y ( block=1)', '0', 'Z ( block=1)', '0', 'N ( block=1)', '0', 'Time ( block=1)', '0', 'vtkValidPointMask ( block=1)', '0']
	plotDataOverTime1Display.SeriesMarkerSize = ['alpha.air ( block=1)', '4', 'alpha.particles ( block=1)', '4', 'alphat.particles ( block=1)', '4', 'nuFric.particles ( block=1)', '4', 'nut.particles ( block=1)', '4', 'p ( block=1)', '4', 'p_rgh ( block=1)', '4', 'T.air ( block=1)', '4', 'T.particles ( block=1)', '4', 'Theta.particles ( block=1)', '4', 'U.air (0) ( block=1)', '4', 'U.air (1) ( block=1)', '4', 'U.air (2) ( block=1)', '4', 'U.air (Magnitude) ( block=1)', '4', 'U.particles (0) ( block=1)', '4', 'U.particles (1) ( block=1)', '4', 'U.particles (2) ( block=1)', '4', 'U.particles (Magnitude) ( block=1)', '4', 'X ( block=1)', '4', 'Y ( block=1)', '4', 'Z ( block=1)', '4', 'N ( block=1)', '4', 'Time ( block=1)', '4', 'vtkValidPointMask ( block=1)', '4']

	# get layout
	layout1 = GetLayoutByName("Layout #1")

	# add view to a layout so it's visible in UI
	AssignViewToLayout(view=quartileChartView1, layout=layout1, hint=0)

	# Properties modified on plotDataOverTime1Display
	plotDataOverTime1Display.SeriesPlotCorner = ['N ( block=1)', '0', 'T.air ( block=1)', '0', 'T.particles ( block=1)', '0', 'Theta.particles ( block=1)', '0', 'Time ( block=1)', '0', 'U.air (0) ( block=1)', '0', 'U.air (1) ( block=1)', '0', 'U.air (2) ( block=1)', '0', 'U.air (Magnitude) ( block=1)', '0', 'U.particles (0) ( block=1)', '0', 'U.particles (1) ( block=1)', '0', 'U.particles (2) ( block=1)', '0', 'U.particles (Magnitude) ( block=1)', '0', 'X ( block=1)', '0', 'Y ( block=1)', '0', 'Z ( block=1)', '0', 'alpha.air ( block=1)', '0', 'alpha.particles ( block=1)', '0', 'alphat.particles ( block=1)', '0', 'nuFric.particles ( block=1)', '0', 'nut.particles ( block=1)', '0', 'p ( block=1)', '0', 'p_rgh ( block=1)', '0', 'vtkValidPointMask ( block=1)', '0']
	plotDataOverTime1Display.SeriesLineStyle = ['N ( block=1)', '1', 'T.air ( block=1)', '1', 'T.particles ( block=1)', '1', 'Theta.particles ( block=1)', '1', 'Time ( block=1)', '1', 'U.air (0) ( block=1)', '1', 'U.air (1) ( block=1)', '1', 'U.air (2) ( block=1)', '1', 'U.air (Magnitude) ( block=1)', '1', 'U.particles (0) ( block=1)', '1', 'U.particles (1) ( block=1)', '1', 'U.particles (2) ( block=1)', '1', 'U.particles (Magnitude) ( block=1)', '1', 'X ( block=1)', '1', 'Y ( block=1)', '1', 'Z ( block=1)', '1', 'alpha.air ( block=1)', '1', 'alpha.particles ( block=1)', '1', 'alphat.particles ( block=1)', '1', 'nuFric.particles ( block=1)', '1', 'nut.particles ( block=1)', '1', 'p ( block=1)', '1', 'p_rgh ( block=1)', '1', 'vtkValidPointMask ( block=1)', '1']
	plotDataOverTime1Display.SeriesLineThickness = ['N ( block=1)', '2', 'T.air ( block=1)', '2', 'T.particles ( block=1)', '2', 'Theta.particles ( block=1)', '2', 'Time ( block=1)', '2', 'U.air (0) ( block=1)', '2', 'U.air (1) ( block=1)', '2', 'U.air (2) ( block=1)', '2', 'U.air (Magnitude) ( block=1)', '2', 'U.particles (0) ( block=1)', '2', 'U.particles (1) ( block=1)', '2', 'U.particles (2) ( block=1)', '2', 'U.particles (Magnitude) ( block=1)', '2', 'X ( block=1)', '2', 'Y ( block=1)', '2', 'Z ( block=1)', '2', 'alpha.air ( block=1)', '2', 'alpha.particles ( block=1)', '2', 'alphat.particles ( block=1)', '2', 'nuFric.particles ( block=1)', '2', 'nut.particles ( block=1)', '2', 'p ( block=1)', '2', 'p_rgh ( block=1)', '2', 'vtkValidPointMask ( block=1)', '2']
	plotDataOverTime1Display.SeriesMarkerStyle = ['N ( block=1)', '0', 'T.air ( block=1)', '0', 'T.particles ( block=1)', '0', 'Theta.particles ( block=1)', '0', 'Time ( block=1)', '0', 'U.air (0) ( block=1)', '0', 'U.air (1) ( block=1)', '0', 'U.air (2) ( block=1)', '0', 'U.air (Magnitude) ( block=1)', '0', 'U.particles (0) ( block=1)', '0', 'U.particles (1) ( block=1)', '0', 'U.particles (2) ( block=1)', '0', 'U.particles (Magnitude) ( block=1)', '0', 'X ( block=1)', '0', 'Y ( block=1)', '0', 'Z ( block=1)', '0', 'alpha.air ( block=1)', '0', 'alpha.particles ( block=1)', '0', 'alphat.particles ( block=1)', '0', 'nuFric.particles ( block=1)', '0', 'nut.particles ( block=1)', '0', 'p ( block=1)', '0', 'p_rgh ( block=1)', '0', 'vtkValidPointMask ( bfoamlock=1)', '0']
	plotDataOverTime1Display.SeriesMarkerSize = ['N ( block=1)', '4', 'T.air ( block=1)', '4', 'T.particles ( block=1)', '4', 'Theta.particles ( block=1)', '4', 'Time ( block=1)', '4', 'U.air (0) ( block=1)', '4', 'U.air (1) ( block=1)', '4', 'U.air (2) ( block=1)', '4', 'U.air (Magnitude) ( block=1)', '4', 'U.particles (0) ( block=1)', '4', 'U.particles (1) ( block=1)', '4', 'U.particles (2) ( block=1)', '4', 'U.particles (Magnitude) ( block=1)', '4', 'X ( block=1)', '4', 'Y ( block=1)', '4', 'Z ( block=1)', '4', 'alpha.air ( block=1)', '4', 'alpha.particles ( block=1)', '4', 'alphat.particles ( block=1)', '4', 'nuFric.particles ( block=1)', '4', 'nut.particles ( block=1)', '4', 'p ( block=1)', '4', 'p_rgh ( block=1)', '4', 'vtkValidPointMask ( block=1)', '4']


	# Properties modified on plotDataOverTime1Display
	plotDataOverTime1Display.SeriesVisibility = ['alpha.air ( block=1)', 'alpha.particles ( block=1)', 'alphat.particles ( block=1)', 'N ( block=1)', 'nuFric.particles ( block=1)', 'nut.particles ( block=1)', 'p ( block=1)', 'p_rgh ( block=1)', 'T.air ( block=1)', 'T.particles ( block=1)', 'Theta.particles ( block=1)', 'Time ( block=1)', 'U.air (0) ( block=1)', 'U.air (1) ( block=1)', 'U.air (2) ( block=1)', 'U.air (Magnitude) ( block=1)', 'U.particles (0) ( block=1)', 'U.particles (1) ( block=1)', 'U.particles (2) ( block=1)', 'U.particles (Magnitude) ( block=1)', 'vtkValidPointMask ( block=1)', 'X ( block=1)', 'Y ( block=1)', 'Z ( block=1)']

	# Properties modified on plotDataOverTime1Display
	plotDataOverTime1Display.SeriesVisibility = []

	# Properties modified on plotDataOverTime1Display
	plotDataOverTime1Display.SeriesVisibility = ['alpha.particles ( block=1)']

	# Properties modified on plotDataOverTime1Display
	plotDataOverTime1Display.ShowQuartiles = 0

	# Properties modified on plotDataOverTime1Display
	plotDataOverTime1Display.ShowRanges = 0

	# set active source
	SetActiveSource(slice1)

	# create a new 'Plot Data Over Time'
	pressao_overflow_overtime = PlotDataOverTime(registrationName='PlotDataOverTime2', Input=slice1)

	# show data in view
	plotDataOverTime2Display = Show(pressao_overflow_overtime, quartileChartView1, 'QuartileChartRepresentation')

	# trace defaults for the display properties.
	plotDataOverTime2Display.AttributeType = 'Row Data'
	plotDataOverTime2Display.UseIndexForXAxis = 0
	plotDataOverTime2Display.XArrayName = 'Time'
	plotDataOverTime2Display.SeriesVisibility = ['alpha.air ( block=1)', 'alpha.particles ( block=1)', 'alphat.particles ( block=1)', 'nuFric.particles ( block=1)', 'nut.particles ( block=1)', 'p ( block=1)', 'p_rgh ( block=1)', 'T.air ( block=1)', 'T.particles ( block=1)', 'Theta.particles ( block=1)', 'U.air (Magnitude) ( block=1)', 'U.particles (Magnitude) ( block=1)']
	plotDataOverTime2Display.SeriesColor = ['alpha.air ( block=1)', '0', '0', '0', 'alpha.particles ( block=1)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'alphat.particles ( block=1)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'nuFric.particles ( block=1)', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'nut.particles ( block=1)', '0.6', '0.3100022888532845', '0.6399938963912413', 'p ( block=1)', '1', '0.5000076295109483', '0', 'p_rgh ( block=1)', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'T.air ( block=1)', '0', '0', '0', 'T.particles ( block=1)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Theta.particles ( block=1)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'U.air (0) ( block=1)', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'U.air (1) ( block=1)', '0.6', '0.3100022888532845', '0.6399938963912413', 'U.air (2) ( block=1)', '1', '0.5000076295109483', '0', 'U.air (Magnitude) ( block=1)', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'U.particles (0) ( block=1)', '0', '0', '0', 'U.particles (1) ( block=1)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'U.particles (2) ( block=1)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'U.particles (Magnitude) ( block=1)', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'X ( block=1)', '0.6', '0.3100022888532845', '0.6399938963912413', 'Y ( block=1)', '1', '0.5000076295109483', '0', 'Z ( block=1)', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'N ( block=1)', '0', '0', '0', 'Time ( block=1)', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'vtkValidPointMask ( block=1)', '0.220004577706569', '0.4899977111467155', '0.7199969481956207']
	plotDataOverTime2Display.SeriesPlotCorner = ['alpha.air ( block=1)', '0', 'alpha.particles ( block=1)', '0', 'alphat.particles ( block=1)', '0', 'nuFric.particles ( block=1)', '0', 'nut.particles ( block=1)', '0', 'p ( block=1)', '0', 'p_rgh ( block=1)', '0', 'T.air ( block=1)', '0', 'T.particles ( block=1)', '0', 'Theta.particles ( block=1)', '0', 'U.air (0) ( block=1)', '0', 'U.air (1) ( block=1)', '0', 'U.air (2) ( block=1)', '0', 'U.air (Magnitude) ( block=1)', '0', 'U.particles (0) ( block=1)', '0', 'U.particles (1) ( block=1)', '0', 'U.particles (2) ( block=1)', '0', 'U.particles (Magnitude) ( block=1)', '0', 'X ( block=1)', '0', 'Y ( block=1)', '0', 'Z ( block=1)', '0', 'N ( block=1)', '0', 'Time ( block=1)', '0', 'vtkValidPointMask ( block=1)', '0']
	plotDataOverTime2Display.SeriesLabelPrefix = ''
	plotDataOverTime2Display.SeriesLineStyle = ['alpha.air ( block=1)', '1', 'alpha.particles ( block=1)', '1', 'alphat.particles ( block=1)', '1', 'nuFric.particles ( block=1)', '1', 'nut.particles ( block=1)', '1', 'p ( block=1)', '1', 'p_rgh ( block=1)', '1', 'T.air ( block=1)', '1', 'T.particles ( block=1)', '1', 'Theta.particles ( block=1)', '1', 'U.air (0) ( block=1)', '1', 'U.air (1) ( block=1)', '1', 'U.air (2) ( block=1)', '1', 'U.air (Magnitude) ( block=1)', '1', 'U.particles (0) ( block=1)', '1', 'U.particles (1) ( block=1)', '1', 'U.particles (2) ( block=1)', '1', 'U.particles (Magnitude) ( block=1)', '1', 'X ( block=1)', '1', 'Y ( block=1)', '1', 'Z ( block=1)', '1', 'N ( block=1)', '1', 'Time ( block=1)', '1', 'vtkValidPointMask ( block=1)', '1']
	plotDataOverTime2Display.SeriesLineThickness = ['alpha.air ( block=1)', '2', 'alpha.particles ( block=1)', '2', 'alphat.particles ( block=1)', '2', 'nuFric.particles ( block=1)', '2', 'nut.particles ( block=1)', '2', 'p ( block=1)', '2', 'p_rgh ( block=1)', '2', 'T.air ( block=1)', '2', 'T.particles ( block=1)', '2', 'Theta.particles ( block=1)', '2', 'U.air (0) ( block=1)', '2', 'U.air (1) ( block=1)', '2', 'U.air (2) ( block=1)', '2', 'U.air (Magnitude) ( block=1)', '2', 'U.particles (0) ( block=1)', '2', 'U.particles (1) ( block=1)', '2', 'U.particles (2) ( block=1)', '2', 'U.particles (Magnitude) ( block=1)', '2', 'X ( block=1)', '2', 'Y ( block=1)', '2', 'Z ( block=1)', '2', 'N ( block=1)', '2', 'Time ( block=1)', '2', 'vtkValidPointMask ( block=1)', '2']

	plotDataOverTime2Display.SeriesMarkerSize = ['alpha.air ( block=1)', '4', 'alpha.particles ( block=1)', '4', 'alphat.particles ( block=1)', '4', 'nuFric.particles ( block=1)', '4', 'nut.particles ( block=1)', '4', 'p ( block=1)', '4', 'p_rgh ( block=1)', '4', 'T.air ( block=1)', '4', 'T.particles ( block=1)', '4', 'Theta.particles ( block=1)', '4', 'U.air (0) ( block=1)', '4', 'U.air (1) ( block=1)', '4', 'U.air (2) ( block=1)', '4', 'U.air (Magnitude) ( block=1)', '4', 'U.particles (0) ( block=1)', '4', 'U.particles (1) ( block=1)', '4', 'U.particles (2) ( block=1)', '4', 'U.particles (Magnitude) ( block=1)', '4', 'X ( block=1)', '4', 'Y ( block=1)', '4', 'Z ( block=1)', '4', 'N ( block=1)', '4', 'Time ( block=1)', '4', 'vtkValidPointMask ( block=1)', '4']

	

	# Properties modified on plotDataOverTime2Display
	plotDataOverTime2Display.SeriesPlotCorner = ['N ( block=1)', '0', 'T.air ( block=1)', '0', 'T.particles ( block=1)', '0', 'Theta.particles ( block=1)', '0', 'Time ( block=1)', '0', 'U.air (0) ( block=1)', '0', 'U.air (1) ( block=1)', '0', 'U.air (2) ( block=1)', '0', 'U.air (Magnitude) ( block=1)', '0', 'U.particles (0) ( block=1)', '0', 'U.particles (1) ( block=1)', '0', 'U.particles (2) ( block=1)', '0', 'U.particles (Magnitude) ( block=1)', '0', 'X ( block=1)', '0', 'Y ( block=1)', '0', 'Z ( block=1)', '0', 'alpha.air ( block=1)', '0', 'alpha.particles ( block=1)', '0', 'alphat.particles ( block=1)', '0', 'nuFric.particles ( block=1)', '0', 'nut.particles ( block=1)', '0', 'p ( block=1)', '0', 'p_rgh ( block=1)', '0', 'vtkValidPointMask ( block=1)', '0']
	plotDataOverTime2Display.SeriesLineStyle = ['N ( block=1)', '1', 'T.air ( block=1)', '1', 'T.particles ( block=1)', '1', 'Theta.particles ( block=1)', '1', 'Time ( block=1)', '1', 'U.air (0) ( block=1)', '1', 'U.air (1) ( block=1)', '1', 'U.air (2) ( block=1)', '1', 'U.air (Magnitude) ( block=1)', '1', 'U.particles (0) ( block=1)', '1', 'U.particles (1) ( block=1)', '1', 'U.particles (2) ( block=1)', '1', 'U.particles (Magnitude) ( block=1)', '1', 'X ( block=1)', '1', 'Y ( block=1)', '1', 'Z ( block=1)', '1', 'alpha.air ( block=1)', '1', 'alpha.particles ( block=1)', '1', 'alphat.particles ( block=1)', '1', 'nuFric.particles ( block=1)', '1', 'nut.particles ( block=1)', '1', 'p ( block=1)', '1', 'p_rgh ( block=1)', '1', 'vtkValidPointMask ( block=1)', '1']
	plotDataOverTime2Display.SeriesLineThickness = ['N ( block=1)', '2', 'T.air ( block=1)', '2', 'T.particles ( block=1)', '2', 'Theta.particles ( block=1)', '2', 'Time ( block=1)', '2', 'U.air (0) ( block=1)', '2', 'U.air (1) ( block=1)', '2', 'U.air (2) ( block=1)', '2', 'U.air (Magnitude) ( block=1)', '2', 'U.particles (0) ( block=1)', '2', 'U.particles (1) ( block=1)', '2', 'U.particles (2) ( block=1)', '2', 'U.particles (Magnitude) ( block=1)', '2', 'X ( block=1)', '2', 'Y ( block=1)', '2', 'Z ( block=1)', '2', 'alpha.air ( block=1)', '2', 'alpha.particles ( block=1)', '2', 'alphat.particles ( block=1)', '2', 'nuFric.particles ( block=1)', '2', 'nut.particles ( block=1)', '2', 'p ( block=1)', '2', 'p_rgh ( block=1)', '2', 'vtkValidPointMask ( block=1)', '2']
	plotDataOverTime2Display.SeriesMarkerStyle = ['N ( block=1)', '0', 'T.air ( block=1)', '0', 'T.particles ( block=1)', '0', 'Theta.particles ( block=1)', '0', 'Time ( block=1)', '0', 'U.air (0) ( block=1)', '0', 'U.air (1) ( block=1)', '0', 'U.air (2) ( block=1)', '0', 'U.air (Magnitude) ( block=1)', '0', 'U.particles (0) ( block=1)', '0', 'U.particles (1) ( block=1)', '0', 'U.particles (2) ( block=1)', '0', 'U.particles (Magnitude) ( block=1)', '0', 'X ( block=1)', '0', 'Y ( block=1)', '0', 'Z ( block=1)', '0', 'alpha.air ( block=1)', '0', 'alpha.particles ( block=1)', '0', 'alphat.particles ( block=1)', '0', 'nuFric.particles ( block=1)', '0', 'nut.particles ( block=1)', '0', 'p ( block=1)', '0', 'p_rgh ( block=1)', '0', 'vtkValidPointMask ( block=1)', '0']
	plotDataOverTime2Display.SeriesMarkerSize = ['N ( block=1)', '4', 'T.air ( block=1)', '4', 'T.particles ( block=1)', '4', 'Theta.particles ( block=1)', '4', 'Time ( block=1)', '4', 'U.air (0) ( block=1)', '4', 'U.air (1) ( block=1)', '4', 'U.air (2) ( block=1)', '4', 'U.air (Magnitude) ( block=1)', '4', 'U.particles (0) ( block=1)', '4', 'U.particles (1) ( block=1)', '4', 'U.particles (2) ( block=1)', '4', 'U.particles (Magnitude) ( block=1)', '4', 'X ( block=1)', '4', 'Y ( block=1)', '4', 'Z ( block=1)', '4', 'alpha.air ( block=1)', '4', 'alpha.particles ( block=1)', '4', 'alphat.particles ( block=1)', '4', 'nuFric.particles ( block=1)', '4', 'nut.particles ( block=1)', '4', 'p ( block=1)', '4', 'p_rgh ( block=1)', '4', 'vtkValidPointMask ( block=1)', '4']

	# Properties modified on plotDataOverTime2Display
	plotDataOverTime2Display.SeriesVisibility = ['alpha.air ( block=1)', 'alpha.particles ( block=1)', 'alphat.particles ( block=1)', 'N ( block=1)', 'nuFric.particles ( block=1)', 'nut.particles ( block=1)', 'p ( block=1)', 'p_rgh ( block=1)', 'T.air ( block=1)', 'T.particles ( block=1)', 'Theta.particles ( block=1)', 'Time ( block=1)', 'U.air (0) ( block=1)', 'U.air (1) ( block=1)', 'U.air (2) ( block=1)', 'U.air (Magnitude) ( block=1)', 'U.particles (0) ( block=1)', 'U.particles (1) ( block=1)', 'U.particles (2) ( block=1)', 'U.particles (Magnitude) ( block=1)', 'vtkValidPointMask ( block=1)', 'X ( block=1)', 'Y ( block=1)', 'Z ( block=1)']

	# Properties modified on plotDataOverTime2Displaypress
	plotDataOverTime2Display.SeriesVisibility = []

	# Properties modified on plotDataOverTime2Display
	plotDataOverTime2Display.SeriesVisibility = ['p ( block=1)']

	# hide data in view
	Hide(fracao_massica_overtime, quartileChartView1)

	# Properties modified on plotDataOverTime2Display
	plotDataOverTime2Display.ShowQuartiles = 0

	# Properties modified on plotDataOverTime2Display
	plotDataOverTime2Display.ShowRanges = 0

	# set active source
	SetActiveSource(fracao_massica_overtime)

	# set active source
	SetActiveSource(pressao_overflow_overtime)

	# set active source
	SetActiveSource(fracao_massica_overtime)

	# hide data in view
	Hide(pressao_overflow_overtime, quartileChartView1)

	# set active source
	SetActiveSource(fracao_massica_overtime)

	# show data in view
	plotDataOverTime1Display = Show(fracao_massica_overtime, quartileChartView1, 'QuartileChartRepresentation')


	# save screenshot
	name_fracao = root_folder + str(i) + '/' + str(i) + '_fracao.png' 
	SaveScreenshot(name_fracao, quartileChartView1, ImageResolution=[1920, 1080])

	# set active source
	SetActiveSource(pressao_overflow_overtime)

	# show data in view
	plotDataOverTime2Display = Show(pressao_overflow_overtime, quartileChartView1, 'QuartileChartRepresentation')

	# hide data in view
	Hide(fracao_massica_overtime, quartileChartView1)



	# save screenshot
	name_pressao = root_folder + str(i) + '/' + str(i) + '_pressao.png' 
	SaveScreenshot(name_pressao, quartileChartView1, ImageResolution=[1920, 1080])

	# set active source
	SetActiveSource(pressao_overflow_overtime)

