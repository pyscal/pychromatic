
import matplotlib.pyplot as plt
from cycler import cycler
import pychromatic.colors as pc
import matplotlib.colors as mc
from pychromatic.palette import Palette
import matplotlib.gridspec as gridspec
import pychromatic.colors as colorlist
from IPython.display import display, Markdown, Latex

def tabulate(columnlist, header=None, fmt=None):
    """
    Pretty print tables
    """
    if header is not None:
        if len(columnlist) != len(header):
            raise ValueError("Length of columns and headers do not match")
    if fmt is not None:
        if len(columnlist) != len(fmt):
            raise ValueError("Length of columns and headers do not match")
   
    output = []

    if header is None:
        header = [str(i) for i in range(len(columnlist))]
    
    for i in range(len(header)):
        output.append("|")
        output.append(header[i])
    output.append("|")
    output.append("\n")

    #add a line
    for i in range(len(header)):
        output.append("|")
        output.append("---")
    output.append("|")
    output.append("\n")

    #now format the values
    for i in range(len(columnlist[0])):
        for j in range(len(header)):
            output.append("|")
            if fmt is None:
                output.append(str(columnlist[j][i]))
            else:
                output.append(fmt[j]%columnlist[j][i])
        output.append("|")
        output.append("\n")        
    outstr = "".join(output)
    display(Markdown(outstr))

def chromatify(add_subplot): 
    def modify_plot(*args, **kwargs): 
        '''
        Function to modify plot
        '''
        #Process def args
        
        labelsize = kwargs.get('labelsize',  12)
        color = kwargs.get('color',  "#37474F")
        colors = kwargs.get('color',  colorlist.color_palettes['set6']['colors'])
        xlabel = kwargs.get('xlabel',  'ax.set_xlabel()')
        ylabel = kwargs.get('ylabel',  'ax.set_ylabel()')
        labelfont = kwargs.get('labelfont',  12)

        print("this went through decor")

        #Params and splines
        ax = add_subplot(*args, **kwargs)
        ax.tick_params(which='major', length=0, width=1, 
                       direction='in', bottom=True, top=False, 
                       right=False, color=color, 
                       labelsize=labelsize)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_color("#37474F")
        ax.spines['left'].set_color("#37474F")
        
        ax.xaxis.label.set_color("#37474F")
        ax.yaxis.label.set_color("#37474F")
        #Change custom plot colors
        custom_cycler = (cycler(color=colors))
        ax.set_prop_cycle(custom_cycler)       
        
        #labels
        ax.set_xlabel(xlabel, fontsize=labelfont)
        ax.set_ylabel(ylabel, fontsize=labelfont)

        return ax 
    return modify_plot 
