from nicegui import ui

def main():
  ui.add_head_html('<link rel="stylesheet" type="text/css" href="/styles/style.css">')
  with ui.row():
    header = ui.label('Jira Web Visualizer')
  # with ui.row():
  #     ui.text_box()
  dark = ui.dark_mode()
  dark.enable()
  ui.run(port=6060)

if __name__ in ('__main__', '__mp_main__'):
  main()
