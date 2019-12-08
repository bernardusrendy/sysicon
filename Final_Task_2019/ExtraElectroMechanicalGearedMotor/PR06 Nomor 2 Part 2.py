#!/usr/bin/env python
# coding: utf-8

# <h1 align="center"> PR#06 Dinamika Sistem dan Simulasi Nomor 2 Part II</h1>

# <h3>Nama Anggota:</h3>
# <body>
#     <ul>
#         <li>M. Iqbal Anggoro A. (13317007)</li>
#         <li>Devina Caroline T. (13317039)</li>
#         <li>Bernardus Rendy (13317041)</li>
#     </ul>
#     Pengerjaan utama dilakukan oleh Bernardus Rendy
# </body>

# In[7]:


import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact_manual , HBox, VBox, Label, Layout
import ipywidgets as widgets


# ### Deskripsi Sistem
# <img src="./1.jpg" style="width:30%">
# <img src="./3.jpg" style="width:50%">
# 
# #### 1. Input
# effort $e_v$, asumsi input merupakan sinyal step
# 
# #### 2. Output
# $\omega_a$ dan $\omega_b$
# 
# #### 3. Parameter
# $R_a,L_a,K_g,K_1,K_m,N_1,N_2,J_2,c,b_r$

# In[33]:


#DEFINISI WIDGETS PARAMETER
Ra_slider = widgets.FloatSlider(
    value=19.90,
    min=0.1,
    max=20.0,
    step=0.1,
    description='$R_a (\\Omega)$',
    layout=Layout(width='80%', height='50px'),
    style={'description_width': '200px'},
)
La_slider = widgets.FloatSlider(
    value=19.90,
    min=0.1,
    max=20.0,
    step=0.1,
    description='$L_a (H)$',
    layout=Layout(width='80%', height='50px'),
    style={'description_width': '200px'},
)
Kg_slider = widgets.FloatSlider(
    value=19.90,
    min=0.1,
    max=20.0,
    step=0.1,
    description='$K_g (\\frac {V}{rad.s^-1})$',
    layout=Layout(width='80%', height='50px'),
    style={'description_width': '200px'},
)
K1_slider = widgets.FloatSlider(
    value=19.90,
    min=0.1,
    max=20.0,
    step=0.1,
    description='$K_1 (\\frac {V}{V})$',
    layout=Layout(width='80%', height='50px'),
    style={'description_width': '200px'},
)
Km_slider = widgets.FloatSlider(
    value=19.90,
    min=0.1,
    max=20.0,
    step=0.1,
    description='$K_m (\\frac {N.m}{A})$',
    layout=Layout(width='80%', height='50px'),
    style={'description_width': '200px'},
)
N1_slider = widgets.FloatSlider(
    value=19.90,
    min=0.1,
    max=20.0,
    step=0.1,
    description='$N1 Gear Ratio$',
    layout=Layout(width='80%', height='50px'),
    style={'description_width': '200px'},
)
N2_slider = widgets.FloatSlider(
    value=19.90,
    min=0.1,
    max=20.0,
    step=0.1,
    description='$N2 Gear Ratio$',
    layout=Layout(width='80%', height='50px'),
    style={'description_width': '200px'},
)
J2_slider = widgets.FloatSlider(
    value=19.90,
    min=0.1,
    max=20.0,
    step=0.1,
    description='$J_2 (\\frac {Nm}{rad.s^-2})$',
    layout=Layout(width='80%', height='50px'),
    style={'description_width': '200px'},
)
c_slider = widgets.FloatSlider(
    value=19.90,
    min=0.1,
    max=20.0,
    step=0.1,
    description='$c (\\frac {Nm}{rad.s^-1})$',
    layout=Layout(width='80%', height='50px'),
    style={'description_width': '200px'},
)
br_slider = widgets.FloatSlider(
    value=19.90,
    min=0.1,
    max=20.0,
    step=0.1,
    description='$b_r (\\frac {Nm}{rad.s^-1})$',
    layout=Layout(width='80%', height='50px'),
    style={'description_width': '200px'},
)
grid_button = widgets.ToggleButton(
    value=True,
    description='Grid',
    icon='check',
    layout=Layout(width='20%', height='50px',margin='10px 10px 10px 350px'),
    style={'description_width': '200px'},
)


# In[50]:


def plot_w1w2(Ra,La,Kg,K1,Km,N1,N2,J2,c,br,grid):
    # Pembuatan model transfer function
    A= [[(-Ra/La),(-Kg/La)],[Km/((N2/N1)**2 * J2),(-c+br)]]
    B= [[(K1/La)],[0]]
    C= [[0,1],[0,(N2/N1)]]
    D= [[0],[0]]
    sys1=signal.StateSpace(A,B,C,D)
    t1,y1=signal.step(sys1)
    plt.title("Plot $\\omega_1$ dan $\\omega_2$")
    plt.plot(t1,y1)
ui_em = widgets.VBox([Ra_slider,La_slider,Kg_slider,K1_slider,Km_slider,N1_slider,N2_slider,J2_slider,c_slider,br_slider,grid_button])
out_em = widgets.interactive_output(plot_w1w2, {'Ra':Ra_slider,'La':La_slider,'Kg':Kg_slider,'K1':K1_slider,'Km':Km_slider,'N1':N1_slider,'N2':N2_slider,'J2':J2_slider,'c':c_slider,'br':br_slider, 'grid':grid_button})


# In[51]:


display(ui_em,out_em)

