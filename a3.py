# a3.py
#Michael Wang mgw55
#Priscilla Wong pw274
#10/10/2014

""" Functions for Assignment A3"""
import colormodel
import math

def complement_rgb(rgb):
    """Returns: the complement of color rgb.
    
    Precondition: rgb is an RGB object"""
    # We asserted this precondition for you.  You do not need to do anything here.
    assert (type(rgb) == colormodel.RGB), 'Value '+ `rgb`+' is not a RGB object'
    

    red = 255 - rgb.red
    green = 255 - rgb.green
    blue = 255 - rgb.blue
    return colormodel.RGB(red, green, blue)


def truncate5(value):
    """Returns: value, as a string, using exactly 5 characters.
    
    The truncated value will have one of the forms:
       ddd.d      Example:  360.1
       dd.dd      Example:  29.53
       d.ddd      Examples: 4.003,  0.001,  and 0.000
    
    Precondition: value is a number (int or float), 0 <= value <= 999."""
    # To get the desired output, do the following
    #   1. Make sure value is a float.  If it is not, convert it to one.
    #   1. If value < 0.001, set value to 0.
    #      This prevents value appearing in scientific notation, e.g. 1.5E-6.
    #   2. Convert value to a string s, in the usual way. Note that s is guaranteed to
    #      have at least three chars: a decimal point and a digit on either side of it.
    #      Therefore, the simplest thing to do as s is being constructed is to make
    #      sure s has at least 5 chars by appending "00" after the decimal point.
    #   3. Return the first five characters of s.
    
    # ASSERT PRECONDITIONS
    assert 0<= value <= 999.
    assert type(value) == int or float
    if type(value)==int:
        value = float(value)
    if value < 0.001:
        value = 0.0
    s = str(value)
    s = s + '00'
    return s[:5]
    

def round5(value):
    """ Returns: value, as a string, but expand or round to be (if necessary) 
    exactly 5 characters.
    
    Examples:
       Round 1.3546  to  1.355.
       Round 1.3544  to  1.354.
       Round 21.9954 to  22.00.
       Round 21.994  to  21.99.
       Round 130.59  to  130.6.
       Round 130.54  to  130.5.
       Round 1       to  1.000.
    
    Precondition: value is a number (int or float), 0 <= value <= 360."""
  
  
    #
    # MAKE SURE THAT VALUE IS A FLOAT BEFORE USING THE BUILT-IN round() FUNCTION
    # If it is not a float convert it to one with the float() function.
    #
    # Obviously, you want to use the built-in function round().  However, 
    # remember that the rounding takes place at a different place depending on
    # how big value is. Look at the examples in the specification.
    
    # ASSERT PRECONDITIONS
    assert type(value)==int or float
    assert 0<= value <=360
    
    value = float(value)
    q = str(value)  
    if len(q) < 5:
        value = float(value)
        return truncate5(value)    
    if len(q) > 5:
        decimal = q.find('.')
        e = 4 - decimal
        value = round(value, e)
        if len(str(value)) < 5:
            value = float(value)
            r = str(value)
            r = r + '00'
            return r[:5]
        return str(value)
    if len(q)== 5:
        return q
        
        
    # STUB: Replace this return statement


def round5_cmyk(cmyk):
    """Returns: String representation of cmyk in the form "(C, M, Y, K)".
    
    In the output, each of C, M, Y, and K should be exactly 5 characters long.
    Hence the output of this function is not the same as str(cmyk)
    
    Precondition: cmyk is an CMYK object."""
    # STUB: Replace this return statement
    c = round5(cmyk.cyan)
    m = round5(cmyk.magenta)
    y = round5(cmyk.yellow)
    k = round5(cmyk.black)
    #return ( '(' + str(colormodel.CMYK(c))+ ', ' str(colormodel.CMYK(cmyk.magenta)) + ', ' str(colormodel.CMYK(cmyk.yellow)) + ', ' str(colormodel.CMYK(cmyk.black))+ ')'))
    #return ( '(' + str(colormodel.CMYK(c))+ ', ' str(colormodel.CMYK(m)) + ', ' str(colormodel.CMYK(y)) + ', ' str(colormodel.CMYK(b))+ ')'))
    #return ( '(' + str((c))+ ', ' str((m)) + ', ' str((y)) + ', ' str((b))+ ')'))
    return '(' + str(c) + ', ' + str(m) + ', ' + str(y) + ', ' + str(k) + ')'


def round5_hsv(hsv):
    """Returns: String representation of hsv in the form "(H, S, V)".
    
    In the output, each of H, S, and V should be exactly 5 characters long.
    Hence the output of this function is not the same as str(hsv)
    
    Precondition: hsv is an HSV object."""
    # ASSERT PRECONDITIONS
    assert type(hsv) == colormodel.HSV
    h = round5(hsv.hue)
    s = round5(hsv.saturation)
    v = round5(hsv.value)
    # STUB: Replace this return statement
    return '(' + str(h) + ', ' + str(s) + ', ' + str(v) + ')'



def rgb_to_cmyk(rgb):
    """Returns: color rgb in space CMYK, with the most black possible.
    
    Formulae from en.wikipedia.org/wiki/CMYK_color_model.
    
    Precondition: rgb is an RGB object"""
    # ASSERT PRECONDITIONS
    assert type(rgb) == colormodel.RGB
    # STUB: Replace this return statement
    Cx = 1 - (rgb.red/255.0)
    Mx = 1 - (rgb.green/255.0)
    Yx= 1 - (rgb.blue/255.0)
    if Cx == Mx == Yx == 1:
        return colormodel.CMYK(0,0,0,100.0)
    else:
        K = min(Cx,Mx,Yx)
        C = (Cx - K)/(1-K)
        M = (Mx - K)/(1-K)
        Y = (Yx - K)/(1-K)
        return colormodel.CMYK(100.0*C, 100.0*M, 100.0*Y, 100.0*K)


def cmyk_to_rgb(cmyk):
    """Returns : color CMYK in space RGB.
    
    Formulae from en.wikipedia.org/wiki/CMYK_color_model.
    
    Precondition: cmyk is an CMYK object."""
    # ASSERT PRECONDITIONS
    assert type(cmyk) == colormodel.CMYK
    # STUB: Replace this return statement
    #print cmyk.cyan
    C = cmyk.cyan/100.0
    #print C
    M = cmyk.magenta/100.0
    Y = cmyk.yellow/100.0
    K = cmyk.black/100.0
    if C == M == Y == K == 0:
       return colormodel.RGB(255,255,255)
    R = int(round((1-C)*(1-K)*255))
    #print R
    G = int(round((1-M)*(1-K)*255))
    B = int(round((1-Y)*(1-K)*255))
    return colormodel.RGB( R, G, B)

def rgb_to_hsv(rgb):
    """Return: color rgb in HSV color space.
    
    Formulae from wikipedia.org/wiki/HSV_color_space.
    
    Precondition: rgb is an RGB object"""
    # ASSERT PRECONDITIONS
    assert type(rgb) == colormodel.RGB
    R = rgb.red/255.0
    G = rgb.green/255.0
    B = rgb.blue/255.0
    MAX = max(R, G, B)
    MIN = min(R, G, B)
    
    
    
    if MAX == MIN:
        H = 0
    elif MAX == R and G>= B:
        H = 60.0*(G-B)/(MAX-MIN)
    elif MAX == R and G< B:
        H = 60.0*(G-B)/(MAX-MIN) + 360.0
    elif MAX == G:
        H = 60.0 * (B - R) / (MAX - MIN) + 120.0
    elif MAX == B:
        H = 60.0 * (R - G) / (MAX - MIN) + 240.0
    if MAX == 0:
        S = 0
    else:
        S = 1 - MIN/MAX
    V = MAX
        
    return colormodel.HSV(float(round5(H)), float(round5(S)), float(round5(V)))
    

  


def hsv_to_rgb(hsv):
    """Returns: color in RGB color space.
    
    Formulae from http://en.wikipedia.org/wiki/HSV_color_space.
    
    Precondition: hsv is an HSV object."""
    # ASSERT PRECONDITIONS
    
    # STUB: Replace this return statement
    #return None
    assert type(hsv) == colormodel.HSV
    """input type was not valid, input must be an HSV object"""
    
    
    H = hsv.hue
    S = hsv.saturation
    V = hsv.value
    Hi = math.floor(H/60)
    f = H/60 - Hi
    p = V*(1-S)
    q = V*(1-f*S)
    t = V*(1-(1-f)*S)
    
    if Hi == 0:
        R = V
        G = t
        B = p
    if Hi == 1:
        R = q
        G = V
        B = p
    if Hi == 2:
        R = p
        G = V
        B = t
    if Hi == 3:
        R = p
        G = q
        B = V
    if Hi == 4:
        R = t
        G = p
        B = V
    if Hi == 5:
        R = V
        G = p
        B = q
        
    #R = int(255.0) * int(round(R))
                         #, 1))
    #G = int(255.0) * int(round(G))
                               #, 3))
    #B = int(255.0) * int(round(B))
                         #, 3))
    
    return colormodel.RGB((int(round(255*R))), (int(round(255*G))), (int(round(255*B))))
    
    
    