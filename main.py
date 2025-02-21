# main.py
from ttkthemes import ThemedTk
from gui import SalesAnalyzerGUI

def main():
    """Initialize and run the application"""
    try:
        # Create themed main window
        root = ThemedTk(theme="arc")
        root.title("Sistema de Análise de Vendas")
        
        # Set minimum window size
        root.minsize(800, 600)
        
        # Center window on screen
        window_width = 800
        window_height = 600
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_height/2)
        
        root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        
        # Initialize GUI
        app = SalesAnalyzerGUI(root)
        
        # Start main loop
        root.mainloop()
        
    except Exception as e:
        print(f"Erro ao iniciar aplicação: {str(e)}")
        raise

if __name__ == "__main__":
    main()