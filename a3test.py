# a3test.py
# YOUR NAME(S) AND NETID(S) HERE
#Michael Wang mgw55
#Priscilla Wong pw274
# DATE COMPLETED HERE
#10/10/2014

""" Unit Test for Assignment A3"""
import colormodel
import cornelltest
import a3

def test_complement():
    """Test function complement"""
    cornelltest.assert_equals(colormodel.RGB(255-250, 255-0, 255-71), 
            a3.complement_rgb(colormodel.RGB(250, 0, 71)))
    
    # Add another test
    cornelltest.assert_equals(colormodel.RGB(254, 175, 42), 
            a3.complement_rgb(colormodel.RGB(1, 80, 213)))


def test_truncate5():
    """Test function truncate5"""
    cornelltest.assert_equals('130.5',  a3.truncate5(130.59))
    cornelltest.assert_equals('130.5',  a3.truncate5(130.54))
    cornelltest.assert_equals('100.0',  a3.truncate5(100))
    cornelltest.assert_equals('99.56',  a3.truncate5(99.566))
    cornelltest.assert_equals('99.99',  a3.truncate5(99.99))
    cornelltest.assert_equals('99.99',  a3.truncate5(99.995))
    cornelltest.assert_equals('21.99',  a3.truncate5(21.99575))
    cornelltest.assert_equals('21.99',  a3.truncate5(21.994))
    cornelltest.assert_equals('10.01',  a3.truncate5(10.013567))
    cornelltest.assert_equals('10.00',  a3.truncate5(10.000000005))
    cornelltest.assert_equals('9.999',  a3.truncate5(9.9999))
    cornelltest.assert_equals('9.999',  a3.truncate5(9.9993))
    cornelltest.assert_equals('1.354',  a3.truncate5(1.3546))
    cornelltest.assert_equals('1.354',  a3.truncate5(1.3544))
    cornelltest.assert_equals('0.045',  a3.truncate5(.0456))
    cornelltest.assert_equals('0.045',  a3.truncate5(.0453))
    cornelltest.assert_equals('0.005',  a3.truncate5(.0056))
    cornelltest.assert_equals('0.001',  a3.truncate5(.0013))
    cornelltest.assert_equals('0.000',  a3.truncate5(.0004))
    cornelltest.assert_equals('0.000',  a3.truncate5(.0009999))


def test_round5():
    """Test function round5"""
    cornelltest.assert_equals('130.6',  a3.round5(130.59))
    cornelltest.assert_equals('130.5',  a3.round5(130.54))
    cornelltest.assert_equals('100.0',  a3.round5(100))
    cornelltest.assert_equals('99.57',  a3.round5(99.566))
    cornelltest.assert_equals('99.99',  a3.round5(99.99))
    cornelltest.assert_equals('100.0',  a3.round5(99.995))
    cornelltest.assert_equals('22.00',  a3.round5(21.99575))
    cornelltest.assert_equals('21.99',  a3.round5(21.994))
    cornelltest.assert_equals('10.01',  a3.round5(10.013567))
    cornelltest.assert_equals('10.00',  a3.round5(10.000000005))
    cornelltest.assert_equals('10.00',  a3.round5(9.9999))
    cornelltest.assert_equals('9.999',  a3.round5(9.9993))
    cornelltest.assert_equals('1.355',  a3.round5(1.3546))
    cornelltest.assert_equals('1.354',  a3.round5(1.3544))
    cornelltest.assert_equals('0.046',  a3.round5(.0456))
    cornelltest.assert_equals('0.045',  a3.round5(.0453))
    cornelltest.assert_equals('0.006',  a3.round5(.0056))
    cornelltest.assert_equals('0.001',  a3.round5(.0013))
    cornelltest.assert_equals('0.000',  a3.round5(.0004))
    cornelltest.assert_equals('0.001',  a3.round5(.0009999))


def test_round5_color():
    """Test the round5 functions for cmyk and hsv."""
    # Tests for round5_cmyk (add one more)
    cornelltest.assert_equals('(98.45, 25.36, 72.80, 25.00)',
            a3.round5_cmyk(colormodel.CMYK(98.448, 25.362, 72.8, 25.0)));
    cornelltest.assert_equals('(30.64, 89.03, 3.090, 26.90)',
            a3.round5_cmyk(colormodel.CMYK(30.643, 89.029, 3.0900, 26.901)))
    # Tests for round5_hsv (add two)
    cornelltest.assert_equals('(300.0, 0.123, 0.576)',
            a3.round5_hsv(colormodel.HSV(300.0001, 0.12321, 0.5759)))
    cornelltest.assert_equals('(125.4, 0.875, 0.537)',
            a3.round5_hsv(colormodel.HSV(125.433, 0.8748, 0.53741)))


def test_rgb_to_cmyk():
    """Test rgb_to_cmyk"""
    rgb = colormodel.RGB(255, 255, 255);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('0.000', a3.round5(cmyk.cyan))
    cornelltest.assert_equals('0.000', a3.round5(cmyk.magenta))
    cornelltest.assert_equals('0.000', a3.round5(cmyk.yellow))
    cornelltest.assert_equals('0.000', a3.round5(cmyk.black))
    
    rgb = colormodel.RGB(0, 0, 0);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('0.000', a3.round5(cmyk.cyan))
    cornelltest.assert_equals('0.000', a3.round5(cmyk.magenta))
    cornelltest.assert_equals('0.000', a3.round5(cmyk.yellow))
    cornelltest.assert_equals('100.0', a3.round5(cmyk.black))
        
    rgb = colormodel.RGB(217, 43, 164);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('0.000', a3.round5(cmyk.cyan))
    cornelltest.assert_equals('80.18', a3.round5(cmyk.magenta))
    cornelltest.assert_equals('24.42', a3.round5(cmyk.yellow))
    cornelltest.assert_equals('14.90', a3.round5(cmyk.black))
    
    rgb = colormodel.RGB(175, 234, 18);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('25.21', a3.round5(cmyk.cyan))
    cornelltest.assert_equals('0.000', a3.round5(cmyk.magenta))
    cornelltest.assert_equals('92.31', a3.round5(cmyk.yellow))
    cornelltest.assert_equals('8.235', a3.round5(cmyk.black))
    
    rgb = colormodel.RGB(15, 5, 75);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornelltest.assert_equals('80.00', a3.round5(cmyk.cyan))
    cornelltest.assert_equals('93.33', a3.round5(cmyk.magenta))
    cornelltest.assert_equals('0.000', a3.round5(cmyk.yellow))
    cornelltest.assert_equals('70.59', a3.round5(cmyk.black))


def test_cmyk_to_rgb():
    """Test translation function cmyk_to_rgb"""
    cmyk = colormodel.CMYK(0,0,0,0)
    rgb = a3.cmyk_to_rgb(cmyk)
    cornelltest.assert_equals(255, rgb.red)
    cornelltest.assert_equals(255, rgb.green)
    cornelltest.assert_equals(255, rgb.blue)
    
    cmyk = colormodel.CMYK(15.00, 32.00, 85.00, 6.000)
    rgb = a3.cmyk_to_rgb(cmyk)
    cornelltest.assert_equals(204, rgb.red)
    cornelltest.assert_equals(163, rgb.green)
    cornelltest.assert_equals(36, rgb.blue)
    
    cmyk = colormodel.CMYK(50.00, 50.00, 50.00, 50.00)
    rgb = a3.cmyk_to_rgb(cmyk)
    cornelltest.assert_equals(64, rgb.red)
    cornelltest.assert_equals(64, rgb.green)
    cornelltest.assert_equals(64, rgb.blue)
    
    cmyk = colormodel.CMYK(69.99, 69.69, 96.96, 66.99)
    rgb = a3.cmyk_to_rgb(cmyk)
    cornelltest.assert_equals(25, rgb.red)
    cornelltest.assert_equals(26, rgb.green)
    cornelltest.assert_equals(3, rgb.blue)
    
    cmyk = colormodel.CMYK(100.0, 0.000, 50.00, 0.000)
    rgb = a3.cmyk_to_rgb(cmyk)
    cornelltest.assert_equals(0, rgb.red)
    cornelltest.assert_equals(255, rgb.green)
    cornelltest.assert_equals(128, rgb.blue)
    


def test_rgb_to_hsv():
    """Test translation function rgb_to_hsv"""
    #pass # ADD TESTS TO ME
    rgb = colormodel.RGB(15, 5, 75)
    hsv = a3.rgb_to_hsv(rgb)
    cornelltest.assert_equals(248.6, hsv.hue)
    cornelltest.assert_equals(0.933, hsv.saturation)
    cornelltest.assert_equals(0.294, hsv.value)
    
    rgb = colormodel.RGB(0, 0, 0)
    hsv = a3.rgb_to_hsv(rgb)
    cornelltest.assert_equals(0.000, hsv.hue)
    cornelltest.assert_equals(0.000, hsv.saturation)
    cornelltest.assert_equals(0.000, hsv.value)
    
    rgb = colormodel.RGB(100, 100, 100)
    hsv = a3.rgb_to_hsv(rgb)
    cornelltest.assert_equals(0.000, hsv.hue)
    cornelltest.assert_equals(0.000, hsv.saturation)
    cornelltest.assert_equals(0.392, hsv.value)
    
    rgb = colormodel.RGB(235, 19, 25)
    hsv = a3.rgb_to_hsv(rgb)
    cornelltest.assert_equals(358.3, hsv.hue)
    cornelltest.assert_equals(0.919, hsv.saturation)
    cornelltest.assert_equals(0.922, hsv.value)
    
    rgb = colormodel.RGB(1, 2, 3)
    hsv = a3.rgb_to_hsv(rgb)
    cornelltest.assert_equals(210.0, hsv.hue)
    cornelltest.assert_equals(0.667, hsv.saturation)
    cornelltest.assert_equals(0.012, hsv.value)

def test_hsv_to_rgb():
    """Test translation function hsv_to_rgb"""
    #pass # ADD TESTS TO ME
    hsv = colormodel.HSV(1.000, .500, .500)
    rgb = a3.hsv_to_rgb(hsv)
    cornelltest.assert_equals(128, rgb.red)
    cornelltest.assert_equals(65, rgb.green)
    cornelltest.assert_equals(64, rgb.blue)
    
    hsv = colormodel.HSV(200.0, .250, .250)
    rgb = a3.hsv_to_rgb(hsv)
    cornelltest.assert_equals(48, rgb.red)
    cornelltest.assert_equals(58, rgb.green)
    cornelltest.assert_equals(64, rgb.blue)
    
    hsv = colormodel.HSV(312.3, 0.667, 0.913)
    rgb = a3.hsv_to_rgb(hsv)
    cornelltest.assert_equals(233, rgb.red)
    cornelltest.assert_equals(78, rgb.green)
    cornelltest.assert_equals(201, rgb.blue)
    
    hsv = colormodel.HSV(87.20, 0.117, 0.699)
    rgb = a3.hsv_to_rgb(hsv)
    cornelltest.assert_equals(169, rgb.red)
    cornelltest.assert_equals(178, rgb.green)
    cornelltest.assert_equals(157, rgb.blue)
    
    hsv = colormodel.HSV(0.000, 0.000, 0.000)
    rgb = a3.hsv_to_rgb(hsv)
    cornelltest.assert_equals(0, rgb.red)
    cornelltest.assert_equals(0, rgb.green)
    cornelltest.assert_equals(0, rgb.blue)

# Application Code
if __name__ == "__main__":
    test_complement()
    test_truncate5()
    test_round5()
    test_round5_color()
    test_rgb_to_cmyk()
    test_cmyk_to_rgb()
    test_rgb_to_hsv()
    test_hsv_to_rgb()
    print "Module a3 is working correctly"
