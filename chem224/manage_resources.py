import json
class LectureResources:
    def __init__(self):
        self.equations = []
        self.figures = []
        self.problems = []
        self.keywords = []
        self.symbols = []

    def add_equation(self, name, eq_type, keywords, form, description):
        equation_data = {
            "name": name,
            "type": eq_type,
            "keyword": keywords,
            "form": form,
            "description": description
        }
        self.equations.append(equation_data)
        
    def add_figure(self, name, fig_type, keywords, caption, code):
        figure_data = {
            "name": name, # name of the figure
            "type": fig_type, # figure type (e.g. plot, diagram, image etc.)
            "keyword": keywords,  # Generate a list of keywords from the caption, name, and code
            "caption": caption, # caption associated with the figure
            "code": code # code associated with the figure
        }
        self.figures.append(figure_data)
    
    def add_problem(self, name, keywords, description, graphics, solution, references, code):
        problem_data = {
            "name": name,
            "keyword": keywords,
            "description": description,
            "graphics": graphics,
            "solution": solution,
            "references": references,
            "code": code
        }
        self.problems.append(problem_data)

    def add_keyword(self, definition, references):
        keyword_data = {
            "definition": definition,
            "references": references
        }
        self.keywords.append(keyword_data)

    def add_symbol(self, name, keywords, equations, definition, references):
        symbol_data = {
            "name": name,
            "keyword": keywords,
            "equations": equations,
            "definition": definition,
            "references": references
        }
        self.symbols.append(symbol_data)

    def to_json(self):
        return json.dumps({
            "equations": self.equations,
            "figures": self.figures,
            "problems": self.problems,
            "keywords": self.keywords,
            "symbols": self.symbols
        }, indent=4)
# a script to update the JSON files with new objectives, concepts, equations, etc.