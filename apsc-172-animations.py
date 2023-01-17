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


class Spaghetti(ThreeDScene):
    def construct(self):

        def surface_equation(u,v):
            return np.array([u,v,u**2+v**2])

        def parametric_curve(z_value, t):
            return np.array([z_value * sin(t), z_value * cos(t), z_value**2])

        axes = ThreeDAxes(x_range=[-8,8], y_range=[-8,8], z_range=[-8,8], x_length=10, y_length=10, z_length=10)
        surface = Surface(lambda u,v: axes.c2p(*surface_equation(u,v)), u_range=[-3,3], v_range=[-3,3], resolution=8, fill_opacity=0.3)

        e = ValueTracker(0.01)

        plane = always_redraw(lambda: Surface(lambda u,v: axes.c2p(u,v,e.get_value()), u_range=[-4,4], v_range=[-4,4], fill_opacity=0.4, checkerboard_colors=[ORANGE, ORANGE], resolution=8))
        curve1 = ParametricFunction(lambda t: axes.c2p(*parametric_curve(sqrt(2), t)), t_range=[0, 2*PI])

        self.set_camera_orientation(phi=45*DEGREES, theta=45*DEGREES, zoom=0.75, focal_distance=200)
        self.play(Create(axes))
        self.play(Create(surface))
        self.begin_ambient_camera_rotation(0.44)
        self.play(Create(plane))

        for i in range(10):
            self.play(e.animate.set_value(i))
            curve = ParametricFunction(lambda t: axes.c2p(*parametric_curve(sqrt(1), t)), t_range=[0, 2*PI])
            self.play(Create(curve))
            self.wait(0.3)

        self.wait(5)


