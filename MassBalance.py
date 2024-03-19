#MassBalance

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path_inlet = "/home/n002/Documents/multi_cyclone/027/postProcessing/inletphiMassFlowYourPatch/6.2/surfaceFieldValue.dat"
path_overflow = "/home/n002/Documents/multi_cyclone/027/postProcessing/overflowphiMassFlowYourPatch/6.2/surfaceFieldValue.dat"
path_underflow = "/home/n002/Documents/multi_cyclone/027/postProcessing/underflowphiMassFlowYourPatch/6.2/surfaceFieldValue.dat"

inlet_df = pd.read_csv(path_inlet,sep='\t', skiprows=3)
underflow_df = pd.read_csv(path_overflow,sep='\t', skiprows=3)
overflow_df = pd.read_csv(path_underflow,sep='\t', skiprows=3)
print(inlet_df)

mass_balance_phi = np.abs(inlet_df.loc[:,'sum(phi)']) - np.abs(overflow_df.loc[:,'sum(phi)']) - np.abs(underflow_df.loc[:,'sum(phi)'])
mass_balance_phiParticles = np.abs(inlet_df.loc[:,'sum(phi.particles)']) - np.abs(overflow_df.loc[:,'sum(phi.particles)']) - np.abs(underflow_df.loc[:,'sum(phi.particles)'])
mass_balance_phiAir = np.abs(inlet_df.loc[:,'sum(phi.air)']) - np.abs(overflow_df.loc[:,'sum(phi.air)']) - np.abs(underflow_df.loc[:,'sum(phi.air)'])
mass_balance_alphaRhoPhi = np.abs(inlet_df.loc[:,'sum(alphaRhoPhi)']) - np.abs(overflow_df.loc[:,'sum(alphaRhoPhi)']) - np.abs(underflow_df.loc[:,'sum(alphaRhoPhi)']) 
mass_balance_alphaRhoPhiParticles = np.abs(inlet_df.loc[:,'sum(alphaRhoPhi.particles)']) - np.abs(overflow_df.loc[:,'sum(alphaRhoPhi.particles)']) - np.abs(underflow_df.loc[:,'sum(alphaRhoPhi.particles)'])
mass_balance_alphaRhoPhiAir = np.abs(inlet_df.loc[:,'sum(alphaRhoPhi.air)']) - np.abs(overflow_df.loc[:,'sum(alphaRhoPhi.air)']) - np.abs(underflow_df.loc[:,'sum(alphaRhoPhi.air)'])

print(mass_balance_phi)
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
"""""
path_inlet = path+f'{i}/dados_inlet_{i}.csv'
path_overflow = path+f'{i}/dados_overflow_{i}.csv'
path_underflow = path+f'{i}/dados_underflow_{i}.csv'

inlet_df = pd.read_csv(path_inlet)
overflow_df = pd.read_csv(path_overflow)
underflow_df = pd.read_csv(path_underflow)

"""""