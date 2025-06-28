from transformers import pipeline

# Load summarization model
summarizer = pipeline("summarization")

# Ask user for input
print("Enter the paragraph to summarize (press Enter twice to finish):")

# Take multi-line input
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

text = " ".join(lines)

# Summarize the input text
summary = summarizer(text, max_length=120, min_length=30, do_sample=False)

# Print the summary
print("\n📝 Summary:\n", summary[0]['summary_text'])

