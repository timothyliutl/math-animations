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
        surface = Surface(lambda u,v: axes.c2p(*surface_equation(u,v)), u_range=[-3,3], v_range=[-3,3], resolution=8, fill_opacity=1)

        e = ValueTracker(0.01)

        plane = always_redraw(lambda: Surface(lambda u,v: axes.c2p(u,v,e.get_value()), u_range=[-6,6], v_range=[-6,6], fill_opacity=0.4, checkerboard_colors=[ORANGE, ORANGE], resolution=8))
        curve1 = ParametricFunction(lambda t: axes.c2p(*parametric_curve(sqrt(2), t)), t_range=[0, 2*PI])
        decimal = DecimalNumber(0, 2).to_corner(RIGHT+DOWN).scale(1.2)
        text = Text("Z = ").next_to(decimal, LEFT).scale(1.2)

        self.set_camera_orientation(phi=75*DEGREES, theta=45*DEGREES, zoom=0.75, focal_distance=200)
        self.add_fixed_in_frame_mobjects(decimal)
        self.add_fixed_in_frame_mobjects(text)
        self.play(Create(axes))
        self.play(Create(surface))
        self.begin_ambient_camera_rotation(0.04)
        self.play(Create(plane), Write(decimal), Write(text))
        self.wait(2)


        for i in range(1,7):
            self.play(e.animate.set_value(i))
            curve = ParametricFunction(lambda t: axes.c2p(*parametric_curve(sqrt(i), t)), t_range=[0, 2*PI])
            self.add_fixed_in_frame_mobjects(decimal)
            self.play(Create(curve), decimal.animate.set_value(e.get_value()), run_time = 0.5)
            self.add_fixed_in_frame_mobjects(decimal)
            self.wait(0.2)

        self.wait(2)
        self.move_camera(phi=0*DEGREES, theta=45*DEGREES, zoom=0.75, focal_distance=200)
        self.wait(0.2)
        self.play(plane.animate.set_opacity(0), surface.animate.set_opacity(0))
        self.wait(0.2)

