#MassBalance

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

rho_p = 800
rho_f = 1
for i in range(1,28,1):

    path_inlet = f"/home/n002/Documents/multi_cyclone/{i}/postProcessing/patchFlowRate(name=inlet,patch=inlet)/0/surfaceFieldValue.dat"
    path_overflow = f"/home/n002/Documents/multi_cyclone/{i}/postProcessing/patchFlowRate(name=overflow,patch=overflow)/0/surfaceFieldValue.dat"
    path_underflow = f"/home/n002/Documents/multi_cyclone/{i}/postProcessing/patchFlowRate(name=underflow,patch=underflow)/0/surfaceFieldValue.dat"
    path_inlet_p = f"/home/n002/Documents/multi_cyclone/{i}/postProcessing/patchAverage(alpha.particles,name=inlet,patch=inlet)/0/surfaceFieldValue.dat"
    path_overflow_p = f"/home/n002/Documents/multi_cyclone/{i}/postProcessing/patchAverage(alpha.particles,name=overflow,patch=overflow)/0/surfaceFieldValue.dat"
    path_underflow_p = f"/home/n002/Documents/multi_cyclone/{i}/postProcessing/patchAverage(alpha.particles,name=underflow,patch=underflow)/0/surfaceFieldValue.dat"

    inlet_df = pd.read_csv(path_inlet,sep='\t', skiprows=3)
    underflow_df = pd.read_csv(path_underflow,sep='\t', skiprows=3)
    overflow_df = pd.read_csv(path_overflow,sep='\t', skiprows=3)
    inlet_p_df = pd.read_csv(path_inlet_p,sep='\t', skiprows=3)
    underflow_p_df = pd.read_csv(path_underflow_p,sep='\t', skiprows=3)
    overflow_p_df = pd.read_csv(path_overflow_p,sep='\t', skiprows=3)
    
    volume_inlet = inlet_df.loc[:,'sum(phi)'].abs()
    volume_overflow = overflow_df.loc[:,'sum(phi)'].abs()
    volume_underflow = underflow_df.loc[:,'sum(phi)'].abs()
    volume_balance_phi = volume_inlet - volume_overflow - volume_underflow

    mass_fraction_inlet = ((inlet_p_df.loc[:,'areaAverage(alpha.particles)'])*rho_p/100)/((inlet_p_df.loc[:,'areaAverage(alpha.particles)'])*rho_p/100+rho_f*(1-(inlet_p_df.loc[:,'areaAverage(alpha.particles)'])/100))
    mass_fraction_overflow = ((overflow_p_df.loc[:,'areaAverage(alpha.particles)'])*rho_p)/((overflow_p_df.loc[:,'areaAverage(alpha.particles)'])*rho_p+rho_f*(1-(overflow_p_df.loc[:,'areaAverage(alpha.particles)'])))
    mass_fraction_underflow = ((underflow_p_df.loc[:,'areaAverage(alpha.particles)'])*rho_p)/((underflow_p_df.loc[:,'areaAverage(alpha.particles)'])*rho_p+rho_f*(1-(underflow_p_df.loc[:,'areaAverage(alpha.particles)'])))
    
    #print(mass_fraction_inlet.iat[-1])
    #print(mass_fraction_overflow.iat[-1])
    #print(mass_fraction_underflow.iat[-1])

    volume_particle_inlet = np.abs(inlet_df.loc[:,'sum(phi)'])*(inlet_p_df.loc[:,'areaAverage(alpha.particles)'])
    volume_particle_overflow = np.abs(overflow_df.loc[:,'sum(phi)'])*(overflow_p_df.loc[:,'areaAverage(alpha.particles)'])
    volume_particle_underflow = np.abs(underflow_df.loc[:,'sum(phi)'])*(underflow_p_df.loc[:,'areaAverage(alpha.particles)'])
    volume_balance_phi_p = volume_particle_inlet - volume_particle_overflow - volume_particle_underflow 

    rho_mix_inlet = rho_p*inlet_p_df.loc[:,'areaAverage(alpha.particles)'] + rho_f*(1-inlet_p_df.loc[:,'areaAverage(alpha.particles)'])
    rho_mix_overflow = rho_p*overflow_p_df.loc[:,'areaAverage(alpha.particles)'] + rho_f*(1-overflow_p_df.loc[:,'areaAverage(alpha.particles)'])
    rho_mix_underflow = rho_p*underflow_p_df.loc[:,'areaAverage(alpha.particles)'] + rho_f*(1-underflow_p_df.loc[:,'areaAverage(alpha.particles)'])


    mass_particle_inlet = volume_inlet*mass_fraction_inlet*rho_p
    #print(mass_particle_inlet)
    mass_air_inlet = volume_inlet*(1-mass_fraction_inlet)*rho_f

    mass_particle_overflow = volume_overflow*mass_fraction_overflow*rho_p
    mass_particle_underflow = volume_underflow*mass_fraction_underflow*rho_p
    mass_air_inlet_mean = mass_air_inlet.mean()
    mass_particle_inlet_mean = mass_particle_inlet.mean()
    mass_particle_overflow_mean = mass_particle_overflow.mean()
    mass_particle_underflow_mean = mass_particle_underflow.mean()


    #print(mass_particle_underflow.iat[-1])
    mass_balance_phi_p = mass_particle_inlet - mass_particle_overflow - mass_particle_underflow 
    volume_balance_phi_movel = volume_balance_phi.rolling(10).mean()
    mass_balance_phi_p_movel = mass_balance_phi_p.rolling(10).mean()

    #print(volume_balance_phi_movel)
    #print(mass_balance_phi_p)
    #print(np.abs(inlet_df.loc[:,'sum(phi)'])*(inlet_p_df.loc[:,'areaAverage(alpha.particles)']))
    #plt.plot(volume_balance_phi_movel)
    #plt.plot(mass_balance_phi_p_movel)
    #plt.show()
    #print(underflow_df.loc[:,'sum(phi)'])
    EffSep_m = 100*mass_particle_underflow_mean/(mass_particle_inlet_mean+mass_air_inlet_mean) 
    print(f'eff simulação {i}',EffSep_m)