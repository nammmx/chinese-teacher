from manim import *
import random
import os
import shutil

# === Configuration ===
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0
config.background_color = "#f9f5f0"
config.output_file = "chinese_word_animation"
config.media_dir = "media"

# === Clean previous runs ===
def clear_previous_runs():
    # Clear media directory
    if os.path.exists(config.media_dir):
        shutil.rmtree(config.media_dir)
        print(f"✓ Cleared previous media folder")
    # Recreate media directory
    os.makedirs(config.media_dir, exist_ok=True)

# Call cleanup function when script starts
clear_previous_runs()

# === Sample Data ===
day_number = 1
chinese_word = "茶"  # "tea" - you can change this
pinyin = "chá"
translation = "tea"
hook_line_1 = f"🔥 1 Chinese word a day until we're fluent — Day {day_number}"
hook_line_2 = "You already know this word — even if you've never studied Chinese."
fun_fact = "Tea culture dates back over 2,000 years in China."

# === Color Palettes ===
# Kurzgesagt-inspired palette
kurzgesagt_colors = [
    "#FF9F1C", "#FFBF69", "#CBF3F0", "#2EC4B6", "#3D5A80", 
    "#E71D36", "#FF9F1C", "#2EB6AF", "#4259C3"
]

# Ghibli-inspired palette
ghibli_colors = [
    "#83BCFF", "#EAC7C7", "#A7E8BD", "#FCBC58", "#D6619E",
    "#7EB5A6", "#E8D5C4"
]

class ChineseWordAnimation(Scene):
    def construct(self):
        # 1. Create the dreamy Ghibli-style background
        self.create_dreamy_background()
        
        # 2. Create floating particles (like dust sprites in Ghibli)
        self.create_dust_particles()
        
        # 3. Hook animation
        self.animate_hook_section()
        
        # 4. Transition to word explanation
        self.animate_word_explanation()
        
        # 5. Fun fact with Kurzgesagt-style infographic
        self.animate_fun_fact()
        
        # 6. Outro with call to action
        self.animate_outro()

    def create_dreamy_background(self):
        # Simulate soft, layered painterly sky with gradient
        background_group = VGroup()
        
        # Create base gradient sky
        sky = Rectangle(
            width=config.frame_width + 1,
            height=config.frame_height + 1,
            fill_color=ghibli_colors[0],
            fill_opacity=1,
            stroke_width=0
        )
        
        clouds = VGroup()
        for _ in range(15):
            x = random.uniform(-config.frame_width/2, config.frame_width/2)
            y = random.uniform(-config.frame_height/3, config.frame_height/2)
            radius = random.uniform(0.5, 2.0)
            opacity = random.uniform(0.1, 0.4)
            
            cloud = Circle(
                radius=radius,
                fill_color=WHITE,
                fill_opacity=opacity,
                stroke_width=0
            ).move_to(np.array([x, y, 0]))
            
            clouds.add(cloud)
        
        # Distant mountains (Ghibli style)
        mountain_group = VGroup()
        for i in range(3):
            color = ghibli_colors[i % len(ghibli_colors)]
            opacity = 0.3 - (i * 0.05)
            
            mountain = Polygon(
                np.array([-config.frame_width/2 - 1, -config.frame_height/2 + i, 0]),
                np.array([random.uniform(-2, 0), random.uniform(0, 2), 0]),
                np.array([random.uniform(0, 2), random.uniform(0, 3), 0]),
                np.array([config.frame_width/2 + 1, -config.frame_height/2 + i, 0]),
                fill_color=color,
                fill_opacity=opacity,
                stroke_width=0
            )
            mountain_group.add(mountain)
        
        background_group.add(sky, clouds, mountain_group)
        self.add(background_group)

    def create_dust_particles(self):
        particles = VGroup()
        for _ in range(40):
            x = random.uniform(-config.frame_width/2, config.frame_width/2)
            y = random.uniform(-config.frame_height/2, config.frame_height/2)
            radius = random.uniform(0.02, 0.1)
            color = random.choice(kurzgesagt_colors)
            
            particle = Circle(
                radius=radius,
                fill_color=color,
                fill_opacity=random.uniform(0.4, 0.9),
                stroke_width=0
            ).move_to(np.array([x, y, 0]))
            
            particles.add(particle)
        
        # Animate particles floating gently
        anims = []
        for particle in particles:
            target_pos = particle.get_center() + np.array([
                random.uniform(-1, 1),
                random.uniform(-1, 1),
                0
            ])
            
            anim = AnimationGroup(
                particle.animate.move_to(target_pos),
                run_time=random.uniform(5, 15),
                rate_func=rate_functions.ease_in_out_sine
            )
            anims.append(anim)
        
        self.add(particles)
        self.play(*anims, run_time=8)

    def animate_hook_section(self):
        # Create Kurzgesagt-style geometric decorations
        decorations = self.create_geometric_decorations()
        
        # Title with iconic emoji (Kurzgesagt style)
        hook1 = Text(
            hook_line_1,
            font="Arial",
            font_size=55,
            color="#1d3557",
            weight=BOLD
        ).to_edge(UP, buff=1.2)
        
        # Subtitle with contrasting color
        hook2 = Text(
            hook_line_2,
            font="Arial",
            font_size=42,
            color="#e63946"
        ).next_to(hook1, DOWN, buff=0.5)
        
        # Animate the entrance
        self.play(
            FadeIn(decorations, shift=UP * 0.3, scale=1.1),
            run_time=1.2
        )
        self.play(
            Write(hook1),
            run_time=1.0
        )
        self.play(
            FadeIn(hook2, shift=UP * 0.3),
            run_time=0.8
        )
        
        self.wait(1.5)
        
        # Exit with soft fade
        self.play(
            FadeOut(hook1, shift=UP),
            FadeOut(hook2, shift=UP),
            FadeOut(decorations, scale=0.8),
            run_time=1.0
        )

    def create_geometric_decorations(self):
        # Create Kurzgesagt-style geometric elements
        decorations = VGroup()
        
        # Add some triangles
        for _ in range(5):
            x = random.uniform(-4, 4)
            y = random.uniform(0, 3)
            size = random.uniform(0.1, 0.3)
            color = random.choice(kurzgesagt_colors)
            
            triangle = Triangle(
                fill_color=color, 
                fill_opacity=0.8,
                stroke_width=0
            ).scale(size).move_to([x, y, 0])
            
            decorations.add(triangle)
        
        # Add some circles
        for _ in range(7):
            x = random.uniform(-4, 4)
            y = random.uniform(-1, 4)
            radius = random.uniform(0.1, 0.25)
            color = random.choice(kurzgesagt_colors)
            
            circle = Circle(
                radius=radius,
                fill_color=color,
                fill_opacity=0.7,
                stroke_width=0
            ).move_to([x, y, 0])
            
            decorations.add(circle)
            
        return decorations

    def animate_lantern(self):
        # Create a Ghibli-style lantern with the Chinese character
        outer_glow = Circle(
            radius=2.8,
            fill_color="#FFEFA0",
            fill_opacity=0.2,
            stroke_width=0
        )
        
        inner_glow = Circle(
            radius=2.3,
            fill_color="#FFEFA0",
            fill_opacity=0.5,
            stroke_width=0
        )
        
        lantern = Circle(
            radius=1.8,
            fill_color="#FF9F1C",
            fill_opacity=1,
            stroke_color="#E76F51",
            stroke_width=4,
            stroke_opacity=0.7
        )
        
        # The Chinese character
        word = Text(
            chinese_word,
            font="SimSun", 
            font_size=150,
            color="#1D3557"
        )
        
        lantern_group = VGroup(outer_glow, inner_glow, lantern, word)
        
        # Small decorative elements (Kurzgesagt style)
        decorations = VGroup()
        
        for i in range(8):
            angle = i * PI / 4
            radius = 2.3
            color = random.choice(kurzgesagt_colors)
            
            if i % 2 == 0:
                shape = Circle(
                    radius=0.15,
                    fill_color=color,
                    fill_opacity=0.8,
                    stroke_width=0
                )
            else:
                shape = RegularPolygon(
                    n=3,
                    fill_color=color,
                    fill_opacity=0.8,
                    stroke_width=0
                ).scale(0.15)
            
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            
            shape.move_to([x, y, 0])
            decorations.add(shape)
        
        lantern_group.add(decorations)
        
        # Position and animate
        lantern_group.move_to(ORIGIN)
        
        self.play(
            FadeIn(lantern_group, scale=0.8),
            run_time=1.0
        )
        
        # Subtle floating animation
        self.play(
            lantern_group.animate.shift(UP * 0.3),
            run_time=2.0,
            rate_func=rate_functions.ease_in_out_sine
        )
        self.play(
            lantern_group.animate.shift(DOWN * 0.3),
            run_time=2.0,
            rate_func=rate_functions.ease_in_out_sine
        )
        
        return lantern_group

    def animate_word_explanation(self):
        # Lantern with character
        lantern_group = self.animate_lantern()
        
        # Pronunciation guide with Kurzgesagt-style info panel
        info_panel = RoundedRectangle(
            width=6,
            height=3,
            corner_radius=0.5,
            fill_color="#264653",
            fill_opacity=0.9,
            stroke_color="#2A9D8F",
            stroke_width=3
        ).move_to(DOWN * 3)
        
        # Pronunciation (pinyin)
        pinyin_text = Text(
            f"Pronunciation: {pinyin}",
            font="Arial",
            font_size=40,
            color=WHITE
        ).move_to(info_panel.get_center() + UP * 0.7)
        
        # Translation
        translation_text = Text(
            f"Meaning: {translation}",
            font="Arial",
            font_size=40,
            color=WHITE
        ).move_to(info_panel.get_center() + DOWN * 0.7)
        
        # Kurzgesagt-style decorative elements
        decorative_circle = Circle(
            radius=0.15,
            fill_color=kurzgesagt_colors[0],
            fill_opacity=1,
            stroke_width=0
        ).move_to(info_panel.get_top() + RIGHT * 2.5 + DOWN * 0.25)
        
        decorative_triangle = Triangle(
            fill_color=kurzgesagt_colors[1],
            fill_opacity=1,
            stroke_width=0
        ).scale(0.15).move_to(info_panel.get_top() + RIGHT * 2.8 + DOWN * 0.25)
        
        info_group = VGroup(info_panel, pinyin_text, translation_text, decorative_circle, decorative_triangle)
        
        # Animate the info panel
        self.play(
            FadeIn(info_group, shift=UP * 0.5),
            run_time=0.8
        )
        
        self.wait(2)
        
        # Exit with soft fade
        self.play(
            FadeOut(lantern_group, scale=1.2),
            FadeOut(info_group, shift=DOWN * 0.5),
            run_time=1.0
        )

    def animate_fun_fact(self):
        # Create Kurzgesagt-style info graphic with Ghibli aesthetic
        
        # Background panel
        fact_panel = RoundedRectangle(
            width=8,
            height=5,
            corner_radius=0.5,
            fill_color="#264653",
            fill_opacity=0.85,
            stroke_color="#2A9D8F",
            stroke_width=3
        )
        
        # Title
        fact_title = Text(
            "FUN FACT",
            font="Arial",
            font_size=50,
            color="#FF9F1C",
            weight=BOLD
        ).move_to(fact_panel.get_top() + DOWN * 0.7)
        
        # Fact text
        fact_text = Text(
            fun_fact,
            font="Arial",
            font_size=40,
            color=WHITE
        ).move_to(fact_panel.get_center())
        
        # Kurzgesagt-style decorative elements
        decoration_group = VGroup()
        
        # Tea leaves illustration (simplified geometric version)
        leaf1 = Ellipse(
            width=0.6,
            height=1.3,
            fill_color="#83C167",
            fill_opacity=0.9,
            stroke_width=0
        ).rotate(PI/4).move_to(fact_panel.get_center() + DOWN * 1.5 + LEFT * 1.5)
        
        leaf2 = Ellipse(
            width=0.5,
            height=1.1,
            fill_color="#67B99A",
            fill_opacity=0.9,
            stroke_width=0
        ).rotate(-PI/5).move_to(fact_panel.get_center() + DOWN * 1.5 + RIGHT * 1.5)
        
        # Teacup (simplified)
        cup_base = Ellipse(
            width=1.5,
            height=0.4,
            fill_color="#FFBF69",
            fill_opacity=1,
            stroke_color="#E76F51",
            stroke_width=2
        ).move_to(fact_panel.get_center() + DOWN * 1.5)
        
        cup_body = Arc(
            radius=0.75,
            angle=PI,
            start_angle=PI,
            fill_color="#FFBF69",
            fill_opacity=0,
            stroke_color="#E76F51",
            stroke_width=2
        ).move_to(fact_panel.get_center() + DOWN * 1.3)
        
        # Add geometric accents
        for i in range(5):
            x = random.uniform(-3, 3)
            y = random.uniform(-1.5, 0)
            size = random.uniform(0.1, 0.2)
            color = random.choice(kurzgesagt_colors)
            
            if i % 2 == 0:
                shape = Square(
                    side_length=size,
                    fill_color=color,
                    fill_opacity=0.8,
                    stroke_width=0
                )
            else:
                shape = Circle(
                    radius=size/2,
                    fill_color=color,
                    fill_opacity=0.8,
                    stroke_width=0
                )
            
            shape.move_to(fact_panel.get_center() + [x, y, 0])
            decoration_group.add(shape)
        
        decoration_group.add(leaf1, leaf2, cup_base, cup_body)
        
        # Full fact group
        fact_group = VGroup(fact_panel, fact_title, fact_text, decoration_group)
        
        # Animation
        self.play(
            FadeIn(fact_group, scale=0.9),
            run_time=1.0
        )
        
        self.wait(3)
        
        # Exit
        self.play(
            FadeOut(fact_group, shift=DOWN),
            run_time=1.0
        )

    def animate_outro(self):
        # Create Kurzgesagt-style outro with call to action
        
        # Outro text
        outro_text = Text(
            "Follow for a new word every day!",
            font="Arial",
            font_size=55,
            color="#1d3557",
            weight=BOLD
        )
        
        # Decorative elements
        outro_decorations = VGroup()
        
        # Create a circle of geometric elements
        num_elements = 12
        radius = 2.5
        
        for i in range(num_elements):
            angle = i * (2*PI / num_elements)
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            
            if i % 3 == 0:
                shape = Circle(
                    radius=0.2,
                    fill_color=kurzgesagt_colors[i % len(kurzgesagt_colors)],
                    fill_opacity=0.9,
                    stroke_width=0
                )
            elif i % 3 == 1:
                shape = Triangle(
                    fill_color=kurzgesagt_colors[i % len(kurzgesagt_colors)],
                    fill_opacity=0.9,
                    stroke_width=0
                ).scale(0.2)
            else:
                shape = Square(
                    side_length=0.3,
                    fill_color=kurzgesagt_colors[i % len(kurzgesagt_colors)],
                    fill_opacity=0.9,
                    stroke_width=0
                )
            
            shape.move_to([x, y, 0])
            outro_decorations.add(shape)
        
        # Animated outro
        self.play(
            FadeIn(outro_decorations, scale=1.2, rate_func=rate_functions.ease_out_elastic),
            run_time=1.5
        )
        
        self.play(
            Write(outro_text),
            outro_decorations.animate.scale(1.1),
            run_time=1.2
        )
        
        # Final animation
        self.play(
            FadeOut(outro_text, shift=UP * 0.5),
            FadeOut(outro_decorations, scale=1.5),
            run_time=1.5
        )

# Run the animation
if __name__ == "__main__":
    scene = ChineseWordAnimation()
    scene.render()