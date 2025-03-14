import gradio as gr
import gradio.themes as themes
import argparse
from src.utils.default_config_settings import default_config

gr.themes.builder()


def main():
  parser = argparse.ArgumentParser(description="Gradio UI for Browser Agent")
  parser.add_argument("--ip", type=str, default="127.0.0.1", help="IP address to bind to")
  parser.add_argument("--port", type=int, default=7788, help="Port to listen on")
  args = parser.parse_args()

  config_dict = default_config()

  demo = gr.Blocks(
    title="Pivotal"
  )

  demo.launch(server_name=args.ip, server_port=args.port, favicon_path="./assets/favicon.svg")

if __name__ == '__main__':
    main()