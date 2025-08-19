# craete a file name input.txt

file = open("input.txt", "w")

# To write into the file:
file.write(
    "Hello Instructor"
    "I hope your day went well?"
    "Can i meet you?"
    "Hello world!"
    "I am a student at PLP"
)

# To read content:
file = open("input.txt", "r")
data = file.read()
print(data)

#count the number of words in the line
word_count = len(data.split())
print("Word Count:", word_count)

#convert all text
upper_text = data.upper()
print("Uppercase Text:\n", upper_text)

#Write the processed text and the word count to a new file called output.txt.
 
file = open("output.txt", "w")
file.write("Processed Text:\n")
file.write(upper_text + "\n\n")
file.write(f"Word Count: {word_count}\n")

#Print a success message once the new file is created.
try:
    file = open("output.txt", "r")
    output_data = file.read()
    print("\nOutput File Content:\n", output_data)
    print("\n✅ Success: output.txt has been created and processed.")
except FileNotFoundError:
    print("File Not Found")
    