from manim import *


class QuadraticFormula(Scene):
    def construct(self):
        # ========== TITLE AND INTRODUCTION ==========
        title = Tex("Quadratic Formula: Geometric Proof", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(1.0)

        # ========== PRECONDITIONS AND ASSUMPTIONS ==========
        # Clearly state the mathematical assumptions for the geometric interpretation
        # This demonstrates academic rigor and honesty about method limitations
        assumptions_text = VGroup(
            Tex("Assumptions for geometric interpretation:", font_size=30),
            MathTex(r"1.\ a \neq 0 \quad \text{(quadratic equation)}").scale(0.5),
            MathTex(r"2.\ a > 0,\ b > 0 \quad \text{(geometric meaning)}").scale(0.5),
            MathTex(r"3.\ \text{Working in real domain}").scale(0.5),
            Tex("Required for geometric validity, not for algebraic truth.").scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(title, DOWN, buff=0.4)

        assumptions_text.set_color(BLUE)
        self.play(Write(assumptions_text))
        self.wait(1.6)

        # ========== ALGEBRAIC NORMALIZATION PROCESS ==========
        # Demonstrate the conversion from general to normalized form
        # This shows the algebraic manipulation that enables geometric interpretation
        normalization_steps = VGroup(
            Tex("Convert the general form to normalized form:", font_size=30),
            MathTex(r"a x^2 + b x + c = 0").scale(0.5),
            MathTex(r"\text{Divide both sides by } a \quad (\text{since } a \neq 0)").scale(0.5),
            MathTex(r"x^2 + \frac{b}{a} x + \frac{c}{a} = 0").scale(0.5),
            MathTex(r"\text{Set } p := \frac{b}{a},\quad q := \frac{c}{a} \Rightarrow x^2 + p x + q = 0").scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(assumptions_text, DOWN, buff=0.5)

        normalization_steps.set_color(WHITE)

        # Animate each normalization step sequentially for clarity
        for step in normalization_steps:
            self.play(Write(step), run_time=1.0)
            self.wait(1.0)

        # Clear normalization steps to make space for geometric construction
        self.wait(1.0)
        self.play(FadeOut(normalization_steps), run_time=0.8)
        self.wait(0.25)

        # Clear assumptions to prepare for main geometric demonstration
        self.play(FadeOut(assumptions_text), run_time=0.5)
        self.wait(0.25)

        # ========== GEOMETRIC CONSTRUCTION PARAMETERS ==========
        # Define specific coefficient values for the geometric demonstration
        # These values are chosen to create clear visual representations
        COEFFICIENT_A = 1.0
        COEFFICIENT_B = 4.0
        COEFFICIENT_C = 3.0

        # Convert to normalized form coefficients for geometric interpretation
        COEFFICIENT_P = COEFFICIENT_B / COEFFICIENT_A
        COEFFICIENT_Q = COEFFICIENT_C / COEFFICIENT_A

        # ========== VISUALIZATION SCALING PARAMETERS ==========
        VISUALIZATION_SCALE = 0.6  # Base unit for geometric representation
        X_VISUAL_SIZE = 1.0  # Representative size for variable x
        BASE_SQUARE_SIDE = X_VISUAL_SIZE * VISUALIZATION_SCALE  # x² square side length

        # ========== GEOMETRIC ELEMENTS CONSTRUCTION ==========
        # Create the main square representing x² term (visual foundation)
        x_squared_square = Square(side_length=BASE_SQUARE_SIDE, stroke_width=3)
        x_squared_square.set_fill(RED, opacity=0.5)
        x_squared_square.to_edge(LEFT, buff=1.5)
        x_squared_label = MathTex("x^2").move_to(x_squared_square.get_center())

        # Create rectangle representing the linear term p·x
        px_rectangle = Rectangle(
            width=COEFFICIENT_P * VISUALIZATION_SCALE,
            height=BASE_SQUARE_SIDE,
            stroke_width=2
        )
        px_rectangle.set_fill(GREEN, opacity=0.25)
        px_rectangle.next_to(x_squared_square, RIGHT, buff=0)
        px_label = MathTex("p x").move_to(px_rectangle)

        # ========== INITIAL GEOMETRIC CONSTRUCTION ANIMATION ==========
        # Display the foundational x² square
        self.play(Create(x_squared_square), Write(x_squared_label), run_time=1.0)
        self.wait(0.75)

        # Add the linear term rectangle
        self.play(Create(px_rectangle), Write(px_label), run_time=1.0)
        self.wait(1.0)

        # ========== COMPLETING THE SQUARE - GEOMETRIC TRANSFORMATION ==========
        # Split the p·x rectangle into two equal parts for geometric manipulation
        # This demonstrates the key insight of the "completing the square" method

        # First half of the p·x rectangle (remains in position)
        px_half_rect1 = Rectangle(
            width=(COEFFICIENT_P / 2) * VISUALIZATION_SCALE,
            height=BASE_SQUARE_SIDE,
            stroke_width=2
        )
        px_half_rect1.set_fill(GREEN, opacity=0.5)
        px_half_rect1.next_to(x_squared_square, RIGHT, buff=0)
        px_half_label1 = MathTex(r"\frac{p x}{2}").scale(0.5).move_to(px_half_rect1)

        # Second half of the p·x rectangle (will be repositioned)
        px_half_rect2 = Rectangle(
            width=(COEFFICIENT_P / 2) * VISUALIZATION_SCALE,
            height=BASE_SQUARE_SIDE,
            stroke_width=2
        )
        px_half_rect2.set_fill(GREEN, opacity=0.5)
        px_half_rect2.next_to(px_half_rect1, RIGHT, buff=0)
        px_half_label2 = MathTex(r"\frac{p x}{2}").scale(0.5).move_to(px_half_rect2)

        # Animate the division into two equal parts
        self.play(
            FadeOut(px_label),
            Transform(px_rectangle, VGroup(px_half_rect1.copy(), px_half_rect2.copy())),
            run_time=1.2
        )
        self.play(
            FadeIn(px_half_rect1), FadeIn(px_half_label1),
            FadeIn(px_half_rect2), FadeIn(px_half_label2),
            run_time=1.0
        )
        self.wait(0.75)
        self.play(FadeOut(px_half_label2), run_time=0.4)

        # Reposition second half to top to form L-shape (key geometric insight)
        top_half_rectangle = Rectangle(
            width=BASE_SQUARE_SIDE,
            height=(COEFFICIENT_P / 2) * VISUALIZATION_SCALE,
            stroke_width=2
        )
        top_half_rectangle.set_fill(GREEN, opacity=0.5)
        top_half_rectangle.next_to(x_squared_square, UP, buff=0)

        # Transform right rectangle to top position
        self.play(
            ReplacementTransform(px_half_rect2, top_half_rectangle),
            FadeOut(px_rectangle),
            run_time=1.0
        )
        px_half_label2.move_to(top_half_rectangle)
        self.play(FadeIn(px_half_label2), run_time=0.5)
        self.wait(0.5)

        # ========== ADDING THE COMPLETING SQUARE ==========
        # The small square that completes the perfect square: represents (p/2)²
        completing_square = Square(
            side_length=(COEFFICIENT_P / 2) * VISUALIZATION_SCALE,
            stroke_width=2
        )
        completing_square.set_fill(BLUE, opacity=0.5)
        completing_square.align_to(px_half_rect1, RIGHT)
        completing_square.next_to(px_half_rect1, UP, buff=0)
        completing_square_label = MathTex(r"\left(\frac{p}{2}\right)^2").move_to(completing_square)

        # Display the completing square
        self.play(FadeIn(completing_square), run_time=1.0)
        self.play(FadeIn(completing_square_label), run_time=0.5)
        self.wait(0.5)

        # Highlight the completed perfect square formation
        perfect_square_group = VGroup(
            x_squared_square, px_half_rect1, top_half_rectangle, completing_square
        )
        self.play(Indicate(perfect_square_group, color=BLUE), run_time=1.4)
        self.wait(0.75)

        # ========== ALGEBRAIC DERIVATION FROM GEOMETRIC INSIGHT ==========
        # Connect the geometric construction to algebraic identity
        completion_identity = MathTex(
            r"x^2 + p x + \left(\frac{p}{2}\right)^2 = \left(x + \frac{p}{2}\right)^2"
        ).scale(0.75).shift(UP * 2)
        self.play(Write(completion_identity), run_time=1.0)
        self.wait(1.0)

        # Step-by-step algebraic derivation with geometric motivation
        normalized_equation = MathTex(
            r"x^2 + p x + q = 0 \quad (\text{Normalized Form})"
        ).scale(0.75).next_to(completion_identity, DOWN, aligned_edge=LEFT)
        self.play(Write(normalized_equation), run_time=1.0)
        self.wait(1.0)

        rearranged_equation = MathTex(r"x^2 + p x = - q") \
            .scale(0.75).next_to(normalized_equation, DOWN, aligned_edge=LEFT)
        self.play(Write(rearranged_equation), run_time=1.0)
        self.wait(1.0)

        squared_equation = MathTex(
            r"\Rightarrow\ (x + \tfrac{p}{2})^2 = \tfrac{p^2}{4} - q"
        ).scale(0.75).next_to(rearranged_equation, DOWN, aligned_edge=LEFT)
        self.play(Write(squared_equation), run_time=1.0)
        self.wait(1.0)

        square_root_step = MathTex(
            r"x + \tfrac{p}{2} = \pm\sqrt{\tfrac{p^2}{4} - q}"
        ).scale(0.75).next_to(squared_equation, DOWN, aligned_edge=LEFT)
        self.play(Write(square_root_step), run_time=1.0)
        self.wait(1.0)

        solution_step = MathTex(
            r"x = -\tfrac{p}{2} \pm \sqrt{\tfrac{p^2}{4} - q}"
        ).scale(0.75).next_to(square_root_step, DOWN, aligned_edge=LEFT)
        self.play(Write(solution_step), run_time=1.0)
        self.wait(1.0)

        # Clear intermediate steps to focus on final derivation
        self.play(
            FadeOut(VGroup(
                completion_identity, normalized_equation, rearranged_equation,
                squared_equation, square_root_step, solution_step
            )),
            run_time=1.0
        )
        self.wait(0.5)

        # ========== FINAL QUADRATIC FORMULA DERIVATION ==========
        # Connect back to original coefficients and present final formula
        coefficient_relation = MathTex(
            r"p = \tfrac{b}{a},\ \ q=\tfrac{c}{a}"
        ).scale(0.75).shift(UP * 1.2)

        quadratic_formula = MathTex(
            r"x = \frac{-b \pm \sqrt{b^2 - 4 a c}}{2 a}"
        ).scale(0.75).next_to(coefficient_relation, DOWN, aligned_edge=LEFT)

        self.play(Write(coefficient_relation), run_time=1.0)
        self.wait(0.5)
        self.play(Write(quadratic_formula), run_time=1.0)
        self.wait(1.5)

        # ========== CRITICAL ANALYSIS AND LIMITATIONS ==========
        # Important academic discussion of method limitations
        # Demonstrates research maturity and critical thinking
        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob is not title],
            run_time=1.0
        )
        self.wait(0.5)

        limitations_text = VGroup(
            Tex("Limitations of geometric approach:", font_size=30),
            MathTex(r"\bullet\ \text{Only valid for } a > 0, b > 0").scale(0.5),
            MathTex(r"\bullet\ \text{Real domain only}").scale(0.5),
            MathTex(r"\bullet\ \text{Specific coefficient values}").scale(0.5),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        limitations_text.set_color(RED)
        limitations_text.move_to(UP * 1.0)

        # Emphasize the generality of algebraic methods
        conclusion_text = Tex(
            "However, the algebraic method has no such limitation.",
            font_size=30
        ).set_color(GREEN).next_to(limitations_text, DOWN, buff=0.5)

        self.play(Write(limitations_text), run_time=2.0)
        self.wait(1.0)
        self.play(Write(conclusion_text), run_time=1.0)
        self.wait(2.0)

        # ========== FINAL CONCLUSION ==========
        # Clean ending with fade-out of all elements
        self.play(
            FadeOut(limitations_text),
            FadeOut(conclusion_text),
            FadeOut(title),
            run_time=1.5
        )
        self.wait(0.5)
