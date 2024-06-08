from manim import *
import random
import copy

# Execute: manim -ql external/CreateBackground.py FallingBackground
class FallingBackground(Scene):
    def check_x_y_collision(self, lines, min_distance):
        normal_direction = [-self.direction[1], self.direction[0], 0]
        normal_direction = normal_direction / np.linalg.norm(normal_direction)
        
        # Remove conflicting lines
        lines_to_remove = set()
        for i in range(len(lines)):
            for j in range(i):
                line_x = lines[i]
                line_y = lines[j]
                line_x_start = line_x.get_start()[1]
                line_x_end = line_x.get_end()[1]
                line_y_start = line_y.get_start()[1]
                line_y_end = line_y.get_end()[1]
                # Check if heights overlap
                if (line_x_start < line_y_end and line_x_start > line_y_start) or (line_x_end > line_y_start and line_x_end < line_y_end):
                    # Check if lines are close to each other
                    if abs(normal_direction.dot(line_x.get_start() - line_y.get_start())) < min_distance:
                        lines_to_remove.add(i)

        lines = [line for i, line in enumerate(lines) if i not in lines_to_remove]

        print(f"Removed {len(lines_to_remove)} lines")
                
        return lines

    def create_params(self, line_color, length, num_lines, spread_hor, spread_ver):
        return [{
            'start_pos': (random.random() - 0.5) * spread_ver * UP + (random.random() - 0.5) * RIGHT * spread_hor, 
            'length': (random.random() + 0.5) * length,
            'color': line_color,
            'width': 20
        } for i in range(num_lines)]
    
    def loop_params(self, line_params, loop_distance):
        line_params_loop = copy.deepcopy(line_params)
        for params in line_params_loop:
            params['start_pos'] = params['start_pos'] - loop_distance * self.direction
        line_params += line_params_loop
        return line_params
    
    def create_lines(self, line_params):
        lines = []
        for params in line_params:
            line = Line(params['start_pos'], params['start_pos'] - params['length'] * self.direction)
            line.set_color(params['color'])
            line.set_stroke(width=params['width'])
            line.set_cap_style(CapStyleType.ROUND)
            lines.append(line)

        # Remove colliding lines
        lines = self.check_x_y_collision(lines, min_distance = 0.2)
        return lines

    def construct(self):
        self.direction = DOWN + LEFT
        horizontal_spread = 30
        num_lines = 90
        length = 0.8

        line_params = self.create_params(line_color = ManimColor.from_hex("#93dbe9"), length = length, num_lines = num_lines, spread_hor = horizontal_spread, spread_ver = 10)
        line_params = self.loop_params(line_params, loop_distance = 10)
        lines = self.create_lines(line_params)
        animations = [line.animate.shift(10*self.direction) for line in lines]

        line_params_2 = self.create_params(line_color = ManimColor.from_hex("#689cc5"), length = length, num_lines = num_lines, spread_hor = horizontal_spread, spread_ver = 15)
        line_params_2 = self.loop_params(line_params_2, loop_distance = 15)
        lines_2 = self.create_lines(line_params_2)
        animations_2 = [line.animate.shift(15*self.direction) for line in lines_2]

        line_params_3 = self.create_params(line_color = ManimColor.from_hex("#5e6fa3"), length = length, num_lines = num_lines, spread_hor = horizontal_spread, spread_ver = 20)
        line_params_3 = self.loop_params(line_params_3, loop_distance = 20)
        lines_3 = self.create_lines(line_params_3)
        animations_3 = [line.animate.shift(20*self.direction) for line in lines_3]

        # Combine animations
        animations += animations_2
        animations += animations_3
        

        self.play(
            *animations,
            rate_func=linear,
            run_time=7
        )


# test = FallingBackground()
# test.construct()