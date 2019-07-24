import vim
import cv2 as cv
import numpy as np
import sys
def get_curr_line():
    return vim.current.line


def get_line_buffer():
    buf = vim.current.buffer
    (lnum1, col1) = buf.mark('<')
    (lnum2, col2) = buf.mark('>')
    lines = vim.eval('getline({}, {})'.format(lnum1, lnum2))
    lines[0] = lines[0][col1:]
    lines[-1] = lines[-1][:col2]
    return lines[0]

def print_latex_to_screen(img):
    row, col = latex.shape
    row = int(row/2)
    col = int(col/2)
    t = 250
    output_lines = []
    for r in range(row):
        output_line = u''
        for c in range(col):
            output = '  '
            box = latex[ 2*r:2*r+2 , 2*c:2*c+2 ]
            box_code = [box[0][0]<t, box[0][1]<t, box[1][0]<t, box[1][1]<t]
            if box_code == [False, False, False, False]:
                output = ' '
            elif box_code == [False, False, False, True]:
                output = u'\u2597'
            elif box_code == [False, False, True, False]:
                output = u'\u2596'
            elif box_code == [False, False, True, True]:
                output = u'\u2599'#Can't find line bottom
                #output = u'\u2584'
            elif box_code == [False, True, False, False]:
                output = u'\u259d'
            elif box_code == [False, True, False, True]:
                output = u'\u259c'#Can't find vline right
                #output = u'\u2590'
            elif box_code == [False, True, True, False]:
                output = u'\u259e'
            elif box_code == [False, True, True, True]:
                output = u'\u259f'
            elif box_code == [True, False, False, False]:
                output = u'\u2598'
            elif box_code == [True, False, False, True]:
                output = u'\u259a'
            elif box_code == [True, False, True, False]:
                output = u'\u259b'#Can't find vline left
                #output = u'\u258D'
            elif box_code == [True, False, True, True]:
                output = u'\u2599'
            elif box_code == [True, True, False, False]:
                output = u'\u259b' #Can't find line top
            elif box_code == [True, True, False, True]:
                output = u'\u259c'
            elif box_code == [True, True, True, False]:
                output = u'\u259b'
            elif box_code == [True, True, True, True]:
                output = u'\u259f'
            #print(latex[ 4*r:4*r+2 , 4*c:4*c+2 ])
            output_line += output
        output_lines.append(output_line)
        #print(output_line)
        sys.stdout.write(output_line+'\n')

def print_latex_to_screen_braile(img):
    row, col = img.shape

    padding_r = np.full((4,col), fill_value=255)
    img = np.ma.row_stack([img,padding_r])

    row, col = img.shape
    padding_c = np.full((row,4), fill_value=255)
    img = np.ma.column_stack([img,padding_c])

    row, col = img.shape
    row = int(row/4)
    col = int(col/2)
    t = 250
    output_lines = []
    for r in range(row):
        output_line = u''
        for c in range(col):
            output = '  '
            box = img[ 4*r:4*r+4 , 2*c:2*c+2 ]
            brail_code = [box[0][0]<t, box[1][0]<t, box[2][0]<t, box[0][1]<t, box[1][1]<t, box[2][1]<t, box[3][0]<t, box[3][1]<t]
            brail_code.reverse()
            
            binary = [128, 64, 32, 16, 8, 4, 2, 1]
            code = np.dot(brail_code, binary)
            ucode_hex = hex( int('0x2800',16) + code )
            output = chr(int(ucode_hex, 16))

            #print(latex[ 4*r:4*r+2 , 4*c:4*c+2 ])
            output_line += output
        output_lines.append(output_line)
        #sys.stdout.write(output_line+'\n')
        print(output_line)

import os
import sys
import sympy
def print_latex_eq(latex_eq):
    #sympy.preview(r'$$\int_0^1 e^x\,dx$$', viewer='file', filename='test.png', euler=False)
    #sympy.preview(r'$$1 \in \mathbb{R}^2 2 \in A \in B$$', viewer='file', filename='test.png', euler=False)
    #filepath = '/home/yhong/.vim/bundle/latex_preview/test.png'
    plugin_root_dir = vim.eval('s:plugin_root_dir')
    fp = os.path.join(plugin_root_dir, 'test.png')
    
    #sympy.preview(latex_eq, viewer='file', filename='test.png', euler=False)
    sympy.preview(latex_eq, viewer='file', filename=fp, euler=False)
    #latex = cv.imread('test.png')
    latex = cv.imread(fp)
    #latex = cv.imread('math.png')
    latex = cv.cvtColor(latex, cv.COLOR_BGR2GRAY)
    (thresh, latex) = cv.threshold(latex, 240, 255, cv.THRESH_BINARY)
    #latex = downsample(latex).astype(int)
    #print(latex[10:20,0:10])
    #print(u'\u2596'+u'\u2597'+u'\u2598'+u'\u2599'+u'\u259a'+u'\u259b'+u'\u259c'+u'\u259d'+u'\u259e'+'  '+u'\u259f')
    #latex = cv.resize(latex, (0,0), fx=.7, fy=.7) 
    #imshow(latex,  cmap='gray', vmin=0, vmax=255)
    print_latex_to_screen_braile(latex)

def print_latex():
    #latex_eq = get_line_buffer().strip('$')
    latex_eq = get_curr_line().strip('$')
    latex_eq = r'$$'+latex_eq+r'$$'
    #latex_eq = '\sum{\sqrt{(x_i-y_i)^2}}'
    print_latex_eq(latex_eq)
