from cmath import sin, cos, sqrt
from decimal import Decimal
from tkinter import BOTTOM, CENTER, TOP
from turtle import dot
from typing_extensions import runtime
from unicodedata import decimal
from manim import *
from matplotlib import mathtext
from sympy import binomial
import numpy as np

class Riemann_Sum(Scene):
    def construct(self):
        plane = NumberPlane(
           x_range=(-3,3.2,1),
           y_range=(-1.5,1.5,0.25),
           x_length=8,
           y_length=8
        ).to_edge(DOWN)
        
        function = plane.plot(lambda x: sin(x), color=GREEN)
        rect = plane.get_riemann_rectangles(graph=function, x_range=[0,3,0.2], color=BLUE, stroke_color=GREEN, dx=0.4, fill_opacity=0.5)
        rect2 = plane.get_riemann_rectangles(graph=function, x_range=[0,3,0.2], color=BLUE, stroke_color=GREEN, dx=0.2, fill_opacity=0.5)
        rect3 = plane.get_riemann_rectangles(graph=function, x_range=[0,3,0.2], color=BLUE, stroke_color=GREEN, dx=0.1, fill_opacity=0.5)
        label = MathTex('y = sin(x)')
        dx_label1 = MathTex('dx = 0.4')
        dx_label2 = MathTex('dx = 0.2')
        dx_label3 = MathTex('dx = 0.1')

        dx_label1.next_to(rect)
        dx_label2.next_to(rect2)
        dx_label3.next_to(rect3)

        label.set_color(WHITE)
        label.next_to(function, buff=0.3)
        self.play(DrawBorderThenFill(plane))
        self.play(Create(function), runtime=3)
        self.play(Write(label))
        self.play(DrawBorderThenFill(rect))
        self.play(Write(dx_label1))
        self.wait(3)
        self.play(FadeTransform(rect, rect2, stretch=True), FadeTransform(dx_label1, dx_label2))
        self.wait(2)
        self.play(FadeTransform(rect2, rect3, stretch=True), FadeTransform(dx_label2, dx_label3))
        self.wait(3)

class Derivative_Definition(Scene):
    def construct(self):
        title_text = Text('Definition of a Derivative')
        self.play(Write(title_text))
        self.wait(3)
        self.play(Unwrite(title_text, reverse=False))
        self.wait(1)

        # Have a list here delving into the topics that will be discussed in this animation

        limit_def = MathTex(r"f'(x) = \lim_{a \to 0}")

        to_isolate = ["f", "(x)", "(x+a)"]

        limit_def_part2 = MathTex(r"\frac{f(x+a) - f(x)}{a}")
        limit_def_part2.next_to(limit_def)
        orig_group = VGroup(limit_def, limit_def_part2)
        orig_group.arrange(center=True)
        self.play(Write(orig_group))
        self.wait(2)
        # Intermediate calculation step
        limit_def_intermediate = MathTex(r"{", r"f(x+a)", r" - ", r"f(x)", r"}", r"\over", r"{", r"(x-x)",  r" + a" , r"}", substrings_to_isolate=[r"{", r"f", r"(x+a)", r" - ", r"f(x)", r"}"])
        limit_def_intermediate.next_to(limit_def)
        group_inter = VGroup(limit_def, limit_def_intermediate)
        group_inter.arrange(center=True)
        self.play(TransformMatchingShapes(orig_group, group_inter, replace_mobject_with_target_in_scene=True))
        self.wait(2)
        # Talk about how this may be a bit daunting and connect it back to the definition of slope
        limit_def2 = MathTex(r"f'(x) = \lim_{a \to 0} ")
        limit_def2_part2 = MathTex(r"{", r"f", r"(x+a)", r" - ", r"f", r"(x)", r"}", r"\over", r"{", r"(x+a)", r" - ", r"(x)", r"}")
        limit_def2_part2.next_to(limit_def2)
        group = VGroup(limit_def2, limit_def2_part2)
        group.arrange(center=True)
        self.play(TransformMatchingShapes(group_inter, group, replace_mobject_with_target_in_scene=True), runtime=3)
        self.wait(2)
        text_change_color = MathTex(r"{", r"f(x+a)", r" - ", r"f(x)", r"}", r"\over", r"{", r"(x+a)", r" - ", r"(x)", r"}", tex_to_color_map={"(x+a)": BLUE, "(x)": GREEN, 'f(x+a)': BLUE, 'f(x)': GREEN})
        text_change_color.next_to(limit_def2)
        color_group = VGroup(limit_def2, text_change_color)
        color_group.arrange(center=True)
        self.play(TransformMatchingShapes(group, color_group, replace_mobject_with_target_in_scene=True), runtime=3)
        self.wait(2)
        # put braces on the colored parts of the equation
        y_brace = Brace(text_change_color[1], UP)
        y_brace_text = y_brace.get_tex(r'Y_2')
        y_brace.set_color(BLUE)
        y_brace_text.set_color(BLUE)
    

        y1_brace = Brace(text_change_color[3], UP)
        y1_brace_text = y1_brace.get_tex(r'Y_1')
        y1_brace.set_color(GREEN)
        y1_brace_text.set_color(GREEN)

        x2_brace = Brace(text_change_color[7], DOWN)
        x2_brace_text = x2_brace.get_tex(r'X_2')
        x2_brace.set_color(BLUE)
        x2_brace_text.set_color(BLUE)


        x1_brace = Brace(text_change_color[-2], DOWN)
        x1_brace_text = x1_brace.get_tex(r'X_1')
        x1_brace.set_color(GREEN)
        x1_brace_text.set_color(GREEN)

        self.play(GrowFromCenter(y_brace), Write(y_brace_text))
        self.play(GrowFromCenter(y1_brace), Write(y1_brace_text))
        self.play(GrowFromCenter(x2_brace), Write(x2_brace_text))
        self.play(GrowFromCenter(x1_brace), Write(x1_brace_text))
        self.wait(2)

        # Shrink the group and put it to the side
        entire_formula = VGroup(limit_def2, text_change_color, x1_brace, x1_brace_text, x2_brace, x2_brace_text, y1_brace, y1_brace_text, y_brace, y_brace_text)
        entire_formula.save_state()
        self.play(entire_formula.animate.to_edge(LEFT).scale(0.625))
        formula_title = Text('Derivative Formula').scale(0.7).to_edge(LEFT).shift(UP*1.85 + RIGHT*1.5)
        ul = Underline(formula_title)
        self.play(Write(formula_title))
        self.play(Write(ul))
        self.wait(2)

        # Write the slope formula here on the right side and compare the 2
        slope_formula = MathTex(r"{Slope}",  r"=",  r"{Rise \over Run}")
        slope_formula.to_edge(RIGHT).shift(LEFT*1.5 + UP*1)
        slope_title = Text('Slope Formula').scale(0.7).next_to(slope_formula, UP).shift(UP*0.25)
        ul_slope = Underline(slope_title)
        self.play(Write(slope_title))
        self.play(Write(ul_slope))
        self.play(Write(slope_formula))
        self.wait(2)

        # move brace text into the slope formula to show connection
        other_slope_formula = MathTex(r'{Slope}', r'=', r'{', r'Y_2', r'-', r'Y_1', r'\over', r'X_2', r'-', r'X_1', r'}', tex_to_color_map={'Y_2':BLUE, 'Y_1':GREEN, 'X_1':GREEN, 'X_2': BLUE})
        other_slope_formula.next_to(slope_formula, DOWN)
        group_copy = Group(y1_brace_text, y_brace_text, x1_brace_text, x2_brace_text).copy()
        self.play(TransformMatchingTex(group_copy, other_slope_formula), run_time=2)
        self.wait(2)

class Power_Rule(Scene):
    def construct(self):
        intro_text = Text('Derivation of Power Rule')
        self.play(Write(intro_text))
        self.wait(2)
        self.play(Unwrite(intro_text, reverse=False))

        formula_title = Text('Limit Definition of a Derivative').scale(0.625).to_edge(UP)
        underline_formula_title = Underline(formula_title)
        # Stick to either single or double quotes, also don't need to break things up if we are just mapping text to color
        derivative_formula = MathTex(r"\frac{d}{dx} f(x) = \lim_{a \to 0} { f(x+a) - f(x) \over a }")
        derivative_formula = MathTex(r"\frac{d}{dx}", r"f(x)", r"=", r"\lim_{a \to 0}")
        derivative_formula_right = MathTex(r"f(x+a)", r"-" ,r"f(x)", r"\over", r"a")
        derivative_formula.next_to(formula_title, DOWN)
        derivative_formula_right.next_to(derivative_formula, RIGHT)
        derivative_formula2 = MathTex(r"\frac{d}{dx}", r"x^n", r"=", r"\lim_{a \to 0}", r"{", r"(x+a)^n", r"-" ,r"x^n", r"\over", r"a", r"}")
        derivative_formula2.next_to(formula_title, DOWN)
        group = VGroup(derivative_formula, derivative_formula_right)
        group.arrange(center=True)
        group.next_to(formula_title, DOWN)
        self.play(Write(formula_title))
        self.play(Write(underline_formula_title))
        self.wait(2)
        self.play(Write(group))
        self.wait(2)
        self.play(TransformMatchingTex(group, derivative_formula2))
        self.wait(2)
        copy_df2 = derivative_formula2.copy()
        copy_df2.next_to(derivative_formula2, DOWN)
        copy_df2.shift(DOWN * 0.5)
        self.play(Transform(derivative_formula2, copy_df2))
        braces_polynomial = Brace(copy_df2[5], UP)
        # Change the color of the exponent and brace to emphasize what we are focusing on
        brace_text = braces_polynomial.get_text('Expand with Binomial Theorem')
        self.play(GrowFromCenter(braces_polynomial))
        self.play(Write(brace_text))
        self.wait(2)

        # binomial expansion
        brace_text2 = braces_polynomial.get_tex(r'x^n + \binom{n}{1} x^{n-1}a^1 + \binom{n}{2} x^{n-2}a^2 + \binom{n}{n-3}x^{n-3}a^3 + ...').scale(0.6).shift(DOWN*0.2)
        self.play(FadeTransform(brace_text, brace_text2))
        brace_group = VGroup(brace_text2, braces_polynomial, derivative_formula2)
        formula = MathTex(r'\frac{d}{dx} f(x) = \lim_{a \to 0} \frac{(x^n + \binom{n}{1} x^{n-1}a^1 + \binom{n}{2} x^{n-2}a^2 + \binom{n}{n-3}x^{n-3}a^3 + ...) - x^n}{a}')
        formula.to_edge(UP)
        formula.shift(DOWN*0.5).scale(0.7)
        self.play(FadeTransform(brace_group, formula))
        self.wait(2)
        formula2 = MathTex(r'\frac{d}{dx} f(x) = \lim_{a \to 0} \frac{x^n - x^n + \binom{n}{1} x^{n-1}a^1 + \binom{n}{2} x^{n-2}a^2 + \binom{n}{n-3}x^{n-3}a^3 + ...}{a}')
        formula3 =MathTex(r'\frac{d}{dx} f(x) = \lim_{a \to 0} \frac{\binom{n}{1} x^{n-1}a^1 + \binom{n}{2} x^{n-2}a^2 + \binom{n}{n-3}x^{n-3}a^3 + ...}{a}')
        formula2.to_edge(UP).shift(DOWN*0.5)
        formula3.to_edge(UP).shift(DOWN*0.5)
        formula2.scale(0.7)
        formula3.scale(0.7)
        
        self.play(TransformMatchingShapes(formula, formula2))
        self.wait(2)
        self.play(TransformMatchingShapes(formula2, formula3))
        self.wait(2)
        # To be worked on later, formula derivations don't really seem to be worth my time right now


class Graphing_Example(Scene):
    def construct(self):
        pass

class Example_Problem(Scene):
    def construct(self):
        # Structure of animation
        # Explain the problem and colorize each parametric equation
        # Explain the difference between intersection and collision with a 2d example
        # First remove a dimension and talk about the problem in a 2d setting
        # Answer both questions with that context
        # Bring back the 3 dimensions and answer the question again 
        # Do a 3 graph, then do a separate graph for each dimension

        title = Text('Week 2 Question 8 Explanation')
        self.play(Write(title))
        self.wait(2)
        self.play(Unwrite(title, reverse=False))
        self.wait(1)
        question = ImageMobject('media/images/IMG_8856E74ECEEE-1.jpeg')
        question.to_edge(UP, buff=0.5).scale(0.5)
        self.play(FadeIn(question))
        self.wait(2)
        self.play(FadeOut(question))
        self.wait(2)

        # Explain the difference between collision and intersection
        subsection_title1 = Text('Collision vs Intersection').scale(0.8).to_edge(UP)
        ul = Underline(subsection_title1)
        self.play(Write(subsection_title1))
        self.play(Write(ul))
        collision_def = Paragraph(r'Collision: When the paths of 2 objects intersect at the same time', t2c={'intersect at the same time': RED}).scale(0.7)
        intersection_def = Paragraph('Intersection: When the paths of 2 objects intersect at different \n or the same time', t2c={'intersect at different \n or the same time': BLUE}, alignment='left').scale(0.7)
        collision_def.next_to(ul, DOWN)
        intersection_def.next_to(collision_def, DOWN)
        intersection_def.to_edge(LEFT)
        collision_def.to_edge(LEFT)
        self.play(Write(collision_def))
        self.play(Write(intersection_def))
        self.wait(5)
        self.play(Unwrite(subsection_title1, reverse=False), Unwrite(ul, reverse=False), Unwrite(collision_def, reverse=False), Unwrite(intersection_def, reverse=False))
        self.wait(2)

        subsection_title2 = Text('Intersection Example').scale(0.7)
        subsection_title2.to_edge(LEFT+UP)
        ul2 = Underline(subsection_title2)
        self.play(Write(subsection_title2))
        self.play(Write(ul2))
        # Now go into examples of collisions and intersections
        # Make sure to emphasize the differences and how collision is a subset of intersection (stricter definition)
        e2 = ValueTracker(0.01)
        plane1 = NumberPlane(
           x_range=(-2,10,2),
           y_range=(-3,15,3),
           x_length=5,
           y_length=5, 
           axis_config={"include_numbers": True, 'include_tip':True},
           background_line_style={'stroke_color': GREEN}
        ).to_edge(LEFT)
        self.play(DrawBorderThenFill(plane1))
        graph_intersection1 = always_redraw(lambda: plane1.plot_parametric_curve(lambda t: [t+1, t], t_range=[0, e2.get_value()]).set_color(BLUE))
        graph_intersection1_dot = always_redraw(lambda: Dot(fill_color=BLUE).scale(0.7).move_to(graph_intersection1.get_end()))
        graph_intersection2 = always_redraw(lambda: plane1.plot_parametric_curve(lambda t: [t, t**0.5], t_range=[0, e2.get_value()]).set_color(RED))
        graph_intersection2_dot = always_redraw(lambda: Dot(fill_color=RED).scale(0.7).move_to(graph_intersection2.get_end()))
        eq1_int = MathTex(r'r_1(t) = ', r'<', r't+1', r',', r't', r'>').set_color(BLUE).scale(0.8).set_stroke(width=0.5,color=WHITE)
        eq2_int = MathTex(r'r_2(t) = ',r'<', r't', r',', r'\sqrt{t}', r'>').set_color(RED).scale(0.8).set_stroke(width=0.5,color=WHITE)
        eq1_int.next_to(plane1, UP).shift(DOWN)
        eq2_int.next_to(eq1_int, DOWN)
        t_text = Text('t = ').scale(0.7)
        t_text.next_to(eq2_int, DOWN)
        var1 = always_redraw(lambda: DecimalNumber(num_decimal_places=3).set_value(e2.get_value()).next_to(t_text, RIGHT).scale(0.7))
        self.play(Write(eq1_int), Write(eq2_int), Write(var1), Write(t_text))
        self.add(graph_intersection1, graph_intersection2)
        self.add(graph_intersection1_dot, graph_intersection2_dot)

        # Graph 2 parametric equations that intersect paths but do not collide
        # Adding value tracker that will be the updated value of time
        self.play(e2.animate.set_value(2.618), run_time=3, rate_func=smooth)
        self.wait(0.5)
        intersection_dot1 = Dot(fill_color=WHITE).scale(0.8).move_to(graph_intersection2.get_end())
        self.play(FadeIn(intersection_dot1))
        self.play(e2.animate.set_value(4), run_time=3, rate_func=smooth)
        

        subsection_title3 = Text('Collision Example').scale(0.7).to_edge(RIGHT + UP).shift(LEFT)
        ul3 = Underline(subsection_title3)
        self.play(Write(subsection_title3))
        self.play(Write(ul3))
        plane2 = NumberPlane(
           x_range=(-2,10,2),
           y_range=(-3,15,3),
           x_length=5,
           y_length=5, 
           axis_config={"include_numbers": True, 'include_tip':True},
           background_line_style={'stroke_color': GREEN}
        ).to_edge(RIGHT)
        self.play(DrawBorderThenFill(plane2))
        e = ValueTracker(0.01)
        graph_collision1 = always_redraw(lambda: plane2.plot_parametric_curve(lambda t: [t**2 + 1, t + 2], t_range=[0, e.get_value()]).set_color(BLUE))
        graph_collision2 = always_redraw(lambda: plane2.plot_parametric_curve(lambda t: [t+3, 3*t-2], t_range=[0, e.get_value()]).set_color(RED))
        graph_collision1_dot = always_redraw(lambda: Dot(fill_color=BLUE).scale(0.7).move_to(graph_collision1.get_end()))
        graph_collision2_dot = always_redraw(lambda: Dot(fill_color=RED).scale(0.7).move_to(graph_collision2.get_end()))
        eq1_coll = MathTex(r'r_1(t) = ' ,r'<', r't^2', r',', r't+2', r'>').set_color(BLUE).scale(0.6).set_stroke(width=0.5,color=WHITE)
        eq2_coll = MathTex(r'r_2(t) = ',r'<', r't+3', r',', r'3t-2', r'>').set_color(RED).scale(0.6).set_stroke(width=0.5,color=WHITE)
        eq1_coll.next_to(plane2, UP).shift(DOWN)
        eq2_coll.next_to(eq1_coll, DOWN)
        t2_text = Text('t = ').next_to(eq2_coll, DOWN).scale(0.7)
        var2 = always_redraw(lambda: DecimalNumber(num_decimal_places=3).set_value(e.get_value()).next_to(t2_text, RIGHT).scale(0.7))
        self.play(Write(eq1_coll), Write(eq2_coll), Write(var2), Write(t2_text))

        self.add(graph_collision1, graph_collision2, graph_collision1_dot, graph_collision2_dot)
        self.play(e.animate.set_value(2), run_time=3, rate_func=smooth)
        intersection_dot2 = Dot(fill_color=WHITE).scale(0.8).move_to(graph_collision1.get_end())
        self.play(FadeIn(intersection_dot2))
        self.wait(0.5)
        self.play(e.animate.set_value(2.5), run_time=3, rate_func=smooth)

        parametric_equation1= MathTex(r'r_1(t)', r'=', r'<', r't^2', r',', r'7t-12', r',', r't^2', r'>')
        parametric_equation2 = MathTex(r'r_2(t)', r'=', r'<', r'4t-3', r',', r't^2', r',', r'5t-6', r'>')

        parametric_equation1.to_edge(UP)
        parametric_equation2.next_to(parametric_equation1, DOWN)
        
        #self.play(Write(parametric_equation1))
        #self.play(Write(parametric_equation2))
        self.wait(2)

# start of second part of tutorial question walk through
class Example_Problem2(Scene):
    def construct(self):
        # go back to the original problem
        # first remove the z dimension from the problem and see if there is a collision or intersection on the x-y plane
        # afterwards bring back the z dimension and do a 3d graph
        # then graph each dimension separately
        # show how to set up the equations
        # show results and answers

        back_text = Text('Now back to the problem...').scale(0.8)
        self.play(Write(back_text))
        self.wait(2)
        self.play(Unwrite(back_text, reverse=False))

        parametric_equation1= MathTex(r'r_1(t)', r'=', r'<', r't^2', r',', r'7t-12', r',', r't^2', r'>').set_color(BLUE)
        parametric_equation2 = MathTex(r'r_2(t)', r'=', r'<', r'4t-3', r',', r't^2', r',', r'5t-6', r'>').set_color(RED)

        parametric_equation1_edited = MathTex(r'r_1(t)', r'=', r'<', r't^2', r',', r't^2', r'>').set_color(BLUE)
        parametric_equation2_edited = MathTex(r'r_2(t)', r'=', r'<', r'4t-3', r',', r'5t-6', r'>').set_color(RED)
        parametric_equation1.to_edge(UP)
        parametric_equation2.next_to(parametric_equation1, DOWN)
        parametric_equation1_edited.to_edge(UP)
        parametric_equation2_edited.next_to(parametric_equation1_edited, DOWN)
        cross1 = Cross(parametric_equation1[5])
        cross2 = Cross(parametric_equation2[5])

        self.play(Write(parametric_equation1), Write(parametric_equation2))
        self.wait(1)
        self.play(DrawBorderThenFill(cross1), DrawBorderThenFill(cross2))
        self.wait(2)
        self.play(TransformMatchingTex(parametric_equation1, parametric_equation1_edited), TransformMatchingTex(parametric_equation2, parametric_equation2_edited), FadeOut(cross1), FadeOut(cross2), run_time=2)
        self.wait(2)
        # shrink equations and bring to side
        # add graph of the new 2d parametric equations
        group = VGroup(parametric_equation1_edited, parametric_equation2_edited)
        graph = NumberPlane(
           x_range=(-10,15,2),
           y_range=(-10,15,2),
           x_length=8,
           y_length=5, 
           axis_config={"include_numbers": True, 'include_tip':True},
           background_line_style={'stroke_color': GREEN}
           ).to_edge(RIGHT)
        self.play(group.animate.scale(0.7).to_edge(LEFT))
        self.play(DrawBorderThenFill(graph))

        e = ValueTracker(0)
        parametric1 = always_redraw(lambda: graph.plot_parametric_curve(lambda t: [t**2, t**2], t_range=[0, max(0.1,e.get_value())]).set_color(BLUE))
        parametric2 = always_redraw(lambda: graph.plot_parametric_curve(lambda t: [4*t-3, 5*t-6], t_range=[0, max(0.1,e.get_value())]).set_color(RED))
        dot1 = always_redraw(lambda: Dot(fill_color=BLUE).scale(0.7).move_to(parametric1.get_end()))
        dot2 = always_redraw(lambda: Dot(fill_color=RED).scale(0.7).move_to(parametric2.get_end()))
        self.play(FadeIn(parametric1), FadeIn(parametric2), FadeIn(dot1), FadeIn(dot2))
        time_text = Text('t = ').scale(0.7).next_to(group, DOWN)
        time_var = always_redraw(lambda: DecimalNumber(2).set_value(e.get_value()).scale(0.7).next_to(time_text, RIGHT))
        self.play(Write(time_text), Write(time_var))
        time_table = MathTable([['t', 'r_1(t)', 'r_2(t)'],['1', '(1,1)','(1,-1)'],['2', '(4,4)', '(5, 4)'], ['3', '(9,9)', '(9,9)'], ['4', '(16,16)', '(13,14)']], include_outer_lines=True).next_to(time_text, DOWN).scale(0.65).shift(UP*0.5)
        
        column1 = time_table.get_columns()[1]
        column2 = time_table.get_columns()[2]
        for text in column1:
            text.set_color(BLUE).scale(1.1)
        for text in column2:
            text.set_color(RED).scale(1.1)

        self.play(FadeIn(time_table.get_rows()[0]), FadeIn(time_table.get_horizontal_lines()), FadeIn(time_table.get_vertical_lines()))

        for i in range(1,5):
            self.play(e.animate.set_value(i), run_time=2)
            self.play(FadeIn(time_table.get_rows()[i]))
            new_dot1 = Dot(fill_color=BLUE).move_to(parametric1.get_end())
            new_dot2 = Dot(fill_color=RED).move_to(parametric2.get_end())
            self.play(FadeIn(new_dot1), FadeIn(new_dot2))
        
        # create a table with important points and corresponding times
        # color code the dots on the graphs with the times on the table
        # add dot at collision point
        # add time label at collision point
        box = SurroundingRectangle(time_table.get_rows()[3])
        self.play(Create(box))
        # setting colors in table
        self.wait(2)
#3D animation of the graph, then graphing x, y, z separately
class Example_Problem3(Scene):
    # do a 3d graph of the parametric equations
    def construct(self):
        parametric_equation1= MathTex(r'r_1(t)', r'=', r'<', r't^2', r',', r'7t-12', r',', r't^2', r'>').set_color(BLUE)
        parametric_equation2 = MathTex(r'r_2(t)', r'=', r'<', r'4t-3', r',', r't^2', r',', r'5t-6', r'>').set_color(RED)
        parametric_equation1.to_edge(UP)
        parametric_equation2.next_to(parametric_equation1, DOWN)

        parametric_equation1_edited = MathTex(r'r_1(t)', r'=', r'<', r't^2', r',', r't^2', r'>').set_color(BLUE)
        parametric_equation2_edited = MathTex(r'r_2(t)', r'=', r'<', r'4t-3', r',', r'5t-6', r'>').set_color(RED)
        parametric_equation1_edited.to_edge(UP)
        parametric_equation2_edited.next_to(parametric_equation1_edited, DOWN)

        #re introduce the 3rd parameter in the scene
        self.play(Write(parametric_equation1_edited), Write(parametric_equation2_edited))
        self.wait(2)
        self.play(TransformMatchingTex(parametric_equation1_edited, parametric_equation1), TransformMatchingTex(parametric_equation2_edited, parametric_equation2))

        rect = SurroundingRectangle(parametric_equation1[5])
        rect2 = SurroundingRectangle(parametric_equation2[5])

        self.play(Create(rect), Create(rect2))
        self.wait(2)
        self.play(Uncreate(rect), Uncreate(rect2))
        self.wait(1)

        equation_group = VGroup(parametric_equation1, parametric_equation2)


        self.play(equation_group.animate.to_edge(UP+LEFT).scale(0.75))
        self.wait(1)

class Example_3d_scene(ThreeDScene):
    def construct(self):
        #new 3d scene
        #do a rotating scene first then change the camera angle so it shows the projection on all 3 planes
        # then match up and show how they all intersect at one time and point
        
        axes = ThreeDAxes(x_range=[-10,25],
                        y_range=[-10,25],
                        z_range=[-10,25])

        t_value = ValueTracker(0)
        
        curve1 = always_redraw(lambda: ParametricFunction(
            lambda t: np.array([
                t**2,
                7*t-12,
                t**2
            ], dtype=float), color=RED, t_range=np.array([0,t_value.get_value()], dtype=float))
        )
        curve2 = always_redraw(lambda: ParametricFunction(lambda t: np.array([
            4*t-3,
            t**2,
            5*t-6
        ], dtype=float), color= BLUE, t_range=np.array([0,t_value.get_value()], dtype=float)))
        self.renderer.camera.light_source.move_to(3*IN) # changes the source of the light
        self.set_camera_orientation(phi=70 * DEGREES, theta=250 * DEGREES, zoom=0.4)
        self.play(Create(axes))
        self.wait(1)
        self.add(curve1, curve2)
        self.begin_ambient_camera_rotation(rate=-0.5, about='theta')
        self.play(t_value.animate.set_value(3), run_time=3, rate_funct=smooth)
        self.wait(6)
        self.stop_ambient_camera_rotation(about='theta')


class VolumesOfRevolutions(ThreeDScene):

    def construct(self):
        e = ValueTracker(0.5*PI)
        self.set_camera_orientation(phi=30 * DEGREES, theta=-60 * DEGREES, zoom=0.6)
        self.begin_ambient_camera_rotation(rate=0.05, about='theta')
        

        axes = ThreeDAxes()
        
        curve1 = axes.plot(lambda x: sqrt(x), x_range=[0,4])
        #scales might be weird if we dont use axes.plot and plot the surface instead
        #make sure to use axes.c2p for best results

        surface1 = Surface(lambda u, v: axes.c2p(u**2, u * sin(v) , u * cos(v)), u_range=[0.001, 2], v_range=[0, 2*PI], resolution=8)
        area1 = axes.get_area(curve1, x_range=[0,4])
        area_group = VGroup(area1, curve1)
        rotation = Rotate(area_group, angle=2*PI, axis=RIGHT, about_point= axes.c2p(0,0,0), rate_func=linear, run_time=3, lag_ratio=0)
        animation_group = AnimationGroup(e.animate.set_value(5/2*PI), rate_func=linear, run_time=3, lag_ratio=0)
        area_group.initial_state = area_group.copy()
        def updater(obj):
            obj.become(obj.initial_state)
            obj.rotate(e.get_value()-PI/2,about_point=axes.c2p(0,0,0), axis=RIGHT)
        
        area_group.add_updater(updater)    
        curve_copy = curve1.copy()

        self.add(axes)

        self.wait(2)
        self.play(Create(area_group), Create(area_group.add_updater(updater)), Create(curve_copy))
        self.play(e.animate.set_value(5/2*PI), rate_func=linear, run_time=3, lag_ratio=0)
        self.play(Create(surface1))
        #make it so it just keeps on spinning
        self.play(e.animate.set_value(5*PI), rate_func=linear, run_time=3, lag_ratio=0)
        self.wait(6.5)

class Week_2_Tutorial(Scene):
    def construct(self):
        axis = Axes(x_range=[-15,15, 5], y_range=[-15,15, 5], x_length=7, y_length=7, tips=False, x_axis_config = {
        "numbers_to_include": range(-15, 16, 5),
    },
    y_axis_config = {
         "numbers_to_include": range(-15, 16, 5),
    })
        num_plane = NumberPlane(x_range=[-15,15, 3], y_range=[-15,15, 3], x_length=7, y_length=7)
        dot = Dot(num_plane.c2p(3,7), radius=DEFAULT_DOT_RADIUS*0.6, color=RED)
        text = MathTex(r'(3,7)', color=BLUE_A).scale(0.6).next_to(dot, UP).shift(DOWN*0.1)
        brace = BraceBetweenPoints(num_plane.c2p(3,7), num_plane.c2p(9,7)).shift(UP*0.1)
        brace_text = MathTex(r'radius = 6').scale(0.6).next_to(brace, DOWN)
        self.play(Write(num_plane), Write(axis))
        self.play(Create(axis.plot_parametric_curve(lambda t: [6*cos(t)+3, 6*sin(t)+7], t_range=[0,2*PI+0.5], color=GREEN)))
        self.play(DrawBorderThenFill(dot))
        self.play(Write(text))
        self.play(DrawBorderThenFill(brace), Write(brace_text))

        
class Week_2_Tutorial_b(Scene):
    def construct(self):
        equation_x = MathTex(r'x', r' = ', r'cos(t)', color=RED).scale(1)
        equation_y = MathTex(r'y', r' = ', r'sin(t)', color=RED).next_to(equation_x, DOWN).scale(1)
        self.play(Write(equation_x), Write(equation_y))
        self.play(equation_x.animate.to_edge(UP+RIGHT), equation_y.animate.to_edge(UP+RIGHT).shift(DOWN*0.7))
        time = ValueTracker(0.001)
        axis = Axes(x_range=[-2,2, 1], y_range=[-2,2, 1], x_length=7, y_length=7, tips=False, x_axis_config = {
        "numbers_to_include": range(-2, 3, 1),
    },
    y_axis_config = {
         "numbers_to_include": range(-2, 3, 1),
    })
        num_plane = NumberPlane(x_range=[-2,2, 1], y_range=[-2,2, 1], x_length=7, y_length=7)
        num_plane.shift(LEFT)
        axis.shift(LEFT)

        table = MathTable(
            [['t', 'x', 'y'],
            [0, 1,0],
            [r'\frac{\pi}{2}', r'0', '1'],
            [r'\pi', -1, 0],
            [r'\frac{3}{2}\pi', 0, -1]],
            include_outer_lines=True).scale(0.6).to_edge(RIGHT)
        top_dot = Dot(axis.c2p(0,1), color=BLUE)
        right_dot = Dot(axis.c2p(1,0), color=RED)
        left_dot = Dot(axis.c2p(-1,0), color=ORANGE)
        bottom_dot = Dot(axis.c2p(0,-1), color=YELLOW)

        self.play(Create(num_plane), Create(axis))
        self.play(Create(top_dot), Create(right_dot), Create(left_dot), Create(bottom_dot))
        self.play(Create(table))
        self.wait(1)

        curve = always_redraw(lambda: ParametricFunction(lambda t: num_plane.c2p(cos(t), sin(t)), t_range=[0, time.get_value()], color=GREEN))
        point = always_redraw(lambda: Dot(num_plane.c2p(cos(time.get_value()), sin(time.get_value())), color=GREEN)).scale(0.8)
        decimal_time = DecimalNumber(0, num_decimal_places=3, include_sign=True, unit=None)
        decimal_x = DecimalNumber(0, num_decimal_places=3, include_sign=True, unit=None)
        decimal_y = DecimalNumber(0, num_decimal_places=3, include_sign=True, unit=None)
        decimal_time.add_updater(lambda d: d.set_value(time.get_value()))
        decimal_x.add_updater(lambda d: d.set_value(cos(time.get_value())))
        decimal_y.add_updater(lambda d: d.set_value(sin(time.get_value())))

        self.play(Create(curve), Create(point))
        self.play(time.animate.set_value(2*PI), run_time=4, rate_func=linear)
        # replace with new text and add a new number plane that is bigger

        bigger_number_plane = NumberPlane(x_range=[-15,15, 3], y_range=[-15,15, 3], x_length=7, y_length=7).shift(LEFT)
        bigger_axis = Axes(x_range=[-15,15, 3], y_range=[-15,15, 3], x_length=7, y_length=7, tips=False, x_axis_config = {
        "numbers_to_include": range(-15, 16, 3),
    },
    y_axis_config = {
         "numbers_to_include": range(-15, 16, 3),
    }).shift(LEFT)
        curve_new = ParametricFunction(lambda t: bigger_number_plane.c2p(cos(t), sin(t)), t_range=[0, 2*PI], color=GREEN)
        new_point = always_redraw(lambda: Dot(bigger_number_plane.c2p(cos(time.get_value()), sin(time.get_value())), color=GREEN))
        self.play(axis.animate.become(bigger_axis), num_plane.animate.become(bigger_number_plane), TransformMatchingShapes(curve, curve_new)
        , TransformMatchingShapes(point, new_point),
        top_dot.animate.move_to(bigger_axis.c2p(0,1)), right_dot.animate.move_to(bigger_axis.c2p(1,0)), left_dot.animate.move_to(bigger_axis.c2p(-1,0)), bottom_dot.animate.move_to(bigger_axis.c2p(0,-1)))

        transform_equation_x = MathTex(r'x', r' = ', r'6', r'cos(t)', color=RED).scale(1)
        transform_equation_y = MathTex(r'y', r' = ', r'6', r'sin(t)', color=RED).scale(1)

        bigger_circle = ParametricFunction(lambda t: bigger_number_plane.c2p(6*cos(t), 6*sin(t)), t_range=[0, 2*PI], color=GREEN)
        # rectangles to highlight the changes
        
        self.wait(2)
        newer_point = Dot(bigger_number_plane.c2p(6*cos(time.get_value()), 6*sin(time.get_value())), color=GREEN)
        
        
        self.play(TransformMatchingTex(equation_x, transform_equation_x.to_corner(UP+RIGHT)),
            TransformMatchingTex(equation_y, transform_equation_y.next_to(transform_equation_x, DOWN)))
        rect1 = SurroundingRectangle(transform_equation_x[2])
        rect2 = SurroundingRectangle(transform_equation_y[2])
        self.play(Create(rect1), Create(rect2))
        self.wait(1)
        self.play(Uncreate(rect1), Uncreate(rect2))
        self.wait(1)
        self.play(
            table.get_entries((2,2)).animate.become(MathTex(6).scale(0.6).move_to(table.get_entries((2,2)).get_center())),
            table.get_entries((4,2)).animate.become(MathTex(-6).scale(0.6).move_to(table.get_entries((4,2)).get_center())),
            table.get_entries((3,3)).animate.become(MathTex(6).scale(0.6).move_to(table.get_entries((3,3)).get_center())),
            table.get_entries((5,3)).animate.become(MathTex(-6).scale(0.6).move_to(table.get_entries((5,3)).get_center()))
            )


        self.play(
            TransformMatchingShapes(curve_new, bigger_circle),
            TransformMatchingShapes(new_point, newer_point),
            top_dot.animate.move_to(bigger_axis.c2p(0,6)), right_dot.animate.move_to(bigger_axis.c2p(6,0)), left_dot.animate.move_to(bigger_axis.c2p(-6,0)), bottom_dot.animate.move_to(bigger_axis.c2p(0,-6))
            )
        self.wait(1)
        self.remove(newer_point)

        slide_equation_x = MathTex(r'x', r' = ', r'6', r'cos(t)', r' + 3', color=RED).scale(1)
        slide_equation_y = MathTex(r'y', r' = ', r'6', r'sin(t)', r' + 7', color=RED).scale(1)

        curve_3 = ParametricFunction(lambda t: bigger_number_plane.c2p(6*cos(t) + 3, 6*sin(t)), t_range=[0, 2*PI], color=GREEN)
        self.play(TransformMatchingTex(transform_equation_x, slide_equation_x.to_corner(UP+RIGHT)))
        rect = SurroundingRectangle(slide_equation_x[-1])
        self.play(Create(rect))
        self.wait(1)
        self.play(Uncreate(rect))
        self.play(
            table.get_entries((2,2)).animate.become(MathTex(9).scale(0.6).move_to(table.get_entries((2,2)).get_center())),
            table.get_entries((3,2)).animate.become(MathTex(3).scale(0.6).move_to(table.get_entries((3,2)).get_center())),
            table.get_entries((4,2)).animate.become(MathTex(-3).scale(0.6).move_to(table.get_entries((4,2)).get_center())),
            table.get_entries((5,2)).animate.become(MathTex(3).scale(0.6).move_to(table.get_entries((5,2)).get_center()))
            )

        self.play(TransformMatchingShapes(bigger_circle, curve_3), 
                top_dot.animate.move_to(bigger_axis.c2p(3,6)), right_dot.animate.move_to(bigger_axis.c2p(9,0)), left_dot.animate.move_to(bigger_axis.c2p(-3,0)), bottom_dot.animate.move_to(bigger_axis.c2p(3,-6))
        )

        curve_4 = ParametricFunction(lambda t: bigger_number_plane.c2p(6*cos(t) + 3, 6*sin(t) + 7), t_range=[0, 2*PI], color=GREEN)
        self.play(TransformMatchingTex(transform_equation_y, slide_equation_y.next_to(slide_equation_x, DOWN)))
        rect = SurroundingRectangle(slide_equation_y[-1])
        self.play(Create(rect))
        self.wait(1)
        self.play(Uncreate(rect))
        self.play(
            table.get_entries((2,3)).animate.become(MathTex(7).scale(0.6).move_to(table.get_entries((2,3)).get_center())),
            table.get_entries((3,3)).animate.become(MathTex(13).scale(0.6).move_to(table.get_entries((3,3)).get_center())),
            table.get_entries((4,3)).animate.become(MathTex(7).scale(0.6).move_to(table.get_entries((4,3)).get_center())),
            table.get_entries((5,3)).animate.become(MathTex(1).scale(0.6).move_to(table.get_entries((5,3)).get_center()))
            )
        self.play(TransformMatchingShapes(curve_3, curve_4),
                    top_dot.animate.move_to(bigger_axis.c2p(3,13)), right_dot.animate.move_to(bigger_axis.c2p(9,7)), left_dot.animate.move_to(bigger_axis.c2p(-3,7)), bottom_dot.animate.move_to(bigger_axis.c2p(3,1))
)
        self.wait(1)
        # next steps, create a table and show how the transformations affect 4 points on the circle

class Sussy(Scene):
    def construct(self):
        grid = Axes(x_range=[-15,15, 3], y_range=[-15,15, 3], x_length=7, y_length=7)
        #eq1 = grid.plot_implicit_curve(lambda x,y:((x-0.3)**2)/16 + ((y-1.1)**2)/30-1, x_range=[-2.5, 3.736])
        eq1 = ImplicitFunction(lambda x, y: ((x-0.3)**2)/16 + ((y-1.1)**2)/30-1, x_range=[-2.5, 3.736]).scale(0.6)
        #eq2 = grid.plot_implicit_curve(lambda x,y:((x-0.4)**2)/12 + ((y+0.5)**2)/100-1, y_range=[-4.235,5.03], x_range=[-100, 2])
        
        self.play(Create(grid), Create(eq1))

class Week3Example(Scene):
    def parametric_curve(self,t):
        return[2+t, t**3 - t]

    def tangent_curve(self, t):
        arr = np.array([1, 3*t**2 - 1])
        return arr
    def norm_tangent_curve(self, t):
        arr = np.array([1, 3*t**2 - 1])
        return (arr/np.linalg.norm(arr))

    def min_time(self, t, release_t):
        return min(release_t, t)

    point = [5,-3]
    time_release = 0
    starting_time = -4
    end_time = 4

    def fixed_tangent_curve(self, t_0, t):
        equation = self.parametric_curve(t_0) + (t-t_0)*self.tangent_curve(t_0)
        return equation

    def construct(self):
        grid = Axes(x_range=[-15,15, 3], y_range=[-15,15, 3], x_length=7, y_length=7)
        time = ValueTracker(self.starting_time) #time for tangent line and red dot
        time2 = ValueTracker(self.starting_time) 
        path_equation = MathTex(r'r(t) = <t-2, t^2 +1>', color=BLUE).to_corner(UP + RIGHT)
        der_path_equation = MathTex(r"r'(t) = <1, 2t>", color=RED).next_to(path_equation, DOWN)
        
        
        path = ParametricFunction(lambda t:grid.c2p(*self.parametric_curve(t)), t_range=[-4, 5]).set_opacity(0.5).set_color(BLUE).set_fill(opacity=0)
        tangent_path = always_redraw(lambda: Arrow(stroke_width=3, color=RED).put_start_and_end_on(grid.c2p(*(self.parametric_curve(time.get_value()) - 2*self.tangent_curve(time.get_value()) )), grid.c2p(*(self.parametric_curve(time.get_value()) + 2*self.tangent_curve(time.get_value())))))
        tangent_line = always_redraw(lambda: ParametricFunction(lambda t: grid.c2p(*(t*(self.norm_tangent_curve(self.min_time(self.time_release, time.get_value()))) + self.parametric_curve(self.min_time(self.time_release, time.get_value())))), t_range=[-5,15]).set_color(RED).set_opacity(0.5))
        dot = Dot(grid.c2p(*self.point), color=GREEN)

        def position(t, t_release):
            if t>=t_release:
                return self.fixed_tangent_curve(t_release, t - t_release)
            else:
                return self.parametric_curve(t)

        indy_dot = always_redraw(lambda: Dot(color=RED).move_to(grid.c2p(*position(time.get_value(), self.time_release))))
        curve_dot = always_redraw(lambda: Dot(grid.c2p(*self.parametric_curve(time.get_value())), color=BLUE))
        
        animation_group = AnimationGroup(time.animate.set_value(-2), time2.animate.set_value(-2), run_time=3, rate_func=linear)
        self.add(indy_dot)
        self.play(Create(grid), Create(dot), Create(curve_dot), Create(tangent_line), Create(path), Write(path_equation), Write(der_path_equation))
        
        self.play(time.animate.set_value(self.end_time), run_time = 5)
        

