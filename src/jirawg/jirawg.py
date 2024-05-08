from nicegui import ui

def main():
  with ui.row().style('width: 100%;'):
    header_styles = 'color: #00b4ff; '
    header_styles = header_styles.join('margin: auto; ')
    header_styles = header_styles.join('font-size: 300%; ')
    ui.label('Jira Web Visualizer').style(header_styles)
  dark = ui.dark_mode()
  dark.enable()
  ui.run(port=6060)

if __name__ in ('__main__', '__mp_main__'):
  main()
