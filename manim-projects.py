from cmath import sin
from tkinter import CENTER, TOP
from typing_extensions import runtime
from manim import *
from matplotlib import mathtext

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


