#MassBalance

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def desagregar_vetor_velocidade(df):
    for v_name in ['areaAverage(U.air)','areaAverage(U.particles)']:

        V = df.iloc[:,2].apply(lambda u: u[1:-1].split())

        V_X = []
        V_Y = []
        V_Z = []
        for i in range(len(df)):
            V_X.append(float(V[i][0]))
            V_Y.append(float(V[i][1]))
            V_Z.append(float(V[i][2]))
        V_X = np.array(V_X)
        V_Y = np.array(V_Y)
        V_Z = np.array(V_Z)

        df[v_name+'_X'] = V_X
        df[v_name+'_Y'] = V_Y
        df[v_name+'_Z'] = V_Z

    return df

path_inlet = "/home/n002/Documents/multi_cyclone/027/postProcessing/patchAverage(patch=inlet,fields=(pU.airU.particlesalpha.particlesalpha.air))/6.2/surfaceFieldValue.dat"
path_overflow = "/home/n002/Documents/multi_cyclone/027/postProcessing/patchAverage(patch=overflow,fields=(pU.airU.particlesalpha.particlesalpha.air))/6.2/surfaceFieldValue.dat"
path_underflow = "/home/n002/Documents/multi_cyclone/027/postProcessing/patchAverage(patch=underflow,fields=(pU.airU.particlesalpha.particlesalpha.air))/6.2/surfaceFieldValue.dat"

inlet_df = pd.read_csv(path_inlet,sep='\t', skiprows=3)
underflow_df = pd.read_csv(path_underflow,sep='\t', skiprows=3)
overflow_df = pd.read_csv(path_overflow,sep='\t', skiprows=3)

area_inlet = float(pd.read_csv(path_inlet,sep='\t', skiprows=2,nrows=1,header=None).values[0][0].split()[-1])
area_undeflow = float(pd.read_csv(path_overflow,sep='\t', skiprows=2,nrows=1,header=None).values[0][0].split()[-1])
area_overflow = float(pd.read_csv(path_underflow,sep='\t', skiprows=2,nrows=1,header=None).values[0][0].split()[-1])

inlet_df = desagregar_vetor_velocidade(inlet_df)
overflow_df = desagregar_vetor_velocidade(overflow_df)
underflow_df = desagregar_vetor_velocidade(underflow_df)

inlet_df['Uparticles_mag'] = np.sqrt(inlet_df.iloc[:,9]**2 + inlet_df.iloc[:,10]**2 + inlet_df.iloc[:,11]**2)
inlet_df['Uair_mag'] = np.sqrt(inlet_df.iloc[:,6]**2 + inlet_df.iloc[:,7]**2 + inlet_df.iloc[:,8]**2)

overflow_df['Uparticles_mag'] = np.sqrt(overflow_df.iloc[:,9]**2 + overflow_df.iloc[:,10]**2 + overflow_df.iloc[:,11]**2)
overflow_df['Uair_mag'] = np.sqrt(overflow_df.iloc[:,6]**2 + overflow_df.iloc[:,7]**2 + overflow_df.iloc[:,8]**2)

underflow_df['Uparticles_mag'] = np.sqrt(underflow_df.iloc[:,9]**2 + underflow_df.iloc[:,10]**2 + underflow_df.iloc[:,11]**2)
underflow_df['Uair_mag'] = np.sqrt(underflow_df.iloc[:,6]**2 + underflow_df.iloc[:,7]**2 + underflow_df.iloc[:,8]**2)

inlet_df['alpha.particles_massico'] = inlet_df['areaAverage(alpha.particles)']*800/(800*inlet_df['areaAverage(alpha.particles)'] + (1-inlet_df['areaAverage(alpha.particles)']))
overflow_df['alpha.particles_massico'] = overflow_df['areaAverage(alpha.particles)']*800/(800*overflow_df['areaAverage(alpha.particles)'] + (1-overflow_df['areaAverage(alpha.particles)']))
underflow_df['alpha.particles_massico'] = underflow_df['areaAverage(alpha.particles)']*800/(800*underflow_df['areaAverage(alpha.particles)'] + (1-underflow_df['areaAverage(alpha.particles)']))

inlet_df['alpha.air_massico'] = inlet_df['areaAverage(alpha.air)']*800/(800*inlet_df['areaAverage(alpha.air)'] + (1-inlet_df['areaAverage(alpha.air)']))
overflow_df['alpha.air_massico'] = overflow_df['areaAverage(alpha.air)']*800/(800*overflow_df['areaAverage(alpha.air)'] + (1-overflow_df['areaAverage(alpha.air)']))
underflow_df['alpha.air_massico'] = underflow_df['areaAverage(alpha.air)']*800/(800*underflow_df['areaAverage(alpha.air)'] + (1-underflow_df['areaAverage(alpha.air)']))

inlet_df['vMassico.particles'] = area_inlet*inlet_df['Uparticles_mag']*inlet_df['alpha.particles_massico']*800
overflow_df['vMassico.particles'] = area_overflow*overflow_df['Uparticles_mag']*overflow_df['alpha.particles_massico']*800
underflow_df['vMassico.particles'] = area_undeflow*underflow_df['Uparticles_mag']*underflow_df['alpha.particles_massico']*800

inlet_df['vMassico.air'] = area_inlet*inlet_df['Uair_mag']*inlet_df['alpha.air_massico']
overflow_df['vMassico.air'] = area_overflow*overflow_df['Uair_mag']*overflow_df['alpha.air_massico']
underflow_df['vMassico.air'] = area_undeflow*underflow_df['Uair_mag']*underflow_df['alpha.air_massico']


print((inlet_df['vMassico.particles'].abs() - overflow_df['vMassico.particles'] - underflow_df['vMassico.particles'])*100/inlet_df['vMassico.particles'] )
print((inlet_df['vMassico.air'] - overflow_df['vMassico.air'] - underflow_df['vMassico.air'])*100/inlet_df['vMassico.air'] )

fig,ax = plt.subplots(1,1,figsize=(16,9))
ax.plot((inlet_df['vMassico.particles'].abs() - overflow_df['vMassico.particles'] - underflow_df['vMassico.particles'])*100/inlet_df['vMassico.particles'])
plt.show()
'''print(mass_balance_phi)
print(mass_balance_phiParticles)
print(mass_balance_phiAir)
print('==================')
print(mass_balance_alphaRhoPhi)
print('==================')
print(mass_balance_alphaRhoPhiParticles)
print(mass_balance_alphaRhoPhiAir)

fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3)
fig.suptitle('Mass Balance')
ax1.plot(inlet_df.iloc[:,0],mass_balance_phi)
ax2.plot(inlet_df.iloc[:,0],mass_balance_phiParticles)
ax3.plot(inlet_df.iloc[:,0],mass_balance_phiAir)
ax4.plot(inlet_df.iloc[:,0],mass_balance_alphaRhoPhi)
ax5.plot(inlet_df.iloc[:,0],mass_balance_alphaRhoPhiParticles)
ax6.plot(inlet_df.iloc[:,0],mass_balance_alphaRhoPhiAir)
plt.show()

path_inlet = path+f'{i}/dados_inlet_{i}.csv'
path_overflow = path+f'{i}/dados_overflow_{i}.csv'
path_underflow = path+f'{i}/dados_underflow_{i}.csv'

inlet_df = pd.read_csv(path_inlet)
overflow_df = pd.read_csv(path_overflow)
underflow_df = pd.read_csv(path_underflow)'''

