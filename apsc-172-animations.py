from manim import *
import numpy as np
from math import *

class Tutorial(ThreeDScene):

    

    def construct(self):
        def parametric_surface(t,u):
            return np.array([cos(t), sin(t), u])

        def plane_surface(t,u):
            return np.array([t,u,1-t-u])

        def path(t):
            return np.array([cos(t), sin(t), 1-cos(t)-sin(t)])
        axes = ThreeDAxes()

        plane = Surface(lambda t,u: axes.c2p(*plane_surface(t,u)), u_range=[-2,2], v_range=[-2,2], resolution=8, fill_opacity=0.4, checkerboard_colors=[ORANGE])
        cylinder = Surface(lambda u,v: axes.c2p(*parametric_surface(v,u)), u_range=[-2,2], v_range=[0, 2*PI], resolution=8, fill_opacity=0.4)

        self.set_camera_orientation(phi=45*DEGREES, theta=45*DEGREES, zoom=0.75, focal_distance=200)
        self.play(Create(axes))
        self.play(Create(plane), Create(cylinder))
        self.begin_ambient_camera_rotation(0.44)
        self.wait(5)

