"""
Module containing color palettes
"""

#import the utilities class
from pychromatic.cutils import Color_utils

#default colors
red = '#d32f2f'
pink = '#c2185b'
purple = '#7b1fa2'
blue = '#1976d2'
lightblue = '#0288d1'
cyan = '#0097a7'
teal = '#00796b'
green = '#388e3c'
lightgreen = '#689f38'
lime = '#afb42b'
yellow = '#fbc02d'
orange = '#f57c00'
brown = '#5d4037'
grey = '#616161'
bluegrey = '#455a64'


class default(Color_utils):
    def __init__(self):
        self.colors = [blue,red,green,orange,purple,bluegrey,lightblue,pink,
        				lightgreen,yellow,teal,grey,brown,lime,cyan]
        
class pastels(Color_utils):
    def __init__(self):
        self.colors = ['#8dd3c7','#ffffb3','#bebada','#fb8072','#80b1d3','#fdb462',
        				'#b3de69','#fccde5','#d9d9d9','#bc80bd','#ccebc5','#ffed6f']
    
class basics(Color_utils):
    def __init__(self):
        self.colors = ['#e41a1c','#377eb8','#4daf4a','#984ea3','#ff7f00','#ffff33',
              			'#a65628','#f781bf','#999999']

#3colors color blindself    
class set1_dark(Color_utils):
    def __init__(self):
        self.colors = ['#1b9e77','#d95f02','#7570b3','#e7298a','#66a61e','#e6ab02',
        				'#a6761d','#666666']

#3colors color blindself  
class set1_pastel(Color_utils):
    def __init__(self):
        self.colors = ['#66c2a5','#fc8d62','#8da0cb','#e78ac3','#a6d854','#ffd92f',
        				'#e5c494','#b3b3b3']
        
class excel(Color_utils):
    def __init__(self):
        self.colors = ['#5F7CBB','#B1534F','#9DBD5B','#7D60A0','#E8994B','#999999',
        				'#67A8C4']
                
class set2(Color_utils):
    def __init__(self):
        self.colors = ['#d11141','#00b159','#00aedb','#f37735','#ffc425']


class google(Color_utils):
    def __init__(self):
        self.colors = ['#008744','#0057e7','#d62d20','#ffa700','#B9B9B9']


class set3(Color_utils):
    def __init__(self):
        self.colors = ['#5fad56','#f2c14e','#f78154','#4d9078','#b4436c']


class set4(Color_utils):
    def __init__(self):
        self.colors = ['#363537','#0cce6b','#dced31','#ef2d56','#ed7d3a']


class dark(Color_utils):
    def __init__(self):
        self.colors = ['#007283','#72013f','#c76b0d','#322569','#124d25']    


class earth(Color_utils):
    def __init__(self):
        self.colors = ['#FDBF00','#514939','#BD5340','#90A74F','#D0B388']


class set5(Color_utils):
    def __init__(self):
        self.colors = ['#F4AB33','#EC7176','#C068A8','#5C63A2','#1B4E6B']


class rainbow(Color_utils):
    def __init__(self):
        self.colors = ['#015486','#00B5D0','#6EC626','#FFBE00','#FD5D47']


class set6(Color_utils):
    def __init__(self):
        self.colors = ['#435772','#2DA4A8','#FD9C3C','#FD6041','#CF2257']    


class set7(Color_utils):
    def __init__(self):
        self.colors = ['#4597A3','#D6765D','#99CFAB','#F0CB73','#7B7E7E']
