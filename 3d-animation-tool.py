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
        radius_brace = brace_obj([0,0,line_function(2)[-1]], line_function(2))
        self.play(Create(radius_brace))
        self.wait(1)
        self.play(Uncreate(radius_brace))
        for i in range(len(cylinder_list)-1):
            self.play(temp_group[-i-1].animate.set_opacity(1), temp_group[-i].animate.set_opacity(0.01))
            self.wait(1)

        self.play(temp_group.animate.set_opacity(1))
        self.wait(2)
        #make all by one cylinder transparent 
        #find the area for the cylinder on top
        #adding more cylinders to show we can make this infinite to get closer to the true volume

class ThreeDRotations(ThreeDScene):
    def construct(self):
        rotate_tracker = ValueTracker(0)
        axes = ThreeDAxes()

        def upperbound(t):
            return np.array([t,4,0])

        def lowerbound(t):
            return np.array([t,t**2, 0])

        def ub_shell(u,v):
            return np.array([u, 4*cos(v), 4*sin(v)])
        
        def lb_shell(u,v):
            return np.array([u, u**2*cos(v), u**2*sin(v)])

        def updater(obj):
            obj.become(obj.initial_state)
            obj.rotate(rotate_tracker.get_value(), axis=RIGHT, about_point=axes.c2p(0,0,0))
        
        curve_ub = ParametricFunction(lambda t: axes.c2p(*upperbound(t)), t_range=[0,2])
        curve_lb = ParametricFunction(lambda t: axes.c2p(*lowerbound(t)), t_range=[0,2])
        surface_ub = Surface(lambda u,v: ub_shell(u,v), u_range=[0,2], v_range=[0,2*PI], resolution=8, checkerboard_colors=[ORANGE]).set_opacity(0.5)
        surface_lb = Surface(lambda u,v: lb_shell(u,v), u_range=[0,2], v_range=[0,2*PI], resolution=8, checkerboard_colors=[ORANGE]).set_opacity(0.5)
        area = axes.get_area(curve_ub, [0, 2], bounded_graph=curve_lb, color=BLUE, opacity=0.5)
        curve_ub.initial_state = curve_ub.copy()
        curve_lb.initial_state = curve_lb.copy()
        area.initial_state = area.copy()


        self.set_camera_orientation(phi=0*DEGREES, theta=-90*DEGREES, zoom=0.75, focal_distance=200)
        self.play(Create(axes))
        self.play(Create(curve_ub.add_updater(updater)))
        self.play(Create(curve_lb.add_updater(updater)))
        self.play(Create(area.add_updater(updater)))

        self.move_camera(phi=45*DEGREES, theta=-45*DEGREES, zoom=0.75, focal_distance=200)
        self.play(rotate_tracker.animate.set_value(2*PI), run_time = 2)
        self.play(Create(surface_ub), Create(surface_lb))
        self.begin_ambient_camera_rotation()
        self.play(rotate_tracker.animate.set_value(6*PI), run_time = 10)



        

class Equation_Derivation(Scene):
    def construct(self):
        top_cylinder = MathTex(r'W =', r'M', r' * g * h').scale(0.75).to_edge(UP).shift(RIGHT)
        top_cylinder2 = MathTex(r'W = \rho *', r'V',r'* g * h').next_to(top_cylinder, DOWN).scale(0.7)
        top_cylinder3 = MathTex(r'W = \rho * (\pi *', r'R^2', r'* dh) * g * h').next_to(top_cylinder2, DOWN).scale(0.7)
        cylinder_volume = MathTex(r'V = \pi *', r'R^2', r'* dh').scale(0.75).to_corner(UL)
        mass_formula = MathTex(r'M = \rho * V').scale(0.75).next_to(cylinder_volume, DOWN)
        equation = MathTex(r'h = 5/2 r + 7').scale(0.7).next_to(mass_formula, DOWN)
        equation2 = MathTex(r'R = 2/5*(h-7)').scale(0.7).next_to(equation, DOWN)
        givens = MathTex(r'dh = 0.5, h \in [7,15]').next_to(equation2, DOWN).scale(0.7)
        work1 = MathTex(r'W = \rho * (\pi *', r'R^2', r'* dh) * g * h').next_to(top_cylinder3, DOWN).scale(0.7)
        work2 = MathTex(r'W = \rho * \pi * (2/5(h-7))^2 * g * h * dh').next_to(top_cylinder3, DOWN).scale(0.7)
        rect1 = SurroundingRectangle(top_cylinder[1])
        rect2 = SurroundingRectangle(mass_formula)
        rect3 = SurroundingRectangle(top_cylinder2[1])
        rect4 = SurroundingRectangle(cylinder_volume)
        rect5 = SurroundingRectangle(top_cylinder3[1])
        rect6 = SurroundingRectangle(equation2)

        self.play(Write(cylinder_volume), Write(mass_formula), Write(equation), Write(equation2))
        self.play(Write(top_cylinder))
        self.wait(2)
        self.play(Create(rect1), Create(rect2))
        self.play(Uncreate(rect1), Uncreate(rect2))
        self.wait(2)
        self.play(TransformMatchingShapes(top_cylinder.copy(),top_cylinder2))
        self.play(Create(rect3), Create(rect4))
        self.play(Uncreate(rect3), Uncreate(rect4))
        self.wait(2)
        self.play(TransformMatchingShapes(top_cylinder2.copy(),top_cylinder3))
        self.wait(2)
        self.play(Create(rect5), Create(rect6))
        self.play(Uncreate(rect5), Uncreate(rect6))
        self.play(TransformMatchingShapes(top_cylinder3.copy(),work2))

        


        

