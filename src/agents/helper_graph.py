import os
import tempfile


def show_graph(graph):
    try:
        image_bytes = graph.get_graph().draw_mermaid_png()

        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as f:
            f.write(image_bytes)
            temp_image_path = f.name

        os.system(f'open "{temp_image_path}"')  # macOS

    except Exception as e:
        print(f"Could not display the image: {e}")


def run_graph(graph):
    # show_graph(graph)
    def stream_graph_updates(user_input: str):
        for event in graph.stream(
            {"messages": [{"role": "user", "content": user_input}]}
        ):
            for value in event.values():
                print("Assistant:", value["messages"][-1].content)

    while True:
        try:
            user_input = input("User: ")
            if user_input.lower() in ["quit", "exit", "q"]:
                print("Goodbye!")
                break
            stream_graph_updates(user_input)
        except:
            # fallback if input() is not available
            user_input = "What do you know about LangGraph?"
            print("User: " + user_input)
            stream_graph_updates(user_input)
            break
