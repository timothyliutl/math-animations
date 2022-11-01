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
            return np.array([radius*cos(v), radius*sin(v), u])
       
        def cylinder_end(u,v, height):
            return np.array([u*cos(v), u*sin(v), height])

        def cylinder_group(radius,height, dx):
            cylinder = Surface(lambda u,v: axes.c2p(*cylinder_slice(u,v,radius)), u_range=[height-dx,height], v_range=[0,2*PI], resolution=8, fill_opacity=0.5, fill_color=ORANGE, checkerboard_colors=[ORANGE])
            caps = Surface(lambda u,v: axes.c2p(*cylinder_end(u,v,height)), u_range=[0.01,radius], v_range=[0,2*PI], resolution=8, fill_opacity=0.5, fill_color=ORANGE, checkerboard_colors=[ORANGE])
            caps2 = Surface(lambda u,v: axes.c2p(*cylinder_end(u,v,height-dx)), u_range=[0.01,radius], v_range=[0,2*PI], resolution=8, fill_opacity=0.5, fill_color=ORANGE, checkerboard_colors=[ORANGE])
            return VGroup(cylinder, caps, caps2)

        cone = Surface(lambda u,v: axes.c2p(*solid(u,v)), u_range=[0.1,2], v_range=[0, 2*PI], fill_opacity=0.5, resolution=8)
        self.move_camera(phi=0*DEGREES, theta=0*DEGREES, focal_distance=20)

        self.set_camera_orientation(phi=30 * DEGREES, theta=-60 * DEGREES, zoom=0.5)
        


        self.play(Create(axes))
        self.play(Create(cone))
        num_cylinders = 10
        for i in range(num_cylinders + 1):
            height = (5/num_cylinders)*i
            radius = height*2/5
            dx=5/num_cylinders
            cylinder_surface = Surface(lambda u,v: axes.c2p(*cylinder_slice(u,v,radius)), u_range=[height-dx/2+7,height+7 + dx/2], v_range=[0,2*PI], resolution=8)
            
            self.play(Create(cylinder_group(radius, height+7, dx)))
        self.wait(2)



