import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = "/home/n002/Documents/multi_cyclone/"
diametro_overflow = [60,60,60,60,60,60,60,60,100,100,100,100,100,100,100,100,40,120,80,80,80,80,80,80,80,80,80] #mm
diametro_underflow = [40, 40, 40, 40, 80, 80, 80, 80, 40, 40, 40, 40, 80, 80, 80, 80, 60, 60, 20, 100, 60, 60 , 60, 60, 60 , 60, 60] #mm

for i in range(1,28,1):
    if i!=11:
        try:
            print(f"INICIANDO SIMULAÇÃO {i}")

            path_inlet = path+f'{i}/dados_inlet_{i}.csv'
            path_overflow = path+f'{i}/dados_overflow_{i}.csv'
            path_underflow = path+f'{i}/dados_underflow_{i}.csv'

            inlet_df = pd.read_csv(path_inlet)
            overflow_df = pd.read_csv(path_overflow)
            underflow_df = pd.read_csv(path_underflow)

            dp = inlet_df.loc[:,'avg(p)'].values - overflow_df.loc[:,'avg(p)']

            area_inlet = np.pi*(40**2)/4 #mm²
            area_overflow = np.pi*(np.array(diametro_overflow)**2)/4 #mm²
            area_underflow = np.pi*(np.array(diametro_underflow)**2)/4 #mm²
            

            #vMassica_inlet_p = ((area_inlet/(10**6))*20)*800*0.01 #kg/s
            #vMassica_overflow_p = ((area_overflow[i-1]/(10**6))*overflow_df.loc[:,'avg(alpha.particles)']*overflow_df.loc[:,'avg(U.particles (Magnitude))'])*800 #kg/s
            #vMassica_underflow_p = ((area_underflow[i-1]/(10**6))*underflow_df.loc[:,'avg(alpha.particles)']*underflow_df.loc[:,'avg(U.particles (Magnitude))'])*800 #kg/s
            #mass_balance_p = vMassica_inlet_p-vMassica_overflow_p-vMassica_underflow_p

            #vMassica_inlet_f = ((area_inlet/(10**6))*20)*1*0.99 #kg/s
            #vMassica_overflow_f = ((area_overflow[i-1]/(10**6))*overflow_df.loc[:,'avg(alpha.air)']*overflow_df.loc[:,'avg(U.air (Magnitude))'])*1 #kg/s
            #vMassica_underflow_f = ((area_underflow[i-1]/(10**6))*underflow_df.loc[:,'avg(alpha.air)']*underflow_df.loc[:,'avg(U.air (Magnitude))'])*1 #kg/s
            #mass_balance_f = vMassica_inlet_f-vMassica_overflow_f-vMassica_underflow_f
            

            vMassica_inlet_p = (((area_inlet/(10**6))*20)*inlet_df.loc[:,'avg(U.particles (Magnitude))'])*800 #kg/s
            vMassica_overflow_p = ((area_overflow[i-1]/(10**6))*overflow_df.loc[:,'avg(U.particles (Magnitude))'])*800 #kg/s
            vMassica_underflow_p = ((area_underflow[i-1]/(10**6))*underflow_df.loc[:,'avg(U.particles (Magnitude))'])*800 #kg/s
            mass_balance_p = vMassica_inlet_p-vMassica_overflow_p-vMassica_underflow_p

            vMassica_inlet_f = (((area_inlet/(10**6))*20)*inlet_df.loc[:,'avg(U.air (Magnitude))'])*1  #kg/s
            vMassica_overflow_f = ((area_overflow[i-1]/(10**6))*overflow_df.loc[:,'avg(U.air (Magnitude))'])*1 #kg/s
            vMassica_underflow_f = ((area_underflow[i-1]/(10**6))*underflow_df.loc[:,'avg(U.air (Magnitude))'])*1 #kg/s
            mass_balance_f = vMassica_inlet_f-vMassica_overflow_f-vMassica_underflow_f


            S1 = 1 - (vMassica_overflow_p/vMassica_inlet_p)
            S2 = 1 - (vMassica_underflow_p/vMassica_inlet_p)
        
            path_VR = path+f"VR_{i}.csv"
            variaveis_respostas_df = pd.DataFrame({'dp':dp,'S1':S1, 'S2':S2,'vMassica_inlet_f':vMassica_inlet_f,'vMassica_overflow_f':vMassica_overflow_f,'vMassica_underflow_f':vMassica_underflow_f,'mass_balance_f':mass_balance_f,'vMassica_inlet_p':vMassica_inlet_p,'vMassica_overflow_p':vMassica_overflow_p,'vMassica_underflow_p':vMassica_underflow_p,'mass_balance_p':mass_balance_p})
            variaveis_respostas_df.to_csv(path_VR,index=False)
        except:
            print(f"Simulação {i} deu erro")
