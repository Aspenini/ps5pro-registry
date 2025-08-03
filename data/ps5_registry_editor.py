
import json
import tkinter as tk
from tkinter import filedialog, messagebox

class PS5RegistryEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("PS5 Pro Registry JSON Editor")
        self.root.geometry("400x500")
        self.fields = {}
        self.json_path = ""

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="1. Click to load entries.json", font=('Arial', 12)).pack(pady=10)
        tk.Button(self.root, text="Select JSON File", command=self.load_json).pack()

        self.form_frame = tk.Frame(self.root)
        self.form_frame.pack(pady=20)

        for field in ["number", "name", "discord", "psn", "twitter", "notes"]:
            row = tk.Frame(self.form_frame)
            row.pack(fill='x', pady=5)
            label = tk.Label(row, text=field.capitalize(), width=10, anchor='w')
            label.pack(side='left')
            entry = tk.Entry(row)
            entry.pack(fill='x', expand=True)
            self.fields[field] = entry

        tk.Button(self.root, text="Done", command=self.save_entry, bg="green", fg="white").pack(pady=20)

    def load_json(self):
        path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if path:
            self.json_path = path
            messagebox.showinfo("Loaded", f"Loaded JSON from:\n{path}")

    def save_entry(self):
        if not self.json_path:
            messagebox.showerror("No JSON Selected", "Please select a JSON file first.")
            return

        try:
            with open(self.json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read JSON: {e}")
            return

        new_entry = {
            "number": self.fields["number"].get(),
            "name": self.fields["name"].get() or "Anonymous",
            "notes": self.fields["notes"].get() or "",
            "socials": {
                "discord": self.fields["discord"].get() or "",
                "psn": self.fields["psn"].get() or "",
                "twitter": self.fields["twitter"].get() or ""
            }
        }

        if not new_entry["number"]:
            messagebox.showerror("Missing Field", "Console Number is required.")
            return

        data.append(new_entry)

        try:
            with open(self.json_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
            messagebox.showinfo("Success", "Entry added successfully!")
            self.root.quit()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to write JSON: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PS5RegistryEditor(root)
    root.mainloop()
