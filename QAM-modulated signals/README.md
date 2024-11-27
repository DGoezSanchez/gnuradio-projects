# GNU Radio QAM Modulation and Visualization

This Notebook defines a GNU Radio application that generates and visualizes QAM-modulated signals using a custom block and a graphical interface. Below are the main components and their functionalities:

---

## **Custom Modulation Block (`modulation`)**
The `modulation` block is derived from `gr.sync_block` and is responsible for generating QAM-modulated signals based on the specified modulation order (`M`).

- **Initialization (`__init__`)**  
  - Sets up the block with default parameters.  
  - Accepts `M` as the modulation order (e.g., 4 for QPSK, 16 for 16-QAM).  

- **`symbols_QAM` Method**  
  - Creates a QAM symbol constellation based on the modulation order.  
  - Symbols are distributed in quadrants, scaled appropriately for each `M`.  

- **`work` Method**  
  - Generates a QAM-modulated signal:  
    - Uses the `SP` function to map random bit sequences to QAM symbols.  
    - Produces a time-domain signal by repeating the mapped symbols.  
    - Writes the modulated signal to the output buffer for further processing or visualization.  

---

## **Top Block (`Radio_ML_Synthetic`)**
This is the main GNU Radio flowgraph that incorporates the custom modulation block, signal processing, and graphical visualization.

- **GUI and Signal Processing**  
  - **`qtgui.sink_c`**: Displays the signal's frequency spectrum, time-domain waveform, and constellation.  
  - **`blocks.throttle`**: Limits the data rate to match the sample rate, preventing excessive CPU usage.  

- **Signal Flow**  
  - The custom `modulation` block generates the QAM-modulated signal.  
  - The signal is passed through the throttle block and visualized in real-time using the Qt GUI.  

- **Setup**  
  - The application is built using PyQt5, enabling an interactive GUI for signal visualization.  
  - Adjustable parameters, such as the sample rate, can be modified to suit the application.  

---

## **Execution and Visualization**
The script initializes the flowgraph and starts the GUI, enabling real-time signal visualization.

- **Modulation Order (`M`)**  
  - Adjust the modulation order in the `modulation` block to explore different schemes (e.g., QPSK, 16-QAM, 256-QAM).  

- **Running the Script**  
  - Execute the script to start the flowgraph and display the GUI.  
  - The GUI provides plots for:  
    - Frequency spectrum  
    - Time-domain signal  
    - Constellation diagram  

---

## **Example Use Case**
1. **Generate a 256-QAM Signal**  
   Set `modulation(M=256)` to produce a 256-QAM signal.  

2. **Visualize the Signal**  
   View the frequency spectrum, time-domain waveform, and constellation in the GUI.  

3. **Modify Parameters**  
   Experiment with different modulation orders and observe their impact on the signal characteristics.

---

This application is ideal for exploring QAM modulation, testing signal processing techniques, and visualizing results in real-time using GNU Radio.
