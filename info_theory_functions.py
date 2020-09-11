import numpy as np
import scipy.stats as ss
import scipy.optimize as opt


def entropy(p) :
    the_entropy = ss.entropy( p , base = 2 )
    return the_entropy


def entropy_length_two(x) :
    the_entropy_length_two = entropy( [ x , 1.0 - x ] )
    return the_entropy_length_two


def entropy_length_two__inverse_lower_branch(y) :
    
    if y < 0.0 or y > 1.0 :
        x = np.nan
        
    elif y <= 0.0 :
        x = 0.0
        
    elif y >= 1.0 :
        x = 0.5
        
    else :
        f = lambda s : entropy_length_two(s) - y
        x = opt.bisect( f = f , a = 0.0 , b = 0.5 )
    
    return x


def prescribed_igr_fn101( g , a , b , c0 ) :
    ha  = entropy_length_two(a)
    hc0 = entropy_length_two(c0)
    y = (  ( 1.0 - g ) * ha - ( 1.0 - b ) * hc0 ) / b
    c1 = entropy_length_two__inverse_lower_branch(y)
    return c1