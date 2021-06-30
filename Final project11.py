# coding: utf-8
from arcpy.sa import *
from arcpimport envy
#   File "<string>", line 2
#     from arcpimport envy
#                        ^
# SyntaxError: invalid syntax
from arcpimport envy
#   File "<string>", line 1
#     from arcpimport envy
#                        ^
# SyntaxError: invalid syntax
from arcpy.sa import *
from arcpimport envy
#   File "<string>", line 1
#     from arcpimport envy
#                        ^
# SyntaxError: invalid syntax
from arcpy import env
env.outputCoordinateSystem.name
# 'NAD_1983_StatePlane_Texas_North_Central_FIPS_4202_Feet'
env.extent
# <Extent object at 0x74965f2ef0[0x748e47a800]>
env.mask
# 'parcels_with_appraisal_data_R5'
Roaddis=EucDistance("tl_2015_48085_roads selection")
Flooddist=EucDistance('GIS_Vector1.CCDL.S_FLD_HAZ_AR_PRELIM')
Slope1=Slope('ned30m32096.tif')
Slope2=Slope('ned30m33096.tif')
C,s,m=10.,5.2640
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# ValueError: not enough values to unpack (expected 3, got 2)
C.s.m=10.,5.,2640
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# NameError: name 'C' is not defined
from arcpimport envy
#   File "<string>", line 1
#     from arcpimport envy
#                        ^
# SyntaxError: invalid syntax
from arcpy.sa import *
from arcpimport envy
#   File "<string>", line 1
#     from arcpimport envy
#                        ^
# SyntaxError: invalid syntax
from arcpy import env
from arcpimport envy
#   File "<string>", line 1
#     from arcpimport envy
#                        ^
# SyntaxError: invalid syntax
env.mask
# 'parcels_with_appraisal_data_R5'
C,s,m=10.,5.,2640
roadf=C/(1+("Roaddis"/m)**-s)
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# TypeError: unsupported operand type(s) for /: 'str' and 'int'
roadf=C/(1+(Roaddis/m)**-s)
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
#   File "c:\program files\arcgis\pro\Resources\arcpy\arcpy\sa\Functions.py", line 9013, in FloatDivide
#     in_raster_or_constant2)
#   File "c:\program files\arcgis\pro\Resources\arcpy\arcpy\sa\Utils.py", line 53, in swapper
#     result = wrapper(*args, **kwargs)
#   File "c:\program files\arcgis\pro\Resources\arcpy\arcpy\sa\Functions.py", line 9010, in wrapper
#     ["FloatDivide", in_raster_or_constant1, in_raster_or_constant2])
#   File "c:\program files\arcgis\pro\Resources\arcpy\arcpy\sa\Raster.py", line 73, in __new__
#     return super().__new__(cls, in_raster, is_multidimensional)
# KeyboardInterrupt
C,s,m=10,0.5,math.log(5280)
roadff=C*math.exp(-(math.log(Roaddis)-m)**2/(2*(s**2)))
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# TypeError: must be real number, not Raster
roadff=C*Exp(-(Ln(Roaddis)-m)**2/(2*(s**2)))