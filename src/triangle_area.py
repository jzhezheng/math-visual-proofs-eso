from manim import *


class TriangleAreaRectangle(Scene):
    """
    Geometric proof that triangle area is half the area of its bounding rectangle.
    Demonstrates the fundamental relationship between triangle and rectangle areas.
    """

    def construct(self):
        # ========== RECTANGLE CONSTRUCTION ==========
        # Create a rectangle representing the bounding box
        rectangle = Square(side_length=3, color=BLUE, stroke_width=3)
        rectangle.set_fill(BLUE, opacity=0.3)
        rectangle.move_to(np.array([-2, 0, 0]))

        # Dimension labels
        base_label = MathTex("b").next_to(rectangle, DOWN)
        height_label = MathTex("h").next_to(rectangle, RIGHT)

        # Display rectangle and dimensions
        self.play(Create(rectangle))
        self.play(Write(base_label), Write(height_label))
        self.wait(1)

        # ========== TRIANGLE DECOMPOSITION ==========
        # Draw diagonal to divide rectangle into two congruent triangles
        diagonal = Line(rectangle.get_corner(DL), rectangle.get_corner(UR),
                        color=RED, stroke_width=3)
        self.play(Create(diagonal))
        self.wait(1)

        # Define the two congruent triangles formed by the diagonal
        left_triangle = Polygon(
            rectangle.get_corner(DL),
            rectangle.get_corner(UL),
            rectangle.get_corner(UR),
            color=GREEN,
            fill_opacity=0.5,
            stroke_width=2
        )

        right_triangle = Polygon(
            rectangle.get_corner(DL),
            rectangle.get_corner(DR),
            rectangle.get_corner(UR),
            color=YELLOW,
            fill_opacity=0.5,
            stroke_width=2
        )

        # Transform rectangle into two triangles
        self.play(
            FadeOut(rectangle),
            FadeOut(diagonal),
            FadeIn(left_triangle),
            FadeIn(right_triangle),
        )
        self.wait(1)

        # Emphasize that each triangle has half the area
        self.play(FadeOut(left_triangle))  # Focus on one triangle
        self.wait(1)

        # ========== AREA RELATIONSHIP DERIVATION ==========
        # Rectangle area formula
        rectangle_area_formula = MathTex(r"A_{\text{rectangle}} = b \cdot h") \
            .scale(1.5).move_to(np.array([3.5, 1, 0]))
        self.play(Write(rectangle_area_formula))
        self.wait(2)

        # Triangle area as half of rectangle area
        triangle_area_relationship = MathTex(
            r"A_{\text{triangle}} = \frac{A_{\text{rectangle}}}{2}"
        ).next_to(rectangle_area_formula, DOWN)
        self.play(Write(triangle_area_relationship))
        self.wait(1)

        # Final triangle area formula
        triangle_area_formula = MathTex(r"A = \frac{b \cdot h}{2}") \
            .next_to(triangle_area_relationship, DOWN)
        self.play(Write(triangle_area_formula))
        self.wait(2)

        # Conclusion statement
        conclusion_text = Tex(
            "The area of any triangle rectangle is exactly half the area of its bounding rectangle."
        ).to_edge(DOWN).scale(0.75).set_color(BLUE)
        self.play(Write(conclusion_text))
        self.wait(3)


class TriangleAreaInteriorAltitude(Scene):
    def construct(self):
        # ========== VERTEX COORDINATES DEFINITION ==========
        # Define triangle vertices for the case with interior altitude
        vertex_A = np.array([-2, 2, 0])  # Apex vertex
        vertex_B = np.array([2, 0, 0])  # Right base vertex
        vertex_C = np.array([-2, 0, 0])  # Left base vertex (foot of altitude)
        vertex_D = np.array([-3, 0, 0])  # Extension point for altitude visualization

        # ========== GEOMETRIC ELEMENTS CONSTRUCTION ==========
        # Main triangle ABC
        main_triangle = Polygon(vertex_A, vertex_B, vertex_C, color=BLUE, stroke_width=3)

        # Altitude from A to line BC (extended to point D for clarity)
        altitude_line = DashedLine(vertex_A, vertex_D, color=YELLOW, stroke_width=2)

        # Base line from C to B CD
        extentended_base_line = DashedLine(vertex_C, vertex_D, color=YELLOW, stroke_width=2)

        # Vertex labels
        label_A = MathTex("A").next_to(vertex_A, UP)
        label_B = MathTex("B").next_to(vertex_B, DOWN)
        label_C = MathTex("C").next_to(vertex_C, DOWN)
        label_D = MathTex("D").next_to(vertex_D, DOWN)

        # Two right triangles formed by the altitude
        right_triangle_ACD = Polygon(vertex_A, vertex_C, vertex_D, color=GREEN,
                                     fill_opacity=0.4, stroke_width=2)
        right_triangle_ABD = Polygon(vertex_A, vertex_B, vertex_D, color=RED,
                                     fill_opacity=0.4, stroke_width=2)

        # Group all elements for positioning
        all_elements = VGroup(
            main_triangle, altitude_line, extentended_base_line,
            right_triangle_ACD, right_triangle_ABD,
            label_A, label_B, label_C, label_D
        )
        all_elements.shift(LEFT * 3.5)  # Shift left to make space for formulas

        # ========== ANIMATION SEQUENCE ==========
        # Display main triangle and vertex labels
        self.play(Create(main_triangle), run_time=2)
        self.play(Write(label_A), Write(label_B), Write(label_C))
        self.wait(1)

        # Show altitude and its foot label
        self.play(Create(altitude_line), Write(label_D))
        self.play(Create(extentended_base_line))
        self.wait(1)

        # Reveal the two component right triangles
        self.play(FadeIn(right_triangle_ACD), FadeIn(right_triangle_ABD))
        self.wait(1)

        # ========== AREA FORMULA DERIVATION ==========
        # Step 1: Total area equals sum of two right triangle areas
        area_decomposition = MathTex(
            r"\text{Area}_{ABC} = \text{Area}_{ACD} + \text{Area}_{ABD}"
        ).to_edge(UP).shift(RIGHT * 2)
        self.play(Write(area_decomposition))
        self.wait(1)

        # Step 2: Apply area formula for right triangles
        area_formulas = MathTex(
            r"= \frac{1}{2} \cdot CD \cdot AD + \frac{1}{2} \cdot DB \cdot AD"
        ).next_to(area_decomposition, DOWN * 1.5)
        self.play(Write(area_formulas))
        self.wait(1)

        # Step 3: Factor out common terms
        factored_expression = MathTex(
            r"= \frac{1}{2} \cdot AD \cdot (CD + DB)"
        ).next_to(area_formulas, DOWN * 1.5)
        self.play(Write(factored_expression))
        self.wait(1)

        # Step 4: Simplify using segment addition (CD + DB = CB)
        simplified_expression = MathTex(
            r"= \frac{1}{2} \cdot AD \cdot CB"
        ).next_to(factored_expression, DOWN * 1.5)
        self.play(Write(simplified_expression))
        self.wait(1)

        # Final triangle area formula
        final_formula = MathTex(
            r"\text{Area}_{ABC} = \frac{1}{2} \cdot \text{base} \cdot \text{height}"
        ).next_to(simplified_expression, DOWN * 1.5).set_color(YELLOW)
        self.play(Write(final_formula))
        self.wait(2)

        # Conclusion statement
        conclusion_text = Tex(
            "The area formula remains valid when the altitude lies inside the triangle."
        ).next_to(final_formula, DOWN * 1.5).shift(LEFT * 1.5).set_color(GREEN).scale(0.75)
        self.play(Write(conclusion_text))
        self.wait(3)


class TriangleAreaExteriorAltitude(Scene):
    """
    Geometric demonstration of triangle area formula when the altitude falls outside the triangle.
    Shows how the area can be expressed as the difference of two right triangles.
    """

    def construct(self):
        # ========== VERTEX COORDINATES DEFINITION ==========
        # Define triangle vertices for the case with exterior altitude
        vertex_A = np.array([-2, 2, 0])  # Apex vertex
        vertex_B = np.array([2, -1, 0])  # Right base vertex
        vertex_C = np.array([0, -1, 0])  # Left base vertex
        vertex_D = np.array([-2, -1, 0])  # Foot of altitude (outside triangle)

        # ========== GEOMETRIC ELEMENTS CONSTRUCTION ==========
        # Main triangle ABC
        main_triangle = Polygon(vertex_A, vertex_B, vertex_C, color=BLUE, stroke_width=3)

        # Altitude lines (dashed for extension outside triangle)
        altitude_main = DashedLine(vertex_A, vertex_D, color=YELLOW, stroke_width=2)
        base_extension = DashedLine(vertex_C, vertex_D, color=YELLOW, stroke_width=2)

        # Vertex labels
        label_A = MathTex("A").next_to(vertex_A, UP)
        label_B = MathTex("B").next_to(vertex_B, DOWN)
        label_C = MathTex("C").next_to(vertex_C, DOWN)
        label_D = MathTex("D").next_to(vertex_D, DOWN)

        # Component triangles for area decomposition
        triangle_ACD = Polygon(vertex_A, vertex_C, vertex_D, color=YELLOW,
                               fill_opacity=0.4, stroke_width=2)
        triangle_ACB = Polygon(vertex_A, vertex_C, vertex_B, color=BLUE,
                               fill_opacity=0.4, stroke_width=2)
        triangle_ABD = Polygon(vertex_A, vertex_B, vertex_D, color=RED,
                               fill_opacity=0.4, stroke_width=2)

        # Group all elements for positioning
        all_elements = VGroup(
            main_triangle, altitude_main, base_extension,
            triangle_ACD, triangle_ABD, triangle_ACB,
            label_A, label_B, label_C, label_D
        )
        all_elements.shift(LEFT * 3.5)

        # ========== ANIMATION SEQUENCE ==========
        # Display main triangle and vertex labels
        self.play(Create(main_triangle), run_time=2)
        self.play(Write(label_A), Write(label_B), Write(label_C))
        self.wait(1)

        # Show altitude construction and extension point
        self.play(Create(altitude_main), Create(base_extension), Write(label_D))
        self.wait(1)

        # Reveal component triangles in logical order
        self.play(FadeIn(triangle_ACB))  # Main triangle area
        self.wait(1)
        self.play(FadeIn(triangle_ACD))  # External triangle to be subtracted
        self.wait(1)
        self.play(FadeIn(triangle_ABD))  # Large enclosing triangle
        self.wait(1)

        # ========== AREA FORMULA DERIVATION ==========
        # Step 1: Area as difference of two larger triangles
        area_difference = MathTex(
            r"\text{Area}_{ABC} = \text{Area}_{ABD} - \text{Area}_{ACD}"
        ).to_edge(UP).shift(RIGHT * 2)
        self.play(Write(area_difference))
        self.wait(1)

        # Step 2: Apply area formula for right triangles
        area_calculation = MathTex(
            r"= \frac{1}{2} \cdot DB \cdot AD - \frac{1}{2} \cdot DC \cdot AD"
        ).next_to(area_difference, DOWN * 1.5)
        self.play(Write(area_calculation))
        self.wait(1)

        # Step 3: Factor out common terms
        factored_difference = MathTex(
            r"= \frac{1}{2} \cdot AD \cdot (DB - DC)"
        ).next_to(area_calculation, DOWN * 1.5)
        self.play(Write(factored_difference))
        self.wait(1)

        # Step 4: Simplify using segment subtraction (DB - DC = CB)
        simplified_difference = MathTex(
            r"= \frac{1}{2} \cdot AD \cdot CB"
        ).next_to(factored_difference, DOWN * 1.5)
        self.play(Write(simplified_difference))
        self.wait(1)

        # Final triangle area formula
        final_formula = MathTex(
            r"\text{Area}_{ABC} = \frac{1}{2} \cdot \text{base} \cdot \text{height}"
        ).next_to(simplified_difference, DOWN * 1.5).set_color(YELLOW)
        self.play(Write(final_formula))
        self.wait(2)

        # Conclusion statement
        conclusion_text = Tex(
            "The area formula remains valid when the altitude falls outside the triangle."
        ).next_to(final_formula, DOWN * 1.5).shift(LEFT * 1.5).set_color(GREEN)
        self.play(Write(conclusion_text))
        self.wait(3)
