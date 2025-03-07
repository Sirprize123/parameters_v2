
# USECASES OBRIGATORIOS:
#     XX
#     XX.0
#     XX.X
#     XX.XX
    
#     PARA CADA PARAM 

#O QUE NAAAAAAAAAAAAAAAAAAAAAAAAAAAAO FUNCIONA:
    #QUANDO ADD XX.X NÃO ADD EM NENHUM Z VALUE E NAO MATA O DIALOGO DE ADD Param
    


#usecases z = xx.x não estao adicionando nenhum param_value
#botao z mostra as peças(actdrive true) e user seleciona ql add
#botao actdrive add coisas
#grafico add coisas nas linhas certas, grafico chamar botao
#cada grafico addiciona seu respectivo ponto
#consertar graficos que nao add double click
#figure out act_drive graph




import re
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox, Text, Scrollbar, simpledialog, ttk
import os
from datetime import datetime
import ctypes

def format_value(value):
    value_str = str(value)
    value_str_splitted = value_str.split('.')
    if len(value_str_splitted[1]) == 1:
        if value_str_splitted[1] == '0':
            return f"{int(value)}}}"
    #     else:
    #         value_str = format_value(value)
    # elif len(value_str_splitted[1]) == 2:
    #     value_str = format_value(value)
    return "{:.2f}".format(value) 
def add_tool_rpm(param_name, param_value, content_lines, is_z_height, value, line_number):
    if param_name == 'TOOL_RPM':
                    # For TOOL_RPM, add trigger command for both Z height and print progress
        param_line = f"TRIGGER WHEN DISTANCE=0 DELAY=0 DO TOOL_RPM={param_value}"
        if is_z_height:
            content_lines.insert(line_number + 1, param_line)
                    
        else:
            trigger_pattern = f"TRIGGER WHEN DISTANCE=0 DELAY=0 DO PRINT_PROGRESS={int(value)}"
      
            content_lines.insert(line_number + 1, param_line)
                    
    

# class ParameterGraph:
#     def __init__(self, master, original_content=None):
#         self.original_content = original_content
#         self.z_tool_points = []
#         self.z_feed_points = []
#         self.z_cool_points = []
#         self.z_act_drive_points = []
#         self.tool_points = []
#         self.feed_points = []
#         self.cool_points = []
#         self.act_drive_points = []
#         self.z_points = []  # Initialize z_points here

#         # Create a notebook for tabs
#         self.notebook = ttk.Notebook(master)
#         self.notebook.pack(fill=tk.BOTH, expand=True)

#         # Create tabs for each parameter
#         self.tool_speed_tab = ttk.Frame(self.notebook)
#         self.feed_rate_tab = ttk.Frame(self.notebook)
#         self.cooling_tab = ttk.Frame(self.notebook)
#         self.act_drive_tab = ttk.Frame(self.notebook)

#         self.notebook.add(self.tool_speed_tab, text='Tool Speed')
#         self.notebook.add(self.feed_rate_tab, text='Feed Rate')
#         self.notebook.add(self.cooling_tab, text='Cooling')
#         self.notebook.add(self.act_drive_tab, text='ACT_DRIVE')

#         # Initialize figures for each tab
#         self.tool_speed_figure = plt.Figure(figsize=(6, 4), dpi=100)
#         self.feed_rate_figure = plt.Figure(figsize=(6, 4), dpi=100)
#         self.cooling_figure = plt.Figure(figsize=(6, 4), dpi=100)
#         self.act_drive_figure = plt.Figure(figsize=(6, 4), dpi=100)

#         # Create canvas for each figure
#         self.tool_speed_canvas = FigureCanvasTkAgg(self.tool_speed_figure, master=self.tool_speed_tab)
#         self.feed_rate_canvas = FigureCanvasTkAgg(self.feed_rate_figure, master=self.feed_rate_tab)
#         self.cooling_canvas = FigureCanvasTkAgg(self.cooling_figure, master=self.cooling_tab)
#         self.act_drive_canvas = FigureCanvasTkAgg(self.act_drive_figure, master=self.act_drive_tab)

#         self.tool_speed_canvas.draw()
#         self.feed_rate_canvas.draw()
#         self.cooling_canvas.draw()
#         self.act_drive_canvas.draw()

#         self.tool_speed_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
#         self.feed_rate_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
#         self.cooling_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
#         self.act_drive_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

#         # Bind double-click event to the canvas
#         self.tool_speed_canvas.mpl_connect('button_press_event', self.on_double_click)

#     def set_original_content(self, original_content):
#         self.original_content = original_content
#         self.update_graph_with_loaded_params()

#     def add_data_point(self, z_point, tool_point, feed_point, cool_point, act_drive_point):
#         """Add a new data point to the graph for the specified Z height."""
        
#         # Append new values to the existing lists
#         self.z_tool_points.append(z_point)
#         self.tool_points.append(tool_point)
#         self.z_feed_points.append(z_point)
#         self.feed_points.append(feed_point)
#         self.z_cool_points.append(z_point)
#         self.cool_points.append(cool_point)
#         self.z_act_drive_points.append(z_point)
#         self.act_drive_points.append(act_drive_point)
        
#         # Ensure all points are sorted by Z height
#         sorted_indices = sorted(range(len(self.z_tool_points)), key=lambda i: self.z_tool_points[i])
        
#         self.z_tool_points = [self.z_tool_points[i] for i in sorted_indices]
#         self.tool_points = [self.tool_points[i] for i in sorted_indices]
#         self.z_feed_points = [self.z_feed_points[i] for i in sorted_indices]
#         self.feed_points = [self.feed_points[i] for i in sorted_indices]
#         self.z_cool_points = [self.z_cool_points[i] for i in sorted_indices]
#         self.cool_points = [self.cool_points[i] for i in sorted_indices]
#         self.z_act_drive_points = [self.z_act_drive_points[i] for i in sorted_indices]
#         self.act_drive_points = [self.act_drive_points[i] for i in sorted_indices]
        
#         print(f"Current Z Tool Points: {self.z_tool_points}")  # Debugging output
#         print(f"Current Tool Points: {self.tool_points}")  # Debugging output
        
#         # Update the graph with the new data
#         self.plot_parameters(
#             self.z_tool_points, 
#             self.tool_points, 
#             self.z_feed_points, 
#             self.feed_points, 
#             self.z_cool_points, 
#             self.cool_points, 
#             self.z_act_drive_points, 
#             self.act_drive_points
#         )
#     def plot_parameters(self, z_tool_points, tool_points, z_feed_points, feed_points, z_cool_points, cool_points, z_act_drive_points, act_drive_points):
#         try:
#             # Clear previous plots only if necessary
#             self.tool_speed_figure.clear()
#             self.feed_rate_figure.clear()
#             self.cooling_figure.clear()
#             self.act_drive_figure.clear()

#             # Function to sort points based on Z values
#             def sort_points(z_points, param_points):
#                 sorted_indices = sorted(range(len(z_points)), key=lambda i: z_points[i])
#                 return [z_points[i] for i in sorted_indices], [param_points[i] for i in sorted_indices]

#             self.z_tool_points, self.tool_points = sort_points(self.z_tool_points, self.tool_points)
#             self.z_feed_points, self.feed_points = sort_points(self.z_feed_points, self.feed_points)
#             self.z_cool_points, self.cool_points = sort_points(self.z_cool_points, self.cool_points)
#             self.z_act_drive_points, self.act_drive_points = sort_points(self.z_act_drive_points, self.act_drive_points)

#             # Plot only the loaded parameter values
#             if z_tool_points and tool_points:
#                 ax1 = self.tool_speed_figure.add_subplot(111)
#                 ax1.set_xlabel('Z Height (mm)')
#                 ax1.set_ylabel('Tool Speed (rpm)')
#                 ax1.grid(True)
#                 ax1.set_ylim(-20, 150)  # Expanded Y-axis range for Tool Speed
#                 ax1.set_xlim(-10, 110)  # Expanded X-axis range for Z Height
#                 ax1.scatter(z_tool_points, tool_points, label='Tool Speed', color='#ffb3ff', marker='o')  # Use scatter for dots
#                 ax1.plot(z_tool_points, tool_points, color='#ffb3ff')  # Connect dots with lines
#                 ax1.legend(loc='upper right')

#             if z_feed_points and feed_points:
#                 ax2 = self.feed_rate_figure.add_subplot(111)
#                 ax2.set_xlabel('Z Height (mm)')
#                 ax2.set_ylabel('Feed Rate (mm/s)')
#                 ax2.grid(True)
#                 ax2.set_ylim(-1, 3)  # Expanded Y-axis range for Feed Rate
#                 ax2.set_xlim(-10, 110)  # Expanded X-axis range for Z Height
#                 ax2.scatter(z_feed_points, feed_points, label='Feed Rate', color='#ffb3b3', marker='o')  # Use scatter for dots
#                 ax2.plot(z_feed_points, feed_points, color='#ffb3b3')  # Connect dots with lines
#                 ax2.legend(loc='upper right')

#             if z_cool_points and cool_points:
#                 ax3 = self.cooling_figure.add_subplot(111)
#                 ax3.set_xlabel('Z Height (mm)')
#                 ax3.set_ylabel('Cooling (%)')
#                 ax3.grid(True)
#                 ax3.set_ylim(-10, 150)  # Expanded Y-axis range for Cooling
#                 ax3.set_xlim(-10, 110)  # Expanded X-axis range for Z Height
#                 ax3.scatter(z_cool_points, cool_points, label='Cooling', color='#87CEEB', marker='o')  # Use scatter for dots
#                 ax3.plot(z_cool_points, cool_points, color='#87CEEB')  # Connect dots with lines
#                 ax3.legend(loc='upper right')

#             if z_act_drive_points and act_drive_points:
#                 ax4 = self.act_drive_figure.add_subplot(111)
#                 ax4.set_xlabel('Z Height (mm)')
#                 ax4.set_ylabel('ACT_DRIVE')
#                 ax4.grid(True)
#                 ax4.set_ylim(-0.1, 1.1)  # Expanded Y-axis range for ACT_DRIVE
#                 ax4.set_xlim(-10, 110)  # Expanded X-axis range for Z Height
#                 act_drive_points_bool = ['True' if value == 1 else 'False' for value in act_drive_points]  # Convert 1 to True and 0 to False
#                 ax4.scatter(z_act_drive_points, act_drive_points_bool, label='ACT_DRIVE', color='#90EE90', marker='o')  # Use scatter for dots
#                 ax4.plot(z_act_drive_points, act_drive_points_bool, color='#90EE90')  # Connect dots with lines
#                 ax4.legend(loc='upper right')

#             # Draw the canvases
#             self.tool_speed_canvas.draw()
#             self.feed_rate_canvas.draw()
#             self.cooling_canvas.draw()
#             self.act_drive_canvas.draw()

#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to update graph: {str(e)}")
#             print(f"Error: {str(e)}")
        

#     def update_graph_with_loaded_params(self):
#         z_tool_points, tool_points, z_feed_points, feed_points, z_cool_points, cool_points, z_act_drive_points, act_drive_points = self.extract_parameters()
        
#         # Clear existing data points before loading new ones
#         self.z_tool_points.clear()
#         self.tool_points.clear()
#         self.z_feed_points.clear()
#         self.feed_points.clear()
#         self.z_cool_points.clear()
#         self.cool_points.clear()
#         self.z_act_drive_points.clear()
#         self.act_drive_points.clear()

#         # Load the new data
#         self.z_tool_points.extend(z_tool_points)
#         self.tool_points.extend(tool_points)
#         self.z_feed_points.extend(z_feed_points)
#         self.feed_points.extend(feed_points)
#         self.z_cool_points.extend(z_cool_points)
#         self.cool_points.extend(cool_points)
#         self.z_act_drive_points.extend(z_act_drive_points)
#         self.act_drive_points.extend(act_drive_points)

#         # Update the graph with the extracted values
#         self.plot_parameters(
#             self.z_tool_points, 
#             self.tool_points, 
#             self.z_feed_points, 
#             self.feed_points, 
#             self.z_cool_points, 
#             self.cool_points, 
#             self.z_act_drive_points, 
#             self.act_drive_points
#         )

#     def extract_parameters(self):
#         z_tool_points = []
#         z_feed_points = []
#         z_cool_points = []
#         z_act_drive_points = []
        
#         tool_points = []
#         feed_points = []
#         cool_points = []
#         act_drive_points = []

#         lines = self.original_content.splitlines()
#         for line_num, line in enumerate(lines):
#             # Extract parameter values
#             if 'TOOL_RPM' in line:
#                 tool_match = re.search(r'TOOL_RPM\s*=\s*(\d+\.?\d*)', line)
#                 if tool_match:
#                     tool_value = float(tool_match.group(1))
#                     z_value = self.find_nearby_z_value(lines, line_num)  # Call here for initial parameters
#                     z_tool_points.append(z_value if z_value is not None else (0 if line_num < 10 else 100))
#                     tool_points.append(tool_value)

#             elif '$VEL.CP' in line:
#                 feed_match = re.search(r'\$VEL\.CP\s*=\s*(\d+\.?\d*)', line)
#                 if feed_match:
#                     feed_value = float(feed_match.group(1))
#                     z_value = self.find_nearby_z_value(lines, line_num)  # Call here for initial parameters
#                     z_feed_points.append(z_value if z_value is not None else (0 if line_num < 10 else 100))
#                     feed_points.append(feed_value)

#             elif 'LAYER_COOLING' in line:
#                 cool_match = re.search(r'LAYER_COOLING\s*=\s*(\d+)', line)
#                 if cool_match:
#                     cool_value = float(cool_match.group(1))
#                     z_value = self.find_nearby_z_value(lines, line_num)  # Call here for initial parameters
#                     z_cool_points.append(z_value if z_value is not None else (0 if line_num < 10 else 100))
#                     cool_points.append(cool_value)

#             elif 'ACT_DRIVE' in line:
#                 act_drive_match = re.search(r'ACT_DRIVE\s*=\s*(TRUE|FALSE)', line)
#                 if act_drive_match:
#                     act_drive_value = 1.0 if act_drive_match.group(1) == 'TRUE' else 0.0
#                     z_value = self.find_nearby_z_value(lines, line_num)  # Call here for initial parameters
#                     z_act_drive_points.append(z_value if z_value is not None else (0 if line_num < 10 else 100))
#                     act_drive_points.append(act_drive_value)

#         # Debugging output to check lengths of lists
#         print(f"Z Tool Points Length: {len(z_tool_points)}")
#         print(f"Z Feed Points Length: {len(z_feed_points)}")
#         print(f"Z Cool Points Length: {len(z_cool_points)}")
#         print(f"Z Act Drive Points Length: {len(z_act_drive_points)}")
#         print(f"Tool Points Length: {len(tool_points)}")
#         print(f"Feed Points Length: {len(feed_points)}")
#         print(f"Cool Points Length: {len(cool_points)}")
#         print(f"Act Drive Points Length: {len(act_drive_points)}")

#         # Ensure all lists are of the same length
#         if len(z_tool_points) != len(tool_points) or len(z_feed_points) != len(feed_points) or len(z_cool_points) != len(cool_points) or len(z_act_drive_points) != len(act_drive_points):
#             messagebox.showerror("Error", "Data lists are not of the same length.")
#             return [], [], [], [], []

#         # Return all Z points and their corresponding parameter values
#         return z_tool_points, tool_points, z_feed_points, feed_points, z_cool_points, cool_points, z_act_drive_points, act_drive_points

    # def find_nearby_z_value(self, lines, line_num):
    #     # Check 10 lines before and after the current line for Z values
    #     start = max(0, line_num - 10)
    #     end = min(len(lines), line_num + 11)  # +11 to include the line at line_num

    #     z_pattern = re.compile(r'LIN.*?Z\s*(-?\d+(\.\d+)?)')  # Updated regex pattern

    #     for i in range(start, end):
    #         z_match = z_pattern.search(lines[i])
    #         if z_match:
    #             return float(z_match.group(1))  # Return the matched Z value as a float

    #     # If no Z value found, determine default based on position
    #     if line_num < 1000:  # Near the beginning
    #         return 0
    #     elif line_num >= len(lines) - 1000:  # Near the end
    #         return 100
    #     return None  # Should not reach here

#     def on_double_click(self, event):
#         """Handle double-click event to add a parameter dot."""
#         if event.dblclick:  # Check if it's a double-click
#             # Get the x and y coordinates from the event
#             x = event.xdata
#             y = event.ydata
            
#             # Find the corresponding values for the points based on the coordinates
#             z_point = round(x)  # Assuming x corresponds to Z height
#             tool_point = y  # Assuming y corresponds to Tool Speed
            
#             # Initialize feed_point, cool_point, and act_drive_point
#             feed_point = self.feed_points[-1] if self.feed_points else 0  # Use last value or 0 if empty
#             cool_point = self.cool_points[-1] if self.cool_points else 0  # Use last value or 0 if empty
#             act_drive_point = self.act_drive_points[-1] if self.act_drive_points else 0  # Use last value or 0 if empty
            
#             # Call the method to add the data point
#             self.add_data_point(z_point, tool_point, feed_point, cool_point, act_drive_point)
#             print(f"Added point: Z={z_point}, Tool Speed={tool_point}, Feed Rate={feed_point}, Cooling={cool_point}, ACT_DRIVE={act_drive_point}")  # Debugging output

class SRCModifierApp:
    
    def __init__(self, root):
        
            self.root = root
            self.root.title("SRC File Modifier")
            self.root.geometry("1140x700")
            
            # Load the Forest theme
            
            self.root.tk.call('source', 'forest-light.tcl')
            style = ttk.Style()
            style.theme_use('forest-light')

            # Initialize the menubar
            self.menubar = tk.Menu(self.root)
            self.root.config(menu=self.menubar)
            
            
            
            # Configure custom button styles
            style.configure('Action.TButton', padding=5)
            style.configure('Accent.TButton', padding=5)

            # Create File menu
            self.file_menu = tk.Menu(self.menubar, tearoff=0)
            self.menubar.add_cascade(label="File", menu=self.file_menu)
            self.file_menu.add_command(label="Open", command=self.load_file)
            self.file_menu.add_command(label="Save", command=self.modify_file, state='disabled')
            self.file_menu.add_separator()
            self.file_menu.add_command(label="Exit", command=self.root.quit)

            # Store reference to save menu item for enabling/disabling
            self.save_menu_item = self.file_menu
            # Add collapsible frame for file metadata editing
            self.metadata_frame = ttk.Frame(self.root)
            self.metadata_frame.pack(fill='x', padx=2, pady=2)
            
            # Metadata header with toggle button
            metadata_header = ttk.Frame(self.metadata_frame)
            metadata_header.pack(fill='x')
            
            self.metadata_toggle = ttk.Button(metadata_header, text="▶", width=3)
            self.metadata_toggle.pack(side='left', padx=1)
            ttk.Label(metadata_header, text="Change Name and Start Position").pack(side='left', padx=5)
            
            # Content frame that will be collapsed/expanded
            self.metadata_content = ttk.Frame(self.metadata_frame)
            # Start collapsed - don't pack initially
            
            # DEF name section
            def_frame = ttk.Frame(self.metadata_content) 
            def_frame.pack(fill='x', pady=1)
            ttk.Label(def_frame, text="Display Name:").pack(side='left', padx=5)
            self.def_entry = ttk.Entry(def_frame, width=20)
            self.def_entry.pack(side='left')
            
            # Update button for DEF name
            ttk.Button(def_frame, text="Update", width=8,
                      command=self.update_file_settings).pack(side='left', padx=5)
            
            # PARKPOS section
            parkpos_frame = ttk.Frame(self.metadata_content)
            parkpos_frame.pack(fill='x', pady=1)
            ttk.Label(parkpos_frame, text="Starting Position:").pack(side='left', padx=5)
            
            # Compact position entries
            positions = ['X', 'Y', 'Z', 'A', 'B', 'C', 'S', 'T']
            self.parkpos_entries = {}
            
            pos_frame = ttk.Frame(parkpos_frame)
            pos_frame.pack(side='left')
            
            for i, pos in enumerate(positions):
                ttk.Label(pos_frame, text=pos).pack(side='left')
                self.parkpos_entries[pos] = ttk.Entry(pos_frame, width=5)
                self.parkpos_entries[pos].pack(side='left', padx=(0,3))
            
            # Update button for PARKPOS
            ttk.Button(parkpos_frame, text="Update", width=8,
                      command=self.update_file_settings).pack(side='left', padx=5)
            # Add toggle_metadata_frame method
            def toggle_metadata_frame(self):
                if self.metadata_content.winfo_viewable():
                    self.metadata_content.pack_forget()
                    self.metadata_toggle.configure(text="▶")
                else:
                    self.metadata_content.pack(fill='x', padx=5, pady=2)
                    self.metadata_toggle.configure(text="▼")
            
            # Make toggle_metadata_frame a method of the class
            self.toggle_metadata_frame = toggle_metadata_frame.__get__(self, SRCModifierApp)
            
            # Configure toggle button command
            self.metadata_toggle.configure(command=self.toggle_metadata_frame)
            
            # Initialize parameters
            self.entries = {}
            self.params = {}
            self.param_line_numbers = {}  # Store line numbers for each parameter
            self.param_groups = {}
            self.step_size = 5.0  # Default step size (%)
            
            self.input_file = None
            self.original_content = ""
            # self.show_graph = tk.BooleanVar(value=True)
            
            # Create figure and canvas after UI elements
            self.fig = None
            self.ax = None
            self.canvas = None
            
            self.dragging_point = None
            self.preview_text = None
            # Define colors for each parameter type
            self.param_colors = {
                'TOOL_RPM': '#ffb3ff',  # Light Magenta
                '$VEL.CP': '#ffb3b3',   # Light Red
                'LAYER_COOLING': '#87CEEB',      # Light Blue
                'ACT_DRIVE': '#90EE90'  # Light LIGHT GREEN
            }
            
            # Store custom parameters
            self.print_progress_params = {}  # For print progress parameters
            # Store custom Z height parameters
            self.custom_z_params = {}
            self.param_frames = {}
            # Store Z height parameter frames
            self.z_param_frames = {}
            self.print_progress_frames = {}  # New dict to store print progress frames separately
            self.available_params = ['TOOL_RPM', '$VEL.CP', 'LAYER_COOLING', 'ACT_DRIVE']
            
            # Store parameter groups
            self.param_groups = {}
            
            # Store content frames for each parameter type
            self.content_frames = {}
            
            # Store header labels for each parameter type
            self.header_labels = {}

            # Store frame positions
            self.frame_positions = {}
            
            # Store trigger parameters that should be preserved
            self.trigger_params = {}
            
            # Add undo/redo history
            self.undo_history = []
            self.redo_history = []
            self.max_history = 50  # Maximum number of operations to store
            
            # Add search tracking variables
            self.current_search_pos = "1.0"
            self.last_search_term = ""
            
            # Configure custom styles for the theme
            style = ttk.Style()
            
            # Configure custom button styles
            style.configure('Action.TButton', padding=5)
            style.configure('Accent.TButton', padding=5)
            
            # Create menu bar
            self.menubar = tk.Menu(self.root)
            self.root.config(menu=self.menubar)
            
            # Create File menu
            self.file_menu = tk.Menu(self.menubar, tearoff=0)
            self.menubar.add_cascade(label="File", menu=self.file_menu)
            self.file_menu.add_command(label="Open", command=self.load_file)
            self.file_menu.add_command(label="Save", command=self.modify_file, state='disabled')
            self.file_menu.add_separator()
            self.file_menu.add_command(label="Exit", command=self.root.quit)
            
            
            # Store reference to save menu item for enabling/disabling
            self.save_menu_item = self.file_menu
            # Initialize save button
            self.save_button = tk.Button(self.root, text="Save", command=self.modify_file, state=tk.DISABLED)
            
            # Initialize undo/redo buttons
            self.undo_button = tk.Button(self.root, text="Undo", command=self.undo_last_action, state=tk.DISABLED)
            self.undo_button.pack(side='bottom', pady=5)
            
            self.redo_button = tk.Button(self.root, text="Redo", command=self.redo_last_action, state=tk.DISABLED)
            self.redo_button.pack(side='bottom', pady=5)
            
            # Initialize Z points lists
            self.z_tool_points = []
            self.z_feed_points = []  # Initialize z_feed_points
            self.z_cool_points = []  # Initialize z_cool_points
            self.z_act_drive_points = []
            
            # Create a frame for buttons
            self.add_buttons_frame = ttk.Frame(self.root)  # Define add_buttons_frame here
            self.add_buttons_frame.pack(fill='x', padx=5, pady=5)
            
            
            
            # Create UI elements
            self.create_ui()
           
            
            

           
            
    def update_file_settings(self):
        try:
            if not self.original_content:
                messagebox.showerror("Error", "Please load a file first")
                return
            
            # Save current state before modification
            self.save_state()
            
            lines = self.original_content.splitlines()
            modified = False
            
            # Get file name without extension
            file_name = os.path.basename(self.input_file).split('.')[0]
            
            # Update the lines
            if self.def_entry.get().strip():
                lines[0] = f"DEF {self.def_entry.get()}"
                modified = True
            
            # Build PARKPOS string from entries
            parkpos_str = "PARKPOS = {POS:"
            for pos, entry in self.parkpos_entries.items():
                if pos in ['S', 'T']:
                    parkpos_str += f" {pos} 'B{entry.get()}',"
                else:
                    parkpos_str += f" {pos} {entry.get()},"
            parkpos_str = parkpos_str.rstrip(',') + '}'
            
            for i, line in enumerate(lines):
                if line.startswith("PARKPOS = "):  # Modify PARKPOS line
                    lines[i] = parkpos_str
                    modified = True
                elif line.startswith(";generated with "):  # Overwrite generation info
                    lines[i] = ";generated by @BLU3D, experimental prototype 0.1"
                    modified = True
                elif line.startswith(";Source file name: "):  # Overwrite source file name
                    lines[i] = f";Source file name: {file_name}.src"
                    modified = True
            
            if modified:
                self.original_content = '\n'.join(lines) + '\n'
                
                # Force preview update
                if self.preview_text:
                    self.preview_text.delete("1.0", tk.END)
                    self.preview_text.insert("1.0", self.original_content)
                self.update_preview()
                
                self.save_button.config(state=tk.NORMAL)
        
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update settings: {str(e)}")

    def load_file(self):
         
        try:
            # Open file dialog to select .src file
            file_path = filedialog.askopenfilename(
                filetypes=[("SRC files", "*.src"), ("All files", "*.*")]
            )
            
            if not file_path:
                messagebox.showwarning("Warning", "No file selected.")
                return
                
            self.input_file = file_path
            
            # Read file content
            with open(file_path, 'r', encoding='utf-8') as file:
                self.original_content = file.read()
            
            # Check if original_content is None or empty
            if self.original_content is None or self.original_content.strip() == "":
                messagebox.showerror("Error", "Loaded file is empty or could not be read.")
                return
            
            # After loading file content, extract DEF and PARKPOS values
            lines = self.original_content.splitlines()
            if lines:
                for line in lines:
                    if line.startswith("DEF "):
                        def_value = line.split("DEF  ", 1)[1]
                        self.def_entry.delete(0, tk.END)
                        self.def_entry.insert(0, def_value)
                    elif line.startswith("PARKPOS = "):
                        # Parse PARKPOS values
                        parkpos_str = line.split("PARKPOS = ", 1)[1]
                        # Extract values using regex
                        pos_pattern = re.compile(r'([XYZABCST])\s+(?:\'B)?([^,\s}]+)')
                        matches = pos_pattern.finditer(parkpos_str)
                        
                        for match in matches:
                            pos, value = match.groups()
                            if pos in self.parkpos_entries:
                                self.parkpos_entries[pos].delete(0, tk.END)
                                self.parkpos_entries[pos].insert(0, value.strip("'"))
    
            # Extract parameters and create UI elements
            if self.extract_params_from_file():
                self.create_param_entries()
                
                # Call to update the graph with loaded parameters
                # self.parameter_graph.update_graph_with_loaded_params()  # Use the instance of ParameterGraph
                
                self.save_button.config(state=tk.NORMAL)  # Enable save button when file is loaded
                self.file_menu.entryconfig("Save", state='normal')  # Enable save menu item
                # self.parameter_graph.set_original_content(self.original_content) 
                self.update_preview()
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {str(e)}")

    def add_print_progress(self):
        self.add_frame("Add Print Progress", "Print Progress")
        
    def add_frame(self, title,frame_name):
        try:
            # Save current state before adding
            self.save_state()
            
            # Create dialog window
            dialog = tk.Toplevel(self.root)
            dialog.title(title)
            dialog.geometry("300x100")  # Increased height for header
            
            # Create header frame
            header_frame = tk.Frame(dialog)
            header_frame.pack(fill='x', padx=5, pady=5)
            
            # Create and pack entry widget
            value_var = tk.StringVar()
            entry = tk.Entry(dialog, textvariable=value_var)
            entry.pack(padx=5, pady=5)            
            # Focus the entry widget immediately
            entry.focus_set()

            # Bind the Enter key to add the parameter
            entry.bind('<Return>', lambda event: self.validate_and_add(value_var, frame_name, dialog))
            
            # Create a bound method for the button command
            cmd = lambda: self.validate_and_add(value_var, frame_name, dialog)
            
            # Add button
            tk.Button(dialog, text="Add", command=cmd).pack(pady=5)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add print progress: {str(e)}")
            
    def validate_and_add(self, value_var, frame_name, dialog):
        try:
            if frame_name == "Print Progress":
                percentage = int(value_var.get())
                if percentage < 0 or percentage > 100:
                    messagebox.showerror("Error", "Percentage must be between 0 and 100.")
                    return
                
                if percentage not in self.print_progress_params:
                    self.print_progress_params[percentage] = {}
                
                # Create a frame for the new print progress parameter
                self.create_print_progress_frame(percentage, frame_name, is_z_height=False)
                
            elif frame_name == "Z Height":
                z_height = float(value_var.get())
                max_z = self.get_max_z_value()
                if z_height < 0 or z_height > max_z:
                    messagebox.showerror("Error", f"Z height must be between 0 and {max_z}.")
                    return
                    
                if z_height not in self.custom_z_params:
                    self.custom_z_params[z_height] = {}
                
                # Create a frame for the new Z height parameter
                self.create_print_progress_frame(z_height, frame_name, is_z_height=True)
            
            # Update line numbers and preview
            self.update_line_numbers()
            self.update_preview()
            
            # Get current position in preview text
            current_pos = self.preview_text.index("end-1c")
            
            # Snap preview to the newly added line
            self.preview_text.see(current_pos)
            self.preview_text.tag_add("highlight", current_pos, f"{current_pos} lineend")
            
            # After adding progress/z-height, prompt for parameter
            is_z_height = (frame_name == "Z Height")
            value = float(value_var.get()) if is_z_height else int(value_var.get())
            self.add_param_to_progress(value, is_z_height, dialog)
            
        except ValueError as e:
            if frame_name == "Print Progress":
                messagebox.showerror("Error", "Please enter a valid integer")
            else:
                messagebox.showerror("Error", "Please enter a valid number")
     # Add button
            
    
   
        
    def add_z_height(self):
        self.add_frame("Add Z Height", "Z Height")
        
        # # After adding the Z height, update the graph
        # # Access z_points and other parameters from the ParameterGraph instance
        # self.parameter_graph.plot_parameters(
        #     self.parameter_graph.z_points, 
        #     self.parameter_graph.z_tool_points, 
        #     self.parameter_graph.z_feed_points, 
        #     self.parameter_graph.feed_points, 
        #     self.parameter_graph.z_cool_points, 
        #     self.parameter_graph.cool_points, 
        #     self.parameter_graph.z_act_drive_points, 
        #     self.parameter_graph.act_drive_points
        # )  # Ensure this is called after adding

    def get_max_z_value(self):
        """Extract the maximum Z value from the original content."""
        max_z = 0.0
        z_pattern = re.compile(r'LIN.*?Z\s(\d+\.\d+)')
        for line in self.original_content.splitlines():
            match = z_pattern.search(line)
            
            if match:
                z_value = float(match.group(1))
                
                if z_value > max_z:
                    max_z = z_value
        return max_z
    def find_nearby_z_value(self, lines, line_num):
        # Check 10 lines before and after the current line for Z values
        start = max(0, line_num - 10)
        end = min(len(lines), line_num + 11)  # +11 to include the line at line_num

        z_pattern = re.compile(r'LIN.*?Z\s*(-?\d+(\.\d+)?)')  # Updated regex pattern

        for i in range(start, end):
            z_match = z_pattern.search(lines[i])
            if z_match:
                return float(z_match.group(1))  # Return the matched Z value as a float

        # If no Z value found, determine default based on position
        if line_num < 1000:  # Near the beginning
            return 0
        elif line_num >= len(lines) - 1000:  # Near the end
            return 100
        return None  # Should not reach here
    def create_print_progress_frame(self, value, frame_name, is_z_height=False):
        try:
            # Create new frame with appropriate title
            title = f"{frame_name}: {value}"
            if frame_name == "Print Progress":
                title += "%"
                
            progress_frame = tk.LabelFrame(self.param_frame, text=title)
            progress_frame.pack(fill='x', padx=5, pady=2)
            
            # Store the frame in the correct dictionary
            if frame_name == "Print Progress":
                if value not in self.print_progress_frames:
                    self.print_progress_frames[value] = progress_frame
            else:  # Z Height
                if value not in self.z_param_frames:
                    self.z_param_frames[value] = progress_frame

            # Create button frame at the top
            button_frame = tk.Frame(progress_frame)
            button_frame.pack(fill='x', padx=2, pady=1)

            # Get line number for jump button
            content_lines = self.original_content.splitlines()
            line_number = None
            
            if is_z_height:
                z_pattern = re.compile(r'LIN.*?Z\s*([-\d.]+)')
                for i, line in enumerate(content_lines, 1):
                    match = z_pattern.search(line)
                    if match and abs(float(match.group(1)) - value) < 0.0001:
                        line_number = i
                        break
            else:
                search_text = f"PRINT_PROGRESS={value}"
                for i, line in enumerate(content_lines, 1):
                    if search_text in line:
                        line_number = i
                        break

            # Jump to line button
            if line_number:
                jump_btn = tk.Button(button_frame, text="→", 
                                   command=lambda ln=line_number: self.jump_to_line(ln),
                                   bg='light blue')
                jump_btn.pack(side='left', padx=2)

            # Remove button
            remove_btn = tk.Button(button_frame, text="✕",
                                 bg='#ffb3b3', fg='white',
                                 command=lambda v=value, z=is_z_height: self.remove_param(v, z))
            remove_btn.pack(side='left', padx=2)

            # Add parameter button
            add_btn = tk.Button(button_frame, text="+",
                              bg='LIGHT GREEN', fg='white',
                              command=lambda v=value, z=is_z_height: self.add_param_to_progress(v, z))
            add_btn.pack(side='left', padx=2)

            # Add Parameter button at bottom
            add_param_btn = tk.Button(progress_frame, text="Add Parameter", 
                                    command=lambda: self.add_param_to_progress(value, is_z_height))
            add_param_btn.pack(side='bottom', pady=5)

            return progress_frame

        except Exception as e:
            messagebox.showerror("Error", f"Failed to create frame: {str(e)}")

    def add_param_to_progress(self, value, is_z_height=False, parent_dialog=None):
        try:
            # Create parameter selection dialog
            dialog = tk.Toplevel(self.root)
            dialog.title("Add Parameter") 
            dialog.geometry("300x200")
            dialog.transient(self.root)  # Make dialog modal
            dialog.grab_set()  # Make dialog modal
            
            # Parameter dropdown
            param_frame = ttk.LabelFrame(dialog, text="Select Parameter")
            param_frame.pack(fill='x', padx=5, pady=5)
            
            param_var = tk.StringVar(value='TOOL_RPM')
            param_dropdown = ttk.Combobox(param_frame, textvariable=param_var, 
                                        values=['TOOL_RPM', '$VEL.CP', 'LAYER_COOLING', 'ACT_DRIVE'])
            param_dropdown.pack(padx=5, pady=5)
            
            # Value entry frame
            value_frame = ttk.LabelFrame(dialog, text="Enter Value") 
            value_frame.pack(fill='x', padx=5, pady=5)
            
            # Value entry
            value_var = tk.StringVar()
            value_entry = ttk.Entry(value_frame, textvariable=value_var)
            value_entry.pack(padx=5, pady=5)
            value_entry.focus_set()

            def on_param_select(*args):
                if param_var.get() == 'ACT_DRIVE':
                    value_entry.pack_forget()
                    act_drive_combo = ttk.Combobox(value_frame, textvariable=value_var, 
                                                 values=['TRUE', 'FALSE'], state='readonly')
                    act_drive_combo.pack(padx=5, pady=5)
                    act_drive_combo.set('TRUE')  # Default value
                else:
                    for widget in value_frame.winfo_children():
                        widget.destroy()
                    value_entry = ttk.Entry(value_frame, textvariable=value_var)
                    value_entry.pack(padx=5, pady=5)
                    value_entry.focus_set()

            param_var.trace('w', on_param_select)

            def add_parameter():
                param_name = param_var.get()
                param_value = value_var.get()
                
                if not param_value:
                    messagebox.showerror("Error", "Please enter a value")
                    return
                    
                # Save current state
                self.save_state()
                
                try:
                    # Validate parameter values
                    if param_name == 'TOOL_RPM':
                        param_value = float(param_value)
                        if param_value > 139.8:
                            messagebox.showerror("Error", "Maximum value for TOOL_RPM is 139.8")
                            return
                    elif param_name == '$VEL.CP':
                        param_value = float(param_value)
                        if param_value > 2:
                            messagebox.showerror("Error", "Maximum value for $VEL.CP is 2")
                            return
                        if param_value > 0.5:
                            if not messagebox.askyesno("Warning", 
                                "Values above 0.5 for $VEL.CP could be dangerous.\n\n" +
                                "Do you wish to continue with this value?"):
                                return
                    elif param_name == 'LAYER_COOLING':
                        param_value = int(param_value)
                        if param_value > 200:
                            messagebox.showerror("Error", "Maximum value for LAYER_COOLING is 200")
                            return
                    elif param_name == 'ACT_DRIVE':
                        if param_value.upper() not in ['TRUE', 'FALSE']:
                            messagebox.showerror("Error", "ACT_DRIVE value must be TRUE or FALSE")
                            return
                        param_value = param_value.upper()
                except ValueError:
                    messagebox.showerror("Error", "Please enter a valid number")
                    return

                # Find the line with print progress
                content_lines = self.original_content.splitlines()
                target_line = None
                
                progress_pattern = f"PRINT_PROGRESS={int(value)}"
                for i, line in enumerate(content_lines):
                    if progress_pattern in line:
                        target_line = i
                        break

                if target_line is not None:
                    # Format parameter line
                    if param_name == 'TOOL_RPM':
                        param_line = f"TRIGGER WHEN DISTANCE=0 DELAY=0 DO TOOL_RPM={param_value}"
                    elif param_name == 'ACT_DRIVE':
                        param_line = f"ACT_DRIVE={param_value}"
                    else:
                        param_line = f"{param_name}={param_value}"

                    # Insert parameter
                    content_lines.insert(target_line + 1, param_line)
                    self.original_content = '\n'.join(content_lines) + '\n'

                    # Update UI
                    self.update_preview()
                    self.jump_to_line(target_line + 2)  # +2 because we added a line and line numbers start at 1
                    
                    # Store parameter
                    if value not in self.print_progress_params:
                        self.print_progress_params[value] = {}
                    self.print_progress_params[value][param_name] = param_value

                    # Refresh the parameter frame
                    self.refresh_progress_params(value)
                    
                    # Enable save button
                    self.save_button.config(state=tk.NORMAL)
                    
                    # Close dialogs
                    dialog.destroy()
                    if parent_dialog:
                        parent_dialog.destroy()

            # Add button
            add_button = ttk.Button(dialog, text="Add", command=add_parameter, style='Accent.TButton')
            add_button.pack(pady=5)

            # Bind Enter key
            dialog.bind('<Return>', lambda e: add_parameter())

        except Exception as e:
            messagebox.showerror("Error", f"Failed to add parameter: {str(e)}")
            if dialog:
                dialog.destroy()

    def refresh_progress_params(self, value, is_z_height=False):
        try:
            # Get the correct frame and parameters dictionary based on type
            if is_z_height:
                frame = self.z_param_frames.get(value)
                params_dict = self.custom_z_params.get(value, {})
            else:
                frame = self.print_progress_frames.get(value)
                params_dict = self.print_progress_params.get(value, {})
                
            if frame is None:
                return  # Skip if frame doesn't exist yet
                
            # Clear existing parameter widgets
            for widget in frame.winfo_children():
                widget.destroy()
            
            # Create button frame at the top
            button_frame = tk.Frame(frame)
            button_frame.pack(fill='x', padx=2, pady=1)

            # Get the line number for the jump button
            content_lines = self.original_content.splitlines()
            line_number = None
            
            if is_z_height:
                z_pattern = re.compile(r'LIN.*?Z\s*([-\d.]+)')
                for i, line in enumerate(content_lines, 1):
                    match = z_pattern.search(line)
                    if match and abs(float(match.group(1)) - value) < 0.0001:
                        line_number = i
                        break
            else:
                search_text = f"PRINT_PROGRESS={value}"
                for i, line in enumerate(content_lines, 1):
                    if search_text in line:
                        line_number = i
                        break

            # Jump to line button
            if line_number:
                jump_btn = tk.Button(button_frame, text="→", 
                                   command=lambda ln=line_number: self.jump_to_line(ln),
                                   bg='light blue')
                jump_btn.pack(side='left', padx=2)

            # Add parameter button
            add_btn = tk.Button(button_frame, text="+",
                              bg='LIGHT GREEN', fg='white', 
                              command=lambda v=value, z=is_z_height: self.add_param_to_progress(v, z))
            add_btn.pack(side='left', padx=2)
            
            # Add parameter entries
            for param_name, param_value in params_dict.items():
                param_frame = tk.Frame(frame)
                param_frame.pack(fill='x', padx=2, pady=1)
                
                tk.Label(param_frame, text=param_name).pack(side='left')
                
                # Create entry for value that updates in real-time
                value_var = tk.StringVar(value=str(param_value))
                if param_name == 'ACT_DRIVE':
                    # For ACT_DRIVE, use a readonly Entry instead of Combobox
                    entry = tk.Entry(param_frame, textvariable=value_var, width=10, state='readonly')
                else:
                    entry = tk.Entry(param_frame, textvariable=value_var, width=10)
                entry.pack(side='right')

                # Add jump button for this parameter
                if param_name in self.param_line_numbers:
                    jump_btn = tk.Button(param_frame, text="→", 
                                       command=lambda ln=self.param_line_numbers[param_name]: self.jump_to_line(ln),
                                       bg='light blue')
                    jump_btn.pack(side='right', padx=2)

                # Add remove button for this parameter
                remove_btn = tk.Button(param_frame, text="✕", 
                                     command=lambda p=param_name, v=value: self.remove_param(p, v, is_z_height),
                                     bg='#ffb3b3', fg='white')
                remove_btn.pack(side='right', padx=2)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to refresh parameters: {str(e)}")

    def remove_param(self, param_name, value, is_z_height=False):
        try:
            # Save current state before deletion
            self.save_state()
            
            # Remove parameter from dictionary
            if is_z_height:
                if value in self.custom_z_params and param_name in self.custom_z_params[value]:
                    del self.custom_z_params[value][param_name]
                    # Keep frame even if empty
                    if value in self.z_param_frames:
                        self.refresh_progress_params(value, is_z_height=True)
            else:
                if value in self.print_progress_params and param_name in self.print_progress_params[value]:
                    del self.print_progress_params[value][param_name]
                    # Keep frame even if empty
                    if value in self.print_progress_frames:
                        self.refresh_progress_params(value, is_z_height=False)

            # Remove from content while preserving PRINT_PROGRESS line
            content_lines = self.original_content.splitlines()
            new_content_lines = []
            skip_next = False
            
            for i, line in enumerate(content_lines):
                if skip_next:
                    skip_next = False
                    continue
                    
                if is_z_height:
                    z_pattern = re.compile(r'LIN.*?Z\s*([-\d.]+)')
                    match = z_pattern.search(line)
                    if match and abs(float(match.group(1)) - value) < 0.0001:
                        new_content_lines.append(line)
                        # Skip only the specific parameter line
                        if i + 1 < len(content_lines) and f"{param_name}=" in content_lines[i + 1]:
                            skip_next = True
                        continue
                else:
                    if f"PRINT_PROGRESS={int(value)}" in line:
                        new_content_lines.append(line)  # Keep PRINT_PROGRESS line
                        # Skip only the specific parameter line
                        if i + 1 < len(content_lines) and f"{param_name}=" in content_lines[i + 1]:
                            skip_next = True
                        continue
                
                # Check for $VEL.CP parameter
                if f"$VEL.CP=" in line and param_name == "$VEL.CP":
                    skip_next = True
                    continue
                
                new_content_lines.append(line)

            # Update original content
            self.original_content = '\n'.join(new_content_lines) + '\n'
            
            # Update preview
            self.update_preview()
            
            # Enable save button
            
            self.save_button.config(state=tk.NORMAL)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to remove parameter: {str(e)}")

    def jump_to_line(self, line_number):
        try:
            if line_number is None:
                messagebox.showerror("Error", "Invalid line number. Cannot jump.")
                return
            
            print(f"Jumping to line: {line_number}")  # Debugging line
            self.preview_text.see(f"{line_number}.0")
            self.preview_text.tag_remove("highlight", "1.0", "end")
            self.preview_text.tag_configure("highlight", background="yellow")
            self.preview_text.tag_add("highlight", f"{line_number}.0", f"{line_number}.end")
            
            # Update line numbers to ensure they're in sync
            self.update_line_numbers()
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to jump to line: {str(e)}")

    def accept_param_change(self, percentage, param_name, value_var):
        try:
            if param_name == 'ACT_DRIVE':
                value = value_var.get().upper()
                if value not in ['TRUE', 'FALSE']:
                    messagebox.showerror("Error", "ACT_DRIVE can only be TRUE or FALSE")
                    return
            elif param_name == 'TOOL_RPM':  # Handle TOOL_RPM as int
                value = int(value_var.get())
            elif param_name == 'LAYER_COOLING':  # Handle LAYER_COOLING as int
                value = int(value_var.get())
            else:
                value = float(value_var.get())
                
            self.custom_z_params[percentage][param_name] = value
            
            # Find the line containing Z_HEIGHT=percentage and update the parameter
            content = self.preview_text.get("1.0", tk.END).splitlines()
            param_updated = False
            
            for i, line in enumerate(content):
                if f"Z_HEIGHT={percentage}" in line:
                    # Find and update parameter line after Z_HEIGHT
                    for j in range(i+1, len(content)):
                        if param_name == 'LAYER_COOLING':
                            if 'LAYER_COOLING=' in content[j]:
                                # Keep any text before LAYER_COOLING
                                prefix = content[j].split('LAYER_COOLING=')[0]
                                content[j] = f"{prefix}LAYER_COOLING={value}"
                                param_updated = True
                                break
                        else:
                            if f"{param_name}=" in content[j]:
                                content[j] = f"{param_name}={value}"
                                param_updated = True
                                break
                    break
            
            if not param_updated:
                messagebox.showerror("Error", "Parameter not found in the correct position")
                return
                
            # Update preview
            self.preview_text.delete("1.0", tk.END)
            self.preview_text.insert("1.0", "\n".join(content))
            
            # Highlight modified line and jump to it
            self.preview_text.see(f"{j+1}.0")
            self.preview_text.tag_remove("highlight", "1.0", "end")
            self.preview_text.tag_configure("highlight", background="yellow")
            self.preview_text.tag_add("highlight", f"{j+1}.0", f"{j+1}.end")
            
            # Enable save button when parameter is changed
            
            self.save_button.config(state=tk.NORMAL)
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

    def extract_params_from_file(self):
        if not self.original_content:
            return
            
        try:
            # Clear existing params
            self.params.clear()
            self.param_line_numbers.clear()
            self.param_groups.clear()
            self.trigger_params.clear()
            
            # Split content into lines
            lines = self.original_content.splitlines()            
            # Extract all parameters with line numbers
            for line_num, line in enumerate(lines, 1):
                # Look for TOOL_RPM first
                if 'TOOL_RPM' in line:
                    value = int(re.search(r'TOOL_RPM\s*=\s*(-?\d+)', line).group(1))  # Changed to int
                    key = f"Tool Speed (TOOL_RPM) (Line {line_num})"
                    self.params[key] = value
                    self.param_line_numbers[key] = line_num
                    
                    # Group parameters
                    if 'Tool Speed (TOOL_RPM)' not in self.param_groups:
                        self.param_groups['Tool Speed (TOOL_RPM)'] = []
                    self.param_groups['Tool Speed (TOOL_RPM)'].append(key)
                    
                # Look for trigger parameters next
                trigger_match = re.search(r'TRIGGER WHEN DISTANCE=(\d+\.?\d*)\s*DELAY=(\d+\.?\d*)\s*DO\s+ACT_DRIVE=(TRUE|FALSE)', line)
                if trigger_match:
                    distance = float(trigger_match.group(1))
                    delay = float(trigger_match.group(2))
                    act_drive_value = 'TRUE' if trigger_match.group(3) == 'TRUE' else 'FALSE'
                    
                    # Add ACT_DRIVE to params while preserving trigger
                    key = f"Drive (ACT_DRIVE) (Line {line_num})"
                    self.params[key] = act_drive_value
                    self.param_line_numbers[key] = line_num
                    
                    if 'Drive (ACT_DRIVE)' not in self.param_groups:
                        self.param_groups['Drive (ACT_DRIVE)'] = []
                    self.param_groups['Drive (ACT_DRIVE)'].append(key)
                    
                    self.trigger_params[line_num] = {
                        'distance': distance,
                        'delay': delay,
                        'do': 'ACT_DRIVE',
                        'value': act_drive_value
                    }
                    continue
                
                # Look for other parameters
                if '$VEL.CP' in line:
                    value = float(re.search(r'\$VEL\.CP\s*=\s*(-?\d+\.?\d*)', line).group(1))
                    key = f"Feed Rate ($VEL.CP) (Line {line_num})"
                    self.params[key] = value
                    self.param_line_numbers[key] = line_num
                    
                    if 'Feed Rate ($VEL.CP)' not in self.param_groups:
                        self.param_groups['Feed Rate ($VEL.CP)'] = []
                    self.param_groups['Feed Rate ($VEL.CP)'].append(key)
                    
                elif 'LAYER_COOLING' in line:
                    # Extract everything before LAYER_COOLING
                    prefix = line.split('LAYER_COOLING')[0]
                    value = int(re.search(r'LAYER_COOLING\s*=\s*(-?\d+)', line).group(1))  # Changed to int
                    key = f"Cooling (LAYER_COOLING) (Line {line_num})"
                    self.params[key] = value
                    self.param_line_numbers[key] = line_num
                    
                    # Store the prefix if it exists
                    if prefix:
                        self.params[f"{key}_prefix"] = prefix
                    
                    if 'Cooling (LAYER_COOLING)' not in self.param_groups:
                        self.param_groups['Cooling (LAYER_COOLING)'] = []
                    self.param_groups['Cooling (LAYER_COOLING)'].append(key)
                    
                elif 'ACT_DRIVE' in line:
                    value = 'TRUE' if re.search(r'ACT_DRIVE\s*=\s*(TRUE|FALSE)', line).group(1) == 'TRUE' else 'FALSE'
                    key = f"Drive (ACT_DRIVE) (Line {line_num})"
                    self.params[key] = value
                    self.param_line_numbers[key] = line_num
                    
                    if 'Drive (ACT_DRIVE)' not in self.param_groups:
                        self.param_groups['Drive (ACT_DRIVE)'] = []
                    self.param_groups['Drive (ACT_DRIVE)'].append(key)
                    
            return True
        except Exception as e:
            messagebox.showerror("Error", f"Failed to extract parameters: {str(e)}")
            return False


    def create_ui(self):
        try:
            # Main container
            main_container = tk.PanedWindow(self.root, orient=tk.HORIZONTAL)
            main_container.pack(fill=tk.BOTH, expand=True)

            # Left frame setup with fixed width - use Card style from Forest theme
            left_frame = ttk.Frame(main_container, width=500, style='Card')
            left_frame.pack_propagate(False)
            main_container.add(left_frame)

            # Create notebook (tabbed interface)
            notebook = ttk.Notebook(left_frame)
            notebook.pack(fill='both', expand=True, padx=5, pady=5)

            # Create Parameters tab
            params_tab = ttk.Frame(notebook)
            notebook.add(params_tab, text='Parameters')

            # # Create Graph tab
            # graph_tab = ttk.Frame(notebook)
            # notebook.add(graph_tab, text='Graph')

            # Add content to Parameters tab
            # Create a frame for the add buttons with Card style
            add_buttons_frame = ttk.LabelFrame(params_tab, text="Add Parameters", padding=(5, 5, 5, 5))
            add_buttons_frame.pack(fill='x', padx=5, pady=5)

            # Add print progress button with Accent style from Forest theme
            add_print_progress_btn = ttk.Button(
                add_buttons_frame, 
                text="Add Print Progress Parameter",
                command=self.add_print_progress,
                style='Accent.TButton'
            )
            add_print_progress_btn.pack(fill='x', pady=(0, 2))

            # Add Z height button with Accent style
            add_z_height_btn = ttk.Button(
                add_buttons_frame, 
                text="Add Z Height Parameter",
                command=self.add_parameter_at_z,
                style='Accent.TButton'
            )
            add_z_height_btn.pack(fill='x')
            # Add ACT_DRIVE Parameter button
            add_act_drive_btn = ttk.Button(
                add_buttons_frame, 
                text="Add Parameter at Part Start",
                command=self.add_parameter_at_start,
                style='Accent.TButton'
            )
            add_act_drive_btn.pack(fill='x', pady=(2, 5))

            # Create scrollable frame for parameters
            param_canvas = tk.Canvas(params_tab)
            scrollbar = tk.Scrollbar(params_tab, orient="vertical", command=param_canvas.yview)
            self.param_frame = tk.Frame(param_canvas)
            
            # Bind mouse wheel to scroll
            def _on_mousewheel(event):
                param_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
            param_canvas.bind_all("<MouseWheel>", _on_mousewheel)
                    
            # Configure scrolling
            self.param_frame.bind(
                "<Configure>",
                lambda e: param_canvas.configure(scrollregion=param_canvas.bbox("all"))
            )
            param_canvas.create_window((0, 0), window=self.param_frame, anchor="nw")
            param_canvas.configure(yscrollcommand=scrollbar.set)
            
            # Pack scrollable frame
            param_canvas.pack(side="left", fill="both", expand=True, pady=10)
            scrollbar.pack(side="right", fill="y")

            # # Add content to Graph tab
            # # Create graph frame
            # graph_frame = ttk.LabelFrame(graph_tab, text="Parameter Graph", padding=(5, 5, 5, 5))
            # graph_frame.pack(fill='both', expand=True, padx=5, pady=5)
            
            # # Initialize the parameter graph
            # self.parameter_graph = ParameterGraph(graph_frame, self.original_content)
            # self.update_preview()  # Call to update the graph with initial parameters

            # Create custom button style
            style = ttk.Style()
            style.configure('Action.TButton', 
                           padding=5,
                           font=('Arial', 9))

            # Right paned window for preview with fixed width
            preview_frame = tk.Frame(main_container, width=800)
            preview_frame.pack_propagate(False)  # Prevent frame from shrinking
            main_container.add(preview_frame)

            # Create search frame
            search_frame = tk.Frame(preview_frame)
            search_frame.pack(fill='x', padx=5, pady=5)

            # Search entry and buttons
            self.search_var = tk.StringVar()
            search_entry = tk.Entry(search_frame, textvariable=self.search_var)
            search_entry.pack(side='left', fill='x', expand=True)
            
            # Track current search position and last search term
            self.current_search_pos = "1.0"
            self.last_search_term = ""
            
            def find_text(event=None):
                search_term = self.search_var.get()
                if not search_term:
                    return
                    
                # If new search term, reset position
                if search_term != self.last_search_term:
                    self.current_search_pos = "1.0"
                    self.preview_text.tag_remove("search_highlight", "1.0", "end")
                    self.last_search_term = search_term
                
                # Find next occurrence starting from current position
                pos = self.preview_text.search(search_term, self.current_search_pos, stopindex="end", nocase=True)
                
                if pos:
                    # Calculate end position of match
                    end_pos = f"{pos}+{len(search_term)}c"
                    # Highlight the found text with yellow background and black text
                    self.preview_text.tag_add("search_highlight", pos, end_pos)
                    self.preview_text.tag_configure("search_highlight", background="yellow", foreground="black")
                    # See and select the found text
                    self.preview_text.see(pos)
                    self.preview_text.mark_set("insert", pos)
                    self.preview_text.focus_set()
                    # Update position for next search
                    self.current_search_pos = end_pos
                else:
                    # If no match found, show message and reset position
                    messagebox.showinfo("Find", "No more matches found")
                    self.current_search_pos = "1.0"
                
                # Keep focus on the search entry
                search_entry.focus_set()
            
            find_button = tk.Button(search_frame, text="Find", command=find_text)
            find_button.pack(side='right', padx=10)
            
            # Bind the Enter key to the find_text function
            search_entry.bind('<Return>', find_text)
            
            # Create text widget with line numbers
            self.preview_text = Text(preview_frame, wrap="none")
            y_scrollbar = Scrollbar(preview_frame, orient='vertical', command=self.preview_text.yview)
            x_scrollbar = Scrollbar(preview_frame, orient='horizontal', command=self.preview_text.xview)
            
            # Line numbers text widget
            self.line_numbers = Text(preview_frame, width=4, padx=3, takefocus=0, border=0,
                                background='lightgray', state='disabled')
            self.line_numbers.pack(side='left', fill='y')
            
            # Configure text widget
            self.preview_text.pack(side='left', fill='both', expand=True)
            y_scrollbar.pack(side='right', fill='y')
            x_scrollbar.pack(side='bottom', fill='x')
            self.preview_text.configure(yscrollcommand=y_scrollbar.set)
            self.preview_text.configure(xscrollcommand=x_scrollbar.set)
            
            # Bind scrolling events
            self.preview_text.bind('<Key>', lambda e: self.update_line_numbers())
            self.preview_text.bind('<MouseWheel>', lambda e: self.update_line_numbers())
        
            # Configure text tags for parameter highlighting
            self.preview_text.tag_configure("tool_speed", background=self.param_colors['TOOL_RPM'])
            self.preview_text.tag_configure("feed_rate", background=self.param_colors['$VEL.CP'])
            self.preview_text.tag_configure("cooling", background=self.param_colors['LAYER_COOLING']);
            self.preview_text.tag_configure("drive", background=self.param_colors['ACT_DRIVE']);
            self.preview_text.tag_configure("search_highlight", background="yellow");

            # Configure header colors to match parameters
            for header_label in self.header_labels.values():
                param_type = header_label.cget("text").split(" (")[0][2:]  # Remove arrow and get param type
                if "Tool Speed" in param_type:
                    header_label.configure(bg=self.param_colors['TOOL_RPM'])
                elif "Feed Rate" in param_type:
                    header_label.configure(bg=self.param_colors['$VEL.CP'])
                elif "Cooling" in param_type:
                    header_label.configure(bg=self.param_colors['LAYER_COOLING'])
                elif "Drive" in param_type:
                    header_label.configure(bg=self.param_colors['ACT_DRIVE'])
                    
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create UI: {str(e)}")

    def create_param_entries(self):
        try:
            # Store current frame states before clearing
            expanded_sections = {}
            for param_type, content_frame in self.content_frames.items():
                if content_frame.winfo_viewable():
                    expanded_sections[param_type] = True

            # Clear existing entries
            for widget in self.param_frame.winfo_children():
                widget.destroy()
            self.entries.clear()
            self.content_frames.clear()
            self.header_labels.clear()

            if not self.params:
                return
            
            # Create parent header frame
            parent_header_frame = tk.Frame(self.param_frame, relief=tk.RAISED, borderwidth=1)
            parent_header_frame.pack(fill='x')
            
            # Create buttons frame for parent header
            parent_buttons_frame = tk.Frame(parent_header_frame)
            parent_buttons_frame.pack(fill='x', padx=5, pady=2)
            
            # Parent arrow button
            parent_arrow = tk.Label(parent_buttons_frame, text="▶", cursor="hand2", 
                                  font=("Arial", 8, "bold"), width=2,
                                  anchor='w')
            parent_arrow.pack(side='left')
            
            # Parent header label
            parent_label = tk.Label(parent_buttons_frame, text="Initial parameters",
                                  font=("Arial", 8, "bold"), 
                                  anchor='w')
            parent_label.pack(side='left', fill='x', expand=True)
            
            # Create parent content frame
            parent_content_frame = tk.Frame(self.param_frame)
            # Don't pack initially to start closed
            
            def toggle_parent(event=None):
                if parent_content_frame.winfo_viewable():
                    parent_content_frame.pack_forget()
                    parent_arrow.config(text="▶")
                else:
                    parent_content_frame.pack(fill='x')
                    parent_arrow.config(text="▼")
            
            parent_arrow.bind('<Button-1>', toggle_parent)
            parent_label.bind('<Button-1>', toggle_parent)

            for param_type, param_keys in self.param_groups.items():
                # Container frame for parameter type
                container = tk.Frame(parent_content_frame)
                container.pack(fill='x', padx=5, pady=2)
                
                # Header frame
                header_frame = tk.Frame(container, relief=tk.RAISED, borderwidth=1)
                header_frame.pack(fill='x')
                
                # Buttons frame
                buttons_frame = tk.Frame(header_frame)
                buttons_frame.pack(fill='x', padx=5, pady=2)
                
                # Arrow button
                arrow_btn = tk.Label(buttons_frame, text="▶", cursor="hand2",
                                   font=("Arial", 10, "bold"),
                                   width=2,
                                   anchor='w')
                arrow_btn.pack(side='left')
                
                # Header label
                header_label = tk.Label(buttons_frame, 
                                      text=f"{param_type} ({len(param_keys)} occurrences)",
                                      font=("Arial", 10, "bold"),
                                      anchor='w')
                header_label.pack(side='left', fill='x', expand=True)
                self.header_labels[param_type] = header_label
                
                # Content frame
                content_frame = tk.Frame(container)
                content_frame.pack(fill='x')
                self.content_frames[param_type] = content_frame
                
                def make_toggle_function(content_frame, arrow_btn, header_label, param_type):
                    def toggle(event=None):
                        if content_frame.winfo_viewable():
                            content_frame.pack_forget()
                            arrow_btn.config(text="▶")
                        else:
                            content_frame.pack(fill='x', padx=20)
                            arrow_btn.config(text="▼")
                    return toggle
                
                toggle_func = make_toggle_function(content_frame, arrow_btn, header_label, param_type)
                arrow_btn.bind('<Button-1>', toggle_func)
                header_label.bind('<Button-1>', toggle_func)
                
                # Create entries for parameters
                for param_key in param_keys:
                    row = tk.Frame(content_frame)
                    row.pack(fill='x', padx=5, pady=2)
                    
                    # Extract just the variable name and line number
                    param_parts = param_key.split(' (')
                    var_name = param_parts[1].split(')')[0]  # Gets the variable name (e.g., $VEL.CP)
                    line_num = param_parts[-1].split(')')[0]  # Gets the line number
                    simplified_label = f"{var_name} ({line_num})"
                    
                    tk.Label(row, text=simplified_label).pack(side='left')
                    
                    value_var = tk.StringVar(value=str(self.params[param_key]))
                    if "Drive" in param_key:
                        entry = ttk.Combobox(row, textvariable=value_var, values=['TRUE', 'FALSE'],
                                            width=7)
                    else:
                        entry = tk.Entry(row, width=10, textvariable=value_var)
                    entry.pack(side='right')
                    
                    self.entries[param_key] = entry
                    
                    # Accept button
                    accept_btn = tk.Button(row, text="✓", bg='LIGHT GREEN', fg='white',
                                         command=lambda k=param_key, v=value_var, ln=self.param_line_numbers[param_key]:
                                         self.update_line_and_preview(k, v, ln))
                    accept_btn.pack(side='right', padx=2)
                    
                    # Delete button
                    delete_btn = tk.Button(row, text="✕", bg='#ffb3b3', fg='white',
                                         command=lambda k=param_key, ln=self.param_line_numbers[param_key]:
                                         self.delete_parameter(k, ln))
                    delete_btn.pack(side='right', padx=2)
                    
                    # Jump button
                    if param_key in self.param_line_numbers:
                        jump_btn = tk.Button(row, text="→",
                                           command=lambda ln=self.param_line_numbers[param_key]: self.jump_to_line(ln),
                                           bg='light blue')
                        jump_btn.pack(side='right', padx=5)
                    
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create parameter entries: {str(e)}")

    def update_line_and_preview(self, key, value_var, line_number):
        try:
            # Save current state before update
            self.save_state()
            
            # Validate and get the value based on parameter type
            if "Feed Rate" in key:  # For $VEL.CP
                value = float(value_var.get())
                if value > 2:
                    messagebox.showerror("Error", "Maximum value for $VEL.CP is 2")
                    return
                if value > 0.5:
                    if not messagebox.askyesno("Warning", 
                        "Values above 0.5 for $VEL.CP could be dangerous.\n\n" +
                        "Do you wish to continue with this value?"):
                        return
            elif "Tool Speed" in key:  # For TOOL_RPM
                value = float(value_var.get())
                if value > 139.8:
                    messagebox.showerror("Error", "Maximum value for TOOL_RPM is 139.8")
                    return
            elif "Cooling" in key:  # For LAYER_COOLING
                value = int(value_var.get())
                if value > 200:
                    messagebox.showerror("Error", "Maximum value for LAYER_COOLING is 200")
                    return
            else:  # For other parameters
                value = value_var.get()
            
            self.params[key] = value
            
            # Get the parameter type from the key
            param_type = key.split(' (')[0]
            
            # Update the specific line in the original content
            content = self.original_content.splitlines()
            line_idx = line_number - 1
            
            if "Tool Speed" in param_type:
                # Check if line contains "TRIGGER WHEN" string
                if "TRIGGER WHEN" in content[line_idx]:
                    aux = re.match("^(.+?)TOOL_RPM=\\d*\\.?\\d*", content[line_idx]).group(1)
                    content[line_idx] = f"{aux}TRIGGER WHEN DISTANCE=0 DELAY=0 DO TOOL_RPM={value}"
                else:
                    content[line_idx] = f"TRIGGER WHEN DISTANCE=0 DELAY=0 DO TOOL_RPM={value}"
                
            elif "Feed Rate" in param_type:
                content[line_idx] = f"$VEL.CP={value}"
            elif "Cooling" in param_type:
                # Check if line contains "TRIGGER WHEN" string
                if "TRIGGER WHEN" in content[line_idx]:
                    aux = re.match("^(.+?)LAYER_COOLING=\\d*\\.?\\d*", content[line_idx]).group(1)
                    content[line_idx] = f"{aux}LAYER_COOLING={value}"
                else:
                    content[line_idx] = f"LAYER_COOLING={value}"
            elif "Drive" in param_type:
                # Check if line contains "TRIGGER WHEN" string
                if "TRIGGER WHEN" in content[line_idx]:
                    aux = re.match("^(.+?)ACT_DRIVE=\\d*\\.?\\d*", content[line_idx]).group(1)
                    content[line_idx] = f"{aux}ACT_DRIVE={value}"
                else:
                    content[line_idx] = f"ACT_DRIVE={value}"
                
            # Update original content
            self.original_content = "\n".join(content) + "\n"
            
            # Update preview using update_preview to maintain highlighting
            self.update_preview()
            
            # Highlight the modified line and jump to it
            self.preview_text.see(f"{line_number}.0")
            self.preview_text.tag_add("highlight", f"{line_number}.0", f"{line_number}.end")
            
            # Enable save button when line is updated
            self.save_button.config(state=tk.NORMAL)
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

    def update_line_numbers(self):
        try:
            if not self.preview_text:
                return
                
            self.line_numbers.config(state='normal')
            self.line_numbers.delete('1.0', tk.END)
            
            # Get visible lines
            first_line = int(self.preview_text.index("@0,0").split('.')[0])
            last_line = int(self.preview_text.index("@0,%d" % self.preview_text.winfo_height()).split('.')[0])
            
            # Add line numbers for visible lines
            for line_num in range(first_line, last_line + 1):
                self.line_numbers.insert(tk.END, f"{line_num}\n")
                
            self.line_numbers.config(state='disabled')
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update line numbers: {str(e)}")

    def update_preview(self):
        try:
            if not self.preview_text or not self.original_content:
                return
                
            self.preview_text.delete(1.0, tk.END)
            modified_lines = self.calculate_new_params()
            
            z_tool_points = []
            z_feed_points = []
            z_cool_points = []
            z_act_drive_points = []
            
            tool_points = []
            feed_points = []
            cool_points = []
            act_drive_points = []
            
            for i, line in enumerate(modified_lines):
                # Check for TOOL_RPM
                if 'TOOL_RPM=' in line:
                    tool_match = re.search(r'TOOL_RPM=(\d+\.?\d*)', line)
                    if tool_match:
                        tool_value = float(tool_match.group(1))
                        z_value = self.find_nearby_z_value(modified_lines, i)
                        z_tool_points.append(z_value if z_value is not None else 0)  # Default Z value if none found
                        tool_points.append(tool_value)
                        print(f"Parameter: TOOL_RPM, Z Value: {z_value}, Tool Value: {tool_value}")

                # Check for $VEL.CP
                elif '$VEL.CP=' in line:
                    feed_match = re.search(r'\$VEL\.CP=(\d+\.?\d*)', line)
                    if feed_match:
                        feed_value = float(feed_match.group(1))
                        z_value = self.find_nearby_z_value(modified_lines, i)
                        z_feed_points.append(z_value if z_value is not None else 0)  # Default Z value if none found
                        feed_points.append(feed_value)
                        print(f"Parameter: $VEL.CP, Z Value: {z_value}, Feed Value: {feed_value}")

                # Check for LAYER_COOLING
                elif 'LAYER_COOLING=' in line:
                    cool_match = re.search(r'LAYER_COOLING=(\d+)', line)
                    if cool_match:
                        cool_value = float(cool_match.group(1))
                        z_value = self.find_nearby_z_value(modified_lines, i)
                        z_cool_points.append(z_value if z_value is not None else 0)  # Default Z value if none found
                        cool_points.append(cool_value)
                        print(f"Parameter: LAYER_COOLING, Z Value: {z_value}, Cool Value: {cool_value}")

                # Check for ACT_DRIVE
                elif 'ACT_DRIVE=' in line:
                    act_drive_match = re.search(r'ACT_DRIVE\s*=\s*(TRUE|FALSE)', line)
                    if act_drive_match:
                        act_drive_value = 1.0 if act_drive_match.group(1) == 'TRUE' else 0.0
                        z_value = self.find_nearby_z_value(modified_lines, i)
                        z_act_drive_points.append(z_value if z_value is not None else 0)  # Default Z value if none found
                        act_drive_points.append(act_drive_value)
                        print(f"Parameter: ACT_DRIVE, Z Value: {z_value}, Act Drive Value: {act_drive_value}")

            # # Update graph if we have data
            # if z_tool_points or z_feed_points or z_cool_points or z_act_drive_points:
            #     # self.parameter_graph.plot_parameters(
            #         z_tool_points, tool_points, 
            #         z_feed_points, feed_points, 
            #         z_cool_points, cool_points, 
            #         z_act_drive_points, act_drive_points
        
        
            # Update text preview
            for line in modified_lines:
                if 'TOOL_RPM=' in line:
                    self.preview_text.insert(tk.END, line, "tool_speed")
                elif '$VEL.CP=' in line:
                    self.preview_text.insert(tk.END, line, "feed_rate")
                elif 'LAYER_COOLING=' in line:
                    self.preview_text.insert(tk.END, line, "cooling")
                elif 'ACT_DRIVE=' in line:
                    self.preview_text.insert(tk.END, line, "drive")
                else:
                    self.preview_text.insert(tk.END, line)
        
            self.update_line_numbers()
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update preview: {str(e)}")

    def calculate_new_params(self):
        try:
            if not self.original_content:
                return []
                
            lines = self.original_content.splitlines(True)
            modified_lines = []
            
            # Compile regex patterns
            z_pattern = re.compile(r'LIN\s+X\s*[-\d.]+\s+Y\s*[-\d.]+\s+Z\s*([-\d.]+)')
            
            for line in lines:
                z_match = z_pattern.search(line)
                if z_match:
                    z_height = float(z_match.group(1))
                    
                    # Add original line
                    modified_lines.append(line)
                    
                    # Add custom parameters if they exist for this Z height
                    if z_height in self.custom_z_params:
                        for param_name, param_value in self.custom_z_params[z_height].items():
                            modified_lines.append(f'{param_name}={param_value}\n')
                else:
                    modified_lines.append(line)
                    
            return modified_lines
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to calculate new parameters: {str(e)}")
            return []

    def modify_file(self):
        try:
            if not self.input_file:
                return
                
            for key, entry in self.entries.items():
                try:
                    # Special handling for ACT_DRIVE
                    if "Drive" in key:
                        value = entry.get()
                        if value not in ['TRUE', 'FALSE']:
                            tk.messagebox.showerror("Error", f"Invalid value for {key}. Must be TRUE or FALSE")
                            return
                        self.params[key] = value
                    else:
                        # Convert other parameters to float
                        self.params[key] = float(entry.get())
                except ValueError:
                    tk.messagebox.showerror("Error", f"Invalid value for {key}")
                    return
            
            # Get input file name without extension
            input_name = os.path.splitext(os.path.basename(self.input_file))[0]
            default_output = f"{input_name}_modified.src"
            
            # Open file save dialog
            output_file = filedialog.asksaveasfilename(
                defaultextension=".src",
                initialfile=default_output,
                filetypes=[("SRC files", "*.src"), ("All files", "*.*")]
            )
            
            if not output_file:  # User cancelled
                return
                
            # Create changelog name based on selected output file
            changelog_base = os.path.splitext(output_file)[0]
            default_changelog = f"{changelog_base}_changelog.txt"
                    
            modified_lines = self.calculate_new_params()
            
            # Create changelog entry
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            changelog_entry = f"\n=== {timestamp} ===\n"
            changelog_entry += f"Modified file: {self.input_file}\n"
            changelog_entry += f"Output file: {output_file}\n"
            changelog_entry += "Parameter changes:\n"
            
            # Add parameter changes to changelog
            for key, value in self.params.items():
                changelog_entry += f"- {key}: {value}\n"
            
            # Add custom Z height parameters to changelog
            if self.custom_z_params:
                changelog_entry += "\nCustom Z height parameters:\n"
                for z, params in self.custom_z_params.items():
                    changelog_entry += f"Z = {z}:\n"
                    for param_type, value in params.items():
                        changelog_entry += f"  - {param_type}: {value}\n"
            
            # Write modified file
            with open(output_file, 'w', encoding='utf-8') as file:
                file.writelines(modified_lines)
                
            # Append to changelog
            with open(default_changelog, 'a', encoding='utf-8') as log:
                log.write(changelog_entry)
            
            # Update menu item state
            self.file_menu.entryconfig("Save", state='disabled')
            
            tk.messagebox.showinfo("Success", f"File saved as {output_file}\nChangelog updated in {default_changelog}")
                
        except Exception as e:
            tk.messagebox.showerror("Error", f"Failed to save file: {str(e)}")

    def delete_parameter(self, key, line_number):
        try:
            # Save current state before deletion
            self.save_state()
            
            # Get the line containing the parameter we want to delete
            content_lines = self.original_content.splitlines()
            param_line = content_lines[line_number - 1]
            
            # Identify parameter type
            param_type = None
            if 'TOOL_RPM=' in param_line:
                param_type = 'TOOL_RPM'
            elif '$VEL.CP=' in param_line:
                param_type = '$VEL.CP'
            elif 'LAYER_COOLING=' in param_line:
                param_type = 'LAYER_COOLING'
            elif 'ACT_DRIVE=' in param_line:
                param_type = 'ACT_DRIVE'

            # Search backwards for position marker
            for i in range(line_number - 2, -1, -1):
                current_line = content_lines[i]
                
                # Found Z height marker
                z_match = re.search(r'LIN.*?Z\s*([-\d.]+)', current_line)
                if z_match:
                    z_value = float(z_match.group(1))
                    if z_value in self.custom_z_params and param_type in self.custom_z_params[z_value]:
                        del self.custom_z_params[z_value][param_type]
                        if not self.custom_z_params[z_value]:
                            del self.custom_z_params[z_value]
                    break
                    
                # Found print progress marker
                progress_match = re.search(r'PRINT_PROGRESS=(\d+)', current_line)
                if progress_match:
                    progress_value = int(progress_match.group(1))
                    if progress_value in self.print_progress_params and param_type in self.print_progress_params[progress_value]:
                        del self.print_progress_params[progress_value][param_type]
                        if not self.print_progress_params[progress_value]:
                            del self.print_progress_params[progress_value]
                    break

            # Remove the line from content
            del content_lines[line_number - 1]
            
            # Remove from tracking dictionaries
            if key in self.params:
                del self.params[key]
            if key in self.param_line_numbers:
                del self.param_line_numbers[key]

            # Remove from param_groups
            for group_name, group_keys in self.param_groups.items():
                if key in group_keys:
                    group_keys.remove(key)
                    if group_name in self.header_labels:
                        header_label = self.header_labels[group_name]
                        header_label.config(text=f"{group_name} ({len(group_keys)} occurrences)")
                    break

            # Update line numbers
            for param_key, line_num in list(self.param_line_numbers.items()):
                if line_num > line_number:
                    self.param_line_numbers[param_key] = line_num - 1
                    if param_key in self.params:
                        value = self.params[param_key]
                        new_key = param_key.replace(f"Line {line_num}", f"Line {line_num - 1}")
                        del self.params[param_key]
                        self.params[new_key] = value
                        for group_keys in self.param_groups.values():
                            if param_key in group_keys:
                                group_keys.remove(param_key)
                                group_keys.append(new_key)

            # Update content and UI
            self.original_content = '\n'.join(content_lines) + '\n'
            self.update_preview()
            self.extract_params_from_file()
            self.create_param_entries()
            
            # Enable save button
            self.save_button.config(state=tk.NORMAL)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete parameter: {str(e)}")

    def save_state(self):
        """Save current state for undo"""
        state = {
            'params': self.params.copy(),
            'param_line_numbers': self.param_line_numbers.copy(), 
            'param_groups': {k: v[:] for k, v in self.param_groups.items()},
            'original_content': self.original_content,
            'custom_z_params': {k: v.copy() for k, v in self.custom_z_params.items()},
            'print_progress_params': {k: v.copy() for k, v in self.print_progress_params.items()},
            'z_param_frames': self.z_param_frames.copy(),
            'print_progress_frames': self.print_progress_frames.copy(),
            'header_labels': {k: v.cget("text") for k, v in self.header_labels.items()}  # Save header labels
        }
        self.undo_state = state
        self.undo_button.config(state=tk.NORMAL)
        self.redo_state = None  # Clear redo state when new state is saved
        self.redo_button.config(state=tk.DISABLED)

    def undo_last_action(self):
        try:
            if not self.undo_state:
                self.undo_button.config(state=tk.DISABLED)
                return
            
            # Save current state to redo
            current_state = {
                'params': self.params.copy(),
                'param_line_numbers': self.param_line_numbers.copy(),
                'param_groups': {k: v[:] for k, v in self.param_groups.items()},
                'original_content': self.original_content,
                'custom_z_params': {k: v.copy() for k, v in self.custom_z_params.items()},
                'print_progress_params': {k: v.copy() for k, v in self.print_progress_params.items()},
                'z_param_frames': self.z_param_frames.copy(),
                'print_progress_frames': self.print_progress_frames.copy(),
                'header_labels': {k: v.cget("text") for k, v in self.header_labels.items()}
            }
            self.redo_state = current_state
            
            # Restore undo state
            state = self.undo_state
            self.params = state['params']
            self.param_line_numbers = state['param_line_numbers']
            self.param_groups = state['param_groups']
            self.original_content = state['original_content']
            self.custom_z_params = state['custom_z_params']
            self.print_progress_params = state['print_progress_params']
            self.z_param_frames = state['z_param_frames']
            self.print_progress_frames = state['print_progress_frames']
            
            # Restore header labels
            for k, text in state['header_labels'].items():
                if k in self.header_labels:
                    self.header_labels[k].config(text=text)
            
            # Update UI
            self.update_preview()
            self.create_param_entries()
            
            # Update button states
            self.undo_state = None
            self.undo_button.config(state=tk.DISABLED)
            self.redo_button.config(state=tk.NORMAL)
            
            # Enable save button
            self.save_button.config(state=tk.NORMAL)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to undo: {str(e)}")

    def redo_last_action(self):
        try:
            if not self.redo_state:
                self.redo_button.config(state=tk.DISABLED)
                return
                
            # Save current state to undo
            current_state = {
                'params': self.params.copy(),
                'param_line_numbers': self.param_line_numbers.copy(),
                'param_groups': {k: v[:] for k, v in self.param_groups.items()},
                'original_content': self.original_content,
                'custom_z_params': {k: v.copy() for k, v in self.custom_z_params.items()},
                'print_progress_params': {k: v.copy() for k, v in self.print_progress_params.items()},
                'z_param_frames': self.z_param_frames.copy(),
                'print_progress_frames': self.print_progress_frames.copy(),
                'header_labels': {k: v.cget("text") for k, v in self.header_labels.items()}
            }
            self.undo_state = current_state
            
            # Restore redo state
            state = self.redo_state
            self.params = state['params']
            self.param_line_numbers = state['param_line_numbers']
            self.param_groups = state['param_groups']
            self.original_content = state['original_content']
            self.custom_z_params = state['custom_z_params']
            self.print_progress_params = state['print_progress_params']
            self.z_param_frames = state['z_param_frames']
            self.print_progress_frames = state['print_progress_frames']
            
            # Restore header labels
            for k, text in state['header_labels'].items():
                if k in self.header_labels:
                    self.header_labels[k].config(text=text)
            
            # Update UI
            self.update_preview()
            self.create_param_entries()
            
            # Update button states
            self.redo_state = None
            self.redo_button.config(state=tk.DISABLED)
            self.undo_button.config(state=tk.NORMAL)
            
            # Enable save button
            self.save_button.config(state=tk.NORMAL)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to redo: {str(e)}")

    def create_undo_redo_buttons(self):
        """Create undo and redo buttons with custom styling"""
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=5)
        
        # Undo button with counterclockwise arrow (↺)
        self.undo_button = tk.Button(button_frame, text="↺ Undo", 
                                   command=self.undo_last_action,
                                   bg='#FFE4B5',  # Light orange
                                   activebackground='#FFDEAD', # Slightly darker orange on hover
                                   relief='raised',
                                   state=tk.DISABLED)
        self.undo_button.pack(side=tk.LEFT, padx=5)
        # Redo button with clockwise arrow (↻)
        self.redo_button = tk.Button(button_frame, text="↻ Redo",
                                   command=self.redo_last_action,
                                   bg='#D8BFD8',  # Using a different light purple color (Thistle)
                                   activebackground='#E6E6FA',  # Original light purple on hover
                                   relief='raised',
                                   state=tk.DISABLED)
        self.redo_button.pack(side=tk.LEFT, padx=5)

    def jump_to_z_height(self, z_height):
        try:
            content = self.preview_text.get("1.0", tk.END).splitlines()
            z_pattern = re.compile(r'LIN\s+X\s*[-\d.]+\s+Y\s*[-\d.]+\s+Z\s*([-\d.]+)')
            
            for i, line in enumerate(content, 1):
                match = z_pattern.search(line)
                if match and abs(float(match.group(1)) - z_height) < 0.0001:  # Use small epsilon for float comparison
                    self.jump_to_line(i)
                    break
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to jump to Z height: {str(e)}")

    def add_parameter_at_start(self):
        """Open a dialog to add parameters."""
        try:
            # Create a dialog window
            dialog = tk.Toplevel(self.root)
            dialog.title("Add Parameter at Part Start")
            dialog.geometry("800x500")  # Set the size of the dialog

            # Create main container frame
            main_frame = tk.Frame(dialog)
            main_frame.pack(fill='both', expand=True, padx=5, pady=5)

            # Create a frame for the parts list that takes up 2/3 of the width
            parts_frame = tk.Frame(main_frame)
            parts_frame.pack(side='left', fill='both', expand=True)

            # Create canvas and scrollbar for parts list
            canvas = tk.Canvas(parts_frame)
            scrollbar = tk.Scrollbar(parts_frame, orient="vertical", command=canvas.yview)
            scrollable_frame = tk.Frame(canvas)

            # Configure the canvas
            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )

            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)

            # Pack canvas and scrollbar
            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")

            # Find all part start locations
            content_lines = self.original_content.splitlines()
            part_start_lines = []
            
            for i in range(len(content_lines)-1):
                if ("LIN" in content_lines[i] and "Z" in content_lines[i] and "C_DIS" in content_lines[i] and
                    "TRIGGER WHEN DISTANCE=0 DELAY=0 DO ACT_DRIVE=TRUE" in content_lines[i+1]):
                    part_start_lines.append((i + 2, content_lines[i]))

            # Create compact entries for each part
            self.part_start_entries = []
            if not part_start_lines:
                tk.Label(scrollable_frame, text="No part start locations found.").pack()
            else:
                # Create a row frame for every 4 parts
                for i in range(0, len(part_start_lines), 4):
                    row_frame = tk.Frame(scrollable_frame)
                    row_frame.pack(fill='x', pady=2)

                    # Add up to 4 parts in this row
                    for j in range(4):
                        if i + j < len(part_start_lines):
                            part_num = i + j + 1
                            line_num, line = part_start_lines[i + j]
                            
                            # Create individual part frame
                            part_frame = tk.Frame(row_frame, relief='groove', borderwidth=1)
                            part_frame.pack(side='left', fill='both', expand=True, padx=2)

                            # Part number and jump button in one row
                            header_frame = tk.Frame(part_frame)
                            header_frame.pack(fill='x')

                            tk.Label(header_frame, text=f"Part {part_num}", font=('Arial', 9, 'bold')).pack(side='left')
                            tk.Label(header_frame, text=f" (Line {line_num-1})", font=('Arial', 8)).pack(side='left')
                            
                            jump_btn = tk.Button(header_frame, text="→", command=lambda ln=line_num-1: self.jump_to_line(ln),
                                               bg='light blue', width=2, height=1)
                            jump_btn.pack(side='right')

                            # Create separate parameter entries
                            params_frame = tk.Frame(part_frame)
                            params_frame.pack(fill='x', pady=1)

                            # TOOL_RPM parameter
                            tool_rpm_frame = tk.Frame(params_frame)
                            tool_rpm_frame.pack(fill='x', pady=1)
                            tk.Label(tool_rpm_frame, text="TOOL_RPM:").pack(side='left')
                            tool_rpm_entry = tk.Entry(tool_rpm_frame, width=10)
                            tool_rpm_entry.pack(side='left')

                            # $VEL.CP parameter
                            vel_cp_frame = tk.Frame(params_frame)
                            vel_cp_frame.pack(fill='x', pady=1)
                            tk.Label(vel_cp_frame, text="$VEL.CP:").pack(side='left')
                            vel_cp_entry = tk.Entry(vel_cp_frame, width=10)
                            vel_cp_entry.pack(side='left')

                            # Layer-cooling parameter
                            layer_cooling_frame = tk.Frame(params_frame)
                            layer_cooling_frame.pack(fill='x', pady=1)
                            tk.Label(layer_cooling_frame, text="Layer-cooling:").pack(side='left')
                            layer_cooling_entry = tk.Entry(layer_cooling_frame, width=10)
                            layer_cooling_entry.pack(side='left')

                            # ACT_DRIVE parameter
                            act_drive_frame = tk.Frame(params_frame)
                            act_drive_frame.pack(fill='x', pady=1)
                            tk.Label(act_drive_frame, text="ACT_DRIVE:").pack(side='left')
                            act_drive_combo = ttk.Combobox(act_drive_frame, values=['TRUE', 'FALSE'], width=8, state='readonly')
                            act_drive_combo.pack(side='left')

                            # Store references
                            self.part_start_entries.append((line_num, {
                                'TOOL_RPM': tool_rpm_entry,
                                '$VEL.CP': vel_cp_entry,
                                'Layer-cooling': layer_cooling_entry,
                                'ACT_DRIVE': act_drive_combo
                            }))

                    # Add a separator after each row
                    ttk.Separator(scrollable_frame, orient='horizontal').pack(fill='x', pady=2)

            def add_parameters():
                # Save current state before modifications
                self.save_state()
                
                content_lines = self.original_content.splitlines()
                modified = False
                lines_added = 0  # Keep track of how many lines we've added
                
                # Process each part's parameters
                for line_num, entries in self.part_start_entries:
                    params_to_add = []
                    params_to_replace = {}  # Track parameters that need replacement
                    adjusted_line_num = line_num + lines_added
                    
                    # Scan existing parameters for this part
                    current_params = {'TOOL_RPM': None, '$VEL.CP': None, 'LAYER_COOLING': None, 'ACT_DRIVE': None}
                    search_range = 10  # Look at next few lines for existing parameters
                    for i in range(adjusted_line_num, min(adjusted_line_num + search_range, len(content_lines))):
                        line = content_lines[i]
                        if 'TOOL_RPM=' in line:
                            current_params['TOOL_RPM'] = i
                        elif '$VEL.CP=' in line:
                            current_params['$VEL.CP'] = i
                        elif 'LAYER_COOLING=' in line:
                            current_params['LAYER_COOLING'] = i
                        elif 'ACT_DRIVE=' in line:
                            current_params['ACT_DRIVE'] = i
                    
                    # Check TOOL_RPM
                    tool_rpm = entries['TOOL_RPM'].get().strip()
                    if tool_rpm:
                        try:
                            rpm_value = float(tool_rpm)
                            if rpm_value > 139.8:
                                messagebox.showerror("Error", f"Maximum value for TOOL_RPM is 139.8 (Part at line {line_num})")
                                return
                            param_line = f"TRIGGER WHEN DISTANCE=0 DELAY=0 DO TOOL_RPM={rpm_value}"
                            if current_params['TOOL_RPM'] is not None:
                                params_to_replace[current_params['TOOL_RPM']] = param_line
                            else:
                                params_to_add.append(param_line)
                        except ValueError:
                            messagebox.showerror("Error", f"Invalid TOOL_RPM value at part line {line_num}")
                            return

                    # Check $VEL.CP
                    vel_cp = entries['$VEL.CP'].get().strip()
                    if vel_cp:
                        try:
                            vel_value = float(vel_cp)
                            if vel_value > 2:
                                messagebox.showerror("Error", f"Maximum value for $VEL.CP is 2 (Part at line {line_num})")
                                return
                            if vel_value > 0.5:
                                if not messagebox.askyesno("Warning", 
                                    f"Values above 0.5 for $VEL.CP could be dangerous (Part at line {line_num}).\n\n" +
                                    "Do you wish to continue with this value?"):
                                    return
                            param_line = f"$VEL.CP={vel_value}"
                            if current_params['$VEL.CP'] is not None:
                                params_to_replace[current_params['$VEL.CP']] = param_line
                            else:
                                params_to_add.append(param_line)
                        except ValueError:
                            messagebox.showerror("Error", f"Invalid $VEL.CP value at part line {line_num}")
                            return

                    # Check LAYER_COOLING
                    layer_cooling = entries['Layer-cooling'].get().strip()
                    if layer_cooling:
                        try:
                            cool_value = int(layer_cooling)
                            if cool_value > 200:
                                messagebox.showerror("Error", f"Maximum value for LAYER_COOLING is 200 (Part at line {line_num})")
                                return
                            param_line = f"LAYER_COOLING={cool_value}"
                            if current_params['LAYER_COOLING'] is not None:
                                params_to_replace[current_params['LAYER_COOLING']] = param_line
                            else:
                                params_to_add.append(param_line)
                        except ValueError:
                            messagebox.showerror("Error", f"Invalid LAYER_COOLING value at part line {line_num}")
                            return

                    # Check ACT_DRIVE
                    act_drive = entries['ACT_DRIVE'].get()
                    if act_drive:
                        if act_drive not in ['TRUE', 'FALSE']:
                            messagebox.showerror("Error", f"ACT_DRIVE must be TRUE or FALSE (Part at line {line_num})")
                            return
                        param_line = f"TRIGGER WHEN DISTANCE=0 DELAY=0 DO ACT_DRIVE={act_drive}"
                        if current_params['ACT_DRIVE'] is not None:
                            params_to_replace[current_params['ACT_DRIVE']] = param_line
                        else:
                            params_to_add.append(param_line)

                    # Replace existing parameters
                    for line_idx, new_line in params_to_replace.items():
                        content_lines[line_idx] = new_line
                        modified = True

                    # Add new parameters
                    if params_to_add:
                        for i, param in enumerate(params_to_add):
                            content_lines.insert(adjusted_line_num + i, param)
                        lines_added += len(params_to_add)
                        modified = True

                if modified:
                    # Update content and UI
                    self.original_content = '\n'.join(content_lines) + '\n'
                    self.update_preview()
                    if self.extract_params_from_file():
                        self.create_param_entries()
                    self.save_button.config(state=tk.NORMAL)
                else:
                    messagebox.showinfo("Info", "No parameters were added. Please enter at least one parameter value.")

            # Add confirm button at the bottom
            confirm_button = tk.Button(dialog, text="Confirm", command=add_parameters)
            confirm_button.pack(side='bottom', pady=5)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to add parameter at part start: {str(e)}")
    # #             act_drive_value = 1.0 if value.lower() == 'true' else 0.0
    # #             self.z_act_drive_points[line_num - 1] = act_drive_value  # Update the corresponding point
    # #             print(f"Updated ACT_DRIVE for line {line_num}: {act_drive_value}")

    def add_parameter_at_z(self):
        """Open a dialog to add parameters at Z heights."""
        try:
            # Create a dialog window
            dialog = tk.Toplevel(self.root)
            dialog.title("Add Parameter at Z Height")
            dialog.geometry("800x500")

            # Create main container frame
            main_frame = tk.Frame(dialog)
            main_frame.pack(fill='both', expand=True, padx=5, pady=5)

            # Create Z height input frame at the top
            z_input_frame = tk.Frame(main_frame)
            z_input_frame.pack(fill='x', pady=5)
            
            tk.Label(z_input_frame, text="Enter Z Height:").pack(side='left')
            z_height_entry = tk.Entry(z_input_frame, width=10)
            z_height_entry.pack(side='left', padx=5)

            # Create frame for the Z instances list
            instances_frame = tk.Frame(main_frame)
            instances_frame.pack(fill='both', expand=True)

            # Create canvas and scrollbar
            canvas = tk.Canvas(instances_frame)
            scrollbar = tk.Scrollbar(instances_frame, orient="vertical", command=canvas.yview)
            scrollable_frame = tk.Frame(canvas)

            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )

            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)

            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")

            self.z_entries = []  # Store entries for each Z instance

            def update_z_instances(*args):
                # Clear existing frames
                for widget in scrollable_frame.winfo_children():
                    widget.destroy()
                self.z_entries.clear()

                try:
                    z_height = float(z_height_entry.get())
                    content_lines = self.original_content.splitlines()
                    z_instances = []
                    current_part = 1
                    i = 0

                    while i < len(content_lines)-1:
                        # Check for part start pattern
                        if ("LIN" in content_lines[i] and "Z" in content_lines[i] and "C_DIS" in content_lines[i] and
                            i+1 < len(content_lines) and
                            "TRIGGER WHEN DISTANCE=0 DELAY=0 DO ACT_DRIVE=TRUE" in content_lines[i+1]):
                            current_part += 1
                            i += 2
                            continue

                        # Check for Z value
                        z_match = re.search(r'LIN.*?Z\s*([-\d.]+)', content_lines[i])
                        if z_match and abs(float(z_match.group(1)) - z_height) < 0.0001:
                            z_instances.append((current_part, i + 1, content_lines[i]))
                        i += 1

                    # Create a row frame for every 4 instances
                    for i in range(0, len(z_instances), 4):
                        row_frame = tk.Frame(scrollable_frame)
                        row_frame.pack(fill='x', pady=2)

                        # Add up to 4 instances in this row
                        for j in range(4):
                            if i + j < len(z_instances):
                                part_num, line_num, line = z_instances[i + j]
                                
                                # Create individual instance frame
                                instance_frame = tk.Frame(row_frame, relief='groove', borderwidth=1)
                                instance_frame.pack(side='left', fill='both', expand=True, padx=2)

                                # Instance header and jump button
                                header_frame = tk.Frame(instance_frame)
                                header_frame.pack(fill='x')

                                tk.Label(header_frame, text=f"Part {part_num}", font=('Arial', 9, 'bold')).pack(side='left')
                                tk.Label(header_frame, text=f" (Line {line_num})", font=('Arial', 8)).pack(side='left')
                                
                                jump_btn = tk.Button(header_frame, text="→", command=lambda ln=line_num: self.jump_to_line(ln),
                                                   bg='light blue', width=2, height=1)
                                jump_btn.pack(side='right')

                                # Parameter entries
                                params_frame = tk.Frame(instance_frame)
                                params_frame.pack(fill='x', pady=1)

                                # TOOL_RPM parameter
                                tool_rpm_frame = tk.Frame(params_frame)
                                tool_rpm_frame.pack(fill='x', pady=1)
                                tk.Label(tool_rpm_frame, text="TOOL_RPM:").pack(side='left')
                                tool_rpm_entry = tk.Entry(tool_rpm_frame, width=10)
                                tool_rpm_entry.pack(side='left')

                                # $VEL.CP parameter
                                vel_cp_frame = tk.Frame(params_frame)
                                vel_cp_frame.pack(fill='x', pady=1)
                                tk.Label(vel_cp_frame, text="$VEL.CP:").pack(side='left')
                                vel_cp_entry = tk.Entry(vel_cp_frame, width=10)
                                vel_cp_entry.pack(side='left')

                                # Layer-cooling parameter
                                layer_cooling_frame = tk.Frame(params_frame)
                                layer_cooling_frame.pack(fill='x', pady=1)
                                tk.Label(layer_cooling_frame, text="Layer-cooling:").pack(side='left')
                                layer_cooling_entry = tk.Entry(layer_cooling_frame, width=10)
                                layer_cooling_entry.pack(side='left')

                                # ACT_DRIVE parameter
                                act_drive_frame = tk.Frame(params_frame)
                                act_drive_frame.pack(fill='x', pady=1)
                                tk.Label(act_drive_frame, text="ACT_DRIVE:").pack(side='left')
                                act_drive_combo = ttk.Combobox(act_drive_frame, values=['TRUE', 'FALSE'], width=8, state='readonly')
                                act_drive_combo.pack(side='left')

                                # Store references
                                self.z_entries.append((line_num, {
                                    'TOOL_RPM': tool_rpm_entry,
                                    '$VEL.CP': vel_cp_entry,
                                    'Layer-cooling': layer_cooling_entry,
                                    'ACT_DRIVE': act_drive_combo
                                }))

                        # Add a separator after each row
                        ttk.Separator(scrollable_frame, orient='horizontal').pack(fill='x', pady=2)

                    if not z_instances:
                        tk.Label(scrollable_frame, text=f"No instances found for Z = {z_height}").pack()

                except ValueError:
                    tk.Label(scrollable_frame, text="Please enter a valid Z height").pack()

            # Bind the update function to the Z height entry
            z_height_entry.bind('<Return>', update_z_instances)
            update_button = tk.Button(z_input_frame, text="Update", command=update_z_instances)
            update_button.pack(side='left', padx=5)

            def add_parameters():
                # Save current state before modifications
                self.save_state()
                
                content_lines = self.original_content.splitlines()
                modified = False
                lines_added = 0

                # Sort entries by line number in descending order to avoid line number shifting
                sorted_entries = sorted(self.z_entries, key=lambda x: x[0], reverse=True)

                for line_num, entries in sorted_entries:
                    params_to_add = []
                    params_to_replace = {}
                    
                    # Scan existing parameters
                    current_params = {'TOOL_RPM': None, '$VEL.CP': None, 'LAYER_COOLING': None, 'ACT_DRIVE': None}
                    search_range = 10
                    for i in range(line_num, min(line_num + search_range, len(content_lines))):
                        line = content_lines[i]
                        if 'TOOL_RPM=' in line:
                            current_params['TOOL_RPM'] = i
                        elif '$VEL.CP=' in line:
                            current_params['$VEL.CP'] = i
                        elif 'LAYER_COOLING=' in line:
                            current_params['LAYER_COOLING'] = i
                        elif 'ACT_DRIVE=' in line:
                            current_params['ACT_DRIVE'] = i

                    # Process parameters
                    # TOOL_RPM
                    tool_rpm = entries['TOOL_RPM'].get().strip()
                    if tool_rpm:
                        try:
                            rpm_value = float(tool_rpm)
                            if rpm_value > 139.8:
                                messagebox.showerror("Error", f"Maximum value for TOOL_RPM is 139.8 (Line {line_num})")
                                return
                            param_line = f"TRIGGER WHEN DISTANCE=0 DELAY=0 DO TOOL_RPM={rpm_value}"
                            if current_params['TOOL_RPM'] is not None:
                                params_to_replace[current_params['TOOL_RPM']] = param_line
                            else:
                                params_to_add.append(param_line)
                        except ValueError:
                            messagebox.showerror("Error", f"Invalid TOOL_RPM value at line {line_num}")
                            return

                    # $VEL.CP
                    vel_cp = entries['$VEL.CP'].get().strip()
                    if vel_cp:
                        try:
                            vel_value = float(vel_cp)
                            if vel_value > 2:
                                messagebox.showerror("Error", f"Maximum value for $VEL.CP is 2 (Line {line_num})")
                                return
                            if vel_value > 0.5:
                                if not messagebox.askyesno("Warning", 
                                    f"Values above 0.5 for $VEL.CP could be dangerous (Line {line_num}).\n\n" +
                                    "Do you wish to continue with this value?"):
                                    return
                            param_line = f"$VEL.CP={vel_value}"
                            if current_params['$VEL.CP'] is not None:
                                params_to_replace[current_params['$VEL.CP']] = param_line
                            else:
                                params_to_add.append(param_line)
                        except ValueError:
                            messagebox.showerror("Error", f"Invalid $VEL.CP value at line {line_num}")
                            return

                    # Layer-cooling
                    layer_cooling = entries['Layer-cooling'].get().strip()
                    if layer_cooling:
                        try:
                            cool_value = int(layer_cooling)
                            if cool_value > 200:
                                messagebox.showerror("Error", f"Maximum value for LAYER_COOLING is 200 (Line {line_num})")
                                return
                            param_line = f"LAYER_COOLING={cool_value}"
                            if current_params['LAYER_COOLING'] is not None:
                                params_to_replace[current_params['LAYER_COOLING']] = param_line
                            else:
                                params_to_add.append(param_line)
                        except ValueError:
                            messagebox.showerror("Error", f"Invalid LAYER_COOLING value at line {line_num}")
                            return

                    # ACT_DRIVE
                    act_drive = entries['ACT_DRIVE'].get()
                    if act_drive:
                        if act_drive not in ['TRUE', 'FALSE']:
                            messagebox.showerror("Error", f"ACT_DRIVE must be TRUE or FALSE (Line {line_num})")
                            return
                        param_line = f"TRIGGER WHEN DISTANCE=0 DELAY=0 DO ACT_DRIVE={act_drive}"
                        if current_params['ACT_DRIVE'] is not None:
                            params_to_replace[current_params['ACT_DRIVE']] = param_line
                        else:
                            params_to_add.append(param_line)

                    # Replace existing parameters
                    for line_idx, new_line in params_to_replace.items():
                        content_lines[line_idx] = new_line
                        modified = True

                    # Add new parameters
                    if params_to_add:
                        # Insert parameters in reverse order to maintain correct line positions
                        for param in reversed(params_to_add):
                            content_lines.insert(line_num, param)
                            modified = True

                if modified:
                    # Update content and UI
                    self.original_content = '\n'.join(content_lines) + '\n'
                    self.update_preview()
                    if self.extract_params_from_file():
                        self.create_param_entries()
                    self.save_button.config(state=tk.NORMAL)
                else:
                    messagebox.showinfo("Info", "No parameters were added. Please enter at least one parameter value.")

            # Add confirm button at the bottom
            confirm_button = tk.Button(dialog, text="Confirm", command=add_parameters)
            confirm_button.pack(side='bottom', pady=5)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to add parameter at Z height: {str(e)}")

    def create_z_parameter_dialog(self, z_height):
        """Create a dialog showing all instances of the specified Z height."""
        try:
            # Create dialog window
            dialog = tk.Toplevel(self.root)
            dialog.title(f"Add Parameters at Z = {z_height}")
            dialog.geometry("800x500")

            # Create main container frame with canvas and scrollbar
            main_frame = tk.Frame(dialog)
            main_frame.pack(fill='both', expand=True, padx=5, pady=5)

            canvas = tk.Canvas(main_frame)
            scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
            scrollable_frame = tk.Frame(canvas)

            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )

            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)

            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")

            # Find all instances of this Z height
            content_lines = self.original_content.splitlines()
            z_instances = []
            current_part = 1  # Start from part 1
            seen_z_values = set()

            for i, line in enumerate(content_lines):
                z_match = re.search(r'LIN.*?Z\s*([-\d.]+)', line)
                if z_match:
                    current_z = float(z_match.group(1))
                    # If we see a Z value we've seen before, it's a new part
                    if current_z in seen_z_values:
                        current_part += 1
                        seen_z_values.clear()
                    seen_z_values.add(current_z)
                    
                    if abs(current_z - z_height) < 0.0001:
                        z_instances.append((current_part, i + 1, line))

            # Create frames for each instance (4 per row)
            for i in range(0, len(z_instances), 4):
                row_frame = tk.Frame(scrollable_frame)
                row_frame.pack(fill='x', pady=2)

                # Add up to 4 instances in this row
                for j in range(4):
                    if i + j < len(z_instances):
                        part_num, line_num, line = z_instances[i + j]
                        
                        # Create individual instance frame
                        instance_frame = tk.Frame(row_frame, relief='groove', borderwidth=1)
                        instance_frame.pack(side='left', fill='both', expand=True, padx=2)

                        # Instance header and jump button
                        header_frame = tk.Frame(instance_frame)
                        header_frame.pack(fill='x')

                        tk.Label(header_frame, text=f"Part {part_num}", font=('Arial', 9, 'bold')).pack(side='left')
                        tk.Label(header_frame, text=f" (Line {line_num})", font=('Arial', 8)).pack(side='left')
                        
                        jump_btn = tk.Button(header_frame, text="→", 
                                           command=lambda ln=line_num: self.jump_to_line(ln),
                                           bg='light blue', width=2, height=1)
                        jump_btn.pack(side='right')

                        # Parameter entries
                        params_frame = tk.Frame(instance_frame)
                        params_frame.pack(fill='x', pady=1)

                        # Create parameter entries
                        param_entries = {}

                        # TOOL_RPM parameter
                        tool_rpm_frame = tk.Frame(params_frame)
                        tool_rpm_frame.pack(fill='x', pady=1)
                        tk.Label(tool_rpm_frame, text="TOOL_RPM:").pack(side='left')
                        tool_rpm_entry = tk.Entry(tool_rpm_frame, width=10)
                        tool_rpm_entry.pack(side='left')
                        param_entries['TOOL_RPM'] = tool_rpm_entry

                        # $VEL.CP parameter
                        vel_cp_frame = tk.Frame(params_frame)
                        vel_cp_frame.pack(fill='x', pady=1)
                        tk.Label(vel_cp_frame, text="$VEL.CP:").pack(side='left')
                        vel_cp_entry = tk.Entry(vel_cp_frame, width=10)
                        vel_cp_entry.pack(side='left')
                        param_entries['$VEL.CP'] = vel_cp_entry

                        # Layer-cooling parameter
                        layer_cooling_frame = tk.Frame(params_frame)
                        layer_cooling_frame.pack(fill='x', pady=1)
                        tk.Label(layer_cooling_frame, text="Layer-cooling:").pack(side='left')
                        layer_cooling_entry = tk.Entry(layer_cooling_frame, width=10)
                        layer_cooling_entry.pack(side='left')
                        param_entries['Layer-cooling'] = layer_cooling_entry

                        # ACT_DRIVE parameter
                        act_drive_frame = tk.Frame(params_frame)
                        act_drive_frame.pack(fill='x', pady=1)
                        tk.Label(act_drive_frame, text="ACT_DRIVE:").pack(side='left')
                        act_drive_combo = ttk.Combobox(act_drive_frame, values=['TRUE', 'FALSE'], 
                                                     width=8, state='readonly')
                        act_drive_combo.pack(side='left')
                        param_entries['ACT_DRIVE'] = act_drive_combo

                        if not hasattr(self, 'z_entries'):
                            self.z_entries = []
                        self.z_entries.append((line_num, param_entries))

                # Add a separator after each row
                ttk.Separator(scrollable_frame, orient='horizontal').pack(fill='x', pady=2)

            def add_parameters():
                self.save_state()
                content_lines = self.original_content.splitlines()
                modified = False
                lines_added = 0

                for line_num, entries in self.z_entries:
                    params_to_add = []
                    params_to_replace = {}
                    adjusted_line_num = line_num + lines_added

                    # Scan existing parameters
                    current_params = {'TOOL_RPM': None, '$VEL.CP': None, 'LAYER_COOLING': None, 'ACT_DRIVE': None}
                    search_range = 10
                    for i in range(adjusted_line_num, min(adjusted_line_num + search_range, len(content_lines))):
                        line = content_lines[i]
                        for param in current_params:
                            if f"{param}=" in line:
                                current_params[param] = i

                    # Process each parameter
                    for param_name, entry in entries.items():
                        value = entry.get().strip()
                        if value:
                            try:
                                if param_name == 'TOOL_RPM':
                                    rpm_value = float(value)
                                    if rpm_value > 139.8:
                                        messagebox.showerror("Error", f"Maximum value for TOOL_RPM is 139.8 (Line {line_num})")
                                        return
                                    param_line = f"TRIGGER WHEN DISTANCE=0 DELAY=0 DO TOOL_RPM={rpm_value}"
                                elif param_name == '$VEL.CP':
                                    vel_value = float(value)
                                    if vel_value > 2:
                                        messagebox.showerror("Error", f"Maximum value for $VEL.CP is 2 (Line {line_num})")
                                        return
                                    if vel_value > 0.5 and not messagebox.askyesno("Warning", 
                                        f"Values above 0.5 for $VEL.CP could be dangerous (Line {line_num}).\n\n" +
                                        "Do you wish to continue with this value?"):
                                        return
                                    param_line = f"$VEL.CP={vel_value}"
                                elif param_name == 'Layer-cooling':
                                    cool_value = int(value)
                                    if cool_value > 200:
                                        messagebox.showerror("Error", f"Maximum value for LAYER_COOLING is 200 (Line {line_num})")
                                        return
                                    param_line = f"LAYER_COOLING={cool_value}"
                                elif param_name == 'ACT_DRIVE':
                                    param_line = f"TRIGGER WHEN DISTANCE=0 DELAY=0 DO ACT_DRIVE={value}"

                                if current_params[param_name] is not None:
                                    params_to_replace[current_params[param_name]] = param_line
                                else:
                                    params_to_add.append(param_line)
                                    
                            except ValueError:
                                messagebox.showerror("Error", f"Invalid value for {param_name} at line {line_num}")
                                return

                    # Replace existing parameters
                    for line_idx, new_line in params_to_replace.items():
                        content_lines[line_idx] = new_line
                        modified = True

                    # Add new parameters
                    if params_to_add:
                        for i, param in enumerate(params_to_add):
                            content_lines.insert(adjusted_line_num + i, param)
                        lines_added += len(params_to_add)
                        modified = True

                if modified:
                    self.original_content = '\n'.join(content_lines) + '\n'
                    self.update_preview()
                    if self.extract_params_from_file():
                        self.create_param_entries()
                    self.save_button.config(state=tk.NORMAL)
                    dialog.destroy()
                else:
                    messagebox.showinfo("Info", "No parameters were added. Please enter at least one parameter value.")

            confirm_button = tk.Button(dialog, text="Confirm", command=add_parameters)
            confirm_button.pack(side='bottom', pady=5)

            return dialog

        except Exception as e:
            messagebox.showerror("Error", f"Failed to create Z parameter dialog: {str(e)}")
            return None

    # def validate_and_add(self, value_var, frame_name, dialog):
    #     try:
    #         if frame_name == "Z Height":
    #             z_height = float(value_var.get())
    #             max_z = self.get_max_z_value()
    #             if z_height < 0 or z_height > max_z:
    #                 messagebox.showerror("Error", f"Z height must be between 0 and {max_z}.")
    #                 return
                
    #             z_dialog = self.create_z_parameter_dialog(z_height)
    #             if z_dialog:
    #                 dialog.destroy()
                
    #             self.update_line_numbers()
    #             self.update_preview()
            
    #     except ValueError:
    #         messagebox.showerror("Error", "Please enter a valid number")
    #      except Exception as e:
    #          messagebox.showerror("Error", f"Failed to update ACT_DRIVE parameter: {str(e)}")

    # # Create the button for adding ACT_DRIVE parameters
        


if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = SRCModifierApp(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start application: {str(e)}")
