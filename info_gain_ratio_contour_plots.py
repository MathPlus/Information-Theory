import numpy as np
from info_theory_functions import prescribed_igr_fn101
import matplotlib.pyplot as plt

dirname_fig = 'info_gain_ratio_contour_plots'

plt.rcParams['font.weight']        = 'bold'
plt.rcParams['figure.titleweight'] = 'bold'
plt.rcParams['axes.titleweight']   = 'bold'
plt.rcParams['axes.labelweight']   = 'bold'
plt.rcParams['axes.grid']          = True
fontsize = 12

list_a = [ 0.02 , 0.1 , 0.25 , 0.5 ]
list_b = [ 0.05 , 0.5 ]
list_g = [ 0.1 , 0.25 , 0.5 , 0.75 , 0.9 ]

list_c0 = np.linspace( 0.0 , 0.5 , 51 ).tolist()

list_color = [ 'red' , 'magenta' , 'green' , 'blue' , 'black' ]

assert len(list_g) == len(list_color)

n = 2 * len(list_c0) - 1

label_x = 'c0'
label_y = 'c1'

for b in list_b :
    for a in list_a :
        
        label_title = 'a = %s , b = %s' % ( a , b )
        filename_fig = '%s/%s .png' % ( dirname_fig , label_title )
        fig , ax = plt.subplots()
        plt.title( label_title )
        
        for j, g in enumerate(list_g) :
            
            x = [ np.nan for _ in range(n) ]
            y1 = x.copy()
            y2 = x.copy()
            
            for i, c0 in enumerate(list_c0) :
                c1 = prescribed_igr_fn101( g , a , b , c0 )
                if not np.isnan(c1) :
                    x[i]   = c0
                    y1[i]  = c1
                    y2[i]  = 1.0 - c1
                    ii     = n - 1 - i
                    x[ii]  = 1.0 - x[i]
                    y1[ii] = y1[i]
                    y2[ii] = y2[i]
                    
            color = list_color[j]
            label_plot = 'g = %s' % g
            plt.plot( x , y1 , color = color , label = label_plot )
            plt.plot( x , y2 , color = color )
            plt.xlim(0.0,1.0)
            plt.ylim(0.0,1.0)
            plt.tick_params( axis = 'both' , which = 'major' )
            plt.xlabel( label_x , fontsize = fontsize )
            plt.ylabel( label_y , fontsize = fontsize )
        
        ax.legend( loc = 'lower left' )
        fig.savefig( filename_fig , dpi = fig.dpi )
       #plt.close(fig)
