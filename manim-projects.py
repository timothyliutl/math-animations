from cmath import sin
from tkinter import BOTTOM, CENTER, TOP
from typing_extensions import runtime
from manim import *
from matplotlib import mathtext
from sympy import binomial

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

        parametric_equation1_edited = MathTex(r'r_1(t)', r'=', r'<', r't^2', r',', r'7t-12', r'>').set_color(BLUE)
        parametric_equation2_edited = MathTex(r'r_2(t)', r'=', r'<', r'4t-3', r',', r't^2', r'>').set_color(RED)
        parametric_equation1.to_edge(UP)
        parametric_equation2.next_to(parametric_equation1, DOWN)
        parametric_equation1_edited.to_edge(UP)
        parametric_equation2_edited.next_to(parametric_equation1_edited, DOWN)
        cross1 = Cross(parametric_equation1[7])
        cross2 = Cross(parametric_equation2[7])

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
           x_range=(-2,20,2),
           y_range=(-3,15,3),
           x_length=8,
           y_length=5, 
           axis_config={"include_numbers": True, 'include_tip':True},
           background_line_style={'stroke_color': GREEN}
           ).to_edge(RIGHT)
        self.play(group.animate.scale(0.7).to_edge(LEFT))
        self.play(DrawBorderThenFill(graph))
        

        