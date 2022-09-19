import playsound # allows the playing of sound files
import time #download current time for sleep function
import pygame #Library for running graphical interface

class imageHandler:
  def __init__ ( self ):
    self.pics = dict()

  def loadFromFile ( self, filename, id=None ):
    if id == None: id = filename
    self.pics [ id ] = pygame.image.load ( filename ).convert()

  def loadFromSurface ( self, surface, id ):
    self.pics [ id ] = surface.convert_alpha()

  def render ( self, surface, id, position = None, clear = False, size = None ):
    if clear == True:
      surface.fill ( (5,2,23) ) #

    if position == None:
      picX = int ( surface.get_width() / 2 - self.pics [ id ].get_width() / 2 )
    else:
      picX = position [0]
      picY = position [1]

    if size == None:
      surface.blit ( self.pics [ id ], ( picX, picY ) ) #

    else:
      surface.blit ( pygame.transform.smoothscale ( self.pics [ id ], size ), ( picX, picY ) )
      
#Initialises the display-------------------------------------------------------
pygame.display.init() # Initiates the display pygame
#screen = pygame.display.set_mode((400,400), pygame.RESIZABLE) #uncomment this line for smaller window
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) #allows fullscreen #comment this line out for smaller window
handler = imageHandler()

def display():
    handler.loadFromFile ( "c://jarvis/jarvisface/1.jpg", "1" ) #add your own file location here
    handler.loadFromFile ( "c://jarvis/jarvisface/2.jpg", "2" ) #add your own file location here
    handler.loadFromFile ( "c://jarvis/jarvisface/3.jpg", "3" ) #add your own file location here
    handler.loadFromFile ( "c://jarvis/jarvisface/4.jpg", "4" ) #add your own file location here
    handler.loadFromFile ( "c://jarvis/jarvisface/5.jpg", "5" ) #add your own file location here
    handler.loadFromFile ( "c://jarvis/jarvisface/6.jpg", "6" ) #add your own file location here
    handler.loadFromFile ( "c://jarvis/jarvisface/7.jpg", "7" ) #add your own file location here
    handler.loadFromFile ( "c://jarvis/jarvisface/8.jpg", "8" ) #add your own file location here
    handler.loadFromFile ( "c://jarvis/jarvisface/9.jpg", "9" ) #add your own file location here
    handler.loadFromFile ( "c://jarvis/jarvisface/10.jpg", "10" ) #add your own file location here
display()

def face():
    A = 30
    B = 300
    x = 1024
    y = 768
    
    handler.render ( screen, "1", ( A, B ), True, ( x, y ) )
    pygame.display.update(30,300,1024,768) 
    # or replace with this line for easier coding 
    #pygame.display.update(A,B,x,y) 
    time.sleep(.2)
    handler.render ( screen, "2", ( A, B ), True, ( x, y ) )
    pygame.display.update(30,300,1024,768)
    time.sleep(.2)
    handler.render ( screen, "3", ( A, B ), True, ( x, y ) )
    pygame.display.update(30,300,1024,768)
    time.sleep(.2)
    handler.render ( screen, "4", ( A, B ), True, ( x, y ) )
    pygame.display.update(30,300,1024,768)
    time.sleep(.2)
    handler.render ( screen, "5", ( A, B ), True, ( x, y ) )
    pygame.display.update(30,300,1024,768)
    time.sleep(.2)
    handler.render ( screen, "6", ( A, B ), True, ( x, y ) )
    pygame.display.update(30,300,1024,768)
    time.sleep(.2)
    handler.render ( screen, "7", ( A, B ), True, ( x, y ) )
    pygame.display.update(30,300,1024,768)
    time.sleep(.2)
    handler.render ( screen, "8", ( A, B ), True, ( x, y ) )
    pygame.display.update(30,300,1024,768)
    time.sleep(.2)
    handler.render ( screen, "9", ( A, B ), True, ( x, y ) )
    pygame.display.update(30,300,1024,768)
    time.sleep(.2)
    handler.render ( screen, "10", ( A, B ), True, ( x, y ) )
    pygame.display.update(30,300,1024,768)
    time.sleep(.2)
face()