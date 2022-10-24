from cmath import sqrt
from math import sin, cos 
from manim import *

#scene to help out with integrating volumes
class ThreeDTool(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes()

        def equation1(t):
            # replace second value in the array with any equation in terms of t
            return sqrt(t)
        
        def surface1(u,v):
            return np.array([u, equation1(u)*sin(v),equation1(u) * cos(v)])

        def curve1(t):
            return np.array([t, ])

        surface1 = Surface(lambda u,v: axes.c2p(*surface1(u,v)), u_range=[0.1, 5], v_range=[0, 2*PI], resolution=12)


        self.set_camera_orientation(phi=30 * DEGREES, theta=-60 * DEGREES, zoom=0.6)

        self.play(Create(axes))
        self.play(Create(surface1))
        

class WorkIntegral(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes(x_range=[-10,10], y_range=[-10,10], z_range=[0,10])

        def solid(u,v):
            #cone with height 5 and radius 2
            return np.array([u*cos(v), u*sin(v), 5/2*u+ 7])
        
        def radius(height):
            return 5/2*(height-7)

        def cylinder_slice(u,v, radius):
            return np.array([sqrt(radius)*cos(v), sqrt(radius)*sin(v), u])
       
        def cylinder_end(u,v, height):
            return np.array([sqrt(u)*cos(v), sqrt(u)*sin(v), height])

        def cylinder_group(radius,height, dx):
            cylinder = Surface(lambda u,v: axes.c2p(*cylinder_slice(u,v,2)), u_range=[height-dx,height], v_range=[0,2*PI])
            caps = Surface(lambda u,v: axes.c2p(*cylinder_end(u,v,height)), u_range=[0,radius], v_range=[0,2*PI])
            caps2 = Surface(lambda u,v: axes.c2p(*cylinder_end(u,v,height-dx)), u_range=[0,radius], v_range=[0,2*PI])
            return VGroup(cylinder, caps, caps2)

        cone = Surface(lambda u,v: axes.c2p(*solid(u,v)), u_range=[0.1,5/2], v_range=[0, 2*PI])

        self.set_camera_orientation(phi=30 * DEGREES, theta=-60 * DEGREES, zoom=0.8)


        self.play(Create(axes))
        self.play(Create(cone))
        self.play(Create(cylinder_group(2, 12, 0.5)))


