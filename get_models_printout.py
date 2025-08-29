from ollama_ls_parser import get_ollama_models_via_ls

def print_models():
    models = get_ollama_models_via_ls()
    for m in models:
        print(m)

# somewhere else in your project
if __name__ == "__main__":
    print_models()
