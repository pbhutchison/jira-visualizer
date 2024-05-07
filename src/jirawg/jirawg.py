from nicegui import ui
def main():
    ui.icon('thumb_up')
    ui.markdown('This is **Markdown**.')
    ui.html('This is <strong>HTML</strong>.')
    with ui.row():
        ui.label('CSS').style('color: #888; font-weight: bold')
        ui.label('Tailwind').classes('font-serif')
        ui.label('Quasar').classes('q-ml-xl')
    dark = ui.dark_mode()
    dark.enable()
    ui.run(port=6060)


if __name__ in ("__main__", "__mp_main__"):
    main()
