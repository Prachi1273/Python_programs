import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog, Label, Entry, Button, Frame
import os
import pandas as pd
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled

# --- SUMY Summarizer Imports ---
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

# --- Global Settings ---
SUMMARY_SENTENCES = 15 # Number of sentences in the final summary
EXCEL_FILE = "youtube_notes.xlsx"

# ==============================================================================
# Step 2 & 3: Get and Process YouTube Transcript
# ==============================================================================
def get_video_id(url):
    """Extracts the YouTube video ID from a URL."""
    # Handles standard, shortened, and embed URLs
    parsed_url = urlparse(url)
    if parsed_url.hostname == 'youtu.be':
        return parsed_url.path[1:]
    if parsed_url.hostname in ('www.youtube.com', 'youtube.com'):
        if parsed_url.path == '/watch':
            p = parse_qs(parsed_url.query)
            return p.get('v', [None])[0]
        if parsed_url.path.startswith('/embed/'):
            return parsed_url.path.split('/embed/')[1]
        if parsed_url.path.startswith('/v/'):
            return parsed_url.path.split('/v/')[1]
    return None

def get_transcript(video_id):
    """
    Fetches and cleans the transcript for a given video ID.
    Returns the full transcript text or an error message.
    """
    try:
        # Fetch transcript using the API
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Clean and join the transcript text
        # The API returns a list of dictionaries, each with a 'text' key
        full_transcript = " ".join([d['text'] for d in transcript_list])
        return full_transcript
    except NoTranscriptFound:
        return "Error: No transcript found for this video. It might be disabled or not have subtitles."
    except TranscriptsDisabled:
        return "Error: Transcripts are disabled for this video."
    except Exception as e:
        return f"Error: An unexpected error occurred: {e}"

# ==============================================================================
# Step 4: Summarize the Transcript
# ==============================================================================
def summarize_text(text):
    """
    Summarizes the given text using Sumy's TextRank algorithm.
    """
    if text.startswith("Error:"):
        return text # Pass through error messages

    # Initialize the parser and tokenizer for Sumy
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    
    # Initialize the TextRank summarizer
    summarizer = TextRankSummarizer()
    
    # Generate the summary
    summary = summarizer(parser.document, SUMMARY_SENTENCES)
    
    # Join the summarized sentences into a single string
    summarized_notes = " ".join([str(sentence) for sentence in summary])
    return summarized_notes

# ==============================================================================
# Step 5: Save the Notes
# ==============================================================================
def save_notes_to_files(video_title, video_url, notes):
    """Saves the generated notes to a .txt file and an Excel file."""
    # Sanitize title to create a valid filename
    safe_filename = "".join([c for c in video_title if c.isalpha() or c.isdigit() or c==' ']).rstrip()
    txt_filename = f"{safe_filename}.txt"

    # --- Save to .txt file ---
    try:
        with open(txt_filename, 'w', encoding='utf-8') as f:
            f.write(f"Title: {video_title}\n")
            f.write(f"URL: {video_url}\n\n")
            f.write("--- NOTES ---\n")
            f.write(notes)
        txt_save_status = f"Notes saved to {txt_filename}"
    except Exception as e:
        txt_save_status = f"Error saving .txt file: {e}"

    # --- Save to Excel file using pandas ---
    try:
        new_data = pd.DataFrame({
            'Title': [video_title],
            'URL': [video_url],
            'Notes': [notes]
        })

        if os.path.exists(EXCEL_FILE):
            # Append to existing file without writing header
            with pd.ExcelWriter(EXCEL_FILE, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
                # Find the last row to append after
                existing_df = pd.read_excel(EXCEL_FILE)
                startrow = len(existing_df) + 1
                new_data.to_excel(writer, index=False, header=False, startrow=startrow)

        else:
            # Create a new file with header
            new_data.to_excel(EXCEL_FILE, index=False)
            
        excel_save_status = f"Notes also appended to {EXCEL_FILE}"
    except Exception as e:
        excel_save_status = f"Error saving to Excel: {e}"
        
    return txt_save_status, excel_save_status

# ==============================================================================
# Step 6: GUI using Tkinter
# ==============================================================================
class App:
    def __init__(self, root):
        self.root = root
        root.title("YouTube Notes Generator")
        root.geometry("800x600")

        # --- Frames for layout ---
        top_frame = Frame(root, padx=10, pady=10)
        top_frame.pack(fill='x')

        middle_frame = Frame(root, padx=10, pady=5)
        middle_frame.pack(fill='both', expand=True)

        # --- Widgets ---
        Label(top_frame, text="Enter YouTube Video URL:", font=("Arial", 12)).pack(side='left')
        
        self.url_entry = Entry(top_frame, width=60, font=("Arial", 12))
        self.url_entry.pack(side='left', fill='x', expand=True, padx=5)

        self.generate_button = Button(top_frame, text="Generate Notes", command=self.generate_notes_action, font=("Arial", 11, "bold"))
        self.generate_button.pack(side='left')

        self.results_text = scrolledtext.ScrolledText(middle_frame, wrap=tk.WORD, font=("Arial", 11), state='disabled')
        self.results_text.pack(fill='both', expand=True)
    
    def generate_notes_action(self):
        """The main function triggered by the button click."""
        video_url = self.url_entry.get()
        if not video_url:
            messagebox.showerror("Error", "Please enter a YouTube URL.")
            return

        self.update_results("Processing... Please wait.")
        self.root.update_idletasks() # Force UI update

        # --- Main Logic Flow ---
        try:
            video_id = get_video_id(video_url)
            if not video_id:
                messagebox.showerror("Error", "Invalid YouTube URL. Could not extract video ID.")
                self.update_results("Failed. Please check the URL and try again.")
                return

            # Step 2 & 3: Get and clean transcript
            transcript = get_transcript(video_id)
            if transcript.startswith("Error:"):
                messagebox.showerror("Transcript Error", transcript)
                self.update_results(transcript)
                return

            # Step 4: Summarize
            notes = summarize_text(transcript)

            # A placeholder for video title - in a real app, you might use an API like pytube to get this
            # For simplicity, we'll use the video ID as the title.
            video_title = f"Video Notes for ID {video_id}"

            # Step 5: Save notes
            txt_status, excel_status = save_notes_to_files(video_title, video_url, notes)

            # Display results in the GUI
            final_display_text = (
                f"--- NOTES FOR: {video_title} ---\n\n"
                f"{notes}\n\n"
                f"----------------------------------------\n"
                f"Status:\n- {txt_status}\n- {excel_status}"
            )
            self.update_results(final_display_text)
            messagebox.showinfo("Success", "Notes generated and saved successfully!")

        except Exception as e:
            error_message = f"An unexpected error occurred: {e}"
            messagebox.showerror("Critical Error", error_message)
            self.update_results(error_message)

    def update_results(self, text):
        """Updates the text in the results box."""
        self.results_text.config(state='normal')
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, text)
        self.results_text.config(state='disabled')


if __name__ == "__main__":
    main_window = tk.Tk()
    app = App(main_window)
    main_window.mainloop()
