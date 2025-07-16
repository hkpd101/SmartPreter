import ollama
import subprocess
import time
import threading
import os

class LocalOllamaRunner:
    def __init__(self, model_name="deepseek-coder:6.7b-instruct"):
        self.model_name = model_name
        self.ollama_process = None
        self.is_running = False
        
    def start_ollama_server(self):
        """Start Ollama server in background"""
        try:
            # Check if Ollama is already running
            try:
                ollama.list()
                self.is_running = True
                print("Ollama server already running")
                return True
            except:
                pass
            
            # Start Ollama serve in background
            print("Starting Ollama server...")
            self.ollama_process = subprocess.Popen(
                ['ollama', 'serve'],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            
            # Wait for server to start
            for _ in range(30):  # Wait up to 30 seconds
                try:
                    time.sleep(1)
                    ollama.list()
                    self.is_running = True
                    print("Ollama server started successfully")
                    return True
                except:
                    continue
                    
            print("Failed to start Ollama server")
            return False
            
        except Exception as e:
            print(f"Error starting Ollama: {e}")
            return False
    
    def ensure_model_available(self):
        """Ensure the model is downloaded and available"""
        try:
            models = ollama.list()
            model_names = [model.model for model in models.models]
            
            if self.model_name not in model_names:
                print(f"Downloading model {self.model_name}...")
                ollama.pull(self.model_name)
                print("Model downloaded successfully")
            else:
                print(f"Model {self.model_name} already available")
            return True
            
        except Exception as e:
            print(f"Error ensuring model availability: {e}")
            return False
    
    def run_inference(self, prompt: str) -> str:
        """Run inference with the local model"""
        try:
            # Ensure server is running
            if not self.is_running:
                if not self.start_ollama_server():
                    return "Error: Failed to start Ollama server"
            
            # Ensure model is available
            if not self.ensure_model_available():
                return "Error: Failed to load model"
            
            print(f"Running inference with model: {self.model_name}")
            
            # Run inference
            response = ollama.generate(
                model=self.model_name,
                prompt=prompt,
                stream=False
            )
            
            return response['response']
            
        except Exception as e:
            return f"Error during inference: {str(e)}"
    
    def stop_server(self):
        """Stop the Ollama server"""
        if self.ollama_process:
            self.ollama_process.terminate()
            self.ollama_process = None
            self.is_running = False

# Global instance
local_runner = LocalOllamaRunner()

def run_ollama_inference(prompt: str, model="deepseek-coder:6.7b-instruct") -> str:
    """
    Run inference using local Ollama instance.
    
    Args:
        prompt (str): The input prompt for the model
        model (str): The model to use for inference
        
    Returns:
        str: The model's response or error message
    """
    if model != local_runner.model_name:
        local_runner.model_name = model
    
    return local_runner.run_inference(prompt)

if __name__ == "__main__":
    # Test the function when running this file directly
    print("Testing local Ollama connection...")
    result = run_ollama_inference("Say hello in one sentence.")
    print(f"Result: {result}")
    
    # Clean up
    local_runner.stop_server()