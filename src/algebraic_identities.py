from manim import *


class SumSquare(Scene):
    """
    Geometric demonstration of the square of a sum formula: (a + b)² = a² + 2ab + b²
    Uses area decomposition of a square into smaller squares and rectangles.
    """

    def construct(self):
        # ========== PARAMETERS INITIALIZATION ==========
        LENGTH_A = 2.0  # Length of side a
        LENGTH_B = 1.0  # Length of side b

        # ========== TITLE AND INTRODUCTION ==========
        title = MathTex(r"\text{Square of a Sum: } (a+b)^2").to_edge(UP)
        self.play(Write(title))

        # ========== COLOR SCHEME DEFINITION ==========
        COLOR_A_SQUARE = BLUE  # Color for a² area
        COLOR_B_SQUARE = YELLOW  # Color for b² area
        COLOR_AB_RECTANGLE = RED  # Color for ab areas

        # ========== GEOMETRIC CONSTRUCTION ==========
        # Position the large square at origin
        square_origin = ORIGIN

        # Construct the four components of the large square
        # Large square representing a²
        square_a2 = Square(
            side_length=LENGTH_A,
            color=WHITE,
            fill_color=COLOR_A_SQUARE,
            fill_opacity=0.7
        ).move_to(square_origin + LEFT * LENGTH_B / 2 + DOWN * LENGTH_B / 2)

        # Small square representing b²
        square_b2 = Square(
            side_length=LENGTH_B,
            color=WHITE,
            fill_color=COLOR_B_SQUARE,
            fill_opacity=0.7
        ).move_to(square_origin + RIGHT * LENGTH_A / 2 + UP * LENGTH_A / 2)

        # First rectangle representing ab
        rectangle_ab1 = Rectangle(
            width=LENGTH_B,
            height=LENGTH_A,
            color=WHITE,
            fill_color=COLOR_AB_RECTANGLE,
            fill_opacity=0.7
        ).move_to(square_origin + RIGHT * LENGTH_A / 2 + DOWN * LENGTH_B / 2)

        # Second rectangle representing ab
        rectangle_ab2 = Rectangle(
            width=LENGTH_A,
            height=LENGTH_B,
            color=WHITE,
            fill_color=COLOR_AB_RECTANGLE,
            fill_opacity=0.7
        ).move_to(square_origin + LEFT * LENGTH_B / 2 + UP * LENGTH_A / 2)

        # ========== AREA LABELS ==========
        label_a2 = MathTex("a^2").move_to(square_a2.get_center())
        label_b2 = MathTex("b^2").move_to(square_b2.get_center())
        label_ab1 = MathTex("ab").move_to(rectangle_ab1.get_center())
        label_ab2 = MathTex("ab").move_to(rectangle_ab2.get_center())

        # ========== DIMENSION BRACES ==========
        # Vertical brace on left side showing a and b segments
        top_left_point = rectangle_ab2.get_corner(DL)
        bottom_left_point = square_a2.get_corner(DL)
        brace_left_a = BraceBetweenPoints(top_left_point, bottom_left_point, LEFT)
        brace_label_a = brace_left_a.get_tex("a")

        top_left_point2 = rectangle_ab2.get_corner(UL)
        bottom_left_point2 = square_a2.get_corner(UL)
        brace_left_b = BraceBetweenPoints(top_left_point2, bottom_left_point2, LEFT)
        brace_label_b = brace_left_b.get_tex("b")

        # Horizontal brace at bottom showing total length a + b
        bottom_left_point = square_a2.get_corner(DL)
        bottom_right_point = rectangle_ab1.get_corner(DR)
        brace_bottom_total = BraceBetweenPoints(bottom_left_point, bottom_right_point, DOWN)
        brace_label_total = brace_bottom_total.get_tex("a + b")

        # ========== ALGEBRAIC FORMULAS ==========
        # Step-by-step derivation formulas
        formula_area_definition = MathTex(r"\text{Area of square} = \text{side}^2")
        formula_side_expression = MathTex(r"= (a + b)^2")
        formula_area_sum_text = MathTex(r"\text{Area of square} ")
        formula_area_sum_description = MathTex(r"= \text{sum of small areas}")
        formula_area_expanded = MathTex(r"= a^2 + b^2 + 2ab")

        # Final simplified formula
        formula_left_side = MathTex(r"(a + b)^2")
        formula_equals = MathTex(r"=")
        formula_right_side = MathTex(r"a^2 + 2ab + b^2")

        # ========== SCENE ORGANIZATION ==========
        # Group all geometric elements for positioning
        geometric_elements = VGroup(
            square_a2, square_b2, rectangle_ab1, rectangle_ab2,
            label_a2, label_b2, label_ab1, label_ab2
        )
        geometric_elements.shift(LEFT * 3)

        # Position braces with the geometric elements
        brace_left_a.shift(LEFT * 3)
        brace_label_a.shift(LEFT * 3)
        brace_left_b.shift(LEFT * 3)
        brace_label_b.shift(LEFT * 3)
        brace_bottom_total.shift(LEFT * 3)
        brace_label_total.shift(LEFT * 3)

        # ========== ANIMATION SEQUENCE ==========
        # Display geometric construction
        self.play(FadeIn(square_a2, square_b2, rectangle_ab1, rectangle_ab2))
        self.play(Write(label_a2), Write(label_b2), Write(label_ab1), Write(label_ab2))
        self.wait(1)

        # Show dimension measurements
        self.play(Create(brace_left_a), Write(brace_label_a))
        self.play(Create(brace_bottom_total), Write(brace_label_total))
        self.play(Create(brace_left_b), Write(brace_label_b))
        self.wait(1)

        # Position and display step-by-step formulas
        formula_area_definition.move_to(ORIGIN).shift(RIGHT * 2.5, UP * 1.5)
        formula_side_expression.next_to(formula_area_definition, DOWN)
        formula_area_sum_text.next_to(formula_side_expression, DOWN)
        formula_area_sum_description.next_to(formula_area_sum_text, DOWN)
        formula_area_expanded.next_to(formula_area_sum_description, DOWN)

        formula_steps_group = VGroup(
            formula_area_definition, formula_side_expression,
            formula_area_sum_text, formula_area_sum_description, formula_area_expanded
        )

        # Position final formula elements
        formula_equals.move_to(ORIGIN).shift(UP * 0.3, RIGHT * 2.5)
        formula_left_side.next_to(formula_equals, UP)
        formula_right_side.next_to(formula_equals, DOWN)

        # Animate formula derivation
        self.play(Write(formula_area_definition))
        self.wait(1)
        self.play(Write(formula_side_expression))
        self.wait(1)
        self.play(Write(formula_area_sum_text))
        self.wait(1)
        self.play(Write(formula_area_sum_description))
        self.wait(1)
        self.play(Write(formula_area_expanded))
        self.play(FadeOut(formula_steps_group), run_time=2.5)
        self.wait(1)

        # Display final formula
        self.play(Write(formula_left_side))
        self.wait(1)
        self.play(Write(formula_equals))
        self.wait(1)
        self.play(Write(formula_right_side))
        self.wait(3)


class DifferenceSquare(Scene):
    """
    Geometric demonstration of the square of a difference formula: (a - b)² = a² - 2ab + b²
    Shows the area decomposition and correction for over-subtraction.
    """

    def construct(self):
        # ========== PARAMETERS INITIALIZATION ==========
        LENGTH_A = 3.5  # Length of side a
        LENGTH_B = 1.0  # Length of side b
        LENGTH_A_MINUS_B = LENGTH_A - LENGTH_B  # Length of side (a - b)

        # ========== COLOR SCHEME DEFINITION ==========
        COLOR_LARGE_SQUARE = BLUE  # Color for a² area
        COLOR_TARGET_SQUARE = GREEN  # Color for (a-b)² area
        COLOR_SUBTRACT_RECTANGLE = RED  # Color for subtracted ab areas
        COLOR_CORRECTION_SQUARE = YELLOW  # Color for b² correction

        # ========== TITLE AND INTRODUCTION ==========
        title = MathTex(r"\text{Square of a Difference: } (a-b)^2").to_edge(UP)
        self.play(Write(title))

        # ========== LARGE SQUARE CONSTRUCTION ==========
        # Create the large square representing a²
        large_square = Square(side_length=LENGTH_A, color=COLOR_LARGE_SQUARE, fill_opacity=0.2)
        large_square.to_edge(LEFT, buff=2.75)

        # Dimension braces for the large square
        brace_bottom = Brace(large_square, DOWN, buff=0.1)
        label_bottom_a = MathTex("a").next_to(brace_bottom, DOWN)

        brace_left_full = Brace(large_square, LEFT, buff=0.1)
        label_left_a = MathTex("a").next_to(brace_left_full, LEFT)

        self.play(DrawBorderThenFill(large_square))
        self.play(
            GrowFromCenter(brace_bottom), Write(label_bottom_a),
            GrowFromCenter(brace_left_full), Write(label_left_a)
        )
        self.wait(1)

        # ========== INITIAL FORMULA DISPLAY ==========
        equation_components = MathTex(r"(a-b)^2", r"=", r"a^2")
        equation_components.shift(UP, RIGHT)
        self.play(Write(equation_components[0]))
        self.wait(1)

        # ========== DIVISION LINES CONSTRUCTION ==========
        # Vertical division line
        top_right_corner = large_square.get_corner(UR)
        bottom_right_corner = large_square.get_corner(DR)
        vertical_split_top = top_right_corner + LEFT * LENGTH_B
        vertical_split_bottom = bottom_right_corner + LEFT * LENGTH_B
        dashed_line_vertical = DashedLine(vertical_split_top, vertical_split_bottom, color=GRAY)

        # Horizontal division line
        top_left_corner = large_square.get_corner(UL)
        horizontal_split_left = top_left_corner + DOWN * LENGTH_B
        horizontal_split_right = top_right_corner + DOWN * LENGTH_B
        dashed_line_horizontal = DashedLine(horizontal_split_left, horizontal_split_right, color=GRAY)

        self.play(Create(dashed_line_vertical), Create(dashed_line_horizontal))

        # ========== SPLIT LEFT BRACE ==========
        # Split the left brace into two parts: b and (a-b)
        split_point_left = large_square.get_left() + UP * (LENGTH_A / 2 - LENGTH_B)

        # Upper brace for b
        brace_upper_b = BraceBetweenPoints(large_square.get_corner(UL), split_point_left, direction=LEFT)
        label_upper_b = MathTex("b").next_to(brace_upper_b, LEFT)

        # Lower brace for (a-b)
        brace_lower_a_minus_b = BraceBetweenPoints(split_point_left, large_square.get_corner(DL), direction=LEFT)
        label_lower_a_minus_b = MathTex("a-b").next_to(brace_lower_a_minus_b, LEFT)

        self.play(
            ReplacementTransform(brace_left_full, VGroup(brace_upper_b, brace_lower_a_minus_b)),
            ReplacementTransform(label_left_a, VGroup(label_upper_b, label_lower_a_minus_b))
        )

        # ========== TARGET SQUARE IDENTIFICATION ==========
        # The green square representing (a-b)²
        target_square = Square(side_length=LENGTH_A_MINUS_B, color=COLOR_TARGET_SQUARE, fill_opacity=0.6)
        target_square.align_to(large_square, DL)
        target_label = MathTex("(a-b)^2").move_to(target_square.get_center()).scale(0.7)

        self.play(FadeIn(target_square), Write(target_label))
        self.play(Write(equation_components[1]), Write(equation_components[2]))
        self.wait(1)

        # ========== SUBTRACTION OF RECTANGLES ==========
        # Top rectangle to subtract (area = ab)
        rectangle_top = Rectangle(
            width=LENGTH_A,
            height=LENGTH_B,
            color=COLOR_SUBTRACT_RECTANGLE,
            fill_opacity=0.4
        )
        rectangle_top.align_to(large_square, UP)
        rectangle_top.match_x(large_square)

        # Right rectangle to subtract (area = ab)
        rectangle_right = Rectangle(
            width=LENGTH_B,
            height=LENGTH_A,
            color=COLOR_SUBTRACT_RECTANGLE,
            fill_opacity=0.4
        )
        rectangle_right.align_to(large_square, RIGHT)
        rectangle_right.match_y(large_square)

        # Animate first subtraction
        self.play(FadeIn(rectangle_top))
        term_minus_ab1 = MathTex(r"- ab").next_to(equation_components[2], DOWN, aligned_edge=LEFT)
        self.play(Write(term_minus_ab1))

        # Animate second subtraction
        self.play(FadeIn(rectangle_right))
        term_minus_ab2 = MathTex(r"- ab").next_to(term_minus_ab1, DOWN, aligned_edge=LEFT)
        self.play(Write(term_minus_ab2))
        self.wait(1)

        # ========== OVERLAP CORRECTION ==========
        # The yellow square that was subtracted twice
        overlap_square = Square(side_length=LENGTH_B, color=COLOR_CORRECTION_SQUARE, fill_opacity=0.8)
        overlap_square.align_to(large_square, UR)
        overlap_label = MathTex("b^2").move_to(overlap_square.get_center()).set_color(BLACK).scale(0.7)

        self.play(FadeIn(overlap_square), Write(overlap_label))
        self.play(Indicate(overlap_square, scale_factor=1.2))

        # Explanation of the correction needed
        correction_explanation = Tex(
            "We subtracted $b^2$ twice!",
            color=YELLOW
        ).scale(0.8).next_to(large_square, DOWN, buff=1.0)
        self.play(Write(correction_explanation))
        self.wait(1)

        # Add the correction term
        term_plus_b2 = MathTex(r"+ b^2").next_to(term_minus_ab2, DOWN, aligned_edge=LEFT)
        self.play(Write(term_plus_b2))
        self.play(FadeOut(correction_explanation))

        # ========== FINAL FORMULA DERIVATION ==========
        final_formula = MathTex(r"= a^2 - 2ab + b^2").next_to(equation_components[0], RIGHT)
        terms_to_transform = VGroup(
            equation_components[1], equation_components[2],
            term_minus_ab1, term_minus_ab2, term_plus_b2
        )
        self.play(ReplacementTransform(terms_to_transform, final_formula))

        # Highlight the final formula
        final_equation_group = VGroup(equation_components[0], final_formula)
        self.play(FadeOut(final_equation_group))
        final_equation_group.shift(DOWN * 1)
        self.play(FadeIn(final_equation_group))
        highlight_box = SurroundingRectangle(final_equation_group, color=YELLOW)
        self.play(Create(highlight_box))
        self.wait(3)


class SumDifferenceProduct(Scene):
    """
    Geometric demonstration of the product of sum and difference: (a+b)(a-b) = a² - b²
    Shows area equivalence through geometric transformation.
    """

    def construct(self):
        # ========== PARAMETERS AND COLOR SCHEME ==========
        RECTANGLE_STROKE_COLOR = WHITE
        COLOR_B_RECTANGLE = RED
        COLOR_B_SQUARE = BLUE

        # ========== TITLE AND INTRODUCTION ==========
        title = MathTex(r"\text{Difference of Squares: } (a+b)(a-b)").to_edge(UP)
        self.play(Write(title))

        # ========== INITIAL GEOMETRIC CONSTRUCTION ==========
        # Large rectangle representing a(a-b) = a² - ab
        rectangle_top = Rectangle(
            width=3,
            height=2,
            color=RECTANGLE_STROKE_COLOR,
            fill_color=COLOR_B_RECTANGLE,
            fill_opacity=0.7
        )
        rectangle_top.to_edge(LEFT * 2).shift(UP * 0.5)

        # Brace for dimension a on top
        brace_top_a = Brace(rectangle_top, UP)
        text_top_a = brace_top_a.get_text("a")
        label_top_a = VGroup(brace_top_a, text_top_a)

        # Small square representing b² (to be subtracted)
        square_b = Square(
            side_length=1,
            color=RECTANGLE_STROKE_COLOR,
            fill_color=COLOR_B_SQUARE,
            fill_opacity=0.7
        )
        square_b.next_to(rectangle_top, DOWN, buff=0).align_to(rectangle_top, LEFT)

        # Brace for dimension b below the square
        brace_square_b = Brace(square_b, DOWN)
        text_square_b = brace_square_b.get_text("b")
        label_square_b = VGroup(brace_square_b, text_square_b)

        # Bottom rectangle representing remaining area
        rectangle_bottom = Rectangle(
            width=2,
            height=1,
            color=RECTANGLE_STROKE_COLOR,
            fill_color=COLOR_B_RECTANGLE,
            fill_opacity=0.7
        )
        rectangle_bottom.next_to(square_b, RIGHT, buff=0)

        # Brace for dimension (a-b) on the right
        brace_right_a_minus_b = Brace(rectangle_top, RIGHT, color=WHITE)
        label_right_a_minus_b = brace_right_a_minus_b.get_text("a-b").set_color(WHITE)

        # ========== SCENE ORGANIZATION ==========
        # Group all initial elements
        initial_figure = VGroup(
            rectangle_top, square_b, rectangle_bottom,
            label_top_a, label_square_b, brace_right_a_minus_b, label_right_a_minus_b
        )
        initial_figure.move_to(ORIGIN).shift(LEFT * 2.5)

        # ========== TRANSFORMED CONFIGURATION ==========
        # Side rectangle for the transformed figure
        rectangle_side = Rectangle(
            width=1,
            height=2,
            color=RECTANGLE_STROKE_COLOR,
            fill_color=COLOR_B_RECTANGLE,
            fill_opacity=0.7
        )
        rectangle_side.next_to(rectangle_top, LEFT, buff=0)

        # Combined brace for (a+b) in transformed figure
        top_combined_group = VGroup(rectangle_side, rectangle_top)
        brace_combined_top = Brace(top_combined_group, UP)
        text_combined_top = brace_combined_top.get_text("a+b")
        new_label_combined_top = VGroup(brace_combined_top, text_combined_top)

        # ========== ALGEBRAIC FORMULAS ==========
        formula_area1 = MathTex(r"\text{Area}_1 = a^2 - b^2")
        formula_area2 = MathTex(r"\text{Area}_2 = (a+b)(a-b)")
        formula_area_equivalence = MathTex(r"\text{Area}_2 = \text{Area}_1")
        formula_final_identity = MathTex(r"(a+b)(a-b) = a^2 - b^2")

        formula_group = VGroup(formula_area1, formula_area2, formula_area_equivalence, formula_final_identity)
        formula_group.shift(RIGHT * 2.5, UP)

        # ========== ANIMATION SEQUENCE ==========
        # Display initial construction with dimension labels
        self.play(Create(rectangle_top), Create(label_top_a))
        self.play(Create(square_b), Create(label_square_b))
        self.play(Create(rectangle_bottom))
        self.play(Create(brace_right_a_minus_b), Write(label_right_a_minus_b))

        self.play(Create(formula_area1))
        self.wait(1)

        # Transform to new configuration
        self.play(Transform(rectangle_bottom, rectangle_side))
        self.play(FadeOut(square_b), FadeOut(label_square_b))
        self.play(Transform(label_top_a, new_label_combined_top))

        # Display second area formula
        formula_area2.next_to(formula_area1, DOWN)
        self.play(Create(formula_area2))
        self.wait(2)

        # Clean up geometric elements
        final_figure = VGroup(
            rectangle_top, label_top_a, rectangle_bottom,
            brace_right_a_minus_b, label_right_a_minus_b
        )
        self.play(FadeOut(final_figure))

        # Final algebraic derivation
        self.play(formula_area1.animate.move_to(ORIGIN).move_to(UP * 2))
        self.play(formula_area2.animate.next_to(formula_area1, DOWN))

        formula_area_equivalence.next_to(formula_area2, DOWN)
        self.play(Create(formula_area_equivalence))
        self.wait(2)

        formula_final_identity.next_to(formula_area_equivalence, DOWN * 1.5)
        self.play(Create(formula_final_identity))
        self.wait(3)
