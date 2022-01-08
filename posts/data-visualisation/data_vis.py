from bokeh.theme import Theme

theme = Theme(filename="./theme.yaml")

doc = Document(theme=theme) #### or Document().theme = theme
doc.add_root(plot)

