# main_gui.py

import tkinter as tk
from tkinter import ttk, messagebox
import serial_handler # Assuming serial_handler.py is in the same directory
import challenge_response_logic # Assuming challenge_response_logic.py is in the same directory

class RS232TesterGUI:
    def __init__(self, master):
        self.master = master
        master.title("RS232 Challenge-Response Tester")
        master.geometry("600x500")

        self.serial_handler = serial_handler.SerialHandler()
        self.challenge_logic = challenge_response_logic

        # --- Connection Frame ---
        conn_frame = ttk.LabelFrame(master, text="Connection Settings", padding="10")
        conn_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        ttk.Label(conn_frame, text="Serial Port:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.port_var = tk.StringVar()
        self.port_combobox = ttk.Combobox(conn_frame, textvariable=self.port_var, width=15)
        self.port_combobox.grid(row=0, column=1, padx=5, pady=5)
        self.update_port_list()

        ttk.Label(conn_frame, text="Baud Rate:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.baudrate_var = tk.StringVar(value="9600")
        self.baudrate_entry = ttk.Entry(conn_frame, textvariable=self.baudrate_var, width=10)
        self.baudrate_entry.grid(row=0, column=3, padx=5, pady=5)

        self.connect_button = ttk.Button(conn_frame, text="Connect", command=self.connect_serial)
        self.connect_button.grid(row=0, column=4, padx=5, pady=5)

        self.disconnect_button = ttk.Button(conn_frame, text="Disconnect", command=self.disconnect_serial, state=tk.DISABLED)
        self.disconnect_button.grid(row=0, column=5, padx=5, pady=5)

        # --- Command Frame ---
        cmd_frame = ttk.LabelFrame(master, text="Challenge-Response", padding="10")
        cmd_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        ttk.Label(cmd_frame, text="Command (5 bytes):").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.command_entry = ttk.Entry(cmd_frame, width=20)
        self.command_entry.grid(row=0, column=1, padx=5, pady=5)
        # Default command bytes (hex string for example)
        self.command_entry.insert(0, "0102030405") 

        self.send_cmd_button = ttk.Button(cmd_frame, text="Send Command", command=self.send_command, state=tk.DISABLED)
        self.send_cmd_button.grid(row=0, column=2, padx=5, pady=5)

        # --- Data Display Frame ---
        data_frame = ttk.LabelFrame(master, text="Data Exchange", padding="10")
        data_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        master.grid_rowconfigure(2, weight=1)
        master.grid_columnconfigure(0, weight=1)

        # Received Data
        ttk.Label(data_frame, text="Received Data (16 bytes):").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.received_data_text = tk.Text(data_frame, height=5, width=50, wrap=tk.WORD)
        self.received_data_text.grid(row=1, column=0, padx=5, pady=5)
        self.received_data_text.config(state=tk.DISABLED) # Make read-only

        # Calculated Answer
        ttk.Label(data_frame, text="Calculated Answer:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.calculated_answer_text = tk.Text(data_frame, height=2, width=50, wrap=tk.WORD)
        self.calculated_answer_text.grid(row=3, column=0, padx=5, pady=5)
        self.calculated_answer_text.config(state=tk.DISABLED) # Make read-only

    def update_port_list(self):
        """Updates the list of available serial ports in the combobox."""
        available_ports = self.serial_handler.list_available_ports()
        self.port_combobox['values'] = available_ports
        if available_ports:
            self.port_var.set(available_ports[0]) # Select the first port by default
        else:
            self.port_var.set("") # No ports available

    def connect_serial(self):
        """Handles the connect button action."""
        port = self.port_var.get()
        baudrate_str = self.baudrate_var.get()

        if not port:
            messagebox.showerror("Connection Error", "Please select a serial port.")
            return

        try:
            baudrate = int(baudrate_str)
        except ValueError:
            messagebox.showerror("Connection Error", "Invalid baud rate. Please enter a number.")
            return

        if self.serial_handler.connect(port, baudrate):
            messagebox.showinfo("Connection Status", f"Successfully connected to {port}.")
            self.connect_button.config(state=tk.DISABLED)
            self.disconnect_button.config(state=tk.NORMAL)
            self.send_cmd_button.config(state=tk.NORMAL)
            self.port_combobox.config(state=tk.DISABLED)
            self.baudrate_entry.config(state=tk.DISABLED)
        else:
            messagebox.showerror("Connection Error", f"Failed to connect to {port}.")

    def disconnect_serial(self):
        """Handles the disconnect button action."""
        self.serial_handler.disconnect()
        messagebox.showinfo("Connection Status", "Disconnected.")
        self.connect_button.config(state=tk.NORMAL)
        self.disconnect_button.config(state=tk.DISABLED)
        self.send_cmd_button.config(state=tk.DISABLED)
        self.port_combobox.config(state=tk.NORMAL)
        self.baudrate_entry.config(state=tk.NORMAL)
        self.clear_data_display()

    def send_command(self):
        """Handles sending a command."""
        command_str = self.command_entry.get()
        try:
            # Expecting hex string input
            command_bytes = bytes.fromhex(command_str)
            if len(command_bytes) != 5:
                messagebox.showerror("Input Error", "Command must be 5 bytes long (enter as hex string, e.g., 0102030405).")
                return

            if self.serial_handler.send_data(command_bytes):
                # After sending, immediately try to receive the 16-byte response
                response = self.serial_handler.receive_data(16)
                if response:
                    self.display_received_data(response)
                    # Process the received data to calculate the answer
                    try:
                        challenge_data = self.challenge_logic.decode_challenge_data(response)
                        answer_bytes = self.challenge_logic.calculate_xor_offset_answer(challenge_data)
                        final_protocol_message = self.challenge_logic.assemble_response_protocol(answer_bytes)
                        self.display_calculated_answer(final_protocol_message)
                        # Optionally send the answer back to the device
                        # self.serial_handler.send_data(final_protocol_message)
                    except ValueError as e:
                        messagebox.showerror("Processing Error", str(e))
                else:
                    self.display_received_data(None) # Indicate no data or timeout

        except ValueError:
            messagebox.showerror("Input Error", "Invalid hex string for command. Please enter a valid 5-byte hex string.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def display_received_data(self, data):
        """Displays received data in the text area."""
        self.received_data_text.config(state=tk.NORMAL)
        self.received_data_text.delete(1.0, tk.END)
        if data:
            self.received_data_text.insert(tk.END, data.hex())
        else:
            self.received_data_text.insert(tk.END, "No data received or timeout.")
        self.received_data_text.config(state=tk.DISABLED)

    def display_calculated_answer(self, data):
        """Displays calculated answer in the text area."""
        self.calculated_answer_text.config(state=tk.NORMAL)
        self.calculated_answer_text.delete(1.0, tk.END)
        if data:
            self.calculated_answer_text.insert(tk.END, data.hex())
        else:
            self.calculated_answer_text.insert(tk.END, "Could not calculate answer.")
        self.calculated_answer_text.config(state=tk.DISABLED)

    def clear_data_display(self):
        """Clears the data display areas."""
        self.display_received_data(None)
        self.display_calculated_answer(None)

if __name__ == "__main__":
    root = tk.Tk()
    gui = RS232TesterGUI(root)
    root.mainloop()
