import gradio as gr
from dotenv import load_dotenv
from src.controller.RunController import run_search_agent
import sys
print(sys.path)

load_dotenv(override=True)


async def run_ui_request(query: str):
    async for chunk in run_search_agent(query):
        yield chunk


with gr.Blocks(theme=gr.themes.Default(primary_hue="sky")) as ui:
    gr.Markdown("# Deep Research")
    query_textbox = gr.Textbox(label="What topic would you like to research?")
    run_button = gr.Button("Run", variant="primary")
    report = gr.Markdown(label="Report")
    
    run_button.click(fn=run_ui_request, inputs=query_textbox, outputs=report)
    query_textbox.submit(fn=run_ui_request, inputs=query_textbox, outputs=report)

ui.launch(inbrowser=True)