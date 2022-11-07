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


        self.set_camera_orientation(phi=30 * DEGREES, theta=-60 * DEGREES, zoom=0.6, focal_distance=1000)

        self.play(Create(axes))
        self.play(Create(surface1))
        

class WorkIntegral(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes(x_range=[-10,10], y_range=[-10,10], z_range=[0,10]).shift(-3* OUT)

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

        def line_function(t):
            return np.array([0,t, 5/2*t + 7])

        # https://github.com/3b1b/manim/issues/730
        line = ParametricFunction(lambda t: axes.c2p(*line_function(t)), t_range=[0,2])
        rotate_tracker = ValueTracker(0.001)
        line.initial_state = line.copy()
        def updater(obj):
            obj.become(obj.initial_state)
            obj.rotate(rotate_tracker.get_value()-PI/2, axis=OUT, about_point=axes.c2p(0,0,7))

        self.set_camera_orientation(phi=90 * DEGREES, theta=90*DEGREES, zoom=0.75, focal_distance=200)

        #drawing the line that makes the cone then rotating it        
        #drawing the cone as well as the cylinders used to approximate the volume

        self.play(Create(axes))
        self.play(Create(line.add_updater(updater)))

        self.move_camera(phi=60*DEGREES, theta=45*DEGREES, zoom=0.75, focal_distance=200)

        self.play(rotate_tracker.animate.set_value(2*PI))

        self.wait(2)
        self.play(Create(cone))
        self.play(rotate_tracker.animate.set_value(4*PI))
        
        self.move_camera(phi=40 * DEGREES, theta=60 * DEGREES, gamma=0*DEGREES, zoom=0.75, focal_distance=200)
        
        num_cylinders = 7
        cylinder_list = []
        for i in range(1, num_cylinders + 1):
            height = (5/num_cylinders)*i
            height_prev = (5/num_cylinders)*(i-1)
            radius =  (height_prev+height)/2*2/5
            dx=5/num_cylinders
            cylinder_surface = Surface(lambda u,v: axes.c2p(*cylinder_slice(u,v,radius)), u_range=[height-dx/2+7,height+7 + dx/2], v_range=[0,2*PI], resolution=8)
            cylinder_list.append(cylinder_group(radius, height+7, dx))
            self.play(DrawBorderThenFill(cylinder_list[-1], run_time=0.75))
        self.wait(2)

        for cylinder in cylinder_list:
            self.play(cylinder.animate.shift(-2.5*LEFT), run_time=0.5)



