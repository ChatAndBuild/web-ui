import gradio as gr

theme = gr.themes.Origin(
    primary_hue="zinc",
    secondary_hue="purple",
    neutral_hue="neutral",
)

with gr.Blocks(theme=theme) as demo:
    ...