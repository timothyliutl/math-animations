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

        axes = ThreeDAxes(x_range=[-10,10], y_range=[-10,10], z_range=[0,13]).shift(-3* OUT)

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
        rotate_tracker = ValueTracker(0)
        line.initial_state = line.copy()
        def updater(obj):
            obj.become(obj.initial_state)
            obj.rotate(rotate_tracker.get_value(), axis=OUT, about_point=axes.c2p(0,0,7))
        
        def brace_obj(point1, point2):
            brace = BraceBetweenPoints(axes.c2p(*point1), axes.c2p(*point2)).rotate(90*DEGREES, axis=UP, about_point=axes.c2p(*point1))
            return brace

        brace = BraceBetweenPoints(axes.c2p(0,0,line_function(1.75)[2]), axes.c2p(*line_function(1.75))).rotate(90*DEGREES, axis=UP, about_point=axes.c2p(0,0,line_function(1.75)[2]))
        radius_text = MathTex('Radius').set_color(BLUE).next_to(brace, IN).rotate(90*DEGREES, axis=UP).scale(0.5).rotate(90*DEGREES, axis=RIGHT)
        equation = MathTex(r'h = 5/2 r + 7')
        equation2 = MathTex(r'r = 2/5*(h-7)')

        self.set_camera_orientation(phi=90 * DEGREES, theta=0*DEGREES, zoom=0.75, focal_distance=200)

        #drawing the line that makes the cone then rotating it        
        #drawing the cone as well as the cylinders used to approximate the volume
        
        equation.to_corner(UR)
        self.play(Create(axes))
        
        self.add_fixed_in_frame_mobjects(equation)
        self.play(Write(equation))
        self.play(Create(line.add_updater(updater)))
        self.play(Write(brace), Write(radius_text))
        self.wait(1)

        

        self.move_camera(phi=60*DEGREES, theta=-45*DEGREES, zoom=0.75, focal_distance=200)

        self.play(Unwrite(equation))
        self.play(rotate_tracker.animate.set_value(2*PI))

        self.wait(2)
        self.play(Create(cone))
        self.play(rotate_tracker.animate.set_value(4*PI))
        self.play(Unwrite(brace), Unwrite(radius_text))
    
        self.move_camera(phi=40 * DEGREES, theta=-60 * DEGREES, gamma=0*DEGREES, zoom=0.75, focal_distance=200)

        num_cylinders = 10
        cylinder_list = []
        for i in range(1, num_cylinders + 1):
            height = (5/num_cylinders)*i
            height_prev = (5/num_cylinders)*(i-1)
            radius =  height_prev*2/5
            dx=5/num_cylinders
            cylinder_surface = Surface(lambda u,v: axes.c2p(*cylinder_slice(u,v,radius)), u_range=[height-dx/2+7,height+7 + dx/2], v_range=[0,2*PI], resolution=8)
            cylinder_list.append(cylinder_group(radius, height+7, dx))
            self.play(DrawBorderThenFill(cylinder_list[-1], run_time=0.75))
        self.wait(2)

        #for cylinder in cylinder_list:
        #    self.play(cylinder.animate.shift(2.5*RIGHT), run_time=0.5)

        self.move_camera(phi=90 * DEGREES, theta=0*DEGREES, zoom=0.75, focal_distance=200)

        temp_group = VGroup(*cylinder_list)
        self.play(cone.animate.set_opacity(0))
        self.play(temp_group[-1].animate.set_opacity(1))
        self.play(temp_group[0:-1].animate.set_opacity(0.01))
        for i in range(len(cylinder_list)-1):
            self.play(temp_group[-i-1].animate.set_opacity(1), temp_group[-i].animate.set_opacity(0.01))
            self.wait(1)

        self.play(temp_group.animate.set_opacity(1))
        self.wait(2)
        #make all by one cylinder transparent 
        #find the area for the cylinder on top


        

class Equation_Derivation(Scene):
    def construct(self):
        top_cylinder = MathTex(r'work = m * g * h').scale(0.5).to_edge(UP).shift(RIGHT)
        top_cylinder2 = MathTex(r'work = \rho *', r'V',r'* g * h').scale(0.5).to_edge(UP).shift(RIGHT)
        top_cylinder3 = MathTex(r'work = \rho * (\pi * R^2 * dh) * g * h').scale(0.5).to_edge(UP).shift(RIGHT)
        givens = MathTex(r'dh = 0.5, h \in [7,15]')
        work1 = MathTex(r'W = \rho * (\pi * R^2 * dh) * g * h')
        self.play(Write(top_cylinder))
        self.wait(2)
        self.play(TransformMatchingShapes(top_cylinder, top_cylinder2))
        self.wait(2)
        self.play(TransformMatchingShapes(top_cylinder2, top_cylinder3))
        self.wait(2)

        

