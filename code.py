from tkinter import *
import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.root.geometry("400x300")
        self.contacts = self.load_contacts()
        
        self.create_widgets()
    
    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Contact Manager",font=("Arial", 24))
        self.title_label.place(relx=0.5, rely=0.1, anchor='center')
        
        self.add_button = tk.Button(self.root, text="Add Contact", font=("Arial", 14),fg='#9370DB', command=self.add_contact)
        self.add_button.place(relx=0.5, rely=0.3,height=30, width=150, anchor='center')
        
        self.view_button = tk.Button(self.root, text="View Contacts", font=("Arial", 14), fg='#9370DB',command=self.view_contacts)
        self.view_button.place(relx=0.5, rely=0.5, height=30, width=150,anchor='center')
        
        self.edit_button = tk.Button(self.root, text="Edit Contact", font=("Arial", 14), fg='#9370DB',command=self.edit_contact)
        self.edit_button.place(relx=0.5, rely=0.7,height=30, width=150, anchor='center')
    
        self.delete_button = tk.Button(self.root, text="Delete Contact", font=("Arial", 14),fg='#9370DB', command=self.delete_contact)
        self.delete_button.place(relx=0.5, rely=0.9,height=30, width=150, anchor='center')
    
    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name:")
        if not name:
            return
        
        phone = simpledialog.askstring("Input", "Enter contact phone number:")
        email = simpledialog.askstring("Input", "Enter contact email address:")
        
        self.contacts[name] = {"phone": phone, "email": email}
        self.save_contacts()
        messagebox.showinfo("Success", f"Contact {name} added successfully!")
    
    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts found!")
            return
        
        contacts_str = "\n".join([f"{name}: {info['phone']} ({info['email']})" for name, info in self.contacts.items()])
        messagebox.showinfo("Contact List", contacts_str)
    
    def edit_contact(self):
        name = simpledialog.askstring("Input", "Enter the name of the contact to edit:")
        if not name or name not in self.contacts:
            messagebox.showerror("Error", "Contact not found!")
            return
        
        new_phone = simpledialog.askstring("Input", "Enter new phone number:", initialvalue=self.contacts[name]["phone"])
        new_email = simpledialog.askstring("Input", "Enter new email address:", initialvalue=self.contacts[name]["email"])
        
        self.contacts[name] = {"phone": new_phone, "email": new_email}
        self.save_contacts()
        messagebox.showinfo("Success", f"Contact {name} updated successfully!")
    
    def delete_contact(self):
        name = simpledialog.askstring("Input", "Enter the name of the contact to delete:")
        if not name or name not in self.contacts:
            messagebox.showerror("Error", "Contact not found!")
            return
        
        del self.contacts[name]
        self.save_contacts()
        messagebox.showinfo("Success", f"Contact {name} deleted successfully!")
    
    def load_contacts(self):
        if not os.path.exists("contacts.json"):
            return {}
        
        with open("contacts.json", "r") as file:
            return json.load(file)
    
    def save_contacts(self):
        with open("contacts.json", "w") as file:
            json.dump(self.contacts, file, indent=4)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
