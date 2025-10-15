from manim import *
import math


class PythagoreanTheorem(Scene):
    def construct(self):
        # ========== INITIAL PARAMETERS ==========
        # Initial triangle dimensions for the first demonstration
        LEG_A = 2.0  # Length of first leg
        LEG_B = 1.2  # Length of second leg
        OUTER_SQUARE_SIDE = LEG_A + LEG_B  # Side length of large containing square
        HYPOTENUSE = math.sqrt(LEG_A ** 2 + LEG_B ** 2)  # Calculated hypotenuse length
        ROTATION_ANGLE = math.atan2(LEG_B, LEG_A)  # Angle to align central square

        # ==========================================================
        # GEOMETRIC–ALGEBRAIC PREFACE (logical context explanation)
        # ==========================================================
        # Introduce the geometric and algebraic interpretation of the theorem

        preface_title = Tex(
            "Mathematical Context of the Pythagorean Theorem", font_size=40
        ).to_edge(UP)

        preface_text_1 = Tex(
            "The Pythagorean theorem is fundamentally a geometric statement,",
            " describing the relationship between the side lengths of a right triangle.",
            font_size=30
        ).next_to(preface_title, DOWN, buff=0.5)

        preface_text_2 = Tex(
            "Therefore, in its original context, the side lengths ",
            "$a$, $b$, and $c$",
            " are assumed to be real and strictly positive —",
            " giving the theorem geometric meaning.",
            font_size=32
        ).next_to(preface_text_1, DOWN, buff=0.35)

        preface_text_3 = Tex(
            "When generalized algebraically as ",
            "$a^2 + b^2 = c^2$,",
            " the variables $a$ and $b$ may take any real value, including negatives,",
            " allowing for broader mathematical applications.",
            font_size=32
        ).next_to(preface_text_2, DOWN, buff=0.35)

        preface_text_4 = Tex(
            "However, since squaring removes the effect of sign,",
            " the validity of the formula for all real numbers",
            " is already implied by its geometric proof under $a, b > 0$.",
            font_size=32
        ).next_to(preface_text_3, DOWN, buff=0.35)

        preface_text_5 = Tex(
            "In other words, a purely geometric proof — based only on positive lengths —",
            " is sufficient to establish the universal truth of $a^2 + b^2 = c^2$.",
            font_size=32
        ).next_to(preface_text_4, DOWN, buff=0.35)

        preface_text_6 = Tex(
            "In this demonstration, we focus on this geometric interpretation,",
            " assuming $a, b > 0$ and $c$ as the hypotenuse.",
            font_size=32
        ).next_to(preface_text_5, DOWN, buff=0.35)

        # Sequential appearance with fade and write transitions
        self.play(Write(preface_title))
        self.wait(0.5)
        self.play(FadeIn(preface_text_1, shift=UP * 0.2))
        self.play(FadeIn(preface_text_2, shift=UP * 0.2))
        self.wait(1.75)
        self.play(FadeIn(preface_text_3, shift=UP * 0.2))
        self.play(FadeIn(preface_text_4, shift=UP * 0.2))
        self.wait(1.75)
        self.play(FadeIn(preface_text_5, shift=UP * 0.2))
        self.play(FadeIn(preface_text_6, shift=UP * 0.2))
        self.wait(2.5)

        # Smooth fade-out before geometric visualization
        self.play(
            *[FadeOut(mob) for mob in [
                preface_title, preface_text_1, preface_text_2,
                preface_text_3, preface_text_4, preface_text_5, preface_text_6
            ]],
            run_time=1.5
        )

        # ========== GEOMETRIC CONSTRUCTION ==========
        # Create the outer square that frames the entire proof
        outer_square = Square(side_length=OUTER_SQUARE_SIDE)
        outer_square.set_stroke(width=3).set_fill(opacity=0)
        outer_square.move_to(ORIGIN)  # Center for visual symmetry

        # Calculate precise vertex coordinates for triangle placement
        HALF_SIDE = OUTER_SQUARE_SIDE / 2
        VERTEX_BOTTOM_LEFT = np.array([-HALF_SIDE, -HALF_SIDE, 0])
        VERTEX_BOTTOM_RIGHT = np.array([HALF_SIDE, -HALF_SIDE, 0])
        VERTEX_TOP_RIGHT = np.array([HALF_SIDE, HALF_SIDE, 0])
        VERTEX_TOP_LEFT = np.array([-HALF_SIDE, HALF_SIDE, 0])

        # Construct four congruent right triangles at each corner
        # Each triangle has legs of lengths LEG_A and LEG_B in different orientations

        # Bottom-left triangle (blue)
        triangle_bottom_left = Polygon(
            VERTEX_BOTTOM_LEFT,
            VERTEX_BOTTOM_LEFT + np.array([LEG_B, 0, 0]),  # Horizontal leg
            VERTEX_BOTTOM_LEFT + np.array([0, LEG_A, 0]),  # Vertical leg
            stroke_width=2,
            fill_opacity=0.5,
        ).set_fill(BLUE)

        # Bottom-right triangle (purple)
        triangle_bottom_right = Polygon(
            VERTEX_BOTTOM_RIGHT,
            VERTEX_BOTTOM_RIGHT + np.array([-LEG_A, 0, 0]),  # Horizontal leg left
            VERTEX_BOTTOM_RIGHT + np.array([0, LEG_B, 0]),  # Vertical leg up
            stroke_width=2,
            fill_opacity=0.5,
        ).set_fill(PURPLE)

        # Top-right triangle (green)
        triangle_top_right = Polygon(
            VERTEX_TOP_RIGHT,
            VERTEX_TOP_RIGHT + np.array([-LEG_B, 0, 0]),  # Horizontal leg left
            VERTEX_TOP_RIGHT + np.array([0, -LEG_A, 0]),  # Vertical leg down
            stroke_width=2,
            fill_opacity=0.5,
        ).set_fill(GREEN)

        # Top-left triangle (light pink)
        triangle_top_left = Polygon(
            VERTEX_TOP_LEFT,
            VERTEX_TOP_LEFT + np.array([LEG_A, 0, 0]),  # Horizontal leg right
            VERTEX_TOP_LEFT + np.array([0, -LEG_B, 0]),  # Vertical leg down
            stroke_width=2,
            fill_opacity=0.5,
        ).set_fill(LIGHT_PINK)

        # Central square formed by the hypotenuses
        central_square = Square(side_length=HYPOTENUSE)
        central_square.rotate(ROTATION_ANGLE).move_to(ORIGIN)
        central_square.set_stroke(width=3).set_fill(TEAL, opacity=0.6)

        # ========== LABELS AND ANNOTATIONS ==========
        # Title for the proof demonstration
        title = Tex("Geometric Proof: Pythagorean Theorem", font_size=40).to_edge(UP)

        # Measurement braces for the bottom-left triangle
        brace_vertical = Brace(
            Line(VERTEX_BOTTOM_LEFT, VERTEX_BOTTOM_LEFT + np.array([0, LEG_A, 0])),
            LEFT, buff=0.15
        )
        brace_vertical_label = brace_vertical.get_tex("a")

        brace_horizontal = Brace(
            Line(VERTEX_BOTTOM_LEFT, VERTEX_BOTTOM_LEFT + np.array([LEG_B, 0, 0])),
            DOWN, buff=0.15
        )
        brace_horizontal_label = brace_horizontal.get_tex("b")

        # Hypotenuse brace with careful positioning
        hypotenuse_segment = Line(
            VERTEX_BOTTOM_LEFT + np.array([0, LEG_A, 0]),
            VERTEX_BOTTOM_LEFT + np.array([LEG_B, 0, 0])
        )
        brace_hypotenuse = Brace(
            hypotenuse_segment,
            direction=hypotenuse_segment.copy().rotate(PI / 2).get_unit_vector(),
            buff=0.15
        )
        brace_hypotenuse_label = brace_hypotenuse.get_tex("c")
        # Adjust label position for better visibility
        brace_hypotenuse_label.move_to(brace_hypotenuse.get_center() + UP * 0.3 + RIGHT * 0.375)

        # ========== PROOF DEMONSTRATION SEQUENCE ==========
        # Begin with title presentation
        self.play(Create(title))
        self.wait(0.6)

        # Show the outer square and its area formula
        self.play(Create(outer_square))

        # Reveal the four congruent triangles
        self.play(
            FadeIn(triangle_bottom_left),
            FadeIn(triangle_bottom_right),
            FadeIn(triangle_top_right),
            FadeIn(triangle_top_left),
            run_time=1.2
        )

        # Display side length measurements
        self.play(
            FadeIn(brace_vertical),
            FadeIn(brace_vertical_label),
            FadeIn(brace_horizontal),
            FadeIn(brace_horizontal_label)
        )
        self.wait(1)

        # Introduce the central square and hypotenuse
        self.play(Create(central_square))
        self.play(Create(brace_hypotenuse), Write(brace_hypotenuse_label))
        self.wait(0.8)

        # Show the outer square's explanation and its area formula
        area_outer_explanation = MathTex(
            r"\text{We form a square with side length }",
            "a + b",
            r"\text{ in the following arrangement.}",
            font_size=36
        )
        area_outer_explanation.next_to(outer_square, UP, buff=0.25)
        self.play(Write(area_outer_explanation))
        self.wait(1.0)
        self.play(FadeOut(area_outer_explanation), run_time=1.0)

        area_outer_formula = MathTex(r"\text{Area} = (a+b)^2", font_size=36)
        area_outer_formula.next_to(outer_square, UP, buff=0.25)
        self.play(Write(area_outer_formula))

        self.wait(0.5)

        # ========== ALGEBRAIC DERIVATION ==========
        # Step 1: Area equivalence equation
        area_equation = MathTex(
            r"(a+b)^2 = 4\cdot\left(\tfrac{1}{2}ab\right) + c^2",
            font_size=36,
        ).to_edge(DOWN)
        self.play(Write(area_equation))
        self.wait(1.5)

        # Step 2: Simplify the triangle area term
        equation_step1 = MathTex(r"(a+b)^2 = 2ab + c^2", font_size=36).to_edge(DOWN)
        self.play(Transform(area_equation, equation_step1))
        self.wait(1.5)

        # Step 3: Expand the binomial
        equation_step2 = MathTex(r"a^2 + 2ab + b^2 = 2ab + c^2", font_size=36).to_edge(DOWN)
        self.play(Transform(area_equation, equation_step2))
        self.wait(1.5)

        # Step 4: Cancel common terms to reach final theorem
        equation_step3 = MathTex(r"a^2 + b^2 = c^2", font_size=36).to_edge(DOWN)
        self.play(Transform(area_equation, equation_step3), run_time=1.2)
        self.wait(1.75)

        # Display concluding statement
        conclusion_text = Tex(
            "After derivation, we get:\\\\"
            r"$c^2 = a^2 + b^2$",
            font_size=30,
        ).move_to(ORIGIN).shift(RIGHT * 4.5)
        self.play(FadeIn(conclusion_text))
        self.wait(2.0)

        # ========== GENERALITY DEMONSTRATION ==========
        # Show that the theorem holds for different triangle dimensions
        dimension_change_announcement = Tex(
            "Now we change the dimensions of $a$ and $b$",
            font_size=30
        ).to_edge(UP, buff=1.0)
        self.play(Write(dimension_change_announcement))
        self.wait(1.0)

        # New triangle dimensions for generality demonstration
        NEW_LEG_A = 1.5
        NEW_LEG_B = 2.5

        # Recalculate geometric properties with new dimensions
        NEW_OUTER_SQUARE_SIDE = NEW_LEG_A + NEW_LEG_B
        NEW_HYPOTENUSE = math.sqrt(NEW_LEG_A ** 2 + NEW_LEG_B ** 2)
        NEW_ROTATION_ANGLE = math.atan2(NEW_LEG_B, NEW_LEG_A)

        # Update vertex coordinates for new configuration
        NEW_HALF_SIDE = NEW_OUTER_SQUARE_SIDE / 2
        NEW_BOTTOM_LEFT = np.array([-NEW_HALF_SIDE, -NEW_HALF_SIDE, 0])
        NEW_BOTTOM_RIGHT = np.array([NEW_HALF_SIDE, -NEW_HALF_SIDE, 0])
        NEW_TOP_RIGHT = np.array([NEW_HALF_SIDE, NEW_HALF_SIDE, 0])
        NEW_TOP_LEFT = np.array([-NEW_HALF_SIDE, NEW_HALF_SIDE, 0])

        # Update all triangle positions for new dimensions
        triangle_bottom_left.generate_target()
        triangle_bottom_left.target.set_points_as_corners([
            NEW_BOTTOM_LEFT,
            NEW_BOTTOM_LEFT + np.array([NEW_LEG_B, 0, 0]),
            NEW_BOTTOM_LEFT + np.array([0, NEW_LEG_A, 0])
        ])

        triangle_bottom_right.generate_target()
        triangle_bottom_right.target.set_points_as_corners([
            NEW_BOTTOM_RIGHT,
            NEW_BOTTOM_RIGHT + np.array([-NEW_LEG_A, 0, 0]),
            NEW_BOTTOM_RIGHT + np.array([0, NEW_LEG_B, 0])
        ])

        triangle_top_right.generate_target()
        triangle_top_right.target.set_points_as_corners([
            NEW_TOP_RIGHT,
            NEW_TOP_RIGHT + np.array([-NEW_LEG_B, 0, 0]),
            NEW_TOP_RIGHT + np.array([0, -NEW_LEG_A, 0])
        ])

        triangle_top_left.generate_target()
        triangle_top_left.target.set_points_as_corners([
            NEW_TOP_LEFT,
            NEW_TOP_LEFT + np.array([NEW_LEG_A, 0, 0]),
            NEW_TOP_LEFT + np.array([0, -NEW_LEG_B, 0])
        ])

        # Remove old measurement annotations
        self.play(
            FadeOut(brace_vertical), FadeOut(brace_vertical_label),
            FadeOut(brace_horizontal), FadeOut(brace_horizontal_label),
            FadeOut(brace_hypotenuse), FadeOut(brace_hypotenuse_label)
        )
        self.wait(0.3)

        # Create new measurement braces for updated configuration
        new_brace_vertical = Brace(
            Line(NEW_BOTTOM_LEFT, NEW_BOTTOM_LEFT + np.array([0, NEW_LEG_A, 0])),
            LEFT, buff=0.15
        )
        new_brace_vertical_label = new_brace_vertical.get_tex("a")

        new_brace_horizontal = Brace(
            Line(NEW_BOTTOM_LEFT, NEW_BOTTOM_LEFT + np.array([NEW_LEG_B, 0, 0])),
            DOWN, buff=0.15
        )
        new_brace_horizontal_label = new_brace_horizontal.get_tex("b")

        new_hypotenuse_segment = Line(
            NEW_BOTTOM_LEFT + np.array([0, NEW_LEG_A, 0]),
            NEW_BOTTOM_LEFT + np.array([NEW_LEG_B, 0, 0])
        )
        new_brace_hypotenuse = Brace(
            new_hypotenuse_segment,
            direction=new_hypotenuse_segment.copy().rotate(PI / 2).get_unit_vector(),
            buff=0.15
        )
        new_brace_hypotenuse_label = new_brace_hypotenuse.get_tex("c")
        new_brace_hypotenuse_label.move_to(new_brace_hypotenuse.get_center() + UP * 0.45 + RIGHT * 0.25)

        # Update central and outer squares
        central_square.generate_target()
        central_square.target.become(
            Square(side_length=NEW_HYPOTENUSE)
            .rotate(NEW_ROTATION_ANGLE)
            .move_to(ORIGIN)
            .set_fill(TEAL, opacity=0.6)
        )

        outer_square.generate_target()
        outer_square.target.become(
            Square(side_length=NEW_OUTER_SQUARE_SIDE)
            .set_stroke(width=3)
            .move_to(ORIGIN)
        )

        # Adjust area formula position
        self.play(area_outer_formula.animate.shift(UP * 0.35))

        # Animate transformation to new configuration
        self.play(
            MoveToTarget(triangle_bottom_left),
            MoveToTarget(triangle_bottom_right),
            MoveToTarget(triangle_top_right),
            MoveToTarget(triangle_top_left),
            MoveToTarget(central_square),
            MoveToTarget(outer_square),
            run_time=3.0
        )

        # Emphasize the invariant nature of the theorem
        invariance_statement = Tex(
            "Even though the sides change, \\\\ the relationship $a^2 + b^2 = c^2$ \\\\ remains true!",
            font_size=30
        ).shift(LEFT * 4.5)

        # Display new measurement annotations
        self.play(
            FadeIn(new_brace_vertical),
            FadeIn(new_brace_vertical_label),
            FadeIn(new_brace_horizontal),
            FadeIn(new_brace_horizontal_label),
            FadeIn(new_brace_hypotenuse),
            FadeIn(new_brace_hypotenuse_label),
            run_time=1.5
        )

        # Conclude with the universal validity statement and the final conclusion
        self.play(Write(invariance_statement))
        self.wait(2.0)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.5
        )

        # Final conclusion
        final_conclusion = Tex(
            "Therefore, in any right triangle:\\\\"
            r"$c^2 = a^2 + b^2$",
            font_size=40
        )

        self.play(Write(final_conclusion), run_time=2.0)
        self.wait(0.2)
        self.play(Indicate(final_conclusion), color=BLUE)
        self.wait(1.5)

        self.play(FadeOut(final_conclusion), run_time=1.0)

        self.wait(0.5)
