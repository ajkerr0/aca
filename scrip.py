# -*- coding: utf-8 -*-
"""
Created on Thu May 12 15:51:38 2016

@author: Alex
"""

#import PyPDF2
#import reportlab

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
width, height = landscape(letter)
 

def hello(c):
    c.drawString(100,100,"Hello World")
    
def set_bg(c):
    c.drawImage("aca.png", 0.,0., width=width,height=height,mask=None)
    
c = canvas.Canvas("test.pdf", pagesize=(width, height))


#define locations of forms



set_bg(c)
hello(c)



c.showPage()
c.save()


